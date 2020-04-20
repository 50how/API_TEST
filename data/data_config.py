class global_val:
    Id = '0'
    name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    headers = '5'
    token = '6'
    case_depend = '7'
    data_depend = '8'
    data = '9'
    expect = '10'
    respond_data = '11'
    result = '12'


def get_id():
    """获取case_id"""
    return global_val.Id


def get_name():
    """获取请求模块名称"""
    return global_val.name


def get_url():
    """获取请求url"""
    return global_val.url


def get_run():
    """获取是否运行"""
    return global_val.run


def get_run_way():
    """获取请求方式"""
    return global_val.request_way

def get_headers():
    """获取headers"""
    return global_val.headers

def get_token():
    """获取是否携带token"""
    return global_val.token


def get_case_depend():
    """case依赖"""
    return global_val.case_depend


def get_data_depend():
    """依赖的返回数据"""
    return global_val.data_depend


def get_data():
    """获取请求数据"""
    return global_val.data


def get_expect():
    """获取预期结果"""
    return global_val.expect

def get_resond():
    """获取响应结果"""
    return global_val.respond_data


def get_result():
    """获取返回结果"""
    return global_val.result

