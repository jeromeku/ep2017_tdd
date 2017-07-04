import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)

    def find(self, *args, **kwargs):
        args_result = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )

        return self.__class__(
            [d for d in args_result if kwargs.items() <= d.items()]
        )
