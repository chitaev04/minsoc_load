import re

from locust import TaskSet

from auxiliary_func import failure_task
from const.urls import DOCUMENT_DO_URL, LOGOUT_URL


class MainPageRequest(TaskSet):

    def open_main_page(self, login):
        """Открытие главной страницы"""
        expected_response = 200
        with self.client.get(DOCUMENT_DO_URL, verify=False, catch_response=True,
                             allow_redirects=True, name=f"Open_Main_Page - {login}") as response:
            if "logout" in response.text and response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Open main page Fail')

    def logout(self, login):
        """Выполение логаута"""
        expected_response = 200
        with self.client.get(LOGOUT_URL, name=f"LogOut - {login}", verify=False,
                             catch_response=True) as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='LogOut Fail')
        self.client.cookies.clear()
