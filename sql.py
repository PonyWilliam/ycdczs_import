import pymysql
from config import getConf
mysqlconf = getConf()
db = pymysql.connect(
    host=mysqlconf['host'],
    port=mysqlconf['port'],
    user=mysqlconf['user'],
    password=mysqlconf['password'],
    db=mysqlconf['db'],
    charset='utf8mb4'
)
def GetDB():
    return db