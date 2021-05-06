import time
import csv
import numpy as np
import os
import time
import numpy as np
import sys
from PIL import Image

'''************************************************************
** 函数名称:  taz_gird
** 功能描述:  将预测的流量还原到对应的polygon
** 输入参数:   openpath 原始数据的路径,savepath 处理完成后保存路径,(row, column) 表示划分的规格，比如25x50,50x100,100x200

** 日    期:  2019年8月26日
**************************************************************'''
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def taz_gird(openpath, savepath, row, column):
    str_open = openpath
    str_save = savepath
    row = row
    column = column
    grid_flow = np.load(str_open)
    #加载csv文件
    with open('./TAZcsv/sz_1066_25x50_Intersect.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data_csv = [(row['grid_id'], row['ORIG_ID'], row['grid_area'], row['segArea']) for row in reader]
    region_num = 1066
    region_flow = np.zeros((96, 2, region_num))
    for interval_id in range(0, 96):
        for in_out_id in range(0, 2):
            for seg in data_csv:
                row_id = row - 1 - int(int(seg[0]) / column)
                column_id = int(seg[0]) % column
                flow = (float(seg[3]) / float(seg[2])) * grid_flow[interval_id][in_out_id][row_id][column_id]

                region_flow[interval_id][in_out_id][int(seg[1])] += flow
    np.save(str_save, region_flow)
if __name__ == '__main__':

    #保存print
    path = os.path.abspath(os.path.dirname(__file__))
    type = sys.getfilesystemencoding()
    sys.stdout = Logger('./save/sz_1066_trc_grid_flow_50x100.txt')  #日志保存文件

    row = 25
    column = 50
    # root_dir为要读取文件的根目录
    root_dir = r"./predict_data/new_data_flow_1066_25x50" #输入文件目录
    save = r'./predict_data/new_data_1066_mapping_25x50'  #存储目录
    data_index = os.listdir(root_dir)
    data_index.sort()
    # print(data_index[0])
    # print(data_index)
    for index in data_index:
        # 获取文件夹的路径
        domain = os.path.abspath(root_dir)
        save = os.path.abspath(save)
        txt_name =index.split('.')[0] + 'predict.npy'
        # 将路径与文件名结合起来就是每个文件的完整路径
        str_open = os.path.join(domain, index)
        str_save = os.path.join(save, txt_name)
        print(str_open)
        print(str_save)
        taz_gird(str_open, str_save, row, column)
        break


