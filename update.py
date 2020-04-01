# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用
#以下空行不要删除，以便运行时插入机密
#
id_list = [r'b2b60c8e-e838-4a86-94a6-1b5f689028b0',r'9a587110-8249-4f22-a686-e11b553f5f6e']
secret_list = [r'OldV=42tW9l1/FYuzB.sipZmo@dnFKHc',r'.alg52tc5:DDhL4Dmn/lDzJIeupgyBV.']
config_list = {'每次轮数':3,'是否启动随机时间':'N','延时范围起始':10,'结束':15,'是否开启随机api顺序':'Y'}

num1 = [0]*len(id_list)
randomapi = [1,2,3,4,5,6,7,8,9,10]
ran = 0
str2=''
path2=sys.path[0]+r'/randomapi.txt'

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
    with open(path, 'w+') as f:
        f.write(refresh_token)
#    with open(path, 'w+') as f2:
#        f2.write(randomapi2) 
def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    gettoken(refresh_token)
for a in range(0, len(id_list)):
    c=random.randint(5,10)
    path=sys.path[0]+r'/'+str(a)+'.txt'
    arr = random.shuffle(randomapi)
    print(arr)
#    for i in range(10): 
#        arr[i] = str(arr[i])
#    str2 = ','.join(arr)
#    print (str2)
#    main()
