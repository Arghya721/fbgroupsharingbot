from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
import pyautogui
import time

# str = input("Enter the content you want to share\n")
str = "Enter the content you want to share"
PATH = "C:\Program Files (x86)\chromedriver.exe"  #path of chromedriver
driver = webdriver.Chrome(PATH)


driver.get("https://www.facebook.com/")

username = driver.find_element_by_id("email")
username.send_keys("Username")   #Enter your fb username 
time.sleep(2)
password = driver.find_element_by_id("pass")
password.send_keys("password")   #Enter your fb password 
password.send_keys(Keys.RETURN) 

now = driver.current_url
find = "https://www.facebook.com/"
while now.find(find) == -1:
 now = driver.current_url

links = ["",""]  #put all the links where the post button starts with "What's on your mind {Your Name}". See the pic post2.png and replace it with yours.

keyboard.send("esc")
for share in links:
    driver.get(share)
    time.sleep(3)
    keyboard.send("esc")
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(3)
    # pyautogui.moveTo(309,746)
    public = pyautogui.locateOnScreen('post2.png', grayscale=False, confidence=0.8)
    print(public)
    # public = post2
    pyautogui.moveTo(public)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite(str)
    time.sleep(5)
    post = pyautogui.locateOnScreen('post.png', grayscale=True, confidence=0.8)
    while not post:
        post = pyautogui.locateOnScreen('post.png', grayscale=False, confidence=0.7)
        print(post)
    pyautogui.moveTo(post)
    pyautogui.click()
    time.sleep(3)

linkpublic = [""] #put all the links where the post button starts with "Create a public post". See the pic publicpost.png and replace it with yours.


for share in linkpublic:
    driver.get(share)
    time.sleep(3)
    keyboard.send("esc")
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(3)
    # pyautogui.moveTo(309,746)
    public = pyautogui.locateOnScreen('publicpost.png', grayscale=True, confidence=0.9)
    print(public)
    # public = post2
    pyautogui.moveTo(public)
    pyautogui.click()
    time.sleep(3)
    pyautogui.typewrite(str)
    time.sleep(5)
    post = pyautogui.locateOnScreen('post.png', grayscale=True, confidence=0.8)
    while not post:
        post = pyautogui.locateOnScreen('post.png', grayscale=False, confidence=0.7)
        print(post)
    pyautogui.moveTo(post)
    pyautogui.click()
    time.sleep(3)

driver.close()
