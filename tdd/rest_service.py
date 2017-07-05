import json
import time

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Example JSON element
# {
#     'age': 20,
#     'surname': 'Frazier',
#     'name': 'Leonard',
#     'salary': '£28943'
# }
#
# 'age' goes from 18 to 70
# 'salary' goes from 20000 to 90000


class RestService:

    def __init__(self):
        with open(os.path.join(dir_path, 'data.json')) as f:
            self.data = {}
            for elem in json.load(f):
                elem_id = elem.pop('id')
                self.data[elem_id] = elem

    def list(self):
        time.sleep(3)
        return self.data

    def get(self, elem_id):
        time.sleep(3)
        return self.data[elem_id]


if __name__ == '__main__':
    r = RestService()
    print(r.get(4))
