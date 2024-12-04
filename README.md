## PSEUDO-RANDOM NUMBER GENERATORS IN THE GAME OF LIFE 

A novel Python implementation of John Conway’s Game of Life and evaluation of the performance of the Mersenne Twister and Permuted Congruential generators in the game. Game of Life takes place on a 2D matrix with cells that evolve based on their neighbors’ states. Other Python implementations do not include randomized grid dimensions, randomized cell states, the ability to set specific pseudo random number (PRN) generators, and automatic program termination when a pattern starts repeating. Including these features allows users to tailor the simulation to their interests and needs. Additionally, the program can be used to test the difference in means between two PRN generators’ simulation output. Specifically, testing the difference in the mean number of generations produced from the Mersenne Twister and PCG-64 shows there is no significant difference. Users of the program can experiment with other PRN generators to see which yields longer runs in Game of Life.

## Code Description
Python code to simulate The Game of Life, compute summary statistics from 10,000 runs, and run a t-test for whether the means of two generators' number of generations are equal. 

## Installation
Install dependencies:
'''
pip install numpy matplotlib scipy collections numpy random statistics
'''
