import csv

from numpy import array, identity, transpose, matmul, std, mean
from numpy.linalg import eig

from clustering_kmeans import kmeans


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
print(countries)
print(data_country)

X = array(data_country).reshape(-1, 9)
n = len(countries)
p = X.shape[1]
Y = X - matmul(transpose(array([n * [1]])), transpose(array([[mean(variable)] for variable in transpose(X)])))
Z = matmul(Y, array(list(map(lambda variable: [1. / std(variable)], transpose(X)))) * identity(p))
R = matmul(matmul(transpose(Z), 1. / n * identity(n)), Z)
eigenvectors = eig(R)[1]
components = [matmul(Z, eigenvectors[:, 0]), matmul(Z, eigenvectors[:, 1])]
data_reduced = [[round(float(components[0][i]), 2), round(float(components[1][i]), 2)] for i in range(n)]
print(data_reduced)

k_2 = 2
initial_centroids_2 = [[-100, 0], [100, 0]]
point_names_2 = countries
fileDataName = "data_country"
fileDataName2 = "data_country2"
savePath = 'caseStudies_graphs/'
scale = 0.00000000000000001

kmeans(data_reduced,  # Liste des points
       k_2,  # Nombre de clusters   # Centroïdes initiaux (Optionel. Par défaut, ils seront tirés au hasard.)
       point_names=point_names_2,
       centroids=initial_centroids_2,  # Nom des points (Optionel. Par défaut, les points ne seront pas nommés.)
       saveFigs=True,  # Sauvegarder les figures (Optionel. Par défaut, les figures ne seront pas sauvegardées.)
       savePath=savePath,
       filename=fileDataName,
       scale=scale)  # Répertoire RELATIF pour sauvegarder les graphiques (Optionel. Par défaut, les figures seront sauvegardées sur le même répertoire.)

kmeans(data_reduced,  # Liste des points
       3,
       centroids=initial_centroids_2,
       # Nombre de clusters   # Centroïdes initiaux (Optionel. Par défaut, ils seront tirés au hasard.)
       point_names=point_names_2,  # Nom des points (Optionel. Par défaut, les points ne seront pas nommés.)
       saveFigs=True,  # Sauvegarder les figures (Optionel. Par défaut, les figures ne seront pas sauvegardées.)
       savePath=savePath,
       filename=fileDataName2,
       scale=scale)  # Répertoire RELATIF pour sauvegarder les graphiques (Optionel. Par défaut, les figures seront sauvegardées sur le même répertoire.)
