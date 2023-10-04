class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print('Dot product is:', sum([float(x*y) for x, y in zip(V1, V2)]))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print('Add vector is:', [float(x*y) for x, y in zip(V1, V2)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print('Sous vector is ', [float(x-y) for x, y in zip(V1, V2)])


# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a, b)
# calculator.add_vec(a, b)
# calculator.sous_vec(a, b)
