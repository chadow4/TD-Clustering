import csv

from numpy import array, identity, transpose, matmul, std, mean
from numpy.linalg import eig

from clustering_kmeans import kmeans
from clustering_hierarchique import genDistanceMatrix, getDendrogram


def parseCSV(csv_file='Country-data.csv'):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        countries = []
        data = []
        for row in csv_reader:
            countries.append(row[0])
            data.extend(map(float, row[1:]))
    return countries, data


countries, data_country = parseCSV()
#print(countries)
#print(data_country)

X = array(data_country).reshape(-1, 9)
n = len(countries)
p = X.shape[1]
Y = X - matmul(transpose(array([n * [1]])), transpose(array([[mean(variable)] for variable in transpose(X)])))
Z = matmul(Y, array(list(map(lambda variable: [1. / std(variable)], transpose(X)))) * identity(p))
R = matmul(matmul(transpose(Z), 1. / n * identity(n)), Z)
eigenvectors = eig(R)[1]
components = [matmul(Z, eigenvectors[:, 0]), matmul(Z, eigenvectors[:, 1])]
data_reduced = [[round(float(components[0][i]), 2), round(float(components[1][i]), 2)] for i in range(n)]
#print(data_reduced)

k_2 = 2
point_names_2 = countries
fileDataName = "data_country"
fileDataName2 = "data_country2"
savePath = 'caseStudies_graphs/'
scale = 0.00000000000000001

if __name__ == '__main__':


    kmeans(data_reduced,
           k_2,
           point_names=point_names_2,
           saveFigs=True,
           savePath=savePath,
           filename=fileDataName,
           scale=scale)

    kmeans(data_reduced,
           3,

           point_names=point_names_2,
           saveFigs=True,
           savePath=savePath,
           filename=fileDataName2,
           scale=scale)


    countries_distance_matrice = genDistanceMatrix(data_reduced)
    getDendrogram("Countries", countries, dist_matrice=countries_distance_matrice, savePath=savePath, method="single",orientation="right")

    getDendrogram("Countries", countries, dist_matrice=countries_distance_matrice, savePath=savePath, method="complete",orientation="right")
