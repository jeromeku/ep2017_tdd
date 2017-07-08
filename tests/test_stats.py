import pytest

import json

from tdd.stats import DataStats


@pytest.fixture
def test_data():
    return [
        {
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        },
        {
            "id": 2,
            "name": "Mikayla",
            "surname": "Henry",
            "age": 49,
            "salary": "£67137"
        },
        {
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        }
    ]


def test_init_with_data(test_data):

    ds = DataStats(test_data)

    assert len(ds.data) == 3


def test_age_avg(test_data):
    ds = DataStats(test_data)

    assert ds._age_avg() == 62


def test_salary_avg(test_data):
    ds = DataStats(test_data)

    assert ds._salary_avg() == 55165


def test_yearly_avg_increase(test_data):
    ds = DataStats(test_data)

    assert ds._yearly_avg_increase(20, 20000) == 837


def test_max_salary(test_data):
    ds = DataStats(test_data)

    assert ds._max_salary() == [{
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "£70472"
    }]


def test_min_salary(test_data):
    ds = DataStats(test_data)

    assert ds._min_salary() == [{
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "£27888"
    }]


def test_json(test_data):
    ds = DataStats(test_data)

    assert ds.stats(20, 20000) == json.dumps(
        {
            'avg_age': 62,
            'avg_salary': 55165,
            'avg_yearly_increase': 837,
            'max_salary': [{
                "id": 3,
                "name": "Garth",
                "surname": "Fields",
                "age": 70,
                "salary": "£70472"
            }],
            'min_salary': [{
                "id": 1,
                "name": "Laith",
                "surname": "Simmons",
                "age": 68,
                "salary": "£27888"
            }]
        }
    )
