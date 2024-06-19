import unittest

from klasy.auth import Authentication


def do_something():
    return "coś robię..."


def addition(a, b):
    return a + b


class MyTestCase(unittest.TestCase):

    def test_something(self):
        result = do_something()
        assert result == "coś robię"

    def test_main(self):
        result = addition(3, 2)
        assert result == 5

    def test_one(self):
        pass

    def test_two(self):
        pass


class MySecondTestCase(unittest.TestCase):
    def test_3(self):
        pass

    def test_4(self):
        pass


class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser",
                       "password": "testpass"}]
        resp = auth.login("testuser", "testpass")
        assert resp == {"username": "testuser",
                         "password": "testpass"}


if __name__ == '__main__':
    unittest.main()
