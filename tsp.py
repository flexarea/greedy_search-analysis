from random import random, shuffle
from matplotlib import pyplot as plt
from time import time

def distance(x, y):
    """
    compute the Euclidean distance between two 2d points x and y
    """
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def random_locations(n):
    """
    generate n random 2d points
    """
    points = [(random(), random()) for i in range(n)]
    return points

def distance_matrix(points):
    """
    compute the matrix of euclidean distances between all pairs of points passed in a list. 
    The matrix is represented as a list of lists, so the distance between points i and j is dists[i][j]
    """
    n = len(points)
    distances = [[distance(points[i], points[j]) for i in range(n)] for j in range(n)]
    return distances

def plot_points(points):
    x = [points[i][0] for i in range(len(points))]
    y = [points[i][1] for i in range(len(points))]
    plt.scatter(x, y, color = "black", zorder = 100)
    plt.show()

def plot_tour(seq, points, title):
    """
    Visualize a path through a sequence of points and save it to the img directory. 
    """
    n = len(points)
    x = [points[seq[i]][0] for i in range(n)]
    x.append(points[seq[0]][0])
    y = [points[seq[i]][1] for i in range(n)]
    y.append(points[seq[0]][1])
    plt.plot(x, y)
    plt.scatter(x, y, color = "black", zorder = 100)
    plt.scatter(x[0], y[0], color = "orange", zorder = 100)
    
    dists = distance_matrix(points)
    n = len(seq)
    dist = 0
    for i in range(n-1):
        dist += dists[seq[i]][seq[i+1]]
    dist += dists[seq[n-1]][seq[0]]

    plt.title(f"{title}\nDistance traveled: {dist:.2f}km")
    plt.gca().set_xlim(0, 1)
    plt.gca().set_ylim(0, 1)
    
    plt.savefig(f"img/{title}.png")
    plt.close()
    # plt.show()

def plot_times(times, title):
    """
    Visualize a series of timing results and save them to the img directory. 
    """
    plt.scatter(range(2, len(times)+2), times)
    plt.title(f"{title}")
    plt.gca().set_xlabel("Number of locations to visit")
    plt.gca().set_ylabel("Time elapsed (seconds)")
    plt.savefig(f"img/{title}.png")
    plt.close()
    # plt.show()
    

def random_tour(points):
    """
    create a random sequence of points. 
    """
    s = list(range(len(points)))
    shuffle(s)
    return s    

def time_search(search_fun, n):
    """
    time the result of running a search function on a problem of size n. 
    """
    points = random_locations(n)
    dists = distance_matrix(points)
    
    start = time()
    seq, dist = search_fun(dists)
    end = time()
    
    return end - start