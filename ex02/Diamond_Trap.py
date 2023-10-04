from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""
    def __init__(self, name, state=True):
        """The king class, inherits from both baratheon and lannister.
        It then inherits the init from the first class it inhereits :
        Baratheon"""
        super().__init__(name, state)

    def set_eyes(self, color):
        """set eye color"""
        self.eyes = color

    def set_hairs(self, color):
        """set hair color"""
        self.hairs = color

    def get_eyes(self):
        """get eye color"""
        return self.eyes

    def get_hairs(self):
        """get eye color"""
        return self.hairs
