from tkinter import*
root = Tk()
root.title("ASCII AND ENCRYPTED CODE")
root.geometry("400x400")
root.configure(background='purple')

entry = Entry(root)
entry.place(relx = 0.5, rely = 0.4, anchor = CENTER)

name_in_ascii = Label(root, bg='yellow', fg="purple")
name_in_ascii.place(relx = 0.5, rely = 0.6, anchor = CENTER)

encryted_name = Label(root, bg='yellow', fg="purple")
encryted_name.place(relx = 0.5, rely = 0.7, anchor=CENTER)

def ascii():
    input_word = str(entry.get())
    for letter in input_word:
        name_in_ascii["text"]+= str(ord(letter))+" "
        ascii = int(ord(letter))
        encryted = ascii-1
        encryted_name["text"]+=str(chr(encryted))
        
btn = Button(root,text="display the Ascii code and Encrypted value ", command=ascii, bg='orange', fg='white')
btn.place (relx = 0.5, rely=0.5, anchor=CENTER)

root.mainloop()      