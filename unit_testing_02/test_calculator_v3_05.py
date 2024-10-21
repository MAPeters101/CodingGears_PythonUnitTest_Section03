"""
Topics:
    Test Suite >>>>>
        A test suite is a collection of test cases, test suites, or both.
        It is used to aggregate tests that should be executed together.
    Test runner >>>>>
        A test runner is a component which orchestrates the execution of tests and
        provides the outcome to the user.  The runner may use a graphical interface,
        a textual interface, or return a special value to indicate the results of
        executing the tests.
"""

# 1. Import unitttest & the required modules
import unittest
from unit_testing_02 import test_calculator_v3_01
from unit_testing_02 import test_calculator_v3_02
from unit_testing_02 import test_calculator_v3_03
from unit_testing_02 import test_calculator_v3_04

# 2. Create an instance of the TestLoader
loader = unittest.TestLoader()

# 3. Create an instance of the TestSuite
suite = unittest.TestSuite()

# 4. Add Test Cases to the TestSuite instance
# >> Load test cases from a module
suite.addTests(loader.loadTestsFromModule(test_calculator_v3_01))

# >> Load test cases from a class

# 5. Create an instance of the TextTestRunner
runner = unittest.TextTestRunner()

# 6. Run the TextTestRunner instance
runner.run(suite)



