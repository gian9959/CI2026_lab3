from random import sample, random
from optimal_test import brute_force

N = 10
C = 5

CHILDREN = [
    {   "name": f"{n}",
        "chars": [sample([True, False], 1)[0] for c in range(C)]}
    for n in range(N)
]

POP_SIZE = 50
GENERATIONS = 100

def fitness(sol):
    fit = 0
    if None not in sol:
        for i in range(N):
            a = sol[i]["chars"]
            b = sol[(i + 1) % N]["chars"]
            fit += sum(x != y for x, y in zip(a, b))
    return fit

def select_parents(pop, sample_size=3):
    parents = sorted(sample(pop, sample_size), key=lambda i: fitness(i), reverse=True)
    return sample([parents[0], parents[1]], 2)

def crossover(sol_1, sol_2):
    half = N//2

    sol_c = [None] * N
    sol_c[0:half] = sol_1[0:half]
    rest = [r for r in sol_2 if r not in sol_c[0:half]]

    for j, i in enumerate(range(half, N)):
        sol_c[i] = rest[j]
    return sol_c

def mutate(sol, rate=0.1):
    if random() < rate:
        i_0, i_1 = sample(range(N), 2)
        sol[i_0], sol[i_1] = sol[i_1], sol[i_0]
    return sol

population = [sample(CHILDREN, N) for p in range(POP_SIZE)]
best = { "solution": None, "fitness": 0}
for g in range(GENERATIONS):
        ordered_pop = sorted(population, key=lambda i: fitness(i), reverse=True)
        best_fit = fitness(ordered_pop[0])
        if best_fit > best["fitness"]:
            best = { "solution": ordered_pop[0], "fitness": best_fit}
        new_population = [best["solution"]]
        while len(new_population) < POP_SIZE:
            p_1, p_2 = select_parents(population)
            child = mutate(crossover(p_1, p_2))
            new_population.append(child)
        population = new_population
        print(f"GENERATION {g+1}:")
        print(f"Best solution: {[b['name'] for b in best['solution']]}")
        print(f"Best fitness: {best['fitness']}")
        print()

print(f"OVERALL SOLUTION")
print(f"{best['solution']}")
print(f"Fitness: {best['fitness']}")
print()
# print(f"BEST POSSIBLE SOLUTION:")
# brute = brute_force(best["solution"])
# print(brute[0])
# print(f"Fitness: {brute[1]}")
