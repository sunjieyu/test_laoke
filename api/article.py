import apiConfig
import requests,time,logging


class MpPubArticle:
    """自媒体发布文章接口"""

    def __init__(self):
        # 地址
        self.mp_article_url = apiConfig.mp_host_url + "/articles"

    def mp_publish_article(self, title, content, channel_id):
        """发布文章"""
        # 请求body
        mp_article_body = {
            "title": title,
            "content": content,
            "channel_id": channel_id,
            "cover":
                {
                    "type": 0,
                    "images": []
                }
        }
        logging.info("自媒体文章发发布地址:{}".format(self.mp_article_url))
        logging.info("自媒体文章发发布body:{}".format(mp_article_body))
        # 发起网络请求
        return requests.post(self.mp_article_url, json=mp_article_body, headers=apiConfig.mp_login_header)


class MisPubArticle:
    """后台文章查询 和 文章审核"""

    def __init__(self):
        # 地址
        self.article_url = apiConfig.mis_host_url + "/articles"

    def query_article(self, title, channel):
        """
        查询文章
        :param title: 查询文章标题
        :param channel: 查询文章渠道
        :return:
        """
        # 请求body
        query_body = {"title": title, "channel": channel}

        logging.info("后台管理查询地址:{}".format(self.article_url))
        logging.info("后台管理查询body:{}".format(query_body))

        # 发起请求 params 会将字典拼接成 url?key=value&key=value
        return requests.get(self.article_url, params=query_body, headers=apiConfig.mis_header)

    def audit_article(self, article_ids, status):
        """
        审核文章
        :param article_ids: 审核文章id列表
        :param status: 文章审核状态 2：审核通过 已知问题：文章发布后就是审核状态所以在审核会报错
        :return:
        """
        # 防止传入字符串 做一次转换 isinstance(变量,"类型") 变量符合类型返回True 不符合返回False
        if not isinstance(article_ids, list):
            article_ids = [article_ids]

        # 请求body
        audit_body = {"article_ids": article_ids, "status": status}

        logging.info("后台管理审核地址:{}".format(self.article_url))
        logging.info("后台管理审核body:{}".format(audit_body))

        # 发起请求
        return requests.put(self.article_url, json=audit_body, headers=apiConfig.mis_header)


class AppQueryChannelArticle:

    def __init__(self):
        # 地址
        self.query_channel_article_url = apiConfig.app_host_url_v1_1 + "/articles"

    def query_article(self, channel_id, with_top):
        """
        查询渠道文章列表
        :param channel_id: 渠道id
        :param with_top: 是否置顶 1：置顶
        :return:
        """
        # 请求body channel_id=1&timestamp=1222333&with_top=1
        query_body = {"channel_id": channel_id, "timestamp": int(time.time()*1000), "with_top": with_top}

        logging.info("app端查询渠道文章地址:{}".format(self.query_channel_article_url))
        logging.info("app端查询渠道文章body:{}".format(query_body))

        # 请求方法
        return requests.get(self.query_channel_article_url, params=query_body, headers=apiConfig.app_header)
