import pytest
import unittest.mock as mock

# from src.util.helpers import hasAttribute, ValidationHelper
from src.controllers.usercontroller import emailValidator, UserController

@pytest.fixture
def sut(email: str):
    mockedusercontroller = mock.MagicMock()
    mockedusercontroller.dao.find.return_value = {'email': email}
    mockedsut = UserController(usercontroller=mockedusercontroller)
    return mockedsut

@pytest.mark.lab1
@pytest.mark.parametrize('obj, expected', [({'email': 'Janedoe@example.com'}, "Janedoe@example.com")])
def test_valid_email(sut, expected):
    # assert hasAttribute(obj, 'name') == expected
    validationresult = sut.get_user_by_email(email=None)
    assert validationresult == expected


# @pytest.fixture
# def sut():
#     mocked_user_controller = MagicMock()
#     mocked_user_controller.dao.find.return_value = {'email': 'Janedoe@example.com'}
#     mocked_sut = UserController(usercontroller=mocked_user_controller)
#     return mocked_sut

# @pytest.mark.lab1
# @pytest.mark.parametrize('email, expected_email', [('Janedoe@example.com', 'Janedoe@example.com')])
# def test_valid_email(sut, email, expected_email):
#     validation_result = sut.get_user_by_email(email=email)
#     assert validation_result['email'] == expected_email



# tests for the hasAttribute method
# @pytest.mark.demo
# @pytest.mark.parametrize('obj, expected', [({'name': 'Jane'}, True), ({'email': 'jane.doe@gmail.com'}, False), (None, False)])
# def test_hasAttribute_true(obj, expected):
#     assert hasAttribute(obj, 'name') == expected


# # tests for the validateAge method
# @pytest.fixture
# def sut(age: int):
#     mockedusercontroller = mock.MagicMock()
#     mockedusercontroller.get.return_value = {'age': age}
#     mockedsut = ValidationHelper(usercontroller=mockedusercontroller)
#     return mockedsut

# @pytest.mark.demo
# @pytest.mark.parametrize('age, expected', [(-1, 'invalid'), (0, 'underaged'), (1, 'underaged'), (17, 'underaged'), (18, 'valid'), (19, 'valid'), (119, 'valid'), (120, 'valid'), (121, 'invalid')])
# def test_validateAge(sut, expected):
#     validationresult = sut.validateAge(userid=None)
#     assert validationresult == expected
