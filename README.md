# 🎮 Voice-Controlled Tic-Tac-Toe (AI Edition)

An AI-powered, voice-activated Tic-Tac-Toe game built using Python, Pygame, and speech recognition. Designed with a futuristic dark-mode UI inspired by holographic themes.

![screenshot](assets/demo.png)

---

## 🔥 Features

- 🎤 Voice-controlled player moves (e.g. "top left", "center")
- 🤖 Unbeatable AI opponent using minimax algorithm
- ✨ Neon-glow themed UI inspired by futuristic holograms
- 🖥️ Built with Pygame + custom-designed Figma visuals
- 🧠 Developed partially with help from ChatGPT, Cursor AI, and prompt engineering techniques
- 📱 Plans to extend this project into a Swift-based iOS app with multiple voice operated minigames

---

## 🧠 Technologies Used

- Python 3.12  
- Pygame  
- SpeechRecognition  
- PyAudio  
- Figma (for UI/UX)  
- ChatGPT & Cursor AI (prompt engineering)  

---

## 🗣️ How to Speak Commands

Use simple 2-word phrases to place your move. Valid commands include:

```
top left        top center       top right
middle left     center           middle right
bottom left     bottom center    bottom right
```

- You can say `"center"` or `"middle center"` for the center tile.
- `"middle"` and `"center"` are interchangeable for the second row or column.

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/PranavC287/Voice_Tic-Tac-Toe.git
cd Voice_Tic-Tac-Toe

# 2. Install dependencies
# Note: Installing PyAudio on Windows may require a precompiled wheel from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

pip install -r requirements.txt

# If requirements.txt is missing, install manually:
pip install pygame SpeechRecognition pyaudio

# 3. Run the game
python main.py
```

---

## 🗂️ Project Structure

```
voice_tictactoe/
├── assets/                         # Fonts, background images, screenshots
│   ├── Orbitron-VariableFont.ttf
│   ├── background_grid.png
│   └── demo.png
├── board.py                        # Game logic: board creation, win checks
├── ai.py                           # AI logic using Minimax
├── voice.py                        # Voice input parsing via speech recognition
├── main.py                         # Main game loop and UI
├── README.md
└── requirements.txt
```

---

## 📱 Future Plans

- Porting this game into a Swift-based iOS app  
- Adding a hub of voice operated mini games  
- Enhancing speech input with natural language understanding  

---

## 📸 Demo

![demo](assets/demo.png)

---

## 📩 Contact

**Pranav C**  
GitHub: [https://github.com/PranavC287/Voice_Tic-Tac-Toe](https://github.com/PranavC287/Voice_Tic-Tac-Toe)
