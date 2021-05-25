from tkinter import *

window = Tk()
window.title("Ticket Sales")
window.config(bg="#0d1117")
window.geometry("500x500")


def bmi_calc():
    if variable.get() == "Male":
        _weight = float(weight_entry.get())
        _height = float(height_entry.get())
        bmi_m_ans = ((0.5 * float(_weight)) / ((float(_height) / 100) ** 2)) + 11.5
        ideal_bmi.set(bmi_m_ans)
        bmi_ans = float(_weight) / ((float(_height) / 100) ** 2)
        bmi.set(bmi_ans)

    elif variable.get() == "Female":
        _weight = float(weight_entry.get())
        _height = float(weight_entry.get())
        age = float(age_entry.get())
        bmi_f_ans = ((0.5 * _weight) / ((_height / 100) ** 2)) + (0.03 * age) + 11
        ideal_bmi.set(bmi_f_ans)
        bmi_ans = float(_weight) / ((float(_height) / 100) ** 2)
        bmi.set(bmi_ans)

def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')

def exit_window():
    return window.destroy()


def clear():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_entry.config(state='normal')
    ideal_bmi_entry.config(state='normal')
    age_entry.delete(0, END)
    bmi_entry.delete(0, END)
    ideal_bmi_entry.delete(0, END)
    age_entry.config(state='readonly')
    bmi_entry.config(state='readonly')
    ideal_bmi_entry.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])


# global variables
bmi = StringVar()
ideal_bmi = StringVar()
variable = StringVar()
# y=100
weight = Label(window, text="Weight:")
weight_entry = Entry(window)
kg_label = Label(window, text="kilograms:")
weight.place(x=10, y=100)
weight_entry.place(x=100, y=100)
kg_label.place(x=300, y=100)

# y=150
height = Label(window, text="Height:")
height_entry = Entry(window)
cm_label = Label(window, text="CM:")
height.place(x=10, y=150)
height_entry.place(x=100, y=150)
cm_label.place(x=300, y=150)
# y=200
calculate_body_mass_index = Button(window, text="Calculate Your Ideal Body Mass Index", command=bmi_calc)
calculate_body_mass_index.place(x=25, y=200)
# y=250
gender = Label(window, text="Gender:")
options = ['Select...', 'Male', "Female"]
variable.set(options[0])
gender_menu = OptionMenu(window, variable, *options, command=activate)
age_label = Label(window, text="Age:")
age_entry = Entry(window)
gender.place(x=10, y=250)
gender_menu.place(x=100, y=250)
age_label.place(x=250, y=250)
age_entry.place(x=300, y=250)
# y=350
bmi_label = Label(window, text="BMI:")
bmi_entry = Entry(window, textvariable=bmi, )
ideal_bmi_label = Label(window, text="Ideal BMI:")
ideal_bmi_entry = Entry(window,  textvariable=ideal_bmi,)
bmi_label.place(x=10, y=300)
bmi_entry.place(x=100, y=300)
ideal_bmi_label.place(x=10, y=340)
ideal_bmi_entry.place(x=100, y=340)

# y=375
clear_button = Button(window, text="Clear", command=clear)
exit_button = Button(window, text="Exit", command=exit_window)
clear_button.place(x=50, y=375)
exit_button.place(x=150, y=375)

window.mainloop()
