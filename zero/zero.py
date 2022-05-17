'''
this is lab assignment 1
it use lab/one/data
and 
data/act01 is walking
data/act02 is sitting
data/act03 is jogging
data/test is test file
'''

#Task1
#open files
import numpy as np

#walking
walking = [None] * 7
for i in range(7):
    walking[i] = np.loadtxt("data/act01/0{}.txt".format(i+1), delimiter="\t", comments="#", dtype={
        'names':('x', 'y', 'z'),
        'formats':('f8', 'f8', 'f8')})

#sitting
sitting = [None] * 7
for i in range(7):
    sitting[i] = np.loadtxt("data/act02/0{}.txt".format(i+1), delimiter="\t", comments="#", dtype={
        'names':('x', 'y', 'z'),
        'formats':('f8', 'f8', 'f8')})

#jogging
jagging = [None] * 7
for i in range(7):
    jagging[i] = np.loadtxt("data/act03/0{}.txt".format(i+1), delimiter="\t", comments="#", dtype={
        'names':('x', 'y', 'z'),
        'formats':('f8', 'f8', 'f8')})


import matplotlib.pyplot as plt
import pandas as pd

walking1_x = []
walking1_y = []
walking1_z = []

#data01
for i in range(100):
    walking1_x.append(float(walking[0][i][0]))
    walking1_y.append(float(walking[0][i][1]))
    walking1_z.append(float(walking[0][i][2]))


#data02
walking2_x = []
walking2_y = []
walking2_z = []

for i in range(100):
    walking2_x.append(float(walking[1][i][0]))
    walking2_y.append(float(walking[1][i][1]))
    walking2_z.append(float(walking[1][i][2]))

#data03
walking3_x = []
walking3_y = []
walking3_z = []

for i in range(100):
    walking3_x.append(float(walking[2][i][0]))
    walking3_y.append(float(walking[2][i][1]))
    walking3_z.append(float(walking[2][i][2]))

#data03
walking4_x = []
walking4_y = []
walking4_z = []

for i in range(100):
    walking4_x.append(float(walking[3][i][0]))
    walking4_y.append(float(walking[3][i][1]))
    walking4_z.append(float(walking[3][i][2]))

#data05
walking5_x = []
walking5_y = []
walking5_z = []

for i in range(100):
    walking5_x.append(float(walking[4][i][0]))
    walking5_y.append(float(walking[4][i][1]))
    walking5_z.append(float(walking[4][i][2]))

#data06
walking6_x = []
walking6_y = []
walking6_z = []

for i in range(100):
    walking6_x.append(float(walking[5][i][0]))
    walking6_y.append(float(walking[5][i][1]))
    walking6_z.append(float(walking[5][i][2]))

#data07
walking7_x = []
walking7_y = []
walking7_z = []

for i in range(100):
    walking7_x.append(float(walking[6][i][0]))
    walking7_y.append(float(walking[6][i][1]))
    walking7_z.append(float(walking[6][i][2]))


plt.title('walking')
plt.plot(walking2_x,color = 'red',marker = ',')
plt.plot(walking2_y,color = 'blue',marker = ',')
plt.plot(walking2_z,color = 'green',marker = ',')
plt.show()

sitting1_x = []
sitting1_y = []
sitting1_z = []

#data01
for i in range(100):
    sitting1_x.append(float(sitting[0][i][0]))
    sitting1_y.append(float(sitting[0][i][1]))
    sitting1_z.append(float(sitting[0][i][2]))


#data02
sitting2_x = []
sitting2_y = []
sitting2_z = []

for i in range(100):
    sitting2_x.append(float(sitting[1][i][0]))
    sitting2_y.append(float(sitting[1][i][1]))
    sitting2_z.append(float(sitting[1][i][2]))

#data03
sitting3_x = []
sitting3_y = []
sitting3_z = []

for i in range(100):
    sitting3_x.append(float(sitting[2][i][0]))
    sitting3_y.append(float(sitting[2][i][1]))
    sitting3_z.append(float(sitting[2][i][2]))

#data03
sitting4_x = []
sitting4_y = []
sitting4_z = []

for i in range(100):
    sitting4_x.append(float(sitting[3][i][0]))
    sitting4_y.append(float(sitting[3][i][1]))
    sitting4_z.append(float(sitting[3][i][2]))

#data05
sitting5_x = []
sitting5_y = []
sitting5_z = []

