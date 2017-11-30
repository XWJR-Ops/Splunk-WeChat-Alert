#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther:xwjr.com
import sys,gzip,csv,json
import requests
import time
import urllib3
urllib3.disable_warnings()

def get_token(corp_id, secret):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corp_id, secret)
    r = requests.get(url=url)
    token = r.json()['access_token']
    return token


def send_message(message, tag_id, agent_id, token):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token
    Header = "splunk提醒！！"
    data = {
        "totag": tag_id,
        "msgtype": "text",
        "agentid": agent_id,
        "text": {
            "content": Header + '\n' + message
        },
        "safe":"0"
    }
    r = requests.post(url=url, data=json.dumps(data), verify=False)
    print(r.json())

if __name__ == '__main__':

    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    gzip_file = sys.argv[8]
    csv_file = gzip.open(gzip_file)
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        splunk_log_info = row[3]
    message = "日志：" + splunk_log_info + '\n时间：' + time_now

    corp_id = "changeme"
    secret = "changeme"
    tag_id = "changeme"
    agent_id = "changeme"

    token = get_token(corp_id, secret)
    send_message(message, tag_id, agent_id, token)
