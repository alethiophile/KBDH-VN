# This is a proof-of-concept K:BDH VN.

init:    

    image bg classroom = "Backgrounds/classroom.jpg"
    image bg hallway = "Backgrounds/hallway.png"
    image bg stairwell = "Backgrounds/stairwell.jpg"
    image bg stairwellbarrier = "Backgrounds/stairwellbarrier.jpg"
    image bg roof = "Backgrounds/roof.jpg"
    image bg roofclose = "Backgrounds/roofclose.jpg"
    image bg roofsky = "Backgrounds/roofsky.jpg"
    image bg roofright = "Backgrounds/roofright.jpg"
    image bg BeamOrange1 = "Backgrounds/BeamOrange1.jpg"
    image bg BeamOrange2 = "Backgrounds/BeamOrange2.jpg"
    image bg BeamOrange3 = "Backgrounds/BeamOrange3.jpg"
    image bg BeamOrange4 = "Backgrounds/BeamOrange4.jpg"
    image bg KyonRoomLeftClosed = "Backgrounds/KyonRoomLeftClosed.png"
    image bg KyonHouseNight = "Backgrounds/KyonHouseNight.png"
    image bg TownStreetNight1 = "Backgrounds/TownStreetNight1.png"
    image bg TownStreetNight2 = "Backgrounds/TownStreetNight2.png"
    image bg YukiApartment = "Backgrounds/YukiApartment.jpg"
    image bg YukiRoomLeft = "Backgrounds/YukiRoomLeft.png"
    image bg YukiRoomRight = "Backgrounds/YukiRoomLeft.png"
    image bg YukiRoomCenter = "Backgrounds/YukiRoomCenter.jpg"
    
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    image title0 = "Backgrounds/title0.png"
    image Barrier = "Backgrounds/barrier2.jpg"
    image Bluesword = "Backgrounds/bluesword1.png"
    image field = "Sprites/Effects/InterdictionField.png"
    image BarrierSmall = "Sprites/Effects/BarrierSmall.png"
    image BarrierSmall Bright = im.MatrixColor("Sprites/Effects/BarrierSmall.png",
                                       im.matrix.brightness(.5))
    image Knife1 = "Sprites/Effects/Knife1.png"
    image Knife2 = "Sprites/Effects/Knife2.png"
    image Knife3 = "Sprites/Effects/Knife3.png"
    image Spike1 = "Sprites/Effects/NetSpike1.png"
    image Spike2 = "Sprites/Effects/NetSpike2.png"
    image Spike3 = "Sprites/Effects/NetSpike3.png"
    image Spike4 = "Sprites/Effects/NetSpike4.png"
    image Spike5 = "Sprites/Effects/NetSpike5.png"
    image knifethrow = "Sprites/Effects/knifethrowlong.png"
    #Haruhi Sprites
    image Haruhi Sup1 = "Sprites/Haruhi/HaruhiSideSurprised1.png"
    image Haruhi Ang1 = "Sprites/Haruhi/HaruhiSideAngry1.png"
    image Haruhi Ang2 = "Sprites/Haruhi/HaruhiSideAngry2.png"
    image Haruhi Ang3 = "Sprites/Haruhi/HaruhiSideAngry3.png"
    image Haruhi Hap1 = "Sprites/Haruhi/HaruhiSideHappy1.png"
    image Haruhi Hap2 = "Sprites/Haruhi/HaruhiSideHappy2.png"
    image Haruhi Hap3 = "Sprites/Haruhi/HaruhiSideHappy3.png"
    image Haruhi Hap4 = "Sprites/Haruhi/HaruhiSideHappy4.png"
    image Haruhi Pout1 = "Sprites/Haruhi/HaruhiSidePout1.png"
    image Haruhi Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Eyeroll1 = "Sprites/Haruhi/HaruhiSideEyeroll1.png"
    image Haruhi Quest1 = "Sprites/Haruhi/HaruhiSideQuestion1.png"
    image Haruhi Grin1 = "Sprites/Haruhi/HaruhiSideGrin1.png"
    image Haruhi Worry1 = "Sprites/Haruhi/HaruhiSideWorry1.png"
    image Haruhi Smile1 = "Sprites/Haruhi/HaruhiSideSmile1.png"
    image Haruhi Smile2 = "Sprites/Haruhi/HaruhiSideSmile2.png"
    image Haruhi Smile3 = "Sprites/Haruhi/HaruhiSideSmile3.png"
    image Haruhi Sigh1 = "Sprites/Haruhi/HaruhiSideSigh1.png"
    
    image Haruhi Casual Sup1 = "Sprites/Haruhi/HaruhiSideCasualSurprised1.png"
    image Haruhi Casual Ang1 = "Sprites/Haruhi/HaruhiSideCasualAngry1.png"
    image Haruhi Casual Ang2 = "Sprites/Haruhi/HaruhiSideCasualAngry2.png"
    image Haruhi Casual Ang3 = "Sprites/Haruhi/HaruhiSideCasualAngry3.png"
    image Haruhi Casual Hap1 = "Sprites/Haruhi/HaruhiSideCasualHappy1.png"
    image Haruhi Casual Hap2 = "Sprites/Haruhi/HaruhiSideCasualHappy2.png"
    image Haruhi Casual Hap3 = "Sprites/Haruhi/HaruhiSideCasualHappy3.png"
    image Haruhi Casual Hap4 = "Sprites/Haruhi/HaruhiSideCasualHappy4.png"
    image Haruhi Casual Pout1 = "Sprites/Haruhi/HaruhiSideCasualPout1.png"
    image Haruhi Casual Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiSideCasualPout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Casual Eyeroll1 = "Sprites/Haruhi/HaruhiSideCasualEyeroll1.png"
    image Haruhi Casual Quest1 = "Sprites/Haruhi/HaruhiSideCasualQuestion1.png"
    image Haruhi Casual Grin1 = "Sprites/Haruhi/HaruhiSideCasualGrin1.png"
    image Haruhi Casual Worry1 = "Sprites/Haruhi/HaruhiSideCasualWorry1.png"
    image Haruhi Casual Smile1 = "Sprites/Haruhi/HaruhiSideCasualSmile1.png"
    image Haruhi Casual Smile2 = "Sprites/Haruhi/HaruhiSideCasualSmile2.png"
    image Haruhi Casual Smile3 = "Sprites/Haruhi/HaruhiSideCasualSmile3.png"
    image Haruhi Casual Sigh1 = "Sprites/Haruhi/HaruhiSideCasualSigh1.png"
    
    image Haruhi Crossed Sup1 = "Sprites/Haruhi/HaruhiCrossedSurprised1.png"
    image Haruhi Crossed Ang1 = "Sprites/Haruhi/HaruhiCrossedAngry1.png"
    image Haruhi Crossed Ang2 = "Sprites/Haruhi/HaruhiCrossedAngry2.png"
    image Haruhi Crossed Ang3 = "Sprites/Haruhi/HaruhiCrossedAngry3.png"
    image Haruhi Crossed Hap1 = "Sprites/Haruhi/HaruhiCrossedHappy1.png"
    image Haruhi Crossed Hap2 = "Sprites/Haruhi/HaruhiCrossedHappy2.png"
    image Haruhi Crossed Hap3 = "Sprites/Haruhi/HaruhiCrossedHappy3.png"
    image Haruhi Crossed Hap4 = "Sprites/Haruhi/HaruhiCrossedHappy4.png"
    image Haruhi Crossed Pout1 = "Sprites/Haruhi/HaruhiCrossedPout1.png"
    image Haruhi Crossed Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiCrossedPout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Crossed Eyeroll1 = "Sprites/Haruhi/HaruhiCrossedEyeroll1.png"
    image Haruhi Crossed Quest1 = "Sprites/Haruhi/HaruhiCrossedQuestion1.png"
    image Haruhi Crossed Grin1 = "Sprites/Haruhi/HaruhiCrossedGrin1.png"
    image Haruhi Crossed Worry1 = "Sprites/Haruhi/HaruhiCrossedWorry1.png"
    image Haruhi Crossed Smile1 = "Sprites/Haruhi/HaruhiCrossedSmile1.png"
    image Haruhi Crossed Smile2 = "Sprites/Haruhi/HaruhiCrossedSmile2.png"
    image Haruhi Crossed Smile3 = "Sprites/Haruhi/HaruhiCrossedSmile3.png"
    image Haruhi Crossed Sigh1 = "Sprites/Haruhi/HaruhiCrossedSigh1.png"
    
    image Haruhi Crossed Casual Sup1 = "Sprites/Haruhi/HaruhiCrossedCasualSurprised1.png"
    image Haruhi Crossed Casual Ang1 = "Sprites/Haruhi/HaruhiCrossedCasualAngry1.png"
    image Haruhi Crossed Casual Ang2 = "Sprites/Haruhi/HaruhiCrossedCasualAngry2.png"
    image Haruhi Crossed Casual Ang3 = "Sprites/Haruhi/HaruhiCrossedCasualAngry3.png"
    image Haruhi Crossed Casual Hap1 = "Sprites/Haruhi/HaruhiCrossedCasualHappy1.png"
    image Haruhi Crossed Casual Hap2 = "Sprites/Haruhi/HaruhiCrossedCasualHappy2.png"
    image Haruhi Crossed Casual Hap3 = "Sprites/Haruhi/HaruhiCrossedCasualHappy3.png"
    image Haruhi Crossed Casual Hap4 = "Sprites/Haruhi/HaruhiCrossedCasualHappy4.png"
    image Haruhi Crossed Casual Pout1 = "Sprites/Haruhi/HaruhiCrossedCasualPout1.png"
    image Haruhi Crossed Casual Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiCrossedCasualPout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Crossed Casual Eyeroll1 = "Sprites/Haruhi/HaruhiCrossedCasualEyeroll1.png"
    image Haruhi Crossed Casual Quest1 = "Sprites/Haruhi/HaruhiCrossedCasualQuestion1.png"
    image Haruhi Crossed Casual Grin1 = "Sprites/Haruhi/HaruhiCrossedCasualGrin1.png"
    image Haruhi Crossed Casual Worry1 = "Sprites/Haruhi/HaruhiCrossedCasualWorry1.png"
    image Haruhi Crossed Casual Smile1 = "Sprites/Haruhi/HaruhiCrossedCasualSmile1.png"
    image Haruhi Crossed Casual Smile2 = "Sprites/Haruhi/HaruhiCrossedCasualSmile2.png"
    image Haruhi Crossed Casual Smile3 = "Sprites/Haruhi/HaruhiCrossedCasualSmile3.png"
    image Haruhi Crossed Casual Sigh1 = "Sprites/Haruhi/HaruhiCrossedCasualSigh1.png"
    
    #Kyon Sprites
    image Kyon Ser1 = "Sprites/Kyon/KyonSerious1.png"
    image Kyon Ser2 = "Sprites/Kyon/KyonSerious2.png"
    image Kyon Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Sigh1 = "Sprites/Kyon/KyonSigh1.png"
    image Kyon Sigh2 = "Sprites/Kyon/KyonSigh2.png"
    image Kyon Neutral1 = "Sprites/Kyon/KyonNeutral1.png"
    image Kyon Neutral2 = "Sprites/Kyon/KyonNeutral2.png"
    image Kyon Ang1 = "Sprites/Kyon/KyonAngry1.png"
    image Kyon Pain1 = "Sprites/Kyon/KyonPained1.png"
    image Kyon Pain2 = "Sprites/Kyon/KyonPained2.png"
    image Kyon Smile1 = "Sprites/Kyon/KyonSmile1.png"
    image Kyon Worry1 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Worry2 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Puzzle1 = "Sprites/Kyon/KyonPuzzled1.png"
    image Kyon Sup1 = "Sprites/Kyon/KyonSurprised1.png"
    image Kyon Sup2 = "Sprites/Kyon/KyonSurprised2.png"
    
    
    image Kyon Casual Ser1 = "Sprites/Kyon/KyonCasualSerious1.png"
    image Kyon Casual Ser2 = "Sprites/Kyon/KyonCasualSerious2.png"
    image Kyon Casual Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonCasualSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Casual Sigh1 = "Sprites/Kyon/KyonCasualSigh1.png"
    image Kyon Casual Sigh2 = "Sprites/Kyon/KyonCasualSigh2.png"
    image Kyon Casual Neutral1 = "Sprites/Kyon/KyonCasualNeutral1.png"
    image Kyon Casual Neutral2 = "Sprites/Kyon/KyonCasualNeutral2.png"
    image Kyon Casual Ang1 = "Sprites/Kyon/KyonCasualAngry1.png"
    image Kyon Casual Pain1 = "Sprites/Kyon/KyonCasualPained1.png"
    image Kyon Casual Pain2 = "Sprites/Kyon/KyonCasualPained2.png"
    image Kyon Casual Smile1 = "Sprites/Kyon/KyonCasualSmile1.png"
    image Kyon Casual Worry1 = "Sprites/Kyon/KyonCasualWorry1.png"
    image Kyon Casual Worry2 = "Sprites/Kyon/KyonCasualWorry2.png"
    image Kyon Casual Puzzle1 = "Sprites/Kyon/KyonCasualPuzzled1.png"
    image Kyon Casual Sup1 = "Sprites/Kyon/KyonCasualSurprised1.png"
    image Kyon Casual Sup2 = "Sprites/Kyon/KyonCasualSurprised2.png"
    
    image Ksweat = "Sprites/Kyon/KyonSweat1.png"
    image Skinsuit = "Sprites/Kyon/KyonSkinsuitTemplate.png"
    image Skinsuit Bright = im.MatrixColor("Sprites/Kyon/KyonSkinsuitTemplate.png",
                                       im.matrix.brightness(.5))
    image Coat Bright = im.MatrixColor("Sprites/Kyon/KyonCoat.png",
                                       im.matrix.brightness(.5))
    image Coat = "Sprites/Kyon/KyonCoat.png"
    
    #Asakura Sprites
    image Asakura Smile1 = "Sprites/Asakura/AsakuraSmile1.png"
    image Asakura Smile2 = "Sprites/Asakura/AsakuraSmile2.png"
    image Asakura Smile3 = "Sprites/Asakura/AsakuraSmile3.png"
    image Asakura Sup1 = "Sprites/Asakura/AsakuraSurprise1.png"
    image Asakura Frown1 = "Sprites/Asakura/AsakuraFrown1.png"
    image Asakura Frown2 = "Sprites/Asakura/AsakuraFrown2.png"
    image Asakura Frown3 = "Sprites/Asakura/AsakuraFrown3.png"
    image Asakura Unhap1 = "Sprites/Asakura/AsakuraUnhappy1.png"
    image Asakura Sigh1 = "Sprites/Asakura/AsakuraSigh1.png"
    image Asakura Pain1 = "Sprites/Asakura/AsakuraPain1.png"
    image Asakura Pain2 = "Sprites/Asakura/AsakuraPain2.png"
    image Asakura Pain2 Bright = im.MatrixColor("Sprites/Asakura/AsakuraPain2.png",
                                       im.matrix.brightness(.5))
    #Yuki Sprites
    image Yuki EyesClosed1 = "Sprites/Yuki/YukiSideEyesClosed1.png"
    image Yuki EyesClosed1 Bright = im.MatrixColor("Sprites/Yuki/YukiSideEyesClosed1.png",
                                       im.matrix.brightness(.5))
    image Yuki Side1 = "Sprites/Yuki/YukiSide1.png"
    image Yuki Side2 = "Sprites/Yuki/YukiSide2.png"
    image Yuki Talk1 = "Sprites/Yuki/YukiSideTalk1.png"
    image Yuki Talk2 = "Sprites/Yuki/YukiSideTalk2.png"
    image Yuki Sad1 = "Sprites/Yuki/YukiSideSad1.png"
    image Yuki Sad2 = "Sprites/Yuki/YukiSideSad2.png"
    image Yuki Sad3 = "Sprites/Yuki/YukiSideSad3.png"
    image Yuki SadTalk1 = "Sprites/Yuki/YukiSideSadTalk1.png"
    image Yuki SadTalk2 = "Sprites/Yuki/YukiSideSadTalk2.png"
    image Yuki SadTalk3 = "Sprites/Yuki/YukiSideSadTalk3.png"
   
    image Yuki Casual EyesClosed1 = "Sprites/Yuki/YukiSideCasualEyesClosed1.png"
    image Yuki Casual EyesClosed1 Bright = im.MatrixColor("Sprites/Yuki/YukiSideCasualEyesClosed1.png",
                                       im.matrix.brightness(.5))
    image Yuki Casual Side1 = "Sprites/Yuki/YukiSideCasual1.png"
    image Yuki Casual Side2 = "Sprites/Yuki/YukiSideCasual2.png"
    image Yuki Casual Talk1 = "Sprites/Yuki/YukiSideTalkCasual1.png"
    image Yuki Casual Talk2 = "Sprites/Yuki/YukiSideTalkCasual2.png"
    image Yuki Casual Sad1 = "Sprites/Yuki/YukiSideCasualSad1.png"
    image Yuki Casual Sad2 = "Sprites/Yuki/YukiSideCasualSad2.png"
    image Yuki Casual Sad3 = "Sprites/Yuki/YukiSideCasualSad3.png"
    image Yuki Casual SadTalk1 = "Sprites/Yuki/YukiSideCasualSadTalk1.png"
    image Yuki Casual SadTalk2 = "Sprites/Yuki/YukiSideCasualSadTalk2.png"
    image Yuki Casual SadTalk3 = "Sprites/Yuki/YukiSideCasualSadTalk3.png"

    # Mikuru Sprites
    image Mikuru Cower Nervous1 = "Sprites/Mikuru/MikuruCowerNervous1.png"
    image Mikuru Cower Nervous2 = "Sprites/Mikuru/MikuruCowerNervous2.png"
    image Mikuru Cower Neutral1 = "Sprites/Mikuru/MikuruCowerNeutral1.png"
    image Mikuru Cower Sup1 = "Sprites/Mikuru/MikuruCowerSurprised1.png"
    image MBlush = "Sprites/Mikuru/MikuruCowerBlush.png"
    
    image Mikuru Cower Casual Nervous1 = "Sprites/Mikuru/MikuruCowerCasualNervous1.png"
    image Mikuru Cower Casual Nervous2 = "Sprites/Mikuru/MikuruCowerCasualNervous2.png"
    image Mikuru Cower Casual Neutral1 = "Sprites/Mikuru/MikuruCowerCasualNeutral1.png"
    image Mikuru Cower Casual Sup1 = "Sprites/Mikuru/MikuruCowerCasualSurprised1.png"
    image MBlush = "Sprites/Mikuru/MikuruCowerBlush.png"
    
    #Koizumi Sprites
    image Koizumi Crossed Ser1 = "Sprites/Koizumi/KoizmuiCrossedSerious1.png"
    image Koizumi Crossed Ser2 = "Sprites/Koizumi/KoizmuiCrossedSerious2.png"
    image Koizumi Crossed Smile1 = "Sprites/Koizumi/KoizmuiCrossedSmile1.png"
    image Koizumi Crossed Smile2 = "Sprites/Koizumi/KoizmuiCrossedSmile2.png"
    image Koizumi Crossed Uneasy1 = "Sprites/Koizumi/KoizmuiCrossedUneasy1.png"
    image Koizumi Crossed Uneasy2 = "Sprites/Koizumi/KoizmuiCrossedUneasy2.png"
    
    image Koizumi Crossed Casual Ser1 = "Sprites/Koizumi/KoizmuiCrossedCasualSerious1.png"
    image Koizumi Crossed Casual Ser2 = "Sprites/Koizumi/KoizmuiCrossedCasualSerious2.png"
    image Koizumi Crossed Casual Smile1 = "Sprites/Koizumi/KoizmuiCrossedCasualSmile1.png"
    image Koizumi Crossed Casual Smile2 = "Sprites/Koizumi/KoizmuiCrossedCasualSmile2.png"
    image Koizumi Crossed Casual Uneasy1 = "Sprites/Koizumi/KoizmuiCrossedCasualUneasy1.png"
    image Koizumi Crossed Casual Uneasy2 = "Sprites/Koizumi/KoizmuiCrossedCasualUneasy2.png"
    
    

    image Credits0 = "Backgrounds/credits0.png"
    image Credits1 = "Backgrounds/credits1.png"
    image Credits2 = "Backgrounds/credits2.png"
    image Credits3 = "Backgrounds/credits3.png"

    python: # TODO: figure out a way to quickly switch on/off the window show/hide statements below.
        basechar = Character(None, kind=nvl)
        kyon = Character("Kyon", kind=basechar, color="#777755")
        sister = Character("Nonoko", kind=basechar, color="#999977")
        yuki = Character("Nagato Yuki", kind=basechar, color="#aaaaff")
        narrator = Character(None, kind=basechar)
        irisoutfast = CropMove(0.2, "irisout")
        slowfadein = Fade(0.5, 0.5, 5)
        wipeleftfast = CropMove(0.3, "wipeleft")
        wiperightfast = CropMove(0.3, "wiperight")
        wipeupslow = CropMove(2, "wipeup")
        wipeupfast = CropMove(0.3, "wipeup")
        teleport = ImageDissolve("id_teleport.png", 1.0, 0)
        coatin = ImageDissolve("id_clouds.png", 1.0, 0)
        coatout = ImageDissolve("id_clouds.png", 1.0, 0, reverse=True)
        menu = nvl_menu
        style.nvl_window.background = "nvl_window.png"
        style.nvl_window.xpadding = 55
        style.nvl_window.ypadding = 55
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
        renpy.music.set_volume(0.2, .5, channel="music")
        flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
        renpy.music.register_channel("sound2", "sfx", 0)
        _preferences.set_volume("sfx", 0.5)

        config.keymap['skip'].remove('K_LCTRL')
        config.keymap['skip'].remove('K_RCTRL')
        config.keymap['skip'].append('K_LALT')
        config.keymap['skip'].append('K_RALT')

