"""
What's My Grade, Really — encodes a teacher's exact grading rules (category weights,
dropped lowest scores) to calculate true current grade and the final exam score needed
to hit a target grade.

Usage: python grade_calculator.py sample_grades.json
"""

import json
import sys


def category_average(scores, drop_lowest=0):
    if not scores:
        return None
    scores_sorted = sorted(scores)
    kept = scores_sorted[drop_lowest:] if drop_lowest else scores_sorted
    if not kept:
        return None
    return sum(kept) / len(kept)


def current_grade(policy, scores):
    """Returns (overall_grade, breakdown, weight_of_missing_categories)."""
    breakdown = {}
    earned_weight = 0.0
    weighted_sum = 0.0
    missing_weight = 0.0

    for cat, rules in policy["categories"].items():
        weight = rules["weight"]
        avg = category_average(scores.get(cat, []), rules.get("drop_lowest", 0))
        if avg is None:
            missing_weight += weight
            breakdown[cat] = {"average": None, "weight": weight}
        else:
            weighted_sum += avg * weight
            earned_weight += weight
            breakdown[cat] = {"average": round(avg, 2), "weight": weight}

    # Grade so far, based only on completed categories (normalized)
    grade_so_far = (weighted_sum / earned_weight) if earned_weight > 0 else None
    return grade_so_far, breakdown, missing_weight, weighted_sum


def score_needed_for_target(policy, scores, target, missing_category):
    """Solve for the score needed in `missing_category` to reach `target` overall grade."""
    _, _, _, weighted_sum_known = current_grade(policy, scores)
    missing_weight = policy["categories"][missing_category]["weight"]
    # target = weighted_sum_known + needed_score * missing_weight  (weights sum to 1.0)
    needed = (target - weighted_sum_known) / missing_weight
    return needed


def main():
    if len(sys.argv) < 2:
        print("Usage: python grade_calculator.py <grades.json>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)

    policy = data["grading_policy"]
    scores = data["scores"]
    target = data.get("target_grade")

    total_weight = sum(c["weight"] for c in policy["categories"].values())
    if abs(total_weight - 1.0) > 0.001:
        print(f"WARNING: category weights sum to {total_weight}, not 1.0 — check the policy.")

    grade_so_far, breakdown, missing_weight, weighted_sum_known = current_grade(policy, scores)

    print("=" * 55)
    print("GRADE REPORT")
    print("=" * 55)
    for cat, info in breakdown.items():
        avg_str = f"{info['average']}" if info["average"] is not None else "not yet graded"
        print(f"  {cat:<15} avg: {avg_str:<15} weight: {info['weight']*100:.0f}%")

    if grade_so_far is not None:
        print(f"\nCurrent grade (completed categories only, normalized): {grade_so_far:.2f}")

    if target is not None and missing_weight > 0:
        missing_cats = [c for c, info in breakdown.items() if info["average"] is None]
        if len(missing_cats) == 1:
            needed = score_needed_for_target(policy, scores, target, missing_cats[0])
            print(f"\nTo reach a target overall grade of {target}, you need "
                  f"{needed:.1f} in '{missing_cats[0]}'.")
            if needed > 100:
                print("⚠ That score is above 100 — target grade is not achievable with this category alone.")
            elif needed < 0:
                print("✓ Target is already secured regardless of this category's score.")
        elif len(missing_cats) > 1:
            print(f"\nMultiple categories still missing ({missing_cats}); "
                  f"cannot solve for a single needed score.")
    print("=" * 55)


if __name__ == "__main__":
    main()
