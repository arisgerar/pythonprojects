import tkinter as tk
import sys
import json


def load_lyrics(path):
    lyrics = []
    metadata = {
        "album": "Single"
    }

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("[album:"):
                metadata["album"] = line[7:-1].strip()
                continue

            if line.startswith("["):
                continue

            if line:
                lyrics.append(line)

    return lyrics, metadata


def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class App:
    def __init__(self, root, lines, template, metadata):
        self.root = root
        self.lines = lines
        self.template = template
        self.metadata = metadata
        self.i = 0

        # Window settings
        width = template.get("window_width", 600)
        height = template.get("window_height", 200)

        root.geometry(f"{width}x{height}")
        root.attributes("-topmost", True)

        # Font style
        font_style = []

        if template.get("bold", False):
            font_style.append("bold")

        if template.get("italic", False):
            font_style.append("italic")

        if not font_style:
            font_style = ["normal"]

        self.label = tk.Label(
            root,
            font=(
                template.get("font", "Arial"),
                template.get("size", 20),
                *font_style
            ),
            fg=template.get("color", "white"),
            bg=template.get("background", "black"),
            wraplength=width - 20
        )

        self.label.pack(expand=True, fill="both")

        # Song information window
        self.info = tk.Toplevel(root)
        self.info.title("Song Information")
        self.info.geometry("250x100")

        self.album_label = tk.Label(
            self.info,
            text=f"Album: {self.metadata['album']}",
            font=("Arial", 12)
        )

        self.album_label.pack(padx=10, pady=10)

        root.configure(
            bg=template.get("background", "black")
        )

        root.bind("<Button-1>", self.next)
        root.bind("<space>", self.next)

        self.show()


    def show(self):
        if self.i < len(self.lines):
            self.label.config(
                text=self.lines[self.i]
            )
        else:
            self.root.destroy()


    def next(self, event=None):
        self.i += 1
        self.show()


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("usage: python lyriclicker.py lyrics.txt template.json")
        sys.exit()

    lyrics, metadata = load_lyrics(sys.argv[1])
    template = load_template(sys.argv[2])

    root = tk.Tk()

    App(
        root,
        lyrics,
        template,
        metadata
    )

    root.mainloop()