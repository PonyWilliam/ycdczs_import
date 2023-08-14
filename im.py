import xlrd
def im_data(FileName):
    data = xlrd.open_workbook(FileName,encoding_override="utf-8")
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    villages = ["四明山","贯子头","沙子","大力元","保方","黄茶园","张家排","岭口","西岭","陡角头","回龙","胡家桥","堆子头"]


    vdata = []
    other = []

    for i in villages:
        vdata.append([])

    for i in range(4,nrows):
        alldate = table.row_values(i)
        time = alldate[1]
        money = alldate[2]
        bank = alldate[5]
        name = alldate[6]
        remark = alldate[9]
        
        
        if(money != "" and float(money) > 0):
            # 对money进行判断，只统计支出的钱
            flag = 0
            for i in range(0,13):
                if remark.count(villages[i]) > 0:
                    info = {
                    'money':money,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                    }
                    vdata[i].append(info)
                    flag = 1
                    break
            # 找不到加入到疑难表中
            if(flag == 0):
                info = {
                    'money':money,
                    'bank':bank,
                    'name':name,
                    'remark':remark,
                    'time':time
                }
                other.append(info)
    return vdata,other