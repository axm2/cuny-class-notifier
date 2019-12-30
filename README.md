# cuny-class-notifier

## What is this? 

Run this script on your desktop. When your chosen class opens up, it'll play a sound loud enough that you will be able to run to your desk and enroll.

## Why not just make a script to enroll me in the class?

;)

## What are the requirements?

python, playsound, selenium, chromedriver

Download python: https://www.python.org/downloads/

Install playsound: `$ pip install playsound -U`

Install selenium: `$ pip install selenium -U`

Download chromedriver: https://chromedriver.chromium.org/downloads
edit line 84 to point to wherever you downloaded chromedriver

## Okay, how do I run it then?

Download the zip, extract it, open a terminal in that folder (powershell for instance if you're on windows)

sample usage: `$ python.exe .\main.py --institution 'Queens College' --term 'Spring' --year '2020' --subject 'Computer Science' --visible --classnum '54313'`

or without any arguments `$ python.exe .\main.py`

if and when the class opens up, it'll play a loud noise 10 times and quit
