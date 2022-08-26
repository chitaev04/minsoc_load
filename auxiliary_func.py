import datetime
import os
import random
import json

from locust.user.task import TaskSet
from const.urls import attr_value, STORAGE_URL
from request_transform import request_transform


def failure_task(self, response, error_text=None):
    print('Task fail')
    print(error_text)
    print(response.text)
    response.failure(error_text)
    TaskSet.interrupt(self)


# import requests
#
# def test_x():
#     requests.post(url='https://10.10.3.66:8443/MinsoprDocflow/docflow/storage/multiUpload?', files={'file': open('load_file.doc', 'rb')})


class DictValues(TaskSet):

    def get_dict_values(self, attribute_name, name=False):
        try:
            with self.client.get(url=attr_value(attribute_name),
                                 verify=False, catch_response=True, name='get_dict_values') as response:
                if response.json()['total'] == 0:
                    failure_task(self, response=response, error_text="Не верное имя словаря, либо словарь пустой")
                else:
                    values = response.json()['result']
        except:
            failure_task(self, response=response, error_text="Нет доступа до словаря")
        if name == True:
            return random.choice(values)['name']
        else:
            return random.choice(values)


class FileGet(TaskSet):

    def load_file(self):
        load_file = random.choice(os.listdir("load_file"))
        multipart_form_data = {'files': (load_file, open(f'load_file/{load_file}', 'rb'), 'application/msword')}
        try:
            with self.client.post(url=STORAGE_URL,
                                  verify=False, catch_response=True, name='load_file',
                                  files=multipart_form_data) as response:
                if response.json()['total'] == 0:
                    failure_task(self, response=response, error_text="Ошибка отправки файла на сервер")
                else:
                    values = response.json()['result'][0]['id']
                    return values
        except:
            failure_task(self, response=response, error_text="Нет доступа до файла")
        # if name == True:
        #     x = random.choice(values)['name']
        #     print(x)
        #     return random.choice(values)['name']
        # else:
        #     x = random.choice(values)
        #     print(x)
        #     return random.choice(values)


def request_slice2(resp=None):
    for key, value in list(resp.items()):
        if key not in ['attrValues', "project", "deleted", "read", "hasRestrictions", "activeTab",
                       "alternativeDocumentViewClass", "entityClass", "fullId", "processParams", "actionType"]:
            del resp[key]
    attrvalues = resp['attrValues']
    for key_attr, value_attr in list(attrvalues.items()):
        for key_attr_attr, value_attr_attr in list(value_attr['attr'].items()):
            if key_attr_attr not in ["name", 'attributeType']:
                del value_attr['attr'][key_attr_attr]
            if key_attr_attr == 'attributeType':
                for key_attrtype, value_attrtype in list(value_attr_attr.items()):
                    if type(value_attrtype) != bool or value_attrtype != True or key_attrtype == 'showLinkOnDocForm':
                        del value_attr['attr']['attributeType'][key_attrtype]
    print(resp)


def create_json(name, resp):
    with open(f'const/jsons/{name}.json', 'wb') as o:
        o.write(json.dumps(resp, indent=4, sort_keys=True, ensure_ascii=False).encode())


def request_slice(json_name):
    create_json(resp=request_transform, name=json_name)
    with open(f'const/jsons/{json_name}.json', 'rb') as f:
        resp = json.load(f)
    for key, value in list(resp.items()):
        if key not in ['attrValues', "project", "deleted", "read", "hasRestrictions", "activeTab",
                       "alternativeDocumentViewClass", "entityClass", "fullId", "processParams", "actionType",
                       "processAwaiting"]:
            del resp[key]
    attrvalues = resp['attrValues']
    for key_attr, value_attr in list(attrvalues.items()):
        for key_attr_attr, value_attr_attr in list(value_attr['attr'].items()):
            if key_attr_attr not in ["name", 'attributeType']:
                del value_attr['attr'][key_attr_attr]
            if key_attr_attr == 'attributeType':
                for key_attrtype, value_attrtype in list(value_attr_attr.items()):
                    if type(value_attrtype) != bool or value_attrtype != True or key_attrtype == 'showLinkOnDocForm':
                        del value_attr['attr']['attributeType'][key_attrtype]
    # print(resp)
    create_json(name=json_name, resp=resp)


# request_slice(resp=qwe)
# def request_modified(resp):
#     work_resp = request_slice(resp)
#     for key, value in work_resp.items():
#         if key == 'attrValues':
#             for key_attr, value_attr in value:
#                 pass


def random_parameter_bool():
    return random.choice([True, False])


def give_tomorrow_date():
    import datetime as DT
    from datetime import date, timedelta
    date_str = date_tomorrow = date.strftime(date.today() + timedelta(days=1), '%Y-%m-%d')
    dt = int(DT.datetime.strptime(date_str, '%Y-%m-%d').timestamp())
    return dt


# def parameter_date(key_param):
#     key_param = date.strftime(date.today(), '%d.%M.%Y')
#
#
# def parameter_dict(key_param):
#     key_param = date.strftime(date.today(), '%d.%M.%Y')
#
#
# def parameter_selection(resp):
#     work_resp = resp.copy()
#     for key, value in work_resp.items():
#         if key == 'attrValues':
#             for key_param, value_param in value:
#                 if value_param['readonly'] == False:
#                     if value_param['mandatory'] == True:
#                         if value_param['bool'] == True:
#                             work_resp['value'] = True
#                     else:
#                         if value_param['bool'] == True:
#                             parameter_bool(key_param=value_param['bool'])
#                         if value_param['date'] == True:
#                             parameter_date(key_param=value_param['date'])
#                         if value_param['dictionary'] == True:
#                             pass


if __name__ == "__main__":
    request_slice2(request_transform)
