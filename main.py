from itertools import permutations
from random import sample, randint

N = 10
C = 5

CHILDREN = [
    {   "name": f"{n}",
        "chars": [sample([True, False], 1)[0] for c in range(C)]}
    for n in range(N)
]

def fitness(sol):
    fitness = 0
    for i in range(N):
        c_0 = sol[i]
        c_1 = sol[(i+1) % N]
        c_2 = sol[(i+2) % N]
        for j, ch in enumerate(c_1["chars"]):
            if ch != c_0["chars"][j]:
                fitness += 1
            if ch != c_2["chars"][j]:
                fitness += 1
    return fitness

def tweak(sol):
    i_0, i_1 = sample(range(N), 2)
    tmp = sol[i_0]
    sol[i_0] = sol[i_1]
    sol[i_1] = tmp
    return sol

solution = CHILDREN
for i in range(1000):
    new_solution = tweak(solution.copy())
    new_fitness = fitness(new_solution)
    if new_fitness > fitness(solution):
        solution = new_solution
        print(f"FITNESS: {new_fitness}")
        print()