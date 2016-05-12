from model.project import Project
import mysql.connector


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        # init group creation
        self.fill_group_form(project)
        # add project
        wd.find_element_by_css_selector("input.button").click()

    def fill_group_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/mantisbt-1.2.19/manage_proj_page.php")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.get('http://localhost:8080/mantisbt-1.2.19/manage_proj_edit_page.php?project_id='+str(project[0]))
        # submit deletion
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()

    def get_project_list(self):
        connection = mysql.connector.connect(host="127.0.0.1", database="bugtracker", user="root", password="")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `mantis_project_table`;")
        projects = []
        for row in cursor:
            projects.append(row)
        connection.close()
        return projects