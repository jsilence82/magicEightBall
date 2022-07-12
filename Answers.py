import random


class Answers:

    __answer_pool = ["Sure, whatever.", "Ask me again when I sober up.",
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
                     "Don't do it. Seriously, I knew a guy who did it and he's got cancer."
                     "Hmmm, not too sure. Yeah screw it. Why not?",
                     "Are you really that fucking stupid? Of course it's a bad idea.",
                     "Two words: killer bees. That's what is waiting for you."]

    def __init__(self):
        self.random_answer = None

    def answers(self):
        self.random_answer = random.choice(self.__answer_pool)
        return self.random_answer
