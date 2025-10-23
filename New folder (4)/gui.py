import tkinter as tk
import random

root = tk.Tk()
root.title("rock paper scissors") 
root.geometry("1000x1000")    



def but():
    enemy_list = ["scissors", "paper", "rock"]
    enemy_list_random = random.choice(enemy_list)
    
    if enemy_list_random == enemy_list[0]:
        label = tk.Label(root, text="draw")
        label.pack()
    elif enemy_list_random == enemy_list[1]:
        label1 = tk.Label(root, text="you won")
        label1.pack()
    elif enemy_list_random == enemy_list[2]:
        label2 = tk.Label(root, text="you won")
        label2.pack()
        
        
    

def but2():
    enemy_list = ["scissors", "paper", "rock"]
    enemy_list_random = random.choice(enemy_list)
    
    if enemy_list_random == enemy_list[0]:
        label = tk.Label(root, text="you won")
        label.pack()
    elif enemy_list_random == enemy_list[1]:
        label1 = tk.Label(root, text="you lose")
        label1.pack()
    elif enemy_list_random == enemy_list[2]:
        label2 = tk.Label(root, text="draw")
        label2.pack()
    
 

def but3():
    enemy_list = ["scissors", "paper", "rock"]
    enemy_list_random = random.choice(enemy_list)
    
    if enemy_list_random == enemy_list[0]:
        label = tk.Label(root, text="you lost")
        label.pack()
    elif enemy_list_random == enemy_list[1]:
        label1 = tk.Label(root, text="draw")
        label1.pack()
    elif enemy_list_random == enemy_list[2]:
        label2 = tk.Label(root, text="you won:")
        label2.pack()
    
 



button = tk.Button(root, text="scissors",command=but)
button.pack(side=tk.RIGHT, anchor="center")
button1 = tk.Button(root, text="rock", command=but2)
button1.pack(side=tk.BOTTOM, anchor="center")
button2 = tk.Button(root, text="paper", command=but3)
button2.pack(side=tk.LEFT, anchor="center")


                   
root.mainloop()

    
    

    
    
    
    