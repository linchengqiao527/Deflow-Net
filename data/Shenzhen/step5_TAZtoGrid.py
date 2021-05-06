import time
import csv
import numpy as np
import os
import time
import numpy as np
import sys
from PIL import Image
'''************************************************************
** 函数名称:  count_grid
** 功能描述:  仅对TAZ划分使用,将polygon 映射到对应的矩阵中,比如50x100,100x200
** 输入参数:   openpath 原始数据的路径,savepath 处理完成后保存路径,(row, column) 表示划分的规格，比如25x50,50x100,100x200
             
** 日    期:  2019年8月26日
**************************************************************'''


def count_grid(open_path, save_path, row, column):
    save_path = save_path
    row = row
    column = column
    region_flow = np.load(open_path)
    grid_flow = np.zeros((181, 48, 2, row, column))

    with open(r'C:\Users\11838\PycharmProjects\Python_Learning\Dataprocessing\TAZ\CSV\sz_491_50x100_Intersect.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data_csv = [(row['grid_id'], row['ORIG_FID'], row['NewArea'], row['segArea']) for row in reader]
    #统计每个方格的流量
    for mm in range(region_flow.shape[0]):
        for interval_id in range(0, 48):
            for in_out_id in range(0, 2):
                for seg in data_csv:
                    row_id = row - 1 - int(int(seg[0]) / column)
                    column_id = int(seg[0]) % column
                    flow = (float(seg[3]) / float(seg[2])) * region_flow[mm][interval_id][in_out_id][int(seg[1])]
                    # print(type(flow))
                    grid_flow[mm][interval_id][in_out_id][row_id][column_id] += flow

    np.save(save_path, grid_flow)

    # 画图


if __name__ == '__main__':


    #保存print
    path = os.path.abspath(os.path.dirname(__file__))
    # root_dir为要读取文件的根目录
    row = 50
    column = 100

    count_grid(r'C:\Users\11838\PycharmProjects\Python_Learning\Dataprocessing\TAZ\491\TaxiSZ_taz491_deal.npy', r'C:\Users\11838\PycharmProjects\Python_Learning\Dataprocessing\TAZ\50×100\50×100', row, column)


