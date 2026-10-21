from itertools import permutations

N = 10

def fitness(sol):
    fit = 0
    if None not in sol:
        for i in range(N):
            a = sol[i]["chars"]
            b = sol[(i + 1) % N]["chars"]
            fit += sum(x != y for x, y in zip(a, b))
    return fit

def brute_force(children):
    all = [[children[0]] + list(p) for p in permutations(children[1:])]
    best_fit = 0
    best_sol = None
    for a in all:
        fit = fitness(a)
        if fit > best_fit:
            best_sol = a
            best_fit = fit
    return best_sol, best_fit