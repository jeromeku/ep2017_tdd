import collections

from tdd import dictregister as dr


def test_init():
    dr.DictRegister()


def test_mutable_sequence():
    assert isinstance(dr.DictRegister(), collections.MutableSequence)


def test_append_works():
    d = dr.DictRegister()

    d.append({'a': 1, 'b': 2})

    assert len(d) == 1
    assert d[0] == {'a': 1, 'b': 2}
