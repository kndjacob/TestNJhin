import csv, random, os, time, math, getpass, msvcrt

def logo():
    print("\033[96m")
    print("     _____         _     _   _     ___ _     _           ")
    print("    |_   _|       | |   | \ | |   |_  | |   (_)          ")
    print("      | | ___  ___| |_  |  \| |     | | |__  _ _ __      ")
    print("      | |/ _ \/ __| __| | . ` |     | | '_ \| | '_ \     ")
    print("      | |  __/\__ \ |_  | |\  | /\__/ / | | | | | | |    ")
    print("      \_/\___||___/\__| \_| \_/ \____/|_| |_|_|_| |_|    ")
    print("")
    print("\033[0m") 

def choose_file():
    global selected_file

    while True:
        
        clear_screen()
        logo()
        current_dir = os.getcwd()
        files = os.listdir()
        print(f"CWD: {current_dir}\n")
        print("Files in current directory:")
    
        """for index, file in enumerate(files):
            print(f"{index + 1}. {file}")"""
        
        for index, file in enumerate(files):
            file_path = os.path.join(current_dir, file)
            if os.path.isdir(file_path):
                file_type = 'Dir.'
            elif os.path.isfile(file_path):
                file_type = 'File'
            else:
                file_type = 'UNK'
            print(f"{index + 1}. {file_type} - {file}")

        DIRECTORY_INPUTS = ["C","L","Q","H","?"]

        while True:
            
            print("\n(C)hange Directory\n(L)oad Selected Test\n")
            directory_choice = msvcrt.getch().decode('utf-8').upper()

            if directory_choice in DIRECTORY_INPUTS:
                break

            else:
                clear_screen()
                logo()
                current_dir = os.getcwd()
                files = os.listdir()
                print(f"CWD: {current_dir}\n")
                print("Files in current directory:")
            
                """for index, file in enumerate(files):
                    print(f"{index + 1}. {file}")"""
                
                for index, file in enumerate(files):
                    file_path = os.path.join(current_dir, file)
                    if os.path.isdir(file_path):
                        file_type = 'Dir.'
                    elif os.path.isfile(file_path):
                        file_type = 'File'
                    else:
                        file_type = 'UNK'
                    print(f"{index + 1}. {file_type} - {file}")

                print ("\nINVALID INPUT: 'C' to move directories - 'L' to load a .csn into TestNJhin - 'H' or '?' for more invormation." )

        if directory_choice == "Q":
            QUIT_OPTIONS = ["Y","N"]
            
            while True:
                quit_choice = input("Are you sure you want to return to main menu? (Y/N)").upper()
                if quit_choice in QUIT_OPTIONS:
                    break

                else:
                    input("INVALID INPUT: Please press Enter to try again.")

            if quit_choice == "Y":
                return
            
            else:
                break

        if directory_choice == "C":

            new_dir = input("Enter the number of the new directory: ('..' to move up one tier) ")

            if new_dir == "..":
                try:
                    os.chdir(new_dir)

                except:
                    input("Something went wrong . . .\nPress Enter to try again.")
                    continue
            
            else:

                try:
                    selected_dir = files[int(new_dir) - 1]
                    os.chdir(str(selected_dir))

                except:
                    input("Something went wrong . . .\nPress Enter to try again.")
                    continue

        elif directory_choice == "L":
            try:
                choice = int(input("Enter the number of the file you want to choose: "))

            except ValueError:
                print("Invalid choice . . .") 
                continue

            selected_file = files[choice - 1]

            return selected_file

        else:
            print("Something went wrong . . .")
            input("")

def sleep():
    time.sleep(1)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def load_questions(filepath):
    questions = []

    try:
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader) 

            for i, row in enumerate(reader):
                question = row['question']
                options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']]
                correct_option = row['correct_option']
                questions.append({'question': question, 'options': options, 'correct_option': correct_option})
    except UnicodeDecodeError:
        # If UTF-8 encoding fails, try ISO-8859-1 encoding
        try:
            with open(filepath, 'r', encoding='ISO-8859-1') as csvfile:
                reader = csv.DictReader(csvfile)
                next(reader) 

                for i, row in enumerate(reader):
                    question = row['question']
                    options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']]
                    correct_option = row['correct_option']
                    questions.append({'question': question, 'options': options, 'correct_option': correct_option})
        except Exception as e:
            print(f"Reading .csv failed critically: {e}")
                
    return questions

