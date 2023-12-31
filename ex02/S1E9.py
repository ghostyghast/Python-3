from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self):
        """Your docstring for constructor"""
        pass

    @abstractmethod
    def die(self):
        """your docstring for method"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name, state=True):
        """Your docstring for constructor"""
        self.first_name = name
        self.is_alive = state

    def die(self):
        """method sets is_alive bool to false"""
        self.is_alive = False
