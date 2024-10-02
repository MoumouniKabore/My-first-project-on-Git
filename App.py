from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calcul BMI")
root.geometry('300x400')
root.minsize(300, 400)
root.maxsize(500, 500)


# Fonction
def CalculBMI():
    # Calcul BMI
    try:
        valueWeight = float(entryWeight.get())
        valueHeight = float(entryHeight.get())
        BMI = valueWeight / valueHeight ** 2
    except ValueError:
        messagebox.showwarning("Warning", "You Must Enter a Number !!!")
    except ZeroDivisionError:
        messagebox.showwarning("Warning", "Enter Number Greater than Zero !!!")
    labelRes["text"] = round(BMI, 2)

    # Show Category
    if labelRes["text"] < 18.5:
        labelCat["text"] = "Under Weight"
    elif 18.5 <= labelRes["text"] <= 24.9:
        labelCat["text"] = "Normal Weight"
    elif 25 <= labelRes["text"] <= 29.9:
        labelCat["text"] = "Over Weight"
    elif 30 <= labelRes["text"] <= 34.9:
        labelCat["text"] = "Obesity"
    else:
        labelCat["text"] = "Severe Obesity"


# Main Frame
main_frame = Frame(root)
main_frame.pack(expand=True, fill="both", padx=20)

# Label title
label_title = Label(main_frame, text="Calcul Your BMI Here", font=("verdana", 15))
label_title.pack(expand=True, fill="both")

# Frame widget
middle_frame = Frame(main_frame)
category_frame = Frame(main_frame)
# Frame layout
middle_frame.pack(expand=True, fill="both", pady=30)
category_frame.pack(expand=True, fill="both", pady=10)

# Midle Frame
labelWeight = Label(middle_frame, text="Enter Your Weight (kg)", font=("verdana", 10))
entryWeight = Entry(middle_frame, justify="center")
labelHeight = Label(middle_frame, text="Enter Your Height (m)", font=("verdana", 10))
entryHeight = Entry(middle_frame, justify="center")
button = Button(middle_frame, text="Calcul", command=CalculBMI)
label = Label(middle_frame, text="Your BMI", font=("verdana", 10))
labelRes = Label(middle_frame, text="", relief="ridge")

# Middle Frame layout
middle_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
middle_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
labelWeight.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=15)
entryWeight.grid(row=0, column=3, columnspan=1, sticky="nsew", pady=5)
labelHeight.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=15)
entryHeight.grid(row=1, column=3, columnspan=1, sticky="nsew", pady=5)
button.grid(row=2, column=1, columnspan=2, sticky="ew")
label.grid(row=3, column=1, columnspan=1, sticky="nsew")
labelRes.grid(row=3, column=2, columnspan=1, sticky="nsew", pady=5)

# Category Frame
labelFrame = LabelFrame(category_frame, text='Your Category BMI', font=("verdana", 9), relief="ridge")
labelCat = Label(labelFrame, text='', font=("verdana", 11))
# Category Frame layout
labelFrame.pack(expand=True, fill="both", padx=30)
labelCat.pack(expand=True)

root.mainloop()


