from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

from playsound import playsound

import time, re, os, getpass, sys, argparse


def main():
    classnum = -1
    institution = ""
    term = ""
    year = -1
    subject = ""

    parser = argparse.ArgumentParser()
    parser.add_argument("--classnum", help="class number", type=int)
    parser.add_argument("--institution",
                        help="college name in full eg. Queens College",
                        type=str)
    parser.add_argument("--term",
                        help="Spring, Summer, Fall, Winter",
                        type=str)
    parser.add_argument("--year", help="YYYY", type=int)
    parser.add_argument("--subject",
                        help="Subject name in full eg. Computer Science",
                        type=str)
    parser.add_argument("--visible",
                        help="Makes the browser visible",
                        action="store_true")
    args = parser.parse_args()
    if args.classnum:
        print("Class " + str(args.classnum) + " selected")
        classnum = args.classnum
    if args.institution:
        print("Institution " + args.institution + " selected")
        institution = args.institution
    if args.term:
        print("Term " + args.term + " selected")
        term = args.term
    if args.year:
        print("Year " + str(args.year) + " selected")
        year = args.year
    if args.subject:
        print("Subject " + args.subject + " selected")
        subject = args.subject

    if not args.institution:
        institution = institutionmenu()
        print("Institution " + institution + " selected")

    if not args.year:
        year = yearmenu()
        print("Year " + str(year) + " selected")

    if not args.term:
        term = termmenu()
        print("Term " + term + " selected")

    if not args.subject:
        subject = subjectmenu()
        print("Subject " + subject + " selected")

    if not args.classnum:
        classnum = classmenu()
        print("Class " + str(classnum) + " selected")

    # print all vars and ask the user is this correct? if not we ask again, if yes then we run
    flag = False

    options = Options()
    #options.binary_location = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
    if not args.visible:
        options.add_argument('headless')
    driver = webdriver.Chrome(
        chrome_options=options,
        executable_path="C:/Downloads/chromedriver_win32/chromedriver.exe",
    )
    driver.get("https://globalsearch.cuny.edu/")
    collegeID = driver.find_elements_by_xpath("//*[contains(text(), '" +
                                              institution +
                                              "')]")[0].get_attribute("for")
    driver.find_element_by_id(collegeID).click()
    selecttermyear = Select(driver.find_element_by_id('t_pd'))
    selecttermyear.select_by_visible_text(str(year) + " " + term + " Term")
    driver.find_element_by_name('next_btn').click()

    selectsubject = Select(driver.find_element_by_id('subject_ld'))
    selectsubject.select_by_visible_text(str(subject))
    selectcareer = Select(driver.find_element_by_id('courseCareerId'))
    selectcareer.select_by_visible_text('Undergraduate')
    driver.find_element_by_id(
        'open_classId').click()  #uncheck open classes only
    driver.find_element_by_id('btnGetAjax').click()
    classhtml = collegeID = driver.find_elements_by_xpath(
        "//*[contains(text(), '" + str(classnum) + "')]")[0].get_attribute("href")

    while not flag:
        driver.get(str(classhtml))
        classstatus = driver.find_element_by_id(
            'SSR_CLS_DTL_WRK_SSR_DESCRSHORT').get_attribute('innerHTML')
        if classstatus == "Open":
            flag = True
            for x in range(10):
                playsound('sound.mp3')
                time.sleep(1)
        print(classstatus)


def yearmenu():
    return input("Enter a year: ")  # i dont want to handle non int so i wont


def classmenu():
    return input(
        "Enter a class number: ")  # i dont want to handle non int so i wont


def termmenu():
    choice = '0'
    while choice == '0':
        print("Choose a term")
        print("Choose 1 for Spring")
        print("Choose 2 for Summer")
        print("Choose 3 for Fall")
        print("Choose 4 for Winter")

        choice = input("Please make a choice: ")

        if choice == "4":
            return "Winter"
        elif choice == "3":
            return "Fall"
        elif choice == "2":
            return "Summer"
        elif choice == "1":
            return "Spring"
        else:
            print("I don't understand your choice.")


def subjectmenu():
    choice = '0'
    while choice == '0':
        print("Choose a subject")
        print("Choose 1 for Computer Science")
        print("Choose 2 for Mathematics")
        print("Choose 3 for Other")

        choice = input("Please make a choice: ")

        if choice == "1":
            return "Computer Science"
        elif choice == "2":
            return "Mathematics"
        elif choice == "3":
            return input("Enter FULL subject name: ")
        else:
            print("I don't understand your choice.")


def institutionmenu():
    choice = '0'
    while choice == '0':
        print("Choose a college")
        print("Choose 1 for Queens College")
        print("Choose 2 for Other")

        choice = input("Please make a choice: ")

        if choice == "1":
            return "Queens College"
        elif choice == "2":
            return input("Enter FULL institution name: ")
        else:
            print("I don't understand your choice.")


main()
