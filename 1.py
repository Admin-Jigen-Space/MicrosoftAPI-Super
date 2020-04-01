# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用
#以下空行不要删除，以便运行时插入机密

id_list = [r'b2b60c8e-e838-4a86-94a6-1b5f689028b0',r'OldV=42tW9l1/FYuzB.sipZmo@dnFKHc']
secret_list = [r'9a587110-8249-4f22-a686-e11b553f5f6e',r'.alg52tc5:DDhL4Dmn/lDzJIeupgyBV.']

num1 = [0]*len(id_list)
def gettoken(refresh_token):
    headers={'Content-Type':'application/x-www-form-urlencoded'
            }
    data={'grant_type': 'refresh_token',
          'refresh_token': refresh_token,
          'client_id':id_list[a],
          'client_secret':secret_list[a],
          'redirect_uri':'http://localhost:53682/'
         }
    html = req.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    return access_token
def main():
    print(a)
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    print(refresh_token)
for _ in range(3): 
    for i in range(random.randint(5,10),0,-1):
        time.sleep(1)
    for a in range(1, len(id_list)):
	    path=sys.path[0]+r'/'+str(a)+'.txt'
	    main()
