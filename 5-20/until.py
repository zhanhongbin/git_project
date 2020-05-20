import json


class Ass_ERT:
    def ass_in(self,ept_results,atl_results,Self):
        Self.assertIn(ept_results,atl_results)

    def ass_equal(self,ept_results,atl_results,Self):
        Self.assertEqual(ept_results, atl_results)


class Assert_Operating:
    def __init__(self):
        self.ass = Ass_ERT()

    def login_eq_status(self,status_code,response,Self):
        # 断言响应码200
        response_1 = response.status_code
        self.ass.ass_equal(status_code,response_1,Self)


    def login_eq_success(self,success,response,Self):
        #断言success
        response_2 = response.json().get("success")
        self.ass.ass_equal(success,response_2,Self)


    def login_eq_code(self,code,response,Self):
        #断言code
        response_3 =response.json().get("code")
        self.ass.ass_equal(code, response_3, Self)


    def login_in_message(self,login_in_message,response,Self):
        # 断言message
        response_4 = response.json().get("message")
        self.ass.ass_in(login_in_message,response_4,Self)



class Ass_Operating:
    def __init__(self):
        self.ass_oper = Assert_Operating()

    def asslogin(self,status_code,success,code,message,response,Self):
        # 登录模块断言
        self.ass_oper.login_eq_status(status_code,response,Self)
        self.ass_oper.login_eq_success(success,response,Self)
        self.ass_oper.login_eq_code(code,response,Self)
        self.ass_oper.login_in_message(message,response,Self)





def j_file(filename):
    data = list()
    with open(filename,"r",encoding="utf-8") as f:
        jda = json.load(f)
        for i in jda.values():
            data.append(i.values())
    return data












