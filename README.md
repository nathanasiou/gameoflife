# Conway's Game of Life — Python Implementation

A clean, object‑oriented Python implementation of **John Conway’s Game of Life**, featuring:

- User‑defined grid size  
- Choice of pseudo‑random number generators (MT19937 or PCG64)  
- Randomized initial states  
- Automatic termination when a repeating pattern is detected  
- Optional animated visualization using Matplotlib  

This project is designed to be simple, readable, and faithful to the original rules of the Game of Life.

---

## Project Structure

### `gameoflife_animated.py`
Contains the `GameOfLife` class, which implements:
- Board initialization  
- Neighbor counting  
- Generation updates  
- Loop detection  
- Optional animation  

### `gameoflife_animated_run.py`
Entry point for running the simulation.  
You may edit the default parameters (grid size, RNG, animation toggle).

Run with:

```bash
python gameoflife_animated_run.py run
```

## Future Improvements

Planned enhancements include:

- **Switch to a non‑blocking animation backend**  
  (e.g., `FuncAnimation`, `blit=True`, or a GUI toolkit like PyQt/Pygame)

- **Asynchronous rendering**  
  Use a separate thread or event loop to prevent UI freezing.

- **Custom initial patterns**  
  Load gliders, oscillators, spaceships, etc.

- **Command‑line arguments**  
  Let users specify grid size, RNG, speed, and seed from the terminal.

- **GIF or MP4 export**  
  Save animations of the simulation.