import tkinter as tk
import sys
import json


def load_lyrics(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class App:
    def __init__(self, root, lines, template):
        self.root = root
        self.lines = lines
        self.template = template
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
        print(
            "usage: python app.py lyrics.txt template.json"
        )
        sys.exit()


    lyrics = load_lyrics(sys.argv[1])
    template = load_template(sys.argv[2])


    root = tk.Tk()

    App(
        root,
        lyrics,
        template
    )

    root.mainloop()