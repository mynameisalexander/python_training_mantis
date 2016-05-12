# -*- coding: utf-8 -*-
from model.project import Project


def test_additional_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(Project(id=None, name="name", description="description"))
    new_projects = app.project.get_project_list()
    assert new_projects == old_projects