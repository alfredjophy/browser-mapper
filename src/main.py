#!/bin/python

import json
import sys
import re
import subprocess


# loading config file
# config_file = open('$HOME/.config/ubm/config','r')

# if not config_file:
    # config_file=open('$HOME/.config/ubm/config','w')
    # config_file.write('''{


    # }''')

# config = json.loads(config_file)

config = [
    {
        'url_patterns' : ['0.0.0.0','localhost','127.0.0.0'],
        'browser' : 'firefox',
        'browser_profile' : 'dev'
    },
    {
        'url_patterns' : ['google.com','meet.google.com','forms.google.com'],
        'browser' : 'firefox',
        'browser_profile' : 'college_stuff'
    }
]

url = sys.argv[1]

def launch_command(config,url) : 
    command = "{} -P {} {}".format(config["browser"],config["browser_profile"],url)
    return command

process = ""
for i in config:
    for j in i["url_patterns"]:
        if re.match(j,url,re.I) :
            command=launch_command(i,url)
            process = subprocess.Popen(command,stdout=subprocess.DEVNULL,start_new_session=True,stderr=subprocess.STDOUT,shell=True)
            break
    else:
        continue
    break


process.communicate() 
exit()
            



