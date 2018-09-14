import time
from datetime import datetime



host_path = '/etc/hosts'
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "mail.google.com", "mail.yahoo.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.writeline()
            file.truncate()

    time.sleep(5)
