#TACE Final culminating
#This game is liverpool jeopardy

class board:
    def __init__(self):
        self.image = pygame.image.load("Liverpool Jeopardy.jpg")
        self.image = pygame.transform.scale(self.image, self.size)


import tkinter as tk

def create_grid(event=None):
    print("Ethan")
    for i in range(5):
        for j in range(4):
            cell = tk.Label(root, text=f'({i},{j})', borderwidth=1, relief="solid", width=10, height=3)
            cell.grid(row=i, column=j)

# Create the main window
root = tk.Tk()
root.title("5x4 Grid")

# Bind the window resizing event to recreate the grid
root.bind("<Configure>", create_grid)
    win.blit("Liverpooldy.jpg")
# Initial creation of the grid
create_grid()

# Run the Tkinter event loop
root.mainloop()