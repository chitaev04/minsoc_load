from locust.user.task import TaskSet
from auxiliary_func import failure_task


class AssignmentRequest(TaskSet):
    """Список запросов для поручений"""

    def open_assignment_list_window(self, login):
        """Открытие поручений"""
        expected_response = 200
        with self.client.get(url="/MinsoprDocflow/docflow/order/grid.json?_dc=1660053912344&nodeType=ALL&"
                                 "dateFilter=ACTIVE&showOnlyNotRead=false&showRequests=DEFAULT&"
                                 "showForwards=DEFAULT&rootNode=allOrdersId&initGrid=true&paging=true"
                                 "&docTypeId=&typeIds=093DD5A0-15B1-41FD-B84D-A21955AA8343&"
                                 "typeIds=5CE54410-EC4F-48C1-8100-741419A3FAB5&page=1&start=0&limit=50",
                             verify=False, catch_response=True, name=f"Open_Assignment_Window -  {login}") as response:
            if response.status_code == expected_response:
                response.success()
            else:
                failure_task(self, response, error_text='Open assignment list fail')
