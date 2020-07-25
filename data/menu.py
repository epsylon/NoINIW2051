#!/usr/bin/env python3 
# -*- coding: utf-8 -*-"
"""
NoINIW 2051 - by psy (epsylon@riseup.net)
"""
import os, sys, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
import pygameMenu

from data.levels.level0.level0 import login as level0

FPS=60.0

VERSION = "V:0.1(beta)_25072020"
CAPTION = "cYpher.PunK! { //Shell_Based//m-RPG// }: [ NoINIW_2051 ]"
TITLE = "[NoINIW-2051]"

WINDOW_SIZE = (1024, 768)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GRAY = (50, 50, 50)
COLOR_GREEN = (0, 160, 0)
COLOR_BLUE = (0, 0, 228)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (242, 91, 37)
logo_path = "data/images/logo.png"
icon_path = "data/images/icon.png"
play_path = "data/images/play.png"
options_path = "data/images/options.png"
exit_path = "data/images/exit.png"
cheats_path = "data/images/cheats.png"
howto_path = "data/images/howto.png"
forum_path= "data/images/forum.png"
update_path= "data/images/update.png"
author_path = "data/images/author.png"
music_path = "data/sounds/menu.ogg"
menu_cfg = "data/menu.cfg"
####### start of: translations section ########
translations_menu = "data/translations/menu.txt"
tutorial_EN_path = "data/translations/tutorial_EN.txt"
tutorial_ES_path = "data/translations/tutorial_ES.txt"
updates_EN_path = "data/translations/updates_EN.txt"
updates_ES_path = "data/translations/updates_ES.txt"
forum_EN_path = "data/translations/forum_EN.txt"
forum_ES_path = "data/translations/forum_ES.txt"
credits_EN_path = "data/translations/credits_EN.txt"
credits_ES_path = "data/translations/credits_ES.txt"
translations_cheats_path = "data/translations/cheats.txt"
####### end of: translations section ########
pygame.init() # pygame lib init
pygame.font.init()
font_type = "data/fonts/Vera.ttf"
font_type_bold = "data/fonts/VeraBold.ttf"
font_type_logo = "data/fonts/DejaVuSerif-BoldItalic.ttf"
font_size = 18
font_REA_size = 15
font_version_size = 16
font_counter_size = 52
fontObj = pygame.font.Font(font_type, font_size) # create font object for menu
fontObjBold = pygame.font.Font(font_type_bold, font_size) # create font bold object for menu
fontVerObj = pygame.font.Font(font_type, font_version_size) # create font object for version
fontCounterObj = pygame.font.Font(font_type_bold, font_counter_size) # create font object for counter
fontREAObj = pygame.font.Font(font_type, font_REA_size) # create font object for REA
sound = pygameMenu.sound.Sound() # load game menu sounds
sound.load_example_sounds() # load menu sounds
music = pygame.mixer.music.load(music_path) # load game menu music
logo = pygame.image.load(logo_path) # load game logo image
icon = pygame.image.load(icon_path) # load game icon image
surface = pygame.display.set_icon(icon) # set icon on window
surface = pygame.display.set_mode(WINDOW_SIZE) # set display mode

