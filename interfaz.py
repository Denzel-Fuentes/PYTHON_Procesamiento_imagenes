import tkinter as tk
import cv2
import matplotlib.pyplot as plt
foto = cv2.imread("flowers.jpg")
win= tk.Tk()
win.geometry("750x550")
def print_text(text):
   tk.Label(win, text=text,font=('Helvetica 13 bold')).pack()
   if (text == "imagen"):
          plt.imshow(cv2.cvtColor(foto,cv2.COLOR_BGR2RGB))
          plt.show()
          print(w.get())
   elif( text == "rojo"):
          plt.imshow(foto[:,:,0])
          plt.show()
   elif( text == "verde"):
          plt.imshow(foto[:,:,1])
          plt.show()
   elif( text == "azul"):
          plt.imshow(foto[:,:,2])
          plt.show()       
   elif( text == "gris"):
          plt.imshow(cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY) ,cmap="gray")
          plt.show()                 
w = tk.Scale(win, from_=0, to=42)
w.pack()
w2 = tk.Scale(win, from_=0, to=200, orient=tk.HORIZONTAL)
w2.pack()
btn1= tk.Button(win, text="Imagen" ,command= lambda:print_text("imagen"))
btn1.pack(pady=10)
btn2= tk.Button(win, text="Color Rojo",command= lambda:print_text("rojo"))
btn2.pack(pady=10)
btnVerde= tk.Button(win, text="Color verde",command= lambda:print_text("verde"))
btnVerde.pack(pady=10)
btnAzul= tk.Button(win, text="Color azul",command= lambda:print_text("azul"))
btnAzul.pack(pady=10)
btnBlancoNegro= tk.Button(win, text="Gris",command= lambda:print_text("gris"))
btnBlancoNegro.pack(pady=10)
btn3= tk.Button(win, text="Button3" ,command= lambda:print_text("Button 3"))
btn3.pack(pady=10)
 
win.mainloop()