import numpy as np

ITERATIONS = 100


### TODO 1: Compute stochastic matrix M
def getM(L):
    # TODO1: Compute stochastic matrix M
    matrix = np.zeros([len(L), len(L)], dtype=float)
    # number of outgoing links
    c = np.zeros([len(L)], dtype=float)

    for i in range(0, len(L)):
        c[i] = sum(L[i])
        for j in range(0, len(L)):
            if L[i][j] == 1:
                matrix[i][j] = 1 / c[i]
    return matrix


def pageRank(M, q):
    # TODO2: compute PageRank with damping factor q (method parameter)
    pagerank = np.ones([len(M)], dtype=float)

    for i in range(0, ITERATIONS):
        for j in range(0, len(M)):
            pageRankValue = 0
            for k in range(0, len(M)):
                pageRankValue += pagerank[k] * M[k][j]
            pagerank[j] = ((1 - q) * pageRankValue) + q

    return pagerank


def trustRank(M, q):
    # TODO3: compute TrustRank with damping factor q (method parameter)
    # pages 1 and 2 are good (indexes 0 and 1)
    # return array of TrustRank values (indexes: page number - 1, e.g. result[0] = TrustRank of page 1).
    trustrank = np.zeros([len(M)], dtype=float)
    trustrank[0] = 1
    trustrank[1] = 1
    trustrankSum = sum(trustrank)

    for i in range(0, len(M)):
        trustrank[i] = (trustrank[i] / trustrankSum)

    for i in range(0, ITERATIONS):
        for j in range(0, len(M)):
            trustRankValue = 0
            for k in range(0, len(M)):
                trustRankValue += trustrank[k] * M[k][j]
            trustrank[j] = ((1 - q) * trustRankValue) + q * trustrank[j]
    return trustrank


def sortAndPrint(vector):
    arr = []
    for i in range(0, 10):
        arr.append((i, vector[i]))
    arr.sort(key=lambda x: (x[1]), reverse=True)
    for i in range(0, 10):
        print(str(arr[i][0] + 1) + " : " + str(arr[i][1]))


L1 = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
L2 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
L3 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
L4 = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
L5 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
L6 = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
L7 = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
L8 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
L9 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
L10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

L = np.array([L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
q = 0.15

print("Matrix L (indices)")
print(L)

M = getM(L)

print("Matrix L (indices)")
print(L)

M = getM(L)

print("Matrix M (stochastic matrix)")
print(M)

print("PAGERANK")

pr = pageRank(M, q)
sortAndPrint(pr)

print()
print("TRUSTRANK (DOCUMENTS 1 AND 2 ARE GOOD)")
pr = trustRank(M, q)
sortAndPrint(pr)

print()
print("TRUSTRANK (AFTER REMOVING CONNECTIONS)")
L[0][4] = 0
L[2][6] = 0
M = getM(L)
pr = trustRank(M, q)
sortAndPrint(pr)
