import apiConfig
import pytest,logging
from api.apiFactory import ApiFactory
# 导入通用断言方法
from utils.assert_common import assert_common
from utils.analysisData import AnalysisData


def get_data():
    """组装测试数据 --只演示登录数据"""
    # 预期结果列表 [(),()]
    mp_login_list = []
    # 读yaml文件数据
    data = AnalysisData.get_yml_data("pub_article.yml")
    # 遍历 组装元素
    for i in data.get("PubArticle").get("mp_login").values():
        mp_login_list.append(tuple(i.values()))
    return mp_login_list


class TestPublishArticle:
    """发文章测试用例"""
    # 文章标题
    title = "红茶绿茶还有什么茶"
    # 文章id
    article_id = None
    # 渠道id
    channel_id = 1

    @pytest.mark.parametrize("mobile, code, status_code, message", get_data())
    def test_mp_login(self, mobile, code, status_code, message):
        """
        自媒体登录
        :param mobile: 手机号
        :param code: 验证码
        :param status_code: 预期响应状态码
        :param message: 预期响应message
        :return:
        """
        # 登录操作
        res = ApiFactory.get_mp_login().login(mobile, code)

        logging.info("自媒体登录返回数据:{}".format(res.json()))

        # # 断言 -状态码 和 message
        assert_common(res, status_code, message)
        # 保存token Bearer+空格+token
        apiConfig.mp_login_header["Authorization"] = "Bearer " + res.json().get("data").get("token")
        # print("\n添加登录token后header:{}".format(apiConfig.mp_login_header))

    def test_mp_publish_article(self):
        """自媒体发布文章接口"""
        # 标题
        title = TestPublishArticle.title
        # 内容
        content = "红茶绿茶还有什么茶红茶绿茶还有什么茶"
        # 渠道 1:html10渠道
        channel_id = TestPublishArticle.channel_id
        # 请求发布文章
        res = ApiFactory.get_mp_publish_article().mp_publish_article(title, content, channel_id)

        logging.info("自媒体发布文章返回数据:{}".format(res.json()))

        # # 断言 -状态码 和 message
        assert_common(res, 201)
        # 断言文章id存在
        assert res.json().get("data").get("id") > 0

    def test_mis_login(self):
        """后台管理登录"""
        # 账号
        account = "testid"
        # 密码
        password = "testpwd123"
        # 登录请求
        res = ApiFactory.get_mis_login().login(account, password)

        logging.info("后台管理登录返回数据:{}".format(res.json()))

        # 断言 响应状态码 和 message
        assert_common(res, 201)
        # 保存token
        apiConfig.mis_header["Authorization"] = "Bearer " + res.json().get("data").get("token")
        # print("\n最新后台登录头信息:{}".format(apiConfig.mis_header))

    def test_mis_query_article(self):
        """后台管理查询文章接口"""
        # 文章名字
        title = TestPublishArticle.title
        # 渠道名字
        channel = "html"
        # 请求
        res = ApiFactory.get_mis_article().query_article(title, channel)

        logging.info("后台管理查询文章返回数据:{}".format(res.json()))

        # 断言 状态码 和 message
        assert_common(res)
        # 保存文章id -审核文章接口请求body使用
        TestPublishArticle.article_id = res.json().get("data").get("articles")[0].get("article_id")
        # print("\n文章id:{}".format(TestPublishArticle.article_id))

    def test_mis_audit_article(self):
        """后台管理审核文章接口"""
        # 文章id
        article_id = TestPublishArticle.article_id
        # 审核状态 文章发布后就是审核状态 所以本次会报错
        status = 2
        # 审核文章请求
        res = ApiFactory.get_mis_article().audit_article(article_id, status)

        logging.info("后台管理审核文章返回数据:{}".format(res.json()))

        # 断言 状态码 和 message
        assert_common(res, 201)

    def test_app_login(self):
        """app登录测试"""
        # 手机号
        mobile = "13911111111"
        # 验证码
        code = "246810"
        # 请求
        res = ApiFactory.get_app_login().login(mobile, code)

        logging.info("app登录返回数据:{}".format(res.json()))

        # 断言
        assert_common(res, 201)
        # 保存登录token
        apiConfig.app_header["Authorization"] = "Bearer " + res.json().get("data").get("token")
        # print("\napp最新header:{}".format(apiConfig.app_header))

    def test_app_query_article(self):
        """app查询渠道文章"""
        # 渠道id
        channel_id = TestPublishArticle.channel_id
        # 是否置顶 1:置顶
        with_top = 1
        # 请求方法
        res = ApiFactory.get_app_qury_article().query_article(channel_id, with_top)

        logging.info("app渠道文章查询返回数据:{}".format(res.json()))

        # 断言 状态码 和 message
        assert_common(res)
        # 断言 发布文章 是否在返回文章列表中
        # 存储查询结果中所有title
        title_list = []
        # 取所有文章列表
        for i in res.json().get("data").get("results"):
            title_list.append(i.get("title"))

        # print("\n文章列表:{}".format(title_list))
        assert TestPublishArticle.title in title_list
