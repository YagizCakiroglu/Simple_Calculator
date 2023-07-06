
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator")
input_value = ""
display_text = tk.StringVar()

#Fonksiyon
def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)
def clear_button_action():
    global input_value
    input_value = ""
    display_text.set("")

def equal_button_action():
    global input_value
    try:
        result = str(eval(input_value))
        display_text.set(result)
        input_value = ""
    except ZeroDivisionError:
        messagebox.showerror("Hata", "Sıfıra bölmeye izin verilmez!")
        input_value = ""
        display_text.set("")

def delete_last_char():
    global input_value
    input_value = input_value[:-1]
    display_text.set(input_value)

def close_window():
    win.destroy()

input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=2)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=50, bg="#eee", bd=0,
                       justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
ygz_frame = tk.Frame(win, width=312, height=272.5, bg="black")
ygz_frame.pack()

# 1st row
button_back = tk.Button(ygz_frame, text="Back", fg="black", width=10, height=3, bd=0, bg="#FF0000", cursor="hand2",
                        command=lambda: delete_last_char())
button_clear = tk.Button(ygz_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#FF0000", cursor="hand2",
                      command=lambda: clear_button_action())
button_close = tk.Button(ygz_frame, text="Close", fg="black", width=10, height=3, bd=0, bg="#FF0000", cursor="hand2",
                         command=lambda: close_window())
button_divide = tk.Button(ygz_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#FF4500", cursor="hand2",
                       command=lambda: click_button_action("/"))

# 2nd row
button_7 = tk.Button(ygz_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(7))

button_8 = tk.Button(ygz_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(8))

button_9 = tk.Button(ygz_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(9))
button_hit = tk.Button(ygz_frame, text="X", fg="black", width=10, height=3, bd=0, bg="#FF8C00", cursor="hand2",
                         command=lambda: click_button_action("*"))

# 3rd row
button_4 = tk.Button(ygz_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(4))

button_5 = tk.Button(ygz_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(5)).grid(row=2, column=1, padx=1, pady=1)

button_6 = tk.Button(ygz_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(6)).grid(row=2, column=2, padx=1, pady=1)

button_extraction = tk.Button(ygz_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#DAA520", cursor="hand2",
                      command=lambda: click_button_action("-"))
# 4th row
button_1 = tk.Button(ygz_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(1))

button_2 = tk.Button(ygz_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(2))

button_3 = tk.Button(ygz_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(3))

button_add = tk.Button(ygz_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#FFD700", cursor="hand2",
                     command=lambda: click_button_action("+"))

# 5th row
button_0 = tk.Button(ygz_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#00FFFF", cursor="hand2",
                  command=lambda: click_button_action(0))

button_point = tk.Button(ygz_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#ADFF2F", cursor="hand2",
                      command=lambda: click_button_action("."))

button_equal = tk.Button(ygz_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#FFFF00", cursor="hand2",
                       command=lambda: equal_button_action())

#grid not: button_5 i buraya koyduğumda çalışmadı o yüzden yukarıdadır
button_back.grid(row=0,column=0,padx=1,pady=1)
button_clear.grid(row=0, column=1,padx=1, pady=1)
button_close.grid(row=0,column=2,padx=1,pady=1)
button_divide.grid(row=0, column=3, padx=1, pady=1)
button_7.grid(row=1, column=0, padx=1, pady=1)
button_8.grid(row=1, column=1, padx=1, pady=1)
button_9.grid(row=1, column=2, padx=1, pady=1)
button_hit.grid(row=1, column=3, padx=1, pady=1)
button_4.grid(row=2, column=0, padx=1, pady=1)
button_extraction.grid(row=2, column=3, padx=1, pady=1)
button_1.grid(row=3, column=0, padx=1, pady=1)
button_2.grid(row=3, column=1, padx=1, pady=1)
button_3.grid(row=3, column=2, padx=1, pady=1)
button_add.grid(row=3, column=3, padx=1, pady=1)
button_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
button_point.grid(row=4, column=2, padx=1, pady=1)
button_equal.grid(row=4, column=3, padx=1, pady=1)

win.mainloop()