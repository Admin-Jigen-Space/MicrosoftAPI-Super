# -*- coding: UTF-8 -*-
import requests as req
import json,sys,time,random
#先注册azure应用,确保应用有以下权限:
#files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
#user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
#mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
#注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用




def main2():
    for key in id_list:
	    congif_id[key] = repr(id_list[key])
    for key in config:
	    print congif_id[key]

main2()
