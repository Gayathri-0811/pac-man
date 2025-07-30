# 🟡 Pac-Man: Classic Arcade Game (Python + Pygame)

A fun, lightweight recreation of the **Pac-Man** arcade game using Python and the **Pygame** library. Eat fruits 🥝, avoid ghosts 👻, and try to get the highest score!

---
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/e65f07d3-b786-496a-bc84-a2c882d96b05" />
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/75fac826-8c77-4b9c-8d1f-884e0ebd66bd" />
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/076dd9db-bd7a-421b-86a6-5e5b975a5379" />



## 🧠 Features

- 🔼🔽◀️▶️ Smooth grid-based movement using arrow keys
- 🍓 Randomly spawning fruit
- 👻 Basic ghost AI that follows Pac-Man
- 💯 Score counter and Game Over screen
- 🔁 Restart game without restarting the script

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pacman-game.git
cd pacman-game
```
### 2. Install dependencies
pip install pygame


## 🕹️ Controls

| Key       | Action         |
|-----------|----------------|
| ⬆️ Up     | Move Up        |
| ⬇️ Down   | Move Down      |
| ⬅️ Left   | Move Left      |
| ➡️ Right  | Move Right     |
| R         | Restart Game   |
| Q         | Quit Game      |


## 🚀 How the Game Works

- `Pacman` moves in a grid and checks for collisions with fruit.
- `Ghosts` track Pacman's position using basic directional movement.
- Eating fruit gives +10 points and respawns the fruit randomly.
- Collision with ghost ends the game and displays the final score.
- Press `R` to restart or `Q` to quit.
