import gameoflife_animated as gol
gl = gol.GameOfLife(m=10,n=10,show_plot=True)
gl.initialize_board()
gl.decide_update()