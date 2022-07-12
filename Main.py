# A fun interactive Magic 8 Ball simulator with a twist. Warning: twisted humor
import time
from Answers import Answers
from FortuneTeller import FortuneTeller
from Opening import Opening


def main():

    opening_line = Opening()
    print("Welcome to Magic8Ball, {}".format(opening_line.opening()))

    time.sleep(1.5)
    user_name = input("\nOh, sorry. What I meant was... What's your name? ")

    while True:
        while True:
            try:
                user_number = int(input("\nAlright, {}. Give me a number. "
                                        "I'm going to use it to tell your fortune later: ".format(user_name)))
            except ValueError:
                print("I need a number, dumb-dumb. Try it again.")
            else:
                break

        user_question = input("\nSo {}. What's your question? ".format(user_name))

        print("\n\nOK. Here we go...")
        answer = Answers()
        fortune = FortuneTeller()

        i = 0
        while i < 3:
            time.sleep(1)
            print("\n'Shaking...'")
            i = i + 1

        time.sleep(1)
        print("\nThe answer to '{}' is:".format(user_question))
        time.sleep(3)
        print(answer.answers())

        time.sleep(2)
        print("\nYour lucky number was", user_number, "\nHere's your fortune:".format(user_number))
        time.sleep(2)
        print(fortune.fortune())

        time.sleep(3)
        print("\nHave a nice day :)")

        time.sleep(3)

        repeat = input("\nOh. you're still here? \nType any key if you want to continue. "
                       "Type 'N' if you want to stop: ")
        if repeat.lower() != "n":
            continue
        else:
            print("Alright. Smell you later.")
            break


if __name__ == '__main__':
    main()
