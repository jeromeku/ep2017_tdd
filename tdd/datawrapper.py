from tdd.dictregister import DictRegister
from tdd.rest_service import RestService


class DataWrapper:

    def __init__(self):
        self.rest = RestService()

    def list(self, **kwds):
        dr = DictRegister(self.rest.list())

        return dr.find(**kwds)

    def get(self, elem_id):
        return self.rest.get(elem_id)
