from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

points = ['p1', 'p2', 'p3', 'p4', 'p5', 'p1', 'p2', 'p3', 'p4', 'p5']
dist_matrice = [0.1, 0.9, 0.35, 0.8, 0.3, 0.4, 0.5, 0.6, 0.7, 0.2]

linkage_matrice = linkage(dist_matrice)

plt.figure(figsize=(25, 10))
dendrogram(
    linkage_matrice,
    leaf_rotation=90.,
    leaf_font_size=8.,
)
plt.show()