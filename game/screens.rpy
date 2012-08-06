# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu

##############################################################################
# Chapters screen 
#
# Screen that's used to display the list of chapters

screen Chapters:
    # This ensures that any other menu screen is replaced.
    tag menu

    use main_menu

    frame:
        style_group "chm"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        #background None

        has vbox
        vbox:
            side "l c":
                area (0.0, 5, 450, 0.7)
                
                viewport:
                    yadjustment adj
                    mousewheel True
                    
                    vbox:
                        for arc in chapters:
                            frame:
                                has vbox
                                for name, label, buttonp in arc:
                                    if buttonp:
                                            button:
                                                action Start(label)
                                                ypadding 5
                                                xfill True
                                                size_group "chb"
                                            
                                                hbox:
                                                    xalign 0.5
                                                    text name style "button_text" size 18 line_leading -2 text_align 0.5 #min_width 420
                                    else:
                                        hbox:
                                            xalign 0.5
                                            text name style "button_text" size 18 text_align 0.5 color "#000"

                bar adjustment adj style "vscrollbar" 
                
        null height 5

        textbutton "Dismiss.":
            #size_group "chb"
            xmargin 9
            xminimum 465
            action ShowMenu("main_menu")
            
        null height 5


##############################################################################
# Extras menu
#
# Screen that's used to display the Extras menu

screen Extras:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    if xtras_origin == 'mm':
        use main_menu
    else:
        use navigation
    
    # The main menu buttons."
    frame:
        style_group "em"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        #background None

        has vbox
        # vbox:
            # side "l c":
                # area (0.0, 0.0, 450, 0.7)
        
        textbutton _("Achievements") action ShowMenu("Achievscr")
        textbutton _("Tropes Collection") action ShowMenu("Tropes")
        textbutton _("Skynet Database") action ShowMenu("Database")
        textbutton _("Skynet Mediaplayer") #action ShowMenu("Musicbox")
        textbutton _("Skynet Wallpapers") #action ShowMenu("BG_gallery")
        textbutton _("Skynet Avatars") #action ShowMenu("Sprites_gallery")
        null height 5
        if xtras_origin == 'mm':
            textbutton _("Dismiss") action ShowMenu("main_menu")
        
init -2 python:

    # Make all the main menu buttons be the same size.
    style.em_button.size_group = "em"


##############################################################################
# Skynet Database menu
#
# Screen that's used to display the Skynet Database Extras

screen Database:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    if xtras_origin == 'mm':
        use main_menu
    else:
        use navigation
    
    # The main menu buttons."
    frame:
        style_group "em"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        #background None

        has vbox
        # vbox:
            # side "l c":
                # area (0.0, 0.0, 450, 0.7)
        
        textbutton _("Kyon's Time-travel list") action Show("TTNscr", ttnmode = 'order')
        for e in Xtras_DB_Dossiers:
            textbutton _("Dossier / [e[0]]") #action ShowMenu("[e[1]]")
        null height 5
        if xtras_origin == 'mm':
            textbutton _("Dismiss") action ShowMenu("main_menu")
        
        
init -2 python:

    # Make all the main menu buttons be the same size.
    style.em_button.size_group = "em"


##########################################################################
# TTN screen
#
# Used to show time-travel notes

