import numpy as np
from numpy.random import Generator, MT19937, PCG64
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import time


class GameOfLife:
    """
    A Python implementation of Conway's Game of Life with optional animation,
    random initialization, and automatic termination when a repeating pattern occurs.
    """

    def __init__(
        self,
        m: int = 10,
        n: int = 10,
        show_plot: bool = False,
        rng: Generator = Generator(MT19937())
    ):
        self.m = m
        self.n = n
        self.rng = rng
        self.show_plot = show_plot

        self.population = np.zeros((m, n), dtype=int)
        self.last_population = np.zeros((m, n), dtype=int)
        self.second_last_population = np.zeros((m, n), dtype=int)

        self.iterations = 0
        self.fig = Figure()

    def initialize_board(self) -> None:
        """randomly initialize the board with alive cells."""
        num_alive = int(self.rng.random() * self.m * self.n)

        rows = self.rng.integers(0, self.m, size=num_alive)
        cols = self.rng.integers(0, self.n, size=num_alive)

        self.population[rows, cols] = 1

    def count_neighbors(self, grid: np.ndarray, row: int, col: int) -> int:
        """return the number of alive neighbors around (row, col)."""
        r0, r1 = max(0, row - 1), min(self.m - 1, row + 1)
        c0, c1 = max(0, col - 1), min(self.n - 1, col + 1)
        return np.sum(grid[r0:r1 + 1, c0:c1 + 1]) - grid[row, col]

    def update_generation(self) -> None:
        """apply one iteration of Conway's Game of Life rules."""
        new_population = self.population.copy()

        for row in range(self.m):
            for col in range(self.n):
                neighbors = self.count_neighbors(self.population, row, col)

                if self.population[row, col] == 1:
                    # alive cell rules
                    if neighbors < 2 or neighbors > 3:
                        new_population[row, col] = 0
                else:
                    # dead cell rules
                    if neighbors == 3:
                        new_population[row, col] = 1

        self.population = new_population

        if self.show_plot:
            plt.imshow(self.population, interpolation="nearest")
            plt.pause(0.2)
            time.sleep(0.2)

    def run(self) -> None:
        """run the simulation until extinction or a repeating pattern occurs."""
        while True:
            self.iterations += 1

            # Track last two states to detect loops
            self.second_last_population = self.last_population.copy()
            self.last_population = self.population.copy()

            self.update_generation()

            # Termination conditions
            if np.sum(self.population) == 0:
                plt.close()
                break

            if (
                self.iterations > 3
                and np.array_equal(self.population, self.second_last_population)
            ):
                plt.close()
                break