for i in range(100):
    sitting5_x.append(float(sitting[4][i][0]))
    sitting5_y.append(float(sitting[4][i][1]))
    sitting5_z.append(float(sitting[4][i][2]))

#data06
sitting6_x = []
sitting6_y = []
sitting6_z = []

for i in range(100):
    sitting6_x.append(float(sitting[5][i][0]))
    sitting6_y.append(float(sitting[5][i][1]))
    sitting6_z.append(float(sitting[5][i][2]))

#data07
sitting7_x = []
sitting7_y = []
sitting7_z = []

for i in range(100):
    sitting7_x.append(float(sitting[6][i][0]))
    sitting7_y.append(float(sitting[6][i][1]))
    sitting7_z.append(float(sitting[6][i][2]))


plt.title('sitting')
plt.plot(sitting2_x,color = 'red',marker = ',')
plt.plot(sitting2_y,color = 'blue',marker = ',')
plt.plot(sitting2_z,color = 'green',marker = ',')
plt.show()

jagging1_x = []
jagging1_y = []
jagging1_z = []

#data01
for i in range(100):
    jagging1_x.append(float(jagging[0][i][0]))
    jagging1_y.append(float(jagging[0][i][1]))
    jagging1_z.append(float(jagging[0][i][2]))


#data02
jagging2_x = []
jagging2_y = []
jagging2_z = []

for i in range(100):
    jagging2_x.append(float(jagging[1][i][0]))
    jagging2_y.append(float(jagging[1][i][1]))
    jagging2_z.append(float(jagging[1][i][2]))

#data03
jagging3_x = []
jagging3_y = []
jagging3_z = []

for i in range(100):
    jagging3_x.append(float(jagging[2][i][0]))
    jagging3_y.append(float(jagging[2][i][1]))
    jagging3_z.append(float(jagging[2][i][2]))

#data03
jagging4_x = []
jagging4_y = []
jagging4_z = []

for i in range(100):
    jagging4_x.append(float(jagging[3][i][0]))
    jagging4_y.append(float(jagging[3][i][1]))
    jagging4_z.append(float(jagging[3][i][2]))

#data05
jagging5_x = []
jagging5_y = []
jagging5_z = []

for i in range(100):
    jagging5_x.append(float(jagging[4][i][0]))
    jagging5_y.append(float(jagging[4][i][1]))
    jagging5_z.append(float(jagging[4][i][2]))

#data06
jagging6_x = []
jagging6_y = []
jagging6_z = []

for i in range(100):
    jagging6_x.append(float(jagging[5][i][0]))
    jagging6_y.append(float(jagging[5][i][1]))
    jagging6_z.append(float(jagging[5][i][2]))

#data07
jagging7_x = []
jagging7_y = []
jagging7_z = []

for i in range(100):
    jagging7_x.append(float(jagging[6][i][0]))
    jagging7_y.append(float(jagging[6][i][1]))
    jagging7_z.append(float(jagging[6][i][2]))


plt.title('jagging')
plt.plot(jagging2_x,color = 'red',marker = ',')
plt.plot(jagging2_y,color = 'blue',marker = ',')
plt.plot(jagging2_z,color = 'green',marker = ',')
plt.show()

#Task2 start
#RMSは2乗平均平方根なので、順番としては1:二乗して合計する 2:それを7(データ数)で割る
#3:それをmath.sqrtする
import math

walking_squared_sum_x = [0,0,0,0,0,0,0]
walking_squared_sum_y = [0,0,0,0,0,0,0]
walking_squared_sum_z = [0,0,0,0,0,0,0]


walking_squared_sum_x[0] = sum(np.power(walking1_x,2))
walking_squared_sum_y[0] = sum(np.power(walking1_y,2))
walking_squared_sum_z[0] = sum(np.power(walking1_z,2))
walking_squared_sum_x[1] = sum(np.power(walking2_x,2))
walking_squared_sum_y[1] = sum(np.power(walking2_y,2))
walking_squared_sum_z[1] = sum(np.power(walking2_z,2))
walking_squared_sum_x[2] = sum(np.power(walking3_x,2))
walking_squared_sum_y[2] = sum(np.power(walking3_y,2))
walking_squared_sum_z[2] = sum(np.power(walking3_z,2))
walking_squared_sum_x[3] = sum(np.power(walking4_x,2))
walking_squared_sum_y[3] = sum(np.power(walking4_y,2))
walking_squared_sum_z[3] = sum(np.power(walking4_z,2))
walking_squared_sum_x[4] = sum(np.power(walking5_x,2))
walking_squared_sum_y[4] = sum(np.power(walking5_y,2))
walking_squared_sum_z[4] = sum(np.power(walking5_z,2))
walking_squared_sum_x[5] = sum(np.power(walking6_x,2))
walking_squared_sum_y[5] = sum(np.power(walking6_y,2))
walking_squared_sum_z[5] = sum(np.power(walking6_z,2))
walking_squared_sum_x[6] = sum(np.power(walking7_x,2))
walking_squared_sum_y[6] = sum(np.power(walking7_y,2))
walking_squared_sum_z[6] = sum(np.power(walking7_z,2))

