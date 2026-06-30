# Project 2 — What's My Grade, Really

## Problem
School grade apps don't know my actual teacher's grading rules — category weights, the lowest
quiz score being dropped, etc. This script encodes those exact rules to find my true current
grade and the score I need on the final exam.

## AI Tool Used
Claude (Anthropic)

## Initial Prompt
> "Here are my scores by category and my teacher's grading policy (quizzes 15%, assignments 20%,
> midterm 25%, final exam 40%, lowest quiz score dropped). Write a script to calculate my current
> grade."

## Improved Prompt
> "Also let me set a target overall grade and have the script tell me exactly what score I need
> on the final exam to reach it."

## How I Verified
I calculated the quizzes category by hand: scores were [85, 70, 90, 60, 95]; lowest (60) gets
dropped per policy, leaving [70, 85, 90, 95], average = 340 / 4 = **85.0**. The script reported
quizzes average as **85.0** — matched exactly. I also hand-verified the final weighted sum
(85×0.15 + 88.5×0.20 + 72×0.25 = 48.45) and the "score needed" formula, which matched the
script's output of 78.9.

## Result
- Current grade across completed categories (quizzes, assignments, midterm): **80.75**
- To reach a target overall grade of **80**, I need **78.9** on the final exam.

## What Worked / What Didn't
- Worked: encoding "drop lowest" as a simple sort-and-slice was correct and easy to verify.
- Didn't work initially: first version normalized the "current grade" using all weights
  (including the not-yet-graded final), which made the in-progress number misleadingly low.
  Asked the AI to normalize only over completed categories instead, which is more meaningful
  mid-term.

## Files
- `grade_calculator.py` — the script
- `sample_grades.json` — sample scores + grading policy (dummy values; real scores not committed)
