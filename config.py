mysqlconf = {
    'host':'admin.dadiqq.cn',
    'port':3306,
    'user':'fapiao',
    'password':'fapiao123',
    'db':'fapiao'
}
dev = 1
back_url = ""
if dev == 1:
    back_url = "http://localhost:7584"
else:
    back_url = "http://ycdback.dadiqq.cn"
def getConf():
    return mysqlconf

def getUrl():
    return back_url