from locust import HttpUser, TaskSet, task, between, constant
import random
import logging
import json

HEADERS = {
    'Authorization': 'Bearer e689bac03864fe06730ed093371da40a9e32c5be1d738d20f02b35243de32918',
    'X-ENTITYID': '101507',
    'cache-control': 'no-cache',
    'Cookie': 'ingress=fa163c74fcc9ff5cfb51bf7cab516eb8; CAKEPHP=3gr5u2vqcloi8eour2pl9p43dj',
    'Content-type': 'application/json'
}

class UserBehavior(TaskSet):  
    @task(1)
    def props(self):
        logging.info("Properties")
        with self.client.get("/v2/properties/{}".format(random.choice([107506,102486,106788,106504,107270,107212,107215,106414,106490,106680,106417,107631])), headers=HEADERS, catch_response=True) as response:
            print(response)

class WebsiteUser(HttpUser):
    # host = "https://api-staging.arthuronline.co.uk"
    host = "https://auth-staging.arthuronline.co.uk/oauth/token"
    tasks = [UserBehavior]
    wait_time = between(0.5, 3.0)