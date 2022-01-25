
# Pass Flag To Terminal
import argparse
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument("-f", "--file", dest = "file", default = "", help="Enter the file.", required=True)
optional.add_argument("-s", "--split", dest = "splitcharacter", default = "\n&&&\n", help="Enter the split characters of questions")
optional.add_argument("-a", "--answer", dest = "answer", default = False, help="Display or not the answer.", action='store_true')
args = parser.parse_args()


def GetSplitString():
    splitCharacter = args.splitcharacter
    return splitCharacter

def Answer():
    return args.answer

def ReadFile(str):
    filename = args.file
    file = open(filename, "r")
    contents = file.read().split(str)
    return contents

def Ask(contents, showAnswer):
    countQuestions = len(contents)-1
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
                counter += 1
                if not showAnswer:
                    print("\n\033[2;32;40mNice!!!\n")
                    grade += 1
            else:
                print("\n\033[2;31;40mWrong Answer!!!")
                print("\033[2;32;40mRight Answer is: %s\n" % answerLetter)
                continue
    if not showAnswer:
        print("\033[2;32;40m Your Grade: %d / 100" % ( (grade*100)/countQuestions ))
    print("\033[2;37;40m")
            




if "__main__" == __name__:
    splitCharacter = GetSplitString()
    contents = ReadFile(splitCharacter)
    Ask(contents, Answer())