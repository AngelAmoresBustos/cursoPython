from tkinter import *

root=Tk()
root.title("Calculadora")
root.geometry("325x350")
root.resizable(0,0)
root.config(bg="black")
root.eval('tk::PlaceWindow . center')
# root.attributes("-topmost", True)
# root.attributes("-alpha", 0.9)

#------------------Pantalla------------------
i=0
def click_boton(valor):
    global i
    display.insert(i, valor)
    i+=1


def borrar():
    display.delete(0, END)
    i=0


def operacion():
    ecuacion=display.get()
    resultado=eval(ecuacion)
    display.delete(0, END)
    display.insert(0, resultado)
    i=0


display=Entry(root, font=("arial", 20, "bold"), bg="black", fg="green", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)


#------------------Botones------------------
boton1=Button(root, text="1", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(1))
boton1.grid(row=1, column=0, padx=5, pady=5)

boton2=Button(root, text="2", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(2))
boton2.grid(row=1, column=1, padx=5, pady=5)

boton3=Button(root, text="3", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(3))
boton3.grid(row=1, column=2, padx=5, pady=5)

boton_sum=Button(root, text="+", width=7, height=3, bg="orange", fg="white", borderwidth=0, command=lambda: click_boton("+"))
boton_sum.grid(row=1, column=3, padx=5, pady=5)

boton4=Button(root, text="4", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(4))
boton4.grid(row=2, column=0, padx=5, pady=5)

boton5=Button(root, text="5", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(5))
boton5.grid(row=2, column=1, padx=5, pady=5)

boton6=Button(root, text="6", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(6))
boton6.grid(row=2, column=2, padx=5, pady=5)

boton_rest=Button(root, text="-", width=7, height=3, bg="orange", fg="white", borderwidth=0, command=lambda: click_boton("-"))
boton_rest.grid(row=2, column=3, padx=5, pady=5)

boton7=Button(root, text="7", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(7))
boton7.grid(row=3, column=0, padx=5, pady=5)

boton8=Button(root, text="8", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(8))
boton8.grid(row=3, column=1, padx=5, pady=5)

boton9=Button(root, text="9", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(9))
boton9.grid(row=3, column=2, padx=5, pady=5)

boton_mult=Button(root, text="*", width=7, height=3, bg="orange", fg="white", borderwidth=0, command=lambda: click_boton("*"))
boton_mult.grid(row=3, column=3, padx=5, pady=5)

boton_borr=Button(root, text="C", width=7, height=3, bg="red", fg="white", borderwidth=0, command=borrar)
boton_borr.grid(row=4, column=0, padx=5, pady=5)

boton0=Button(root, text="0", width=7, height=3, bg="gray", fg="white", borderwidth=0, command=lambda: click_boton(0))
boton0.grid(row=4, column=1, padx=5, pady=5)

boton_igual=Button(root, text="=", width=7, height=3, bg="blue", fg="white", borderwidth=0, command=operacion)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

boton_div=Button(root, text="/", width=7, height=3, bg="orange", fg="white", borderwidth=0, command=lambda: click_boton("/"))
boton_div.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()