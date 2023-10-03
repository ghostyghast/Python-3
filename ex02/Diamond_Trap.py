from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""
    def __init__(self, name, state=True):
        self.name, self.family_name = name, 'Baratheon'
        self.eyes, self.hairs = 'brown', 'dark'
        self.is_alive = state

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


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