transform center_left:
    xalign 0.1 yalign 1.0
    
transform HalfRight:
    xalign 0.75 yalign 1.0
transform HalfLeft:
    xalign 0.25 yalign 1.0
    
transform KyonRightFast:
    xalign -0.5 yalign 1.0
    linear 0.15 xalign 1.5   
#    linear 0.15 xalign 1.0   

label start:
    jump prologue

label prologue:
    stop music fadeout 1
    scene title0 with slowfadein
    
    pause
    play sound "SE/Pageflip3.mp3" 

    nvl clear
    scene bg classroom with fade:
        size (800,600)
    "Class had started innocently enough that day, but he'd long ago given up on expecting that to mean anything."
    "With each passing moment after lunch, he grew more and more anxious, stealing glances behind him to make certain that she was still there—{w=.4}still safe."
    "And every time their eyes met, she smirked knowingly and quickly looked outside, trying to pretend eye contact was never made."
    "He was absolutely certain that if his sense of anxiety weren't imagined, she was the one behind it — one way or another." 
    "When the fifth period bell rang, he was prepared."    
    nvl clear
    play music "Music/Gouin.mp3" fadein 1
    $ renpy.music.set_volume(0.2, .5, channel="music")
    "In a way, he'd always wanted to do this; exact that one tiny bit of revenge upon her for all the times she'd done it to him."
    "So when she rose, turned in one smooth motion, and made to bolt out of the room—"
    nvl clear
    "—he was there first, seizing the decorative ties of her sailor uniform's neckerchief and making for the door at top speed." 
    nvl clear
    scene bg hallway with fade:
        size (800,600)
    show Haruhi Sup1 at left
    show Kyon Ser1 at center
    "\"Bwa!\" she protested, arms waving frantically as she dashed to keep up, or risk the knot being pulled out." 
    show Haruhi Ang2 at left
    "\"What the hell do you think you're doing!?\""
    show Haruhi Sup1 at left
    scene bg hallway with None:
        xanchor .5 yanchor .5
        xpos .5 ypos .5
        linear .5 rotate 360
    hide Haruhi
    hide Kyon  
    pause .5
    nvl clear
    scene bg stairwell with fade:
        size (800,600)
    "Naturally, he said nothing to her during the entire mad dash to the remote stairwell where she had first hauled him by his own tie, so long ago."
    "He released her at the top of the steps after looking around to ensure that no one else was nearby."
    "Her momentum carried her forward, resulting in him pressing one hand flat against her chest, just below her neck."
    "Her eyes quickly sharpened, her features fixed into a scowl."
    nvl clear
    show Haruhi Ang3 at center_left
    "\"What the hell, Kyon!?\""
    show Kyon Ser1 at right
    "He held up one hand and said, \"Something's up.\""
    show Haruhi Hap3 at center_left
    "Her irritation vanished instantly, replaced with wide-eyed excitement. She clapped her hands together and hopped from foot to foot."
    show Haruhi Hap4 at center_left
    "\"Yes!\" she cheered. \"It's been so boring lately!\""
    nvl clear
    "\"This better not be your fault!\""
    show Kyon Sigh1 at right
    "He shook his head in irritation, then patted his left coat pocket. Then right, then both pants pockets, then the back of each hand."
    "After that, he traced the fingertips of his right hand above his ear, eyes distant, and pulled his cell phone from one pocket."
    nvl clear
    show Haruhi Ang1 at center_left
    "\"What is it?\" she asked, when he spent a long minute studying the screen."
    show Kyon Neutral1 at right
    "\"Maybe a false alarm,\" he admitted, shifting his shoulders.{nw} "
    show Kyon Ang1 at right
    extend "\"Are you messing with me?\""   
    show Haruhi Ang2 at center_left
    "\"I should be asking you that! But whatever! You hauled me all the way out here—by my shirt, I might add!—so tongues are going to wag! If you're going to do this, then you know what I want!\""
    show Haruhi Hap1 at center_left
    nvl clear
    show Kyon Sigh2 at right
    "\"Haruhi....\""
    show Haruhi Hap2 at center_left
    "\"Do it!\" she said, bouncing on the balls of her feet in excitement. \"I want to see it!\""
    show Kyon Neutral2 at right
    "\"Is now really the time? Break's going to be over soon—\""
    show Haruhi Hap3 at center_left
    "\"Get it out now! I want to see!\""
    nvl clear
    show Kyon Sigh1 at right
    "Heaving the sigh of the eternally doomed, he put his phone away and muttered underneath his breath."
    show Haruhi Hap4 at center_left
    "\"Do that voice, too! You know the one? Like from a movie voice-over guy? I love that! Do it! Come on!\""
    show Kyon Ser1 at right
    "\"Fine,\" he grumbled.{nw}"
    show Kyon Sigh2 at right
    extend " \"But you come up with the excuse for class.\""
    nvl clear
    show Haruhi Hap4 at center_left
    "\"Student council president,\" she said without hesitation. \"Blame him.\""
    show Kyon Sigh2 at right
    "\"Ahem,\" he coughed, shooting her a dark look.{nw}"
    show Kyon Ser1 at right
    stop music fadeout 1
    extend " \"Take a step back, I don't want to catch you in the interdiction field again.\""
    show Haruhi Hap4 at center_left
    "She nodded and stepped backwards, against the wall."
    show Haruhi Hap4:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.0
    pause 0.4
    nvl clear
    play music "music/YukiAsakuraFight.mp3" fadein 1
    show Kyon Ser2 at right
    pause 1
    play sound "SE/DunDun.mp3"
    "Standing perfectly straight, hands at his sides, he closed his eyes, and began speaking in his best faux movie announcer voice-over."
    "\"Skinsuit active,\" "
    play sound "SE/Sizzle2.mp3"
    show Skinsuit at right with wipeupslow
    extend "as something that looked like nothing so much as black paint suddenly engulfed his entire body beneath his uniform."
    nvl clear
    play sound "SE/NanoRepair.mp3"
    "\"Gravimetric stabilizers and secondary gyrometrics online,\" as ridged metal studs appeared on the back of each knuckle, and beneath his uniform pants, metallic vertical rails were described in the skinsuit."
    nvl clear
    "\"Greatcoat thermoptic stealth disengaged,\" "
    play sound "SE/CloakOff.mp3"
    show Coat at right with coatin
    extend "as a knee-length tan greatcoat coalesced, covering his shoulders with a thick mantle."
    show Haruhi Hap3 at left
    "\"Doesn't that get hot?\" Her smile had only grown, her eyes shining with anticipation."
    nvl clear
    show Kyon Neutral2 at right
    "\"We had environmental conditioning added last night, since the weather's heating up,\" he said in a normal voice."
    show Kyon Ser2 at right
    "Switching back, he said, \"Primary weapons check.\""     
    nvl clear
    play sound "SE/lowswoosh.mp3"
    pause .02
    play sound "SE/lowswoosh.mp3"
    pause .02
    play sound "SE/lowswoosh.mp3"
    "He pulled a fifty centimeter long glittering metal cylinder from within the greatcoat, releasing it to spin on its axis in midair to one side, announcing, \"Long range precision and high yield weaponry is at full charge.\""
    play sound "SE/Barrier2.mp3"
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show Coat Bright at right
    show field at right with dissolve
    pause .1
    hide field at right
    show Kyon Ser2 at right
    show Skinsuit at right 
    show Coat at right
    with dissolve
    "A circle of light appeared on the floor around him, a simple white ring with glittering sparks chasing around in either direction, sending brilliant flashes to streak upwards."
    nvl clear
    "Another cylinder, wider but shorter than the last was released to float next to the first."
    "\"Mid- and short-range crowd-control weaponry is at ... ninety seven percent capacity and charging,\" he continued, squinting at the featureless gunmetal tube."
    nvl clear
    play sound "SE/clink.mp3"
    "Pulling a well-crafted sword hilt with no cross-guard or blade from one pocket, he released it horizontally, and it hung before him between the other weapons. \"Beam saber is at full capacity.\""
    show Kyon Ser1 at right
    "After pulling his cell phone from one pocket, he brushed his fingertips over his ear, revealing three dull metal studs in the skinsuit."
    "\"All systems nominal; no proximity alarms—\""
    nvl clear
    show Kyon Ang1 at right
    "He broke off suddenly, scowling. \"Okay,\" he said in his normal voice. \"My mistake. We've got incoming.\""
    show Haruhi Hap4:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign 0.1
    "\"God damn it Kyon, you're so cool when you do this,\" Haruhi gushed, clapping her hands together. \"What is it?\""
    nvl clear
    show Kyon Neutral1 at right
    "\"I'm not sure,\" he said, as a cold, familiar chuckle echoed."
    show Kyon Ser1 at right
    "One eyebrow twitched and he stowed his weapons, banishing the ring of light and flinging his phone at Haruhi."
    show Kyon Ser2 at right
    "\"Speed dial two,\" he snapped. \"Stay in the circle.\""
    show Haruhi Pout1:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.0
    pause 0.4
    play sound "SE/Barrier1.mp3"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    "She pouted, but did as she was told, the ring of light reappearing on the floor around her this time."
    nvl clear
    hide Kyon 
    hide Skinsuit
    hide Coat
    hide Haruhi
    play sound "SE/footsteps5.mp3" 
    pause 5
    show Asakura Smile2 at center with wipeup
    pause 1
    play sound "SE/DunDun.mp3"
    show Asakura Smile1 at center
    "\"Kyon-kun~!\" someone caroled up the stairwell, the echoing click of their shoes sounding as they climbed the stairs."
    show Asakura Smile2 at center
    "\"It's been a while, hasn't it?\""
    show Asakura Sup1 at center
    "The school bell chimed just as she rounded the landing, and he activated the beam saber. The blade made a crackling, whirring buzz and shed a soft, pale blue light."
    play sound "SE/saberon.mp3"
    show Bluesword with wipeupfast
    pause 1
    hide Bluesword with dissolve
    show Asakura Frown1 at center
    "\"Y...you....\" she began, before she frowned, blinking, staring at the energy weapon."
    nvl clear
    show Asakura Frown1 at left
    show Kyon Ang1 at right
    show Skinsuit at right
    show Coat at right
    "\"Long time no see,\" he said, switching stance to the long-sword style, Ni-Ten Ichi Ryu."
    show Asakura Frown2 at left
    "\"Um.... Hm. This is different. You've certainly changed, Kyon-kun.\""
    nvl clear
    show Kyon Ser2 at right
    "\"That's funny, Asakura-san, because you haven't.\""
    # stop music fadeout 1
    # scene black with fade
    # # The hardpause calls are necessary because otherwise Ren'py wants to skip over all the pause statements on a single press of the key.
    # show Credits0 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits1 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits2 with dissolve
    # pause
    # $ renpy.pause(.1, hard=True)
    # show Credits3 with dissolve
    # pause
