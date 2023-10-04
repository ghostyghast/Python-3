
class calculator:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, object) -> None:
        """adds """
        self.nums = [x + object for x in self.nums]
        print(self.nums)

    def __mul__(self, object) -> None:
        self.nums = [x * object for x in self.nums]
        print(self.nums)

    def __sub__(self, object) -> None:
        self.nums = [x - object for x in self.nums]
        print(self.nums)

    def __truediv__(self, object) -> None:
        assert object != 0, "can't divide by 0"
        self.nums = [x / object for x in self.nums]
        print(self.nums)
