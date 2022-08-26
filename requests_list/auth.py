import random
import time

import lxml
import lxml.html
import urllib3
from locust import TaskSet

from auxiliary_func import failure_task
from const.urls import AUTH_PAGE_URL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class LoginPageRequest(TaskSet):

    def open_auth_page(self):
        """Открытие главное страницы для получения значния ключа 'Keycloak'"""
        self.client.cookies.clear()
        expected_response = 200
        with self.client.get(AUTH_PAGE_URL, verify=False, catch_response=True, allow_redirects=True,
                             name="Open_Auth_Page") as response:
            if response.status_code == expected_response:
                response.success()
                # Получение session_code
                tree = lxml.html.fromstring(response.text)
                title_elem = tree.cssselect('[id="kc-form-login"]')[0].attrib['action']
            else:
                failure_task(self, response, error_text='Open Auth Page Fail')
        return title_elem

    def login(self, login):
        time.sleep(random.randint(1,10))
        """Выполнение авторизации пользователя"""
        expected_response = 200
        with self.client.post(self.open_auth_page(), data={'username': f'{login}',
                                                           'password': f'{login}', 'credentialId': '',
                                                           'clientId': "minsopr-app",
                                                           'clientSecret': '9cf21c5a-2893-4292-be78-680bb80fb765'},
                              verify=False, catch_response=True, allow_redirects=True,
                              name=f"Login_success -  {login}") as response:
            if 'login?error' not in response.url and response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Auth fail')
            print("Логин пользователя =" + login)