import requests
import json
def get_v():
    v=''
    try:
        res= requests.get("")
        r=res.json()

        v="版本信息："+json.dumps(res, ensure_ascii=False)
    except Exception as  e:
        v='获取版本信息失败'
        print('获取版本信息失败')

    return v