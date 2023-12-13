# Created by Venujan Malaiyandi
# For Task 2.1P

# Function to return a sequence of Fibonacci numbers
def fibonacci(number_of_steps):
    seq = []
    i, j = 0, 1
    for _ in range(number_of_steps):
        seq.append(i)
        i, j = j, i + j
    return seq

# Function using a while loop to repeatedly request for valid input
def getInput():

    global input_bool

    while input_bool == True:
        try:
            usr_input = int(input("Please input the number of steps: "))
            if usr_input > 0:  # Check if the input is greater than 0
                input_bool = False
            else:
                print("Input must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    return usr_input


# Main logic of the program

input_bool : bool = True

user_input = getInput()

fib_seq = fibonacci(user_input)

print("Fibonacci sequence:", fib_seq)

# Access the most recent element of the collection using indexing
output = fib_seq[-1]
print("Last element in the sequence:", output)