RMS_walking_x = [0,0,0,0,0,0,0]
RMS_walking_y = [0,0,0,0,0,0,0]
RMS_walking_z = [0,0,0,0,0,0,0]

for i in range(7):
    RMS_walking_x[i] = math.sqrt(walking_squared_sum_x[i])
    RMS_walking_y[i] = math.sqrt(walking_squared_sum_y[i])
    RMS_walking_z[i] = math.sqrt(walking_squared_sum_z[i])

#sitting
sitting_squared_sum_x = [0,0,0,0,0,0,0]
sitting_squared_sum_y = [0,0,0,0,0,0,0]
sitting_squared_sum_z = [0,0,0,0,0,0,0]


sitting_squared_sum_x[0] = sum(np.power(sitting1_x,2))
sitting_squared_sum_y[0] = sum(np.power(sitting1_y,2))
sitting_squared_sum_z[0] = sum(np.power(sitting1_z,2))
sitting_squared_sum_x[1] = sum(np.power(sitting2_x,2))
sitting_squared_sum_y[1] = sum(np.power(sitting2_y,2))
sitting_squared_sum_z[1] = sum(np.power(sitting2_z,2))
sitting_squared_sum_x[2] = sum(np.power(sitting3_x,2))
sitting_squared_sum_y[2] = sum(np.power(sitting3_y,2))
sitting_squared_sum_z[2] = sum(np.power(sitting3_z,2))
sitting_squared_sum_x[3] = sum(np.power(sitting4_x,2))
sitting_squared_sum_y[3] = sum(np.power(sitting4_y,2))
sitting_squared_sum_z[3] = sum(np.power(sitting4_z,2))
sitting_squared_sum_x[4] = sum(np.power(sitting5_x,2))
sitting_squared_sum_y[4] = sum(np.power(sitting5_y,2))
sitting_squared_sum_z[4] = sum(np.power(sitting5_z,2))
sitting_squared_sum_x[5] = sum(np.power(sitting6_x,2))
sitting_squared_sum_y[5] = sum(np.power(sitting6_y,2))
sitting_squared_sum_z[5] = sum(np.power(sitting6_z,2))
sitting_squared_sum_x[6] = sum(np.power(sitting7_x,2))
sitting_squared_sum_y[6] = sum(np.power(sitting7_y,2))
sitting_squared_sum_z[6] = sum(np.power(sitting7_z,2))

RMS_sitting_x = [0,0,0,0,0,0,0]
RMS_sitting_y = [0,0,0,0,0,0,0]
RMS_sitting_z = [0,0,0,0,0,0,0]

for i in range(7):
    RMS_sitting_x[i] = math.sqrt(sitting_squared_sum_x[i])
    RMS_sitting_y[i] = math.sqrt(sitting_squared_sum_y[i])
    RMS_sitting_z[i] = math.sqrt(sitting_squared_sum_z[i])

#jagging
jagging_squared_sum_x = [0,0,0,0,0,0,0]
jagging_squared_sum_y = [0,0,0,0,0,0,0]
jagging_squared_sum_z = [0,0,0,0,0,0,0]


