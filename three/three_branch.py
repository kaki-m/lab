import numpy as np
import math
#画数ごとのデータが必要で、一画ごとにマッチングをおこなっていく
f = open('./001.001.000.sdt')

datalist = f.readlines()
last_data = '-1 -9999 -9999 -9999 -9999 -9999'
datalist.append(last_data)
datanum1 = int(datalist[0]) + 1
int_datalist = [[0]*5]*datanum1


delete_index = []

for i in range(datanum1):
    int_datalist[i] = datalist[i+1].split(' ')
    if 0 > int(int_datalist[i][1]):
        delete_index.append(i)

    for j in range(6):
        #int_datalist[i][j].strip()
        int_datalist[i][j] = int(int_datalist[i][j])

#これで、deleteindexの場所が一画の分け目なのでそこで分けた3次元リストを作る
kaku_array = [[[0 for i3 in range(2)] for i2 in range(1)] for i1 in range(len(delete_index))]
#画数だけ用意した　二次元目はappendで増やしていく 三次元目はx,yの二つ
i = 0
j = 0
k = 0
flag = 0 #これは各画の最初の点であるかどうかを判断するflagもし最初の点ならば初期化が必要
int_datalist_xy = [[0]*2]*datanum1 #これはint_datalistのxyだけを抜いたもの
while i < (len(delete_index)):
#これで消す数になるまで繰り返す　外れ値に到達した場合に
#インクリメントしたいためにここはwhileでループさせる
    if j == delete_index[i]: #外れ値に到達したらインクリメントをする
        i += 1
        flag = 0 #そして次の点は画の最初の点となるのでflagは0に戻しておく
        k = 0 #各画の中でいくつめの点なのかは初期化する
        j+=1 #スキップする前に次の点にいく。そうしないとずっと-9999を読み取ってしまう
        continue
    
    if flag == 0: #画の最初の点であるならば、リストに直接格納する
        kaku_array[i][0][0] = int_datalist[j][0]
        kaku_array[i][0][1] = int_datalist[j][1]
        flag = 1
    else:#最初の点でないならappendでok
        append_xy = [0]*2
        append_xy[0] = int_datalist[j][0]
        append_xy[1] = int_datalist[j][1]
        kaku_array[i].append(append_xy)


    j += 1 #次の点にいく jは最大でもlen(int_datalist)になるはず

import numpy as np
#画数ごとのデータが必要で、一画ごとにマッチングをおこなっていく
f = open('./001.001.001.sdt')

datalist2 = f.readlines()
last_data = '-1 -9999 -9999 -9999 -9999 -9999'
datalist2.append(last_data)
datanum2 = int(datalist2[0]) + 1
int_datalist2 = [[0]*5]*datanum2


delete_index2 = []

for i in range(datanum2):
    int_datalist2[i] = datalist2[i+1].split(' ')
    if 0 > int(int_datalist2[i][1]):
        delete_index2.append(i)

    for j in range(6):
        #int_datalist[i][j].strip()
        int_datalist2[i][j] = int(int_datalist2[i][j])

#これで、deleteindexの場所が一画の分け目なのでそこで分けた3次元リストを作る
kaku_array2 = [[[0 for i3 in range(2)] for i2 in range(1)] for i1 in range(len(delete_index2)+1)]
#画数だけ用意した　二次元目はappendで増やしていく 三次元目はx,yの二つ
i = 0
j = 0
k = 0
flag = 0 #これは各画の最初の点であるかどうかを判断するflagもし最初の点ならば初期化が必要
int_datalist_xy = [[0]*2]*datanum2 #これはint_datalistのxyだけを抜いたもの
while i < (len(delete_index2)):
#これで消す数になるまで繰り返す　外れ値に到達した場合に
#インクリメントしたいためにここはwhileでループさせる
    if j == delete_index2[i]: #外れ値に到達したらインクリメントをする
        i += 1
        flag = 0 #そして次の点は画の最初の点となるのでflagは0に戻しておく
        k = 0 #各画の中でいくつめの点なのかは初期化する
        j+=1 #スキップする前に次の点にいく。そうしないとずっと-9999を読み取ってしまう
        continue
    
    if flag == 0: #画の最初の点であるならば、リストに直接格納する
        kaku_array2[i][0][0] = int_datalist2[j][0]
        kaku_array2[i][0][1] = int_datalist2[j][1]
        flag = 1
    else:#最初の点でないならappendでok
        append_xy = [0]*2
        append_xy[0] = int_datalist2[j][0]
        append_xy[1] = int_datalist2[j][1]
        kaku_array2[i].append(append_xy)


    j += 1 #次の点にいく jは最大でもlen(int_datalist)になるはず

#ここまででkaku_arrayに読み取ることはできた

#ここからはkaku_arrayとkaku_array2を使ってそれらをプロットしていく
from PIL import Image, ImageDraw

im = Image.new('RGB', (400, 200), (255, 255, 255))
draw = ImageDraw.Draw(im)
#ここで書くための基盤を作った。次は座標をline_listにx,y,x2,y2,...の形にしてプロットする

for i in range(len(kaku_array)):#kaku_array全部を読み取るためのループ
    line_list = [] #それぞれの画ごとに描画していきたいため別々にする
    for j in range(len(kaku_array[i])):#一画を読み取るためのループ
        for k in range(2):#x,yを読み取るためのループ
            line_list.append(kaku_array[i][j][k])
    draw.line(line_list,fill = (255,0,0))

