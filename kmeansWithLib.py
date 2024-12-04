from sklearn.cluster import KMeans
from numpy import array



if __name__ == '__main__':

    data_1d = [[1], [2], [18], [20], [31]]
    data_2d = [[-2, 3], [-2, 1], [-2, -1], [2, -1], [2, 1], [1, 0]]

    print("=============================")
    print("With Kmeans from Sklearn : ")
    print("=============================")

    print(f"\ntest de {data_1d}")
    print("\nTest 1D with centroids [[2], [6]]")
    print(KMeans(n_clusters=2, n_init=1, init=array([[2], [6]])).fit(data_1d).labels_)
    print("\nTest 1D with centroids [[12], [24]]")
    print(KMeans(n_clusters=2, n_init=1, init=array([[12], [24]])).fit(data_1d).labels_)

    print(f"\ntest de {data_2d}")
    print("\nTest 2D with centroids [[-2, 3], [-2, 1]]")
    print(KMeans(n_clusters=2, n_init=1, init=array([[-2, 3], [-2, 1]])).fit(data_2d).labels_)
    print("\nTest 2D with centroids [[2, -1], [1, 0]]")
    print(KMeans(n_clusters=2, n_init=1, init=array([[2, -1], [1, 0]])).fit(data_2d).labels_)
