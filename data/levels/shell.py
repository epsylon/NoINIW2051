#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
NOINIW 2051 - by psy (epsylon@riseup.net)
"""
import time

from data.levels.level0.level0_2 import login as level0_2

VERSION = "y-shell v0.1 'NoWb1e sh3ll' (23042020)"

def getPWD(current_position): # pwd
    current_path = current_position
    if not current_path.startswith("/"):
       current_path = "/"+current_path
    return current_path

def changePWD(mac_root, current_position, files_tree, direc): # cd+dir
   current_path = None
   for k in files_tree.keys():
        if direc in k:
            current_path = direc
        else:
            if direc == mac_root:
                current_path = mac_root
   if not current_path:
       current_path = current_position
   if not current_path.startswith("/"):
       current_path = "/"+current_path
   return current_path

def getList(mac_root, current_position, files_tree): # ls/dir
    for k,v in files_tree.items():
        if len(current_position) > 2 and current_position in k: # not /
            listed_files = v
        else:
            if current_position == mac_root:
                listed_files = files_tree.keys()
    return listed_files

def getId(ACCESS_LEVEL): # id/whois
    user_id = ACCESS_LEVEL
    return user_id

def getHostName(NETWORK_MACHINE_NUMBER): # hostname
    hostname = NETWORK_MACHINE_NUMBER
    return hostname

def getUname(mac_uname): # uname
    uname = mac_uname
    return uname

def getCdUP(mac_root, current_position): # cd_up
    current_path = mac_root 
    return current_path

def getCAT(CURRENT_LANGUAGE, level, current_position, files_tree, file_target): # cat
    file_text = None
    final_text = []
    final_file_text = []
    for k,v in files_tree.items():
        if current_position in str(k):
            for f in v:
                if file_target == str(f).replace("  ",""):
                    if str(f.replace("  ","")) == "FAQ.pdf": # level_0: fake FAQ.pdf file
                        f = "FAQ.txt"
                        CURRENT_LANGUAGE = -1
                    if str(f.replace("  ","")) == "last_connections.log": # level_0: last connection logs
                        f = "last_connections.txt"
                        CURRENT_LANGUAGE = -1
                    m = open("data/levels/level"+str(level)+"/data/"+str(f.replace("  ","")), "r")
                    file_text = m.readlines()
                    for line in file_text:
                        if CURRENT_LANGUAGE == "0": # ENGLISH
                            if line.startswith("ENGLISH"):
                                final_text.append(str(line.split(":")[1]))         
                        elif CURRENT_LANGUAGE == "1": # SPANISH
                            if line.startswith("SPANISH"):
                                final_text.append(str(line.split(":")[1]))
                        else: # NOT TRANSLATION REQUIRED (CURRENT_LANGUAGE= -1)
                            final_text.append(str(line))
                    m.close()
    if file_text == None:
        file_text = 'y-shell: file not found: "'+str(file_target)+'"'
        final_file_text.append(str(file_text))
    else:
        for text in final_text:
            final_file_text.append(str(text).replace("\n", ""))
    return final_file_text

def installProgram(current_position, files_tree, file_target): # install program
    file_text = None
    for k,v in files_tree.items():
        if current_position in str(k):
            for f in v:
                if file_target == str(f).replace("  ","") and file_target.endswith(".app"):
                    file_text = "y-shell: program '"+str(file_target)+"' has been installed!"
    if not file_text:
        file_text = "y-shell: program '"+str(file_target)+"' not valid!"
    return file_text

def connectMac(current_position, macs_tree, file_target, surface, WINDOW_SIZE, CURRENT_LANGUAGE): # connect to machine
    file_text = None
    for v in macs_tree:
        if file_target == str(v).replace("\n",""):
            file_text = "y-shell: connecting to: '"+str(file_target)+"' ..."
            time.sleep(3) # wait for login
            NETWORK_MACHINE_NUMBER = file_target
            level0_2(surface, WINDOW_SIZE, CURRENT_LANGUAGE, NETWORK_MACHINE_NUMBER) # go for level 2
    if not file_text:
        file_text = "y-shell: connection to: '"+str(file_target)+"' failed!"
    return file_text
