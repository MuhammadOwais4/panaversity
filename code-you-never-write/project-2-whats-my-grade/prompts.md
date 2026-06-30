# Prompts Used — Project 2: What's My Grade, Really

## Prompt 1 (initial)
Here are my scores by category and my teacher's grading policy (quizzes 15%, assignments 20%,
midterm 25%, final exam 40%, lowest quiz score dropped). Write a Python script that calculates
my current grade from a JSON file of scores and policy.

## Prompt 2 (refinement)
Also let me set a target overall grade and have the script tell me exactly what score I need on
the final exam to reach it. Handle the case where the final exam hasn't happened yet.

## Prompt 3 (fix)
The "current grade" number looks too low because it's including the not-graded final exam as a
zero. Fix it to normalize only across categories that have scores so far.
