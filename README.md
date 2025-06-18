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
- 📱 Plans to extend this project into an iOS app with multiple voice operated minigames

---

## 🧠 Technologies Used

- Python 3.12
- Pygame
- SpeechRecognition
- PyAudio
- Figma (for UI/UX)
- ChatGPT & Cursor AI (prompt engineering)

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/PranavC287/Voice_Tic-Tac-Toe.git
cd Voice_Tic-Tac-Toe
```

### 2. Install dependencies

> Note: Installing `pyaudio` on Windows may require a precompiled wheel. You can download it from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) if needed.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install pygame SpeechRecognition pyaudio
```

### 3. Run the game

```bash
python main.py
```

---

## 🗂️ Project Structure

```
voice_tictactoe/
│
├── assets/                         # Fonts, background images, screenshots
│   ├── Orbitron-VariableFont.ttf
│   ├── background_grid.png
│   └── demo.png
│
├── board.py                        # Game logic: board creation, win checks
├── ai.py                           # AI logic using Minimax
├── voice.py                        # Voice input parsing via speech recognition
├── main.py                         # Main game loop and UI
├── README.md
└── requirements.txt
```

---

## 📱 Future Plans

- Porting this game into a **Swift-based iOS app**
- Adding a hub of **voice operated mini games**
- Enhance speech handling with more natural language understanding

---

## 📸 Demo

[demo](assets/demo.png)

---

## 📩 Contact
 
**Pranav C** • [GitHub](https://github.com/PranavC287)

---
