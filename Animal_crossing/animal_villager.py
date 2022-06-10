import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL定義
villager_url = "https://www.doumori.com/guide/people_birthday.html"
 
# HTML取得
r = requests.get(villager_url)
soup = BeautifulSoup(r.content, "html.parser")

#リストを定義 ここに各行（住民のデータ）を加えていく．
rows = []
 
#各行を処理する
for tr in soup.find("table", {"id":"myTable1"}).find_all("tr"):
    #thタグがあればtableのカラムとしてデータを取得
    if tr.find("th"):
        columns = [x.getText().strip() for x in tr.find_all("th")]
 
    #tdタグがあればリストに挿入
    if tr.find("td"):
        rows.append([x.getText().strip() for x in tr.find_all("td")])

#DataFrameに変換する
df = pd.DataFrame(rows,columns=columns)

#CSVファイルに保存
df.to_csv("data/animal_villager.csv", sep= ',', header = True, index = False)
