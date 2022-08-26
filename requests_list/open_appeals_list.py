import requests
from locust import TaskSet

from auxiliary_func import failure_task

from const.urls import *


class AppealsRequest(TaskSet):
    """Список запросов для обращений"""

    def open_appeal_list(self, login):
        """Открытия списка обращений"""
        expected_response = 200
        with self.client.get(OPEN_APPEALS_LIST_URL, verify=False, catch_response=True,
                             name=f"Open_Appeal_List -  {login}") \
                as response:
            if response.status_code == expected_response:
                response.success()
                return response.json()['result']
            else:
                failure_task(self, response, error_text='Open appeal list fail')

    # doc_json = {}
    # @staticmethod
    # def give_attrValue_dict():
    #     abc = attrValue
    #     return abc['attrValues']

    # @staticmethod
    # def give_docType_dict():
    #     global doc_json
    #     doc_json_full = AppealsRequest.open_appeal_create_form()
    #     doc_json = doc_json_full['docType']['content']
    #     return doc_json

    # list_mnemonics = []

    # @staticmethod
    # def search_dictionary(old_json=give_docType_dict()):
    #     print(doc_json)
    #     # doc_json_full = attrValue
    #     # doc_json = doc_json_full['docType']['content']
    #     # old_json = doc_json
    #     # print(old_json)
    #
    #     print(old_json)
    #     for i in old_json:
    #         if i['content'] in i:
    #             for j in i['content']:
    #                 search_dictionary(old_json=j)
    #         else:
    #             if i['attributeType'] in i:
    #                 if i['attributeType']['dictionary'] == True or i['attributeType']['reference '] == True:
    #                     AppealsRequest.list_mnemonics.append(i['mnemonic'])
    #     print(AppealsRequest.list_mnemonics)
