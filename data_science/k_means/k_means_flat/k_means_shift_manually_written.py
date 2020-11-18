import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.cluster import KMeans

style.use("ggplot")

data = np.array(
    [
        [20, 20],
        [-3.4, 20.8],
        [30, 8],
        [10, 80],
        [110, 0.6],
        [9, 11],
        [8, 2],
        [10, 3],
    ]
)


plt.scatter(data[:, 0], data[:, 1], s=150, linewidth=5)
plt.show()

colors = 10 * ["g", "r", "c", "b", "k"]


class Means_shift:
    def __init__(self, radius=None, radius_norm_step=100):
        self.radius = radius
        self.radius_norm_step = radius_norm_step
        self.radius = all_data_norm / self.radius_norm_step

    def fit(self, data):
        self.centroids = {}

        for i in range(len(data)):
            centroids = data[i]

        while True:
            new_centroids = []
            for i in centroids:
                in_bandwith = []
                centroids = centroids[i]
                for featureset in data:
                    if np.linalg.norm(featureset - centroids) < self.bandwith:
                        in_bandwith.append(featureset)

                new_centroid = np.average(in_bandwith, axis=0)
                new_centroids.append(tuple(new_centroid))

        uniques = sorted(list(set(new_centroids)))

        prev_centroids = dict(centroids)

        centroids = {}

        for i in range(len(uniques)):
            centroids[i] = np.array(uniques[i])

            optimized = True
            for i in centroids:
                if not np.array_equal(centroids[i], prev_centroids[i]):
                    optimized = False

                    if not optimized:
                        break

            if optimized:
                break

        self.centroids = centroids

    def predict():
        pass


clf = Means_shift()
clf.fit(data)

centroids = clf.centroids
plt.scatter(data[:, 0], data[:1], s=150)

for c in centroids:
    plt.scatter(centroids[c][9], centroids[c][1], color="k", marker="*", s=150)

plt.show()
