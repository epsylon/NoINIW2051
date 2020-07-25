#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
NOINIW 2051 - by psy (epsylon@riseup.net)
"""
def init():
    uname = "Linux"
    starting_position = "/public  "
    root = "/" #
    files_tree = {"/contribute  ":("CONTRIBUTE.txt  ","PUBLISH_YOUR_LEVELS.txt  ","FINANCES.txt  "), "/public  ":("FAQ.pdf  ", "HELP.txt  ", "last_connections.log  ", "LEVEL.txt  ")}
    macs_tree = [212121]
    return uname, root, starting_position, files_tree, macs_tree
