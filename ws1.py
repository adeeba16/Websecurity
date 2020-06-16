from datetime import datetime as dt
import time
temp_host = 'hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com']
hosts_path = '/etc/hosts'


while True:
    today = dt.now()
    if (dt(dt.now().year, dt.now().month, dt.now().day,15)<today<dt(dt.now().year, dt.now().month, dt.now().day,16,30)):
        print('working',dt.now())
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect+ " "+website+ '\n')
        

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('not working hour',dt.now())

    time.sleep(1)