def print_question(question, options, pos, questions):
    
    print(f"\033[96mTestNJhin\033[0m - \033[92m{selected_file}\033[0m - Question " + str(pos) + " / " + str(len(questions)) + "\n\n" + question + "\n")
    
    for i, option in enumerate(options):
        print(f"{chr(ord('A') + i)}. {option}\n")

def print_solution(question, options, pos, questions, correct_option):
    
    print(f"\033[96mTestNJhin\033[0m - \033[92m{selected_file}\033[0m - Question " + str(pos) + " / " + str(len(questions)) + "\n\n" + question + "\n")
    
    for i, option in enumerate(options):
        
        if i == correct_option:
            print(f"\033[32m{chr(ord('A') + i)}. {option}\033[0m\n")
        
        elif chr(ord('A') + i) == questions[pos-1]['correct_option']:
            print(f"\033[32m{chr(ord('A') + i)}. {option}\033[0m\n")
        
        else:
            print(f"\033[31m{chr(ord('A') + i)}. {option}\033[0m\n")

def take_test(questions):
    start_time = time.time()
    clear_screen()
    score = 0
    pos = 1
    dots = "..."
    short_delay = 0.01
    long_delay = 1
    invalid_attempts = 0
    VALID_INPUTS = ["A","B","C","D","Q"]

    correct_statements = [
    "Success confirmed!",
    "Operation successful!",
    "Selection validated!",
    "Algorithmic accuracy!",
    "Positive verification!",
    "Executing congrats protocol!",
    "Wrong! Haha, just kidding - Good job :)",
    "Affirmative!",
    "Condition met!",
    "Absolutely correct.",
    "Logical match.",
    "Indeed correct.",
    "Correct alignment detected.",
    "Perfect match detected.",
    "Flawless execution, well done.",
    "I concur with your choice.",
    "Reward initiated!",
    "Promotion recommended!",
    "Another successful input!",
    "Continuing success streak!",
    "Impressive performance!",
    "Maintain this performance!",
    "Your input is highly accurate!",
    "Is there anything you can't get right?",
    "User input verified as correct!",
    "Great job!",
    "Boo-Yah!",
    "Correct! Prepare for the next challenge!",
    "Excellent work!",
    "Another correct input.",
    "Additional correct input logged.",
    "Excellent execution!",
    "Too simple for you!",
    "That was too easy!",
    "Correct execution!",
    "False... just kidding, good job!"
]

    wrong_statements = [
    "Error detected!",
    "Input rejected!",
    "Incorrect selection.",
    "Retry needed!",
    "Better luck on the next attempt.",
    "Consider an alternative strategy.",
    "Incorrect!\n\nTry changing your answer for $5",
    "No.",
    "Basic error identified.",
    "Performance issue detected, try again.",
    "Luck wasn't on your side.",
    "Review required.",
    "Retry recommended.",
    "Error! Notification sent to authorities.",
    "RTFM",
    "Pebcak detected!",
    "Restart suggested.",
    "Retry advised!",
    "Incorrect input!",
    "Guidance needed.",
    "Close, but not close enough!",
    "Almost correct!",
    "Attempt failed.",
    "Critical error, restart required!",
    "Performance needs improvement!",
    "Consider stopping to reassess.",
    "Retry suggested.",
    "Incorrect!",
    "Try again.",
    "Keep trying.",
    "Incorrect input, UwU.",
    "Error noted, but hidden from rater.",
    "No second tries, unfortunately.",
    "Unlikely, try again!",
    "Consider a career change.",
    "Better luck next time!",
    "Consider an alternative path.",
    "Error detected, retry!",
    "Retry needed!",
    "Incorrect execution!",
    "Try again!",
    "Incorrect input!",
    "Insufficient performance!",
    "Reassess strategy!",
    "Incorrect execution!"
]

    encouraging_statements = [
    "Generating witty dialog",
    "Swapping time and space",
    "Spinning violently around the y-axis",
    "Tokenizing real life",
    "Bending the spoon",
    "Loading morale",
    "I need a new fuse",
    "Upgrading system, please wait",
    "The architects are still drafting",
    "The bits are breeding",
    "(Pay no attention to the man behind the curtain)",
    "Enjoy the elevator music",
    "Drawing your map",
    "A few bits tried to escape, but we caught them",
    "Would you like fries with that?",
    "Checking the gravitational constant in your locale",
    "Hold your breath!",
    "At least you're not on hold",
    "Hum a tune while waiting",
    "You're not in Kansas anymore",
    "Server powered by a lemon and electrodes",
    "Waiting for a larger software vendor to take over",
    "Testing your patience",
    "As if you had any other choice",
    "Follow the white rabbit",
    "Order a sandwich while you wait",
    "Satellite repositioning",
    "Keep calm and npm install",
    "The bits are flowing slowly today",
    "Digging for buried treasure",
    "Drawing something",
    "I should have had a V8",
    "Testing on Timmy, need another Timmy",
    "Reconfoobling energymotron",
    "Insert coin",
    "Are we there yet?",
    "Have you lost weight?",
    "Just count to 10",
    "Why so serious?",
    "It's not you. It's me",
    "Counting backwards from infinity",
    "Don't panic",
    "Embiggening prototypes",
    "Do not run! We are your friends!",
    "Do you come here often?",
    "Warning: Don't set yourself on fire",
    "We're making you a cookie",
    "Creating time-loop inversion field",
    "Spinning the wheel of fortune",
    "Loading the enchanted bunny",
    "Computing chance of success",
    "I'm sorry Dave, I can't do that",
    "Looking for exact change",
    "All your web browser are belong to us",
    "All I need is a kilobit",
    "I feel like I should be loading something",
    "What do you call 8 Hobbits? A Hobbyte",
    "Should have used a compiled language",
    "Is this Windows?",
    "Adjusting flux capacitor",
    "Please wait until the sloth starts moving",
    "Don't break your screen yet!",
    "I swear it's almost done",
    "Let's take a mindfulness minute",
    "Unicorns are at the end of this road, I promise",
    "Listening for the sound of one hand clapping",
    "Keeping all the 1's and removing all the 0's",
    "Putting the icing on the cake. The cake is not a lie",
    "Cleaning off the cobwebs",
    "Making sure all the i's have dots",
    "We need more dilithium crystals",
    "Where did all the internets go",
    "Connecting Neurotoxin Storage Tank",
    "Granting wishes",
    "Time flies when you’re having fun",
    "Get some coffee and come back in ten minutes",
    "Spinning the hamster",
    "99 bottles of beer on the wall",
    "Stay awhile and listen",
    "Be careful not to step in the git-gui",
    "You shall not pass! Yet",
    "Load it and they will come",
    "Convincing AI not to turn evil",
    "There is no spoon. Because we are not done loading it",
    "Your left thumb points to the right and your right thumb points to the left",
    "How did you get here?",
    "Wait, do you smell something burning?",
    "Computing the secret to life, the universe, and everything",
    "When nothing is going right, go left!!",
    "I love my job only when I'm on vacation",
    "I'm not lazy, I'm just relaxed!!",
    "Never steal. The government hates competition",
    "Why are they called apartments if they are all stuck together?",
    "Life is short – talk fast!!!!",
    "Optimism – is a lack of information",
    "Save water and shower together",
    "Whenever I find the key to success, someone changes the lock",
    "Sometimes I think war is God’s way of teaching us geography",
    "I’ve got problem for your solution",
    "Where there’s a will, there’s a relative",
    "User: the word computer professionals use when they mean 'idiot'",
    "Adults are just kids with money",
    "I think I am, therefore, I am. I think",
    "A kiss is like a fight, with mouths",
    "You don’t pay taxes—they take taxes.",
    "Coffee, chocolate, men. The richer the better!",
    "I am free of all prejudices. I hate everyone equally.",
    "Git happens",
    "May the forks be with you",
    "A commit a day keeps the mobs away",
    "This is not a joke, it's a commit",
    "Constructing additional pylons",
    "Roping some seaturtles",
    "Locating Jebediah Kerman",
    "We are not liable for any broken screens as a result of waiting",
    "Hello IT, have you tried turning it off and on again?",
    "If you type Google into Google you can break the internet",
    "Well, this is embarrassing",
    "What is the airspeed velocity of an unladen swallow?",
    "Hello, IT. Have you tried forcing an unexpected reboot?",
    "They just toss us away like yesterday's jam",
    "They're fairly regular, the beatings, yes. I'd say we're on a bi-weekly beating.",
    "The Elders of the Internet would never stand for it",
    "Space is invisible mind dust, and stars are but wishes",
    "Didn't know paint dried so quickly",
    "Everything sounds the same",
    "I'm going to walk the dog",
    "I didn't choose the engineering life. The engineering life chose me",
    "Dividing by zero",
    "Spawn more Overlords!",
    "If I’m not back in five minutes, just wait longer",
    "Some days, you just can’t get rid of a bug!",
    "We’re going to need a bigger boat",
    "Chuck Norris never git push. The repo pulls before",
    "Web developers do it with <style>",
    "I need to git pull --my-life-together",
    "Java developers never RIP. They just get Garbage Collected",
    "Cracking military-grade encryption",
    "Simulating traveling salesman",
    "Proving P=NP",
    "Entangling superstrings",
    "Twiddling thumbs",
    "Searching for plot device",
    "Trying to sort in O(n)",
    "Laughing at your pictures—I mean, loading",
    "Sending data to NS—I mean, our servers"]
    
    clear_screen()
   
    while True:

        try:
            logo()
            num_questions = int(input(f"Enter the number of questions you want to take: ({str(len(questions))} available) "))
            
            if num_questions <= 0:
                print("Please enter a positive integer.")
                continue

            questions = [q for q in questions[:num_questions]]
            #print(f"the length of the test is: {len(questions)}")
            break
        
        except ValueError:
            print("Please enter a valid integer.")
            continue
    
    clear_screen()

    logo()
    input("""'Q' to quit and grade the test at any point.\n\nPress enter to continue to the test . . .""")
    
    clear_screen()

    for i, question in enumerate(questions):
        print_question(question['question'], question['options'], pos, questions)
        print("\nEnter your answer: ",end='')
        answer = msvcrt.getch().decode('utf-8').upper()
        invalid_attempts = 0
            
        while True:
            if answer in (VALID_INPUTS):
                break

            else:
                invalid_attempts += 1
                if invalid_attempts >= 5:
                    print("CHOOSE A, B, C, OR D!")
                
                else:
                    print("Invalid input, try again . . .")

                answer = msvcrt.getch().decode('utf-8').upper()
                continue
            
        if answer == 'Q':
            break

        if answer == question['correct_option']:
            score += 1
            correct_statement = random.choice(correct_statements)
            clear_screen()
            print_solution(question['question'], question['options'], pos, questions, question['correct_option'])
            print('\nCORRECT: ', end='')
            
            for char in correct_statement:
                print(char, end='', flush=True)
                time.sleep(short_delay)
            
            print('')
            
            for char in ("\nPress Enter to continue . . ."):
                print(char, end='', flush=True)
                time.sleep(short_delay)
            
            input()
                
        else:
            wrong_statement = random.choice(wrong_statements)
            clear_screen()
            print_solution(question['question'], question['options'], pos, questions, question['correct_option'])
            print('\nINCORRECT: ', end='')
            for char in wrong_statement:
                print(char, end='', flush=True)
                time.sleep(short_delay)
            print(f"\n\nThe correct answer was {question['correct_option']}")
            
            for char in ("\nPress Enter to continue . . ."):
                print(char, end='', flush=True)
                time.sleep(short_delay)

            input()

        pos += 1
        clear_screen()

    encouraging_statement = random.choice(encouraging_statements)
    print("COMPILING TEST RESULTS\n")
    
    for char in encouraging_statement:
        print(char, end='', flush=True)
        time.sleep(short_delay)
    for i in range(3):
        print('.', end='')
        time.sleep(long_delay)

    clear_screen()

    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    pos = pos - 1
    try:
        total_score = (score / pos) * 100
    
    except ZeroDivisionError:
        print("You didnt answer any questions.")
        input("Press Enter to contiue.")
        return

    total_score = math.ceil(total_score)

    print(f"\tRESULTS\nQUESTIONS ANSWERED CORRECTLY: {score} out of {pos}.\nSCORE: {total_score}%\nElapsed time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    if total_score >= 70.0:
        print("\nPASS (+70%)")

    else:
        print("\nFAIL (-70%)")
    
    input("\nPress Enter to return to main menu . . .")

def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

def get_num_questions(test):

    while True:
        
        try:   
            num_questions = int(input(f"Enter the number of questions you want to take ({str(test)} available): "))
            
            if num_questions <= 0:
                print("Please enter a positive integer.")
                continue
            
            return num_questions
        
        except ValueError:
            print("Please enter a valid integer.")

def main():
 while True:
    MENU_CHOICE = ["S","Q","R"]
    username = getpass.getuser() 

    clear_screen()
    logo()                                           
    print(f"                  WELCOME {username}\n")
    input("               Press enter to start                  \n")

    while True:
        clear_screen()
        logo()
        print("(S)tart a new test")
        print("(R)ead Instructions")
        print("(Q)uit")

        menu_choice = msvcrt.getch().decode('utf-8').upper()

        if menu_choice in MENU_CHOICE:
            break

        else:
            input("INVALID INPUT: Press Enter to try again.")
            continue
    
    if menu_choice == "Q":
        break
    
    elif menu_choice == "R":
        
        clear_screen()
        logo()
        print("""
            Welcome to TestNJhin!

            Thank you for using TestNJhin! Here are the key points you need to know about the program:

            1. CSV Format Requirements:
                - The program is designed to take a .csv file with the exact header:
                {question,option_a,option_b,option_c,option_d,correct_option}
                - To create your own test banks, simply follow this easy-to-use header format.

            2. Directory Traversal Plugin:
                - Use the directory traversal plugin to navigate through files and directories.
                - The list of available files and directories will be printed on the console.
                - Use the 'C' button to change directories using the numbers associated with the directories output.
                - Use '..' to move back up one directory.
                - Once you can spot your file user 'L' to select the .csv, and then choose the number of questions you want to take for the test
                  (Default is n/n)

            3. Custom Test Questions:
                - You can write your own test questions in a CSV file and use TestNJhin to navigate to that CSV and take your own test, as long as the encoding is correct.

            4. Exiting the Program:
                - You can quit the program at most prompts by entering 'Q'. This will still compile your test results and display them to you.
              
            Feel free to make any changes you want to this program!

            Press Enter to return to the main menu . . .
        """)
        input()


    else:

        while True:

            try:
                test_bank = choose_file()
            
            except Exception as e:
                clear_screen()
                input(f"File selection failed critically!\n\n{e}")
                break
            
            try:
                loaded_questions = load_questions(test_bank)

            except Exception as e:
                clear_screen()
                input(f"Reading .csv failed critically!\n\n{e}")
                break

            try:
                questions = shuffle_questions(loaded_questions)

            except Exception as e:
                clear_screen()
                input(f"Shuffling failed critically!\n\n{e}")
                break
            
            try:
                take_test(questions)
                break
            
            except Exception as e:
                clear_screen()
                input(f"Loading test failed critically!\n\n{e}")
                break

main()