from im import im_data


from concurrent import futures
import grpc
import info_pb2
import info_pb2_grpc

import os

def check_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

# 调用函数进行判断


# 实现 proto 文件中定义的 GRPCServicer
class GetInfoService(info_pb2_grpc.GetInfoService):
    # 实现 proto 文件中定义的 rpc 调用
    def GetInfo(self, request, context):
        if check_file_exists(request.filename) == False:
            return info_pb2.Rsp(villagesInfo=None,otherInfo=None,errCode=True)
        vdata,other = im_data(request.filename)
        # float money = 1;
        # string bank = 2;
        # string name = 3;
        # string remark = 4;
        # string time = 5;
        otherInfo = info_pb2.ArrInfo()
        for k in other:
            info = info_pb2.Info()
            info.bankno = k['bankno']
            info.money = float(k['money'])
            info.bank = k['bank']
            info.name = k['name']
            info.remark = k['remark']
            info.time = k['time']
            
            otherInfo.Ainfo.append(info)
        villiage = []
        for j in vdata:
            Arrinfo = info_pb2.ArrInfo()
            for x in j:
                info = info_pb2.Info()
                info.bankno = x['bankno']
                info.money = float(x['money'])
                info.bank = x['bank']
                info.name = x['name']
                info.remark = x['remark']
                info.time = x['time']
                Arrinfo.Ainfo.append(info)
            villiage.append(Arrinfo)
        return info_pb2.Rsp(villagesInfo=villiage,otherInfo=otherInfo,errCode=False)


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    info_pb2_grpc.add_GetInfoServiceServicer_to_server(GetInfoService(), server)
    server.add_insecure_port('[::]:10086')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
   serve()

# 通过proto传递数据
