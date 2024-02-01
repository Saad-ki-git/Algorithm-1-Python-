#What is monte Carlo Percolation Thresholds
# To estimate the percolation threshold, consider the following computational experiment:
# * Initialize all sites to be blocked.
# * Repeat the following until the system percolates:
# * Choose a site uniformly at random among all blocked sites.
# * Open the site.
# The fraction of sites that are opened when the system percolates provides an estimate of the percolation threshold.

import random
import statistics

class QuickUnion:
    def __init__(self, n):
        self.id = list(range(n))

    def root(self, i):
        while i != self.id[i]:
            i = self.id[self.id[i]]
        return i

    def connect(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id[p] = self.root(q)
        return self.id[p]

def Percolation(n, number_trials):
    percolation_thresholds = []

#Loop through the trial
    for _ in range(number_trials):
        quick_union = QuickUnion(n)

        #initially block all sites
        open_sites = 0
        while not quick_union.connect(0, n - 1): #if top is not connected to the bottom 
            site1 = random.randint(0, n - 1)
            site2 = random.randint(0, n - 1)
            quick_union.union(site1, site2) #then union the tow sites that are blocked to open them
            open_sites += 1 #increase the number of open sites

        # Calculate percolation threshold for this trial
        percolation_threshold = open_sites / (n * n)
        percolation_thresholds.append(percolation_threshold)

    # Calculate mean and standard deviation
    mean_threshold = statistics.mean(percolation_thresholds)
    std_deviation = statistics.stdev(percolation_thresholds)

    return mean_threshold, std_deviation,percolation_thresholds

N = 10  # Size of the grid
number_trials = 1000  # Number of Monte Carlo trials
mean_result, std_dev_result, percolation_thresholds = Percolation(N, number_trials)
print("Mean Percolation Threshold:", mean_result)
print("Standard Deviation:", std_dev_result)