screen TTNscr:
    
    $ l = len(persistent.ttnotes)
    $ t = persistent.ttnotes[:]
    if ttnmode == 'dates':
        $ t.sort(None, ttndestkey)
        
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # use main_menu
    
    if xtras_origin == 'mm':
        window:
            style "mm_root"
    else:
        window:
            style "gm_root"
    
    frame:
        style_group "tm"
        # style "gm_nav_button"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        #background None

        # frame:
        has vbox
        frame:
            xminimum 630
            text "Kyon's helpful time-travelling notes\nhe used to keep track on his Yet. [l]" style "button_text" size 20 line_leading 2 text_align 0.5 color "#fff"
        vbox:
            side "l c":
                area (0.0, 0.0, 620, 0.7)
                frame:
                    left_margin 5
                    xpadding 10
                    ypadding 10
                    
                    viewport:
                        yadjustment adjttn
                        mousewheel True
                        
                        vbox:
                            $ e = {}
                            for e in t:
                                if e['pending']:
                                    $ ttncol = "#005"
                                else:
                                    $ ttncol = "#222"
                                hbox:
                                    # xalign 0.5
                                    $ ttndest = tupledest2date(e['dest'])
                                    vbox:
                                        area (0.0, 0.0, 150, 0.1)
                                        text ttndest style "button_text" size 18 text_align 0.0 color ttncol
                                    text '   ' style "button_text" size 18 text_align 0.0
                                    text e['descr'] style "button_text" size 18 text_align 0.0 color ttncol

                bar adjustment adjttn style "vscrollbar" 
                
        null height 5
        
        hbox:
            if ttnmode == 'order':
                textbutton "Sort by destination." xmargin 5 xminimum 260 action Show("TTNscr", ttnmode = 'dates')
            else:
                textbutton "Show as added." xmargin 5 xminimum 260 action Show("TTNscr", ttnmode = 'order')
            textbutton "Back.":
                #size_group "chb"
                xmargin 5
                xminimum 375
                action ShowMenu("Extras")
            
        null height 5



##########################################################################
# Tropes screen
#
# Used to show collected tropes

screen Tropes:
    # This ensures that any other menu screen is replaced.
    tag menu
    
    if xtras_origin == 'mm':
        use main_menu
    else:
        use navigation
    
    frame:
        style_group "tm"
        # style "gm_nav_button"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        #background None

        # frame:
        has vbox
        hbox:
            fixed:
                xmaximum 430
                ymaximum 50
                xcenter 0.55
                text "{b}Welcome to the Spot-The-Tropes'\ncaught trope collection.{/b}" style "button_text" size 19 color "#fff" #outlines [(1, "#000", 0, 0)]
            textbutton "?" action ShowMenu("SpotTheTrope_help")
            
        $ Ncaught = len(persistent.collected_tropes)
        text "{b}You caught [Ncaught] / [max_tropes] tropes. \nYou currently have [persistent.balance] Þ.{/b}" style "button_text" size 18 color "#fff" #outlines [(1, "#000", 0, 0)]
            
        vbox:
            side "l c":
                area (0.0, 0.0, 450, 0.7)
                frame:
                    left_margin 5
                    xpadding 10
                    ypadding 10
                    
                    viewport:
                        yadjustment adjTC
                        mousewheel True
                        
                        vbox:
                            for t in persistent.collected_tropes.keys():
                                hbox:
                                    xalign 0.5
                                    text t style "button_text" size 18 text_align 0.5 color "#000"

                bar adjustment adjTC style "vscrollbar" 
                
        null height 5

        textbutton "Back.":
            #size_group "chb"
            xmargin 5
            xminimum 465
            action ShowMenu("Extras")
            
        null height 5


##############################################################################
# SpotTheTrope help
#
# Screen that's used to display the help message for Spot-The-Trope 'game'

screen SpotTheTrope_help:
    
    # use main_menu
    
    if xtras_origin == 'mm':
        window:
            style "mm_root"
    else:
        window:
            style "gm_root"
    
    tag menu
    
    modal True

    frame:
        style_group "yesno_prompt"
        xfill True
        xmargin 100
        ycenter .5

        frame:
            # background Frame('#6496c8', 1, 1)
            xpadding 25
            ypadding 25
            vbox:
                xfill True
                spacing 25

                text "Describe the Spot-The-Trope here.\nEach trope caught will net you 1 (one) Þ, which you can spend on unlocking the features in Extras menu.":
                    text_align 0.5
                    xalign 0.5

                hbox:
                    spacing 100
                    xalign .5
                    textbutton "Dismiss":
                        action ShowMenu("Tropes")


