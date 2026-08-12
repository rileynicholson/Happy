# About the Testing of Happy
Since Happy is an AI, standard `unittest` cases that involve the same results every time are mostly ineffective for this project when it comes to directly testing Happy. Happy's outputs will always be different. In order to work around this, ouputs and responses just need to be simply observed. If an error happens during a program or if Happy's output does not line up with what the output should generally be, then there is a problem. In most of the test case files that directly test Happy, I put comments under the line in the programs that display Happy's output. These comments explain what Happy's output should be given the hardcoded input given to Happy per test file. I will also include information about each of the test files and what they are testing down below.

# About the Test Files
`test_date.py`
- Tests Happy's ability to understand the current date and time. Happy is prompted to display the current date and time with given information about the current date and time. This information is courtesy of the `datetime` standard library.

`test_happy_detecting_user_progress_across_elapsed_time.py`
- Tests Happy's ability to understand elapsed time during a conversation. Happy is given a conversation that includes a goal the user wants to work towards. This simulated conversation is simulated to have been taken place on July 3rd, 2026, a while back. Happy is then prompted in present day about how the user has made progress with his goal. This test asks if Happy is able to see the progress the user has made, and how far the user has come.

`test_happy_referencing_message_history.py`
- Simulates the program gathering the conversation history from JSON files. Happy is prompted about information about the old, saved conversation. The `datetime` library is used in a formatted string to represent the dates used in this test.

`test_happy_referencing_multiple_message_history.py`
- This test acts as a simple stress test. The test simulates the program gathering multiple conversations from JSON files. Happy is prompted about information from the oldest saved conversation. The `datetime` library is used in a formatted string to represent the dates used in this test.

`test_message_history.py`
- Simulates a conversation between the user and Happy about a Birthday Party, then uses `unittest` to ensure proper storage of message history of both sides. One test looks at the storage of all of the messages Happy sends, and the other test looks at the storage of all the messages the user sends.