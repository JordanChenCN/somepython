from dns import resolver
import requests

iplist = []
appdomain = "www.google.com"

def get_iplist(domain):
    try:
        A = resolver.query(domain,"A")
    except Exception as e:
        print("dns reslover error:"+str(e))
        exit(1)
    for i in A.rrset:
        iplist.append(i.to_text())

def checkip(iplist):
    for ip in iplist:
        try:
            checkurl = "http://"+ ip + ":80"
            timeout = 1
            conn = requests.get(url=checkurl,timeout=timeout)
            code = conn.status_code
            if code == 200 :
                print(ip+" [OK]")
            else:
                print(ip+" [Error]")
        except requests.RequestException as e:
            print("Error:" + str(e))
            exit(2)


get_iplist(appdomain)
checkip(iplist)