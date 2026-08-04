# About the Testing of Happy
Since Happy is an AI, standard `unittest` cases that involve the same results every time are mostly ineffective for this project. Happy's outputs will always be different. In order to work around this, ouputs and responses just need to be simply observed. If an error happens during a program or if Happy's output does not line up with what the output should generally be, then there is a problem. In the test case files, I put comments under the line in the programs that display Happy's output. These comments explain what Happy's output should be given the hardcoded input given to Happy per test file. I will also include information about each of the test files below and what they are testing.

# About the Test Files
`test_date.py`
- Tests Happy's ability to understand the current date and time. Happy is prompted to display the current date and time with given information about the current date and time. This information is courtesy of the `datetime` standard library.

`test_message_history.py`
- Simulates a conversation between the user and Happy about a Birthday Party, then uses `unittest` to ensure proper storage of message history of both sides. One test looks at the storage of all of the messages Happy sends, and the other test looks at the storage of all the messages the user sends.