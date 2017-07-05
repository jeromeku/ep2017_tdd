from tdd.rest_service import RestService


class DataWrapper:

    def __init__(self):
        self.rest = RestService()

    def list(self):
        return self.rest.list()

    def get(self, elem_id):
        return self.rest.get(elem_id)
