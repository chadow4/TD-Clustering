import random
from math import sqrt

import matplotlib.pyplot as plt


def getDistance(p1, p2):
    # Retourne la distance euclidienne entre deux points de même dimension.
    dist = 0
    dims = len(p1)
    for dim in range(dims):
        dist += (p2[dim] - p1[dim]) ** 2
    return sqrt(dist)


def getClosestCentroid(p, centroids):
    # Retourne le centroïde le plus proche du point donné.
    minDist = None
    for c in centroids:
        dist = getDistance(p, c)
        if (minDist == None) or (dist < minDist):
            minDist, closest_centroid = dist, c
    return closest_centroid


def getRandomCentroids(points, nbClusters):
    # Retourne une séléction de n éléments parmi une liste.
    return random.sample(points, nbClusters)


def determineNewCentroid(points):
    # Détermine le centroïde d'une liste de points de même dimension, en utilisant la moyenne pour chaque axe.
    dims = len(points[0])
    newCentroid = []
    for dim in range(dims):
        nc_pos = []
        for point in points:
            nc_pos.append(point[dim])
        newCentroid.append(sum(nc_pos) / len(nc_pos))
    return newCentroid


def getSSE(centroids, centrDict):
    # Retourne la Sum of Squared Error
    sse = 0
    for centroid in centroids:
        for point in centrDict[str(centroid)]:
            sse += getDistance(point, centroid) ** 2
    return sse


def getNameDict(points, point_names):
    # Crée et retourne un dictionnaire pour associer les coordonnées des noeuds avec les noms des noeuds
    nameDict = {}
    print(points)
    if len(point_names) > 0:
        for i in range(len(point_names)):
            nameDict[point_names[i]] = points[i]
    return nameDict


def getNameOfPoint(point, nameDict):
    # Retourne le nom du noeud à partir de ses coordonnées
    for key, value in nameDict.items():
        if point == value:
            return key
    return "unnamed"


def gen2dGraph(centroids, centrDict, nameDict, iteration, savePath, filename, scale):
    # Génère et sauvegarde un graphique du clustering
    availableColors = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'black', 'brown', 'grey']
    colorIdx = 0
    cx, cy, px, py, pcol, ccol = [], [], [], [], [], []

    fig, ax = plt.subplots(figsize=(5, 5) if scale == 1 else (15, 15))


    for centroid in centroids:
        for point in centrDict[str(centroid)]:
            px.append(point[0])
            py.append(point[1])
            ax.annotate(getNameOfPoint(point, nameDict), [point[0], point[1]])
            pcol.append(availableColors[colorIdx])
        cx.append(centroid[0])
        cy.append(centroid[1])
        ccol.append(availableColors[colorIdx])
        colorIdx += 1

    ax.scatter(cx, cy, c=ccol, marker='X')
    ax.scatter(px, py, c=pcol, marker='.')

    minX, maxX, minY, maxY = min(px), max(px), min(py), max(py)
    ax.set_xlim([minX - (scale * (maxX - minX)), maxX + (scale * (maxX - minX))])
    ax.set_ylim([minY - (scale * (maxY - minY)), maxY + (scale * (maxY - minY))])

    plt.grid(True)
    plt.title("K-Means, Iteration " + str(iteration))
    fig.savefig(savePath + f"Iteration_{filename}-{iteration}.pdf")
    plt.close(fig)


def kmeans(points, nbclusters, centroids=[], point_names=[], saveFigs=True, savePath='', filename='', iterMax=20,
           scale=1):
    # On définit le nombre d'itérations maximum.
    iteration, iterMax = 1, iterMax

    # On créé un dictionnaire pour mapper les noms des noeuds.
    nameDict = getNameDict(points, point_names)

    # On tire des centroïdes par défaut s'ils ne sont pas donnés.
    if len(centroids) == 0:
        centroids = getRandomCentroids(points, nbclusters)

    # Boucle principale.
    print("Début de l'algorithme K-Means...")
    for _ in range(iterMax):
        print('Iteration ' + str(iteration))
        # On initialise un dictionnaire {str(centroïde) : List[Points]}.
        centrDict = {}
        # Pour chaque point, on détermine son plus proche centroïde et on l'ajoute dans le dictionnaire à la clé correspondante.
        for p in points:
            closest_centroid = getClosestCentroid(p, centroids)
            if str(closest_centroid) in centrDict:
                centrDict[str(closest_centroid)].append(p)
            else:
                centrDict[str(closest_centroid)] = [p]

        # On initialise une liste qui contiendra les centroïdes pour l'itération suivante.
        newCentroids = []
        # Pour chaque cluster, on appelle une méthode qui détermine son nouveau centroïde.
        for centroid in centrDict.keys():
            print('Centroid : ' + str(centroid) + '   Points : ' + str(centrDict[str(centroid)]))
            newCentroids.append(determineNewCentroid(centrDict[str(centroid)]))

            # On sauvegarde le graphique des clusters pour l'itération courante dans le dossier spécifié.
        if saveFigs and len(points[0]) == 2:
            gen2dGraph(centroids, centrDict, nameDict, iteration, savePath, filename, scale)
            print(
                "Graphiques des clusters pour l'itération " + str(iteration) + " sauvegardé (path : " + savePath + ")")

        # Si convergence atteinte, on sort de la fonction en affichant le SSE.
        if centroids == newCentroids:
            print("Convergence atteinte.\nSSE : " + str(getSSE(centroids, centrDict)))
            return
        # Sinon, on met à jour les centroïdes pour une nouvelle itération.
        else:
            centroids = newCentroids
            iteration += 1
    # Si le nombre maximum d'itérations est atteint, on sort de la boucle en affichant le SSE.
    print("Nombre maximum d'itérations (" + iterMax + ") atteint.\nSSE : " + str(getSSE(centroids, centrDict)))


data_1 = [[1], [2], [18], [20], [31]]
initial_centroids_1 = [[18], [20], [31]]
point_names_1 = ['M1', 'M2', 'M3', 'M4', 'M5']
k_1 = 3

data_2 = [[-2, 3], [-2, 1], [-2, -1], [2, -1], [2, 1], [1, 0]]
initial_centroids_2 = [[-2, 3], [-2, 1]]
point_names_2 = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']
k_2 = 3
fileDataName = "data_2"
savePath = 'kmeans_graphs/'

if __name__ == '__main__':
    kmeans(data_1,  # Liste des points
           k_2,  # Nombre de clusters
           centroids=initial_centroids_1,  # Centroïdes initiaux (Optionel. Par défaut, ils seront tirés au hasard.)
           point_names=point_names_1,  # Nom des points (Optionel. Par défaut, les points ne seront pas nommés.)
           saveFigs=True,  # Sauvegarder les figures (Optionel. Par défaut, les figures ne seront pas sauvegardées.)
           savePath=savePath,
           filename=fileDataName)
# Répertoire RELATIF pour sauvegarder les graphiques (Optionel. Par défaut, les figures seront sauvegardées sur le même répertoire.)


    kmeans(data_2,  # Liste des points
           k_2,  # Nombre de clusters
           centroids=initial_centroids_2,  # Centroïdes initiaux (Optionel. Par défaut, ils seront tirés au hasard.)
           point_names=point_names_2,  # Nom des points (Optionel. Par défaut, les points ne seront pas nommés.)
           saveFigs=True,  # Sauvegarder les figures (Optionel. Par défaut, les figures ne seront pas sauvegardées.)
           savePath=savePath,
           filename=fileDataName)  # Répertoire RELATIF pour sauvegarder les graphiques (Optionel. Par défaut, les figures seront sauvegardées sur le même répertoire.)
