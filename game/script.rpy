# This is a proof-of-concept K:BDH VN. Main script file; contains init code and code declarations.

init:
    image bg classroom = "Backgrounds/classroom.jpg"
    image bg hallway = "Backgrounds/hallway.png"
    image bg stairwell = "Backgrounds/stairwell.jpg"
    image bg stairwellbarrier = "Backgrounds/stairwellbarrier.jpg"
    image bg roof = "Backgrounds/roof.jpg"
    image bg roofclose = "Backgrounds/roofclose.jpg"
    image bg daysky = "Backgrounds/daysky.png"
    image bg MorningSky = "Backgrounds/MorningSky.png"
    image bg roofright = "Backgrounds/roofright.jpg"
    image bg BeamOrange1 = "Backgrounds/BeamOrange1.jpg"
    image bg BeamOrange2 = "Backgrounds/BeamOrange2.jpg"
    image bg BeamOrange3 = "Backgrounds/BeamOrange3.jpg"
    image bg BeamOrange4 = "Backgrounds/BeamOrange4.jpg"
    image bg BeamOrange5 = "Backgrounds/BeamOrange5.jpg"
    image bg KyonRoomLeftClosed = "Backgrounds/KyonRoomLeftClosed.png"
    image bg KyonRoomLeftMorning = "Backgrounds/KyonRoomLeftMorning.png"
    image bg KyonHouseNight = "Backgrounds/KyonHouseNight.png"
    image bg TownStreetNight1 = "Backgrounds/TownStreetNight1.png"
    image bg TownStreetNight2 = "Backgrounds/TownStreetNight2.png"
    
    image bg YukiApartmentNight = "Backgrounds/YukiApartmentNight.png"
    image bg YukiRoomLeft = "Backgrounds/YukiRoomLeft.png"
    image bg YukiRoomRight = "Backgrounds/YukiRoomRight.png"
    image bg YukiRoomCenter = "Backgrounds/YukiRoomCenter.jpg"
    image bg MemoryYuki = "Backgrounds/MemoryYuki.jpg"
    image bg MemoryMikuru = "Backgrounds/MemoryMikuru.jpg"
    image bg MemoryKoizumi = "Backgrounds/MemoryKoizumi.jpg"
    
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    image title0 = "Backgrounds/title0.png"
    image title1 = "Backgrounds/title1.png"
    image Barrier = "Backgrounds/barrier2.jpg"
    image Bluesword = "Backgrounds/bluesword1.png"
    image field = "Sprites/Effects/InterdictionField.png"
    image healfield = "Sprites/Effects/HealingField.png"
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
    
    image TownHillLeftMorning =  "Backgrounds/TownHillLeftMorning.png"
    
    #Haruhi Sprites
    image Haruhi Sup1 = "Sprites/Haruhi/HaruhiSideSurprised1.png"
    image Haruhi Ang1 = "Sprites/Haruhi/HaruhiSideAngry1.png"
    image Haruhi Ang2 = "Sprites/Haruhi/HaruhiSideAngry2.png"
    image Haruhi Ang3 = "Sprites/Haruhi/HaruhiSideAngry3.png"
    image Haruhi Ang4 = "Sprites/Haruhi/HaruhiSideAngry4.png"
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
    image Haruhi Unhap1 = "Sprites/HaruhiSideUnhappy1.png"
    image Haruhi Unhap2 = "Sprites/HaruhiSideUnhappy2.png"
    image Haruhi Focus1 = "Sprites/Haruhi/HaruhiSideFocus1.png"
    
    image Haruhi Casual Sup1 = "Sprites/Haruhi/HaruhiSideCasualSurprised1.png"
    image Haruhi Casual Sup2 = "Sprites/Haruhi/HaruhiSideCasualSurprised2.png"
    image Haruhi Casual Sup3 = "Sprites/Haruhi/HaruhiSideCasualSurprised3.png"
    image Haruhi Casual Ang1 = "Sprites/Haruhi/HaruhiSideCasualAngry1.png"
    image Haruhi Casual Ang2 = "Sprites/Haruhi/HaruhiSideCasualAngry2.png"
    image Haruhi Casual Ang3 = "Sprites/Haruhi/HaruhiSideCasualAngry3.png"
    image Haruhi Casual Ang4 = "Sprites/Haruhi/HaruhiSideCasualAngry4.png"
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
    image Haruhi Casual Unhap1 = "Sprites/Haruhi/HaruhiSideCasualUnhappy1.png"
    image Haruhi Casual Unhap2 = "Sprites/Haruhi/HaruhiSideCasualUnhappy2.png"
    image Haruhi Casual Focus1 = "Sprites/Haruhi/HaruhiSideCasualFocus1.png"
    
    image Haruhi Crossed Sup1 = "Sprites/Haruhi/HaruhiCrossedSurprised1.png"
    image Haruhi Crossed Sup2 = "Sprites/Haruhi/HaruhiCrossedSurprised2.png"
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
    image Haruhi Crossed Tsun1 = "Sprites/Haruhi/HaruhiCrossedTsun1.png"
    
    image Haruhi Crossed Casual Sup1 = "Sprites/Haruhi/HaruhiCrossedCasualSurprised1.png"
    image Haruhi Crossed Casual Sup2 = "Sprites/Haruhi/HaruhiCrossedCasualSurprised2.png"
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
    image Haruhi Crossed Casual Tsun1 = "Sprites/Haruhi/HaruhiCrossedCasualTsun1.png"
    
    image Haruhi Point Ang1 = "Sprites/Haruhi/HaruhiPointAngry1.png"
    image Haruhi Point Scold1 = "Sprites/Haruhi/HaruhiPointScold1.png"
    
    image Haruhi Point Casual Ang1 = "Sprites/Haruhi/HaruhiPointCasualAngry1.png"
    image Haruhi Point Casual Scold1 = "Sprites/Haruhi/HaruhiPointCasualScold1.png"
    
    image Hblush = "Sprites/Haruhi/HaruhiSideBlush1.png"
    image Hblush Casual = "Sprites/Haruhi/HaruhiSideCasualBlush1.png"
    image Htears ="Sprites/Haruhi/HTearsSide1.png"
    image Htears Casual = "Sprites/Haruhi/HTearsSideCasual1.png"
    
    
    #Kyon Sprites
    image Kyon Ser1 = "Sprites/Kyon/KyonSerious1.png"
    image Kyon Ser2 = "Sprites/Kyon/KyonSerious2.png"
    image Kyon Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Ser3 = "Sprites/Kyon/KyonSerious3.png"
    image Kyon Sigh1 = "Sprites/Kyon/KyonSigh1.png"
    image Kyon Sigh2 = "Sprites/Kyon/KyonSigh2.png"
    image Kyon Sigh3 = "Sprites/Kyon/KyonSigh3.png"
    image Kyon Neutral1 = "Sprites/Kyon/KyonNeutral1.png"
    image Kyon Neutral2 = "Sprites/Kyon/KyonNeutral2.png"
    image Kyon Neutral3 = "Sprites/Kyon/KyonNeutral3.png"
    image Kyon Ang1 = "Sprites/Kyon/KyonAngry1.png"
    image Kyon Pain1 = "Sprites/Kyon/KyonPained1.png"
    image Kyon Pain2 = "Sprites/Kyon/KyonPained2.png"
    image Kyon Smile1 = "Sprites/Kyon/KyonSmile1.png"
    image Kyon Smile2 = "Sprites/Kyon/KyonSmile2.png"
    image Kyon Worry1 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Worry2 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Puzzle1 = "Sprites/Kyon/KyonPuzzled1.png"
    image Kyon Sup1 = "Sprites/Kyon/KyonSurprised1.png"
    image Kyon Sup2 = "Sprites/Kyon/KyonSurprised2.png"
    
    
    image Kyon Casual Ser1 = "Sprites/Kyon/KyonCasualSerious1.png"
    image Kyon Casual Ser2 = "Sprites/Kyon/KyonCasualSerious2.png"
    image Kyon Casual Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonCasualSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Casual Ser3 = "Sprites/Kyon/KyonCasualSerious3.png"
    image Kyon Casual Sigh1 = "Sprites/Kyon/KyonCasualSigh1.png"
    image Kyon Casual Sigh2 = "Sprites/Kyon/KyonCasualSigh2.png"
    image Kyon Casual Sigh3 = "Sprites/Kyon/KyonCasualSigh3.png"
    image Kyon Casual Neutral1 = "Sprites/Kyon/KyonCasualNeutral1.png"
    image Kyon Casual Neutral2 = "Sprites/Kyon/KyonCasualNeutral2.png"
    image Kyon Casual Neutral3 = "Sprites/Kyon/KyonCasualNeutral3.png"
    image Kyon Casual Ang1 = "Sprites/Kyon/KyonCasualAngry1.png"
    image Kyon Casual Pain1 = "Sprites/Kyon/KyonCasualPained1.png"
    image Kyon Casual Pain2 = "Sprites/Kyon/KyonCasualPained2.png"
    image Kyon Casual Smile1 = "Sprites/Kyon/KyonCasualSmile1.png"
    image Kyon Casual Smile2 = "Sprites/Kyon/KyonCasualSmile2.png"
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
    image Asakura Blink1:
        "Sprites/Asakura/AsakuraFrown1.png"
        0.1
        "Sprites/Asakura/AsakuraFrown3.png"
        0.2
        "Sprites/Asakura/AsakuraFrown1.png"
        3
        repeat
        
    
    #Yuki Sprites
    image Yuki EyesClosed1 = "Sprites/Yuki/YukiSideEyesClosed1.png"
    image Yuki EyesClosed1 Bright = im.MatrixColor("Sprites/Yuki/YukiSideEyesClosed1.png",
                                       im.matrix.brightness(.5))
    image Yuki Side1 = "Sprites/Yuki/YukiSide1.png"
    image Yuki Side2 = "Sprites/Yuki/YukiSide2.png"
    image Yuki SideDisappointed1 = "Sprites/Yuki/YukiSideDisappointed1.png"
    image Yuki SideDisappointedTalk1 = "Sprites/Yuki/YukiSideDisappointedTalk1.png"
    image Yuki SideEyesClosed1 = "Sprites/Yuki/YukiSideEyesClosed1.png"
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
    image Yuki Casual Talk1 = "Sprites/Yuki/YukiSideCasualTalk1.png"
    image Yuki Casual Talk2 = "Sprites/Yuki/YukiSideCasualTalk2.png"
    image Yuki Casual Sad1 = "Sprites/Yuki/YukiSideCasualSad1.png"
    image Yuki Casual Sad2 = "Sprites/Yuki/YukiSideCasualSad2.png"
    image Yuki Casual Sad3 = "Sprites/Yuki/YukiSideCasualSad3.png"
    image Yuki Casual SadTalk2 = "Sprites/Yuki/YukiSideCasualSadTalk2.png"
    image Yuki Casual SadTalk3 = "Sprites/Yuki/YukiSideCasualSadTalk3.png"
    
    image Yuki Side Blink:
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSideEyesClosed1.png"
        0.1
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSide1.png"
    image Yuki Side SmallBlink:
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSideEyesClosed1.png"
        0.15
        "Sprites/Yuki/YukiSide1.png"
        3
        repeat
    
    # Mikuru Sprites
    image Mikuru Cower Nervous1 = "Sprites/Mikuru/MikuruCowerNervous1.png"
    image Mikuru Cower Nervous2 = "Sprites/Mikuru/MikuruCowerNervous2.png"
    image Mikuru Cower Nervous3 = "Sprites/Mikuru/MikuruCowerNervous3.png"
    image Mikuru Cower Neutral1 = "Sprites/Mikuru/MikuruCowerNeutral1.png"
    image Mikuru Cower Sup1 = "Sprites/Mikuru/MikuruCowerSurprised1.png"
    image Mikuru Cower Sigh1 = "Sprites/Mikuru/MikuruCowerSigh1.png"
    image Mikuru Cower Wince1 = "Sprites/Mikuru/MikuruCowerWince1.png"
    image Mikuru Cower Smile1 ="Sprites/Mikuru/MikuruCowerSmile1.png"
    image MBlush = "Sprites/Mikuru/MikuruCowerBlush1.png"
    image MTears = "Sprites/Mikuru/MTearsCower1.png"
    
    image Mikuru Cower Casual Nervous1 = "Sprites/Mikuru/MikuruCowerCasualNervous1.png"
    image Mikuru Cower Casual Nervous2 = "Sprites/Mikuru/MikuruCowerCasualNervous2.png"
    image Mikuru Cower Casual Nervous3 = "Sprites/Mikuru/MikuruCowerCasualNervous3.png"
    image Mikuru Cower Casual Neutral1 = "Sprites/Mikuru/MikuruCowerCasualNeutral1.png"
    image Mikuru Cower Casual Sup1 = "Sprites/Mikuru/MikuruCowerCasualSurprised1.png"
    image Mikuru Cower Casual Sigh1 = "Sprites/Mikuru/MikuruCowerCasualSigh1.png"
    image Mikuru Cower Casual Wince1 = "Sprites/Mikuru/MikuruCowerCasualWince1.png"
    image Mikuru Cower Casual Smile1 ="Sprites/Mikuru/MikuruCowerCasualSmile1.png"
    image MTears Casual = "Sprites/Mikuru/MTearsCowerCasual1.png"
    
    #Koizumi Sprites
    image Koizumi Crossed Ser1 = "Sprites/Koizumi/KoizumiCrossedSerious1.png"
    image Koizumi Crossed Ser2 = "Sprites/Koizumi/KoizumiCrossedSerious2.png"
    image Koizumi Crossed Smile1 = "Sprites/Koizumi/KoizumiCrossedSmile1.png"
    image Koizumi Crossed Smile2 = "Sprites/Koizumi/KoizumiCrossedSmile2.png"
    image Koizumi Crossed Uneasy1 = "Sprites/Koizumi/KoizumiCrossedUneasy1.png"
    image Koizumi Crossed Uneasy2 = "Sprites/Koizumi/KoizumiCrossedUneasy2.png"
    image Koizumi Crossed Uneasy3 = "Sprites/Koizumi/KoizumiCrossedUneasy3.png"
    
    image Koizumi Crossed Casual Ser1 = "Sprites/Koizumi/KoizumiCrossedCasualSerious1.png"
    image Koizumi Crossed Casual Ser2 = "Sprites/Koizumi/KoizumiCrossedCasualSerious2.png"
    image Koizumi Crossed Casual Smile1 = "Sprites/Koizumi/KoizumiCrossedCasualSmile1.png"
    image Koizumi Crossed Casual Smile2 = "Sprites/Koizumi/KoizumiCrossedCasualSmile2.png"
    image Koizumi Crossed Casual Uneasy1 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy1.png"
    image Koizumi Crossed Casual Uneasy2 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy2.png"
    image Koizumi Crossed Casual Uneasy3 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy3.png"
    

    image Credits0 = "Backgrounds/credits0.png"
    image Credits1 = "Backgrounds/credits1.png"
    image Credits2 = "Backgrounds/credits2.png"
    image Credits3 = "Backgrounds/credits3.png"

