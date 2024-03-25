#Haidar Al-Ali
#INFR 2820U

# importing all necessary modules

import tkinter as tk
import time
import numpy as np
import random
import matplotlib.colors as mcolors
import winsound


def create_chart(numbers):
     root = tk.Tk()
     canvas = tk.Canvas(root, width=800 , height=400)
     canvas.grid(row=0, column= 0 , columnspan= 2)
     return root,canvas

def draw_chart(numbers, canvas, colours):
    canvas.delete('all')
    max_val = max(numbers)
    bar_width = 800 // len(numbers)
    for i, number in enumerate(numbers):
          canvas.create_rectangle(i * bar_width, 400, (i + 1) * bar_width, 400 - number, fill=colours[i])
          canvas.create_text(i * bar_width + bar_width / 2, 400 - number - 10, text=str(number), fill="black")
          canvas.update()

def shuffle(numbers, canvas, colours):
     np.random.shuffle(numbers)
     draw_chart(numbers,canvas,colours )
     

def array_add_from_user():
    try:
        number_of_elements = int(input("Please enter the number of elements that you want to be in this array: "))
        numbers = []
        for i in range (number_of_elements):
            values = int(input(f"enter number {i + 1}: "))
            numbers.append(values)
        return numbers
    except: 
        print ("invalid input. please enter a valid number")
        return[]

def merge_sort(numbers, canvas, colours):
    if len(numbers) <= 1:
        return numbers
    
    
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid], canvas,colours)
    right_half = merge_sort(numbers[mid:], canvas,colours)

    return merge(left_half, right_half, canvas,colours)

def merge(left, right, canvas, colours):
    merge_list = []
    i = 0
    j = 0

    # End when you reach the end of the list
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
        draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
        time.sleep(0.7)
        winsound.Beep(1000,500)
        print("Merge step: ", merge_list + left[i:] + right[j:])

    while i < len(left):
            merge_list.append(left[i])
            i += 1
            draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
            time.sleep(0.7)
            print("Merge step: ", merge_list + left[i:] + right[j:])

    while j < len(right):
            merge_list.append(right[j])
            j += 1 
            draw_chart(merge_list + left[i:] + right[j:], canvas, colours)
            time.sleep(0.7)
            print("Merge step: ", merge_list + left[i:] + right[j:])
    return merge_list

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
