#!/bin/python
import argparse
import json
import os
import pathlib

CONFIG_DIRECTORY = pathlib.Path.home()/'.config/ubm'
CONFIG_FILE = CONFIG_DIRECTORY/'config.json'

def update_config_file(config):
    CONFIG_TEMP = CONFIG_DIRECTORY/'config.json.tmp'
    new_config_file = open(CONFIG_TEMP,'w')
    json.dump(config,new_config_file,indent=4)
    new_config_file.close()
    try:
        os.remove(CONFIG_FILE)
    except:
        None
    os.renames(CONFIG_TEMP,CONFIG_FILE)

def init_config():
    config={}
    config["default_browser"]={
        "browser" : '',
        "profile" : ''
    }
    config["mappings"]=[]
    return config

def print_config (config) : 
    default = config["default_browser"]
    mappings = config["mappings"] 
    print("Default:\n\tBrowser : {}\n\tProfile : {}".format(default["browser"],default["profile"]))
    for i,ele in  enumerate(mappings, start=0):
        print("\n{}:\tBrowser : {}\n\tProfile : {}\n\tURL Patterns:".format(i,ele["browser"],ele["profile"]))
        for j,ele_j in enumerate(ele["url_patterns"],start=0):
            print("\t\t{} : {}".format(j,ele_j))
    update_config_file(config)

def set_default(config,args) : 
    config["default_browser"]["browser"] = args[0]
    config["default_browser"]["profile"] = args[1]
    update_config_file(config)

def add_browser(config,args) : 
    new_browser = {
        "browser" : args[0],
        "profile" : args[1],
        "url_patterns" : []
    }
    config["mappings"].append(new_browser)
    update_config_file(config)

def add_map(config,args) : 
    try:
        config["mappings"][int(args[0])]["url_patterns"].append(args[1])
    except:
        print("Invalid Arguments")
    update_config_file(config)

def delete_map(config,args) : 
    try:
        config["mappings"][args[0]]["url_patterns"].pop(args[1])
    except:
        print("Invalid Arguments")
    update_config_file(config)
def delete_browser(config,args):
    try:
        config["mappings"].pop(args[0])
    except:
        print("Invalid Arguments")
    print_config(config)
    update_config_file(config)

########################################

parser = argparse.ArgumentParser(prog='ubmctl',description='Map browsers to url patterns.')
parser.add_argument('--list-maps','-l',help='list current browsers-url mappings',action='store_true')
parser.add_argument('--delete-map',help='delete a mapping',type=int,nargs=2,metavar=('BROWSER_INDEX','MAP_INDEX'))
parser.add_argument('--delete-browser',help='delete a browser',type=int,nargs=1,metavar=('BROWSER_INDEX'))
parser.add_argument('--set-default',help="Set default browser and profile",nargs=2,metavar=('BROWSER','PROFILE'))
parser.add_argument('--add-browser',help='Add a new browsers',nargs=2,metavar=('BROWSER','PROFILE'))
parser.add_argument('--add-map',help='Add a url pattern to a browser+profile',nargs=2,metavar=('BROWSER_INDEX','URL_PATTERN'),)

args = parser.parse_args()

if not CONFIG_DIRECTORY.is_dir() : 
    os.mkdir(CONFIG_DIRECTORY) 

if not CONFIG_FILE.is_file() :
    config = init_config()
    update_config_file(config)
else :
    config_file=open(CONFIG_FILE,'r')
    config=json.load(config_file)
    config_file.close()

if args.list_maps : 
    print_config(config)
elif args.set_default:
    set_default(config,args.set_default)
elif args.add_browser:
    add_browser(config,args.add_browser)
elif args.add_map:
    add_map(config,args.add_map)
elif args.delete_map:
    delete_map(config,args.delete_map)
elif args.delete_browser:
    delete_browser(config,args.delete_browser)
