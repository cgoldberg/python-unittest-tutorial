# Python Unit Testing Tutorial

This is an update to Doug Hellman's excellent PyMOTW article found here:

* [PyMOTW - unittest (2007)](http://www.doughellmann.com/PyMOTW/unittest/index.html)

The code and examples here have been updated by [Corey Goldberg](https://github.com/cgoldberg) to reflect Python 3.3.

further reading:

* [unittest - Python Standard Library 3.3 Documentation](http://docs.python.org/3.3/library/unittest.html)
  
----

## unittest - Automated testing framework

Python's `unittest` module, sometimes referred to as 'PyUnit', is based on the XUnit framework design by Kent Beck and Erich Gamma. The same pattern is repeated in many other languages, including C, Perl, Java, and Smalltalk. The framework implemented by `unittest` supports fixtures, test suites, and a test runner to enable automated testing for your code.

## Basic Test Structure

Tests, as defined by unittest, have two parts: code to manage test "fixtures", and the test itself. Individual tests are created by subclassing `TestCase` and overriding or adding appropriate methods. For example,

```python
import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```

In this case, the `SimplisticTest` has a single `test()` method, which would fail if True is ever False.

## Running Tests

The easiest way to run unittest tests is to include:

```python
if __name__ == '__main__':
    unittest.main()
```

at the bottom of each test file, then simply run the script directly from the command line:

```
$ python3 test_simple.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

This abbreviated output includes the amount of time the tests took, along with a status indicator for each test (the "." on the first line of output means that a test passed). For more detailed test results, include the `-v` option:

```
$ python3 test_simple.py -v

test (__main__.SimplisticTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Test Outcomes

Tests have 3 possible outcomes:

```
ok
```

The test passes.

```
FAIL
```

The test does not pass, and raises an `AssertionError` exception.

```
ERROR
```

The test raises an exception other than `AssertionError`.

There is no explicit way to cause a test to "pass", so a test's status depends on the presence (or absence) of an exception.

```python
import unittest

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()
```

When a test fails or generates an error, the traceback is included in the output.

```
$ python3 test_outcomes.py


EF.
======================================================================
ERROR: test_error (__main__.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_outcomes.py", line 13, in test_error
    raise RuntimeError('Test error!')
RuntimeError: Test error!

======================================================================
FAIL: test_fail (__main__.OutcomesTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_outcomes.py", line 9, in test_fail
    self.assertTrue(False)
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1, errors=1)
```

In the example above, `test_fail()` fails and the traceback shows the line with the failure code. It is up to the person reading the test output to look at the code to figure out the semantic meaning of the failed test, though. To make it easier to understand the nature of a test failure, the `assert*()` methods all accept an argument `msg`, which can be used to produce a more detailed error message.

```python
import unittest

class FailureMessageTest(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(False, 'failure message goes here')

if __name__ == '__main__':
    unittest.main()
```

```
$ python3 test_failwithmessage.py -v

test_fail (__main__.FailureMessageTest) ... FAIL

======================================================================
FAIL: test_fail (__main__.FailureMessageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_failwithmessage.py", line 6, in test_fail
    self.assertTrue(False, 'failure message goes here')
AssertionError: failure message goes here

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

## Asserting Truth

Most tests assert the truth of some condition. There are a few different ways to write truth-checking tests, depending on the perspective of the test author and the desired outcome of the code being tested. If the code produces a value which can be evaluated as true, the method `assertTrue()` should be used. If the code produces a false value, the method `assertFalse()` makes more sense.

```python
import unittest

class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
```

```
$ python3 test_truth.py -v

test_assert_false (__main__.TruthTest) ... ok
test_assert_true (__main__.TruthTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Assertion Methods

The `TestCase` class provides a number of methods to check for and report failures:

* [`TestCase` class](http://docs.python.org/3.3/library/unittest.html#unittest.TestCase)
* [`assert*` methods](http://docs.python.org/3.3/library/unittest.html#assert-methods)

### Common Assertions

<table>
  <tr><th>Method</th></tr>
  <tr><td><code>assertTrue(x, msg=None)</code></td></tr>
  <tr><td><code>assertFalse(x, msg=None)</code></td></tr>
  <tr><td><code>assertIsNone(x, msg=None)</code></td></tr>
  <tr><td><code>assertIsNotNone(x, msg=None)</code></td></tr>
  <tr><td><code>assertEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertNotEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertIs(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertIsNot(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertIn(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertNotIn(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertIsInstance(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertNotIsInstance(a, b, msg=None)</code></td></tr>
</table>

### Other Assertions

<table>
  <tr><th>Method</th></tr>
  <tr><td><code>assertAlmostEqual(a, b, places=7, msg=None, delta=None)</code></td></tr>
  <tr><td><code>assertNotAlmostEqual(a, b, places=7, msg=None, delta=None)</code></td></tr>
  <tr><td><code>assertGreater(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertGreaterEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertLess(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertLessEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertRegex(text, regexp, msg=None)</code></td></tr>
  <tr><td><code>assertNotRegex(text, regexp, msg=None)</code></td></tr>
  <tr><td><code>assertCountEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertMultiLineEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertSequenceEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertListEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertTupleEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertSetEqual(a, b, msg=None)</code></td></tr>
  <tr><td><code>assertDictEqual(a, b, msg=None)</code></td></tr>
</table>

### Failure Messages

These assertions are handy, since the values being compared appear in the failure message when a test fails.

```python
import unittest

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertNotEqual(1, 3-2)

    def testNotEqual(self):
        self.assertEqual(2, 3-2)

if __name__ == '__main__':
    unittest.main()
```

And when these tests are run:

```
$ python3 test_notequal.py -v

testEqual (__main__.InequalityTest) ... FAIL
testNotEqual (__main__.InequalityTest) ... FAIL

======================================================================
FAIL: test_equal (__main__.InequalityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_notequal.py", line 7, in test_equal
    self.assertNotEqual(1, 3-2)
AssertionError: 1 == 1

======================================================================
FAIL: test_not_equal (__main__.InequalityTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_notequal.py", line 10, in test_not_equal
    self.assertEqual(2, 3-2)
AssertionError: 2 != 1

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=2)
```

All the assert methods above accept a `msg` argument that, if specified, is used as the error message on failure.

## Testing for Exceptions (and Warnings)

The `TestCase` class provides methods to check for expected exceptions:

* [`TestCase` class](http://docs.python.org/3.3/library/unittest.html#unittest.TestCase)
* [`assert*` methods](http://docs.python.org/3.3/library/unittest.html#assert-methods)

<table>
  <tr><th>Method</th></tr>
  <tr><td><code>assertRaises(exception)</code></td></tr>
  <tr><td><code>assertRaisesRegex(exception, regexp)</code></td></tr>
  <tr><td><code>assertWarns(warn, fun, *args, **kwds)</code></td></tr>
  <tr><td><code>assertWarnsRegex(warn, fun, *args, **kwds)</code></td></tr>
</table>

As previously mentioned, if a test raises an exception other than `AssertionError` it is treated as an error. This is very useful for uncovering mistakes while you are modifying code which has existing test coverage. There are circumstances, however, in which you want the test to verify that some code does produce an exception. For example, if an invalid value is given to an attribute of an object. In such cases, `assertRaises()` makes the code more clear than trapping the exception yourself. Compare these two tests:

```python
import unittest

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))

class ExceptionTest(unittest.TestCase):

    def test_trap_locally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')

if __name__ == '__main__':
    unittest.main()
```

The results for both are the same, but the second test using `assertRaises()` is more succinct.

```
$ python3 test_exception.py -v

test_assert_raises (__main__.ExceptionTest) ... ok
test_trap_locally (__main__.ExceptionTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Test Fixtures

Fixtures are resources needed by a test. For example, if you are writing several tests for the same class, those tests all need an instance of that class to use for testing. Other test fixtures include database connections and temporary files (many people would argue that using external resources makes such tests not "unit" tests, but they are still tests and still useful). `TestCase` includes a special hook to configure and clean up any fixtures needed by your tests. To configure the fixtures, override `setUp()`. To clean up, override `tearDown()`.

```python
import unittest

class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('in test()')
        self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()
```

When this sample test is run, you can see the order of execution of the fixture and test methods:

```
$ python3 test_fixtures.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
In setUp()
in test()
In tearDown()
```

## Test Suites

The standard library documentation describes how to organize test suites manually. I generally do not use test suites directly, because I prefer to build the suites automatically (these are automated tests, after all). Automating the construction of test suites is especially useful for large code bases, in which related tests are not all in the same place. Tools such as nose make it easier to manage tests when they are spread over multiple files and directories.
