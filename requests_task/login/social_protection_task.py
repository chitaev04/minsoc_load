import random

from locust import task

from const.department.social_protection_of_the_population import *
from requests_list.auth import LoginPageRequest


class LoginRegistrar(LoginPageRequest):

    @task
    def login_registrar(self):
        self.login(login=random.choice(REGISTRAR_PROTECTION))


class LoginAuthorResolution(LoginPageRequest):

    @task
    def login_author_resolution(self):
        self.login(login=random.choice(AUTHOR_RESOLUTION_PROTECTION))


class LoginExecutor(LoginPageRequest):

    @task
    def login_executor(self):
        self.login(login=random.choice(EXECUTOR_PROTECTION))


class LoginSignatory(LoginPageRequest):

    @task
    def login_signatory(self):
        self.login(login=random.choice(SIGNATORY_PROTECTION))


class LoginController(LoginPageRequest):

    @task
    def login_controller(self):
        self.login(login=random.choice(CONTROLLER_PROTECTION))