def load_menu_translations(set_language):
    if set_language == "0": # English
        language_translation = "ENGLISH"
    else: # Spanish
        language_translation = "SPANISH"
    f = open(translations_menu, "r")
    translations = f.readlines()
    f.close()
    for lost in translations:
        lost = lost.replace("\n", "")
        if language_translation in str(lost):
            if "MENU_GAME_HOWTO" in lost:
                MENU_GAME_TUTORIAL = str(lost.split(":")[1])
            elif "MENU_GAME_START" in lost:
                MENU_GAME_PLAY = str(lost.split(":")[1])
            elif "MENU_GAME_SETTINGS" in lost:
                MENU_GAME_OPTIONS = str(lost.split(":")[1])
            elif "MENU_GAME_UPGRADE" in lost:
                MENU_GAME_UPDATE = str(lost.split(":")[1])
            elif "MENU_GAME_PUBLIC" in lost:
                MENU_GAME_FORUM = str(lost.split(":")[1])
            elif "MENU_GAME_AUTHOR" in lost:
                MENU_GAME_AUTHOR = str(lost.split(":")[1])
            elif "MENU_GAME_CHEATS" in lost:
                MENU_GAME_CHEATS = str(lost.split(":")[1])
            elif "MENU_GAME_END" in lost:
                MENU_GAME_EXIT = str(lost.split(":")[1])
            elif "MENU_GAME_LANG" in lost:
                MENU_GAME_LANG = str(lost.split(":")[1])
            elif "MENU_GAME_L-EN" in lost:
                MENU_GAME_LANG_EN = str(lost.split(":")[1])
            elif "MENU_GAME_L-ES" in lost:
                MENU_GAME_LANG_ES = str(lost.split(":")[1])
            elif "MENU_GAME_FULLSCREEN" in lost:
                MENU_GAME_FULLSCREEN = str(lost.split(":")[1])
            elif "MENU_GAME_MUSIC" in lost:
                MENU_GAME_MUSIC = str(lost.split(":")[1])
            elif "MENU_GAME_RETURN_SETTINGS" in lost:
                MENU_GAME_RETURN_SETTINGS = str(lost.split(":")[1])
    return MENU_GAME_TUTORIAL, MENU_GAME_PLAY, MENU_GAME_OPTIONS, MENU_GAME_UPDATE, MENU_GAME_FORUM, MENU_GAME_AUTHOR, MENU_GAME_CHEATS, MENU_GAME_EXIT, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS

def load_stored_settings():
    f = open(menu_cfg, "r")
    stored_config = f.readlines()
    f.close()
    for conf in stored_config:
        if "LANGUAGE" in conf: # language
            set_language = conf.replace("\n","").split(":")[1]
        elif "FULLSCREEN" in conf: # screen size
            set_fullscreen = conf.replace("\n","").split(":")[1]
            if set_fullscreen == "0": # window mode
                surface = pygame.display.set_mode(WINDOW_SIZE)
            else: # fullscreen
                surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else: # music
            set_music = conf.replace("\n","").split(":")[1]
            if set_music == "0": # music disabled
                music = pygame.mixer.music.stop()
            else: # music enabled
                music = pygame.mixer.music.play(-1)
    return set_language, set_fullscreen, set_music

def button(img, coords, surface):
    image = pygame.image.load(img)
    imagerect = image.get_rect()
    imagerect.topright = coords
    surface.blit(image, imagerect)
    return (image, imagerect)

