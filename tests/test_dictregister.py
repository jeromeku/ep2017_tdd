import pytest

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


def test_append_checks_if_mapping():
    d = dr.DictRegister()

    d.append({'a': 1, 'b': 2})

    with pytest.raises(TypeError):
        d.append([1, 2, 3, 4])