jagging_squared_sum_x[0] = sum(np.power(jagging1_x,2))
jagging_squared_sum_y[0] = sum(np.power(jagging1_y,2))
jagging_squared_sum_z[0] = sum(np.power(jagging1_z,2))
jagging_squared_sum_x[1] = sum(np.power(jagging2_x,2))
jagging_squared_sum_y[1] = sum(np.power(jagging2_y,2))
jagging_squared_sum_z[1] = sum(np.power(jagging2_z,2))
jagging_squared_sum_x[2] = sum(np.power(jagging3_x,2))
jagging_squared_sum_y[2] = sum(np.power(jagging3_y,2))
jagging_squared_sum_z[2] = sum(np.power(jagging3_z,2))
jagging_squared_sum_x[3] = sum(np.power(jagging4_x,2))
jagging_squared_sum_y[3] = sum(np.power(jagging4_y,2))
jagging_squared_sum_z[3] = sum(np.power(jagging4_z,2))
jagging_squared_sum_x[4] = sum(np.power(jagging5_x,2))
jagging_squared_sum_y[4] = sum(np.power(jagging5_y,2))
jagging_squared_sum_z[4] = sum(np.power(jagging5_z,2))
jagging_squared_sum_x[5] = sum(np.power(jagging6_x,2))
jagging_squared_sum_y[5] = sum(np.power(jagging6_y,2))
jagging_squared_sum_z[5] = sum(np.power(jagging6_z,2))
jagging_squared_sum_x[6] = sum(np.power(jagging7_x,2))
jagging_squared_sum_y[6] = sum(np.power(jagging7_y,2))
jagging_squared_sum_z[6] = sum(np.power(jagging7_z,2))

RMS_jagging_x = [0,0,0,0,0,0,0]
RMS_jagging_y = [0,0,0,0,0,0,0]
RMS_jagging_z = [0,0,0,0,0,0,0]

for i in range(7):
    RMS_jagging_x[i] = math.sqrt(jagging_squared_sum_x[i])
    RMS_jagging_y[i] = math.sqrt(jagging_squared_sum_y[i])
    RMS_jagging_z[i] = math.sqrt(jagging_squared_sum_z[i])

#Task3 3D plot about RMS data
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection = '3d')
ax.set_title("RMSdata")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.scatter(RMS_walking_x,RMS_walking_y,RMS_walking_z,c = 'blue')
ax.scatter(RMS_sitting_x,RMS_sitting_y,RMS_sitting_z,c = 'green')
ax.scatter(RMS_jagging_x,RMS_jagging_y,RMS_jagging_z,c = 'red')

plt.show()

#Task4 start RMS feature from sample test data
test = [None] * 10
for i in range(10):
    test[i] = np.loadtxt("data/test/0{}.txt".format(i+1), delimiter="\t", comments="#", dtype={
        'names':('x', 'y', 'z'),
        'formats':('f8', 'f8', 'f8')})

test1_x = []
test1_y = []
test1_z = []
for i in range(100):
    test1_x.append(float(test[0][i][0]))
    test1_y.append(float(test[0][i][1]))
    test1_z.append(float(test[0][i][2]))

test2_x = []
test2_y = []
test2_z = []
for i in range(100):
    test2_x.append(float(test[1][i][0]))
    test2_y.append(float(test[1][i][1]))
    test2_z.append(float(test[1][i][2]))
test3_x = []
test3_y = []
test3_z = []
for i in range(100):
    test3_x.append(float(test[2][i][0]))
    test3_y.append(float(test[2][i][1]))
    test3_z.append(float(test[2][i][2]))
test4_x = []
test4_y = []
test4_z = []
for i in range(100):
    test4_x.append(float(test[3][i][0]))
    test4_y.append(float(test[3][i][1]))
    test4_z.append(float(test[3][i][2]))
test5_x = []
test5_y = []
test5_z = []
for i in range(100):
    test5_x.append(float(test[4][i][0]))
    test5_y.append(float(test[4][i][1]))
    test5_z.append(float(test[4][i][2]))
test6_x = []
test6_y = []
test6_z = []
for i in range(100):
    test6_x.append(float(test[5][i][0]))
    test6_y.append(float(test[5][i][1]))
    test6_z.append(float(test[5][i][2]))
test7_x = []
test7_y = []
test7_z = []
for i in range(100):
    test7_x.append(float(test[6][i][0]))
    test7_y.append(float(test[6][i][1]))
    test7_z.append(float(test[6][i][2]))
test8_x = []
test8_y = []
test8_z = []
for i in range(100):
    test8_x.append(float(test[7][i][0]))
    test8_y.append(float(test[7][i][1]))
    test8_z.append(float(test[7][i][2]))
test9_x = []
test9_y = []
test9_z = []
for i in range(100):
    test9_x.append(float(test[8][i][0]))
    test9_y.append(float(test[8][i][1]))
    test9_z.append(float(test[8][i][2]))
