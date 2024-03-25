#Haidar Al-Ali
#INFR 2820U

# importing all necessary modules
import tkinter as tk
import time
import numpy as np
import random
import matplotlib.colors as mcolors
import winsound


#this command created a chart with tkinter
def create_chart(numbers):
    #creating a tkinter window
     root = tk.Tk()
     # creating a canvas for drawing
     canvas = tk.Canvas(root, width=800 , height=400)
     #placing the canvas on the window on the grid spicified
     canvas.grid(row=0, column= 0 , columnspan= 2)
     # returing the window and canvas
     return root,canvas

# this command makes a function to draw the char on the canvas
def draw_chart(numbers, canvas, colours):
    # clearing the canvas
    canvas.delete('all')
    # getting the maximum value from the numbers
    max_val = max(numbers)
    # ca,culating the width of each bar
    bar_width = 800 // len(numbers)
    #drawing each bar on the canvas
    for i, number in enumerate(numbers):
          #creating  a rectangle bar for each number
          canvas.create_rectangle(i * bar_width, 400, (i + 1) * bar_width, 400 - number, fill=colours[i])
          # this command will add the number text above each bar
          canvas.create_text(i * bar_width + bar_width / 2, 400 - number - 10, text=str(number), fill="black")
          # this command updates the canvas
          canvas.update()

# this command is used to shuffle the numbers and re-draw the chart
def shuffle(numbers, canvas, colours):
     # shuffling the numbers
     np.random.shuffle(numbers)
     # this command will redraw the chart
     draw_chart(numbers,canvas,colours )
     
# this command will add numbers to the array from the user input
def array_add_from_user():
    try:
        # this command is asking the user to input the numer of elements
        number_of_elements = int(input("Please enter the number of elements that you want to be in this array: "))
        numbers = []
        # depinding of the number chosen this will ask the user # number of times 
        for i in range (number_of_elements):
            values = int(input(f"enter number {i + 1}: "))
            numbers.append(values)
        return numbers
    # if the user input any value other than numeric
    except: 
        print ("invalid input. please enter a valid number")
        return[]

# this command functions tp preform merge sort on the numbers
def merge_sort(numbers, canvas, colours):
    # this command acheck if the list is one or zeore then it is allready sorted
    if len(numbers) <= 1:
        return numbers
    
    # this command splits the list in half
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid], canvas,colours)
    right_half = merge_sort(numbers[mid:], canvas,colours)
    # this command mergin the two haves
    return merge(left_half, right_half, canvas,colours)

# function to merge two lists
def merge(left, right, canvas, colours):
    merge_list = []
    i = 0
    j = 0

    # this command will merge the lists until one is empty
    while i < len(left) and j < len(right):
        # this command will check if the current element of the peft list is smaller , add it to the merge list
        if left[i] <= right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            # otherwise add the current element of right list
            merge_list.append(right[j])
            j += 1
            #this command will redraw the chart with the current state of the merge
        draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
        # adding a dely for visulization
        time.sleep(0.7)
        # makes a beep sound every swap that happens
        winsound.Beep(1000,500)
        # this command will prin the current state of the merge
        print("Merge step: ", merge_list + left[i:] + right[j:])

    # adding the remaining elements of the left list, if any
    while i < len(left):
            merge_list.append(left[i])
            i += 1
            draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
            time.sleep(0.7)
            print("Merge step: ", merge_list + left[i:] + right[j:])
    # adding the remaining elements of the right list, if any
    while j < len(right):
            merge_list.append(right[j])
            j += 1 
            draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
            time.sleep(0.7)
            print("Merge step: ", merge_list + left[i:] + right[j:])
    # this command will return the merged list            
    return merge_list

# the main functions
if __name__ == "__main__":
    user_numbers = array_add_from_user()
    if user_numbers:
        colours = [random.choice(list(mcolors.CSS4_COLORS.keys())) for lable in range(len(user_numbers))]
        print(f"Numbers entered: {user_numbers}")
        root, canvas = create_chart(user_numbers)
        shuffle_button = tk.Button(root, text= "Shuffle", command=lambda: shuffle(user_numbers , canvas, colours))
        sort_button = tk.Button(root, text="Sort", command=lambda: merge_sort(user_numbers, canvas,colours))
        sorted_numbers = merge_sort(user_numbers,canvas, colours)
        print(f"sorted numbers:{ sorted_numbers}")
        shuffle_button.grid(row=1,column=0)
        sort_button.grid(row=1,column=1)
        root.mainloop()
