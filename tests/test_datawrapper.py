from unittest.mock import patch

from tdd import datawrapper as dw


def test_init():
    dw.DataWrapper()


@patch('tdd.datawrapper.RestService')
def test_datawrapper_initializes_restservice(mock_restservice):
    dw.DataWrapper()

    assert mock_restservice.called


@patch('tdd.datawrapper.RestService')
def test_datawrapper_list_calls_list_method(mock_restservice):
    w = dw.DataWrapper()
    w.list()

    assert mock_restservice().list.called
