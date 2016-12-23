import json
import requests

def sending(token,content):
    srv_url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (token)
    params = {}
    params['msgtype'] = 'text'
    params['text'] = {'content':content}
    params['isAtAll'] = False
    header = {'Content-Type':'Application/Json'}
    r = requests.post(srv_url, headers=header, data=json.dumps(params))
    print r
    print r.text.encode('utf-8')
if __name__ == "__main__":
    sending('28215ac99776ace06cef34d84cebaf796305f548b157b08ab6047652fed2f191','make test')
