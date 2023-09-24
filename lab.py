#test
from itertools import permutations
from tsp import *
import matplotlib


locs = random_locations(10)
print(locs)
print(locs[6])
print(locs[6][1])

def total_dist(seq, dists):
    tot_dist = 0
    for i in range(len(seq)):
        if i+1 < len(seq):
            tot_dist += dists[seq[i]][seq[i+1]]
        else:
            tot_dist += dists[seq[-1]][seq[0]]
    return tot_dist
# print(total_dist([4, 1, 0, 3, 2], dists = distance_matrix(random_locations(5))))



def exhaustive_search(locs):
    n = distance_matrix(locs)
    best_seq = None
    best_dist = 1000000
    for seq in permutations(range(len(locs)), len(locs)):
        if total_dist(seq, distance_matrix(locs)) < best_dist:
            best_dist = total_dist(seq, distance_matrix(locs))
            best_seq = seq
    return best_seq, best_dist


locs = random_locations(10)
best_seq, best_dist = exhaustive_search(locs)
print(best_seq)
print(best_dist)


locs = random_locations(10)

seq = random_tour(locs)
plot_tour(seq, locs, "Random Tour")

best_seq, best_dist = exhaustive_search(locs)
plot_tour(best_seq, locs, "Exhaustive Search")


def greedy_search(locs):
    distances = distance_matrix(locs)
    to_visit = list(range(1, len(locs)))
    seq = []
    current_loc = 0

    while len(to_visit) > 0:
        new_loc = to_visit[0]
        for i in to_visit:
            if distances[current_loc][i] != 0.0:
                if distances[current_loc][i] < distances[current_loc][new_loc]:
                    new_loc = i

        to_visit.remove(new_loc)
        seq.append(new_loc)
        current_loc = new_loc

    return seq, total_dist(seq, distance_matrix(locs))

locs = random_locations(10)
seq, dist = greedy_search(locs)
print(seq)
print(dist)

locs = random_locations(10)

seq = random_tour(locs)
plot_tour(seq, locs, "Random Tour")

seq, dist = exhaustive_search(locs)
plot_tour(seq, locs, "Exhaustive Search")

seq, dist = greedy_search(locs)
plot_tour(seq, locs, "Greedy Search")
"""
Greedy search appears to be more organized than the random tour, there is a logical pattern in how each location
is visited in a certain order. The graphs they produce are very different.
"""


max_n = 10

exhaustive_times = [time_search(exhaustive_search, n) for n in range(2, max_n)]
plot_times(exhaustive_times, "Exhaustive Search Times")

greedy_times = [time_search(greedy_search, n) for n in range(2, max_n)]
plot_times(greedy_times, "Greedy Search Times")

"""
It looks like as the location changes, time increases linearly for greedy_search and exponentially for
exhaustive_search()
"""
"""
After executing exhaustive_search() for 10 locations it appears that it will run for 90 seconds on an Apple M1 Chip, which is 2.853881278538813e-06 years.
Therefore, 20 locations will be 2.853881278538813e-06*2, and that is 5.707762557077626e-06 years.
"""

max_n = 201

greedy_times = [time_search(greedy_search, n) for n in range(2, max_n)]
plot_times(greedy_times, "Greedy Search Times Large")

locs = random_locations(max_n)
seq, dist = greedy_search(locs)
plot_tour(seq, locs, "Greedy Search Large")

