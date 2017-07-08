import math
import json


class DataStats:

    def __init__(self, data):
        self.data = data

    def _age_avg(self):
        return math.floor(sum([e['age'] for e in self.data])/len(self.data))

    def _salary_avg(self):
        return math.floor(sum(
            [int(e['salary'][1:]) for e in self.data])/len(self.data))

    def _yearly_avg_increase(self, iage, isalary):
        average_age_increase = math.floor(
            sum([e['age'] for e in self.data])/len(self.data)) - iage
        average_salary_increase = math.floor(
            sum([int(e['salary'][1:]) for e in self.data])/len(self.data)) - \
            isalary

        return math.floor(average_salary_increase/average_age_increase)

    def _max_salary(self):
        salaries = [int(e['salary'][1:]) for e in self.data]
        threshold = '£' + str(max(salaries))

        return [e for e in self.data if e['salary'] == threshold]

    def stats(self, iage, isalary):
        data = self.data

        # Compute min salary
        salaries = [int(d['salary'][1:]) for d in data]
        min_salary = [e for e in data if e['salary'] ==
                      '£{}'.format(str(min(salaries)))]

        return json.dumps({
            'avg_age': self._age_avg(),
            'avg_salary': self._salary_avg(),
            'avg_yearly_increase': self._yearly_avg_increase(iage, isalary),
            'max_salary': self._max_salary(),
            'min_salary': min_salary
        })
