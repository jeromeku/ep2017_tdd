import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)
