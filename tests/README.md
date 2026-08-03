# Testing of Happy
Since Happy is an AI, standard `unittest` cases that involve the same results every time are ineffective for this project. Happy's outputs will always be different. In order to work around this, ouputs and responses just need to be simply observed. If an error happens during a program or if Happy's output does not line up with what the output should generally be, then there is a problem. In the test case files, I put comments under the line in the programs that display Happy's output. These comments explain what Happy's output should be given the hardcoded input given to Happy per test file. I will also include information about each of the test files below and what they are testing.

# Test Files
`test_date.py`
- Tests Happy's ability to understand the current date and time. Happy is prompted to display the current date and time with given information about the current date and time. This information is courtesy of the `datetime` standard library.