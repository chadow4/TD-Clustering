from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt
from clustering_kmeans import getDistance

def genDistanceMatrix(points, normalize=False) :
    dist_matrice = []
    # Créer une matrice avec les distances réelles (euclidiennes)
    for i in range(len(points)) :
        for j in range(i+1, len(points)) :
            dist_matrice.append(getDistance(points[i], points[j]))

    # Normaliser la matrice pour avoir des valeurs entre 0 et 1
    if normalize :
        distMin, distMax = min(dist_matrice), max(dist_matrice)
        for i in range(len(dist_matrice)) :
            dist_matrice[i] = (dist_matrice[i] - distMin) / (distMax - distMin)
    
    return dist_matrice

def genDendrogram(name, labels, linkage_matrice, savePath, method,orientation) :
    plt.figure(figsize=(50, 20))
    dendrogram(
        linkage_matrice,
        orientation=orientation,
        leaf_font_size=8.,
        labels=labels,
    )
    plt.title(f"Clustering hiérarchique - {name} - {method} link")
    plt.savefig(savePath + f"{name}_{method}.pdf")
    plt.close()

def transformMatriceSimilToDistance(simil_matrice) :
    for i in range(len(simil_matrice)) :
        simil_matrice[i] = 1-simil_matrice[i]
    return simil_matrice

def getDendrogram(name, labels=None, dist_matrice=[], simil_matrice=[], savePath='', method='single',orientation="top") :
    if len(dist_matrice)<1 and len(simil_matrice)<1 :
        print("Renseignez une matrice de distance ou une matrice de similarité")
        return
    if len(dist_matrice)>0 and len(simil_matrice)>0 :
        print("Renseignez une seule des deux matrices")
        return
    if len(simil_matrice)>0 :
        dist_matrice = transformMatriceSimilToDistance(simil_matrice)

    linkage_matrice = linkage(dist_matrice, method=method)
    genDendrogram(name, labels, linkage_matrice, savePath, method,orientation)
    print("Dendrograme '" + name + "_" + method + "' généré et sauvegardé")


if __name__ == '__main__':

    savePath = "hierarchic_graphs/"

    # Avec Matrice de distance
    name1 = "Ex.1"
    dist_matrice = [0.1, 0.9, 0.35, 0.8, 0.3, 0.4, 0.5, 0.6, 0.7, 0.2]
    labels = ['p1','p2','p3','p4','p5',]

    getDendrogram(name1, labels=labels, dist_matrice=dist_matrice, method='single', savePath=savePath)
    getDendrogram(name1, labels=labels, dist_matrice=dist_matrice, method='complete', savePath=savePath)

    # Avec Matrice de similarité
    name2 = "Ex.2"
    simil_matrice = [0.1, 0.41, 0.64, 0.55, 0.47, 0.44, 0.35, 0.98, 0.85, 0.76]
    labels = ['p1','p2','p3','p4','p5',]

    getDendrogram(name2, labels=labels, simil_matrice=simil_matrice, method='single', savePath=savePath)
    getDendrogram(name2, labels=labels, simil_matrice=simil_matrice, method='complete', savePath=savePath)
    