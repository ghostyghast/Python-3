class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Static method that prints the scalar product of two given arrays"""
        print('Dot product is:', sum([float(x*y) for x, y in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """static method that prints an array of each item in each
        given array, added together"""
        print('Add vector is:', [float(x*y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """static method that prints an array of each item in each
        given array, subtracted from each other"""
        print('Sous vector is ', [float(x-y) for x, y in zip(V1, V2)])
