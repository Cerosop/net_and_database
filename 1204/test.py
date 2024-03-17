from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


def my_kmeans(X):
    labels = None
    centroids = X[np.random.choice(len(X), 4, replace=False)]
    for _ in range(300):
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(4)])
        if np.linalg.norm(new_centroids - centroids) < 1e-4:
            break
        centroids = new_centroids
    return labels, centroids


def sklearn_kmeans(features):
    scalar = StandardScaler()
    scaled_feature = scalar.fit_transform(features)

    kmeans = KMeans(
        init="random",
        n_clusters=4,
        n_init=10,
        max_iter=300,
        random_state=42
    )
    kmeans.fit(scaled_feature)
    kmeans.predict(scaled_feature)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids


if __name__ == '__main__':
    features, true = make_blobs(
        n_samples=400, centers=4, cluster_std=2.75, random_state=42
    )
    
    labels, centroids = my_kmeans(features)
    plt.scatter(features[:, 0], features[:, 1], c=labels, cmap='viridis', edgecolors='k')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=3, color='red')
    plt.title('K-means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()