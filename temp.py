import xlrd
import requests
data = xlrd.open_workbook("2.xls",encoding_override="utf-8")
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    alldata = table.row_values(i)
    print(alldata[5])
    
    
    



headers =  {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTY5MTQ2MzkzNn0.3GhwHPU4vZNV_jlEEQbsoQM7rB-J_M3D7je9vz8MFFIc-jcIuT3qU1gmbTZ1AdKzGr-fiapXyq624FXJRfsbGw",
    "dbschema": "county431011",
    "ipaddr": "",
    "opuser": "431011003002",
    "partitioncode": "P1_SERVICE",
    "serialnumber": "{\"biosSn\":\"\",\"baseboardSn\":\"\",\"cpuSn\":\"\"}",
    "servicecheckcode": "a479497397c08a27eb55c789fd1ac847",
    "tenantid": "431011"
}
# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "ipaddr": "",
#     "serialnumber": "{\"biosSn\":\"\",\"baseboardSn\":\"\",\"cpuSn\":\"\"}",
#     "x-requested-with": "XMLHttpRequest"
# }
# rsp = requests.get("http://10.104.3.3:30005/hncb/sys/user/login?data=%7B%22userCode%22%3A%22431011003002%22%2C%22passwd%22%3A%22CxIzzM%2FyWpi2Rop2a16VOylAiRsTYS3kkM2Tf0gZYtE%3D%22%2C%22key%22%3A%22c08cd2b7-40a9-4da2-9ff2-63b5b6f1f8c1%22%2C%22verifyCode%22%3A%22xsni%22%2C%22verifyKey%22%3A%2276bf50e3-c281-4bbf-b801-d8775b7ec75b%22%2C%22original_jsp%22%3A%22%22%2C%22signed_data%22%3A%22%22%2C%22errorcode%22%3A%22%22%2C%22errormsg%22%3A%22%22%7D&_=1691377522971",
#                   headers=headers)

rsp = requests.get("http://10.104.3.3:30005/hncb/api/baseObject/qryObjectListByCondition?data=%7B%22categorycode%22%3A%22431011003%22%2C%22objectname%22%3A%22%E5%91%A8%E5%85%89%E8%8D%A3%22%7D&t=1691376095&start=0&length=19&draw=1",
             headers=headers)
print(rsp.text)
    
# fetch("http://10.104.3.3:30005/hncb/api/baseObject/qryObjectListByCondition?data=%7B%22categorycode%22%3A%22431011003%22%2C%22objectname%22%3A%22%E5%91%A8%E5%85%89%E8%8D%A3%22%7D&t=1691376095&start=0&length=19&draw=1", {
#   "headers": {
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImF1dGgiOiJST0xFX0FETUlOLFJPTEVfVVNFUiIsImV4cCI6MTY5MTQ2MjQzOX0.7UfDttK-3Favt--n_IyiKQwVFb6iAO_fXrZ1DJWAf2Y1UhWj-LFu1inuapYoz4x4C45ChGD0TApylXbK_Bwhqw",
#     "dbschema": "county431011",
#     "ipaddr": "",
#     "opuser": "431011003002",
#     "partitioncode": "P1_SERVICE",
#     "serialnumber": "{\"biosSn\":\"\",\"baseboardSn\":\"\",\"cpuSn\":\"\"}",
#     "servicecheckcode": "3267f49230da4994a9e33168d7a4e9da",
#     "tenantid": "431011"
#   },
#   "referrer": "http://10.104.3.3:30005/index.html",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });