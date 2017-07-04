import collections


class DictRegister(list):

    def append(self, elem):
        if not isinstance(elem, collections.Mapping):
            raise TypeError
        super().append(elem)

    def _match(self, item, keyop, value):
        # Split key and operator
        if '__' not in keyop:
            keyop = keyop + '__eq'
        key, op = keyop.split('__')

        if op == "eq":
            try:
                return item[key] == value
            except KeyError:
                return False
        else:
            return item[key] > value

    def find(self, *args, **kwds):
        starting_list = self.__class__(
            [d for d in self if set(args).issubset(set(d.keys()))]
        )

        filtered_list = []
        for key, value in kwds.items():
            for item in starting_list:
                if self._match(item, key, value):
                    filtered_list.append(item)
            starting_list = filtered_list
            filtered_list = []

        return self.__class__(starting_list)

    def kadd(self, key, value):
        for item in self:
            try:
                # Use the key as a set
                item[key].add(value)
            except KeyError:
                # This happens if the key is not present
                item[key] = value
            except AttributeError:
                # This happens if the key is present but is not a set
                item[key] = set([item[key], value])

    def kremove(self, key, value=None):
        for item in self:
            if value is None:
                item.pop(key, None)
            else:
                if item[key] == value:
                    item.pop(key)
