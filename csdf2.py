import random
import string
from tkinter import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk

def generate_random_captcha_text(length=4):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_captcha():
    global captcha_text, captcha_image
    captcha_text = generate_random_captcha_text()
    image = ImageCaptcha(width=250, height=100)
    image.write(captcha_text, 'captcha.png')
    pil_image = Image.open('captcha.png')
    captcha_image = ImageTk.PhotoImage(pil_image)
    canvas.itemconfig(image_on_canvas, image=captcha_image)

def captcha_login():
    username = u.get()
    password = p.get()
    entered_captcha = c.get().replace(" ", "")
    if username == 'test' and password == '1234':
        if entered_captcha.upper() == captcha_text:
            messagebox.showinfo("Login Status", "Login Successful")
        else:
            messagebox.showinfo("Login Status", "Login failed: Incorrect captcha")
    else:
        messagebox.showinfo("Login Status", "Login failed: Incorrect username or password")

root = Tk()
root.title("Login System with Captcha")
canvas = Canvas(root, width=250, height=100)
canvas.pack()
image_on_canvas = canvas.create_image(0, 0, anchor=NW)
Label(root, text="Username", font=("Courier", 14)).pack()
u = Entry(root)
u.pack()
Label(root, text="Password", font=("Courier", 14)).pack()
p = Entry(root, show="*")
p.pack()
Label(root, text="Captcha", font=("Courier", 14)).pack()
c = Entry(root)
c.pack()
Button(root, text="Refresh Captcha", command=generate_captcha).pack()
Button(root, text="Login", command=captcha_login).pack()
generate_captcha()
root.mainloop()