#     
    nvl clear
    hide Asakura
    show Kyon Ser2 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Hap3 at left
    "Haruhi bounced on her heels with a wide grin, holding Kyon's cell phone in both hands as she remained in the center of the glowing circle."
    show Haruhi Hap4 at left
    "\"I knew it!\" she cheered.{nw} "
    show Haruhi Hap1 at left
    extend "\"There was something off about Asakura! What is it?\""
    nvl clear
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Haruhi
    show Asakura Unhap1 at center
    "\"Um...\" the onetime class representative said, frowning."
    hide Asakura
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    "\"She's alien,\" Kyon volunteered.{nw} "
    show Kyon Neutral2 at right
    extend "\"From the same place as Yuki-chan and Kimidori, but she tried to kill me once.\""
    show Haruhi Sup1 at left
    "\"Whaaaat? What did you do to make her mad?\" Haruhi asked, looking at him in bemusement."
    nvl clear
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Haruhi
    show Asakura Frown3 at left
    "\"Er,\" Asakura said, crossing her arms beneath her chest."
    show Asakura Frown2 at left
    "\"Evidently my information requires an update. I was sent to dispatch Kyon-kun, because he's become an undesirable element for my superiors.\""
    show Asakura Sup1 at left
    nvl clear
    "\"Really, I'd hoped to see a new state, maybe even provoke it with his death."
    show Asakura Smile2 at left
    "\"But, those toys seem to say that's already happened! So disappointing ... I suppose if I'd been more patient, I could see it anyway?\""
    show Kyon Sigh1 at right
    show Skinsuit at right
    show Coat at right
    "\"I personally like to see it as a lesson on the effects of {i}randomly stabbing people,{/i}\" Kyon muttered."
    nvl clear
    show Asakura Smile1 at left
    "\"Oh, it wasn't random,\" she countered.{nw} "
    show Asakura Smile2 at left
    extend "\"It was highly specific! I put a whole two hours of thought into it, you know. For us, that's quite a while!\""
    show Kyon Ser2 at right
    "\"I'm touched,\" he said dryly."
    nvl clear
    #show Asakura Smile1 at center
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Asakura
    show Haruhi Eyeroll1 at left
    "\"Blah blah blah,\" Haruhi muttered, crossing her arms over her chest and rolling her eyes."
    show Haruhi Ang1 at left
    "\"Skip the speeches — if I don't know the complete back story, it's all meaningless to me. I think it's about time we get down to business, right?\""
    nvl clear
    hide Haruhi
    stop music
    play music "Music/AsakuraTheme.mp3" fadein 1
    play sound "SE/horror.mp3"
    scene bg stairwellbarrier with teleport:
        size (800,600)
    show Asakura Smile2 at center
    "\"Happy to oblige!\" Asakura said brightly, as their surroundings pulsed, the window turning into a gunmetal gray steel barrier, strange patterns coalescing across the walls."
    play sound "SE/powerdown.mp3"
    "The circle on the floor around Haruhi abruptly winked out."
    nvl clear
    "\"Now, I've converted the entire space of this stairwell into-\""
    hide Asakura
    "Kyon spun on one foot, crying out with a great, \"Ki-yah!\" "
    play sound "SE/lowswoosh.mp3"
    pause (0.2)
    play sound "SE/impact.mp3"
    with vpunch
    pause (0.2)
    play sound "SE/glassbreak1.mp3"
    with hpunch
    extend "and kicking the door halfway across the roof."
    show Haruhi Sup1 at left
    pause (.01)
    show Kyon Ser1 at left behind Haruhi
    show Skinsuit at left behind Haruhi
    show Coat at left behind Haruhi
    with moveinright
    pause (0.5)
    hide Kyon
    hide Haruhi
    hide Skinsuit
    hide Coat
    with moveoutleft
    "Sparing no more time, he swept Haruhi up in one arm and dashed through the opening."
    scene bg roof with wiperight
    nvl clear
    "\"Waaah!\" she protested.{fast} \"Why are you running away!?\""
    show Haruhi Sup1 at left
    show Kyon Ser1 at right
    show Skinsuit at right
    show Coat at right
    with moveinleft
    "\"Confined spaces,\" he answered, sliding to a halt in the middle of the roof and setting her down.{fast} \"Speed dial two again.\""
    nvl clear
    show Haruhi Pout1 at left
    pause .4
    play sound "SE/Barrier1.mp3"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    "\"Right, right,\" she mumbled, reactivating the circle of light."
    show Haruhi Quest1 at left
    "\"So, what's so great about this if she can just turn it off, anyway?\""
    nvl clear
    show Kyon Ser1 at right
    play sound "SE/SaberOn.mp3"
    "\"It's a barrier and emergency help function,\" he answered, reactivating the beam saber and reassuming a defensive stance."
    show Kyon Ser2 at right
    "\"Unless she seals this space off —{w=0.5} again — {w=0.5}she can't disable it.\""
    nvl clear
    hide Kyon 
    hide Haruhi
    hide Skinsuit
    hide Coat
    scene bg roofclose
    show Asakura Sigh1 at center with wipeup
    "Asakura gave a pained sigh as she stepped through the jagged distortion between her controlled dataspace and the rooftop. "
    show Asakura Frown2 at center
    "\"You shouldn't be able to manipulate data like that,\" she said reprovingly."
    show Asakura Smile2 at center
    "\"I suppose that means it's time to stop holding back.\""
    nvl clear
    show Knife1 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.3)
    show Knife2 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.3)
    show Knife3 at center
    play sound "SE/clink.mp3"
    play sound "SE/clink.mp3"
    pause (0.8)
    play sound "SE/DunDun.mp3"
    show Asakura Smile3 at center
    "She clapped her hands together before her and drew them apart, flinging a fan of dozens of identical knives outward."
    hide Asakura
    play sound "SE/lowswoosh.mp3"
    scene black with fade
    show knifethrow with moveinleft
    scene bg roof with fade
    show Kyon Ang1 at right
    show Skinsuit at right
    show Coat at right    
    "Kyon maintained his guard position, his free hand already clenched into a fist, the metal ridges of his skinsuit facing outward."
    nvl clear
    play sound "SE/Barrier1.mp3"
    show BarrierSmall at HalfRight with dissolve
    pause 0.5
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    show BarrierSmall Bright at HalfRight
    play sound "SE/block.mp3"
    pause (0.1)
    show BarrierSmall at HalfRight
    pause (0.1)
    play sound "SE/GlassBreak3.mp3"
    hide BarrierSmall with dissolve
    "The knives adjusted their course, most homing in on him to suddenly be halted by a semi-circular barrier of glowing blue force before shattering into nothingness, but a handful stopping suddenly in the space over the circle around Haruhi."
    nvl clear
    play sound "SE/lowswoosh.mp3"
    show Asakura Smile3 at left
    show Asakura Smile3:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign 0.6
    show Kyon Pain1 at right
    pause (0.1)
    play sound "SE/slash2.mp3"
    "He opened his mouth to retort, but Asakura was already within his guard, driving yet another blade into his stomach."
    scene bg roofright
    play sound "SE/lowswoosh.mp3"
    pause (0.1)
    show Kyon Pain1 at KyonRightFast
    show Skinsuit at KyonRightFast
    show Coat at KyonRightFast
    pause (0.2)
    play sound "SE/touhoudead.wav"
    hide Kyon
    hide Skinsuit
    hide Coat
    "The inner carbon-nano-weave of the greatcoat and the force field of the skinsuit beneath it converted the stabbing force into a distributed shock wave, so instead of being pierced, Kyon was merely hit with the force of a speeding minivan, flying clear across the roof with a choked grunt."
    nvl clear
    scene bg roof
    show Asakura Smile1:
        xalign 0.6 yalign 1.0
        #xalign 0.0 yalign 1.0
        #linear 0.1 xalign 0.6 # at right
    show Asakura Smile1 at HalfRight
    "\"In the end,\" Asakura remarked, watching his form tumble off the edge of the school building,{fast} \"all those toys are pretty silly if you don't actually know how to use them.\""
    show Haruhi Hap1 at left
    "\"You have to give him credit, though,\" Haruhi said, peering very closely at the knives frozen over her barrier, not even glancing back to where Kyon had vanished."
    show Haruhi Grin1 at left
    "\"He comes up with one hell of a distraction ploy, doesn't he?\""
    nvl clear
    show Asakura Sup1 at HalfRight
    "The blue-haired interface cocked her head to one side, blinking."
    stop music fadeout 1
    "\"What?\""
    nvl clear
    hide Haruhi
    hide Asakura
    scene bg roofsky with fade
    play music "SE/lowwind.mp3" 
    "The sensation of being hit with a force that would crush a mid-sized car into a work of modern art was not entirely new, but was without a doubt extremely unpleasant."
    "His skinsuit did what it could to distribute the kinetic force evenly across his body, so the crushing pain was at least perfectly uniform in infliction."
    "The balancing gizmos gave up the ghost on keeping him upright, and struggled to guarantee he wouldn't land wherever he flew head-first."
    "His gravity manipulation defenses all strained to bleed the inertia of his impact off without even {i}more{/i} pain, but the end result was that he didn't slow appreciably until after he passed the edge of the five story rooftop."
    nvl clear
    "Not what he'd hoped for by a long shot."
    "All of the \"toys\" would keep him mobile, even if he was afraid he'd need to be {i}poured{/i} out of the skinsuit when it was over."
    "He'd have to beg Nagato or Haruhi to help him out and repair things later, but there was just too damn much to keep track of with all the attack vectors, defensive capabilities...."
    "\"It started off such a nice day, too,\" he mumbled, as his forward momentum was arrested and he began the downward plummet in earnest."
    nvl clear
    "How had it come to this, anyway...?"
    stop music fadeout 1
    nvl clear
    scene black with dissolve
    nvl clear
    play music "Music/Nichijou.mp3"
    scene bg KyonRoomLeftClosed with fade
    nvl clear
    "That day had started normally enough, but then, in his experience, that was true of nearly all days." 
    "This had caused him to become naturally suspicious of every day, to the point where he was starting to suspect a slow but sure slide into absolute paranoia."
    "Haruhi was taking her toll on him ... even if she was calming down, her behavior after that horrific (in retrospect) run-in with Sasaki was doing absolutely nothing to soothe him."
    nvl clear
    "His preferred refuge from total madness was quite simple: Drink some milk."
    "He didn't know why it had such a calming, reassuring effect on him, but it did."
    "So he poured himself a large glass in the kitchen, one ear perking up and catching the sounds of his sister playing a video game in the living room."
    nvl clear
    "Damn it, he thought. He'd even left his cell in the other room specifically to lay a claim on the system!"
    "Seriously, he thought darkly, taking a large swallow of his milk, the system was a Playstation Two — about ten years out of date now, and he had to haul it all the way upstairs if he wanted to play games in his room. "
    "He probably shouldn't even bother getting worked up about such an antiquated gaming system."
    "Even if it was the only gaming system in the house."
    "His phone rang and he sighed, rolling his eyes but staying in the kitchen."
    nvl clear
    "\"Kyon-kun,\" his sister called, pausing the game with a loud chirp, \"phone!\""
    "He lowered his glass, already able to anticipate Haruhi demanding his participation in something."
    "\"Answer it for me,\" he called back between gulps.\"I'm busy.\""
    nvl clear
    "\"Okaaaaaay,\" she said, before he heard her say,\"Kyon-kun's phone! He's too lazy to answer!\""
    "\'Thanks,\" he muttered under his breath."
    "\"Oh? Okay! I'll tell him. Feel better!\" Then her voice rose from conversational, to an unnecessary bellow, \"Kyon-kun! Yuki-nee-san says she's sick and really wants you to visit her!\""
    nvl clear
    "He didn't even bother to grab the phone on the way out."
    "\"Can I come with...\"{nw}"
    play sound "SE/doorclose.mp3"
    scene bg KyonHouseNight
    "she began, before the door slammed shut. Shrugging, she turned back to the game after flipping Kyon's phone closed."
    nvl clear
    stop music fadeout 1
    play music "Music/Nagato2.mp3"
    "He calculated the ride to Nagato's place as a twenty minute trip, at one point."
    scene bg TownStreetNight1 with wiperight
    pause 1
    scene bg TownStreetNight2 with wiperight
    pause 1
    scene bg YukiApartment with wiperight
    "When he reached the lobby, barely pausing long enough to lock up his bike, he wondered if he'd beaten his best time, but didn't feel the need to check."
    "Instead, he dashed to the console, still gasping for breath, and fumbled, mis-dialing her room number and needing to hammer the 'cancel' button to dial again."
    "\"Nagato!\" he called, the second she picked up.\"It's me!\""
    nvl clear
    "The door opened."
    scene bg YukiRoomCenter with wipeup
    "After taking the elevator to her floor, he slowed his mad pace, seeing her standing outside the doorway to her apartment, waiting for him."
    nvl clear
    show Yuki Casual Sad1 at left
    "He tried to imagine that he saw some relief around her eyes when he reached her side, but wasn't confident enough to be certain that was the case."
    show Kyon Casual Ser1 at right
    "\"Nagato,\" he said, nodding.\"What's wrong?\""
    nvl clear
    show Yuki Casual Sad2 at left
    "She gestured him inside, leading him to the table."
    "He kicked off his shoes and went to the kotatsu, watching her warily."
    "After pouring a cup of tea for each of them in silence, she finally spoke."
    nvl clear
    show Yuki Casual SadTalk1 at left
    "\"The Integrated Data Sentience Entity has determined that I have become a liability, \" she said in a soft monotone, nearly devoid of inflection."
    show Kyon Casual Sup1 at right
    nvl clear
    "He stared at her for a long minute, blinking. \"What ... do you mean?\""
    show Kyon Casual Sup2 at right
    show Yuki Casual SadTalk2 at left
    "\"Factors within my makeup have become too unpredictable. It has been calculated that I will commit another error.\""
    nvl clear
    show Yuki Casual SadTalk1 at left
    "\"To prevent this, deletion has been scheduled in three hours, twenty one minutes, fifteen seconds; I will be replaced with an interface more suited to defending against possible Sky Canopy Domain interference.\""
    nvl clear
    show Kyon Casual Sigh1 at right
    "After taking a deep breath, he growled, \"There isn't enough milk in the world.\""
    show Yuki Casual EyesClosed1 at left
    pause (0.2)
    show Yuki Casual Sad1 at left
    "She blinked several times in response."
    show Kyon Casual Worry2 at right
    "\"How set is this?\" he asked, his hands shaking too much to hold the teacup properly."
    show Yuki Casual SadTalk2 at left
    "\"It is absolute."
    nvl clear
    show Kyon Casual Sigh1 at right
    show Ksweat at right
    "He took another deep breath, then jumped to his feet, nearly upsetting the table, and began pacing back and forth in her living room."
    show Yuki Casual Sad2 at left
    "She watched him silently."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"Okay,\" he said, after a moment of thought.\"I'll just—\""
    show Kyon Casual Ser1 at right
    "He broke off, fumbling at his pocket when he realized his phone was still at home."
    show Kyon Casual Worry2 at right
    "Biting off a curse, he asked, \"Can I use your phone, Nagato? I need to call Haruhi and the others.\""
    nvl clear
    show Yuki Casual Sad3 at left
    "For a moment, mild disappointment flickered around her eyes. \"It is not necessary.\""
    show Kyon Casual Ser1 at right
    "He stared at her, then shook his head. \"What do you mean?\""
    show Yuki Casual SadTalk3 at left
    "\"I requested your presence for ... personal reasons,\" she said. \"It was not a request for help.\""
    nvl clear
    show Kyon Casual Ang1 at right
    "\"I don't care!\" he shouted."
    "\"I've always relied on you — now that you need help, I am not going to just stand by and watch you get taken away from— from us!\""
    show Yuki Casual EyesClosed1 at left
    pause (0.2)
    show Yuki Casual Sad1 at left
    "She blinked, considering, then lowered her head slightly in her infinitesimal nod."
    nvl clear
    show Yuki Casual SadTalk1 at left
    "\"I see,\" she said quietly."
    show Kyon Casual Sigh1 at right
    "\"So, I need to make some phone calls.\""
    show Yuki Casual SadTalk2 at left
    "\'Understood.\""
    stop music fadeout 1 
    nvl clear
    
    # scene bg YukiApartment with fade
    # play music "Music/Kankyou.mp3"
    # "She couldn't imagine what had possessed Kyon to call her, ranting like a lunatic about Yuki being sick. "
    # "But he'd done it from her phone, which meant for whatever reason that he and Yuki were alone together. "
    # "She wasn't certain why that bothered her, but it did — so when he demanded her presence, instead of telling him what he could do for trying to order the Brigade leader around, she swore that she'd be there."
    # nvl clear
    # "After trekking all the way there, much to her annoyance, she found that she was the last to arrive."
    # "Mikuru sat at one side of the table, opposite Yuki."
    # "Koizumi sat between them, his eternal smile faded to half its normal strength."
    # "Kyon himself stood next to her — he was the one who had answered the intercom and let her in."
    # nvl clear
    # "She narrowed her eyes at him and kicked her shoes off, storming into the room to Yuki's side and immediately pressing one palm onto the smaller girl's forehead."
    # "\"You don't feel feverish,\" she finally commented."
    # "\"But if you're sick, you shouldn't be up and about anyway.\""
    # nvl clear
    # "\"Not sick,\" Yuki answered."
    # "When Haruhi turned to Kyon and scowled at him, she corrected, \"Dying.\""
    # nvl clear
    # "Her irritation at Kyon's practical joke momentarily blew away, like settled dust being disturbed."
    # "\"Dying!?\" she yelped, turning to stare at the smaller girl."
    # "\"What of? How?\""
    # "Yuki blinked twice, then answered, \"I am not able to say.\""
    # nvl clear
    # "\"Mikuru?\""
    # "\"Um ... classified.\""
    # nvl clear
    # "She scowled at Koizumi, daring him to be a defiant annoyance, too."
    # "\"I don't know,\" he said, looking embarrassed and flustered."
    # nvl clear
    # "Turning around, she glared at Kyon, letting her irritation return and focus on him full-force."
    # "\"I am not in the mood for pranks!\" she snapped."
    # "\"This better not be a joke!\""
    # nvl clear
    # "\"I wish it was,\" he said back crossly, and she found herself taken aback at the force in his tone."
    # "She had a mental catalogue of Kyon-like behaviors, and this fell firmly into the category of the seldom-seen but always feared angry Kyon."
    # "Dour, upset, irked, sarcastic, caustic ... sure. But angry?"
    # nvl clear
    # "Hell, she'd once smashed his head into her desk — entirely on accident — and he was only annoyed."
    # "And it wasn't for hitting his head, it was for disrupting a class!"
    # "Nevermind that he had been dozing off before that."
    # nvl clear
    # "She'd seen him genuinely angry two times."
    # "Only once had it been at her."
    # "She hated that memory more than anything else she knew about him, but couldn't dare to forget it."
    # "Once it had been at — of all things — his unfinished homework over summer break, though that was the lesser of the two displays; also the first."
    # "She didn't understand it, but she knew whatever it was, she wanted to be on his side against it."
    # nvl clear
    # "Even then, some small part of her really didn't like the way that when he chose to, he simply seized command of her precious hand-crafted Brigade and, no matter how cute it was—"
    # "She firmly suplexed that thought into oblivion."
    # nvl clear
    # stop music fadeout 1
    # "\"Alright,\" she said evenly. \"Tell me what's going on.\""
    # play music "Music/Gyumnopedies.mp3"
    # "Kyon ran his hands through his hair and began pacing, not looking at her."
    # "Good; she wasn't the one who had made him mad."
    # nvl clear
    # "\"Have a seat,\" he said."
    # "\"This may take a bit, and I need a promise from you before we start.\""
    # "\"I'm not making a blind promise,\" she retorted, though she did take the seat opposite Koizumi, between Mikuru and Yuki."
    # nvl clear
    # "Yuki wordlessly poured her a cup of tea, which she threw back in a single gulp."
    # "\"I need you to promise to listen to everything we have to say before leaving,\" he answered."
    # "\"That's stupid,\" she grumbled."
    # nvl clear
    # "\"If Yuki's in danger, what kind of person do you take me for?\""
    # "She wasn't that bad about ignoring the needs of her brigade members."
    # "\"Even so.\""
    # "\"Fine,\" she sighed. \"I promise. Now can you get on with it?\""
    # nvl clear
    # "\"Okay,\" he said, pacing around to the window."
    # "\"Almost a year ago — last May — we ended up going on a city search where no one but you and I showed up.\""
    # "\"I remember,\" she said, annoyed."
    # "A stupid practical joke on his part ... though, it had given her the idea for the movie."
    # nvl clear
    # "\"I told you that aliens, espers, and time travelers really existed, right?\""
    # "\"We're going back to that?\" she asked, raising an eyebrow.\"Really?\""
    # "\"Yeah, okay, you remember it, so I don't need to say it again,\" he said with a shrug."
    # nvl clear
    # "\"Koizumi, you promised that if it had to happen, you'd stand next to me when Yuki needed our help. Remember?\""
    # "\"Yes,\" the smiling boy said, though his smile had completely vanished. "
    # "\"As much as it scares me.... Suzumiya-san, Kyon-kun is speaking the truth.\""
    # "\"You're an esper?\" she asked him doubtfully."
    # nvl clear
    # "He gave a solemn nod, and she internalized a sigh."
    # "What, was Kyon just acting?"
    # "Was this is unsubtle way of saying he wanted to be a star in the next movie, not just a camera man?"
    # "She had to admit, his emotion seemed genuine, but why couldn't he just have asked her? "
    # "There was an awful lot he could have just asked for, and never bothered to!"
    # "That thought was drop-kicked to fly off next to the last banished thought."
    # nvl clear
    # "\"And, Mikuru, you're a time traveler?\" she asked, idly spinning her teacup on the table before her."
    # "\"Um ... that is ... I can't....\""
    # "\"Asahina-san,\" Kyon broke in suddenly, \"please ask your supervisor to declassify this for me.\""
    # nvl clear
    # "Mikuru stared at Kyon, her eyes large and confused."
    # "\"Y...yes,\" she agreed, her glance flickering nervously to Haruhi before she pressed a hand against the side of her face, and her eyes became unfocused."
    # "They abruptly snapped back into focus, though her expression had become comically bewildered"
    # nvl clear
    # "\"I ... they said yes!? I don't understand! Kyon-kun, how-\""
    # "\"That's ... classified,\" he answered, looking away."
    # "\"Anyway, go ahead and explain it to Haruhi.\""
    # nvl clear
    # "\'Oh! Um, Suzumiya-san ... what he says is true! I am a time traveler, though, it's more accurate to say that I'm a visitor from the future who is projected into the past, almost like a two-dimensional image projected into—\""
    # "\"Right, right,\" Haruhi cut her off. \"You're a time traveler. Understood.\""
    # nvl clear
    # "Though, Mikuru's acting skills had picked up quite a bit, too...."
    # "This better not be a ploy to make Kyon the male lead opposite Mikuru in the next movie!"
    # "Saving that thought for later, she turned her gaze to Yuki."
    # nvl clear
    # "\"And you're an alien?\""
    # "\"The function allowing me to confirm or deny that data has been denied at this juncture in time,\" she answered."
    # "\"Turning to Kyon, she added, \"One hour and twenty minutes remain.\""
    # nvl clear
    # "He bit off a curse, running his hands through his hair."
    # "Haruhi was taken aback again ... he obviously didn't like getting bad grades or doing poorly on exams, but he almost never got this stressed about things. "
    # "This was starting to become unnerving."
    # nvl clear
    # "\"Okay,\" she said, before he could speak."
    # "\"Look, this has gone far enough. I get it, alright? Your practical joke ... okay. Fine.\""
    # "\"What are you really after? Producer? Co-director? You want to help write the script for the next movie?\""
    # "\'Let's just cut to the chase — this isn't really fun, especially since it's at my expense!\""
    # nvl clear
    # stop music fadeout 1
    # "\"At your expense—\""
    # "That had done it, she realized, flinching back."
    # "Now some of his anger was directed at her, though he quickly controlled it, smacking one palm against his face."
    # play music "Music/Ready.mp3"
    # "\"Last May,\"he said, \"you came to class with your hair in a ponytail.\""
    # nvl clear
    # "She suddenly couldn't meet his eyes, and a previously suplexed thought began to climb back into her awareness."
    # nvl clear
    # "\"It was hot!\" she said defensively.\"What of it?\""
    # "\"You had a dream — a nightmare — that night,\" he added."
    # "\"So?\""
    # nvl clear
    # "She forced her heartbeat to still. "
    # "She'd told him that much, why wouldn't he remember?"
    # "She did, after all, even now."
    # nvl clear
    # "\"So, in your dream, you watched giant blue creatures smash apart the school, and you were very excited about abandoning the Brigade — your friends — and leading an exciting new life in whatever world was to come.\""
    # "Koizumi looked uncomfortable. Mikuru's face turned red, and she began studying the bottom of her teacup intently."
    # "Yuki merely stared at her, unblinking."
    # nvl clear
    # "\"I never told anyone that,\" she mumbled."
    # "\"In the end, I told you that I wanted to come back to this world,\" Kyon said."
    # "\"That it was more interesting than you realized. \""
    # "\"Do I have to say what I did to wake you up?\""
    # nvl clear
    # "She felt her face color."
    # "\"N...no,\" she managed.\"Who— No, what are you?\""
    # "\'I am a normal person,\" he told her, shrugging."
    # nvl clear
    # "\"I happen to have traveled to parallel worlds. I have traveled through time. I've seen some amazing things ... but through it all, I always come back here to be with my friends.\""
    # nvl clear
    # "It was getting very strange, and she didn't know why, but the conversation was starting to make her uncomfortable."
    # "Maybe the knowledge of her dream was just an expert analysis based on her personality? The refusal to mention the kiss specifically was because they didn't know?"
    # "But she wasn't certain she wanted to hear him say it was a kiss, here, right now...."
    # "And she'd promised she would listen."
    # nvl clear
    # "\"You're claiming that you're a slider?\" she asked, blinking, buying herself some time to think."
    # "He was momentarily startled by the question, then exchanged a glance with Koizumi, who shrugged. "
    # "\"Actually, Kyon-kun, you may be,\" the supposed esper said, smiling."
    # "\"That would explain why one never seemed to appear; it was you!\""
    # nvl clear
    # "\"Nevermind that!\" he said quickly, shaking his head."
    # "\"Haruhi, there's something I have to tell you, something I think will make you believe me.\""
    # "\"What's that?\" She couldn't think of anything else to say or ask."
    # nvl clear
    # "\"Tanabata last year was the first time I traveled back in time,\" he began, his expression solemn."
    # "\"I went to a night three years earlier.\""
    # "\"That would be Tanabata four years ago.\""
    # "\"While I was there, I was sent to East Middle school, carrying Asahina-san on my back.\""
    # nvl clear
    # "\"Y...you're...\" she gasped, her eyes widening as the world around her spun, the amazing, simultaneously horrifying and delightful realization that he was speaking the truth was making her dizzy."
    # nvl clear
    # "\"And I met a younger version of yourself, and wrote the message, 'I am here' on the school grounds, following your instructions. You asked who I was, and I told you that I went by ... John Smith.\""
    # nvl clear
    # "\"You're John Smith!\""
    # "She wasn't aware of getting up from the table, uncertain if she had moved around or just jumped over it — she just knew that she had flung herself at him, tackling him to the floor and grabbing on tightly."
    # "\"I knew it!\" she yelled."
    # nvl clear
    # "\"I knew I'd find you again!\""
