from faker import Faker
from unittest.mock import patch
from main.services.access_control_sv import AccessControlSv

fake = Faker()
sut = AccessControlSv()


def test_login_false():
    result = sut.login(
        username=fake.word(),
        password=fake.word(),
    )
    assert result is False


@patch.object(AccessControlSv, "_set_user_session", return_value=None)
@patch.object(AccessControlSv, "_check_password", return_value=True)
def test_login_true(_check_password, _set_user_session):
    username = fake.word()
    password = fake.word()
    result = sut.login(username, password)
    assert result is True
