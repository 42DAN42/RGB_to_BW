from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw


def open_file():
    file = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg"), ("All files", "*.png"), ("Image files", "*.jpeg")))
    if file:
        label1.configure(text=file)
        load = Image.open(file)
        img = ImageTk.PhotoImage(load)
        picture1 = Toplevel()
        picture1.title("Picture")
        label = Label(picture1, image=img)
        label.image = img
        label.pack()


def gray():
    res = label1.cget("text")
    if res:
        image = Image.open(res)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        source = image.split()
        R, G, B = 0, 1, 2

        loadr = source[R]
        loadg = source[G]
        loadb = source[B]

        ar = slider3.get()
        outr = loadr.point(lambda i: i * 0.299 * float(ar))

        ag = slider4.get()
        outg = loadg.point(lambda i: i * 0.587 * float(ag))

        ab = slider5.get()
        outb = loadb.point(lambda i: i * 0.114 * float(ab))

        img1 = Image.merge('RGB', (outr, outg, outb))
        img = img1.convert("L")

        picture = Toplevel()
        picture.title("ImageGray")
        img1 = ImageTk.PhotoImage(img)
        label3 = Label(picture, image=img1)
        label3.image = img1
        label3.pack()

        def save_png():
            filename = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')], defaultextension=".png")
            if filename:
                img.save(filename, "PNG")

        def save_jpeg():
            filename = filedialog.asksaveasfilename(filetypes=[('JPEG files', '*.jpeg')], defaultextension=".jpeg")
            if filename:
                img.save(filename, "JPEG")

        btn6 = Button(picture, text="Сохранить ЧБ в PNG", command=save_png, bg="white", fg="black")
        btn6.pack(side=LEFT, padx=5, pady=5)

        btn7 = Button(picture, text="Сохранить ЧБ в JPEG", command=save_jpeg, bg="white", fg="black")
        btn7.pack(side=LEFT, padx=5, pady=5)

        picture.mainloop()


window = Tk()
window.title("TRUE BW")
window.geometry('320x360')

btn1 = Button(window, text="Открыть изображение", command=open_file, bg="white", fg="black", padx=20, pady=8, font=17)
btn1.place(x=60, y=50)

btn3 = Button(window, text="      Переводим в ЧБ     ", command=gray, bg="white", fg="black", padx=20, pady=8, font=17)
btn3.place(x=65, y=270)

label1 = Label(window, text="Смеситель RGB каналов", fg="#eee")
label1.pack()

label3 = Label(text="Выберите изображение и внесите изменения", fg="#eee")
label3.pack()

slider3 = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=5, tickinterval=0.5, resolution=0.1,
                troughcolor="red")
slider3.place(x=10, y=90)

slider4 = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=5, tickinterval=0.5, resolution=0.1,
                troughcolor="green")
slider4.place(x=10, y=145)

slider5 = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=5, tickinterval=0.5, resolution=0.1,
                troughcolor="blue")
slider5.place(x=10, y=200)

slider3.set(1)
slider4.set(1)
slider5.set(1)

window.mainloop()