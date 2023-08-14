from flask import Flask
from im import im_data
from sql import GetDB
import json
vdata = None
other = None

db = GetDB()
cursor = db.cursor()


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello,World'

@app.route('/show')
def show():

    vdata,other = im_data()
    
    all_data = {
        'villages':vdata,
        'other':other
    }
    # 已处理到村里的数据展示后导入到系统内，付款时间与账单时间保持一致并也要带上

    # 未处理的数据也要展示

    # 重复数据导入判断：时间姓名备注完全一致

    return all_data

@app.route('/im')
def im():
    # 正式导入用这个函数
    return 'success'

@app.route('/test')
def test():
    sql = "select * from bills"
    cursor.execute(sql)
    print(json.dumps(dict(cursor.fetchall())))
    return 'test'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
