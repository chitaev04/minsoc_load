from locust import TaskSet

from auxiliary_func import failure_task
from const.payload.appeal_registration_payload import *
from const.urls import CREATE_APPEAL_FORM_URL, appeal_doc_id_url, registration_appeal_write_url, get_isp_id, get_sogl
from auxiliary_func import FileGet


class CreateAppeal(DictParametrs, FileGet, TaskSet):
    def give_appeal_doc_id(self, login):
        """Получение doc_id для открытия окна создания обращения. Письменное"""
        global doc_id
        expected_response = 201
        with self.client.post(CREATE_APPEAL_FORM_URL,
                              json={"inquiryType": "Письменное"}, verify=False, catch_response=True,
                              name=f'Give_Appeal_doc_id -  {login}') as response:
            if response.status_code == expected_response:
                response.success()
                doc_id = response.json()["id"]
            else:
                failure_task(self, response, error_text='Give appeal doc_id fail')

    def open_appeal_create_form(self, login):
        """Открытие формы создания обращения"""
        global processInstanceId, historyId, connectionId, connectionIdVerbal, nextBlockId, \
            nextBlockIdVerbal, attrValue
        expected_response = 200
        with self.client.get(appeal_doc_id_url(doc_id),
                             verify=False, catch_response=True, name=f'Open_Appeal_Create_Form -  {login}') as response:
            if response.status_code == expected_response:
                attrValue = response.json()
                response.success()
                processInstanceId = response.json()['processAwaiting']['processInstanceId']
                historyId = response.json()['processAwaiting']['variants'][0]['historyId']
                connectionId = response.json()['processAwaiting']['variants'][1]['connectionId']
                nextBlockId = response.json()['processAwaiting']['variants'][1]['nextBlockId']
                if len(response.json()['processAwaiting']['variants']) >= 3:
                    connectionIdVerbal = response.json()['processAwaiting']['variants'][2]['connectionId']
                    nextBlockIdVerbal = response.json()['processAwaiting']['variants'][2]['nextBlockId']
                return attrValue
            else:
                failure_task(self, response, error_text='Open appeal create form fail')

    def registration_write_appeal_content_additions(self, login):
        """Регистрация письменного обращения. Добавления содержания"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id), json=self.registration_body_content_additions(),
                             verify=False, catch_response=True, name=f"Registration Add Content - {login}") as \
                response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Registration step1 appeal fail')

    def registration_write_appeal_save_additions(self, login):
        """Регистрация письменного обращения. Сохранение содержания в обращении"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id),
                             json=self.registration_body_save_additions(),
                             verify=False, catch_response=True, name=f"Save Content - {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                print(response.text)
                failure_task(self, response, error_text='Registration step2 appeal fail')

    def get_question_id(self, login):
        """Открытие формы обращения для получения question_id"""
        global attrValue, question_id
        expected_response = 200
        with self.client.get(appeal_doc_id_url(doc_id),
                             verify=False, catch_response=True, name=f'Get question id -  {login}') as response:
            if response.status_code == expected_response:
                attrValue = response.json()
                response.success()
                inquiryQuestionList = attrValue['attrValues']['inquiryQuestionList']['value'].items()
                question_id = {'question_id': value['inquiryQuestion']['id'] for key, value in inquiryQuestionList}[
                    'question_id']
                return attrValue
            else:
                failure_task(self, response, error_text='Open appeal create form fail')

    def registration_write_appeal_registration(self, login):
        """Регистрация письменного обращения"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id),
                             json=self.registration_body_registration(processInstanceId, historyId,
                                                                      connectionId),
                             verify=False, catch_response=True, name=f"Registration appeal -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text=f'Registration step3 appeal fail')

    def open_appeal(self, login):
        """Открытие обращения"""
        global processInstanceId_res, historyId_res, connectionId_res, nextBlockId_res
        expected_response = 200
        with self.client.get(url=appeal_doc_id_url(doc_id), verify=False, catch_response=True,
                             name=f"Open_appeal - {login}") as response:
            if response.status_code == expected_response:
                response.success()
                processInstanceId_res = response.json()['processAwaiting']['processInstanceId']
                historyId_res = response.json()['processAwaiting']['variants'][0]['historyId']
                connectionId_res = response.json()['processAwaiting']['variants'][0]['connectionId']
                nextBlockId_res = response.json()['processAwaiting']['variants'][0]['nextBlockId']

            else:
                failure_task(self, response, error_text='Open appeal fail')

    def ask_resolution(self, login):
        """Задать резолюцию и исполнителей"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id),
                             json=self.ask_resolution_body(processInstanceId_res, historyId_res, connectionId_res,
                                                           question_id),
                             verify=False, catch_response=True, name=f"Ask Resolution -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Ask_Resolution_Fail')

    def open_res_appeal(self, login):
        """Открытие резолюции"""
        expected_response = 200
        with self.client.get(url=appeal_doc_id_url(doc_id), verify=False, catch_response=True,
                             name=f"Open_Res - {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Open res fail')

    def get_isp(self, login):
        """Открытиые окна исполнения"""
        global resp_id
        expected_response = 200
        with self.client.get(url=get_isp_id(doc_id), verify=False, catch_response=True, name='Get resp_id') as response:
            if response.status_code == expected_response:
                response.success()
                resp_id = response.json()[0]['id']
            else:
                failure_task(self, response, error_text='Open res fail')

    def open_isp_page(self, login, act):
        """Открытие окна исполнения"""
        global processInstanceId_isp, historyId_isp, connectionId_isp, nextBlockId_isp
        expected_response = 200
        with self.client.get(url=appeal_doc_id_url(resp_id),
                             verify=False, catch_response=True, name=f"Open isp page -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
                processInstanceId_isp = response.json()['processAwaiting']['variants'][act]['processInstanceId']
                historyId_isp = response.json()['processAwaiting']['variants'][act]['historyId']
                connectionId_isp = response.json()['processAwaiting']['variants'][act]['connectionId']
                nextBlockId_isp = response.json()['processAwaiting']['variants'][act]['nextBlockId']
            else:
                failure_task(self, response, error_text='Accept_For_Execution_Fail')

    def accept_for_execution(self, login):
        """Принять к исполнению"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(resp_id),
                             json=self.accept_for_execution_body(processInstanceId=processInstanceId_isp, historyId=historyId_isp, connectionIdWriting=connectionId_isp,
                                                                 nextBlockId=nextBlockId_isp),
                             verify=False, catch_response=True, name=f"Ask For Execution -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Accept_For_Execution_Fail')

    def execution(self, login):
        """Исполнение"""
        expected_response = 200
        file_id = self.load_file()
        with self.client.put(url=registration_appeal_write_url(resp_id),
                             json=self.execution_body(processInstanceId=processInstanceId_isp, historyId=historyId_isp,
                                                      connectionIdWriting=connectionId_isp,
                                                      file_id=file_id),
                             verify=False, catch_response=True, name=f"Execution -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Accept_For_Execution_Fail')

    def open_agreement(self, login):
        """Открытие окна согласования"""
        global processInstanceId, historyId, connectionId
        expected_response = 200
        with self.client.get(url=get_sogl(doc_id),
                             verify=False, catch_response=True, name=f'Open_agreement -  {login}') as response:
            if response.status_code == expected_response:
                response.success()
                processInstanceId = response.json()['processAwaiting']['processInstanceId']
                historyId = response.json()['processAwaiting']['variants'][0]['historyId']
                connectionId = response.json()['processAwaiting']['variants'][0]['connectionId']
            else:
                failure_task(self, response, error_text='Open_agreement_Fail')

    def agreement(self, login):
        """Согласование"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id),
                             json=self.body_agreement(processInstanceId, historyId,
                                                      connectionId),
                             verify=False, catch_response=True, name=f"Agreement -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text=f'Agreement fail')

    def drop_from_control(self, login):
        """Снятие с контроля"""
        expected_response = 200
        with self.client.put(url=registration_appeal_write_url(doc_id),
                             json=self.drop_control(processInstanceId_res, historyId_res,
                                                      connectionId_res),
                             verify=False, catch_response=True, name=f"drop_from_control -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text=f'drop from control fail')
