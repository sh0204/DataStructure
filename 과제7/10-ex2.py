from tkinter import *

window = Tk()
window.title("삼각형 프랙탈")

def drawTriangle(x,y,size):
    if size >= 30:
        drawTriangle(x,y,size/2)
        drawTriangle(x+size/2,y,size/2)
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2)
        
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill="red", outline="red")
     
     
wSize = 500
radius = 200
canvas = Canvas(window, height=wSize, width=wSize, bg='white')
drawTriangle(wSize/5, wSize/5*4, wSize*2/3)
canvas.pack()
window.mainloop()

   
    


