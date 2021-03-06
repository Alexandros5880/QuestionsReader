
# Pass Flag To Terminal
def Setup():
    global args
    import argparse
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-f", "--file", dest = "file", default = "", help="Enter the file.", required=True)
    optional.add_argument("-s", "--split", dest = "splitcharacter", default = "\n&&&\n", help="Enter the split characters of questions")
    optional.add_argument("-a", "--answer", dest = "answer", default = False, help="Display or not the answer.", action='store_true')
    args = parser.parse_args()
    return {'filename' : args.file, 'splitCharacter' : args.splitcharacter, 'showAnswer' : args.answer}


# Get Questions from file
def GetQuestions(filename, str):
    file = open(filename, "r")
    contents = file.read().split(str)
    return contents


# Ask questions on terminal
def AskQuestionsTerminal(contents, showAnswer):
    from colorama import init
    init()
    countQuestions = len(contents)-2
    if not showAnswer:
        grade = 0
    counter = 1
    while counter <= countQuestions:
        lines = contents[counter].split("\n")
        answer = ""
        for l in lines:
            if "*" in l:
                answer = l
                break
        if not showAnswer:
            questions = contents[counter].replace("*", "")
        else:
            questions = contents[counter]
        print("\n\033[2;37;40m%d / %d" % (counter, countQuestions) )
        print(questions)
        if answer:
            answerLetter = answer[0]
            if not showAnswer:
                usersUnswer = input("Quit(q), Enter your Answer: ")
            else:
                usersUnswer = input("Quit(q), Enter for next.")
            if usersUnswer == 'q':
                break
            if answerLetter.lower() == usersUnswer.lower() or showAnswer:
                if not showAnswer:
                    print("\n\033[2;32;40mNice!!!\n")
                    grade += 1
            else:
                print("\n\033[2;31;40mWrong Answer!!!")
                print("\033[2;32;40mRight Answer is: %s\n" % answerLetter)
            counter += 1
    if not showAnswer:
        print("\033[2;32;40m Your Grade: %d / 100" % ( (grade*100)/countQuestions ))
    print("\033[2;37;40m")
            




if "__main__" == __name__:
    arguments = Setup()
    contents = GetQuestions(arguments['filename'], arguments['splitCharacter'])
    AskQuestionsTerminal(contents, arguments['showAnswer'])