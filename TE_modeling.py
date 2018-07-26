#encoding=utf-8
""""
function: drawing the TE_modelling
author : kevin fung
data: 2018-7-24
python 2.7
"""
from __future__ import print_function
import matplotlib.pyplot as plt
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
x_data1=[]
y_data1=[]
def read_TE_modelling(TE_modelling_xslx):
    contents=xlrd.open_workbook(TE_modelling_xslx)
    for content in contents.sheets():
        #print('Sheet:%s'%content.name)
        for row in range(content.nrows):
           # print('the row is:%s'%row)
            values=[]
            for col in range(content.ncols):
                values.append(content.cell(row,col).value)
           # print(values)
            x_data1.append(values[0])
            y_data1.append(values[1])
    return [x_data1,y_data1]
def draw_TE_modelling(x_data,y_data):
    fig=plt.subplot()
    fig.plot(x_data,y_data,"ro-",linewidth=2,label="TE_ros")
    fig.set_xlabel("Distance/km")
    fig.set_ylabel("ros/Ω.m")
    fig.legend(loc="lower right")
    plt.show()
if __name__=='__main__':
    x_data=read_TE_modelling('TE.xlsx')[0][:40]
    y_data=read_TE_modelling('TE.xlsx')[1][:40]

    draw_TE_modelling(x_data,y_data)




