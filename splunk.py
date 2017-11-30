#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther:xwjr.com
import sys,gzip,csv,json
import requests
import urllib3
urllib3.disable_warnings()

def get_token(corp_id, secret):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (corp_id, secret)
    r = requests.get(url=url)
    token = r.json()['access_token']
    return token


def send_message(splunk_log_info, tag_id, agent_id, token):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token
    Header = "splunk提醒！！"
    data = {
        "totag": tag_id,
        "msgtype": "text",
        "agentid": agent_id,
        "text": {
            "content": Header + '\n' + splunk_log_info
        },
        "safe":"0"
    }
    r = requests.post(url=url, data=json.dumps(data), verify=False)
    print(r.json())

if __name__ == '__main__':

    gzip_file = sys.argv[8]
    csv_file = gzip.open(gzip_file)
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        splunk_log_info = row[2]

    corp_id = "fffffffff"
    secret = "ddddddd"
    tag_id = "16"
    agent_id = "26"

    token = get_token(corp_id, secret)
    send_message(splunk_log_info, tag_id, agent_id, token)
