
class calculator:
    def __init__(self, nums):
        """save the given list of numbers to internal variable"""
        self.nums = nums

    def __add__(self, object) -> None:
        """overloads the plus operator to update internal vairable to
        new list that is created by adding each item in list by the
        given number"""
        self.nums = [x + object for x in self.nums]
        print(self.nums)

    def __mul__(self, object) -> None:
        """overloads the multiply operator to update internal vairable to
        new list that is created by multiplying each item in list by the
        given number"""
        self.nums = [x * object for x in self.nums]
        print(self.nums)

    def __sub__(self, object) -> None:
        """overloads the minus operator to update internal vairable to
        new list that is created by subtracting each item in list by the
        given number"""
        self.nums = [x - object for x in self.nums]
        print(self.nums)

    def __truediv__(self, object) -> None:
        """overloads the division operator to update internal vairable to
        new list that is created by dividing each item in list by the
        given number
        If given number is 0, raise an assertion error"""
        assert object != 0, "can't divide by 0"
        self.nums = [x / object for x in self.nums]
        print(self.nums)
