import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

centers = [[1,2],[4,4],[2,10]]
X, _ = make_blobs(n_samples = 500, centers = centers, cluster_std = 1)

plt.scatter(X[:,0],X[:,1])
plt.show()

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
n_clusters_ = len(np.unique(labels))

print("Numbers of estimated clusters : ",n_clusters_)
print("Center Points are....\n",cluster_centers)
colors = 10 * ['r.', 'm.', 'g.', 'b.', 'k.', 'y.']

print(colors)
print(labels)
for i in range(len(X)) :
    plt.plot(X[i][0],X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(cluster_centers[:,0],cluster_centers[:,1],
            marker="x", s=150, linewidths=5,zorder=10)
plt.show()

