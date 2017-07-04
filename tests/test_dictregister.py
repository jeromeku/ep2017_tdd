import pytest

import collections

from tdd import dictregister as dr


@pytest.fixture
def simple_dict():
    return {'a': 1, 'b': 2}


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


def test_init_with_list_of_dicts(simple_dict):
    d = dr.DictRegister([simple_dict])

    assert len(d) == 1


def test_equality():
    assert dr.DictRegister([{'a': 1, 'b': 2}]) == \
        dr.DictRegister([{'a': 1, 'b': 2}])

    assert dr.DictRegister([{'a': 1, 'b': 2}]) != \
        dr.DictRegister([{'a': 3, 'b': 2}])

    assert dr.DictRegister([{'a': 1, 'b': 2}]) != \
        dr.DictRegister([{'a': 1}])


def test_find_single_key():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a') == dr.DictRegister([{'a': 1, 'b': 2}, {'a': 5, 'c': 6}])


def test_find_multiple_keys():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a', 'b') == dr.DictRegister([{'a': 1, 'b': 2}])


def test_find_single_key_value():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find(a=1) == dr.DictRegister([{'a': 1, 'b': 2}])


def test_find_single_key_value_multiple_results():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(c=4) == dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4}
    ])


def test_find_multiple_key_values():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(a=1, c=4) == dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4}
    ])


def test_find_unnamed_and_named():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a', b=6) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])


def test_find_explicit_equal():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(b__eq=6) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])


def test_find_greater_than():
    d = dr.DictRegister([
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 5, 'b': 6, 'c': 4},
        {'b': 3, 'c': 9}
    ])

    assert d.find(b__gt=3) == dr.DictRegister([
        {'a': 5, 'b': 6, 'c': 4}
    ])
