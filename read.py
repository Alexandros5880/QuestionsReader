
# Pass Flag To Terminal
import argparse
parser = argparse.ArgumentParser()
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument("-f", "--file", dest = "file", default = "", help="Enter the file.", required=True)
optional.add_argument("-s", "--split", dest = "splitcharacter", default = "\n&&&\n", help="Enter the split characters of questions")
optional.add_argument("-a", "--answer", dest = "answer", default = False, help="Display or not the answer.", action='store_true')
optional.add_argument("-g", "--grade", dest = "grade", default = False, help="Display or not you grade.", action='store_true')
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
    countQuestions = len(contents)
    if args.grade:
        grade = 0
    counter = 1
    while counter < countQuestions:
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
        print(questions)
        if answer:
            answerLetter = answer[0]
            usersUnswer = input("Enter your Answer: ")
            if usersUnswer == 'q':
                break
            if answerLetter.lower() == usersUnswer.lower():
                print("\nNice!!!\n")
                counter += 1
                if args.grade:
                    grade += 1
            else:
                print("\nWrong!!!")
                print("Right Answer is: %s\n" % answerLetter)
                if args.grade:
                    counter += 1
                continue
    print((grade*100)/countQuestions)
            




if "__main__" == __name__:
    splitCharacter = GetSplitString()
    contents = ReadFile(splitCharacter)
    Ask(contents, Answer())