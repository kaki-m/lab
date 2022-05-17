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

#ここからはx,y座標を利用して線を書き、署名データをみえる形にする

#座標データはint_dastalist[1][x] x = 0ならx座標,x = 1ならy座標

from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)

#座標をリストに格納してPILで表示可能な順序に直す
#x1,y1,x2,y2のような感じ

line_list = [0]*(datanum*2)
locate = 0
for i in range(datanum):
    for j in range(2):
        line_list[locate] = int_datalist[i][j]
        locate += 1

draw.point(line_list, fill=(255, 255, 0))

im.show()

#ここまでで点としてデータを可視化することができた
#もっと文字らしくするために、筆圧によって点の大きさを変更するなどすればいいかもしれない
