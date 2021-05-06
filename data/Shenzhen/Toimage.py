import numpy as np
import matplotlib.pyplot as plt
import time,datetime
#image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data_different.npy")
image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\npy\\data_different.npy")
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
all_data=[]


for day in range(76,83):
    day_list = []
    for timesnap in range(48):
        sum = 0
        for row in range(25):
            for cloumn in range(50):
                sum += image_array[day][timesnap][1][row][cloumn]
        day_list.append(sum)
    all_data.extend(day_list)
plt.plot(all_data,marker='*')
plt.axvline(48,color='red',linestyle='--')
plt.axvline(96,color='red',linestyle='--')
plt.axvline(144,color='red',linestyle='--')
plt.axvline(192,color='red',linestyle='--')
plt.axvline(240,color='red',linestyle='--')
plt.axvline(288,color='red',linestyle='--')
plt.axhline(3700,color='green',linestyle='--')
plt.axhline(21520,color='green',linestyle='--')
plt.xlim((0, 336))
#plt.grid(axis="x")
plt.title(return_day(69)+"   -    "+return_day(75))
plt.show()


all_data=[]
month_day=['20190119','20190219','20190319','20190419','20190519','20190619']
for day in month_day:
    day_list = []
    for timesnap in range(48):
        sum = 0
        for row in range(25):
            for cloumn in range(50):
                sum += image_array[get_day(day)][timesnap][1][row][cloumn]
        day_list.append(sum)
    all_data.append(day_list)

plt.plot(all_data[0],label=month_day[0])
plt.plot(all_data[1],label=month_day[1])
plt.plot(all_data[2],label=month_day[2])
plt.plot(all_data[3],label=month_day[3])
plt.plot(all_data[4],label=month_day[4])
plt.plot(all_data[5],label=month_day[5])
plt.legend()
plt.title("Month")
plt.show()


#对于同一天


day = get_day('20190322')
one_day_res=[]
one_day_com=[]
for timesnap in range(48):
    one_day_res.append(image_array[day][timesnap][0][17][6])
for timesnap in range(48):
    one_day_com.append(image_array[day][timesnap][0][19][9])

plt.plot(one_day_res,color='green',label="Residential area")
plt.plot(one_day_com,color='red',label='Work area')
plt.title("Inflow")
plt.legend(loc='upper right')
plt.show()

day = get_day('20190516')
one_day_res=[]
one_day_com=[]
for timesnap in range(48):
    one_day_res.append(image_array[day][timesnap][0][14][14])
for timesnap in range(48):
    one_day_com.append(image_array[day][timesnap][0][14][4])

plt.plot(one_day_res,color='green',label="High-speed Train")
plt.plot(one_day_com,color='red',label='Airport')
plt.title("Inflow")
plt.legend(loc='upper right')
plt.show()



day = get_day('20190516')
one_day_res=[]
one_day_com=[]
for timesnap in range(48):
    one_day_res.append(image_array[day][timesnap][1][14][14])
for timesnap in range(48):
    one_day_com.append(image_array[day][timesnap][1][14][4])

plt.plot(one_day_res,color='green',label="High-speed Train")
plt.plot(one_day_com,color='red',label='Airport')
plt.title("Outflow")
plt.legend(loc='upper right')
plt.show()

trainSet = image_array[get_day("20190309")][17][0]
plt.imshow(trainSet)
plt.colorbar()
plt.title("Traffic inflow in 9:00 am")
plt.show()



trainSet2 = image_array[get_day("20190309")][17][1]
plt.imshow(trainSet2)
plt.colorbar()
plt.title("Traffic outflow in 9:00 am")
plt.show()