def main_background():
    surface.fill(COLOR_BLACK) # main menu background color
    MENU_GAME_TUTORIAL, MENU_GAME_PLAY, MENU_GAME_OPTIONS, MENU_GAME_UPDATE, MENU_GAME_FORUM, MENU_GAME_AUTHOR, MENU_GAME_CHEATS, MENU_GAME_EXIT, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS = load_menu_translations(set_language)
    pygame.draw.rect(surface,COLOR_WHITE,(0,260,WINDOW_SIZE[0],475))
    surface.blit(logo, (WINDOW_SIZE[0]/4+25, WINDOW_SIZE[1]/2-85)) # load logo
    text_surface = fontVerObj.render(VERSION, True, COLOR_WHITE) # load version text with antialiasing
    surface.blit(text_surface, dest=(WINDOW_SIZE[0]/2-500, WINDOW_SIZE[1]/2+360)) # set version number
    pygame.draw.rect(surface,COLOR_WHITE,(0,70,WINDOW_SIZE[0],160))
    howto_rect = pygame.draw.rect(surface,COLOR_WHITE,(160,85,180,60))
    button_howto = button(howto_path,(WINDOW_SIZE[0]/10+120, WINDOW_SIZE[1]/3-170), surface)
    howto_surface = fontObjBold.render(str(MENU_GAME_TUTORIAL), True, COLOR_BLACK)
    surface.blit(howto_surface, dest=(WINDOW_SIZE[0]/10+125, WINDOW_SIZE[1]/3-150))
    play_rect = pygame.draw.rect(surface,COLOR_WHITE,(160,155,180,60))
    button_play = button(play_path,(WINDOW_SIZE[0]/10+120, WINDOW_SIZE[1]/3-100), surface)
    play_surface = fontObjBold.render(str(MENU_GAME_PLAY)+"!", True, COLOR_BLACK)
    surface.blit(play_surface, dest=(WINDOW_SIZE[0]/10+125, WINDOW_SIZE[1]/3-80))
    options_rect = pygame.draw.rect(surface,COLOR_WHITE,(340,85,180,60))
    button_options = button(options_path,(WINDOW_SIZE[0]/10+300, WINDOW_SIZE[1]/3-170), surface)
    options_surface = fontObjBold.render(str(MENU_GAME_OPTIONS), True, COLOR_BLACK)
    surface.blit(options_surface, dest=(WINDOW_SIZE[0]/10+305, WINDOW_SIZE[1]/3-150))
    update_rect = pygame.draw.rect(surface,COLOR_WHITE,(340,155,180,60))
    button_update = button(update_path,(WINDOW_SIZE[0]/10+300, WINDOW_SIZE[1]/3-100), surface)
    update_surface = fontObjBold.render(str(MENU_GAME_UPDATE), True, COLOR_BLACK)
    surface.blit(update_surface, dest=(WINDOW_SIZE[0]/10+305, WINDOW_SIZE[1]/3-80))
    forum_rect = pygame.draw.rect(surface,COLOR_WHITE,(520,85,180,60))
    button_forum = button(forum_path,(WINDOW_SIZE[0]/10+480, WINDOW_SIZE[1]/3-170), surface)
    forum_surface = fontObjBold.render(str(MENU_GAME_FORUM), True, COLOR_BLACK)
    surface.blit(forum_surface, dest=(WINDOW_SIZE[0]/10+485, WINDOW_SIZE[1]/3-150))
    author_rect = pygame.draw.rect(surface,COLOR_WHITE,(520,155,180,60))
    button_author = button(author_path,(WINDOW_SIZE[0]/10+480, WINDOW_SIZE[1]/3-100), surface)
    author_surface = fontObjBold.render(str(MENU_GAME_AUTHOR), True, COLOR_BLACK)
    surface.blit(author_surface, dest=(WINDOW_SIZE[0]/10+485, WINDOW_SIZE[1]/3-80))
    cheats_rect = pygame.draw.rect(surface,COLOR_WHITE,(700,85,200,60))
    button_cheats = button(cheats_path,(760, WINDOW_SIZE[1]/3-170), surface)
    cheats_surface = fontObjBold.render(str(MENU_GAME_CHEATS)+"!", True, COLOR_BLACK)
    surface.blit(cheats_surface, dest=(765, WINDOW_SIZE[1]/3-150))
    exit_rect = pygame.draw.rect(surface,COLOR_WHITE,(700,155,200,60))
    button_exit = button(exit_path,(760, WINDOW_SIZE[1]/3-100), surface)
    exit_surface = fontObjBold.render(str(MENU_GAME_EXIT), True, COLOR_BLACK)
    surface.blit(exit_surface, dest=(765, WINDOW_SIZE[1]/3-80))
    check_menu_events(howto_rect, play_rect, options_rect, update_rect, forum_rect, author_rect, cheats_rect, exit_rect, MENU_GAME_OPTIONS, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS)

def settings_background():
    pygame.draw.rect(surface,COLOR_WHITE,(0,0,0,0))

def display_text_animation(rect, string, l):
    text = ''
    for i in range(len(string)):
        text += string[i]
        text_surface = fontREAObj.render(text, True, COLOR_ORANGE)
        text_rect = rect
        text_rect.center = (WINDOW_SIZE[0]/2+10, WINDOW_SIZE[0]/2-10+l)
        surface.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)

def show_tutorial():
    tutorial_menu = pygameMenu.Menu(surface, # main menu menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=16,
                    font_size_title=28,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=40,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=40,
                    window_width=WINDOW_SIZE[0]
                    )
    topA = "data/images/topA.png"
    topB = "data/images/topB.png"
    top_menu_A = pygame.image.load(topA) # load game top front A
    top_menu_B = pygame.image.load(topB) # load game top front B (exit)
    surface.blit(top_menu_A, (WINDOW_SIZE[0]-1025, WINDOW_SIZE[1]-770)) # load top main image
    surface.blit(top_menu_B, (WINDOW_SIZE[0]-25, WINDOW_SIZE[1]-769)) # load top exit image
    tutorial_rect = pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[0]/9+95,WINDOW_SIZE[1]/2-100,600,400)) # tutorial back box
    if set_language == "0": # English
        f = open(tutorial_EN_path, "r")
    else: # Spanish
        f = open(tutorial_ES_path, "r")
    tutorial = f.readlines()
    f.close()
    l = 0
    for line in tutorial:
        l = l+20 # used to create spaces between lines
        line = line.replace("\n", "")
        display_text_animation(tutorial_rect, line, l)
        for event in pygame.event.get():
            if event.type == 5: # "5" = click DOWN event
                main() # whatever click goes to main menu
    create_counter(10) # create visual ETA counter for return to main menu

