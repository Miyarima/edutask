import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.util.dao import DAO

TEST_USER = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["firstName", "lastName", "email"],
        "properties": {
            "firstName": {
                "bsonType": "string",
                "description": "the first name of a user must be determined"
            }, 
            "lastName": {
                "bsonType": "string",
                "description": "the last name of a user must be determined"
            },
            "email": {
                "bsonType": "string",
                "description": "the email address of a user must be determined",
                "uniqueItems": True
            },
            "tasks": {
                "bsonType": "array",
                "items": {
                    "bsonType": "objectId"
                }
            }
        }
    }
}

@pytest.fixture
def sut():
    with patch("src.util.dao.getValidator", autospec=True) as mockedGetValidator:
        mockedGetValidator.return_value = TEST_USER
        sut = DAO("test_user")
        yield sut
        sut.drop()

@pytest.mark.create
def test_create_valid_user(sut):
    test_dict = {"firstName": "John", "lastName": "Doe", "email": "axel@gamil.com"}
    usr = sut.create(test_dict)
    del usr["_id"]
    assert usr == test_dict

@pytest.mark.create
def test_create_invalid_user(sut):
    test_dict = {"lastName": "Doe","email": "axel@gamil.com"}
    expected = Exception
    with pytest.raises(expected):
        sut.create(test_dict)

@pytest.mark.create
def test_create_unique_items(sut):
    test_dict = {"firstName": "John", "lastName": "Doe","email": "axel@gamil.com", "uniqueItems": "133769"}
    expected = Exception
    with pytest.raises(expected):
        usr1 = sut.create(test_dict)
        usr2 = sut.create(test_dict)

@pytest.mark.create
def test_create_bson_compliant(sut):
    test_dict = {"firstName": "John", "lastName": "Doe","email": "axel@gamil.com", "test": 1337}
    expected = Exception
    with pytest.raises(expected):
        usr = sut.create(test_dict)
