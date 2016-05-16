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
def test_delete_some_group(app, project):
    (username, password) = app.config["webadmin"]["username"], app.config["webadmin"]["password"]
    app.session.login(username, password)
    if len(app.project.get_project_list_via_soap(username, password)) == 0:
        app.project.create(project)
    old_projects = app.project.get_project_list_via_soap(username, password)
    project = choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = app.project.get_project_list_via_soap(username, password)
    assert len(old_projects) - 1 == len(new_projects)