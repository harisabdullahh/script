import tkinter as tk
import os

class MusicPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Control")
        self.create_widgets()

    def create_widgets(self):
        play_button = tk.Button(self.root, text="Play/Pause", command=self.play)
        play_button.pack(pady=10)
        next_button = tk.Button(self.root, text="Next", command=self.next)
        next_button.pack(pady=10)
        previous_button = tk.Button(self.root, text="Previous", command=self.prev)
        previous_button.pack(pady=10)

    def play(self):
        os.system("playerctl play-pause")
        
    def next(self):
        os.system("playerctl next")
        
    def prev(self):
        os.system("playerctl previous")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayerGUI(root)
    root.mainloop()

