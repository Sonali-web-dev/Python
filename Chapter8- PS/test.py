import tkinter as tk

# Create the main window.
root = tk.Tk()
root.title("My First Tkinter App")

# Add a label widget.
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Add a button widget.
def on_button_click():
    label.config(text="Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop.
root.mainloop()
