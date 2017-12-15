import pandas as pd

df = pd.read_csv("2016CoralBacteria1e.csv")
df2 = pd.read_csv("spc.csv")


###Name配列に列名をカンマで分けて保存
M = df.columns
M = M[1:,]
Name = []
for i in range(len(M)):
    Name.append(M[i].split("."))

###phylumの種類を取得?ダブりがないようにまとめる
memo = []
for i in range(len(Name)):
    if Name[i][1] not in memo:
        memo.append(Name[i][1])

###phryum別のindexを取得,辞書にまとめる
queue = [[] for i in range(len(memo))]
memo2 = []
index = -1
for i in range(len(Name)):
    if Name[i][1] not in memo2:
        index += 1
        memo2.append(Name[i][1])
    queue[index].append(i)

dict = {}
n = 0

for i in memo:
    dict[i] = queue[n]
    n += 1

Mat = df.values
Mat2 = Mat[0:12,1:]

res = [[0 for i in range(len(memo))]for i in range(len(Mat2))]
'''
len(Mat) = 12
len(memo)=17
'''

#門ごとに集計
for i in range(len(Mat2)):
    for j in memo:
        sum = 0
        for k in dict[j]:
            sum += int(Mat2[i][k])
        res[i][memo.index(j)] += sum


###Dataframeにするために行名による辞書化
dict2 = {}
n = 0
for i in Mat[0:12,0]:
    dict2[i] = res[n]
    n += 1


###dataframeに変換,転置
data = pd.DataFrame(dict2,index=memo)
data= data.T

###書き出し
data.to_csv("phylum.csv")