#     
    
    
   
    
    
#     
#     

label prologue2:    
    scene bg roofclose with fade
    show Asakura Sup1 at center
    "\"Hmm,\" Ryouko mused, turning slowly around, to where her sealed space in the stairway had been breached."
    show Asakura Frown1 at center
    "\"It was broken from the outside, somehow? I wonder—\""
    nvl clear
    play music "Music/Justice.ogg"
    play sound "SE/Barrier2.mp3"
    play sound2 "SE/Laser1.mp3"
    scene bg BeamOrange1 with flashbulb
    "The shrill buzz of a brilliant energy beam licked out from the roof of the tiny structure that housed the stairwell."
    show Asakura Pain1 at center
    "Ryouko was struck in the chest dead-center of mass, her entire body glowing white for a second before she staggered—"
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Barrier1.mp3"
    scene bg BeamOrange2
    show Asakura Pain2 Bright at center
    with flashbulb
    "Instantly another beam shot out from the same location, lighting slightly to one side, near the girl's left shoulder."
    nvl clear
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Slash3.mp3"
    scene bg BeamOrange4
    show Asakura Pain2 Bright at center
    with flashbulb
    "A third, though not as brightly glowing shot was somewhat lower, near her stomach, {nw}"
    scene bg roofclose
    show Asakura Unhap1
    play sound "SE/impact.mp3"
    with dissolve
    extend "and Ryouko dropped to her knees, eyes widened."
    "\"High yield neutron flare?\" she asked. \"Quantum entanglement to disrupt my connection....\""
    scene bg roofright
    pause (0.01)
    play sound "SE/CloakOff.mp3"
    show Kyon Ser1 at right
    show Skinsuit at right
    show Coat at right
    with coatin
    "De-stealthing, Kyon stood from his hiding place atop the stairwell housing, his greatcoat billowing behind him."
    nvl clear
    "The end of his weapon was glowing orange with discharge, the shape changed from a simple cylinder to a much thinner meter-long construction of sturdy rails and curving hand guards."
    "He slung it over his shoulder and ignored it, pulling the second cylinder from his coat and leaping the twenty meter distance between himself and Ryouko."
    play sound "SE/lowswoosh.mp3"
    scene bg roofclose with wiperightfast
    nvl clear
    show Asakura Unhap1 at center
    pause (0.3)
    play sound "SE/guncock.mp3"
    "Beneath him, a widening circle of dust marked where he leapt from, and while in midair he flipped over, a sequence of touch-points converting the unadorned cylinder into a stocky, blunt, two-handed gun."
    play sound "SE/netlaunch.mp3"
    pause (1)
    play sound "SE/stake1.mp3"
    show Spike1 at center
    pause (0.1)
    play sound "SE/stake2.mp3"
    show Spike2 at center
    pause (0.1)
    play sound "SE/stake3.mp3"
    show Spike3 at center
    pause (0.1)
    play sound "SE/stake1.mp3"
    show Spike4 at center
    pause (0.5)
    hide Spike1
    hide Spike2
    hide Spike3
    hide Spike4
    show Spike5 at center
    play sound "SE/elec1.mp3"
    "It fired with a rasping cough, launching a ring of metallic spikes to burrow into the rooftop around Ryouko, and then a grid of crackling brissant energy raked between each of the spikes, snaring the girl in a glowing, shuddering net."
    nvl clear
    "\"Ah,\" she said, her voice disappointed as Kyon's repulsor and gravimetric systems flared his momentum and spread it evenly across the entire rooftop, landing him near Haruhi, at Ryouko's side."
    show Asakura Sigh1 at center
    "\"I failed again.\""
    nvl clear
    hide Asakura
    hide Spike5
    scene bg roof
    show Haruhi Ang1 at left   
    "\"Is that going to hurt her?\" Haruhi asked, crossing her arms over her chest and raising an eyebrow at Kyon in concern."
    show Kyon Ser2 at right
    show Skinsuit at right
    show Coat at right
    nvl clear
    "\"Hurt her?\" he asked, somewhat indignantly."
    show Kyon Ang1 at right
    "\"Haruhi, she's tried to kill me. Three times, now, and you just saw one of them! Your primary concern is that I not hurt her?\""
    show Kyon Sigh1 at right
    play sound "Guncock.mp3"
    "He muttered to himself beneath his breath, folding away his firearm into storage."
    nvl clear
    show Haruhi Ang3 at left
    nvl clear
    "Haruhi tapped a toe impatiently, still staring at him."
    show Kyon Neutral1 at right
    "Pulling a phone identical to the one Haruhi was holding from one pocket, he punched a key. \"Nagato should be here shortly,\" he added, shaking his head."
    show Kyon Ser1 at right
    nvl clear
    "\"This is all up to you. I already know you'll take care of things just fine.\""
    show Haruhi Hap4 at left
    "\"Yes!\" she said, pumping one fist in the air. \"I get to do something! "
    show Haruhi Hap1 at left
    extend "Hey, how's the future?\""
    nvl clear
    show Kyon Sigh1 at right
    "\"It's awesome,\" he said, annoyed. "
    show Kyon Ser2 at right
    extend "\"Try and have some pity for the me that nearly got murdered off a building, huh?"
    show Kyon Neutral1 at right
    "\"Anyway, just so you know, she's programmed to try and kill me; she won't do anything to you.\""
    nvl clear
    show Kyon Neutral2 at right
    "\"And you won't see me tomorrow at school, because I'm going to be ... well. You'll find out.\""
    show Haruhi Pout1 at left
    "\"Okay,\" she agreed, frowning. "
    show Haruhi Quest1 at left
    extend "\"But, hey, why aren't you going to be around?\""
    nvl clear
    show Kyon Ser1 at right
    "\"Further information is not available here,\" he warned, shaking his head."
    show Kyon Smile1 at right
    "\"Now, when you see that other me, tell him I said 'hi', like I always do.\""
    show Kyon Ser1 at right
    "He paused before glancing at his phone again with a grimace."
    "\"My time's up,\"{nw}"
    play sound "SE/CloakOn.mp3"
    hide Kyon
    hide Skinsuit
    hide Coat
    with coatout
    extend " he announced, re-engaging his stealth field and vanishing from sight."
    stop music fadeout 1
    nvl clear
    scene bg roofclose
    show Asakura Sup1 at center
    show Spike5 at center
    "\"What?\" Ryouko asked, still trapped in the containment field. "
    show Asakura Smile3 at center
    extend "\"He just abandoned me here with you?\""
    play music "Music/NagatoTheme.mp3"
    scene bg roofright
    pause (0.5)
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    with wipeup
    "\"Damn it,\" Kyon groaned, from where he was just climbing over the edge of the building, breathing hard. "
    show Kyon Sigh1 at right
    "\"I hate when I have to rely on time-travel to take care of things.\""
    nvl clear
    scene bg roof
    show Haruhi Hap1 at left
    "\"Oh!\" Haruhi said cheerfully. \"Future-you says 'hi', like always!\""
    scene bg roofright
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    "\"Yeah? That guy always annoys me. Probably almost as much as I'm annoyed by having to save past-me.\""
    nvl clear
    scene bg roof
    show Haruhi Hap1 at left
    pause (0.5)
    play sound "SE/Barrier1.mp3"
    show Yuki EyesClosed1 Bright  at center
    show field at center
    with flashbulb
    show Yuki EyesClosed1 at center
    hide field with dissolve
    "There was a flash of light and a warping of space, and then Nagato appeared at Haruhi's side."
    show Yuki Side1 at center
    "The circle of illumination around Haruhi's feet had vanished."
    scene bg roofclose with wipeup
    show Asakura Sigh1 at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft with moveinleft
    "While Nagato knelt to examine Ryouko, Haruhi dashed to Kyon's side and helped him stand."
    nvl clear
    scene bg roofright
    show Kyon Pain2 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center with moveinleft
    "\"How bad was it, anyway? Future-you seemed to think you weren't very tough, and that you were hurt pretty badly.\""
    show Kyon Pain1 at right
    "\"I think I've got some internal bleeding,\" he said, wincing, one hand pressed to his abdomen. "
    show Kyon Pain2 at right
    extend "\"And some of my gear is messed up from the impact and overload. While this is fun for you, I wouldn't mind some medical assistance.\""
    nvl clear
    show Haruhi Hap3 at center
    "\"Sure!\" she said cheerfully, clapping one hand on his shoulder. "
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    extend "\"Happy, healing, all-better thoughts!\""
    scene bg roofclose
    show Asakura Sigh1 at center
    show Spike5 at center
    show Yuki Talk1 at HalfLeft
    "\"Medical program loaded,\" Nagato added helpfully from where she was studying the other interface. "
    show Yuki Talk2 at HalfLeft
    extend "\"Permission to proceed?\""
    scene bg roofright
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center
    "\"Granted.\" Kyon said, {nw}"
    play sound "SE/heal1.wav"
    show field at right
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show Coat Bright at right
    with dissolve
    pause .1
    hide field at right
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    with dissolve
    extend "straightening up as a sparkle of green and white lights suffused up from the rooftop beneath him, flowing through his body and undoing the damage."
    nvl clear
    show Kyon Smile1 at right
    "\"Oh, that feels so much better! Thank you; that probably saved my life."
    show Kyon Neutral2 at right
    "\"And for future reference, you can probably assume that I'm okay with that one being used.\""
    "\"Acknowledged,\" Nagato agreed."
    nvl clear
    show Haruhi Smile2 at left with move
    "\"Hmm, hey, Kyon, you know, you're going to have to really step up your game,\" Haruhi said suddenly, tossing his cell phone back to him."
    show Kyon Ser1 at right
    play sound "SE/woosh.mp3"
    hide Skinsuit with wipedown
    play sound "SE/CloakOn.mp3"
    hide Coat with coatout
    "He scowled, pocketed it, and then banished all of his equipment, the greatcoat taking the longest to phase out of view."
    show Kyon Ser2 at right
    "\"What's that supposed to mean?\" he asked in irritation."
    nvl clear
    show Haruhi Sigh1 at left
    "\"Well, this is fun and all, but you can hardly expect me to take your lectures on using power responsibly seriously when you're always relying on your future self to save you,\" she warned, raising one finger and waggling it at him."
    show Kyon Sigh2 at right
    "He sighed and hung his head. \"You know, I really am trying my hardest,\""
    show Kyon Worry1 at right
    show Haruhi Worry1 at left
    extend " he muttered, crossing his arms over his chest and looking away towards the sea."
    nvl clear
    show Kyon Ser1 at right
    "\"But I can't just leave you alone, and Nagato can't handle another interface right now.\""
    scene bg roofclose
    show Asakura Smile2  at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft
    "\"And you did such a great job!\" Ryouko encouraged from beneath her energy net."
    show Asakura Smile1 at center
    "\"Time travel, is it? Now that's one tool you seem to know how to use well.\""
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\"It's fine,\" Nagato said tonelessly."
    show Yuki Talk2 at HalfLeft
    "\"Asakura Ryouko is isolated and confined; she is limited to her organic functions at this moment."
    show Yuki Talk1 at HalfLeft
    "\"After she is dispatched, I will retrieve defenses to protect against further interference.\""
    nvl clear
    scene bg roofright
    show Haruhi Sup1 at left
    show Kyon Ser1 at right
    "\"Waaaait!\" Haruhi yelled, stomping one foot and spinning to face Yuki."
    show Haruhi Ang2 at left
    "\"'Dispatched'? I don't think so! If you need something from her, there's got to be a way to do it without killing her!"
    show Haruhi Ang1 at left
    "\"What's the point of running into another alien, just to kill them?\""
    nvl clear
    show Kyon Sigh1 at right
    "\"But the fighting is fine,\" Kyon observed, stretching his arms above his head, then swiveling his hips and stretching his spine out."
    show Kyon Ang1 at right
    "\"After all, no one of any importance was smashed off a building.\""
    show Haruhi Eyeroll1 at left
    "\"Kyon!\""
    show Kyon Sigh2 at right
    "\"Alright,\" he said, shaking his head."
    nvl clear
    show Kyon Ser1 at right
    "\"I don't really want Asakura to die either. But if her body were destroyed, she'd just go back to the place she came from."
    show Kyon Worry1 at right
    "\"At least, as I understand it.\" He shot a questioning glance towards Nagato."
    nvl clear
    "She didn't meet his eyes."
    nvl clear
    show Haruhi Hap1 at left
    "\"Good!\" Haruhi nodded decisively, grinning again."
    show Haruhi Smile3 at left
    "\"Yuki, let's come up with a backup plan. Something that will let you get your power-up and let us reform Ryouko. Can we do that?\""
    scene bg roofclose
    show Asakura Frown1  at center
    show Spike5 at center
    show Yuki Side1 at HalfLeft
    "Nagato stared intently at Ryouko, then gave a decisive nod. "
    show Yuki Talk1 at HalfLeft
    extend "\"Awaiting program,\" she announced."
    nvl clear
    show Haruhi Ang3 at left with moveinleft
    show Kyon Ser1 at right with moveinright
    show Yuki Side1
    "\"Hmm,\" Haruhi mused, narrowing her eyes and peering intently at Ryouko, who merely watched back curiously."
    show Haruhi Ang2 at left
    "\"Um ... some kind of second chance ... a chance to start over, prove herself, and ... let's see, realize she doesn't want to kill Kyon at all.\""
    nvl clear
    show Haruhi Smile2 at left
    "\"And she gets to give Yuki what she needs to make her equal to the next interface that comes along.... But no brainwashing, that's not cool."
    show Haruhi Smile3 at left
    "\"So, maybe an 'evil' module or something like that, which Yuki can purify and use for good, letting Ryouko learn how to become a nicer person?\""
    nvl clear
    show Haruhi Hap3 at left
    "\"Yeah! That sounds very good! Let's do that.\""
    show Haruhi Smile2 at left
    nvl clear
    show Asakura Frown3 at center
    pause (0.4)
    show Asakura Frown1 at center
    "The pinned interface blinked several times, then turned her eyes to Kyon from beneath the glowing energy net."
    show Asakura Frown2 at center
    "\"None of this has been reported to my superiors,\" she commented."
    show Asakura Smile2 at center
    "\"It's entirely possible that this new knowledge could change their perceptions; there's no reason to be hasty!\""
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\"Program loaded,\" Nagato replied."
    show Yuki Talk2 at HalfLeft
    "\"Permission to proceed?\""
    nvl clear
    show Yuki Side1 at HalfLeft
    show Asakura Pain1 at center
    "\"We can be reasonable!\" Ryouko protested."
    show Kyon Sigh1 at right
    "\"You're probably the most reasonable person I've ever had try to kill me,\" Kyon agreed."
    show Kyon Ang1 at right
    "\"But I remember that time you did stab me all too well.\""
    show Haruhi Ang1 at left
    "\"No stabbing!\" Haruhi said in a chastising tone. "
    show Haruhi Ang2 at left
    extend "\"Bad Ryouko! No class rep votes for you!\""
    nvl clear
    show Haruhi Smile1 at left
    show Kyon Neutral1 at right
    "\"...you don't really think that's her prime concern, do you? Aside from which, did you even vote last time?\""
    show Asakura Frown1 at center
    "\"It isn't,\" Ryouko agreed. \"And no, she didn't. "
    show Asakura Smile2 at center
    extend "But, about being reasonable...\""
    show Kyon Puzzle1 at right
    "\"Anything that I should know about this program, Nagato?\" Kyon asked, quirking one eyebrow higher."
    nvl clear
    show Yuki Talk1 at HalfLeft
    "\"It will be beneficial to all involved,\" Nagato assured him, while Haruhi nodded knowingly."
    show Kyon Sigh2 at right
    show Asakura Unhap1 at center
    "\"Okay,\" he sighed, shaking his head."
    show Kyon Ser1 at right
    "\"Granted.\""
    nvl clear
    show Yuki Side2 at HalfLeft
    "The smaller girl turned her gaze back to Ryouko's bound form, the faintest hint of a smile coming to her lips."
    nvl clear
    scene black
    stop music
    "\"I will not let you harm him again.\""
    
    
    