def update_menu():
    update_m = pygameMenu.Menu(surface, # main menu menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=16,
                    font_size_title=28,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=40,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=40,
                    window_width=WINDOW_SIZE[0]
                    )
    topA = "data/images/topA.png"
    topB = "data/images/topB.png"
    top_menu_A = pygame.image.load(topA) # load game top front A
    top_menu_B = pygame.image.load(topB) # load game top front B (exit)
    surface.blit(top_menu_A, (WINDOW_SIZE[0]-1025, WINDOW_SIZE[1]-770)) # load top main image
    surface.blit(top_menu_B, (WINDOW_SIZE[0]-25, WINDOW_SIZE[1]-769)) # load top exit image
    update_rect = pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[0]/9+95,WINDOW_SIZE[1]/2-100,600,400)) # update back box
    if set_language == "0": # English
        f = open(updates_EN_path, "r")
    else: # Spanish
        f = open(updates_ES_path, "r")
    updates = f.readlines()
    f.close()
    l = 0
    for line in updates:
        l = l+35 # used to create spaces between lines
        line = line.replace("\n", "")
        display_text_animation(update_rect, line, l)
        for event in pygame.event.get():
            if event.type == 5: # "5" = click DOWN event
                main() # whatever click goes to main menu
    l = 150
    r = 9
    create_counter(10) # create visual ETA counter for return to main menu

def forum_menu():
    forum_m = pygameMenu.Menu(surface, # main menu menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=16,
                    font_size_title=28,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=40,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=40,
                    window_width=WINDOW_SIZE[0]
                    )
    topA = "data/images/topA.png"
    topB = "data/images/topB.png"
    top_menu_A = pygame.image.load(topA) # load game top front A
    top_menu_B = pygame.image.load(topB) # load game top front B (exit)
    surface.blit(top_menu_A, (WINDOW_SIZE[0]-1025, WINDOW_SIZE[1]-770)) # load top main image
    surface.blit(top_menu_B, (WINDOW_SIZE[0]-25, WINDOW_SIZE[1]-769)) # load top exit image
    forum_rect = pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[0]/9+95,WINDOW_SIZE[1]/2-100,600,400)) # update back box
    if set_language == "0": # English
        f = open(forum_EN_path, "r")
    else: # Spanish
        f = open(forum_ES_path, "r")
    forums = f.readlines()
    f.close()
    l = 0
    for line in forums:
        l = l+35 # used to create spaces between lines
        line = line.replace("\n", "")
        display_text_animation(forum_rect, line, l)
        for event in pygame.event.get():
            if event.type == 5: # "5" = click DOWN event
                main() # whatever click goes to main menu
    create_counter(10) # create visual ETA counter for return to main menu

def author_menu():
    credits_m = pygameMenu.Menu(surface, # main menu menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=16,
                    font_size_title=28,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=40,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=40,
                    window_width=WINDOW_SIZE[0]
                    )
    topA = "data/images/topA.png"
    topB = "data/images/topB.png"
    top_menu_A = pygame.image.load(topA) # load game top front A
    top_menu_B = pygame.image.load(topB) # load game top front B (exit)
    surface.blit(top_menu_A, (WINDOW_SIZE[0]-1025, WINDOW_SIZE[1]-770)) # load top main image
    surface.blit(top_menu_B, (WINDOW_SIZE[0]-25, WINDOW_SIZE[1]-769)) # load top exit image
    author_rect = pygame.draw.rect(surface,COLOR_BLACK,(WINDOW_SIZE[0]/9+95,WINDOW_SIZE[1]/2-100,600,400)) # update back box
    if set_language == "0": # English
        f = open(credits_EN_path, "r")
    else: # Spanish
        f = open(credits_ES_path, "r")
    credits = f.readlines()
    f.close()
    l = 0
    for line in credits:
        l = l+35 # used to create spaces between lines
        line = line.replace("\n", "")
        display_text_animation(author_rect, line, l)
        for event in pygame.event.get():
            if event.type == 5: # "5" = click DOWN event
                main() # whatever click goes to main menu
    create_counter(10) # create visual ETA counter for return to main menu

