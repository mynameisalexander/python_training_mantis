# -*- coding: utf-8 -*-
from model.project import Project
from random import *
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])

testdata = [
    Project(name=random_string('name', 10), description=random_string('name', 100))
]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_additional_project(app, project):
    app.session.login(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(new_projects) == len(old_projects)+1