#kaku_array2用
for i in range(len(kaku_array2)):#kaku_array全部を読み取るためのループ
    line_list = [] #それぞれの画ごとに描画していきたいため別々にする
    for j in range(len(kaku_array2[i])):#一画を読み取るためのループ
        for k in range(2):#x,yを読み取るためのループ
            line_list.append(kaku_array2[i][j][k])
    draw.line(line_list,fill = (0,0,255))
#ここまでで二つの文字をプロットするところまではできた
#次は線形マッチングをしていく
#線形マッチングはそれぞれの画で点とてんを繋いでいく
#同時に、dに文字間距離を格納していく
#画ごとに点と点のそれぞれの距離を合計し、その画の持つ点の数で割るとd(Si,Si')が完成するつまり
#まずは画の数だけdを入れなければならないため、dを定義する
d = [0] * len(kaku_array)
distance = 0
for i in range(len(kaku_array)):
    kazu_awase = (len(kaku_array[i]) / len(kaku_array2[i]))
    for j in range(len(kaku_array2[i])):
        index = round(j * kazu_awase)
        distance = ((kaku_array[i][index][0] - kaku_array2[i][j][0])**2) + ((kaku_array[i][index][1] - kaku_array2[i][j][1])**2)
        distance = math.sqrt(distance)
        d[i] = d[i] + distance
        if (j % 10) == 0: #線形マッチングの直線を全てかくと多すぎておかしいのでここで調整する
            draw.line(((kaku_array[i][index][0],kaku_array[i][index][1]),(kaku_array2[i][j][0],kaku_array2[i][j][1])),fill=(0, 255, 0,0))
im.show()

#次にも時間距離D(C,C')を算出するため、dをそれぞれの画が持つ点の数で割り、sumを取る
D_liner = 0
for i in range(len(kaku_array)):
    d[i] = d[i] / len(kaku_array[i])#画の持つ点の数で割る
    D_liner += d[i]

print("線形マッチングによる文字間距離: " + str(D_liner))

#線形マッチングはここで距離を出すことができたため、次はDPマッチングで計算をしていく

#まずはDPマッチング用のDを求める
#ここからreferenceの通りに進めてみる
#project3によると、project2の問題2の式をdで置き換えるとできるらしい
#それぞれの画で全ての点同士の距離を出す
d_dp = [] * len(kaku_array)
#各画によって点の数は違うため、上のように空の三次元リストを宣言し、appendで拡張していく
for i in range(len(kaku_array)):
    distance_list_list = []
    for j in range(len(kaku_array[i])):
        distance_list = []
        for k in range(len(kaku_array2[i])):
            distance = (((kaku_array[i][j][0]-kaku_array2[i][k][0])**2)+((kaku_array[i][j][1]-kaku_array2[i][k][1])**2))
            distance = math.sqrt(distance)
            distance_list.append(distance)
        distance_list_list.append(distance_list)
    d_dp.append(distance_list_list)

#これで全ての距離がd_dpに格納できた
#それぞれの点同士で一番距離が短いところ同士を結べばok
#kaku_arrayのそれぞれの点が一番近い点がどこかの配列を作る
dp_lines = [] * len(d_dp)
D_dp = 0
min_index = 0
for i in range(len(d_dp)):
    min_indexes = []
    tmp = 0
    for j in range(len(d_dp[i])):
        #list.index(max(list)) //listはリストの名前でいい
        tmp += min(d_dp[i][j])
        min_index = d_dp[i][j].index(min(d_dp[i][j]))
        min_indexes.append(min_index)
    dp_lines.append(min_indexes)
    tmp /= len(d_dp[i])
    D_dp += tmp

#dp_linesには何個目の画の何個目の点の一番近い点はkaku_array2の何番目のインデックスなのかを
im2 = Image.new('RGB', (400, 200), (255, 255, 255))
draw2 = ImageDraw.Draw(im2)

for i in range(len(kaku_array)):#kaku_array全部を読み取るためのループ
    line_list = [] #それぞれの画ごとに描画していきたいため別々にする
    for j in range(len(kaku_array[i])):#一画を読み取るためのループ
        for k in range(2):#x,yを読み取るためのループ
            line_list.append(kaku_array[i][j][k])
    draw2.line(line_list,fill = (255,0,0))

#kaku_array2用
for i in range(len(kaku_array2)):#kaku_array全部を読み取るためのループ
    line_list = [] #それぞれの画ごとに描画していきたいため別々にする
    for j in range(len(kaku_array2[i])):#一画を読み取るためのループ
        for k in range(2):#x,yを読み取るためのループ
            line_list.append(kaku_array2[i][j][k])
    draw2.line(line_list,fill = (0,0,255))

print("DPマッチングによる文字間距離: " + str(D_dp))
for i in range(len(kaku_array)):
    for j in range(len(kaku_array[i])):
        index = dp_lines[i][j]
        print(index)
        if (j % 10) == 0: #線形マッチングの直線を全てかくと多すぎておかしいのでここで調整する
            draw2.line(((kaku_array[i][j][0],kaku_array[i][j][1]),(kaku_array2[i][index][0],kaku_array2[i][index][1])),fill=(0, 255, 0,0))

im2.show()