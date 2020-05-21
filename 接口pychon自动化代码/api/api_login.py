import requests


class Api_LE:
    def __init__(self):
        self.url = "http://ihrm-test.itheima.net"
        self.login_url = "/api/sys/login"
        self.login_url_post = self.url + self.login_url
        self.headers = {"Content-Type": "application/json"}


    def login(self,json):
        response = requests.post(url=self.login_url_post, headers=self.headers, json=json)
        return  response
















































