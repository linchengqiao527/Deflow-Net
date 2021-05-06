import numpy as np
import matplotlib.pyplot as plt
import time,datetime
#image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\data_different.npy")
image_array = np.load("C:\\Users\\11838\\PycharmProjects\\Python_Learning\\Dataprocessing\\deal\\npy\\data_different.npy")

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
days = 0
for i in range(180):
    for day in range(days,days+1):
        if days ==2:
            image_array[day][27]= (image_array[day-1][27]+image_array[day+1][27])/2
            image_array[day][28] = (image_array[day - 1][28]+ image_array[day + 1][28]) / 2
            image_array[day][34] = (image_array[day - 1][34] + image_array[day + 1][34]) / 2
        if days ==3:
            image_array[day][23] = (image_array[day-1][23]+image_array[day+1][24])/2

        if days ==8:
            image_array[day][34] = (image_array[day-1][34]+image_array[day+1][34])/2
        if days ==11:
            image_array[day][28]  = (image_array[day - 1][28]  + image_array[day + 1][28] ) / 2
            image_array[day][29]  = (image_array[day - 1][29]  + image_array[day + 1][29] ) / 2
            image_array[day][30]  = (image_array[day - 1][30]  + image_array[day + 1][30] ) / 2
        if days ==14:
            image_array[day][30]  = image_array[day - 7][30] 
            image_array[day][32]  = image_array[day + 7][32] 
            image_array[day][31]  = (image_array[day - 1][31]  + image_array[day + 1][31] ) / 2
        if days ==15:
            image_array[day][25]  = (image_array[day - 1][25]  + image_array[day + 1][25] ) / 2
            image_array[day][26]  = (image_array[day - 1][26]  + image_array[day + 1][26] ) / 2
            image_array[day][27]  = (image_array[day - 1][27]  + image_array[day + 1][27] ) / 2
            image_array[day][28]  = (image_array[day - 1][28]  + image_array[day + 1][28] ) / 2
            image_array[day][29]  = (image_array[day - 1][29]  + image_array[day + 1][29] ) / 2
            image_array[day][30]  = (image_array[day - 1][30]  + image_array[day + 1][30] ) / 2
            image_array[day][32]  = (image_array[day - 2][32]  + image_array[day + 1][32] ) / 2
            image_array[day][33]  = (image_array[day - 1][33]  + image_array[day + 1][33] ) / 2
            image_array[day][34]  = (image_array[day - 1][34]  + image_array[day + 1][34] ) / 2
        if days ==19:
            image_array[day][23]  = (image_array[day - 1][23]  + image_array[day + 1][23] ) / 2
            image_array[day][24]  = (image_array[day - 1][24]  + image_array[day + 1][24] ) / 2
            image_array[day][25]  = (image_array[day - 1][25]  + image_array[day + 1][25] ) / 2
            image_array[day][26]  = (image_array[day - 1][26]  + image_array[day + 1][26] ) / 2
            image_array[day][27]  = (image_array[day - 1][27]  + image_array[day + 1][27] ) / 2
            image_array[day][32]  = (image_array[day - 2][32]  + image_array[day + 1][32] ) / 2
            image_array[day][31]  = (image_array[day - 1][31]  + image_array[day + 1][31] ) / 2
        if days ==23:
            image_array[day][35]  = (image_array[day - 1][35]  + image_array[day + 1][35] ) / 2
            image_array[day][19]  = (image_array[day - 1][19]  + image_array[day + 1][19] ) / 2
        if days ==29:
            image_array[day][21]  = (image_array[day - 1][21]  + image_array[day + 1][21] ) / 2
            image_array[day][22]  = (image_array[day - 1][22]  + image_array[day + 1][22] ) / 2
            image_array[day][23]  = (image_array[day - 1][23]  + image_array[day + 1][23] ) / 2
            image_array[day][24]  = (image_array[day - 1][24]  + image_array[day + 1][24] ) / 2
        if days ==56:
            image_array[day][30]  = (image_array[day - 1][30]  + image_array[day + 1][30] ) / 2
            image_array[day][31]  = (image_array[day - 1][31]  + image_array[day + 1][31] ) / 2
            image_array[day][32]  = (image_array[day - 2][32]  + image_array[day + 1][32] ) / 2
            image_array[day][33]  = (image_array[day - 1][33]  + image_array[day + 1][33] ) / 2
            image_array[day][34]  = (image_array[day - 1][34]  + image_array[day + 1][34] ) / 2
            image_array[day][35]  = (image_array[day - 1][35]  + image_array[day + 1][35] ) / 2
        if days ==62:
            image_array[day] = (image_array[55] + image_array[69]) / 2
        if days ==59:
            image_array[day] = (image_array[52] +image_array[73]) / 2
        if days ==60:
            image_array[day]= (image_array[53] + image_array[67]) / 2
        if days ==63:
            image_array[day][16:35]= (image_array[56][16:35]+ image_array[70][16:35]) / 2
        if days ==66:
            image_array[day][24]  = (image_array[day - 1][24]  + image_array[day + 1][24] ) / 2
        if days == 79:
            image_array[day][32]  = (image_array[day - 2][32]  + image_array[day + 1][32] ) / 2
            image_array[day][33]  = (image_array[day - 1][33]  + image_array[day + 1][33] ) / 2
        if days == 80:
            image_array[day][43]  = (image_array[day - 1][43]  + image_array[day + 1][43] ) / 2
        if days == 89:
            image_array[day][30]  = (image_array[82][30]  + image_array[96][30] ) / 2
        if days ==93:
            image_array[day][25]  = (image_array[day - 1][25]  + image_array[day + 7][25] ) / 2
            image_array[day][26]  = (image_array[day - 1][26]  + image_array[day + 7][26] ) / 2
            image_array[day][27]  = (image_array[day - 1][27]  + image_array[day + 7][27] ) / 2
            image_array[day][28]  = (image_array[day - 1][28]  + image_array[day + 7][28] ) / 2
            image_array[day][29]  = (image_array[day - 1][29]  + image_array[day + 7][29] ) / 2
            image_array[day][30]  = (image_array[day - 1][30]  + image_array[day + 7][30] ) / 2
        if days ==100:
            image_array[day][3]  = (image_array[day - 1][3]  + image_array[day + 7][3] ) / 2
        if days ==112:
            image_array[112:120] = (image_array[98:106] + image_array[105:113]) / 2
        if days == 141:
            image_array[day][20]  = (image_array[day - 1][20]  + image_array[day -7][20] ) / 2
        if days == 143:
            image_array[day][19:] = (image_array[day - 1][19:] + image_array[day -7][19:]) / 2
        if days == 144:
            image_array[144:147]= (image_array[137:140] + image_array[130:133]) / 2
        if days == 147:
            image_array[days][0:24] = (image_array[day - 1][0:24] + image_array[day - 7][0:24]) / 2
        if days == 151:
            image_array[days][42:] = (image_array[day - 1][42:] + image_array[day - 7][42:]) / 2
        if days == 152:
            image_array[days] = (image_array[day - 1]+ image_array[day - 7]) / 2
        if days == 153:
            image_array[days][0:22] = (image_array[day - 1][0:22]+ image_array[day - 7][0:22]) / 2
        if days == 159:
            image_array[days][31:35] = (image_array[day - 1][31:35]+ image_array[day - 7][31:35]) / 2
        days += 1


np.save("TaxiSZ.npy",image_array)