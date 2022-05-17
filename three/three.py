import matplotlib.pyplot as plt
import numpy as np

f = open('./001.001.000.sdt')

datalist = f.readlines()
datanum1 = int(datalist[0])
int_datalist = [[0]*5]*datanum1

delete_index = []

for i in range(datanum1):
    int_datalist[i] = datalist[i+1].split(' ')
    if 0 > int(int_datalist[i][1]):
        delete_index.append(i)

    for j in range(6):
        int_datalist[i][j].strip()
        int_datalist[i][j] = int(int_datalist[i][j])


print("外れ値が存在し削除する行の数1 " + str(len(delete_index)))
print("消去する最後のインデックス:" + str(delete_index[30]))
#ここで外れ値の存在する行を削除する
delindex = 0
deletenum = 0
for i in range(len(delete_index)):
    delindex = delete_index[i]
    print(str(i) + ":" + str(delindex))
    del int_datalist[delindex-i]

f.close()

#ここまではone1.pyの使い回し
from PIL import Image, ImageDraw

im = Image.new('RGB', (400, 200), (255, 255, 255))
draw = ImageDraw.Draw(im)

#座標をリストに格納してPILで表示可能な順序に直す
#x1,y1,x2,y2のような感じ

line_list1 = [0]*(datanum1*2)
locate = 0
for i in range(datanum1-len(delete_index)):
    for j in range(2):
        line_list1[locate] = int_datalist[i][j]
        locate += 1

draw.line(line_list1, fill=(255, 0, 0))
import copy #int_datalistをAとBの両方残せるようにAにコピーしておく
A_datalist = copy.copy(int_datalist)



f = open('./001.001.001.sdt')

datalist = f.readlines()
datanum2 = int(datalist[0])
int_datalist = [[0]*5]*datanum2

delete_index = []

for i in range(datanum2):
    int_datalist[i] = datalist[i+1].split(' ')
    if 0 > int(int_datalist[i][1]):
        delete_index.append(i)
    for j in range(6):
        int_datalist[i][j].strip()
        int_datalist[i][j] = int(int_datalist[i][j])

print("外れ値が存在し削除する行の数2 " + str(len(delete_index)))
#ここで外れ値の存在する行を削除する
delindex = 0
deletenum = 0
for i in range(len(delete_index)):
    delindex = delete_index[i]
    print(str(i) + ":" + str(delindex))
    del int_datalist[delindex-i]


f.close()

#ここまではone1.pyの使い回し

#座標をリストに格納してPILで表示可能な順序に直す
#x1,y1,x2,y2のような感じ

line_list2 = [0]*(datanum2*2)
locate = 0
for i in range(datanum2-len(delete_index)):
    for j in range(2):
        line_list2[locate] = int_datalist[i][j]
        locate += 1

draw.line(line_list2, fill=(0, 0, 255))

B_datalist = copy.copy(int_datalist)
#ここまでで同一平面じょうにふたつの署名データを表示できた
print("データの数1:" + str(datanum1))
print("データの数2:" + str(datanum2))

#まずは線形マッチングをしてプロットする
#ふたつの署名にはデータ数の違いがあるため、工夫する

#何倍すればもう一方の署名に合わせられるかを計算
dif = datanum2/datanum1
#データ１のインデックスにdifを掛けたインデックスがデータ２の場所

for i in range(0,datanum1,10):
    index = round(i * dif)
    if 0 > line_list1[i*2] or 0 > line_list1[i*2+1] or 0 > line_list2[index*2] or 0 > line_list2[index*2+1]:
        continue
    else:
        draw.line(((line_list1[i*2],line_list1[i*2+1]),(line_list2[index*2],line_list2[index*2+1])), fill=(0, 255, 0,0))
#おかしなプロットになるため、-9999は無視するようにする

im.show()
#ここまでで線形マッチングが完成した

#ここからはDPマッチングをしていく
#まずは下の式d(Si,Si') = (1/n) * sum(((xij -x'ij)^2 + (yij - y'ij)^2)^(-2))
'''
今回使用する変数は二つのデータリスト
A_datalist[i][j]
B_datalist[i][j]
iは点の個数
jはその点のx,yの座標の2つ
A_datalist[805][2]
B_datalist[721][2]
'''

#print("Aのリストの個数:" + str(len(A_datalist[1])))
#print("Bのリストの個数:" + str(len(B_datalist)))
#A,Bのリストの個数を格納しておく
A_datanum = len(A_datalist)
B_datanum = len(B_datalist)
#d = np.array([[0] * len(b)]*len(a))

#画数ごとのデータが必要で、一画ごとにマッチングをおこなっていく

f = open('./001.001.000.sdt')

datalist = f.readlines()
datanum1 = int(datalist[0])
int_datalist = [[0]*5]*datanum1

delete_index = []

for i in range(datanum1):
    int_datalist[i] = datalist[i+1].split(' ')
    if 0 > int(int_datalist[i][1]):
        delete_index.append(i)

    for j in range(6):
        int_datalist[i][j].strip()
        int_datalist[i][j] = int(int_datalist[i][j])

#これで、deleteindexの場所が一画の分け目なのでそこで分けた3次元リストを作る
