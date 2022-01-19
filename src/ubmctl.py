#!/bin/python

import argparse
import json
import os

def update_config_file(config):

    new_config_file = open('config.json.tmp','w')
    json.dump(config,new_config_file,indent=4)
    new_config_file.close()
    try:
        os.remove('config.json')
    except:
        None
    os.rename('config.json.tmp','config.json')



def print_config (config) : 
    mappings = config["patterns"] 
    default = config["default_browser"]
    print("Default:\n\tBrowser : {}\n\tProfile : {}".format(default["browser"],default["profile"]))

    for i,ele in  enumerate(mappings, start=0):
        print("\n{}:\tBrowser : {}\n\tProfile : {}\n\tURL Patterns:".format(i,ele["browser"],ele["profile"]))
        for j,ele_j in enumerate(ele["url_patterns"],start=0):
            print("\t\t{} : {}".format(j,ele_j))
    update_config_file(config)

def set_default(config,args) : 
    config["default_browser"]["browser"] = args[0]
    config["default_browser"]["profile"] = args[1]
    print_config(config)

########################################

parser = argparse.ArgumentParser(prog='ubmctl',description='Map browsers to url patterns.')
parser.add_argument('--list-maps','-l',help='list current browsers-url mappings',action='store_true')
parser.add_argument('--delete-map','-d',help='delete a mapping',type=int,nargs=2,metavar=('BROWSER_INDEX','MAP_INDEX'))
parser.add_argument('--set-default',help="Set default browser and profile",nargs=2,metavar=('BROWSER','PROFILE'))
parser.add_argument('--add-browser',help='Add a new browsers',nargs=2,metavar=('BROWSER','PROFILE'))
parser.add_argument('--add-map')

args = parser.parse_args()
print(args)

try:
    config_file = open('./config.json','r')
except : 
    print("File not found!")
    exit()

config = json.load(config_file)
config_file.close()

if args.list_maps : 
    print_config(config)
elif args.set_default:
    set_default(config,args.set_default)
