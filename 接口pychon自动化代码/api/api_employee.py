import requests
import app

class Api_employee:

    def __init__(self):
        self.url = "http://ihrm-test.itheima.net"
        self.employee_url = self.url +"/api/sys/user"

    def employee_add(self, token,username,mobile):
        # 添加员工
        app.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(url=self.employee_url,
                                 headers=app.headers,
                                 json={
                                     "username": username,
                                     "mobile": mobile,
                                     "timeOfEntry": "2020-05-05",
                                     "formOfEmployment": 1,
                                     "workNumber": "1234123",
                                     "departmentName": "测试部",
                                     "departmentId": "1063678149528784896",
                                     "correctionTime": "2020-05-17T16:00:00.000Z"
                                 })
        app.emp_id = response.json().get("data").get("id")
        return response

    def employee_Inquire(self):
        # 查询员工
        app.employee_url_id = self.employee_url + "/" + app.emp_id
        response = requests.get(url=app.employee_url_id,headers=app.headers)
        return response



    def employee_modify(self,json):
        # 修改日子
        response = requests.put(url=app.employee_url_id,headers=app.headers,
                                json=json)

        return response

    def employee_delete(self):
        # 删除
        response = requests.delete(url=app.employee_url_id,headers=app.headers)

        return response

























