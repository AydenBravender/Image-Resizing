import tkinter as tk
from PIL import Image


def image_resize():
    
    # collecting data from tkinter window input
    X_size = int(X_resize.get())
    Y_size = int(Y_resize.get())
    image_dir = img_Dir.get()
    image_name = img_name.get()
    
    with Image.open(image_dir) as img:
        
        new_size = (X_size, Y_size)
        enlarged_img = img.resize(new_size)

        # Save the enlarged image
        image_name += ".jpg"
        enlarged_img.save(image_name)
        window.destroy()
    

window = tk.Tk()
Header = window.title('Image Resizer')
my_canvas = tk.Canvas(window, bg="black", height=600, width=600)
my_canvas.pack()

# adding the labels for the tkinter window
label = tk.Label(window, text='Input The Size of Image You Want to Resize')
label.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 100, window=label)

label_x = tk.Label(window, text='X')
label_x.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 150, window=label_x)

label_Dir = tk.Label(window, text='Enter Directory of Image: ')
label_Dir.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 300, window=label_Dir)

label_name = tk.Label(window, text='Enter Name Of New Image: ')
label_name.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 400, window=label_name)

# creating input windows
X_resize = tk.Entry(window)
my_canvas.create_window(225, 150, height=30, width=100, window=X_resize)

Y_resize = tk.Entry(window)
my_canvas.create_window(375, 150, height=30, width=100, window=Y_resize)

img_Dir = tk.Entry(window)
my_canvas.create_window(300, 350, height=30, width=400, window=img_Dir)

img_name = tk.Entry(window)
my_canvas.create_window(300, 450, height=30, width=400, window=img_name)

# the resize button
button = tk.Button(
    window,
    text="Resize Image",
    width=25,
    height=3,
    bg="black",
    fg="white",
    font=('helvetica', 10, 'bold'),
    command=image_resize
    )

my_canvas.create_window(300, 550, height=40,width=150, window=button)

window.mainloop()





