import os
import numpy as np
import time

def openfile(path):
    # 31 28 31 29 28 30
    #四月 少了25号 5月少了25，26，27
    datamatrix = np.zeros((181,48,2,491))

    def get_day(end_date):
        start_sec = time.mktime(time.strptime("20190101", '%Y%m%d'))
        end_sec = time.mktime(time.strptime(end_date, '%Y%m%d'))
        work_days = int((end_sec - start_sec) / (24 * 60 * 60))
        return work_days

    dirs = os.listdir(path)
    for dir in dirs:

        with open(path+"\\"+dir, 'r',encoding='UTF-8') as readFile:
            lines = readFile.readlines()

            for line in lines:
                line = line.split(',')
                try:
                    if (0<=get_day(line[1])<=180 and 0<=get_day(line[3])<=180) or line[1]=="20181231":
                        if line[1]=='20181231':
                            if line[3]=='20190101':
                               #0进1出
                               datamatrix[0][int(line[4])][0][int(line[6][:-1])]+=1
                        elif line[1]=="20190701":
                            pass
                        elif line[3]=="20190701":
                            datamatrix[180][int(line[2])][1][int(line[5])] += 1
                        else:
                            datamatrix[get_day(line[3])][int(line[4])][0][int(line[6])] += 1
                            datamatrix[get_day(line[1])][int(line[2])][1][int(line[5])] += 1
                except Exception as e:
                    print(line)
        print("File "+path+"\\"+dir+"  has Finish!")
    np.save('20201201.npy', datamatrix)
openfile(r'C:\Users\11838\PycharmProjects\Python_Learning\Dataprocessing\TAZ\data')
