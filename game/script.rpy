# This is a proof-of-concept K:BDH VN.

init:
    image bg classroom = "classroom.jpg"
    image bg hallway = "hallway.png"
    image bg stairwell = "stairwell.jpg"
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    image title = "titlecard1.jpg"
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
    scene title 
    with Dissolve(5.0)
    
    pause 5
    
    window show
    
    nvl clear
    scene bg classroom with fade
    "Class had started innocently enough that day, but he'd long ago given up on expecting that to mean anything."
    "With each passing moment after lunch, he grew more and more anxious, stealing glances behind him to make certain that she was still there—{w=.4}still safe."
    "And every time their eyes met, she smirked knowingly and quickly looked outside, trying to pretend eye contact was never made."
    "He was absolutely certain that if his sense of anxiety weren't imagined, she was the one behind it — one way or another." 
    "When the fifth period bell rang, he was prepared."    
    nvl clear
    "In a way, he'd always wanted to do this; extract that one tiny bit of revenge upon her for all the times she'd done it to him."
    "So when she rose, turned in one smooth motion, and made to bolt out of the room—"
    
    scene bg hallway with fade
#    play sound "dashwacky.wav"
    "—he was there first, seizing the decorative ties of her sailor uniform's neckerchief and making for the door at top speed." 
    "\"Bwa!\""
    "she protested, arms waving frantically as she dashed to keep up, or risk the knot being pulled out." 
    "\"What the hell do you think you're doing!?\""
    nvl clear
    scene bg stairwell with fade
    "Naturally, he said nothing to her during the entire mad dash to the remote stairwell where she had first hauled him by his own tie, so long ago."
    "He released her at the top of the steps after looking around to ensure that no one else was nearby."
    "Her momentum carried her forward, resulting in him pressing one hand flat against her chest, just below her neck."
    "Her eyes quickly sharpened, her features fixed into a scowl."
    "\"What the hell, Kyon!?\""
    
    # scene white with fade

    # window show
    # "The day started normally enough, but that was true of most days."
    # "Put a phone ringing sound effect here."
    # sister "Kyon-kun, phone!"
    # kyon "Answer it for me. I'm busy."
    # sister "Okaaay..."
    # sister "Kyon-kun's phone! He's too lazy to answer!"
    # $ renpy.pause(0.5)
    # sister "Oh? Okay! I'll tell him. Feel better!"
    # sister "Kyon-kun! Yuki-nee-san says she's sick and really wants you to visit her!"
    # nvl clear
    # window hide
    # scene yukibackground with dissolve
    # window show
    # "At one point I calculated that the ride to Nagato's apartment was twenty minutes."
    # "I'm not sure whether or not I beat my best time."
    # kyon "Nagato! It's me!"
    # "Some sort of sound effect or scene change or something."
    # nvl clear
    # kyon "Nagato. What's wrong?"
    # yuki "The Integrated Data Sentience Entity has determined that I have become a liability."
    # kyon "What...do you mean?"
    # yuki "Factors within my makeup have become too unpredictable. It has been calculated that I will commit another error."
    # yuki "To prevent this, deletion has been scheduled in three hours, twenty one minutes, fifteen seconds; I will be replaced with an interface more suited to defending against possible Sky Canopy Domain interference."
    # nvl clear
    # kyon "...There isn't enough milk in the world."
    # kyon "How set is this?"
    # yuki "It is absolute."
    # kyon "Okay. I'll just..."
    # nvl clear
    # kyon "Can I use your phone, Nagato? I need to call Haruhi and the others."
    # yuki "It is not necessary."
    # kyon "What do you mean?"
    # yuki "I requested your presence for...personal reasons. It was not a request for help."
    # kyon "I don't care! I've always relied on you—now that you need help, I am {i}not{/i} going to just stand by and watch you get taken away from—from us!"
    # yuki "...I see."
    # kyon "So, I need to make some phone calls."
    # yuki "Understood."
