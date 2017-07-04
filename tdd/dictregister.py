import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)

    def find(self, key):
        return self.__class__(
            [d for d in self if key in d]
        )
