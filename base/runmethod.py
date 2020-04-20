import json
import requests
from util.log import log
requests.packages.urllib3.disable_warnings()


class RunMethod:
    def post_main(self, url, data=None, header=None,):
        log().info('开始请求')
        res = None
        try:
            if header != None:
                if 'MultipartEncoder'in str(data):
                    res = requests.post(url=url, data=data, headers=header, verify=False)
                else:
                    res = requests.post(url=url, json=data, headers=header, verify=False)
                    # 必须将data传给json，,修改requests库models.py 第466行 body = complexjson.dumps(json,ensure_ascii=False)
            else:
                if 'MultipartEncoder' in str(data):
                    res = requests.post(url=url, data=data, verify=False)
                else:
                    res = requests.post(url=url, json=data, verify=False)
            if not res:
                log().error('响应失败 %s',res)
            else:
                log().info('请求完成 %s',res)
        except Exception as e:
            log().error('请求失败\n%s', e)
        return res.json()

    def get_main(self, url, data=None, header=None):
        log().info('开始请求')
        res = None
        try:
            if header != None:
                res = requests.get(url=url, params=data, headers=header, verify=False)
            else:
                res = requests.get(url=url, params=data, verify=False)
            if not res:
                log().error('响应失败 %s',res)
            else:
                log().info('请求完成 %s',res)
        except Exception as e:
            log().error('请求失败\n%s',e)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data,header)
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    data = {
        'cart': '11'
    }
    run = RunMethod()
    run_test = run.run_main(method="Post", url=url, data=data)
    print(run_test)
