# Automated Software Testing

Course code: 192-211

Name: AUNG MYAT PHONE

Student ID: 6705140057

Class Exercises

Bank exercise: bank.py and test_bank.py

Grades exercise: grades.py and test_grades.py

Dependent and independent tests: test_dependent.py and test_independent.py

# Assertion lab
The assert_lab folder demonstrates several types of pytest assertions.

test_collections.py tests list equality and contents, dictionary equality, and set operations.
test_floats.py tests floating-point values using pytest.approx and demonstrates floating-point precision behavior.
shopping.py implements a simple shopping cart that can add items, count items, and calculate their total price.
test_shopping.py tests that a new shopping cart is empty, starts with a zero total, and increases its item count when an item is added.


# Pytest Markers and Test Results

The pytest.ini file defines how pytest discovers tests, uses shorter traceback output, enables strict marker validation, and registers the following custom markers: smoke, slow, and regression.

The test files demonstrate several pytest features:

test_markers.py shows how tests can be grouped and selected using the smoke, slow, and regression markers.

test_skips.py contains examples of tests that are always skipped, as well as tests skipped depending on the Python version.

test_xfail.py demonstrates expected failures (XFAIL) and unexpected passes (XPASS).

test_conditional.py checks for /etc/hosts and skips the related test when the file is not available.

test_strict.py intentionally uses an unregistered marker to show how --strict-markers detects invalid markers during test collection.

From inside the assert_lab directory, the different marker groups can be tested in PowerShell using:

pytest -m smoke -v
pytest -m "smoke or regression" -v
pytest -m "not slow" -v

To test strict marker validation, run:

pytest test_strict.py

This command is expected to produce an error because nonexistent_marker has intentionally not been registered in pytest.ini. The error is therefore part of the demonstration and does not indicate an accidental problem with the test setup.

# Run the tests

From this folder, run:

python -m pytest -v

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through .gitignore.
