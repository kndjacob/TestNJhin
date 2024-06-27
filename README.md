# Welcome to the Open Source Test Engine!

Here's how to use it:

1. Download TestEngine IV.zip
2. Unzip in a familiar location
3. Execute TestNJhin with Python
    A. CSV Format Requirements:
        - The program is designed to take a .csv file with the exact header:
        {question,option_a,option_b,option_c,option_d,correct_option}
        - To create your own test banks, simply follow this easy-to-use header format.
    B. Directory Traversal Plugin:
        - Use the directory traversal plugin to navigate through files and directories.
        - The list of available files and directories will be printed on the console.
        - Use the 'C' button to change directories using the numbers associated with the directories output.
        - Use '..' to move back up one directory.
        - Once you can spot your file user 'L' to select the .csv, and then choose the number of questions you want to take for the test
        (Default is n/n)
    C. Custom Test Questions:
        - You can write your own test questions in a CSV file and use TestNJhin to navigate to that CSV and take your own test, as long as the encoding is correct.
    D. Exiting the Program:
        - You can quit the program at most prompts by entering 'Q'. This will still compile your test results and display them to you.
4. Find and select your test bank
5. Choose the number of questions.
6. Start and enjoy!

**Note**: Ensure you have Python3 installed. Using **Visual Studio Code** is recommended.

Thanks for using our test engine!
