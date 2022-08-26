import random

from locust import task

from const.department.social_protection_of_the_population import *
from requests_list.auth import LoginPageRequest
from requests_list.main_page import MainPageRequest


class LoginRegistrar(LoginPageRequest, MainPageRequest):

    @task
    def login_registrar(self):
        self.login(login=random.choice(REGISTRAR_PROTECTION))
        self.open_main_page()
        self.logout()



