import pandas as pd  #使用pandas進行表格處理

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

abalone = pd.read_csv(url, header=None) #讀取網路上的表格
abalone.columns = [ 'Sex', 'Length', 'Diameter', 'Height', 'Whole weight','Shucked weight','Viscera weight','Shell weight','Rings'] #加上欄位名稱

print(abalone) #列印表格

import matplotlib.pyplot as plt #使用matplatlib製圖
abalone['Rings'].hist(bins=15)  # 以Rings為橫軸，統計個案數，列出做多15條
plt.show()

abalone2=abalone.drop('Sex',axis=1)
correlation_matrix = abalone2.corr()
print(correlation_matrix)
print(correlation_matrix['Rings'])

X = abalone.drop("Rings", axis=1)  #取Rings欄位以外的所有資料
X = X.drop("Sex", axis=1) #刪除Sex欄位
X = X.values #僅取數值，不取欄位名稱
y = abalone["Rings"] #取Rings欄位的資料
y = y.values #僅取數值，不取欄位名稱

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)

from sklearn.neighbors import KNeighborsRegressor
knn_model = KNeighborsRegressor(n_neighbors=3) #使用kNN(k=3)來訓練
knn_model.fit(X_train, y_train) #使用kNN(k=3)來訓練

import numpy as np 
new_data_point = np.array([ 
    0.569552,
    0.446407,
    0.154437,
    1.016849,
    0.439051,
    0.222526,
    0.291208, 
])

sci_learn_prediction = knn_model.predict([new_data_point])
print("Sci Learn prediction:")
print(sci_learn_prediction)




