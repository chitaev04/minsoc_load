import random

from locust import task

from auxiliary_func import DictValues
from const.department.social_protection_of_the_population import REGISTRAR_PROTECTION, AUTHOR_RESOLUTION_PROTECTION, \
    EXECUTOR_PROTECTION, SIGNATORY_PROTECTION, CONTROLLER_PROTECTION
from requests_list.auth import LoginPageRequest
from requests_list.main_page import MainPageRequest
from requests_list.open_appeals_list import AppealsRequest
from requests_list.create_appeal import CreateAppeal


class Appeals(LoginPageRequest, MainPageRequest, AppealsRequest, CreateAppeal, DictValues):

    @task
    def open_appeal_list(self):
        # Создание документа регистратором
        login = random.choice(REGISTRAR_PROTECTION)
        self.login(login)
        self.open_main_page(login)
        self.give_appeal_doc_id(login)
        self.open_appeal_create_form(login)
        self.registration_write_appeal_content_additions(login)
        self.registration_write_appeal_save_additions(login)
        self.get_question_id(login)
        self.registration_write_appeal_registration(login)
        self.logout(login)
        ## Отправление на резолюцию (добавляется только к одному содержанию)
        login = random.choice(AUTHOR_RESOLUTION_PROTECTION)
        self.login(login)
        self.open_main_page(login)
        self.open_appeal(login)
        self.ask_resolution(login)
        self.logout(login)
        # Принятие к исполнению
        login = random.choice(EXECUTOR_PROTECTION)
        self.login(login)
        self.open_main_page(login)
        self.open_res_appeal(login)
        self.get_isp(login)
        self.open_isp_page(login, act=0)
        self.accept_for_execution(login)
        # Исполнение
        self.open_isp_page(login, act=1)
        self.execution(login)
        self.logout(login)
        # Согласование
        login = random.choice(SIGNATORY_PROTECTION)
        self.login(login)
        self.open_main_page(login)
        self.open_agreement(login)
        self.agreement(login)
        self.logout(login)
        # # Снятие с контроля
        login = random.choice(CONTROLLER_PROTECTION)
        self.login(login)
        self.open_main_page(login)
        self.open_appeal(login)
        self.drop_from_control(login)
        self.logout(login)


