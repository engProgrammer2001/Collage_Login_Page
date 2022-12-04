
# this is used to make GUI.

from tkinter import*
from PIL import ImageTk,Image # this is used to take image
from tkinter import messagebox # This is used to create messagebox

# here i will create a function which will handle my login page
def handle_login():
    email = email_input.get()
    password = password_input.get()
    print(email,password)
    if email == "askushwaha613@gmail.com" and password == 'Ashok@2002':
        messagebox.showinfo("Welcome in SHRI RAM GROUP")
    else:
        messagebox.showerror("Sorry!, Login Failed")


root = Tk()   # This is used to make a new window page
root.title("Collage Login..")  # this is used to change the title of page
root.iconbitmap("login.ico")  # This is used to change icon of the page
# root.minsize(400,650)  #if we will give minsize(x,y) then window will not min from given size.
# root.maxsize(400,650) #if we will give maxsize(x,y) then window will not max from given size.
root.geometry('400x650') # we can create fix size window by using this line.
root.resizable(0,0) #This line can fix of window page
root.configure(background='#8FBC8F')
img = Image.open('shri ram logo.png') # this is store a image in img variable
resize_img = img.resize((120,130)) # this is used to resize the image
img = ImageTk.PhotoImage(resize_img) # by help this line we will bring image
img_label = Label(root,image=img)
# by using pady we can give padding x and y.
img_label.pack(pady=(20,10))  # It will give suggest that where we have to put image

text_label = Label(root,text='Shri Ram Group Jabalpur',fg='white',bg='#8FBC8F') # this line is use for the add text bellow the image
text_label.pack()
text_label.config(font=('italic',24))

# This is use to create space for write email
email_label = Label(root,text='Enter email:',fg='white',bg='#8FBC8F')
email_label.pack(pady=(40,0)) #this show in the display
email_label.config(font=("bold",14)) # this is set font and size of font

# This is use to make space for mail input_
email_input = Entry(root,width=60,fg="blue")
email_input.pack(pady=(10,0),ipady=4) # this is used to display on the screen.

# this is used to create "Enter password" space for this word.
password_label = Label(root,text='Enter password:',fg='white',bg='#8FBC8F')
password_label.pack(pady=(40,5)) # this is used to display on the screen.
password_label.config(font=('bold',14)) # this is used only set font type and size.

# this is used to make Entry space of password
password_input = Entry(root,width=60,fg='blue')
password_input.pack(pady=(10,0),ipady=4)

# this code is for create button
login_button = Button(root,text='Login Here',fg='blue',bg='white',width=12,command=handle_login)
login_button.pack(pady=(50,0))
login_button.config(font=('bold',13))

root.mainloop()  # this is used to stop the windows page in screen.


