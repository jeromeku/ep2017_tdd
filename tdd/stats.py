import math
import json


def _avg(seq):
    return math.floor(sum(seq)/len(seq))


class DataStats:

    def __init__(self, data):
        self.data = data

    @property
    def _ages(self):
        return [e['age'] for e in self.data]

    @property
    def _salaries(self):
        return [int(e['salary'][1:]) for e in self.data]

    def _age_avg(self):
        return _avg(self._ages)

    def _salary_avg(self):
        return _avg(self._salaries)

    def _yearly_avg_increase(self, iage, isalary):
        average_age_increase = self._age_avg() - iage
        average_salary_increase = math.floor(self._salary_avg()) - isalary

        return math.floor(average_salary_increase/average_age_increase)

    def _salary_str(self, salary):
        return '£' + salary

    def _select_salary(self, salary):
        threshold = self._salary_str(str(salary))

        return [e for e in self.data if e['salary'] == threshold]

    def _max_salary(self):
        return self._select_salary(max(self._salaries))

    def _min_salary(self):
        return self._select_salary(min(self._salaries))

    def stats(self, iage, isalary):
        return json.dumps({
            'avg_age': self._age_avg(),
            'avg_salary': self._salary_avg(),
            'avg_yearly_increase': self._yearly_avg_increase(iage, isalary),
            'max_salary': self._max_salary(),
            'min_salary': self._min_salary()
        })
