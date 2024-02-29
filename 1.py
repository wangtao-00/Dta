from openopc2.da_client import OpcDaClient
import time

# 创建 OPC DA 客户端实例
client = OpcDaClient(OPC_SERVER, OPC_HOST, OPC_MODE)
# 替换 OPC_SERVER, OPC_HOST, OPC_MODE 为实际的值

# 定义要读取的标签列表
tags_to_read = ['tag1', 'tag2', 'tag3']

while True:
    try:
        # 从 OPC 服务器读取数据
        values = client.read(tags_to_read)
        print(values)

        # 等待一段时间再进行下一次读取
        time.sleep(1)  # 等待1秒，可以根据需要调整这个时间间隔
    except Exception as e:
        print("Error reading from OPC server:", e)
        # 可以选择在错误发生时中断循环或者进行重连尝试
        break


