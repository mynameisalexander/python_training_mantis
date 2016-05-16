from model.project import Project
from fixture.soap import *
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
        url = self.app.config["web"]["baseUrl"]
        wd.get(url+"/manage_proj_page.php")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.open_project_page()
        url = self.app.config["web"]["baseUrl"]
        wd.get(url+'/manage_proj_edit_page.php?project_id='+str(project[0]))
        # submit deletion
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()

    def get_project_list(self):
        db_connection = self.app.config['dbconnection']
        connection = mysql.connector.connect(
            host=db_connection["host"], database=db_connection["database"], user=db_connection["user"], password=db_connection["password"])
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `mantis_project_table`;")
        projects = []
        for row in cursor:
            projects.append(row)
        connection.close()
        return projects

    def get_project_list_via_soap(self, username, password):
        url = self.app.config["web"]["baseUrl"]
        client = Client(url+"/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_projects_get_user_accessible(username, password)