def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        optimal_move = n % (m + 1)
        if optimal_move == 0:
            return m
        else:
            return optimal_move