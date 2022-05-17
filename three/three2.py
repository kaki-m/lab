#このプログラムはプロットをグラフでやるバージョンを新しく作りたいため用意した
import matplotlib.pyplot as plt
import numpy as np

f = open('./001.001.000.sdt')

datalist = f.readlines()
datanum1 = int(datalist[0])#データの個数はファイルの一番上に書いてある
int_datalist = [[0]*6]*datanum1

for i in range(datanum1):
    int_datalist[i] = datalist[i+1].split(' ')
    #ここで-9999を発見したらそこは飛ばす
    if 0 > int(int_datalist[i][1]):
        continue
    else:
        for j in range(6):
            int_datalist[i][j] = int(int_datalist[i][j])
            print(int_datalist[1][0])
f.close()
#プロットするために、x座標のリストとy座標のリストに分けなければならない
x1 = [0]*len(int_datalist)
y1 = [0]*len(int_datalist)

for i in range(len(int_datalist)):
    #print("x:"+str(torimed_datalist[i][0]))
    x1[i] = int_datalist[i][0]
    y1[i] = int_datalist[i][1]

plt.scatter,(x1,y1,linestyle='solid',color='blue')
plt.show()