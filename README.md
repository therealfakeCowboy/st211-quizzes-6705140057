# Automated Software Testing (AST)

This repository contains the Python exercises and pytest examples completed for
the Automated Software Testing course.

**Course code:** 192-211  
**Name:** AUNG MYAT PHONE  
**Student ID:** 6705140057

## Test case lab

The `testcase_lab` directory contains the original test case exercises:

- `bank.py` and `test_bank.py` cover deposits and withdrawals with a
  `BankAccount`.
- `grades.py` converts scores from 0 to 100 into letter grades and rejects
  invalid scores.
- `validators.py` checks email addresses and ages.
- `test_independent.py` creates a fresh account for every test.
- `test_dependent.py` demonstrates tests that share one account.
- `test_grades.py`, `test_positive.py`, and `test_negative.py` cover valid
  values, invalid values, and expected exceptions.

## Assertion lab

The `assert_lab` directory demonstrates common pytest assertions and test
outcomes.

- `test_collections.py` checks lists, dictionaries, and sets.
- `test_floats.py` uses `pytest.approx` to compare floating-point values.
- `shopping.py` implements a small shopping cart.
- `test_shopping.py` checks the cart's initial state and item count.
- `test_markers.py` demonstrates the `smoke`, `slow`, and `regression` markers.
- `test_skips.py` shows unconditional and conditional skips.
- `test_xfail.py` demonstrates expected failures (`XFAIL`) and unexpected
  passes (`XPASS`).
- `test_conditional.py` skips its hosts-file test when `/etc/hosts` is
  unavailable.
- `test_strict.py` intentionally uses an unregistered marker to demonstrate
  strict marker validation.

The marker groups can be selected from inside `assert_lab` with:

```powershell
pytest -m smoke -v
pytest -m "smoke or regression" -v
pytest -m "not slow" -v
```

To demonstrate strict marker validation, run:

```powershell
pytest test_strict.py
```

This command is expected to report an error because `nonexistent_marker` is
not registered in `pytest.ini`.

## Parametrization lab

The `param_lab` directory practices running one test with multiple inputs using
`pytest.mark.parametrize`. It includes examples from 12 and 19 October 2026.

- `mathutils.py` provides even-number checking and factorial calculation.
- `test_param.py` checks even and odd numbers.
- `test_factorial.py` tests factorials from 0 through 5.
- `discount.py` calculates percentage discounts and rejects percentages outside
  the range 0 to 100.
- `test_discount.py` covers several discount values, including 0% and 100%.
- `test_multi.py` combines two parametrized arguments to create six test cases.
- `test_default_ids.py` demonstrates pytest's automatically generated IDs.
- `test_param_ids.py` assigns readable IDs to individual test cases.
- `test_param_marks.py` applies IDs and an `xfail` marker to selected cases.

### Parameterized fixtures and external data

- `test_param_fixture.py` uses Chrome, Firefox, and Safari as fixture
  parameters, producing six test cases across two tests.
- `test_browsers.py` uses SQLite, PostgreSQL, and MySQL as fixture values.
  Despite its filename, it does not launch browsers or connect to databases.
- `test_cases.json` provides four input and expected-output pairs for uppercase
  conversion.
- `test_data_driven.py` loads the JSON data and creates one test per pair.
- `logins.csv` contains four login-validation scenarios.
- `validate.py` checks that usernames and passwords are not empty.
- `test_csv_driven.py` loads the CSV scenarios and checks each result.

Run the parametrization lab from its own directory because the JSON and CSV
loaders use paths relative to the current working directory:

```powershell
Set-Location param_lab
python -m pytest -v
```

The expected result is **51 passed, 1 xfailed**. The expected failure is the
deliberate square example in `test_param_marks.py`.

To view the generated test IDs without running the tests:

```powershell
python -m pytest --collect-only -q
```

## Running the tests

Run each lab from its own directory. For example:

```powershell
Set-Location testcase_lab
python -m pytest -v
```

The assertion lab includes the intentional strict-marker collection error
described above. The parametrization lab should be run from `param_lab`
because it reads external JSON and CSV files using relative paths.

Only project files are tracked in Git. The virtual environment and Python or
pytest cache folders are excluded through `.gitignore`.
