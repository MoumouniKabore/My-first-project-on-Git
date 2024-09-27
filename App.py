from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calcul BMI")
root.geometry('400x500+450+100')
root.minsize(400, 500)


# Fonction
def CalculBMI():

    # Calcul BMI
    try:
        valueWeight = float(entryWeight.get())
        valueHeight = float(entryHeight.get())
        BMI = valueWeight / valueHeight ** 2
    except ValueError:
        messagebox.showwarning("Warning", "You Must Enter Number !!!")
    except ZeroDivisionError:
        messagebox.showwarning("Warning", "Enter Number Greater than Zero !!!")
    labelRes["text"] = round(BMI, 2)
    
    # Show Category
    if labelRes["text"] < 18.5:
        label_back["text"] = "Under Weight"
    elif 18.5 <= labelRes["text"] <= 24.9:
        label_back["text"] = "Normal Weight"
    elif 25 <= labelRes["text"] <= 29.9:
        label_back["text"] = "Over Weight"
    elif 30 <= labelRes["text"] <= 34.9:
        label_back["text"] = "Obesity"
    else:
        label_back["text"] = "Severe Obesity"


# Main Frame
main_frame = Frame(root, background="dimgrey")
main_frame.pack(expand=True)


# Label title
label_title = Label(main_frame, text="Calcul Your BMI Here", font=("aptos", 20), height=2, width=10, justify=CENTER, background="silver", fg="black")
label_title.pack(expand=True, fill="both", padx=10, pady=10)


# Frame widget
middle_frame = Frame(main_frame, height=250, width=350, background="dimgrey")
category_frame = Frame(main_frame, height=90, width=350, background="dimgrey")
# Frame layout
middle_frame.pack(expand=True, fill="both", pady=5)
category_frame.pack(expand=True, fill="both", pady=20)


# Middle Frame
labelWeight = Label(middle_frame, text="Enter Your Weight (kg)", width=20, font=("aptos", 11), background="dimgrey", fg="white")
entryWeight = Entry(middle_frame, width=6, font=("aptos", 13), justify="center")
labelHeight = Label(middle_frame, text="Enter Your Height (m)", width=20, font=("aptos", 11), background="dimgrey", fg="white")
entryHeight = Entry(middle_frame, width=6, font=("aptos", 13), justify="center")
button = Button(middle_frame, text="Calcul", width=20, font=("aptos", 10), relief="raised", background="silver", fg="black", command=CalculBMI)
label = Label(middle_frame, text="Your BMI", width=8, font=("aptos", 11), background="dimgrey", fg="white")
labelRes = Label(middle_frame, text="", width=6, font=("aptos", 12), justify="center", background="white", fg="black", relief="flat")
# Middle Frame layout
labelWeight.place(x=40, y=50)
entryWeight.place(x=230, y=50)
labelHeight.place(x=40, y=90)
entryHeight.place(x=230, y=90)
button.place(x=90, y=140)
label.place(x=95, y=210)
labelRes.place(x=185, y=210)


# Category Frame
label_back = Label(category_frame, text='', height=4, width=35, font=("aptos", 10), relief="flat", background="white", fg="black")
label_font = Label(category_frame, text='Your Category BMI', height=2, width=25, font=("aptos", 9), relief="raised", background="silver", fg="black")
# Category Frame layout
label_back.place(x=30, y=30)
label_font.place(x=85, y=5)


root.mainloop()


