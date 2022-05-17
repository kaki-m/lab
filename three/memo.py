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

print(kaku_array2)

#ここまででkaku_arrayに読み取ることはできた

print(len(kaku_array2))
print(len(kaku_array2[0]))