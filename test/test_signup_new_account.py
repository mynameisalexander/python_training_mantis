from random import *
import string


def random_username(prefix, maxlen):
    symbols = string.ascii_letters + string.digits*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])

def test_signup_new_account(app):
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = "test"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)
