import tkinter as tk
from tkinter import messagebox


min=100*0

def bill(units):

    if units>=200:
        return min+(100*5)+((units-200))*10
    elif units>100:
        return min+(((units)-100)*5)
    elif units<100:
        return min
def printBill():
    try:  
        button_calculate.pack()
        user=float(entry.get())
        amount=bill(user)
        result_text.set(f"\n\nTotal bill amount:{amount}")
    except:
        messagebox.showerror("Invalid Input!!", " Enter the inputs in number") 


    
        
        
# printBill()
    
window=tk.Tk()
window.maxsize(600, 700)
window.geometry('350x400')
window.title("Bill printer")
mylabel=tk.Label(window,text="Bill printer ",font=("Impact",50),fg='Black')
mylabel.pack()


result_text = tk.StringVar()
label_result = tk.Label(window, textvariable=result_text)
label_result.pack(pady=30)




label_amount= tk.Label(window, text="Enter bill unit",fg='red')
label_amount.pack()
entry = tk.Entry(window, font=("Arial", 20))
entry.pack()
button_calculate = tk.Button(window, text="Calculate",command=printBill,fg='green')
button_calculate.pack(pady=30)
window.mainloop()



