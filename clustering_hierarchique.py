import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def genDendrogram(name, linkage_matrice, savePath, method):
    plt.figure(figsize=(25, 10))
    dendrogram(
        linkage_matrice,
        leaf_rotation=90.,
        leaf_font_size=8.,
    )
    plt.title("Clustering hiérarchique")
    plt.savefig(savePath + f"{name}_{method}.png")


def transformMatriceSimilToDistance(simil_matrice):
    for i in range(len(simil_matrice)):
        simil_matrice[i] = 1 - simil_matrice[i]
    return simil_matrice


def getDendrogram(name, dist_matrice=[], simil_matrice=[], savePath='', method='single'):
    if len(dist_matrice) < 1 and len(simil_matrice) < 1:
        print("Renseignez une matrice de distance ou une matrice de similarité")
        return
    if len(dist_matrice) > 0 and len(simil_matrice) > 0:
        print("Renseignez une seule des deux matrices")
        return
    if len(simil_matrice) > 0:
        dist_matrice = transformMatriceSimilToDistance(simil_matrice)

    linkage_matrice = linkage(dist_matrice, method=method)
    genDendrogram(name, linkage_matrice, savePath, method)
    print("Dendrograme '" + name + "_" + method + "' généré et sauvegardé")


if __name__ == '__main__':
    savePath = "hierarchic_graphs/"

    # Avec Matrice de distance
    name1 = "Ex.1"
    dist_matrice = [0.1, 0.9, 0.35, 0.8, 0.3, 0.4, 0.5, 0.6, 0.7, 0.2]

    getDendrogram(name1, dist_matrice=dist_matrice, method='single', savePath=savePath)
    getDendrogram(name1, dist_matrice=dist_matrice, method='complete', savePath=savePath)

    # Avec Matrice de similarité
    name2 = "Ex.2"
    simil_matrice = [0.1, 0.41, 0.64, 0.55, 0.47, 0.44, 0.35, 0.98, 0.85, 0.76]

    getDendrogram(name2, simil_matrice=simil_matrice, method='single', savePath=savePath)
    getDendrogram(name2, simil_matrice=simil_matrice, method='complete', savePath=savePath)
