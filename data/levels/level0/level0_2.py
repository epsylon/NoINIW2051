#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
NOINIW 2051 - by psy (epsylon@riseup.net)
"""
import time
import pygame
import pygameMenu
import data.menu

import os
import random

NETWORK_DOMAIN = "X/UNd.NeT" # name for level [0-10] layer network

COLOR_RED = (255 ,0 , 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (50, 50, 50)
COLOR_GREEN = (0, 160, 0)
COLOR_BLUE = (0, 0, 228)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (242, 91, 37)

pygame.font.init()
font_type = "data/fonts/Vera.ttf"
font_type_bold = "data/fonts/VeraBold.ttf"
font_size = 18
font_banner_size = 16
fontObj = pygame.font.Font(font_type, font_size) # create font object for menu
fontBANNERObj = pygame.font.Font(font_type, font_banner_size) # create font BANNER object
profile_username_path = "data/profile/username.txt"

PROFILE_PATH = "data/profile"
DEFAULT_USER_NAME = "ANONYMOUS"

translations_level0_intro = "data/translations/level0.txt"

def load_level0_translations(set_language):
    if set_language == "0": # English
        language_translation = "ENGLISH"
    else: # Spanish
        language_translation = "SPANISH"
    f = open(translations_level0_intro, "r")
    translations = f.readlines()
    f.close()
    for lost in translations:
        lost = lost.replace("\n", "")
        if language_translation in str(lost):
            if "SERVICE" in lost:
                TRANS_SERVICE = str(lost.split(":")[1])
            if "USERNAME" in lost:
                TRANS_USERNAME = str(lost.split(":")[1])
            if "PASSWORD" in lost:
                TRANS_PASSWORD = str(lost.split(":")[1])
            if "TRY" in lost:
                TRANS_ACCESS = str(lost.split(":")[1])
            if "LOGINGUESTGRANTED" in lost:
                GUEST_ACCESS_GRANTED =  str(lost.split(":")[1])
            if "LOGINDENIED" in lost:
                DENIED_ACCESS = str(lost.split(":")[1])
    return TRANS_SERVICE, TRANS_USERNAME, TRANS_PASSWORD, TRANS_ACCESS, GUEST_ACCESS_GRANTED, DENIED_ACCESS

def extract_username():
    if os.path.exists(profile_username_path) == True:
        f = open(profile_username_path, "r")
        USERNAME = str(f.read().replace("\n",""))
        f.close()
    else: # create default profile
        if not os.path.exists(PROFILE_PATH): # create new profile folder
            os.mkdir(PROFILE_PATH)
        f = open(profile_username_path, "w")
        f.write(DEFAULT_USER_NAME) # default username
        f.close()
        USERNAME = DEFAULT_USER_NAME
    return USERNAME

def extract_web_banner_text():
   WEB_BANNER_TEXT = "PUBLIC [WEBSITE] for [OPEN-PROXY] MAC: ["+str(NETWORK_MACHINE_NUMBER)+"]" # default web banner for OPEN-PROXY
   return WEB_BANNER_TEXT

def extract_ssh_banner_text():
   SSH_BANNER_TEXT = "SSH-ProxyVPN-32.1 (by ChaOsCL4n) for [OPEN-PROXY] MAC: ["+str(NETWORK_MACHINE_NUMBER)+"]" # default SSH banner for OPEN-PROXY
   return SSH_BANNER_TEXT

def update_menu_service(value, enabled):
    banner_rect = pygame.draw.rect(login_surface,COLOR_BLACK,(WINDOW[0]/10-105,WINDOW[1]/5+120,WINDOW[0]+100,WINDOW[1])) # machine BANNER back box
    if enabled == "WEB":
        WEB_BANNER_TEXT = extract_web_banner_text()
        banner_surface = fontBANNERObj.render(WEB_BANNER_TEXT, True, COLOR_BLUE)
        banner_rect.center = (WINDOW[0]-500, WINDOW[1]-200)
        login_surface.blit(banner_surface, banner_rect)
        if login_menu.get_widget("user_name") and login_menu.get_widget("user_password"):
            login(login_surface, WINDOW, LANGUAGE, NETWORK_MACHINE_NUMBER)
    elif enabled == "SSH":
        SSH_BANNER_TEXT = extract_ssh_banner_text()
        banner_surface = fontBANNERObj.render(SSH_BANNER_TEXT, True, COLOR_BLUE)
        banner_rect.center = (WINDOW[0]-500, WINDOW[1]-200)
        login_surface.blit(banner_surface, banner_rect)
        if not login_menu.get_widget("user_name") and not login_menu.get_widget("user_password"):
            TRANS_SERVICE, TRANS_USERNAME, TRANS_PASSWORD, TRANS_ACCESS, GUEST_ACCESS_GRANTED, DENIED_ACCESS = load_level0_translations(LANGUAGE)
            USERNAME = extract_username()
            login_menu.add_text_input("* "+str(TRANS_USERNAME)+": ",
                        default='',
                        maxchar=12,
                        textinput_id='user_name',
                        input_underline='')
            login_menu.add_text_input("* "+str(TRANS_PASSWORD)+": ",
                        default='',
                        maxchar=12,
                        password=True,
                        textinput_id='user_password',
                        input_underline='')
            def try_login(): # level 0-2 (under development)
                data = login_menu.get_input_data()
                #if str(data['user_name']) == str(NETWORK_MACHINE_NUMBER): # guest access
                #    msg = str(GUEST_ACCESS_GRANTED) # -guest(whatever-pass) granted- on this level
                #    ACCESS_LEVEL = "guest"
                #else: # rest is denied
                msg = str(DENIED_ACCESS)
                ACCESS_LEVEL = False
                show_login_msg(msg, login_surface, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, WINDOW, LANGUAGE, ACCESS_LEVEL, NETWORK_MACHINE_NUMBER)
            login_menu.add_option("-> "+str(TRANS_ACCESS)+" <-", try_login)

def show_login_msg(msg, surface, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, WINDOW_SIZE, set_language, ACCESS_LEVEL, NETWORK_MACHINE_NUMBER):
    #if ACCESS_LEVEL == "guest": # granted!
    #    login_return_text = fontObj.render('[ '+str(msg)+'! ]', True, COLOR_GREEN) # create login GREEN back msg
    #else: # denied!
    login_return_text = fontObj.render('[ '+str(msg)+'! ]', True, COLOR_RED) # create login RED back msg
    login_surface.blit(login_return_text, dest=(WINDOW_SIZE[0]/2-100, WINDOW_SIZE[1]/4+42)) # load msg into surface
    while True:
        pygame.display.flip()
        if ACCESS_LEVEL == "guest": # GO FOR NEXT LEVEL: 0-2
            time.sleep(3) # wait for shell
        else: # back to 'login' menu
            time.sleep(5) # wait until re-login
            pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[1]/10-75,WINDOW_SIZE[1]/2-154,WINDOW_SIZE[0],30)) # used to hide login returned msg
            login(surface, WINDOW_SIZE, set_language, NETWORK_MACHINE_NUMBER)

def login(surface, WINDOW_SIZE, set_language, current_machine):
    global login_menu
    global login_surface
    global WINDOW
    global LANGUAGE
    global NETWORK_MACHINE_NUMBER
    NETWORK_MACHINE_NUMBER = current_machine
    WINDOW = WINDOW_SIZE
    LANGUAGE = set_language
    login_surface = surface
    pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[1]/10-75,WINDOW_SIZE[1]/2-165,WINDOW_SIZE[0],150)) # used to hide login returned msg
    TRANS_SERVICE, TRANS_USERNAME, TRANS_PASSWORD, TRANS_ACCESS, GUEST_ACCESS_GRANTED, DENIED_ACCESS = load_level0_translations(set_language)
    USERNAME = extract_username()
    if not NETWORK_MACHINE_NUMBER:
        NETWORK_MACHINE_NUMBER = random.randrange(1111, 9999) # generate random proxy number (between proxy reserved directions)
    login_menu = pygameMenu.Menu(surface, # level 0: "login" menu
                    bgfun=data.menu.level0_login_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type,
                    font_color=COLOR_WHITE,
                    font_size=18,
                    font_size_title=35,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=220,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=data.menu.main, # back to main menu
                    option_shadow=False,
                    title="["+str(NETWORK_DOMAIN)+"]>[MAC:"+str(NETWORK_MACHINE_NUMBER)+"]>",
                    menu_color_title=COLOR_GREEN,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=220,
                    window_width=int(WINDOW_SIZE[0])
                    )
    login_menu.add_selector('* '+str(TRANS_SERVICE),
                    [('SSH', 'SSH'),
                    ('WEB', 'WEB')],
                    selector_id='service',
                    onchange=update_menu_service,
                    default=1)
    if login_menu.get_widget("user_name"):
        login_menu.get_widget("user_name").clear()
    if login_menu.get_widget("user_password"):
        login_menu.get_widget("user_password").clear()
    while True:
        login_menu.mainloop()
