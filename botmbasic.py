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
    driver.get("https://mbasic.facebook.com")
    try:
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.visibility_of_all_elements_located)
        element=driver.find_element_by_css_selector('#m_login_email')
        element.send_keys(username)
        element=driver.find_element_by_css_selector(".bo")
        element.send_keys(password)
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.visibility_of_all_elements_located)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,('.bq'))))
        LoginButton=driver.find_element_by_css_selector(".bq")
        LoginButton.click()
        print("logged in")
    except:
        pass

def openGroups(driver,wait):
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    element=driver.find_element_by_css_selector('a.bh:nth-child(8)')
    element.click()
    print('opened groups')

             
def getGroups(driver,wait,links):
    try:
        wait.until(EC.visibility_of_all_elements_located)
        wait.until(EC.presence_of_all_elements_located)
        i=1
        time.sleep(5)
        group=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/ul/li['+str(i)+']/table/tbody/tr/td[1]/a')
        #print('group found')
        while(group!=null):
            #print(group.get_attribute('href'))
            print('group found')
            links.append(group.get_attribute('href'))
            i+=1
            group=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/ul/li['+str(i)+']/table/tbody/tr/td[1]/a')
        print('got links for groups')
    except:
        return
    
def removeOneTap(driver,wait):
    wait.until(EC.presence_of_all_elements_located)
    wait.until(EC.visibility_of_all_elements_located)
    notNow=driver.find_element_by_css_selector('a.bm')
    notNow.click()
    print('removed one tap')

def postingroup(driver,wait):
    try:
        wait.until(EC.presence_of_all_elements_located)
        wait.until(EC.visibility_of_all_elements_located)
        moreButton=driver.find_element_by_css_selector('.cq > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)')
        moreButton.click()
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
        Textbox=driver.find_element_by_css_selector('#u_0_0')
        Textbox.send_keys(des)
        photoButton=driver.find_element_by_css_selector('div.bo:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)')
        photoButton.click()
        uploadButton=driver.find_element_by_css_selector('input.bd:nth-child(1)')
        uploadButton.send_keys(os.getcwd()+"\ecell\if.jpeg")
        previewButton=driver.find_element_by_css_selector('.bi')
        time.sleep(1)
        previewButton.click()
        #wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,('input.cd:nth-child(21)'))))
        wait.until(EC.visibility_of_all_elements_located)
        wait.until(EC.presence_of_all_elements_located)
        postButton=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div/form/input[18]')
        time.sleep(2)
        postButton.click()
        print('posted')
    except:
        return

def post(driver,wait,links):
    for link in links:
        driver.get(link)
        postingroup(driver,wait)

def clickSeeAll(driver,wait):
    try:
        seeAllButton=driver.find_element_by_css_selector('#m_more_item > a:nth-child(1)')
        seeAllButton.click()
        print('see all button pressed')
    except:
        return

print('Enter username: ')
usrnm=input()   
print('Enter password: ')
psswrd=input()
driver = webdriver.Firefox()
wait=WebDriverWait(driver,15)
login(driver,wait,usrnm,psswrd)
removeOneTap(driver,wait)
openGroups(driver,wait)
links=[]
clickSeeAll(driver,wait)
getGroups(driver,wait,links)
print(links)
print('is work')
post(driver,wait,links)