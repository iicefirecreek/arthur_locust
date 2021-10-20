from locust import HttpUser, TaskSet, task, between, constant
import random
import logging
import json

HEADERS = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer 3416d79aa385f344bbf8c92f95a0acb5eeff2e9c5a2ee99f381e882b60daa28f',
    'X-ENTITYID': '101507',
    'cache-control': 'no-cache',
    'Cookie': 'CAKEPHP=2gpst84qeg8o95mfdvt3s6k5ts'
}

class UserBehavior(TaskSet):  
    @task(1)
    def props(self):
        logging.info("Properties")
        with self.client.get("/ii/properties/{}".format(random.choice([102486,122913,120756,124754,124339,124360])), headers=HEADERS, catch_response=True) as response:
            print(response)

class WebsiteUser(HttpUser):
    host = "https://system.arthuronline.co.uk"
    tasks = [UserBehavior]
    wait_time = between(0.5, 3.0)