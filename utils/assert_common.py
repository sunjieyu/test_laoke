def assert_common(res, code=200, message="OK"):
    """
    通用断言 状态码 和 message
    :param res: 响应对象
    :param code: 响应状态码
    :param message: 响应message
    :return:
    """
    # 断言 -状态码
    assert res.status_code == code
    # 断言 -message
    assert res.json().get("message") == message