init python:
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
    
    # positions on the (imaginary) screen situated directly left of one shown.
    osl_center = Position(xanchor=0.5, yalign=1.0, xpos=-0.5)
    osl_right = Position(xanchor=0.5, yalign=1.0, xpos=-0.25)
    # positions on the (imaginary) screen situatet directly right of one shown.
    osr_center = Position(xanchor=0.5, yalign=1.0, xpos=1.5)
    osr_left = Position(xanchor=0.5, yalign=1.0, xpos=1.25)
    
    # position of the energy net, lower than truecenter, to cover the Ryoko better.
    spike_net_pos = Position(xalign=0.5, yanchor=0.5, ypos=0.65)
    
    fast_move = MoveTransition(0.2)
    
    # Screen shake effect.
    sshake = Shake((0, 0, 0, 0), 1.0, dist=30)
    
    adj = ui.adjustment()
    music_need = True

    
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


init -1 python:
    chapters = [
        ("In Media Res Prologue\nExactly What it Says on the Tin", "prologue"),
        ("Obligatory Anachronic Order \nExplanation Arc chapter one\n\"Scene Twelve, the Ninth Big Fight\"", "AO1_1"),
    ]


label start:
    # Z0 : TODO: intro. 
    jump prologue
    
    
label credits:
    # Thise entire things could be done with text() displayable...
    # Duly noted. I'll look into that next time there aren't fifteen other things to do.
    stop music fadeout 1
    scene black with fade
    # The hardpause calls are necessary because otherwise Ren'py wants to skip over all the pause statements on a single press of the key.
    show Credits0 with dissolve
    pause
    $ renpy.pause(.1, hard=True)
    show Credits1 with dissolve
    pause
    $ renpy.pause(.1, hard=True)
    show Credits2 with dissolve
    pause
    $ renpy.pause(.1, hard=True)
    show Credits3 with dissolve
    # Maybe a graphic logo here?
    pause
    return
