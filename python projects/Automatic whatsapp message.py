# Importing the required module
import pyautogui as pg
import time

# Giving Dealy to run program
print("program will run after 5 second")
time.sleep(10)
print("running")

# Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

# For loop
for i in range(50):
    # writing the messages
    pg.write("write your message")
    time.sleep(0.2)
    # Seding the messages by pressing enter
    pg.press("Enter")