import xlrd
import requests
from config import getUrl

url = getUrl()
def im_data(FileName):
    data = xlrd.open_workbook(FileName,encoding_override="utf-8")
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    # villages通过api接口去获取
    
    villages = []
    rsp = requests.get(url + "/village")
    rsp = rsp.json()
    for i in rsp:
        if i['Id'] == 10000:
            continue #保留字段
        name = i['Name'][:-1]
        
        villages.append(name)
    print(villages)
    vdata = []
    other = []

    
    
    for i in villages:
        vdata.append([])

    for i in range(4,nrows):
        alldate = table.row_values(i)
        bankno = alldate[0]
        time = alldate[1]
        money = alldate[2]
        incomes = alldate[3]
        bank = alldate[5]
        name = alldate[6]
        remark = alldate[9]
        if(money != "" and float(money) > 0):
            # 对money进行判断，只统计支出的钱
            flag = 0
            for j in range(0,len(villages)):
                if remark.count(villages[j]) > 0:
                    info = {
                    'bankno':bankno,
                    'money':money,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                    }
                    vdata[j].append(info)
                    flag = 1
                    break
            # 找不到加入到疑难表中
            if(flag == 0):
                info = {
                    'bankno':bankno,
                    'money':money,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                }
                other.append(info)
        if(incomes != "" and float(incomes) > 0):
            incomes = -float(incomes)
            flag = 0
            for j in range(0,len(villages)):
                if remark.count(villages[j]) > 0:
                    info = {
                    'bankno':bankno,
                    'money':incomes,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                    }
                    vdata[j].append(info)
                    flag = 1
                    break
            # 找不到加入到疑难表中,加入到其他数据里
            if(flag == 0):
                info = {
                    'bankno':bankno,
                    'money':incomes,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                }
                other.append(info)
    return vdata,other