from model.project import Project
import random


def test_delete_some_group(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(id=None, name="name", description="description"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)