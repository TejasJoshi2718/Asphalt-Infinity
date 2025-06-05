# Asphalt-Infinity

# 🚗 Three lanes. Infinite chaos. (Pygame)

A minimalist infinite runner game where you dodge traffic across 3 fixed lanes. Built using Python and Pygame, this project focuses on game state architecture, dynamic difficulty systems, and real-time input management.

## 🎮 Gameplay Features

- Three selectable difficulty modes with real-time speed ramping:
  - **Easy**: Square-root based progression
  - **Medium**: Linear ramp-up
  - **Hard**: Quadratic increase
- Real-time input handling (non-blocking)
- Smooth background scrolling to simulate forward motion
- Accurate lane-based collision detection
- Time-based scoring with graceful game termination

## 📈 Recent Enhancements

- 🔊 Added support for looping background music via Pygame mixer
- 🧠 Implemented difficulty selection with mathematical ramp functions:
  - `√t`, `t`, and `t²`-based ramp speeds
- 🧠 Speed calculation refactored for cleaner integration into scroll + obstacle motion
- 🎛️ Interactive difficulty selection menu with keyboard input
- 🧹 Ghosting and sizing bugs fixed for clean car lane alignment

## 🗂️ Folder Structure
```bash
project/
├── main.py
└── assets/
├── 3lane.png # Road background
├── porsche.png # Car sprite
└── background_music.mp3 # Optional background music


## ▶️ Running the Game

1. Install Python 3.7+
2. Install dependencies:
   ```bash
   pip install pygame
   python main.py


