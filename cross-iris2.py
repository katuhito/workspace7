import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# アヤメのCSVデータを読み込む
df = pd.read_csv('iris.csv')

# リストを訓練データとラベルに分割する
data = df[["SepalLength","SpealWidth","PetalLength","PetalWidth"]]
label = df["Name"]

# クロスバリデーションを行う
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("各正解率=", scores)
print("正解率=", scores.mean())