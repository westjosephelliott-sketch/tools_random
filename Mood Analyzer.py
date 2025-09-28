import cv2
import numpy as np
from deepface import DeepFace
import pygame
import threading

class Mood_Analyzer:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        pygame.mixer.init()
        self.moods = {
            "happy": "sounds/happy.wav",
            "sad": "sounds/sad.wav",
            "angry": "sounds/angry.wav",
            "surprise": "sounds/surprise.wav",
            "neutral": "sounds/neutral.wav"
        }

    def play_mood(self, mood):
        sound = self.moods.get(mood)
        if sound:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

    def analyze(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            mood = result[0]['dominant_emotion']
            threading.Thread(target=self.play_mood, args=(mood,), daemon=True).start()
            return mood
        except:
            return "unknown"

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            mood = self.analyze(frame)
            cv2.putText(frame, f"Mood: {mood}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow("Mood Mirror", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.capture.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    mirror = Mood_Analyzer()
    print("Starting...")
    mirror.run()
    print("Session ended!")