def cheats_menu():
    cheats_m = pygameMenu.Menu(surface, # cheats menu menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=16,
                    font_size_title=28,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=40,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=40,
                    window_width=WINDOW_SIZE[0]
                    )
    topA = "data/images/topA.png"
    topB = "data/images/topB.png"
    top_menu_A = pygame.image.load(topA) # load game top front A
    top_menu_B = pygame.image.load(topB) # load game top front B (exit)
    surface.blit(top_menu_A, (WINDOW_SIZE[0]-1025, WINDOW_SIZE[1]-770)) # load top main image
    surface.blit(top_menu_B, (WINDOW_SIZE[0]-25, WINDOW_SIZE[1]-769)) # load top exit image
    if set_language == "0": # English
        language_translation = "ENGLISH"
    else: # Spanish
        language_translation = "SPANISH"
    f = open(translations_cheats_path, "r")
    translations_cheats = f.readlines()
    f.close()
    for lost in translations_cheats:
        lost = lost.replace("\n", "")
        if language_translation in str(lost):
            if "MENU_CHEATS_ENTER" in lost:
                MENU_CHEATS_ENTER = str(lost.split(":")[1])
            elif "MENU_CHEATS_TRY" in lost:
                MENU_CHEATS_TRY = str(lost.split(":")[1])
    cheats_menu = pygameMenu.Menu(surface, # cheats menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=14,
                    font_size_title=35,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=220,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=main,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=220,
                    window_width=WINDOW_SIZE[0]
                    )
    cheats_menu.add_text_input("* "+str(MENU_CHEATS_ENTER)+": ",
                        default='',
                        maxchar=16,
                        textinput_id='cheat_code',
                        input_underline='')
    def try_cheat(): # add some code cheats: free shell upgrade, etc. (leaked during videogame unboxing!)
        #data = cheats_menu.get_input_data()
        main() # (btm) returning to main menu
    cheats_menu.add_option("-> "+str(MENU_CHEATS_TRY)+" <-", try_cheat)
    while True:
        cheats_menu.mainloop()

def create_counter(counter):
    l = 150
    r = counter
    for i in range(0,counter): # create counter for reset
        text = str(r)
        text_surface = fontCounterObj.render(text, True, COLOR_BLACK)
        text_rect = pygame.draw.rect(surface,COLOR_WHITE,(WINDOW_SIZE[0]/2-480,WINDOW_SIZE[1]/2-170,100,100)) # counter back box
        text_rect.center = (WINDOW_SIZE[0]/2-420, WINDOW_SIZE[0]/2-250)
        surface.blit(text_surface, text_rect)
        r = r - 1
        time.sleep(1)
        pygame.display.flip()
        if r < 0:
            main()

def check_menu_events(howto_rect, play_rect, options_rect, update_rect, forum_rect, author_rect, cheats_rect, exit_rect, MENU_GAME_OPTIONS, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS):
    for event in pygame.event.get():
        if event.type == 5: # "5" = click DOWN event
            mouse = pygame.mouse.get_pos()
            m1 = mouse[0]
            m2 = mouse[1]
            mouse_rect = pygame.draw.rect(surface,COLOR_ORANGE,(m1,m2,1,1)) # locate cursor position!
            howto_event_zone = pygame.Rect.colliderect(howto_rect, mouse_rect) # tutorial
            play_event_zone = pygame.Rect.colliderect(play_rect, mouse_rect) # play
            options_event_zone = pygame.Rect.colliderect(options_rect, mouse_rect) # options
            update_event_zone = pygame.Rect.colliderect(update_rect, mouse_rect) # update
            forum_event_zone = pygame.Rect.colliderect(forum_rect, mouse_rect) # forum
            author_event_zone = pygame.Rect.colliderect(author_rect, mouse_rect) # credits
            cheats_event_zone = pygame.Rect.colliderect(cheats_rect, mouse_rect) # cheats
            exit_event_zone = pygame.Rect.colliderect(exit_rect, mouse_rect) # exit
            if howto_event_zone == 1:
                show_tutorial()
            elif play_event_zone == 1:
                start_game()
            elif options_event_zone == 1:
                config_menu(MENU_GAME_OPTIONS, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS)
            elif update_event_zone == 1:
                update_menu()
            elif forum_event_zone == 1:
                forum_menu()
            elif author_event_zone == 1:
                author_menu()
            elif cheats_event_zone == 1:
                cheats_menu()
            elif exit_event_zone == 1:
                sys.exit()

