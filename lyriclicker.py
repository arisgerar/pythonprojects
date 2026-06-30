import tkinter as tk
import sys


def load_lyrics(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


class App:
    def __init__(self, root, lines):
        self.root = root
        self.lines = lines
        self.i = 0

        root.geometry("600x200")
        root.attributes("-topmost", True)

        self.label = tk.Label(root, font=("Arial", 20), wraplength=580)
        self.label.pack(expand=True)

        root.bind("<Button-1>", self.next)
        root.bind("<space>", self.next)

        self.show()

    def show(self):
        if self.i < len(self.lines):
            self.label.config(text=self.lines[self.i])
        else:
            self.root.destroy()

    def next(self, event=None):
        self.i += 1
        self.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python app.py lyrics.txt")
        sys.exit()

    lines = load_lyrics(sys.argv[1])

    root = tk.Tk()
    App(root, lines)
    root.mainloop()