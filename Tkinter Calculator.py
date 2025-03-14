# CALCULATOR APP

# Import Library
from tkinter import *

# Function that execute when the button is clicked
def on_button_clicked(value):
    # Code to handle button clicked and also update the entry field

    # Get the current state of the entry field (either empty or occupied)
    current = entry_var.get()

    if value == "C":
        entry_var.set("")
        
    elif value == "⌫":
        entry_var.set(current[:-1])

    elif value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
            
        except:
            entry_var.set("Syntax Error")
            
   
    else:
        # Update the state of the entry var with the value coming from the button argument 
        entry_var.set(current + str(value))

    

    
   

# Initialize the window
root = Tk()
root.title("Optimum Calculator")
root.geometry("450x500")
root.configure(bg="#873e23")
root.resizable(False, False)

font_properties = ("Arial", 14)
btn_bg = "#442510"
btn_fg = "#eab676"

entry_var = StringVar()

calc_entry = Entry(root, textvariable=entry_var, font=("Arial", 20), bg=btn_bg, fg=btn_fg, justify="right", bd=5, relief=FLAT)
calc_entry.grid(row=0, column=0, ipadx=8, pady=8, columnspan=7)

# ROW 1 (C - X - () )
clear_btn = Button(root, text="C", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("C"))
clear_btn.grid(row=1, column=0, padx=4, pady=4)

delete_btn = Button(root, text="⌫", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("⌫"))
delete_btn.grid(row=1, column=1, padx=4, pady=4)

opening_br_btn = Button(root, text="(", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("("))
opening_br_btn.grid(row=1, column=2, padx=4, pady=4)

closing_br_btn = Button(root, text=")", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked(")"))
closing_br_btn.grid(row=1, column=3, padx=4, pady=4)


# ROW 2 (7 - 8 - 9 - / )
btn_7 = Button(root, text="7", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("7"))
btn_7.grid(row=2, column=0, padx=4, pady=2)

btn_8 = Button(root, text="8", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("8"))
btn_8.grid(row=2, column=1, padx=4, pady=2)

btn_9 = Button(root, text="9", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("9"))
btn_9.grid(row=2, column=2, padx=4, pady=2)

btn_div = Button(root, text="/", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("/"))
btn_div.grid(row=2, column=3, padx=4, pady=2)


# ROW 3 (4 - 5 - 6 - + )
btn_4 = Button(root, text="4", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda: on_button_clicked("4"))
btn_4.grid(row=3, column=0, padx=4, pady=2)

btn_5 = Button(root, text="5", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda: on_button_clicked("5"))
btn_5.grid(row=3, column=1, padx=4, pady=2)

btn_6 = Button(root, text="6", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda: on_button_clicked("6"))
btn_6.grid(row=3, column=2, padx=4, pady=2)

btn_add = Button(root, text="+", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda: on_button_clicked("+"))
btn_add.grid(row=3, column=3, padx=4, pady=2)


# ROW 4 (1 - 2 - 3 - - )
btn_1 = Button(root, text="1", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("1"))
btn_1.grid(row=4, column=0, padx=4, pady=2)

btn_2 = Button(root, text="2", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("2"))
btn_2.grid(row=4, column=1, padx=4, pady=2)

btn_3 = Button(root, text="3", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("3"))
btn_3.grid(row=4, column=2, padx=4, pady=2)

btn_sub = Button(root, text="-", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("-"))
btn_sub.grid(row=4, column=3, padx=4, pady=2)

# ROW 5 (. - 0 - # - = )
btn_dot = Button(root, text=".", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("."))
btn_dot.grid(row=5, column=0, padx=4, pady=2) 

btn_0 = Button(root, text="0", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("0"))
btn_0.grid(row=5, column=1, padx=4, pady=2) 

btn_equ = Button(root, text="=", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("="))
btn_equ.grid(row=5, column=2, padx=4, pady=2) 

btn_mul = Button(root, text="*", width=6, height=2, font=font_properties, bg="black", fg=btn_fg, command=lambda:on_button_clicked("*"))
btn_mul.grid(row=5, column=3, padx=4, pady=2) 

root.mainloop()
              
