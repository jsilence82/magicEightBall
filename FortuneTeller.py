import random


class FortuneTeller:
    __fortune_lines = ["One day, you will die.", "Your parents never told you that you were an accident.",
                       "You will get sex.", "You will die a virgin.",
                       "Your mom will learn the blessing that is my penis.",
                       "Your sister is hot.", "One day, you will finally stop wetting the bed.",
                       "I'll see you later... tonight.", "That girl you're interested in? She thinks you're gay.",
                       "I'm going to do things to your dad that will make him leave your mom.",
                       "There's a bottle of hand lotion waiting for you tonight.",
                       "Stop masturbating so much. The frequency is disturbing.", "So much furry porn. So...so much."]

    def __init__(self):
        self.random_fortune = None

    def fortune(self):
        self.random_fortune = random.choice(self.__fortune_lines)
        return self.random_fortune
