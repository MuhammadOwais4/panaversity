"""
Organize the Mess — finds duplicate files (by content hash) and large files in a folder,
and groups files by type. SAFETY FIRST: this script NEVER touches the original folder.

Workflow:
  1. python organize_mess.py --scan <folder>            -> shows a PLAN only, changes nothing
  2. Review the plan printed to the screen / plan.json
  3. python organize_mess.py --execute <folder> <out_dir> -> COPIES files into <out_dir>,
     organized by type, and writes duplicates into a separate "duplicates" subfolder.
     Originals are never deleted or modified.

Usage:
  python organize_mess.py --scan sample_messy_folder
  python organize_mess.py --execute sample_messy_folder organized_output
"""

import hashlib
import json
import os
import shutil
import sys
from collections import defaultdict

LARGE_FILE_THRESHOLD_BYTES = 50 * 1024  # 50 KB, small for demo purposes


def file_hash(path, chunk_size=8192):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def scan_folder(folder):
    by_hash = defaultdict(list)
    large_files = []
    by_type = defaultdict(list)

    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            digest = file_hash(path)
            by_hash[digest].append({"path": path, "name": name, "size": size})

            if size >= LARGE_FILE_THRESHOLD_BYTES:
                large_files.append({"path": path, "size": size})

            ext = os.path.splitext(name)[1].lower().lstrip(".") or "no_extension"
            by_type[ext].append(path)

    duplicates = {h: items for h, items in by_hash.items() if len(items) > 1}
    return duplicates, large_files, by_type


def build_plan(folder):
    duplicates, large_files, by_type = scan_folder(folder)

    plan = {"folder_scanned": folder, "actions": []}

    # Plan: keep first copy of each duplicate group, mark rest for "move to duplicates/"
    for digest, items in duplicates.items():
        keep = items[0]
        for dup in items[1:]:
            plan["actions"].append({
                "action": "copy_to_duplicates_folder",
                "source": dup["path"],
                "reason": f"identical content to '{keep['path']}'",
                "destination": f"duplicates/{os.path.basename(dup['path'])}",
            })

    # Plan: group remaining files by type into folders
    duplicate_paths = {item["path"] for items in duplicates.values() for item in items[1:]}
    for ext, paths in by_type.items():
        for p in paths:
            if p in duplicate_paths:
                continue
            plan["actions"].append({
                "action": "copy_to_type_folder",
                "source": p,
                "destination": f"by_type/{ext}/{os.path.basename(p)}",
            })

    plan["large_files_flagged"] = large_files
    return plan


def print_plan(plan):
    print("=" * 60)
    print("PROPOSED PLAN (nothing has been changed yet)")
    print("=" * 60)
    print(f"Folder scanned: {plan['folder_scanned']}\n")

    dup_actions = [a for a in plan["actions"] if a["action"] == "copy_to_duplicates_folder"]
    type_actions = [a for a in plan["actions"] if a["action"] == "copy_to_type_folder"]

    print(f"--- Duplicates found: {len(dup_actions)} file(s) ---")
    for a in dup_actions:
        print(f"  COPY  {a['source']}  ->  {a['destination']}   ({a['reason']})")

    print(f"\n--- Files to organize by type: {len(type_actions)} file(s) ---")
    for a in type_actions:
        print(f"  COPY  {a['source']}  ->  {a['destination']}")

    print(f"\n--- Large files flagged (>= {LARGE_FILE_THRESHOLD_BYTES // 1024} KB) ---")
    for lf in plan["large_files_flagged"]:
        print(f"  {lf['path']}  ({lf['size']/1024:.1f} KB)")

    print("\nOriginal files are NEVER modified or deleted by this script.")
    print("Run with --execute <folder> <out_dir> to copy files into an organized output folder.")
    print("=" * 60)


def execute_plan(plan, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for action in plan["actions"]:
        dest = os.path.join(out_dir, action["destination"])
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(action["source"], dest)
    print(f"Done. Organized copies written to '{out_dir}'. Originals in "
          f"'{plan['folder_scanned']}' were not touched.")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "--scan":
        folder = sys.argv[2]
        plan = build_plan(folder)
        print_plan(plan)
        with open("plan.json", "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2)
        print("\n(Full plan also saved to plan.json for review)")

    elif mode == "--execute":
        folder, out_dir = sys.argv[2], sys.argv[3]
        plan = build_plan(folder)
        print_plan(plan)
        confirm = input("\nType YES to execute this exact plan (copies only, originals untouched): ")
        if confirm.strip() == "YES":
            execute_plan(plan, out_dir)
        else:
            print("Cancelled. No files were changed.")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
