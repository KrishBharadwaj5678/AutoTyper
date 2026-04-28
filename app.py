import pyautogui as pg

text = input("Enter Your Text: ")
times = int(input("Enter number of repetitions: "))
delay = int(input("Delay between messages: "))

pg.sleep(2)

for i in range(times):
    pg.write(text)
    pg.press("enter")
    pg.sleep(delay)