#!/usr/bin/env python

import Tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.gif")

w1 = tk.Label(root, image=logo).pack(side="right")

# Text appears exactly, including new lines
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(root,
        justify=tk.LEFT, # default is center
        padx = 10, # default is 1
        text=explanation).pack(side="left")

# using this line instead will place the text over the image
#w = tk.Label(root,
#        compound = tk.CENTER,
#        text=explanation,
#        image=logo).pack(side="right")

root.mainloop()
