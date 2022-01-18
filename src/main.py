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
# should represent the domain/IP ,else have full regex

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
    },
    {
        'url_patterns': ['algata.ga'],
        'browser' : 'brave',
        'browser_profile' : 'Profile 13'
    },
    {
        'url_patterns': ['github.com'],
        'browser' : 'firefoxpwa',
        'browser_profile' : '01FFAZW39PG9F70N1ASEZ17G5K'
    }
]

url = sys.argv[1]

browser_defaults = {
    "chromium" : {
        "browsers" : ["brave","chromium","google-chrome"],
        "profile_command" : "--profile_directory=",
    },
    "firefox" : {
        "browsers": ["firefox","icecat","librewolf"],
        "profile_command": "-P",
    },
    "firefox_pwa": {
        "browsers" : ["firefoxpwa"],
        "profile_command" : "site launch",
    }
}

def launch_command(config,url) : 
    command = config["browser"]

    for i in browser_defaults:
        if config["browser"] in browser_defaults[i]["browsers"]:
            command = "{} {} '{}' {}".format(command,browser_defaults[i]["profile_command"],config["browser_profile"],url)
            break

    print(command)
    return command

for i in config:
    for j in i["url_patterns"]:
        if re.match(j,url,re.I) :
            command=launch_command(i,url)
            process = subprocess.Popen(command,start_new_session=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell=True)
            process.communicate() 
            break
    else:
        continue
    break

exit()
            



