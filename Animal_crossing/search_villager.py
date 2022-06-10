import pandas as pd

df = pd.read_csv("data/animal_villager.csv")

#'住民名'列をindexに変更
df.set_index("住民名", inplace=True)

#辞書を定義
villager = {}
 
#各行を辞書に追加
for i in range(len(df)):
    #行データを抽出
    row = df.iloc[i]
    
    #データを辞書型に変換して辞書に追加
    villager[row.name] = dict(row)

#日本語名を入力して結果が返ってくるように表示する．
print(villager[input("名前を入力してください: ")])
