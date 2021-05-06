import shapefile
from matplotlib import pyplot as plt
import numpy as np
def isRayIntersectsSegment(poi,s_poi,e_poi): #[x,y] [lng,lat]
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1]==e_poi[1]: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #线段在射线上边
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #线段在射线下边
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #交点为下端点，对应spoint
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #交点为下端点，对应epoint
        return False
    if s_poi[0]<poi[0] and e_poi[1]<poi[1]: #线段在射线左边
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #求交
    if xseg<poi[0]: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后
def isPoiWithinPoly(poi,poly):
    #输入：点，多边形三维数组
    #poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

    #可以先判断点是否在外包矩形内
    #if not isPoiWithinBox(poi,mbr=[[0,0],[180,90]]): return False
    #但算最小外包矩形本身需要循环边，会造成开销，本处略去
    sinsc=0 #交点个数
    for epoly in poly: #循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
        for i in range(len(epoly)-1): #[0,len-1]
            s_poi=epoly[i]
            e_poi=epoly[i+1]
            if isRayIntersectsSegment(poi,s_poi,e_poi):
                sinsc+=1 #有交点就加1

    return True if sinsc%2==1 else  False






file = shapefile.Reader(r'C:\Users\11838\PycharmProjects\Python_Learning\Dataprocessing\TAZ\shapefile\sz_491\sz_491.shp')
shapes = file.shapes()#
# with open(r'/Dataprocessing/TAZ/shp_point', 'a+', encoding='UTF-8') as writefile:
#     for i in range(file.numRecords):
#         border_points = shapes[i].points
#         for position in border_points:
#             position = list(position)
#             lan,lon  = position[0],position[1]
#             writefile.write(str(lan)+','+str(lon)+" ")
#         writefile.write("\n")

for i in shapes[1].points:
    position = list(i)
    print(str(position[0])+","+str(position[1]))
    #             lan,lon  = position[0],position[1]



# print(str(file.shapeType))  # 输出shp类型
# print(file.encoding)# 输出shp文件编码
# print(file.bbox)  # 输出shp的文件范围（外包矩形）
# print(file.numRecords)  # 输出shp文件的要素数据
# print(file.fields)
# border_shape = file
# # 通过创建reader类的对象进行shapefile文件的读取
# # border_points
# border = border_shape.shapes()
# # .shapes()读取几何数据信息，存放着该文件中所有对象的 几何数据
# # border是一个列表
# border_points = border[1].points
# print(border_points)# 返回第1个对象的所有点坐标
# # border_points = [(x1,y1),(x2,y2),(x3,y3),…]
#
# x, y = zip(*border_points)
# # x=(x1,x2,x3,…)
# # y=(y1,y2,y3,…)
#
# fig, ax = plt.subplots()  # 生成一张图和一张子图
# # plt.plot(x,y,'k-') # x横坐标 y纵坐标 ‘k-’线性为黑色
# plt.plot(x, y, color='#6666ff', label='fungis')  # x横坐标 y纵坐标 ‘k-’线性为黑色
# ax.grid()  # 添加网格线
# ax.axis('equal')
# plt.show()