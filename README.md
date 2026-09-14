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

Run the tests

From this folder, run:

python -m pytest -v

Project-only files are tracked in Git; the virtual environment and pytest/Python cache folders are excluded through .gitignore.
