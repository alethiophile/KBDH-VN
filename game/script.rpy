# This is a proof-of-concept K:BDH VN.

init:
    image white = "#ffffff"
    image yukibackground = "#ccccff"
    python: # TODO: figure out a way to quickly switch on/off the window show/hide statements below.
        basechar = Character(None, kind=nvl)
        kyon = Character("Kyon", kind=basechar, color="#777755")
        sister = Character("Nonoko", kind=basechar, color="#999977")
        yuki = Character("Nagato Yuki", kind=basechar, color="#aaaaff")
        narrator = Character(None, kind=basechar)
        menu = nvl_menu
        style.nvl_window.background = "nvl_window.png"
        style.nvl_window.xpadding = 55
        style.nvl_window.ypadding = 55
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve

label start:
    scene white with fade

    window show
    "The day started normally enough, but that was true of most days."
    "Put a phone ringing sound effect here."
    sister "Kyon-kun, phone!"
    kyon "Answer it for me. I'm busy."
    sister "Okaaay..."
    sister "Kyon-kun's phone! He's too lazy to answer!"
    $ renpy.pause(0.5)
    sister "Oh? Okay! I'll tell him. Feel better!"
    sister "Kyon-kun! Yuki-nee-san says she's sick and really wants you to visit her!"
    nvl clear
    window hide
    scene yukibackground with dissolve
    window show
    "At one point I calculated that the ride to Nagato's apartment was twenty minutes."
    "I'm not sure whether or not I beat my best time."
    kyon "Nagato! It's me!"
    "Some sort of sound effect or scene change or something."
    nvl clear
    kyon "Nagato. What's wrong?"
    yuki "The Integrated Data Sentience Entity has determined that I have become a liability."
    kyon "What...do you mean?"
    yuki "Factors within my makeup have become too unpredictable. It has been calculated that I will commit another error."
    yuki "To prevent this, deletion has been scheduled in three hours, twenty one minutes, fifteen seconds; I will be replaced with an interface more suited to defending against possible Sky Canopy Domain interference."
    nvl clear
    kyon "...There isn't enough milk in the world."
    kyon "How set is this?"
    yuki "It is absolute."
    kyon "Okay. I'll just..."
    nvl clear
    kyon "Can I use your phone, Nagato? I need to call Haruhi and the others."
    yuki "It is not necessary."
    kyon "What do you mean?"
    yuki "I requested your presence for...personal reasons. It was not a request for help."
    kyon "I don't care! I've always relied on you—now that you need help, I am {i}not{/i} going to just stand by and watch you get taken away from—from us!"
    yuki "...I see."
    kyon "So, I need to make some phone calls."
    yuki "Understood."
