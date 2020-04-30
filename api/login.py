import requests, logging
import apiConfig

"""自媒体登录"""


class MpLogin:

    def __init__(self):
        # 登录url
        self.mp_login_url = apiConfig.mp_host_url + "/authorizations"

    def login(self, mobile, code):
        """
        自媒体登录
        :param mobile: 手机号
        :param code: 验证码
        :return: 登录响应对象
        """
        # 登录请求体
        mp_login_body = {"mobile": mobile, "code": code}
        logging.info("自媒体登录地址:{}".format(self.mp_login_url))
        logging.info("自媒体登录body:{}".format(mp_login_body))
        # 发起登录请求
        return requests.post(self.mp_login_url, json=mp_login_body, headers=apiConfig.mp_login_header)


"""后台登录"""


class MisLogin:
    def __init__(self):
        # 后台登录地址
        self.mis_login_url = apiConfig.mis_host_url + "/authorizations"

    def login(self, account, password):
        """后台管理登录"""

        # 登录body
        mis_login_body = {"account": account, "password": password}
        logging.info("后台管理登录地址:{}".format(self.mis_login_url))
        logging.info("后台管理登录body:{}".format(mis_login_body))
        # 发起请求
        return requests.post(self.mis_login_url, json=mis_login_body, headers=apiConfig.mis_header)


"""app登录"""


class AppLogin:
    def __init__(self):
        # app登录地址
        self.app_login_url = apiConfig.app_host_url + "/authorizations"

    def login(self, mobile, code):
        """
        app登录
        :param mobile: 手机号
        :param code: 验证码
        :return:
        """
        # 请求body
        app_login_body = {"mobile": mobile, "code": code}
        logging.info("app登录地址:{}".format(self.app_login_url))
        logging.info("app登录body:{}".format(app_login_body))
        # 请求方法
        return requests.post(self.app_login_url, json=app_login_body, headers=apiConfig.app_header)
