# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random


dd2=[1]
id_list2=[1]






 

path4=sys.path[0]+r'/buconfig.txt'
fj = open(path4, "r+")
daynum = fj.read()
fj.close()
daynum=int(daynum)
def gettoken(refresh_token):
    headers={'Content-Type':'application/x-www-form-urlencoded'
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id_lists[a],
          'client_secret':secret_lists[a],
          'redirect_uri':'http://localhost:53682/'
         }
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    with open(path, 'w+') as f:
        f.write(refresh_token)
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    access_token=gettoken(refresh_token)
for a in range(0, len(id_list)):
    path=sys.path[0]+r'/token/'+str(a)+'.txt'
    id_lists=id_list
    secret_lists=secret_list
    main()
if id_list2 != dd2:
    for a in range(0, len(id_list)):
        path=sys.path[0]+r'/backuptoken/'+str(a)+'.txt'
        id_lists=id_list2
        secret_lists=secret_list2
        main()
if daynum >= 30:
    vv = 0
    with open(path4, 'w+') as fb:
        fb.write(vv)
else:
    daynum+=1
    with open(path4, 'w+') as fb:
        fb.write(str(daynum))
