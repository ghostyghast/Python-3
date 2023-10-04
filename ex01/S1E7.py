from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, name, state=True):
        self.name, self.family_name = name, 'Baratheon'
        self.eyes, self.hairs = 'brown', 'dark'
        self.is_alive = state

    def die(self):
        self.is_alive = False

    def __str__(self):
        """a custom __str__ value"""
        return f'Vector: {self.__dict__.values()}>'

    def __repr__(self) -> str:
        """a custom __repr__ value"""
        return f'Vector: {self.family_name, self.eyes, self.hairs}'


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, name, state=True):
        self.first_name, self.family_name = name, 'Lannister'
        self.eyes, self.hairs = 'blue', 'light'
        self.is_alive = state

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f'Vector: {self.__dict__.values()}>'

    def __repr__(self) -> str:
        return f'Vector: {self.family_name, self.eyes, self.hairs}'

    @classmethod
    def create_lannister(cls, name, state=True):
        """create_lannister(string name, optional state) -> lannister class
        lannister method that returns new lannister class object"""
        return cls(name, state)
