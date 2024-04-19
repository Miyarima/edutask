import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.util.dao import DAO

@pytest.fixture
def sut():
    dao_class = DAO("user")
    test_dict = {"firstName": "John", "lastName": "Doe","email": "axel@gamil.com"}
    usr = dao_class.create(test_dict)
    yield usr
    dao_class.delete(usr["_id"]["$oid"])

@pytest.mark.lab1
@pytest.mark.parametrize('expected', [({"firstName": "John", "lastName": "Doe","email": "axel@gamil.com"})])
def test_create_valid_user(sut, expected): 
    test_dict = sut.copy()
    del test_dict["_id"]
    assert test_dict == expected

@pytest.mark.lab1
@pytest.mark.parametrize('test_dict, expected', [({"lastName": "Doe","email": "axel@gamil.com"}, Exception)])
def test_create_invalid_user(test_dict: dict, expected): 
    dao_class = DAO("user")
    with pytest.raises(expected):
        usr = dao_class.create(test_dict)
        dao_class.delete(usr["_id"]["$oid"])

@pytest.mark.lab1
@pytest.mark.parametrize('test_dict, expected', [({"firstName": "John", "lastName": "Doe","email": "axel@gamil.com", "uniqueItems": "133769"}, Exception)])
def test_create_unique_items(test_dict: dict, expected): 
    dao_class = DAO("user")
    with pytest.raises(expected):
        usr_1 = dao_class.create(test_dict)
        usr_2 = dao_class.create(test_dict)

        dao_class.delete(usr_1["_id"]["$oid"])
        dao_class.delete(usr_2["_id"]["$oid"])

@pytest.mark.lab1
@pytest.mark.parametrize('test_dict, expected', [({"firstName": "John", "lastName": "Doe","email": "axel@gamil.com", "test": 1337}, Exception)])
def test_create_bson_complyant(test_dict: dict, expected): 
    dao_class = DAO("user")
    with pytest.raises(expected):
        usr = dao_class.create(test_dict)
        dao_class.delete(usr["_id"]["$oid"])
