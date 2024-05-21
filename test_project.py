from project import welcome_verification, admin, schema
from views import check_database, check_user_input, check_name
from registration import check_age
from models import boys
import pytest

def test_check_age(mocker):
    mocker.patch('builtins.input', return_value='25')  # Replace '25' with the desired input
    result = check_age()
    assert result == 25

def test_check_database():
    bash = [30, "athletic", "tall", "slim", "fair", "12345bash"]
    assert check_database(boys, bash) == ["Bash"]

def test_check_user_input(monkeypatch):
    user_input = "yes"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    test_str = "Yes or no: "
    test_lst = ["yes", "no"]
    result = check_user_input(test_str, test_lst)
    assert result == user_input
    assert result in test_lst

def test_check_name(monkeypatch):
    user_input = "Bash"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert check_name(user_input) == True


def test_welcome_verification(mocker):
    mocker.patch('builtins.input', return_value='25')
    with mocker.patch('project.register', side_effect=lambda user_age: 'boy'):
        result = welcome_verification()
    assert result == 'boy'

def test_admin():
    assert admin() == 0

def test_schema():
    assert schema() == 0


if __name__ == '__main__':
    pytest.main()
