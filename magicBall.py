# A fun interactive Magic 8 Ball simulator with a twist. Warning: twisted humor
import random
import time


def answers():
    answer_pool = ["Sure, whatever.", "Ask me again when I sober up.",
                   "I don't care. I really don't care. Just make this end.",
                   "All work and no play make Jack a dull boy... what was the question?",
                   "Google says....yes.", "Google says....no.",
                   "I don't think that's a good idea Dave, or whatever the hell your name is.",
                   "Does the pope shit in the woods?", "My own Magic8Ball says... 'Try again later'??? Goddamnit.",
                   "It's not a good idea but will make a great story later.", "Do it, you know you want to.",
                   "Seriously, if you're asking me, you already made up your mind. Just do it already",
                   "Try again later, I'm drunk.", "Try again later, you're drunk.",
                   "This is one of those things where it's better to ask a lawyer first",
                   "Sorry, too busy banging your mom to answer now.", "Sigh. Can you just ask your mother?",
                   "Don't do it. Seriously, I knew a guy who did it and he's got cancer.", 
                   "Hmmm, not too sure. Yeah screw it. Why not?",
                   "Are you really that fucking stupid? Of course it's a bad idea.",
                   "Two words: killer bees. That's what is waiting for you."]

    random_answer = random.choice(answer_pool)
    return random_answer


def openers():
    opening_lines = ["would you like to try our Jalapeño Poppers?", "are you happy with your current insurance?",
                     "please fucking kill me.", "home of the Whopper... in my pants.", "hey gorgeous."
                     "I like big butts and I cannot lie.", "would you like fries with that?",
                     "have you tried turning it off and on again?", "we've got fun and games.",
                     "where our motto is: 'We're not happy until you're pissed off.", "just don't expect much.",
                     "take me to your leader.", "how's your mom doing?", "how's your dad doing? Still working out?",
                     "where if the house is a-rockin, don't come a-knockin.", "we fuck on the first date.",
                     "give me a twenty and I will rock your world.", "ass, grass, or gas. No one rides for free.",
                     "and the first and last words out of your filthy sewers will be 'Sir'. Do you maggots understand that?",
                     "sound off like you got a pair."]

    random_opening_line = random.choice(opening_lines)
    return random_opening_line


def fortune_teller():
    fortune_lines = ["One day, you will die.", "Your parents never told you that you were an accident.",
                     "You will get sex.", "You will die a virgin.", "Your mom will learn the blessing that is my penis.",
                     "Your sister is hot.", "One day, you will finally stop wetting the bed.",
                     "I'll see you later... tonight.", "That girl you're interested in? She thinks you're gay.",
                     "I'm going to do things to your dad that will make him leave your mom.",
                     "There's a bottle of hand lotion waiting for you tonight.",
                     "Stop masterbating so much. The frequency is disturbing.", "So much furry porn. So...so much."]

    random_fortune = random.choice(fortune_lines)
    return random_fortune


def main():

    print("\nWelcome to Magic8Ball, {}".format(openers()))

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


        user_question = input("\nSo, {}. What's your question? ".format(user_name))

        print("\n\nOK. Here we go...")

        i = 0
        while i < 3:
            time.sleep(1)
            print("\n'Shaking...'")
            i = i + 1

        time.sleep(1)
        print("\nThe answer to '{}' is:".format(user_question))
        time.sleep(3)
        print(answers())

        time.sleep(2)
        print("\nYour lucky number was", user_number, "\nHere's your fortune:".format(user_number))
        time.sleep(2)
        print(fortune_teller())

        time.sleep(3)
        print("\nHave a nice day :)")

        time.sleep(3)

        repeat = input("\nOh. you're still here? \nType any key if you want to continue. Type 'N' if you want to stop: ")
        if repeat.lower() != "n":
            continue
        else:
            print("Alright. Smell you later.")
            break


if __name__ == '__main__':
    main()
