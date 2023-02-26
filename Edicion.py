from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageOps

def change_brush_color(new_color):
    global brush_color
    brush_color = new_color

def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

def erase(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")

def insert_image():
    file_path = filedialog.askopenfilename(filetypes=[
        ('JPEG Files','*.jpeg'),
        ('Jpg Files', '*.jpg'),
        ('PNG Files','*.png')])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((500,500))
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=NW, image=photo)

root = Tk()
root.title("Pintar-Borrar")
root.geometry("550x600")
root.resizable(width=False, height=False)

canvas = Canvas(root, bg="white", width=500, height=500) #Tamaño espacio pintar
canvas.grid(row=0, column=0, rowspan=10, padx=25, pady=25)

#Abrir imagen seleccionada
file_path = filedialog.askopenfilename(filetypes=[
        ('JPEG Files','*.jpeg'),
        ('Jpg Files', '*.jpg'),
        ('PNG Files','*.png')])
if file_path:
    image = Image.open(file_path)
    image = image.resize((500,500))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=NW, image=photo)

brush_color = "black"
brush_size = 2

canvas.bind("<B1-Motion>", paint)

image_button = Button(root, text="Insertar Imagen", command=insert_image)
image_button.place(x=69,y=550,anchor=CENTER)

eraser_button = Button(root, text="Borrador", command=lambda: change_brush_color("white"))
eraser_button.place(x=207,y=550,anchor=CENTER)

brush_button = Button(root, text="Pincel", command=lambda: change_brush_color("black"))
brush_button.place(x=345,y=550,anchor=CENTER)

clear_button = Button(root, text="Limpiar", command=lambda: canvas.delete("all"))
clear_button.place(x=483,y=550,anchor=CENTER)

root.mainloop()