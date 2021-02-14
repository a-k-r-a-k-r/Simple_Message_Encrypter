'''
    program: Simple Message Encrypter
    author : akr
    github : a-k-r-a-k-r
'''

#import necessary modules
import tkinter
import pyperclip
from tkinter import DISABLED,messagebox,BOTH,END


#Defining root window
root=tkinter.Tk()
root.title("Message Encrypter")
root.iconbitmap("resources/icons/encrypter.ico")


#mostly used characters
expected_char="qazwsxedcrfvtgbyhnujmikolp!@#$%^&*()1234567890POIUYTREWQASDFGHJKLMNBVCXZ~`<,>.?/:;'[{]}+=_-| "
expected_char+='"'


#colors
button_frame_color="grey"
button_color="green"
output_bg="black"


#Defining functions
def encrypt():
    cipher_text=''
    plain_text=input_data.get()

    if passwd_data.get()!='':
        passwd=int(passwd_data.get())
        for i in plain_text:
            index=expected_char.find(i)
            updated_index=(index+passwd)%94
            cipher_text+=expected_char[updated_index]
        output_data.config(text=cipher_text)
        #input_data.delete(0,END)
    else:
        messagebox.showerror("Invalid Password","You must enter a password")


def decrypt(): 
    plain_text=''
    cipher_text=input_data.get()
    
    if passwd_data.get()!='':
        depasswd=int(passwd_data.get())
        for i in cipher_text:
            new_index=expected_char.find(i)
            new_updated_index=(new_index-depasswd)%94
            plain_text+=expected_char[new_updated_index]
        output_data.config(text=plain_text)
        #input_data.delete(0,END)
    else:
        messagebox.showerror("Invalid Password","You must enter a password inorder to decrypt the message")


def copy_data():
    pyperclip.copy(output_data['text'])


#Defining frames
input_frame=tkinter.Frame(root)
button_frame=tkinter.Frame(root,bg=button_frame_color)
input_frame.pack()
button_frame.pack(fill=BOTH,expand=True)

#Defining widgets for frames
input_data=tkinter.Entry(input_frame,width=80)
output_data=tkinter.Label(input_frame,text="Your output will appear here",bg=output_bg,fg=button_color,width=50,wraplength=200)
copy_button=tkinter.Button(input_frame,text="Copy",bg=button_color,command=copy_data)
passwd_label=tkinter.Button(button_frame,text="Password",bg=button_frame_color,borderwidth=0)
passwd_data=tkinter.Entry(button_frame)
encrypt_button=tkinter.Button(button_frame,text="Encrypt",bg=button_color,command=encrypt)
decrypt_button=tkinter.Button(button_frame,text="Decrypt",bg=button_color,command=decrypt)

input_data.grid(row=0,column=0,columnspan=2,padx=10,pady=10,ipady=50)
output_data.grid(row=1,column=0,padx=10,pady=10,ipady=40,sticky="we")
copy_button.grid(row=1,column=1,pady=10,ipady=10,ipadx=20,padx=(0,10))
passwd_label.grid(row=0,column=0,pady=10,padx=(100,0),ipadx=20,ipady=10)
passwd_data.grid(row=0,column=1,pady=10,padx=(0,10),ipadx=50,ipady=10)
encrypt_button.grid(row=1,column=0,pady=10,padx=(80,0),ipadx=40,ipady=10)
decrypt_button.grid(row=1,column=1,pady=20,ipadx=40,ipady=10)


root.mainloop()