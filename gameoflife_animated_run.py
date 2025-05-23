import gameoflife_animated as gol
gl = gol.GameOfLife(m=50,n=50,show_plot=True)
gl.initialize_board()
gl.decide_update()