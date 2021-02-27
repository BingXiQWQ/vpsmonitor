import requests,json,time
from jsonpath import jsonpath
url = 'https://www.ovh.com/engine/api/dedicated/server/availabilities?country=ca&hardware=1804sk12'
header = {'Content-Type': "application/json"}
responsea = requests.get(url,headers=header)
responseb = responsea.text
responsec = json.loads(responseb)
availability = jsonpath(responsec, "$..availability")
gettime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
count = 0 
for i in range(len(availability)):
    if availability[i] == 'available':
        count = count + 1
if count > 0:
    status = '有货！！！'
    #填入自己的key
    posturl = 'https://maker.ifttt.com/trigger/kimsufi_notification/with/key/*'
    payload = {"value1":status, "value2":gettime}
    requests.post(posturl,data=payload)