import random


class Opening:

    __opening_lines = ["would you like to try our Jalapeño Poppers?", "are you happy with your current insurance?",
                       "please fucking kill me.", "home of the Whopper... in my pants.", "hey gorgeous.",
                       "I like big butts and I cannot lie.", "would you like fries with that?",
                       "have you tried turning it off and on again?", "we've got fun and games.",
                       "where our motto is: 'We're not happy until you're pissed off.", "just don't expect much.",
                       "take me to your leader.", "how's your mom doing?", "how's your dad doing? Still working out?",
                       "where if the house is a-rockin, don't come a-knockin.", "we fuck on the first date.",
                       "give me a twenty and I will rock your world.", "ass, grass, or gas. No one rides for free.",
                       "and the first and last words out of your filthy sewers will be 'Sir'. Do you maggots understand that?",
                       "sound off like you got a pair."]

    def __init__(self):
        self.random_opening_line = None

    def opening(self):
        self.random_opening_line = random.choice(self.__opening_lines)
        return self.random_opening_line
