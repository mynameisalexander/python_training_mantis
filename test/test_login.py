def test_login(app):
    app.session.login(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    assert app.session.is_logged_in_as(app.config["webadmin"]["username"])