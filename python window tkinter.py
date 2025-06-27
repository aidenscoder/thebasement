import tkinter as tk

def update_counter():
    """Update the click counter and display it."""
    global click_counter
    click_counter += 1
    my_button.config(text=f"Clicked {click_counter} times")

def from_rgb(r,g,b):
    """Convert RGB values to hexadecimal color."""
    return f'#{r:02x}{g:02x}{b:02x}'

click_counter = 0
screen = tk.Tk()
screen.configure(bg=from_rgb(255, 255, 255))  # Set background color to blue
screen.title("Click Counter")
screen.geometry("800x600")


my_button = tk.Button(
    screen, 
    text="Click Me!",
    background=from_rgb(0, 255, 0), 
    foreground=from_rgb(255, 0, 0), 
    font=("Arial", 24), 
    command=update_counter
)

my_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

screen.mainloop()