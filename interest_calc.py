from tkinter import *


parent_window = Tk()
parent_window.title("PROJECT 201")
parent_window.geometry("800x800")
parent_window.configure(bg="grey")

def interest_calc():
    p = float(principle.get())
    t = float(time.get())
    r = float(rate.get())
    i = (p*t*r)/100
    interest = round(i,2)

    transaction_number = transaction_id.get()

    result_label.destroy()

    output_message = Label(result_frame, text="FOR TRANSACTION ID: "+ transaction_number + " THE FINAL RATE OF INTEREST IS: " + str(interest),bg="white", font=("Times new roman",15), width=100)
    output_message.place(x=20,y=360)
    output_message.pack()


app_label = Label(parent_window,text="INTEREST CALCULATOR",fg="black",font=("Times New Roman",20),bd=5,bg="grey")
app_label.place(x=230,y=20)

transaction_label = Label(parent_window,text="TRANSACTION NO.: ",fg="black",bg="grey",font=("Calibri",16),bd=1)
transaction_label.place(x=40,y=90)
transaction_id = Entry(parent_window,text="",width="25")
transaction_id.place(x=220,y=90)


amount_label = Label(parent_window,text="AMOUNT: ",fg="black",bg="grey",font=("Calibri",16),bd=1)
amount_label.place(x=40,y=200)
principle = Entry(parent_window,text="",width="25")
principle.place(x=140,y=200)

time_label = Label(parent_window,text="TIME: ",fg="black",bg="grey",font=("Calibri",16),bd=1)
time_label.place(x=40,y=240)
time = Entry(parent_window,text="",width="25")
time.place(x=100,y=240)

rate_label = Label(parent_window,text="RATE: ",fg="black",bg="grey",font=("Calibri",16),bd=1)
rate_label.place(x=40,y=280)
rate = Entry(parent_window,text="",width="25")
rate.place(x=100,y=280)


calc_button = Button(parent_window,text="CALCULATE",fg="white",bg="darkblue",command=interest_calc)
calc_button.place(x=180,y=320)


result_frame = LabelFrame(parent_window,text="RESULT",fg="black",bg="white",font=("Calibri",15))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=360) 

result_label = Label(result_frame,text="",bg="white",font=("Calibri",12),width=35)
result_label.place(x=20,y=360)
result_label.pack()



parent_window.mainloop()