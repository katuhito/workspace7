import pandas as pd
from sklearn import svm, metrics

# XORの演算結果
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 入力を学習データとラベルに分ける
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.iloc[:,0:1]
xor_label = xor_df.iloc[:,2]

# データの学習と予測
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 正解率を求める
sc_score = metrics.accuracy_score(xor_label, pre)
print("正解率=", sc_score)