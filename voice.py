import speech_recognition as sr

POSITION_MAP = {
    "top left": (0, 0),
    "top center": (0, 1),
    "top right": (0, 2),
    "middle left": (1, 0),
    "middle center": (1, 1),
    "middle right": (1, 2),
    "bottom left": (2, 0),
    "bottom center": (2, 1),
    "bottom right": (2, 2)
}

def get_move_from_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak your move (e.g. 'top left'):")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)

        for phrase in POSITION_MAP:
            if phrase in text:
                return POSITION_MAP[phrase]

        print("❌ Move not recognized.")
        return None

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return None
    except sr.RequestError:
        print("❌ Could not connect to Google Speech API.")
        return None
