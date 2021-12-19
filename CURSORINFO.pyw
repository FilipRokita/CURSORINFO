#CURSORINFO
#Filip Rokita
#www.filiprokita.com



#import
import tkinter as tk
import pyautogui



#def
def start():
    startB.configure(state=tk.DISABLED)
    while True:
        root.update()
        pos = pyautogui.position()
        col = pyautogui.pixel(pos[0], pos[1])
        pyautogui.pixel(pos[0], pos[1])
        posL.configure(text=pos)
        colL.configure(text=col)



#main
root = tk.Tk()
root.title('CURSORINFO')
root.geometry('320x180')
root.resizable(False, False)

pyautogui.PAUSE = 0

startB = tk.Button(root, text='Start', command=start); startB.pack(pady=10)
posL = tk.Label(root, text='POSITION'); posL.pack()
colL = tk.Label(root, text='COLOR'); colL.pack()
authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack(pady=10)


root.mainloop()