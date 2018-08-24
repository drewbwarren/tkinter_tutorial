#!/usr/bin/env python
import Tkinter as tk

# initialize tkinter by creating a root widget (a window with a title bar and stuff), there can only be one
root = tk.Tk()

# label widget, first param is the parent window
w = tk.Label(root, text="hello world!")

# tells tk to fit the size of the window to the given text
w.pack()

# the window doesn't appear until the event loop starts
root.mainloop()
