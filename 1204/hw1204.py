import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

features, true_labels = make_blobs(
    n_samples=400, 
    centers=4, 
    cluster_std=2.75, 
    random_state=42
)
#產生clustering測試資料


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
#將資料進行標準化
plt.figure()
plt.scatter(scaled_features[:,0], scaled_features[:,1], c=true_labels, s=30)
plt.title('Dataset')
# plt.show()

kmeans = KMeans(
    init="random", n_clusters=4,
    n_init=10, max_iter=300,
    random_state=42
)

kmeans.fit(scaled_features)
#套入剛剛產生的資料
print(kmeans.n_iter_) #收斂所需的迭代次數
print(kmeans.cluster_centers_)

plt.figure()
plt.scatter(scaled_features[:,0], scaled_features[:,1], c=kmeans.labels_, s=30)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'black', s = 80, marker='*')
plt.title('Dataset2')
# plt.show()


centers = scaled_features[np.random.choice(len(scaled_features), 4, replace=False)]
# print(centers)
_ = 0
for _ in range(300):
    distances = np.linalg.norm(scaled_features[:, np.newaxis] - centers, axis=2)
    labels = np.argmin(distances, axis=1)
    
    new_centers = np.array([scaled_features[labels == i].mean(axis=0) for i in range(4)])
    if np.linalg.norm(new_centers - centers) < 1e-4:
        break
    centers = new_centers
    
print(_)
print(centers)
plt.figure()
plt.scatter(scaled_features[:,0], scaled_features[:,1], c=labels, s=30)
plt.scatter(centers[:, 0], centers[:, 1], c = 'black', s = 80, marker='*')
plt.title('Dataset3')
plt.show()





