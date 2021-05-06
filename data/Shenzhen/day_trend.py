import numpy as np
import matplotlib.pyplot as plt
import time,datetime
#image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data_different.npy")
image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\npy\\TaxiSZ.npy")
# x= 6
# print(image_array.shape)
# for time in range(20):
#     print(x)
#     dict_data = []
#     for i in range(160,x+5):
#         day_list = []
#         for j in range(48):
#             sum = 0
#             for l in range(25):
#                 for m in range(50):
#                     sum += image_array[i][j][0][l][m]
#             day_list.append(sum)
#         dict_data.append(day_list)
#     print(dict_data)
#     plt.show()
#     x +=7
def get_day(end_date):
    start_sec = time.mktime(time.strptime("20190101", '%Y%m%d'))
    end_sec = time.mktime(time.strptime(end_date, '%Y%m%d'))
    work_days = int((end_sec - start_sec) / (24 * 60 * 60))
    return work_days

def return_day(end_date):
    timeArray = time.localtime(int(end_date*24*60*60+1546272000.0))
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime
#============== 一周趋势 =====================

days  = 60
for i in range(50):
    all_data = []
    for day in range(days,days+1):
        day_list = []
        for timesnap in range(48):
            sum = 0
            for row in range(25):
                for cloumn in range(50):
                    sum += image_array[day][timesnap][1][row][cloumn]
            day_list.append(sum)
        all_data.extend(day_list)
    plt.plot(all_data,linewidth=2.5)
    #plt.grid(axis="x")
    plt.title(return_day(days))
    plt.show()
    days+=1