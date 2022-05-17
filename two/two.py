import matplotlib.pyplot as plt
import numpy as np

with open("a.txt", "r") as tf:
    a = tf.read().split('\n')

tf.close()

with open("b.txt", "r") as tf:
    b = tf.read().split('\n')

tf.close()

for i in range(len(a)):
    a[i] = float(a[i])

for i in range(len(b)):
    b[i] = float(b[i])


plt.plot(a)
plt.plot(b)

plt.show()

#ここからはreference1
D = np.array([[0] * len(b)]*len(a))

for i in range(len(a)):
    for j in range(len(b)): 
        D[i][j] = abs(a[i] - b[j])



G = np.array([[0] * len(b)]*len(a))
for i in range(len(a)):
    for j in range(len(b)):
        if(i == 0):
            G[i][j] = D[i][j]
        else:
            
            G[i][j] = min(G[i-1][j], G[i-1][j-1], G[i-1][j-2]) + D[i][j]
            print("D:" + str(D[i][j]))
            print("G:" + str(G[i][j]))
            print("今は" + str(i) +":"+ str(j))
print("-----------")
print(len(a))
print(len(b))
print("類似度は" + str(G[len(a)-1][len(b)-1]))

#類似度が0となるので間違っている気がする

#ここから問題3
Backtrack = np.array([0] * len(a))

i = len(a)-1
j = len(b)-1
'''
1:i-1,j
2:i-1,j-1
3:i-1,j-2
'''
while True:
    if i == 0 & j == 0:
        break

    Backtrack[i] = j
    #最小がどれかを求める
    if (G[i-1][j] <= G[i-1][j-1]) & (G[i-1][j] <= G[i-1][j-2]):
        i = i-1
        j = j
    elif (G[i-1][j-1] <= G[i-1][j]) & (G[i-1][j-1] <= G[i-1][j-2]):
        i = i-1
        j = j-1
    elif (G[i-1][j-2] <= G[i-1][j]) & (G[i-1][j-2] <= G[i-1][j-1]):
        i = i-1
        j = j-2
    else:
        print("最小を決めることができませんでした。")
        print(i)
        print(j)

plt.plot(Backtrack)
print(G)
print(Backtrack)

plt.show()


#ここまででバックトラックは完成した。
#ここからはbを歪ませてaに近づける作業になる
#この時Backtrackを使用する
#bとaの距離が最小になる位置のbのx軸の位置がこの変数に格納されている
#つまり、変更後のbはbacktrackの

new_b = np.array([0]*len(Backtrack))

for i in range(len(Backtrack)):
    new_b[i] = b[Backtrack[i]]

plt.plot(a)
plt.plot(b)
plt.plot(new_b)

plt.show()

#解答例とは異なるものの、歪ませることができた
