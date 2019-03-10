"""This class is about an abstract monster,
also implemented Py Game.

Monster can walk, jump, run and only be killed depends on the tools
that the user have"""


class AbstractMonster:
    WIN = "A Bad day camping is still better than a good day working"

    def __init__(self, name, image, sound):
        """Private variables: name, motions, and
        different ways to scare users, have sounds"""
        self._name = name
        self._image = image
        self._sound = sound

    def get_name(self):
        return self._name

    def get_image(self):
        return self._image

    def get_sound(self):
        return self._sound

    def get_win(self):
        return self.WIN
