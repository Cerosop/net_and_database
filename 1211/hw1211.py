import pandas as pd  
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import numpy as np

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

abalone = pd.read_csv(url, header=None) #讀取網路上的表格
abalone.columns = [ 'Sex', 'Length', 'Diameter', 'Height', 'Whole weight','Shucked weight','Viscera weight','Shell weight','Rings'] #加上欄位名稱
abalone=abalone.drop('Sex',axis=1)

X = abalone.drop("Rings", axis=1)  #取Rings欄位以外的所有資料
X = X.values #僅取數值，不取欄位名稱
y = abalone["Rings"] #取Rings欄位的資料
y = y.values #僅取數值，不取欄位名稱

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12345)

knn_model = KNeighborsRegressor(n_neighbors=3) #使用kNN(k=3)來訓練
knn_model.fit(X_train, y_train) #使用kNN(k=3)來訓練

 
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
print(sci_learn_prediction[0])
print()


distances=np.linalg.norm(X-new_data_point, axis=1) #計算資料案例與新案例的距離list
k = 3
nearest_neighbor_ids = distances.argsort()[:k] #排序距離list並取前k個案例
nearest_neighbor_rings = y[nearest_neighbor_ids] 
prediction = nearest_neighbor_rings.mean() 

print("my prediction:")
print(prediction)





