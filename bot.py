from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os
from docutils.parsers import null

def login(driver,wait,username,password):
    driver.get("https://www.facebook.com")
    try:
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.visibility_of_all_elements_located)
        element=driver.find_element_by_id("email")
        element.send_keys(usrnm)
        element=driver.find_element_by_id("pass")
        element.send_keys(psswrd)
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.visibility_of_all_elements_located)
        wait.until(EC.element_to_be_clickable((By.ID,('u_0_b'))))
        time.sleep(20)
        LoginButton=driver.find_element_by_id("u_0_b")
        LoginButton.click()
    except:
        exit(1)
    
def openGroups(driver,wait):
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    time.sleep(5)
    element=wait.until(EC.element_to_be_clickable((By.ID,'navItem_1434659290104689')))
    element=driver.find_element_by_id('navItem_1434659290104689')
    element.click()

def printLinks(link,i,links):
    try:
        while(link!=null):
            links.append(link.get_attribute('href'))
            i+=1
            link=driver.find_element_by_css_selector('.f4g9fmn2 > div:nth-child(2) > div:nth-child('+str(i)+') > a:nth-child(1)')
            
    except:
        print("added groups")
        return
             
def selectGroup(driver,wait,links):
    time.sleep(10)
    i=1
    link=driver.find_element_by_css_selector('.f4g9fmn2 > div:nth-child(2) > div:nth-child('+str(i)+') > a:nth-child(1)')
    printLinks(link,i,links)

def clickSeeMore(driver,wait):
    try:
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,('.jxbw8zu1'))))
        link=driver.find_element_by_css_selector('.jxbw8zu1')
        time.sleep(1)
        link.click()
        print("see more clicked")
        clickSeeMore(driver,wait)
    except:
        print("will return")
        return

def openLinks(driver,links):
    for i in links:
        driver.get(i)
        wait.until(EC.presence_of_all_elements_located)
        print(i)

def putpost(driver,des):
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    time.sleep(10)
    elm = driver.find_element_by_css_selector('li._1tm3:nth-child(1)')
    elm.click()
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    elm = driver.find_element_by_css_selector('._ikh > div:nth-child(2)')
    elm.click()
    elm.send_keys(des)
    time.sleep(5)
    elm = driver.find_element_by_css_selector('._i-o')
    elm.click()
    elm.send_keys(des)
    
    
    

def Post(driver,link):
    driver.get(link)
    des="""“The secret of getting ahead is getting started”
    E-Summit in association with Incubation Centre, IIIT Delhi brings to you the much
    awaited, StartUp Internship Fair - the biggest confluence of potential interns and
    employers.

    With internships in various profiles like AI, ML, DL, AR, VR, Sales/Marketing,
    Graphic Design, Video Editing, Android/iOS Developer, Web Dev, Content
    Writing, HR, Robotics, Finance, etc find the best internship suited to your skillset
    and enhance your CV.

    250+ Intern Positions Available
    25 Lakh+ Stipend on Offer!!
    Over 70+ StartUps!

    For more updates, 
    buy tickets at-: https://www.townscript.com/e/startup-internship-fair-242132
    check our facebook page:- https://www.facebook.com/ECell.IIITD/
    join our telegram channel:- https://t.me/esummit20"""
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    putpost(driver,des)
    
    

usrnm="puggalokchintan@gmail.com"   
psswrd="chintan20212920"
driver = webdriver.Firefox()
wait=WebDriverWait(driver,15)
login(driver,wait,usrnm,psswrd)
openGroups(driver,wait)
clickSeeMore(driver,wait)
links=[]
selectGroup(driver,wait,links)
#openLinks(driver,links)
Post(driver,links[0])