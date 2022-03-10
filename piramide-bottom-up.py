# 0        1
# 0 1      5 7
# 0 1 2    9 3 8

from random import randint


def min_sum(piramide):
    return solve_bottom_up(piramide)


def solve_bottom_up(piramide):
    # altura da piramide
    n = len(piramide)

    # inicializa matriz de custos zerados
    memo = []
    for i in range(n):
        custos_linha = []
        for j in range(i + 1):
            custos_linha.append(0)
        memo.append(custos_linha)

    # preenche matriz bottom-up
    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            if i == n - 1:
                # base da piramide
                memo[i][j] = piramide[i][j]
            else:
                memo[i][j] = piramide[i][j] + min(memo[i + 1][j], memo[i + 1][j + 1])

    # print(memo)
    return memo[0][0]


# main ==============================================================================

# p = [
#     [1],
#     [5, 7],
#     [9000, 3000, 8]
# ]

while True:
    n = int(input("tamanho da piramide: "))
    if n < 1:
        break

    p = []
    # inicializa a piramide com valores aletorios
    for i in range(n):
        linha = []
        for j in range(i + 1):
            linha.append(randint(0, 9))
        p.append(linha)

    # print(p)

    print("menor soma possível =", min_sum(p))
