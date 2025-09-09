# 🐍 Snake Game

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
  ![Pygame](https://img.shields.io/badge/Pygame-2.5.0+-green.svg)
  ![Status](https://img.shields.io/badge/Status-Complete-success.svg)

  **A classic Snake game built with Python and Pygame**
  
  *Relive the nostalgia of the iconic Snake game with smooth gameplay and modern touches*

</div>

---

## 🎮 Game Preview

```
┌─────────────────────────────────────┐
│  Score: 150                         │
│                                     │
│    ██                               │
│    ██ ██ ██ ██                      │
│                                     │
│              ▓▓                     │
│                                     │
│                                     │
│                                     │
└─────────────────────────────────────┘
```

## ✨ Features

- 🎯 **Classic Gameplay** - Navigate the snake to eat food and grow longer
- 📊 **Score Tracking** - Keep track of your high scores
- ⏸️ **Pause Function** - Take a break anytime with the pause feature
- 🔄 **Quick Restart** - Instantly restart after game over
- 🎨 **Clean Graphics** - Simple, colorful block-based design
- ⚡ **Smooth Controls** - Responsive arrow key movement
- 🏆 **Game Over Screen** - Clean game over interface with restart option

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SharmaVrishab/snake-game.git
   cd snake-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the game**
   ```bash
   python main.py
   ```

## 🎮 How to Play

### Controls
| Key | Action |
|-----|--------|
| ↑ ↓ ← → | Move snake |
| `P` | Pause/Resume game |
| `Space` | Restart after game over |
| `ESC` | Quit game |

### Game Rules
1. 🐍 Control the snake using arrow keys
2. 🍎 Eat red food blocks to grow and increase score
3. 🚫 Avoid hitting walls or your own tail
4. 📈 Try to achieve the highest score possible!

## 🏗️ Project Structure

```
snake_game/
├── 📄 main.py              # Entry point
├── 📄 requirements.txt     # Dependencies
├── 📂 src/
│   ├── 🔧 __init__.py     # Package initializer
│   ├── 🎮 game.py         # Main game logic & loop
│   ├── 🐍 snake.py        # Snake class (movement, collision)
│   ├── 🍎 food.py         # Food spawning & positioning
│   ├── ⚙️ settings.py     # Game constants & configuration
│   └── 🖼️ ui.py           # UI elements & screens
└── 📂 assets/
    └── 📂 sounds/          # Sound effects (optional)
```

## 🛠️ Technical Details

### Built With
- **Python 3.7+** - Core programming language
- **Pygame 2.5.0+** - Game development library

### Key Components
- **Modular Design** - Clean separation of concerns
- **Object-Oriented** - Well-structured classes for game entities
- **Event-Driven** - Responsive to user input
- **Collision Detection** - Accurate boundary and self-collision detection

## 🎨 Customization

Want to modify the game? Here are some easy customizations:

### Change Colors
Edit `src/settings.py`:
```python
# Snake colors
GREEN = (0, 255, 0)        # Snake body
DARK_GREEN = (0, 200, 0)   # Snake head
RED = (255, 0, 0)          # Food
```

### Adjust Game Speed
```python
SNAKE_SPEED = 10  # Increase for faster gameplay
```

### Modify Grid Size
```python
GRID_SIZE = 20    # Change block size
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the project
2. 🌟 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

### Ideas for Contributions
- 🔊 Add sound effects
- 🏆 Implement high score saving
- 🎨 Add different themes/skins
- 📱 Add mobile controls
- 🏅 Create difficulty levels
- 💫 Add power-ups

## 🙏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with the amazing Pygame community resources
- Thanks to all contributors and players!

## 📞 Contact

**Vrishab Sharma** - [@SharmaVrishab](https://github.com/SharmaVrishab)

Project Link: [https://github.com/SharmaVrishab/snake-game](https://github.com/SharmaVrishab/snake-game)

---

<div align="center">
  
  **⭐ Star this repo if you enjoyed playing! ⭐**
  
  *Made with ❤️ and Python*

</div>
