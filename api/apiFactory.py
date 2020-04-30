from api.login import *
from api.article import *


class ApiFactory:
    """返回所有接口统一入口类"""

    @classmethod
    def get_mp_login(cls):
        """返回自媒体登录接口对象"""
        return MpLogin()

    @classmethod
    def get_mp_publish_article(cls):
        """返回自媒体 发布文章接口"""
        return MpPubArticle()

    @classmethod
    def get_mis_login(cls):
        """返回后台管理登录"""
        return MisLogin()

    @classmethod
    def get_mis_article(cls):
        """返回后台管理文章"""
        return MisPubArticle()

    @classmethod
    def get_app_login(cls):
        """返回app登录"""
        return AppLogin()

    @classmethod
    def get_app_qury_article(cls):
        """返回app查询渠道文章"""
        return AppQueryChannelArticle()
