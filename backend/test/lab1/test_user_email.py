import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.mark.email
@pytest.mark.parametrize('email, expected', [({'email': 'Janedoe@example.com'}, 'Janedoe@example.com')])
def test_valid_email(email, expected):
    mocked_usercontroller = mock.MagicMock()
    mocked_usercontroller.find.return_value = [email]
    sut = UserController(mocked_usercontroller)
    valid_result = sut.get_user_by_email('Janedoe@example.com')
    assert valid_result["email"] == expected

@pytest.mark.email
@pytest.mark.parametrize('email, expected', [([{'id': 28, 'name': 'Axel', 'email': 'Janedoe@example.com'},
    {'id': 42, 'name': 'Jonathan', 'email': 'Janedoe@example.com'},
    {'id': 69, 'name': 'Charlie', 'email': 'Janedoe@example.com'}], {'id': 28, 'name': 'Axel', 'email': 'Janedoe@example.com'})])
def test_multiple_valid_emails(email, expected):
    mocked_usercontroller = mock.MagicMock()
    mocked_usercontroller.find.return_value = email
    sut = UserController(mocked_usercontroller)
    valid_result = sut.get_user_by_email('Janedoe@example.com')
    assert valid_result == expected

@pytest.mark.email
@pytest.mark.parametrize('email, expected', [({}, None)])
def test_no_user_associated(email, expected):
    mocked_usercontroller = mock.MagicMock()
    mocked_usercontroller.find.return_value = email
    sut = UserController(mocked_usercontroller)
    valid_result = sut.get_user_by_email('Janedoe@example.com')
    assert valid_result == expected

@pytest.mark.email
@pytest.mark.parametrize('email, expected', [({'email': 'Janedoeexample.com'}, ValueError)])
def test_invalid_email(email, expected):
    mocked_usercontroller = mock.MagicMock()
    sut = UserController(mocked_usercontroller)
    with pytest.raises(expected):
        sut.get_user_by_email(email["email"])
