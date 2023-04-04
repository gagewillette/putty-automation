import pyautogui
import time as t
import subprocess


sleeptime = .1
path = "E:\\Users\\gagew\\Desktop\\putty\\putty.exe"
subprocess.Popen(path)
t.sleep(5)
inputBoxLocation = pyautogui.locateCenterOnScreen("pictures/ip-inputbox.png", confidence=0.7)
serialBoxLocation = pyautogui.locateCenterOnScreen("pictures/serial-clickbox.png", confidence=0.7)
consoleBoxLocation = pyautogui.locateCenterOnScreen("pictures/console.png", confidence=0.7)
aristaText = None
pyautogui.moveTo(serialBoxLocation)
t.sleep(sleeptime)
pyautogui.click()
t.sleep(sleeptime)
pyautogui.moveTo(inputBoxLocation)
t.sleep(sleeptime)
pyautogui.doubleClick()
t.sleep(sleeptime)
pyautogui.typewrite("COM4")
t.sleep(sleeptime)
pyautogui.press("enter")
t.sleep(sleeptime)
while True:
    aristaText = pyautogui.locateCenterOnScreen("pictures/aritsa-text.png" , confidence=0.7)
    if aristaText == None:
        print("Arista Text Not found trying again")
        t.sleep(.5)
        continue
    else:
        print("Found")
        break
# create wait for ctrl c
t.sleep(12)
with pyautogui.hold("ctrl"):
    pyautogui.press("c")
t.sleep(sleeptime)
pyautogui.typewrite("cd /mnt/flash")
pyautogui.press('enter')
t.sleep(sleeptime * 2)
pyautogui.typewrite("fullrecover")
pyautogui.press('enter')
t.sleep(sleeptime * 2)
pyautogui.typewrite('yes')
t.sleep(sleeptime)
pyautogui.press('enter')
while True:
    configsLocation = pyautogui.locateCenterOnScreen("pictures/configs-pic.png", confidence=0.7)
    if configsLocation == None:
        print("Configs text not found trying again")
        t.sleep(.5)
        continue
    else:
        print("Configs text found")
        break
t.sleep(3)
pyautogui.typewrite("cp /mnt/usb1/EOS-4.15.10M.swi /mnt/flash/EOS-4.15.10M.swi")
t.sleep(sleeptime)
pyautogui.press('enter')
t.sleep(sleeptime * 10)
pyautogui.typewrite("vi boot-config")
while True:
    viBootConfigLocation = pyautogui.locateCenterOnScreen("pictures/vi-boot-config.png", confidence=0.7)
    if viBootConfigLocation == None:
        print("Vi Configs text not found trying again")
        t.sleep(.5)
        continue
    else:
        print("Vi Configs text found")
        break
pyautogui.press("enter")
pyautogui.press("a")
for i in range(18):
    pyautogui.press("right")
for i in range(3):
    pyautogui.press("backspace")
pyautogui.typewrite("15.10M")
pyautogui.press("escape")
pyautogui.typewrite(":wq")
pyautogui.press('enter')
pyautogui.typewrite("reboot")
pyautogui.press("enter")
t.sleep(10)
while True:
    finalLoginLocation = pyautogui.locateCenterOnScreen("pictures/final-login.png", confidence=0.7)
    if finalLoginLocation == None:
        print("final login text not found trying again")
        t.sleep(.5)
        continue
    else:
        print("final login text found")
        break
t.sleep(sleeptime * 20)
pyautogui.typewrite("admin")
pyautogui.press("enter")
t.sleep(240)
pyautogui.typewrite("zerotouch disable")
pyautogui.press("enter")
t.sleep(120)
while True:
    finalLoginLocation = pyautogui.locateCenterOnScreen("pictures/final-login.png", confidence=0.7)
    if finalLoginLocation == None:
        print("final login text not found trying again")
        t.sleep(.5)
        continue
    else:
        print("final login text found")
        break
pyautogui.typewrite("show version")
t.sleep(20)



