from tkinter import * 
import time
root = Tk(className=" Digital Clock⌚~zayed")  
root.geometry("325x250") #dimensions 325x250

label1 = Label(root, font=("Boulder", 30, 'bold'), bg="lightcyan2", fg="black", bd=30) 
label1.grid(row=1, column=1)

label2 = Label(root, font=("Boulder", 20, 'bold'), bg="lightcyan2", fg="black", bd=30) 
label2.grid(row=0, column=1)

def digiclock(): 
   time_live2 = time.strftime("%a : %d : %b : %Y") #paramteres passed of day,date,month,year
   time_live1 = time.strftime("%H:%M:%S") #to covert the live tuple time to string 
                                         #paramteres passed of Hour,minutes,seconds
   label2.config(text=time_live2)
   label1.config(text=time_live1) #overwriting over the label widget

   label1.after(180, digiclock) #for time gap between the seconds
                               #gap is of 180 ms(miliseconds) given by me on assumption

b=Button(root,text="Close",
         command=root.destroy,
         bg="snow",
         activebackground="black",
         font=("Comic Sans MS",15,"bold"))
b.grid(row=3,column=1)

digiclock() #giving call to digital clock fucntion
root.mainloop() #end