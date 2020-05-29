import numpy as np
from collections.abc import Iterable


class NumPyCreator:
    @staticmethod
    def from_list(lst, dtype=None):
        if not isinstance(lst, list):
            raise TypeError
        return np.array(lst, dtype)

    @staticmethod
    def from_tuple(tup, dtype=None):
        if not isinstance(tup, tuple):
            raise TypeError
        return np.array(tup, dtype)

    @staticmethod
    def from_iterable(ite, dtype=None):
        if not isinstance(ite, Iterable):
            raise TypeError
        return np.array(ite, dtype)

    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    @staticmethod
    def random(shape, dtype=None):
        return np.random.rand(*shape)

    @staticmethod
    def identity(n, dtype=None):
        return np.identity(n, dtype)


if __name__ == '__main__':
    npc = NumPyCreator()
    print('from list :\n', npc.from_list([[1, 2, 3], [6, 3, 4]]))
    # print(npc.from_list(("a", "b", "c")))
    print('\nfrom tuple :\n', npc.from_tuple(("a", "b", "c")))
    print('\nfrom iterable :\n', npc.from_iterable(range(5)))
    shape = (2, 5)
    print('\nshape = ', shape)
    print('\nfrom_shape :\n', npc.from_shape(shape))
    print('\nfrom_shape :\n', npc.from_shape(shape, 2.5))
    print('\nfrom_shape :\n', npc.from_shape(shape, 2.5, str))
    print('\nrandom :\n', npc.random(shape))
    # print('\nrandom :\n', npc.random((1.5, 2.5)))
    print('\nidentity :\n', npc.identity(5))
