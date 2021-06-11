from random import uniform
from math import sqrt, inf
import numpy as np


def update_k_centers(k_clusters, min_dim, max_dim, dimensions):
    k_centers = []
    for k in range(len(k_clusters)):
        if not k_clusters[k]:
            k_center = []
            for i in range(dimensions):
                min_val = min_dim[i]
                max_val = max_dim[i]
                k_center.append(uniform(min_val, max_val))
        else:
            points = k_clusters[k]
            k_center = []
            for i in range(dimensions):
                val = np.mean(np.array(points)[:, i])
                k_center.append(val)
        k_centers.append(k_center)
    return k_centers


def cluster_points(data_points, k_centers):
    k_clusters = dict()
    for i in range(len(k_centers)):
        k_clusters[i] = []
    for point in data_points:
        shortest = inf
        shortest_k = 0
        for i in range(len(k_centers)):
            val = distance(point, k_centers[i])
            if val < shortest:
                shortest = val
                shortest_k = i
        k_clusters[shortest_k].append(point)
    return k_clusters


def distance(a, b):
    dimensions = len(a)
    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)


def generate_k(data_set, k):
    k_centers = []
    dimensions = len(data_set[0])
    min_dim = [inf for _ in range(dimensions)]
    max_dim = [-inf for _ in range(dimensions)]
    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_dim[i] = min(val, min_dim[i])
            max_dim[i] = max(val, max_dim[i])

    for kn in range(k):
        k_center = []
        for i in range(dimensions):
            min_val = min_dim[i]
            max_val = max_dim[i]
            k_center.append(uniform(min_val, max_val))
        k_centers.append(k_center)

    return k_centers, min_dim, max_dim, dimensions


def k_means(dataset: list, k: int):
    old_k_centers = None
    k_centers, min_dim, max_dim, dimensions = generate_k(dataset, k)
    while old_k_centers != k_centers:
        k_clusters = cluster_points(dataset, k_centers)
        old_k_centers = k_centers
        k_centers = update_k_centers(k_clusters, min_dim, max_dim, dimensions)
    return k_centers


if __name__ == "__main__":
    pass
