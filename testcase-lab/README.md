# Automated Software Testing Quizzes

This folder contains the tested quiz work for the course.

## Today's progress

Set up a Python virtual environment, installed `pytest`, and used test-driven
checks to build and verify the quiz solutions. The BankAccount constructor was
corrected so accounts can start with an initial balance. Deposit and withdrawal
behavior was tested, and the Grades solution was checked at grade boundaries,
including invalid scores.

## Quizzes

- **BankAccount:** tests deposits and withdrawals, including balance updates.
- **Grades:** tests letter-grade boundaries and invalid scores.

## Run the tests

From the repository root, run:

```bash
python -m pytest testcase-lab -v
```

Sample output:

```text
10 passed
```

The tests passed using Python 3.12.5 and pytest 9.1.1.

## Healthy quiz history

Meaningful commits show the work developing step by step:

```text
quiz: set up solution and test files
quiz: add tests for basic cases
quiz: fix BankAccount constructor
quiz: test grade boundaries and invalid scores
quiz: add run instructions and sample output
```

## Finish today's work

From the repository root:

```bash
source .venv/bin/activate
python -m pytest testcase-lab -v
git status
git add testcase-lab/README.md
git commit -m "quiz: restore complete README documentation"
git push
```