def config_menu(MENU_GAME_OPTIONS, MENU_GAME_LANG, MENU_GAME_LANG_EN, MENU_GAME_LANG_ES, MENU_GAME_FULLSCREEN, MENU_GAME_MUSIC, MENU_GAME_RETURN_SETTINGS):
    global settings_menu
    settings_menu = pygameMenu.Menu(surface, # settings menu
                    bgfun=settings_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type_bold,
                    font_color=COLOR_WHITE,
                    font_size=14,
                    font_size_title=35,
                    menu_alpha=100,
                    menu_color=COLOR_BLACK,
                    menu_height=220,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=main,
                    option_shadow=False,
                    title="",
                    menu_color_title=COLOR_ORANGE,
                    widget_alignment=pygameMenu.locals.ALIGN_LEFT,
                    window_height=220,
                    window_width=WINDOW_SIZE[0]
                    )
    settings_menu.add_selector(MENU_GAME_LANG+":",
                    [(MENU_GAME_LANG_EN, 'EN'),
                    (MENU_GAME_LANG_ES, 'ES')],
                    selector_id='language',
                    default=int(set_language))
    settings_menu.add_selector(MENU_GAME_FULLSCREEN+":",
                    [('OFF', 'OFF'),
                    ('ON', 'ON')],
                    selector_id='fullscreen',
                    default=int(set_fullscreen))
    settings_menu.add_selector(MENU_GAME_MUSIC+":",
                    [('OFF', 'OFF'),
                    ('ON', 'ON')],
                    selector_id='music',
                    default=int(set_music))
    settings_menu.add_option(MENU_GAME_RETURN_SETTINGS, check_form_settings, align=pygameMenu.locals.ALIGN_CENTER)
    while True:
        settings_menu.mainloop()

def check_form_settings():
    data = settings_menu.get_input_data()
    for k in data.keys():
        if k == "language": # set language
            set_language = data[k][1]
        elif k == "fullscreen":  # set fullscreen
            set_fullscreen = data[k][1]
        else: # set music
            set_music =  data[k][1]
    save_stored_settings(set_language, set_fullscreen, set_music) # store settings to menu.cfg
    main() # return back to main menu

def save_stored_settings(set_language, set_fullscreen, set_music):
    f = open(menu_cfg, "r")
    menu_config = f.readlines()
    f.close()
    menuc = open(menu_cfg, "w")
    for conf in menu_config:
        if "LANGUAGE" in conf: # language
            menuc.write("LANGUAGE:"+str(set_language)+os.linesep)
        elif "FULLSCREEN" in conf: # screen size
            menuc.write("FULLSCREEN:"+str(set_fullscreen)+os.linesep)
        else: # music
            menuc.write("MUSIC:"+str(set_music))
    menuc.close()

def main(test=False):
    global set_fullscreen
    global set_language
    global set_music
    global main_menu
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    set_language, set_fullscreen, set_music = load_stored_settings()
    main_menu = pygameMenu.Menu(surface, # main menu
                    bgfun=main_background,
                    color_selected=COLOR_YELLOW,
                    font=font_type,
                    font_color=COLOR_BLACK,
                    font_size=14,
                    font_size_title=35,
                    menu_alpha=100,
                    menu_color=COLOR_GRAY,
                    menu_height=1,
                    menu_width=int(WINDOW_SIZE[0]),
                    onclose=pygameMenu.events.EXIT,
                    option_shadow=False,
                    title=TITLE+":",
                    menu_color_title=COLOR_ORANGE,
                    window_height=1,
                    window_width=WINDOW_SIZE[0]
                    )
    main_menu.set_sound(sound, recursive=True) # set menu sounds
    while True:
        clock.tick(FPS)
        main_menu.mainloop(disable_loop=test)
        pygame.display.flip()
        if test == True:
            break

def start_game():
    level0(surface, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GRAY, COLOR_YELLOW, COLOR_ORANGE, WINDOW_SIZE, set_language)

def level0_login_background():
    None

if __name__ == '__main__':
    main()