##############################################################################
# Achievement screen
#
# Shows the Achievements what user unlocked and what user has yet to unlock.

screen Achievscr:
    # This ensures that any other menu screen is replaced.
    tag menu

    if xtras_origin == 'mm':
        use main_menu
    else:
        use navigation

    frame:
        style_group "chm"
        xanchor 0.0
        yanchor 0.0
        xpos 0.1
        ypos 0.1
        xpadding 10
        ypadding 10
        #background None

        has vbox
        
        text '{b}Achievements{/b}' style "button_text" text_align 0.5 color "#fff" #outlines [(1, "#000", 0, 0)]
        $ i_l1 = len(persistent.unlockedAchievs)
        $ i_l2 = len(achievements)
        text '{b}earned [i_l1] / [i_l2]{/b}' style "button_text" size 18 line_leading -2 text_align 0.5 color "#fff" #outlines [(1, "#000", 0, 0)]
        
        vbox:
            side "l c":
                area (0.0, 0.0, 450, 0.7)
                frame:
                    left_margin 5
                    xpadding 10
                    ypadding 10
                    
                    viewport:
                        yadjustment adjAch
                        mousewheel True
                        
                        vbox:
                            xfill True
                            for i_i in range(0, len(achievements)):
                                if i_i in persistent.unlockedAchievs:
                                    text achievements[i_i][0] style "button_text" size 20 line_leading 2 xalign 0.0 color "#000" 
                                    text achievements[i_i][1] style "button_text" size 16 line_leading -2 xalign 0.0 color "#000" first_indent 20
                                else:
                                    text achievements[i_i][0] style "button_text" size 20 line_leading 2 xalign 0.0
                                    text '???' style "button_text" size 16 line_leading -2 xalign 0.0 first_indent 20
                            
                bar adjustment adjAch style "vscrollbar"
                
        null height 5

        textbutton "Back.":
            #size_group "chb"
            xmargin 5
            xminimum 470
            action ShowMenu("Extras")
            
        null height 5

       
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    python:
        if persistent.set_text_styling == None:
            renpy.set_style_preference("text", "Vanilla")
            persistent.text_styling = "Vanilla"
            persistent.set_text_styling = True    

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons."
    frame:
        style_group "mm"
        xalign .98
        # yalign .98
        yalign .03

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Newest Volume") action Start('Vol02_start')
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Chapters") action ShowMenu("Chapters")
        textbutton _("Extras") action [SetVariable('xtras_origin', 'mm'), Show("Extras", xtras_origin = 'mm')] #ShowMenu("Extras")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Extras") action [SetVariable('xtras_origin', 'gm'), Show("Extras", xtras_origin = 'gm')] 
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    # Format the description, and add it as text.
                    $ description = "% 2s. %s\n%s" % (
                        FileSlotName(i, columns * rows),
                        FileTime(i, empty=_("Empty Slot.")),
                        FileSaveName(i))

                    text description

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox
                
                label _("Text Styling")#: [persistent.text_styling]")
                textbutton _("Vanilla") action [SetField(persistent, "text_styling", "Vanilla"), StylePreference("text", "Vanilla")]
                textbutton _("Extra") action [SetField(persistent, "text_styling", "Extra"), StylePreference("text", "Extra")]

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

            frame:
                style_group "pref"
                has vbox
                
                label _("Preview autoadvance")#: [persistent.text_styling]")
                textbutton _("On") action SetField(persistent, "preview_adv", True)
                textbutton _("Off") action SetField(persistent, "preview_adv", False)

            # frame:
                # style_group "pref"
                # has vbox
                
                # label _("Eyecatch style")#: [persistent.text_styling]")
                # textbutton _("Moves In-Out") action SetField(persistent, "eyecatch_styling", "Moves")
                # textbutton _("Dissolves") action SetField(persistent, "eyecatch_styling", "Dissolves")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"
    

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0
    
    

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    style.quick_button_text.outlines = [(1, "#000a", 1, 1)]
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    
