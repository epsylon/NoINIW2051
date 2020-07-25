#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
NOINIW 2051 - by psy (epsylon@riseup.net)
"""
import pygame
import sys, os, random

import data.levels.shell as shell
import data.menu as menu
import data.levels.level0.tree as tree

def level0_shell(surface, WINDOW_SIZE, set_language, ACCESS_LEVEL, NETWORK_MACHINE_NUMBER, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, COLOR_GREEN):
    init(surface, WINDOW_SIZE, set_language, ACCESS_LEVEL, NETWORK_MACHINE_NUMBER, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, COLOR_GREEN)

def init(surface, WINDOW_SIZE, set_language, ACCESS_LEVEL, NETWORK_MACHINE_NUMBER, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, COLOR_GREEN):
    CURRENT_LEVEL = 0 # set current level
    CURRENT_LANGUAGE = set_language # set current language
    ACCESS_LEVEL = str(ACCESS_LEVEL)
    NETWORK_MACHINE_NUMBER = str(NETWORK_MACHINE_NUMBER)
    width= WINDOW_SIZE[0]
    height = WINDOW_SIZE[1]
    fullLine = 18
    font_SHELL_type = "data/fonts/Vera.ttf"
    font_SHELL_size = 15
    myFont = pygame.font.Font(font_SHELL_type, font_SHELL_size) # create font object for SHELL
    listColor = [COLOR_WHITE, COLOR_BLUE, COLOR_GREEN, COLOR_YELLOW, COLOR_ORANGE]
    changeColor = 0
    showCur = 0
    colorCur = listColor.pop(listColor.index(random.choice(listColor)))
    content = []
    contentDisplay = []
    listCommand = []
    indexListCommand = 0
    contentLineCurrent = ''
    contentLineCurrentDisplay = '|'
    posCursor = 0
    currentLine = True
    root = ACCESS_LEVEL+'@'+NETWORK_MACHINE_NUMBER+':~% '
    camTop = 0
    camBot = 0
    line = 0
    mac_uname, mac_root, starting_position, files_tree, macs_tree = tree.init() # extracting basics from shell: uname, root, starting position, trees...
    current_position = starting_position

    def displayText(text, at, x, y, color, bg=None):
        if not ACCESS_LEVEL+'@'+NETWORK_MACHINE_NUMBER+':~% ' in text:
            label = myFont.render(text, at, COLOR_WHITE, bg)
            surface.blit(label, (x, y))    
        else:
            labelUser = myFont.render(ACCESS_LEVEL+'@'+NETWORK_MACHINE_NUMBER, at, (COLOR_ORANGE), bg)
            labelColon = myFont.render(':', at, (COLOR_WHITE), bg)
            labelNS = myFont.render('%', at, (COLOR_WHITE), bg)
            labelTilde = myFont.render('~', at, (COLOR_BLUE), bg)
            surface.blit(labelUser, (0, y))
            surface.blit(labelColon, (105, y))
            surface.blit(labelTilde, (113, y))
            surface.blit(labelNS, (125, y))
            text = text.replace(ACCESS_LEVEL+'@'+NETWORK_MACHINE_NUMBER+':~%', '')
            labelText = myFont.render(text, at, color, bg)
            surface.blit(labelText, (135, y))
  
    def readChar():
        if event.key == pygame.K_BACKSPACE:
            return 'backspace'
        elif event.key == pygame.K_PAGEUP:
            return 'pageup'
        elif event.key == pygame.K_PAGEDOWN:
            return 'pagedown'
        elif event.key == pygame.K_TAB:
            return 'tab'
        elif event.key == pygame.K_RETURN:
            return 'enter'
        elif event.key == pygame.K_ESCAPE:
            return 'esc'
        elif event.key in (pygame.K_RSHIFT, pygame.K_LSHIFT):
            return 'shift'
        elif event.key in (pygame.K_RCTRL, pygame.K_LCTRL):
            return 'control'
        elif event.key == pygame.K_RIGHT:
            return 'kright'
        elif event.key == pygame.K_LEFT:
            return 'kleft'
        elif event.key == pygame.K_UP:
            return 'kup'
        elif event.key == pygame.K_DOWN:
            return 'kdown'
        elif event.key == pygame.K_CAPSLOCK:
            return None
        elif event.key == 283:
            return 'begincur'
        elif event.key == 284:
            return 'endcur'
        elif event.key == 285:
            return 'delall'
        else:
            return event.unicode

    def progressCommand(cmd, current_position):
        cmd = cmd.strip()
        if cmd == '':
            return []
        elif cmd == 'clear': # clear
            return []
        elif cmd == 'help': # help
            current_help = helpCommand()
            return current_position, current_help, True
        elif cmd == 'exit': # exit
            menu.main() # return to login menu
        elif cmd == 'pwd': # pwd
            current_path = shell.getPWD(current_position)
            return current_position, current_path, False
        elif cmd == 'ls' or cmd == 'dir': # ls/dir
            current_tree = shell.getList(mac_root, current_position, files_tree)
            return current_position, current_tree, False
        elif cmd == 'id': # id
            user_id = shell.getId(ACCESS_LEVEL)
            return current_position, user_id, False
        elif cmd == 'whois': # whois
            whois = shell.getId(ACCESS_LEVEL)
            return current_position, whois, False
        elif cmd == 'hostname': # hostname
            hostname = shell.getHostName(NETWORK_MACHINE_NUMBER)
            return current_position, hostname, False
        elif cmd == 'uname': # uname
            uname = shell.getUname(mac_uname)
            return current_position, uname, False
        elif cmd == "cd ..": # cd_up
            current_path = shell.getCdUP(mac_root, current_position)
            current_position = current_path
            return current_position, current_path, False           
        elif cmd.startswith('cd '):
            direc = cmd[3:]
            direc = direc.strip()
            current_path = shell.changePWD(mac_root, current_position, files_tree, direc)
            current_position = current_path
            return current_position, current_path, False
        elif cmd.startswith('cat '):
            file_target = cmd[3:]
            file_target = file_target.strip()
            file_text = shell.getCAT(CURRENT_LANGUAGE, CURRENT_LEVEL, current_position, files_tree, file_target)
            return current_position, file_text, False
        elif cmd.startswith('install '):
            file_target = cmd[7:]
            file_target = file_target.strip()
            file_text = shell.installProgram(current_position, files_tree, file_target)
            return current_position, file_text, False
        elif cmd.startswith('connect '):
            file_target = cmd[7:]
            file_target = file_target.strip()
            file_text = shell.connectMac(current_position, macs_tree, file_target, surface, WINDOW_SIZE, CURRENT_LANGUAGE)
            return current_position, file_text, False
        elif cmd.startswith('disconnect'):
            menu.main() # return to login menu
        else:
            return current_position, 'y-shell: command not found: "'+ str(cmd)+'"', False

    def helpCommand():
        lstHelp = []
        m = open("data/levels/help.txt", "r")
        shell_help = m.readlines()
        m.close
        lstHelp.append("SHELL: "+str(shell.VERSION))
        lstHelp.append(" ")
        for text in shell_help:
            if CURRENT_LANGUAGE == "0": # English
                if text.startswith("ENGLISH"):        
                    lstHelp.append(str(text.split(":")[1].replace("\n","")))
            else: # Spanish
                if text.startswith("SPANISH"):
                    lstHelp.append(str(text.split(":")[1].replace("\n","")))
        lstHelp.append(" ")
        return lstHelp

    # starting main() loop
    while 1:
        fullLine = (height - 120) // 20
        if currentLine:
            if camBot - camTop == (fullLine - 1):
                camBot = len(contentDisplay)
                camTop = camBot - (fullLine - 1)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                newChar = readChar()
                if newChar not in ('delall', 'begincur', 'endcur', 'backspace', 'tab', 'enter', 'esc', 'pageup', 'pagedown',\
                    'shift', 'control', None, 'kright', 'kleft', 'kup', 'kdown'):
                    try:
                        contentLineCurrent = list(contentLineCurrent)
                        contentLineCurrent.insert(posCursor, newChar)
                        contentLineCurrent = ''.join(contentLineCurrent)
                        posCursor += 1
                        lstChar = list(contentLineCurrent)
                        lstChar.insert(posCursor, '|')
                        contentLineCurrentDisplay = ''.join(lstChar)
                    except:
                        posCursor = 0
                        if camBot - camTop == (fullLine - 1):
                            camTop += 1
                        camBot += 1
                        content.append([root])
                        contentLineCurrent = ''
                        contentLineCurrentDisplay = '|'    
                    indexListCommand = 0
                    showCur = 0   
                    currentLine = True
                elif newChar == 'delall':
                    contentLineCurrent = ''
                    posCursor = 0
                    contentLineCurrentDisplay = '|'
                    currentLine = True
                elif newChar == 'begincur':
                    posCursor = 0
                    contentLineCurrentDisplay = '|' + contentLineCurrent
                    currentLine = True
                elif newChar == 'endcur':
                    posCursor = len(contentLineCurrent)
                    contentLineCurrentDisplay = contentLineCurrent + '|'
                    currentLine = True
                elif newChar == 'pageup':    
                    if not len(listCommand) == 0:
                        if -len(listCommand) != indexListCommand:
                            indexListCommand -= 1
                            contentLineCurrent = listCommand[indexListCommand]
                            contentLineCurrentDisplay = contentLineCurrent + '|'
                            posCursor = len(contentLineCurrent)
                    currentLine = True
                    showCur = 0
                elif newChar == 'pagedown':
                    if not len(listCommand) == 0:
                        if indexListCommand < -1:
                            indexListCommand += 1
                            contentLineCurrent = listCommand[indexListCommand]
                            contentLineCurrentDisplay = contentLineCurrent + '|'
                            posCursor = len(contentLineCurrent)
                    currentLine = True
                    showCur = 0
                elif newChar == 'kup':
                    if camTop != 0:
                        if camBot - camTop == (fullLine - 1):
                            camBot -= 1
                            camTop -= 1
                            currentLine = False
                    showCur = 0
                elif newChar == 'kdown':
                    if camBot < len(contentDisplay):
                        camBot += 1
                        camTop += 1
                    showCur = 0
                elif newChar == 'kright':
                    if not len(contentLineCurrent) == posCursor:
                        posCursor += 1
                        lstChar = list(contentLineCurrent)
                        lstChar.insert(posCursor, '|')
                        contentLineCurrentDisplay = ''.join(lstChar)
                    currentLine = True
                    showCur = 0
                elif newChar == 'kleft':
                    if posCursor != 0:
                        posCursor -= 1
                        lstChar = list(contentLineCurrent)
                        lstChar.insert(posCursor, '|')
                        contentLineCurrentDisplay = ''.join(lstChar)
                    currentLine = True
                    showCur = 0
                elif newChar == 'backspace':
                    if len(contentLineCurrent) != 0 and posCursor != 0:
                        try:
                            contentLineCurrent = list(contentLineCurrent)
                            wordPoped = contentLineCurrent.pop(posCursor - 1)
                            contentLineCurrent = ''.join(contentLineCurrent)
                            posCursor -= 1
                        except:
                            contentLineCurrent = contentLineCurrent[1:]
                            posCursor = len(contentLineCurrent)
                        lstChar = list(contentLineCurrent)
                        lstChar.insert(posCursor, '|')
                        contentLineCurrentDisplay = ''.join(lstChar)
                        currentLine = True
                    showCur = 0
                elif newChar == 'enter':
                    currentLine = True
                    indexListCommand = 0
                    if camBot - camTop == (fullLine - 1):
                        camTop += 1
                    camBot += 1
                    content.append([root + contentLineCurrent])
                    if contentLineCurrent.strip() == 'clear':
                        camTop = 0
                        camBot = 0
                        posCursor = 0
                        content = []
                        contentLineCurrent = ''
                        contentLineCurrentDisplay = '|'
                    else:
                        current_position, contentAppend, help_mode = progressCommand(contentLineCurrent, current_position)
                        if help_mode == False:
                            content.append(contentAppend)
                        else:
                            for eachLine in contentAppend:
                                if camBot - camTop == (fullLine - 1):
                                    camTop += 1
                                camBot += 1
                                content.append(eachLine)
                            help_mode = False
                    if len(contentLineCurrent.strip(' ')) != 0:
                        listCommand.append(contentLineCurrent)
                    posCursor = 0
                    contentLineCurrent = ''
                    contentLineCurrentDisplay = '|'
                    showCur = 0
        surface.fill(COLOR_BLACK)
        changeColor += 1
        showCur += 1
        contentDisplay = []
        for i in range(len(content)):
            text = ''.join(content[i])
            if len(text) * 8 > width:
                while len(text) * 8 > width:
                    textMini = text[:width // 8 - 1]
                    contentDisplay.append(textMini)
                    text = text[width // 8 - 1:]
                contentDisplay.append(text)
            else:
                contentDisplay.append(text)
        if currentLine:
            if len(contentDisplay) >= fullLine:
                camBot = len(contentDisplay)
                camTop = camBot - (fullLine - 1)
            else:
                camBot = len(contentDisplay)
                camTop = 0
        for i in range(camTop, camBot):
            displayText(contentDisplay[i], 1, 0, line * 20, COLOR_WHITE)
            line += 1
        if camBot == len(contentDisplay):
            if showCur < 500:
                displayText(root + contentLineCurrentDisplay, 1, 0, line * 20, COLOR_WHITE)
            else:
                displayText(root + contentLineCurrent, 1, 0, line * 20, COLOR_WHITE)
            if showCur > 1000:
                showCur = 0
        else:
            displayText(''.join(contentDisplay[camBot]), 1, 0, line * 20, COLOR_WHITE)
        line = 0
        pygame.display.flip()
