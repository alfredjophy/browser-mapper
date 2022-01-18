#!/bin/python

import json
import sys
import re
import subprocess

try:
    config_file = open('./config.json','r')
except : 
    print("File not found!")
    exit()

config = json.load(config_file)
config_file.close()

patterns=config["patterns"]

url = sys.argv[1]

browser_defaults = {
    "chromium" : {
        "browsers" : ["brave","chromium","google-chrome"],
        "profile_command" : "--profile_directory=",
    },
    "firefox" : {
        "browsers": ["firefox","icecat","librewolf"],
        "profile_command": "-P ",
    },
    "firefox_pwa": {
        "browsers" : ["firefoxpwa"],
        "profile_command" : "site launch ",
    },
    "epiphany" : {
        "browsers" : ["epiphany"],
        "profile_command" : "--profile=",
    }
}

def launch_command(config,url) : 
    command = config["browser"]
    for i in browser_defaults:
        if config["browser"] in browser_defaults[i]["browsers"]:
            command = "{} {}'{}' '{}'".format(command,browser_defaults[i]["profile_command"],config["browser_profile"],url)
            break

    print(command)
    return command

command=''

for i in patterns:
    for j in i["url_patterns"]:
        if re.match(j,url,re.I) :
            command=launch_command(i,url)
            break
    else:
        continue
    break
else:
    if(config["default_browser"]["browser_profile"]==''):
        command = "{} {}".format(config["default_browser"]["browser"],url)
    else:
        commad = launch_command(config["default_browser"],url)

process = subprocess.Popen(command,start_new_session=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT,shell=True)
            



