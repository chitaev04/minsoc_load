import urllib3

from locust import HttpUser, between

from requests_task.appeals import Appeals

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Demographic(HttpUser):

    wait_time = between(1, 7)
    tasks = [Appeals]
    host = "https://10.10.0.250:8443"
    # host = "https://10.10.3.66:8443"
