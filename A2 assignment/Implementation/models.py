import numpy as np

def bak_sneppen(N, n=1000000):
    species = [np.random.rand() for i in range(N)]
    for _ in range(n):
        indexMin = species.index(min(species))
        for i in [indexMin - 1, indexMin, indexMin + 1]:
            if i == N:
                i = 0
            species[i] = np.random.rand()
    return species

def gms(p, n):
    species = []
    for _ in range(n):
        if np.random.rand() < p:
            species.append(np.random.rand())
        else:
            if len(species):
                species.sort()
                species.pop(0)
    return species
