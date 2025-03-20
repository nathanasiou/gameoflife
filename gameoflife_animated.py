from numpy.random import Generator, MT19937, PCG64
from matplotlib import pyplot as plt
from scipy.stats import ttest_ind
from collections import Counter
import numpy as np
import matplotlib.animation as animation
import statistics

MT = Generator(MT19937()) # Mersenne Twister generator
PCG = Generator(PCG64()) # O’Neill’s permutation congruential generator

class GameOfLife():

    def __init__(self, m = 10, n = 10, show_plot = False, rng = MT):
        self.base_population = np.zeros((m,n), dtype = int) # initialize blank board
        self.alive = {}
        self.population = self.base_population
        self.rng = rng
        self.m = m
        self.n = n
        self.show_plot = show_plot

    def initialize_board(self):
        # randomly select number of cells to be initialized with starting state alive or value of 1
        rand_num_ones = int(self.rng.random() * self.m * self.n)
        
        # generate random numbers for row and column indices
        rand_ms = self.rng.integers(low = 0, high = self.m, size = rand_num_ones)
        rand_ns = self.rng.integers(low = 0, high = self.n, size = rand_num_ones)
        
        # set random coordinates above equal to one in the base array of zeros
        for i in range(rand_num_ones):
            self.base_population[rand_ms[i], rand_ns[i]] = 1  

    def update_generations(self):
        current_population = self.population.copy()

        alive = np.where(current_population == 1)
        alive = zip(alive[0], alive[1])

        for coordinate in alive:
            row = coordinate[0]
            col = coordinate[1]
            # set min and max row based on coordinates of cell and bounds of grid
            min_row = row - 1 if row - 1 >= 0 else row
            max_row = row + 1 if row + 1 < self.m else row
            min_col = col - 1 if col - 1 >= 0 else col
            max_col = col + 1 if col + 1 < self.n else col
            neighbor_count = sum([(current_population[min_row][col] == 1), (current_population[row][min_col] == 1), (current_population[min_row][min_col] == 1), \
                                    (current_population[max_row][min_col] == 1), (current_population[min_row][max_col] == 1), (current_population[max_row][max_col] == 1), \
                                    (current_population[max_row][col] == 1), (current_population[row][max_col] == 1)])
            
            # each cell with zero, one, or at least 4 neighbors dies
            if neighbor_count == 1 or neighbor_count == 0 or neighbor_count >= 4:
                self.population[coordinate] = 0
        
        dead = np.where(current_population == 0)
        dead = zip(dead[0], dead[1])
        
        for coordinate in dead:
            dead_row = coordinate[0]
            dead_col = coordinate[1]
            # set min and max row based on coordinates of cell and bounds of grid
            min_row = dead_row - 1 if dead_row - 1 >= 0 else dead_row
            max_row = dead_row + 1 if dead_row + 1 < self.m else dead_row
            min_col = dead_col - 1 if dead_col - 1 >= 0 else dead_col
            max_col = dead_col + 1 if dead_col + 1 < self.n else dead_col
            neighbor_count = sum([(current_population[min_row][dead_col] == 1), (current_population[dead_row][min_col] == 1), (current_population[min_row][min_col] == 1), \
                                    (current_population[max_row][min_col] == 1), (current_population[min_row][max_col] == 1), (current_population[max_row][max_col] == 1), \
                                    (current_population[max_row][dead_col] == 1), (current_population[dead_row][max_col] == 1)])
            # each empty space with three neighbors becomes populated:
            if neighbor_count == 3:
                self.population[coordinate] = 1

        if self.show_plot == True: # display plot of current population (not an animation)
                    plt.imshow(self.population, interpolation='nearest')
                    # plt.show()   
                    # Display the plot for 1 second
                    plt.pause(.2)


        return self.population
            
            
    def decide_update(self):
        # # check conditions for simulation to end
        # # all dead cells
        SimulationComplete = False
        iterations = 0
        while True:
            old_population = self.population.copy()
            iterations += 1
            if iterations == 1:
                second_last_population = np.zeros((self.base_population.shape[0], self.base_population.shape[1]))
                last_population = self.base_population.copy() # making copy to check if 2 states ago equals current state -- then in a repeating sequence
            elif iterations >= 2:
                second_last_population = last_population.copy()
                last_population = old_population
                self.update_generations()
        
            #### call function
            if (np.sum(self.population)) == 0: 
                SimulationComplete = True
            # the state from two iterations ago equals the current state
            elif iterations > 3 and (self.population == second_last_population).all() == True:
                SimulationComplete = True
            # if simulation complete, return iterations and break loop
            if SimulationComplete == True:
                plt.close()
                break
        
        return "Simulation Ended",  iterations, self.base_population