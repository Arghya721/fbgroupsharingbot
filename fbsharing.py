from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
import pyautogui
import time

# str = input("Enter the content you want to share\n")
str = "HTML Series part #3 .. Follow our page for part #4 ...  Coming Tomorrow....  https://www.facebook.com/permalink.php?story_fbid=121385706629240&id=101279261973218 "
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.facebook.com/")

username = driver.find_element_by_css_selector(".inputtext._55r1._6luy._9npi")
username.send_keys("agenamonsetan@gmail.com")
time.sleep(2)
password = driver.find_element_by_id("pass")
password.send_keys("tacmpfe@721507")
password.send_keys(Keys.RETURN)

now = driver.current_url
find = "https://www.facebook.com/"
while now.find(find) == -1:
 now = driver.current_url

links = ["https://www.facebook.com/groups/220286455785894/","https://www.facebook.com/groups/websitedesigndevelopmentcompany/","https://www.facebook.com/groups/codingqna/?multi_permalinks=1307379422966803","https://www.facebook.com/groups/290978921088322/?multi_permalinks=1604096499776551"]

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

linkpublic = ["https://www.facebook.com/groups/512918662821923/","https://www.facebook.com/groups/WebDesignWebDevelopment/?multi_permalinks=2867361253505613","https://www.facebook.com/groups/websitedesigndevelopment","https://www.facebook.com/groups/230331318572435"]


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