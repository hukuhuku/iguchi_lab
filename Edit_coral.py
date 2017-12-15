import pandas as pd

#CoralBacteria1eファイルに区分以外でカンマが使われている箇所があったので
#手作業で取り除いたものを2eファイルとして保存した
df = pd.read_csv("2016_CoralBacteria3e.csv")

M = df.columns
M = M[1:,]

Name = []

#Name配列に列名をカンマで分けて保存
for i in range(len(M)):
    Name.append(M[i].split("."))

#Other,Unassingment以外の先頭三文字を取り除く
for i in range(len(Name)):
    for j in range(len(Name[i])):
        if Name[i][j] != "Other" and Name[i][j] != "Unassigned":
            Name[i][j] = Name[i][j][3:]

#区分別に分ける
df2 = []

for i in range(len(Name[0])):
    S = []
    for j in range(len(Name)):
        S.append(Name[j][i])
    df2.append(S)

df3 = pd.DataFrame([df2[i] for i in range(7)])
df4 = pd.DataFrame(['k','p','c','o','f','g','s'])
df5 = pd.concat([df4,df3],axis=1)

#行名、列名を元のcsvファイルと同じにする
df5.columns = df.columns

#結合(必要ないかも)
#pd.concat([df,df5])

#書き出し
df5.to_csv("spk.csv")