test10_x = []
test10_y = []
test10_z = []
for i in range(100):
    test10_x.append(float(test[9][i][0]))
    test10_y.append(float(test[9][i][1]))
    test10_z.append(float(test[9][i][2]))

test_sum_x = [0,0,0,0,0,0,0,0,0,0]
test_sum_y = [0,0,0,0,0,0,0,0,0,0]
test_sum_z = [0,0,0,0,0,0,0,0,0,0]


test_sum_x[0] = sum(np.power(test1_x,2))
test_sum_y[0] = sum(np.power(test1_y,2))
test_sum_z[0] = sum(np.power(test1_z,2))
test_sum_x[1] = sum(np.power(test2_x,2))
test_sum_y[1] = sum(np.power(test2_y,2))
test_sum_z[1] = sum(np.power(test2_z,2))
test_sum_x[2] = sum(np.power(test3_x,2))
test_sum_y[2] = sum(np.power(test3_y,2))
test_sum_z[2] = sum(np.power(test3_z,2))
test_sum_x[3] = sum(np.power(test4_x,2))
test_sum_y[3] = sum(np.power(test4_y,2))
test_sum_z[3] = sum(np.power(test4_z,2))
test_sum_x[4] = sum(np.power(test5_x,2))
test_sum_y[4] = sum(np.power(test5_y,2))
test_sum_z[4] = sum(np.power(test5_z,2))
test_sum_x[5] = sum(np.power(test6_x,2))
test_sum_y[5] = sum(np.power(test6_y,2))
test_sum_z[5] = sum(np.power(test6_z,2))
test_sum_x[6] = sum(np.power(test7_x,2))
test_sum_y[6] = sum(np.power(test7_y,2))
test_sum_z[6] = sum(np.power(test7_z,2))
test_sum_x[7] = sum(np.power(test4_x,2))
test_sum_y[7] = sum(np.power(test4_y,2))
test_sum_z[7] = sum(np.power(test4_z,2))
test_sum_x[8] = sum(np.power(test5_x,2))
test_sum_y[8] = sum(np.power(test5_y,2))
test_sum_z[8] = sum(np.power(test5_z,2))
test_sum_x[9] = sum(np.power(test6_x,2))
test_sum_y[9] = sum(np.power(test6_y,2))
test_sum_z[9] = sum(np.power(test6_z,2))

RMS_test_x = [0,0,0,0,0,0,0,0,0,0]
RMS_test_y = [0,0,0,0,0,0,0,0,0,0]
RMS_test_z = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    RMS_test_x[i] = math.sqrt(test_sum_x[i])
    RMS_test_y[i] = math.sqrt(test_sum_y[i])
    RMS_test_z[i] = math.sqrt(test_sum_z[i])

#Task5 

#全部の点との距離を測って、設定した距離の間に入っていた場合にはcountをしていき、その数を最後に比較する
predict_distance = 8
result_type = ["","","","","","","","","",""]
result_num = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    count_walk = 0
    count_sit = 0
    count_run = 0
    max_type = ""
    max_num = 0
    
    #testと点との距離を計算する
    for j in range(7):
        distance = np.sqrt(((RMS_sitting_x[j] - RMS_test_x[i])**2) + ((RMS_sitting_y[j] - RMS_test_y[i])**2) + ((RMS_sitting_z[j] - RMS_test_z[i])**2))
        if distance <= predict_distance:
            count_sit += 1
    
    for j in range(7):
        distance = np.sqrt(((RMS_jagging_x[j] - RMS_test_x[i])**2) + ((RMS_jagging_y[j] - RMS_test_y[i])**2) + ((RMS_jagging_z[j] - RMS_test_z[i])**2))
        if distance <= predict_distance:
            count_run += 1

    for j in range(7):
        distance = np.sqrt(((RMS_walking_x[j] - RMS_test_x[i])**2) + ((RMS_walking_y[j] - RMS_test_y[i])**2) + ((RMS_walking_z[j] - RMS_test_z[i])**2))
        if distance <= predict_distance:
            count_walk += 1

    if count_run >= max_num:
        max_type = "run"
        max_num = count_run
    if count_walk >= max_num:
        max_type = "walk"
        max_num = count_walk
    if count_sit >= max_num:
        max_type = "sit"
        max_num = count_sit
    
    result_num[i] = max_num
    result_type[i] = max_type

for i in range(10):
    print("test" + str(i+1))
    print(result_type[i]+"\nbecause"+str(result_num[i]) + "\n")

