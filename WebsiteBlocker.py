import time
from datetime import datetime as dt
import re

path = "<Path to hosts file>"
host_addr = "127.0.0.1"
website_list = []


def isValidURL(str):
# Regex to check valid URL
    regex = ("(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


while True:
    user_input = input("Enter Webstie to Block [q to continue]: " )
    if user_input == 'q' :
        break
    if isValidURL(user_input):
        website_list.append(user_input)
    else:
        print("url is not valid! (please try again)")
        

time = 9
while (time > 8 or time < 1):
     time = int(input("Type in how many hours would you like to block(Number between 1-8 ) :"))

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,8+time):
        with open(path, 'r+') as file:
            content = file.read()
            for web in website_list:
                if web in content:
                    pass
                else:
                    file.write(host_addr + " " + web + "\n")
        print("The block was successful")
    else:
        with open(path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website_list):
                    file.write(line)
            # removing hostnmes from host file
            file.truncate()
    time.sleep(5)
