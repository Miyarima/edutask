import pytest
import unittest.mock as mock

from src.util.helpers import hasAttribute, ValidationHelper
from src.controllers.usercontroller import UserController
from src.util.dao import DAO


# @pytest.mark.lab1
# def test_to_see_if_it_works_with_out_code_just_to_test_delete_later_or_keep_its_up_to_you_any_way():
#     obj = {"name", "joe"}
#     result = hasAttribute(obj, "name")
#     assert result == True


# @pytest.fixture
# def obj():
#     return {"name", "joe"}

# def test_has_name(obj):
#     result = hasAttribute(obj, "name")
#     assert result == True

# def test_has_not_email(obj):
#     result = hasAttribute(obj, "email")
#     assert result == False

# def test_has_joe(obj):
#     result = hasAttribute(obj, "joe")
#     assert result == True

###

# Result code
@pytest.mark.lab1
@pytest.mark.parametrize('email, expected', [({'email': 'Janedoe@example.com'}, {'email': 'Janedoe@example.com'})])
def test_valid_email(email, expected):
    mocked_usercontroller = mock.MagicMock()
    mocked_usercontroller.find.return_value = [email]
    sut = UserController(mocked_usercontroller)
    valid_result = sut.get_user_by_email('Janedoe@example.com')
    assert valid_result == expected

@pytest.mark.lab1
@pytest.mark.parametrize('email, expected', [({'email': 'Janedoeexample.com'}, ValueError)])
def test_invalid_email(email, expected):
    mocked_usercontroller = mock.MagicMock()
    sut = UserController(mocked_usercontroller)
    with pytest.raises(expected):
        sut.get_user_by_email(email["email"])

## Not working as intended
@pytest.mark.lab1
@pytest.mark.parametrize('email, expected', [([{'id': 1, 'name': 'John', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 3, 'name': 'Bob', 'email': 'Janedoe@example.com'}], {'id': 3, 'name': 'Bob', 'email': 'Janedoe@example.com'})])
def test_multiple_valid_emails(email, expected):
    mocked_usercontroller = mock.MagicMock()
    mocked_usercontroller.find.return_value = email
    sut = UserController(mocked_usercontroller)
    valid_result = sut.get_user_by_email('Janedoe@example.com')
    assert valid_result == expected
###
