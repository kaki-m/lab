#次はデータをグラフにする

#署名データの読み込み
#https://daharu.hatenadiary.org/entry/20110915/1316046148
f = open('./001.001.000.sdt')

datalist = f.readlines()
datanum = int(datalist[0])
int_datalist = [[0]*5]*datanum

for i in range(datanum):
    int_datalist[i] = datalist[i+1].split(' ')
    for j in range(6):
        int_datalist[i][j].strip()
        int_datalist[i][j] = int(int_datalist[i][j])
print(int_datalist[1])

f.close()

import numpy as np
import matplotlib.pyplot as plt
 
# 折れ線グラフを出力
#この時、先頭から５次元のデータはそれぞれ
'''
0:x
1:y
2:筆圧
3:方位
4:高度
'''

x_list = [0] * datanum
y_list = [0] * datanum
hituatu_list = [0] * datanum
houi_list = [0] * datanum
koudo_list = [0] * datanum



for i in range(datanum):
    if int_datalist[i][0] < 0:
        x_list[i] = 79
        y_list[i] = 62
        hituatu_list[i] = 463
        houi_list[i] = 860
        koudo_list[i] = 530
    else:
        x_list[i] = int_datalist[i][0]
        y_list[i] = int_datalist[i][1]
        hituatu_list[i] = int_datalist[i][2]
        houi_list[i] = int_datalist[i][3]
        koudo_list[i] = int_datalist[i][4]


fig = plt.figure()
axes= fig.subplots(5)

axes[0].plot(x_list)
axes[1].plot(y_list)
axes[2].plot(hituatu_list)
axes[3].plot(houi_list)
axes[4].plot(koudo_list)

plt.show()