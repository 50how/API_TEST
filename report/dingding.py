import requests
import base.config
import json
import time

def send_ding(text):
    try:
        url='https://oapi.dingtalk.com/robot/send?access_token='+base.config.DINGDING_TOKEN
        head={}
        data ={}
        link={}
        link['title']=time.strftime("%Y-%m-%d %H:%M:%S ")+base.config.REPORT_TITLE
        link['text']=text
        link['messageUrl']=base.config.REPORT_URL
        data['link']=link
        data['msgtype']='link'
        head['Content-Type']='application/json'
        head['charset']='utf-8'
        j=json.dumps(data)
        res=requests.post(url=url,data=j,headers=head)
        print(res.json())

    except Exception as e:
        print('ding send fail'+str(e))

if __name__ == '__main__':
    send_ding('123')
