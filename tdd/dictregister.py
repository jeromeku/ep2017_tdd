import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)

    def find(self, *args, **kwargs):
        result = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )

        norm_kwargs = {}
        for k, v in kwargs.items():
            if '__' not in k:
                k = k + '__eq'
            norm_kwargs[k] = v

        for k, v in norm_kwargs.items():
            key, operator = k.split('__')
            if operator == 'eq':
                result = [d for d in result if key in d and d[key] == v]

        return self.__class__(result)
