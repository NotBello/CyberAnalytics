# Created by Venujan Malaiyandi
# For Task 1.2P

# Function to take width
def inputWidth():
    global input_width_bool

    while input_width_bool == True:
        try:
            width_of_rec = int(input("Please input rect width: "))
            if width_of_rec > 0:  # Check if width is greater than 0
                input_width_bool = False
            else:
                print("Width must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    return width_of_rec

# Function to take height
def inputHeight():
    global input_height_bool

    while input_height_bool == True:
        try:
            height_of_rect = int(input("Please input rect height: "))
            if height_of_rect > 0:  # Check if height is greater than 0
                input_height_bool = False
            else:
                print("Height must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    return height_of_rect

def makeRectangle(h, w):
    for _ in range(w):
        print(h * "*")

# Initializing variables with types for secure coding
width: int
height: int

input_width_bool: bool = True
input_height_bool: bool = True

# Take width and height as input from the user and store them in the variable
while True:
    width = inputWidth()
    height = inputHeight()

    if width > 0 and height > 0:
        break

print("You are here --") # Used for debugging

print("The width is ", width , "\nThe height is ", height)

makeRectangle(height, width)
