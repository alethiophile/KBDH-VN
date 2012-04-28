# This is a proof-of-concept K:BDH VN. Main script file; contains init code and code declarations.

init:
    image almostblack one = "#0008"
    image almostblack two = "#000e"
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
    image bg KyonRoomRightClosed = "Backgrounds/KyonRoomRightClosed.png"
    image bg KyonRoomLeftMorning = "Backgrounds/KyonRoomLeftMorning.png"
    image bg KyonRoomRightMorning = "Backgrounds/KyonRoomRightMorning.png"
    image bg KyonHouseNight = "Backgrounds/KyonHouseNight.png"
    image bg KyonHouseDay = "Backgrounds/KyonHouseDay.png"
    image bg TownStreetNight1 = "Backgrounds/TownStreetNight1.png"
    image bg TownStreetNight2 = "Backgrounds/TownStreetNight2.png"
    image bg TownStreetDay1 = "Backgrounds/TownStreetDay1.jpg"
    image bg TownStreetDay2 = "Backgrounds/TownStreetDay2.jpg"
    image bg Elevator = "Backgrounds/ElevatorInterior.png"
    image bg ClubHallLeft = "Backgrounds/ClubHallLeft.png"
    image bg ClubroomCenterDay = "Backgrounds/ClubroomCenterDay.png"
    image bg ClubroomLeftDay = "Backgrounds/ClubroomLeftDay.png"
    image bg ClubroomFullDay ="Backgrounds/ClubroomFullDay.jpg"
    image bg ClubroomRightDay = "Backgrounds/ClubroomRightDay.png"
    image bg ClubroomFullNight = "Backgrounds/ClubroomFullNight.png"
    image bg ClubroomBack = "Backgrounds/ClubBack.png"
    image ClubTable ="Backgrounds/ClubTable.png"
    image bg YukiApartmentDay = "Backgrounds/YukiApartmentDay.png"
    image bg YukiApartmentNight = "Backgrounds/YukiApartmentNight.png"
    image bg YukiRoomLeft = "Backgrounds/YukiRoomLeft.png"
    image bg YukiRoomRight = "Backgrounds/YukiRoomRight.png"
    image bg YukiRoomCenter = "Backgrounds/YukiRoomCenter.jpg"
    image bg SchoolOutside1 = "Backgrounds/SchoolOutside1.png"
    image bg SchoolEntranceLeft = "Backgrounds/SchoolEntranceLeft.png"
    image bg SchoolEntranceRight = "Backgrounds/SchoolEntranceLeft.png"
    image bg Cafe = "Backgrounds/Cafe.jpg"
    image bg ParkBench = "Backgrounds/ParkBench.png"
    image bg ParkPath = "Backgrounds/ParkPath.png"
    image bg SchoolTable = "Backgrounds/SchoolTable.jpg"
    image bg Cab = "Backgrounds/Cab.jpg"
    image bg Space = "Backgrounds/Space.jpg"
    image bg MemoryYuki = "Backgrounds/MemoryYuki.jpg"
    image bg MemoryMikuru = "Backgrounds/MemoryMikuru.jpg"
    image bg MemoryKoizumi = "Backgrounds/MemoryKoizumi.jpg"
    image bg Kiss = "Backgrounds/kiss.jpg"
    image clouds = "id_clouds.png"
    image bg HaruhiCS = "Backgrounds/HaruhiCS.jpg"
    image bg ClubHallLeft = "Backgrounds/ClubHallLeft.png"
    image bg ClubHallRight = "Backgrounds/ClubHallRight.png"  
    image bg StudentCouncil = "Backgrounds/StudentCouncilRoom.png"
    image bg Alley = "Backgrounds/Alley.png"
    
    
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    # image title0 = "Backgrounds/title0.png"
    # image title1 = "Backgrounds/title1.png"
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
    image Haruhi Sup2 = "Sprites/Haruhi/HaruhiSideSurprised2.png"
    image Haruhi Sup3 = "Sprites/Haruhi/HaruhiSideSurprised3.png"
    image Haruhi Ang1 = "Sprites/Haruhi/HaruhiSideAngry1.png"
    image Haruhi Ang2 = "Sprites/Haruhi/HaruhiSideAngry2.png"
    image Haruhi Ang3 = "Sprites/Haruhi/HaruhiSideAngry3.png"
    image Haruhi Ang4 = "Sprites/Haruhi/HaruhiSideAngry4.png"
    image Haruhi Ang5 = "Sprites/Haruhi/HaruhiSideAngry5.png"
    image Haruhi Hap1 = "Sprites/Haruhi/HaruhiSideHappy1.png"
    image Haruhi Hap2 = "Sprites/Haruhi/HaruhiSideHappy2.png"
    image Haruhi Hap3 = "Sprites/Haruhi/HaruhiSideHappy3.png"
    image Haruhi Hap4 = "Sprites/Haruhi/HaruhiSideHappy4.png"
    image Haruhi Pout1 = "Sprites/Haruhi/HaruhiSidePout1.png"
    image Haruhi Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Pout2 = "Sprites/Haruhi/HaruhiSidePout2.png"
    image Haruhi Eyeroll1 = "Sprites/Haruhi/HaruhiSideEyeroll1.png"
    image Haruhi Eyeroll2 = "Sprites/Haruhi/HaruhiSideEyeroll2.png"
    image Haruhi Quest1 = "Sprites/Haruhi/HaruhiSideQuestion1.png"
    image Haruhi Quest2 = "Sprites/Haruhi/HaruhiSideQuestion2.png"
    image Haruhi Grin1 = "Sprites/Haruhi/HaruhiSideGrin1.png"
    image Haruhi Grin2 = "Sprites/Haruhi/HaruhiSideGrin2.png"
    image Haruhi Worry1 = "Sprites/Haruhi/HaruhiSideWorry1.png"
    image Haruhi Worry2 = "Sprites/Haruhi/HaruhiSideWorry2.png"
    image Haruhi Smile1 = "Sprites/Haruhi/HaruhiSideSmile1.png"
    image Haruhi Smile2 = "Sprites/Haruhi/HaruhiSideSmile2.png"
    image Haruhi Smile3 = "Sprites/Haruhi/HaruhiSideSmile3.png"
    image Haruhi Sigh1 = "Sprites/Haruhi/HaruhiSideSigh1.png"
    image Haruhi Sigh2 = "Sprites/Haruhi/HaruhiSideSigh2.png"
    image Haruhi Sigh3 = "Sprites/Haruhi/HaruhiSideSigh3.png"
    image Haruhi Unhap1 = "Sprites/Haruhi/HaruhiSideUnhappy1.png"
    image Haruhi Unhap2 = "Sprites/Haruhi/HaruhiSideUnhappy2.png"
    image Haruhi Unhap3 = "Sprites/Haruhi/HaruhiSideUnhappy3.png"
    image Haruhi Focus1 = "Sprites/Haruhi/HaruhiSideFocus1.png"
    image Haruhi Neutral1 ="Sprites/Haruhi/HaruhiSideNeutral1.png"
    image Haruhi Neutral2 ="Sprites/Haruhi/HaruhiSideNeutral2.png"
    
    image Haruhi Casual Sup1 = "Sprites/Haruhi/HaruhiSideCasualSurprised1.png"
    image Haruhi Casual Sup2 = "Sprites/Haruhi/HaruhiSideCasualSurprised2.png"
    image Haruhi Casual Sup3 = "Sprites/Haruhi/HaruhiSideCasualSurprised3.png"
    image Haruhi Casual Ang1 = "Sprites/Haruhi/HaruhiSideCasualAngry1.png"
    image Haruhi Casual Ang2 = "Sprites/Haruhi/HaruhiSideCasualAngry2.png"
    image Haruhi Casual Ang3 = "Sprites/Haruhi/HaruhiSideCasualAngry3.png"
    image Haruhi Casual Ang4 = "Sprites/Haruhi/HaruhiSideCasualAngry4.png"
    image Haruhi Casual Ang5 = "Sprites/Haruhi/HaruhiSideCasualAngry5.png"
    image Haruhi Casual Hap1 = "Sprites/Haruhi/HaruhiSideCasualHappy1.png"
    image Haruhi Casual Hap2 = "Sprites/Haruhi/HaruhiSideCasualHappy2.png"
    image Haruhi Casual Hap3 = "Sprites/Haruhi/HaruhiSideCasualHappy3.png"
    image Haruhi Casual Hap4 = "Sprites/Haruhi/HaruhiSideCasualHappy4.png"
    image Haruhi Casual Pout1 = "Sprites/Haruhi/HaruhiSideCasualPout1.png"
    image Haruhi Casual Pout1 Bright = im.MatrixColor("Sprites/Haruhi/HaruhiSideCasualPout1.png",
                                       im.matrix.brightness(.5))
    image Haruhi Casual Pout2 = "Sprites/Haruhi/HaruhiSideCasualPout2.png"
    image Haruhi Casual Eyeroll1 = "Sprites/Haruhi/HaruhiSideCasualEyeroll1.png"
    image Haruhi Casual Eyeroll2 = "Sprites/Haruhi/HaruhiSideCasualEyeroll2.png"
    image Haruhi Casual Quest1 = "Sprites/Haruhi/HaruhiSideCasualQuestion1.png"
    image Haruhi Casual Quest2 = "Sprites/Haruhi/HaruhiSideCasualQuestion2.png"
    image Haruhi Casual Grin1 = "Sprites/Haruhi/HaruhiSideCasualGrin1.png"
    image Haruhi Casual Grin2 = "Sprites/Haruhi/HaruhiSideCasualGrin2.png"
    image Haruhi Casual Worry1 = "Sprites/Haruhi/HaruhiSideCasualWorry1.png"
    image Haruhi Casual Worry2 = "Sprites/Haruhi/HaruhiSideCasualWorry2.png"
    image Haruhi Casual Smile1 = "Sprites/Haruhi/HaruhiSideCasualSmile1.png"
    image Haruhi Casual Smile2 = "Sprites/Haruhi/HaruhiSideCasualSmile2.png"
    image Haruhi Casual Smile3 = "Sprites/Haruhi/HaruhiSideCasualSmile3.png"
    image Haruhi Casual Sigh1 = "Sprites/Haruhi/HaruhiSideCasualSigh1.png"
    image Haruhi Casual Sigh2 = "Sprites/Haruhi/HaruhiSideCasualSigh2.png"
    image Haruhi Casual Sigh3 = "Sprites/Haruhi/HaruhiSideCasualSigh3.png"
    image Haruhi Casual Unhap1 = "Sprites/Haruhi/HaruhiSideCasualUnhappy1.png"
    image Haruhi Casual Unhap2 = "Sprites/Haruhi/HaruhiSideCasualUnhappy2.png"
    image Haruhi Casual Unhap3 = "Sprites/Haruhi/HaruhiSideCasualUnhappy3.png"
    image Haruhi Casual Focus1 = "Sprites/Haruhi/HaruhiSideCasualFocus1.png"
    image Haruhi Casual Neutral1 ="Sprites/Haruhi/HaruhiSideCasualNeutral1.png"
    image Haruhi Casual Neutral2 ="Sprites/Haruhi/HaruhiSideCasualNeutral2.png"
    
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
    image Haruhi Crossed Pout2 = "Sprites/Haruhi/HaruhiCrossedPout2.png"
    image Haruhi Crossed Eyeroll1 = "Sprites/Haruhi/HaruhiCrossedEyeroll1.png"
    image Haruhi Crossed Quest1 = "Sprites/Haruhi/HaruhiCrossedQuestion1.png"
    image Haruhi Crossed Grin1 = "Sprites/Haruhi/HaruhiCrossedGrin1.png"
    image Haruhi Crossed Worry1 = "Sprites/Haruhi/HaruhiCrossedWorry1.png"
    image Haruhi Crossed Worry2 = "Sprites/Haruhi/HaruhiCrossedWorry2.png"
    image Haruhi Crossed Smile1 = "Sprites/Haruhi/HaruhiCrossedSmile1.png"
    image Haruhi Crossed Smile2 = "Sprites/Haruhi/HaruhiCrossedSmile2.png"
    image Haruhi Crossed Smile3 = "Sprites/Haruhi/HaruhiCrossedSmile3.png"
    image Haruhi Crossed Sigh1 = "Sprites/Haruhi/HaruhiCrossedSigh1.png"
    image Haruhi Crossed Sigh2 = "Sprites/Haruhi/HaruhiCrossedSigh2.png"
    image Haruhi Crossed Tsun1 = "Sprites/Haruhi/HaruhiCrossedTsun1.png"
    image Haruhi Crossed Tsun2 = "Sprites/Haruhi/HaruhiCrossedTsun2.png"
    
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
    image Haruhi Crossed Casual Pout2 = "Sprites/Haruhi/HaruhiCrossedCasualPout2.png"
    image Haruhi Crossed Casual Eyeroll1 = "Sprites/Haruhi/HaruhiCrossedCasualEyeroll1.png"
    image Haruhi Crossed Casual Quest1 = "Sprites/Haruhi/HaruhiCrossedCasualQuestion1.png"
    image Haruhi Crossed Casual Grin1 = "Sprites/Haruhi/HaruhiCrossedCasualGrin1.png"
    image Haruhi Crossed Casual Worry1 = "Sprites/Haruhi/HaruhiCrossedCasualWorry1.png"
    image Haruhi Crossed Casual Worry2 = "Sprites/Haruhi/HaruhiCrossedCasualWorry2.png"
    image Haruhi Crossed Casual Smile1 = "Sprites/Haruhi/HaruhiCrossedCasualSmile1.png"
    image Haruhi Crossed Casual Smile2 = "Sprites/Haruhi/HaruhiCrossedCasualSmile2.png"
    image Haruhi Crossed Casual Smile3 = "Sprites/Haruhi/HaruhiCrossedCasualSmile3.png"
    image Haruhi Crossed Casual Sigh1 = "Sprites/Haruhi/HaruhiCrossedCasualSigh1.png"
    image Haruhi Crossed Casual Sigh2 = "Sprites/Haruhi/HaruhiCrossedCasualSigh2.png"
    image Haruhi Crossed Casual Tsun1 = "Sprites/Haruhi/HaruhiCrossedCasualTsun1.png"
    image Haruhi Crossed Casual Tsun2 = "Sprites/Haruhi/HaruhiCrossedCasualTsun2.png"
    
    image Haruhi Point Amuse1 = "Sprites/Haruhi/HaruhiPointAmused1.png"
    image Haruhi Point Ang1 = "Sprites/Haruhi/HaruhiPointAngry1.png"
    image Haruhi Point Hap1 = "Sprites/Haruhi/HaruhiPointHappy1.png"
    image Haruhi Point Scold1 = "Sprites/Haruhi/HaruhiPointScold1.png"
    
    image Haruhi Point Casual Amuse1 = "Sprites/Haruhi/HaruhiPointCasualAmused1.png"
    image Haruhi Point Casual Surpr1 = "Sprites/Haruhi/HaruhiPointCasualSurprised1.png"
    image Haruhi Point Casual Ang1 = "Sprites/Haruhi/HaruhiPointCasualAngry1.png"
    image Haruhi Point Casual Hap1 = "Sprites/Haruhi/HaruhiPointCasualHappy1.png"
    image Haruhi Point Casual Scold1 = "Sprites/Haruhi/HaruhiPointCasualScold1.png"
    
    image Haruhi Hips Ang1 = "Sprites/Haruhi/HaruhiHipsAngry1.png"
    image Haruhi Hips Ang2 = "Sprites/Haruhi/HaruhiHipsAngry2.png"
    image Haruhi Hips Ang3 = "Sprites/Haruhi/HaruhiHipsAngry3.png"
    image Haruhi Hips Ang4 = "Sprites/Haruhi/HaruhiHipsAngry4.png"
    image Haruhi Hips Sigh1 = "Sprites/Haruhi/HaruhiHipsSigh1.png"
    
    image Haruhi Hips Casual Ang1 = "Sprites/Haruhi/HaruhiHipsCasualAngry1.png"
    image Haruhi Hips Casual Ang2 = "Sprites/Haruhi/HaruhiHipsCasualAngry2.png"
    image Haruhi Hips Casual Ang3 = "Sprites/Haruhi/HaruhiHipsCasualAngry3.png"
    image Haruhi Hips Casual Ang4 = "Sprites/Haruhi/HaruhiHipsCasualAngry4.png"
    image Haruhi Hips Casual Sigh1 = "Sprites/Haruhi/HaruhiHipsCasualSigh1.png"
    
    image Hblush = "Sprites/Haruhi/HaruhiSideBlush1.png"
    image Hblush Casual = "Sprites/Haruhi/HaruhiSideCasualBlush1.png"
    image Hblush Hips = "Sprites/Haruhi/HblushHips.png"
    image Hblush Hips = "Sprites/Haruhi/HblushHipsCasual.png"
    image Htears ="Sprites/Haruhi/HTearsSide1.png"
    image Htears Casual = "Sprites/Haruhi/HTearsSideCasual1.png"
    # image Hblush Crossed = "Sprites/Haruhi/HBlushCrossed.png"
    image Hblush Crossed = "Sprites/Haruhi/HBlushCrossed copy.png"
    
    #Kyon Sprites
    image Kyon Ser1 = "Sprites/Kyon/KyonSerious1.png"
    image Kyon Ser2 = "Sprites/Kyon/KyonSerious2.png"
    image Kyon Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Ser3 = "Sprites/Kyon/KyonSerious3.png"
    image Kyon Sigh1 = "Sprites/Kyon/KyonSigh1.png"
    image Kyon Sigh2 = "Sprites/Kyon/KyonSigh2.png"
    image Kyon Sigh3 = "Sprites/Kyon/KyonSigh3.png"
    image Kyon Sigh4 = "Sprites/Kyon/KyonSigh4.png"
    image Kyon Sigh5 = "Sprites/Kyon/KyonSigh5.png"
    image Kyon Neutral1 = "Sprites/Kyon/KyonNeutral1.png"
    image Kyon Neutral2 = "Sprites/Kyon/KyonNeutral2.png"
    image Kyon Neutral3 = "Sprites/Kyon/KyonNeutral3.png"
    image Kyon Neutral4 = "Sprites/Kyon/KyonNeutral4.png"
    image Kyon Neutral5 = "Sprites/Kyon/KyonNeutral5.png"
    image Kyon Ang1 = "Sprites/Kyon/KyonAngry1.png"
    image Kyon Ang2 = "Sprites/Kyon/KyonAngry2.png"
    image Kyon Ang3 = "Sprites/Kyon/KyonAngry3.png"
    image Kyon Ang4 = "Sprites/Kyon/KyonAngry4.png"
    image Kyon Pain1 = "Sprites/Kyon/KyonPained1.png"
    image Kyon Pain2 = "Sprites/Kyon/KyonPained2.png"
    image Kyon Smile1 = "Sprites/Kyon/KyonSmile1.png"
    image Kyon Smile2 = "Sprites/Kyon/KyonSmile2.png"
    image Kyon Smile3 = "Sprites/Kyon/KyonSmile3.png"
    image Kyon Smile4 = "Sprites/Kyon/KyonSmile4.png"
    image Kyon Smile5 = "Sprites/Kyon/KyonSmile5.png"
    image Kyon Worry1 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Worry2 = "Sprites/Kyon/KyonWorry2.png"
    image Kyon Worry3 = "Sprites/Kyon/KyonWorry3.png"
    image Kyon Puzzle1 = "Sprites/Kyon/KyonPuzzled1.png"
    image Kyon Sup1 = "Sprites/Kyon/KyonSurprised1.png"
    image Kyon Sup2 = "Sprites/Kyon/KyonSurprised2.png"
    image Kyon Unhap1 ="Sprites/Kyon/KyonUnhappy1.png"
    image Kyon Unhap2 ="Sprites/Kyon/KyonUnhappy2.png"
    image Kyon Unhap3 ="Sprites/Kyon/KyonUnhappy3.png"
    image Kyon Unhap4 ="Sprites/Kyon/KyonUnhappy4.png"
    image Kyon Unhap5 ="Sprites/Kyon/KyonUnhappy5.png"
    
    image Kyon Casual Ser1 = "Sprites/Kyon/KyonCasualSerious1.png"
    image Kyon Casual Ser2 = "Sprites/Kyon/KyonCasualSerious2.png"
    image Kyon Casual Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonCasualSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Casual Ser3 = "Sprites/Kyon/KyonCasualSerious3.png"
    image Kyon Casual Sigh1 = "Sprites/Kyon/KyonCasualSigh1.png"
    image Kyon Casual Sigh2 = "Sprites/Kyon/KyonCasualSigh2.png"
    image Kyon Casual Sigh3 = "Sprites/Kyon/KyonCasualSigh3.png"
    image Kyon Casual Sigh4 = "Sprites/Kyon/KyonCasualSigh4.png"
    image Kyon Casual Sigh5 = "Sprites/Kyon/KyonCasualSigh5.png"
    image Kyon Casual Neutral1 = "Sprites/Kyon/KyonCasualNeutral1.png"
    image Kyon Casual Neutral2 = "Sprites/Kyon/KyonCasualNeutral2.png"
    image Kyon Casual Neutral3 = "Sprites/Kyon/KyonCasualNeutral3.png"
    image Kyon Casual Neutral4 = "Sprites/Kyon/KyonCasualNeutral4.png"
    image Kyon Casual Ang1 = "Sprites/Kyon/KyonCasualAngry1.png"
    image Kyon Casual Ang2 = "Sprites/Kyon/KyonCasualAngry2.png"
    image Kyon Casual Ang3 = "Sprites/Kyon/KyonCasualAngry3.png"
    image Kyon Casual Ang4 = "Sprites/Kyon/KyonCasualAngry4.png"
    image Kyon Casual Pain1 = "Sprites/Kyon/KyonCasualPained1.png"
    image Kyon Casual Pain2 = "Sprites/Kyon/KyonCasualPained2.png"
    image Kyon Casual Smile1 = "Sprites/Kyon/KyonCasualSmile1.png"
    image Kyon Casual Smile2 = "Sprites/Kyon/KyonCasualSmile2.png"
    image Kyon Casual Smile3 = "Sprites/Kyon/KyonCasualSmile3.png"
    image Kyon Casual Smile4 = "Sprites/Kyon/KyonCasualSmile4.png"
    image Kyon Casual Smile5 = "Sprites/Kyon/KyonCasualSmile5.png"
    image Kyon Casual Worry1 = "Sprites/Kyon/KyonCasualWorry1.png"
    image Kyon Casual Worry2 = "Sprites/Kyon/KyonCasualWorry2.png"
    image Kyon Casual Worry3 = "Sprites/Kyon/KyonCasualWorry3.png"
    image Kyon Casual Puzzle1 = "Sprites/Kyon/KyonCasualPuzzled1.png"
    image Kyon Casual Sup1 = "Sprites/Kyon/KyonCasualSurprised1.png"
    image Kyon Casual Sup2 = "Sprites/Kyon/KyonCasualSurprised2.png"
    image Kyon Casual Unhap1 ="Sprites/Kyon/KyonCasualUnhappy1.png"
    image Kyon Casual Unhap2 ="Sprites/Kyon/KyonCasualUnhappy2.png"
    image Kyon Casual Unhap3 ="Sprites/Kyon/KyonCasualUnhappy3.png"
    image Kyon Casual Unhap4 ="Sprites/Kyon/KyonCasualUnhappy4.png"
    image Kyon Casual Unhap5 ="Sprites/Kyon/KyonCasualUnhappy5.png"
    
    image Ksweat = "Sprites/Kyon/KyonSweat1.png"
    image Skinsuit = "Sprites/Kyon/KyonSkinsuitTemplate.png"
    image Skinsuit Bright = im.MatrixColor("Sprites/Kyon/KyonSkinsuitTemplate.png",
                                       im.matrix.brightness(.5))
    image Coat Bright = im.MatrixColor("Sprites/Kyon/KyonCoat.png",
                                       im.matrix.brightness(.5))
    image Coat = "Sprites/Kyon/KyonCoat.png"

    image Kyon Ser1 Flip = im.Flip("Sprites/Kyon/KyonSerious1.png", horizontal=True)
    image Kyon Ser3 Flip = im.Flip("Sprites/Kyon/KyonSerious3.png", horizontal=True)
    image Kyon Ang1 Flip = im.Flip("Sprites/Kyon/KyonAngry1.png", horizontal=True)
    
    image KTears = "Sprites/Kyon/Ktears.png"
    image KBlush = "Sprites/Kyon/KBlush.png"
    image KBlush Casual = "Sprites/Kyon/KBlushCasual.png"
    image KPaper = "Sprites/Kyon/KyonPaper.png"
    
    
    #Asakura Sprites
    image Stabby = "Sprites/Asakura/AsakuraStabTest.png"
    
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
        5.0
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
    
    image Yuki Chair1 = "Sprites/Yuki/YukiChair1.png"
    image Yuki Chair2 = "Sprites/Yuki/YukiChair2.png"
    image Yuki Chair3 = "Sprites/Yuki/YukiChair3.png"
    image Yuki Chair4 = "Sprites/Yuki/YukiChair4.png"
    
    
    image Yuki Right Neutral1 = "Sprites/Yuki/YukiRightNeutral1.png"
    image Yuki Right Neutral2 = "Sprites/Yuki/YukiRightNeutral2.png"
    image Yuki Right Talk1 = "Sprites/Yuki/YukiRightTalk1.png"
    image Yuki Right Talk2 = "Sprites/Yuki/YukiRightTalk2.png"
    
    image Yuki Right Casual Neutral1 = "Sprites/Yuki/YukiRightCasualNeutral1.png"
    image Yuki Right Casual Neutral2 = "Sprites/Yuki/YukiRightCasualNeutral2.png"
    image Yuki Right Casual Talk1 = "Sprites/Yuki/YukiRightCasualTalk1.png"
    image Yuki Right Casual Talk2 = "Sprites/Yuki/YukiRightCasualTalk2.png"
    
    image YBook = "Sprites/Yuki/YukiBook.png"
    
    image Yuki Side Blink:
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSideSad1.png"
        0.1
        "Sprites/Yuki/YukiSideEyesClosed1.png"
        0.1
        "Sprites/Yuki/YukiSideSad1.png"
        0.1
        "Sprites/Yuki/YukiSide1.png"
        4.0
        repeat
    image Yuki Side SmallBlink:
        "Sprites/Yuki/YukiSide1.png"
        0.1
        "Sprites/Yuki/YukiSideEyesClosed1.png"
        0.15
        "Sprites/Yuki/YukiSide1.png"
        3
        repeat
   
    # Mikuru Sprites 
    image Mikuru Neutral1 = "Sprites/Mikuru/MikuruNeutral1.png"
    image Mikuru Neutral2 = "Sprites/Mikuru/MikuruNeutral2.png"
    image Mikuru Sad1 = "Sprites/Mikuru/MikuruSad1.png"
    image Mikuru Sad2 = "Sprites/Mikuru/MikuruSad2.png"
    image Mikuru Sigh1 = "Sprites/Mikuru/MikuruSigh1.png"
    image Mikuru Ser1 = "Sprites/Mikuru/MikuruSerious1.png"
    image Mikuru Ser2 = "Sprites/Mikuru/MikuruSerious2.png"
    image Mikuru Ser3 = "Sprites/Mikuru/MikuruSerious3.png"
    image Mikuru Smile1 = "Sprites/Mikuru/MikuruSmile1.png"
    image Mikuru Smile2 = "Sprites/Mikuru/MikuruSmile2.png"
    image Mikuru Quest1 = "Sprites/Mikuru/MikuruQuestion1.png"
    image Mikuru Quest2 = "Sprites/Mikuru/MikuruQuestion2.png"
    image Mikuru Unhap1 = "Sprites/Mikuru/MikuruUnhappy1.png"
    image Mikuru Unhap2 = "Sprites/Mikuru/MikuruUnhappy2.png"
    image MBlush1 = "Sprites/Mikuru/MBlush1.png"
  
    image Mikuru Casual Neutral1 = "Sprites/Mikuru/MikuruCasualNeutral1.png"
    image Mikuru Casual Neutral2 = "Sprites/Mikuru/MikuruCasualNeutral2.png"
    image Mikuru Casual Sad1 = "Sprites/Mikuru/MikuruCasualSad1.png"
    image Mikuru Casual Sad2 = "Sprites/Mikuru/MikuruCasualSad2.png"
    image Mikuru Casual Sigh1 = "Sprites/Mikuru/MikuruCasualSigh1.png"
    image Mikuru Casual Ser1 = "Sprites/Mikuru/MikuruCasualSerious1.png"
    image Mikuru Casual Ser2 = "Sprites/Mikuru/MikuruCasualSerious2.png"
    image Mikuru Casual Ser3 = "Sprites/Mikuru/MikuruCasualSerious3.png"
    image Mikuru Casual Smile1 = "Sprites/Mikuru/MikuruCasualSmile1.png"
    image Mikuru Casual Smile2 = "Sprites/Mikuru/MikuruCasualSmile2.png"
    image Mikuru Casual Quest1 = "Sprites/Mikuru/MikuruCasualQuestion1.png"
    image Mikuru Casual Quest2 = "Sprites/Mikuru/MikuruCasualQuestion2.png"
    image Mikuru Casual Unhap1 = "Sprites/Mikuru/MikuruCasualUnhappy1.png"
    image Mikuru Casual Unhap2 = "Sprites/Mikuru/MikuruCasualUnhappy2.png"
    image MBlush1 Casual = "Sprites/Mikuru/MBlushCasual1.png"
    
    image Mikuru Maid Neutral1 = "Sprites/Mikuru/MikuruMaidNeutral1.png"
    image Mikuru Maid Neutral2 = "Sprites/Mikuru/MikuruMaidNeutral2.png"
    image Mikuru Maid Sad1 = "Sprites/Mikuru/MikuruMaidSad1.png"
    image Mikuru Maid Sad2 = "Sprites/Mikuru/MikuruMaidSad2.png"
    image Mikuru Maid Sigh1 = "Sprites/Mikuru/MikuruMaidSigh1.png"
    image Mikuru Maid Ser1 = "Sprites/Mikuru/MikuruMaidSerious1.png"
    image Mikuru Maid Ser2 = "Sprites/Mikuru/MikuruMaidSerious2.png"
    image Mikuru Maid Ser3 = "Sprites/Mikuru/MikuruMaidSerious3.png"
    image Mikuru Maid Smile1 = "Sprites/Mikuru/MikuruMaidSmile1.png"
    image Mikuru Maid Smile2 = "Sprites/Mikuru/MikuruMaidSmile2.png"
    image Mikuru Maid Quest1 = "Sprites/Mikuru/MikuruMaidQuestion1.png"
    image Mikuru Maid Quest2 = "Sprites/Mikuru/MikuruMaidQuestion2.png"
    image Mikuru Maid Unhap1 = "Sprites/Mikuru/MikuruMaidUnhappy1.png"
    image Mikuru Maid Unhap2 = "Sprites/Mikuru/MikuruMaidUnhappy2.png"
    image MBlush1 Maid = "Sprites/Mikuru/MBlushMaid1.png"
    image MTray Maid ="Sprites/Mikuru/MTrayMaid.png"
    
    image Mikuru Think Quest1 = "Sprites/Mikuru/MikuruThinkQuestion1.png"
    image Mikuru Think Quest2 = "Sprites/Mikuru/MikuruThinkQuestion2.png"
    image Mikuru Think Sad1 = "Sprites/Mikuru/MikuruThinkSad1.png"
    image Mikuru Think Sad2 = "Sprites/Mikuru/MikuruThinkSad2.png"
    image Mikuru Think Sup1 = "Sprites/Mikuru/MikuruThinkSurprised1.png"
    
    image Mikuru Think Casual Quest1 = "Sprites/Mikuru/MikuruThinkCasualQuestion1.png"
    image Mikuru Think Casual Quest2 = "Sprites/Mikuru/MikuruThinkCasualQuestion2.png"
    image Mikuru Think Casual Sad1 = "Sprites/Mikuru/MikuruThinkCasualSad1.png"
    image Mikuru Think Casual Sad2 = "Sprites/Mikuru/MikuruThinkCasualSad2.png"
    image Mikuru Think Casual Sup1 = "Sprites/Mikuru/MikuruThinkCasualSurprised1.png"
    
    image Mikuru Think Maid Quest1 = "Sprites/Mikuru/MikuruThinkMaidQuestion1.png"
    image Mikuru Think Maid Quest2 = "Sprites/Mikuru/MikuruThinkMaidQuestion2.png"
    image Mikuru Think Maid Sad1 = "Sprites/Mikuru/MikuruThinkMaidSad1.png"
    image Mikuru Think Maid Sad2 = "Sprites/Mikuru/MikuruThinkMaidSad2.png"
    image Mikuru Think Maid Sup1 = "Sprites/Mikuru/MikuruThinkMaidSurprised1.png"
    image MTears Think = "Sprites/Mikuru/MTearsThink1.png"
    
    image Mikuru Think Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkQuestion1.png", horizontal=True)
    image Mikuru Think Casual Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkCasualQuestion1.png", horizontal=True)
    image Mikuru Think Maid Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkMaidQuestion1.png", horizontal=True)
    
    image Mikuru Cower Nervous1 = "Sprites/Mikuru/MikuruCowerNervous1.png"
    image Mikuru Cower Nervous2 = "Sprites/Mikuru/MikuruCowerNervous2.png"
    image Mikuru Cower Nervous3 = "Sprites/Mikuru/MikuruCowerNervous3.png"
    image Mikuru Cower Neutral1 = "Sprites/Mikuru/MikuruCowerNeutral1.png"
    image Mikuru Cower Sup1 = "Sprites/Mikuru/MikuruCowerSurprised1.png"
    image Mikuru Cower Sigh1 = "Sprites/Mikuru/MikuruCowerSigh1.png"
    image Mikuru Cower Wince1 = "Sprites/Mikuru/MikuruCowerWince1.png"
    image Mikuru Cower Smile1 ="Sprites/Mikuru/MikuruCowerSmile1.png"
    image MBlush Cower = "Sprites/Mikuru/MikuruCowerBlush1.png"
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
    
    image Mikuru Cower Face Wince1 = "Sprites/Mikuru/MikuruCowerFaceWince1.png"
    image Mikuru Cower Face Nervous1 = "Sprites/Mikuru/MikuruCowerFaceNervous1.png"
    image Mikuru Cower Face Nervous2 = "Sprites/Mikuru/MikuruCowerFaceNervous2.png"
    image Mikuru Cower Face Nervous3 = "Sprites/Mikuru/MikuruCowerFaceNervous3.png"
    image Mikuru Cower Face Smile1 = "Sprites/Mikuru/MikuruCowerFaceSmile1.png"
    image Mikuru Cower Face Sup1 = "Sprites/Mikuru/MikuruCowerFaceSurprised1.png"
    image Mikuru Cower Face Sup2 = "Sprites/Mikuru/MikuruCowerFaceSurprised2.png"
    image Mikuru Cower Face Unhap1 = "Sprites/Mikuru/MikuruCowerFaceUnhappy1.png"
    image Mikuru Cower Face Worry1 = "Sprites/Mikuru/MikuruCowerFaceWorry1.png"
    image Mikuru Cower Sigh1 = "Sprites/Mikuru/MikuruCowerSigh1.png"
    image MBlush Cower Face = "Sprites/Mikuru/MBlushFace.png"

    
    image MikuruBig Grin1 = "Sprites/MikuruBig/MikuruBigGrin1.png"
    image MikuruBig Grin2 = "Sprites/MikuruBig/MikuruBigGrin2.png"
    image MikuruBig Hap1 = "Sprites/MikuruBig/MikuruBigHappy1.png"
    image MikuruBig Hap2 = "Sprites/MikuruBig/MikuruBigHappy2.png"
    image MikuruBig Hap3 = "Sprites/MikuruBig/MikuruBigHappy3.png"
    image MikuruBig Hap4 = "Sprites/MikuruBig/MikuruBigHappy4.png"
    image MikuruBig Laugh1 = "Sprites/MikuruBig/MikuruBigLaugh1.png"
    image MikuruBig Neutral1 = "Sprites/MikuruBig/MikuruBigNeutral1.png"
    image MikuruBig Neutral2 = "Sprites/MikuruBig/MikuruBigNeutral2.png"
    image MikuruBig Quest1 = "Sprites/MikuruBig/MikuruBigQuestion1.png"
    image MikuruBig Sad1 = "Sprites/MikuruBig/MikuruBigSad1.png"
    image MikuruBig Ser1 = "Sprites/MikuruBig/MikuruBigSerious1.png"
    image MikuruBig Ser2 = "Sprites/MikuruBig/MikuruBigSerious2.png"
    image MikuruBig Sigh1 = "Sprites/MikuruBig/MikuruBigSigh1.png"
    image MikuruBig Smile1 = "Sprites/MikuruBig/MikuruBigSmile1.png"
    image MikuruBig Smile2 = "Sprites/MikuruBig/MikuruBigSmile2.png"
    image MikuruBig Sup1 = "Sprites/MikuruBig/MikuruBigSurprised1.png"
    image MikuruBig Sup2 = "Sprites/MikuruBig/MikuruBigSurprised2.png"
    image MikuruBig Worry1 = "Sprites/MikuruBig/MikuruBigWorry1.png"
    image MikuruBig Worry2 = "Sprites/MikuruBig/MikuruBigWorry2.png"
    
    image MikuruBig Wink:
        "Sprites/MikuruBig/MikuruBigHappy1.png"
        0.5
        "Sprites/MikuruBig/MikuruBigHappy3.png"
    
    image MikuruBig Grinwink:
        "Sprites/MikuruBig/MikuruBigGrin2.png"
        0.5
        "Sprites/MikuruBig/MikuruBigGrin1.png"
    
    image MKiss = "Sprites/MikuruBig/MKiss.png"
    
    #Tsuruya Sprites
    image Tsuruya Ang1 = "Sprites/Tsuruya/TsuruyaAngry1.png"
    image Tsuruya Ang2 = "Sprites/Tsuruya/TsuruyaAngry2.png"
    image Tsuruya Grin1 = "Sprites/Tsuruya/TsuruyaGrin1.png"
    image Tsuruya Grin2 = "Sprites/Tsuruya/TsuruyaGrin2.png"
    image Tsuruya Grin3 = "Sprites/Tsuruya/TsuruyaGrin3.png"
    image Tsuruya Grin4 = "Sprites/Tsuruya/TsuruyaGrin4.png"
    image Tsuruya Grin5 = "Sprites/Tsuruya/TsuruyaGrin5.png"
    image Tsuruya Hap1 = "Sprites/Tsuruya/TsuruyaHappy1.png"
    image Tsuruya Hap2 = "Sprites/Tsuruya/TsuruyaHappy2.png"
    image Tsuruya Hap3 = "Sprites/Tsuruya/TsuruyaHappy3.png"
    image Tsuruya Hap4 = "Sprites/Tsuruya/TsuruyaHappy4.png"
    image Tsuruya Hap5 = "Sprites/Tsuruya/TsuruyaHappy5.png"
    image Tsuruya Hap6 = "Sprites/Tsuruya/TsuruyaHappy6.png"
    image Tsuruya Laugh1 = "Sprites/Tsuruya/TsuruyaLaugh1.png"
    image Tsuruya Laugh2 = "Sprites/Tsuruya/TsuruyaLaugh2.png"
    image Tsuruya Quest1 = "Sprites/Tsuruya/TsuruyaQuestion1.png"
    image Tsuruya Sigh1 = "Sprites/Tsuruya/TsuruyaSigh1.png"
    image Tsuruya Smile1 = "Sprites/Tsuruya/TsuruyaSmile1.png"
    image Tsuruya Smile2 = "Sprites/Tsuruya/TsuruyaSmile2.png"
    image Tsuruya Smile3 = "Sprites/Tsuruya/TsuruyaSmile3.png"
    image Tsuruya Smile4 = "Sprites/Tsuruya/TsuruyaSmile4.png"
    image Tsuruya Sup1 = "Sprites/Tsuruya/TsuruyaSurprised1.png"
    image Tsuruya Worry1 = "Sprites/Tsuruya/TsuruyaWorry1.png"
    image Tsuruya Worry2 = "Sprites/Tsuruya/TsuruyaWorry2.png"    
    image Tsuruya Neutral1 = "Sprites/Tsuruya/TsuruyaNeutral1.png"
    image Tsuruya Susp1 = "Sprites/Tsuruya/TsuruyaSuspicious1.png"
    image Tsuruya Ser1 = "Sprites/Tsuruya/TsuruyaSerious1.png"
    image Tsuruya Sad1 = "Sprites/Tsuruya/TsuruyaSad1.png"
    
    image Tsuruya Wave Grin1 = "Sprites/Tsuruya/TsuruyaWaveGrin1.png"
    image Tsuruya Wave Grin2 = "Sprites/Tsuruya/TsuruyaWaveGrin2.png"
    image Tsuruya Wave Hap1 = "Sprites/Tsuruya/TsuruyaWaveHappy1.png"
    image Tsuruya Wave Hap2 = "Sprites/Tsuruya/TsuruyaWaveHappy2.png"
    image Tsuruya Wave Hap3 = "Sprites/Tsuruya/TsuruyaWaveHappy3.png"
    image Tsuruya Wave Hap4 = "Sprites/Tsuruya/TsuruyaWaveHappy4.png"
    image Tsuruya Wave Hap5 = "Sprites/Tsuruya/TsuruyaWaveHappy5.png"
    image Tsuruya Wave Hap6 = "Sprites/Tsuruya/TsuruyaWaveHappy6.png"
    image Tsuruya Wave Quest1 = "Sprites/Tsuruya/TsuruyaWaveQuestion1.png"
    image Tsuruya Wave Smile1 = "Sprites/Tsuruya/TsuruyaWaveSmile1.png"
    image Tsuruya Wave Smile2 = "Sprites/Tsuruya/TsuruyaWaveSmile2.png"
    
    #Kanae Sprites
    image Kanae Hap1 = "Sprites/Kanae/KanaeHappy1.png"
    image Kanae Hap2 = "Sprites/Kanae/KanaeHappy2.png"
    image Kanae Hap3 = "Sprites/Kanae/KanaeHappy3.png"
    image Kanae Neutral1 = "Sprites/Kanae/KanaeNeutral1.png"
    image Kanae Quest1 = "Sprites/Kanae/KanaeQuestion1.png"
    image Kanae Sad1 = "Sprites/Kanae/KanaeSad1.png"
    image Kanae Sad2 = "Sprites/Kanae/KanaeSad2.png"
    image Kanae Sad3 = "Sprites/Kanae/KanaeSad3.png"
    image Kanae Sad4 = "Sprites/Kanae/KanaeSad4.png"
    image Kanae Sad5 = "Sprites/Kanae/KanaeSad5.png"
    image Kanae Smile1 = "Sprites/Kanae/KanaeSmile1.png"
    image Kanae Smile2 = "Sprites/Kanae/KanaeSmile2.png"
    image Kanae Smile3 = "Sprites/Kanae/KanaeSmile3.png"
    image Kanae Sup1 = "Sprites/Kanae/KanaeSurprised1.png"
    image Kanae Sup2 = "Sprites/Kanae/KanaeSurprised2.png"
    image Kanae Unhap1 = "Sprites/Kanae/KanaeUnhappy1.png"
    image Kanae Unhap2 = "Sprites/Kanae/KanaeUnhappy2.png"
    image Kanae Unhap3 = "Sprites/Kanae/KanaeUnhappy3.png"
    image Kanae Wince1 = "Sprites/Kanae/KanaeWince1.png"
    image Kanae Wince2 = "Sprites/Kanae/KanaeWince2.png"
    image Kanae Worry1 = "Sprites/Kanae/KanaeWorry1.png"
    image Kanae Worry2 = "Sprites/Kanae/KanaeWorry2.png"
    image Kanae Worry3 = "Sprites/Kanae/KanaeWorry3.png"
    
    image Kanae Face Hap1 =  "Sprites/Kanae/KanaeFaceHappy1.png"
    image Kanae Face Quest1 =  "Sprites/Kanae/KanaeFaceQuestion1.png"
    image Kanae Face Smile1 =  "Sprites/Kanae/KanaeFaceSmile1.png"
    image Kanae Face Smile2  = "Sprites/Kanae/KanaeFaceSmile2.png"
    image Kanae Face Sup1  = "Sprites/Kanae/KanaeFaceSurprised1.png"
    image Kanae Face Worry1 =  "Sprites/Kanae/KanaeFaceWorry1.png"
    
    image KABlush = "Sprites/Kanae/KanaeBlush.png"
    image KABlush Face = "Sprites/Kanae/KanaeFaceBlush.png"
    
    
    #Koizumi Sprites
    image Koizumi Shrug Sigh1 = "Sprites/Koizumi/KoizumiShrugSigh1.png"
    image Koizumi Shrug Smile1 = "Sprites/Koizumi/KoizumiShrugSmile1.png"
    
    image Koizumi Shrug Casual Sigh1 = "Sprites/Koizumi/KoizumiShrugCasualSigh1.png"
    image Koizumi Shrug Casual Smile1 = "Sprites/Koizumi/KoizumiShrugCasualSmile1.png"
    
    image Koizumi Think Ser1 = "Sprites/Koizumi/KoizumiThinkSerious1.png"
    image Koizumi Think Ser2 = "Sprites/Koizumi/KoizumiThinkSerious2.png"
    image Koizumi Think Ser3 = "Sprites/Koizumi/KoizumiThinkSerious3.png"
    image Koizumi Think Ser4 = "Sprites/Koizumi/KoizumiThinkSerious4.png"
    image Koizumi Think Grin1 = "Sprites/Koizumi/KoizumiThinkGrin1.png"
    image Koizumi Think Grin2 = "Sprites/Koizumi/KoizumiThinkGrin2.png"
    image Koizumi Think Sup1 = "Sprites/Koizumi/KoizumiThinkSurprised1.png"
    image Koizumi Think Smile1 = "Sprites/Koizumi/KoizumiThinkSmile1.png"
    image Koizumi Think Sigh1 = "Sprites/Koizumi/KoizumiThinkSigh1.png"
    
    image Koizumi Think Casual Ser1 = "Sprites/Koizumi/KoizumiThinkCasualSerious1.png"
    image Koizumi Think Casual Ser2 = "Sprites/Koizumi/KoizumiThinkCasualSerious2.png"
    image Koizumi Think Casual Ser3 = "Sprites/Koizumi/KoizumiThinkCasualSerious3.png"
    image Koizumi Think Casual Ser4 = "Sprites/Koizumi/KoizumiThinkCasualSerious4.png"
    image Koizumi Think Casual Grin1 = "Sprites/Koizumi/KoizumiThinkCasualGrin1.png"
    image Koizumi Think Casual Grin2 = "Sprites/Koizumi/KoizumiThinkCasualGrin2.png"
    image Koizumi Think Casual Sup1 = "Sprites/Koizumi/KoizumiThinkCasualSurprised1.png"
    image Koizumi Think Casual Smile1 = "Sprites/Koizumi/KoizumiThinkCasualSmile1.png"
    image Koizumi Think Casual Sigh1 = "Sprites/Koizumi/KoizumiThinkCasualSigh1.png"
    
    image Koizumi Crossed Ser1 = "Sprites/Koizumi/KoizumiCrossedSerious1.png"
    image Koizumi Crossed Ser2 = "Sprites/Koizumi/KoizumiCrossedSerious2.png"
    image Koizumi Crossed Smile1 = "Sprites/Koizumi/KoizumiCrossedSmile1.png"
    image Koizumi Crossed Smile2 = "Sprites/Koizumi/KoizumiCrossedSmile2.png"
    image Koizumi Crossed Uneasy1 = "Sprites/Koizumi/KoizumiCrossedUneasy1.png"
    image Koizumi Crossed Uneasy2 = "Sprites/Koizumi/KoizumiCrossedUneasy2.png"
    image Koizumi Crossed Uneasy3 = "Sprites/Koizumi/KoizumiCrossedUneasy3.png"
    image Koizumi Crossed Sigh1 = "Sprites/Koizumi/KoizumiCrossedSigh1.png"
    image Koizumi Crossed Sigh2 = "Sprites/Koizumi/KoizumiCrossedSigh2.png"
    image Koizumi Crossed Neutral1 = "Sprites/Koizumi/KoizumiCrossedNeutral1.png"
    
    image Koizumi Crossed Casual Ser1 = "Sprites/Koizumi/KoizumiCrossedCasualSerious1.png"
    image Koizumi Crossed Casual Ser2 = "Sprites/Koizumi/KoizumiCrossedCasualSerious2.png"
    image Koizumi Crossed Casual Smile1 = "Sprites/Koizumi/KoizumiCrossedCasualSmile1.png"
    image Koizumi Crossed Casual Smile2 = "Sprites/Koizumi/KoizumiCrossedCasualSmile2.png"
    image Koizumi Crossed Casual Uneasy1 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy1.png"
    image Koizumi Crossed Casual Uneasy2 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy2.png"
    image Koizumi Crossed Casual Uneasy3 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy3.png"
    image Koizumi Crossed Casual Sigh1 = "Sprites/Koizumi/KoizumiCrossedCasualSigh1.png"
    image Koizumi Crossed Casual Sigh2 = "Sprites/Koizumi/KoizumiCrossedCasualSigh2.png"
    image Koizumi Crossed Casual Neutral1 = "Sprites/Koizumi/KoizumiCrossedCasualNeutral1.png"
    
    #Taniguchi Sprites
    image Taniguchi Grin1 = "Sprites/Taniguchi/TaniguchiGrin1.png"
    image Taniguchi Sup1 = "Sprites/Taniguchi/TaniguchiSurprised1.png"
    image Taniguchi Sup2 = "Sprites/Taniguchi/TaniguchiSurprised2.png"
    image Taniguchi Smile1 = "Sprites/Taniguchi/TaniguchiSmile1.png"
    image Taniguchi Hap1 = "Sprites/Taniguchi/TaniguchiHappy1.png"
    image Taniguchi Hap2 = "Sprites/Taniguchi/TaniguchiHappy2.png"
    image Taniguchi Ser1 = "Sprites/Taniguchi/TaniguchiSerious1.png"
    image Taniguchi Ser2 = "Sprites/Taniguchi/TaniguchiSerious2.png"
    image Taniguchi Sigh1 = "Sprites/Taniguchi/TaniguchiSigh1.png"
    image Taniguchi Sigh2 = "Sprites/Taniguchi/TaniguchiSigh2.png"
    image Taniguchi Unhap1 = "Sprites/Taniguchi/TaniguchiUnhappy1.png"
    
    #Kunikida Sprites
    image Kunikida Neutral1 = "Sprites/Kunikida/KunikidaNeutral1.png"
    image Kunikida Neutral2 = "Sprites/Kunikida/KunikidaNeutral2.png"
    image Kunikida Neutral3 = "Sprites/Kunikida/KunikidaNeutral3.png"
    image Kunikida Smile1 ="Sprites/Kunikida/KunikidaSmile1.png"
    image Kunikida Smile2 ="Sprites/Kunikida/KunikidaSmile2.png"
    image Kunikida Ser1 = "Sprites/Kunikida/KunikidaSerious1.png"
    image Kunikida Ser2 = "Sprites/Kunikida/KunikidaSerious2.png"



    #Nonoko Sprites
    image Nonoko Smile1 = "Sprites/Nonoko/NonokoSmile1.png"
    image Nonoko Sup1 = "Sprites/Nonoko/NonokoSurprised1.png"
    image Nonoko Pout1 = "Sprites/Nonoko/NonokoPout1.png"
    image Nonoko Hap1 = "Sprites/Nonoko/NonokoHappy1.png"
    image Nonoko Quest1 = "Sprites/Nonoko/NonokoQuestion1.png"
    image Nonoko Laugh1 = "Sprites/Nonoko/NonokoLaughing1.png"
    image Nonoko Yell1 = "sprites/Nonoko/NonokoYell1.png"
    
    #Mori Sprites
    image Mori Neutral1 = im.Flip("Sprites/Mori/MoriNeutral1.png", horizontal=True)
    image Mori Neutral2 = im.Flip("Sprites/Mori/MoriNeutral2.png", horizontal=True)
    image Mori Neutral3 = im.Flip("Sprites/Mori/MoriNeutral3.png", horizontal=True)
    image Mori Neutral4 = im.Flip("Sprites/Mori/MoriNeutral4.png", horizontal=True)
    image Mori Serious1 = im.Flip("Sprites/Mori/MoriSerious1.png", horizontal=True)
    image Mori Serious2 = im.Flip("Sprites/Mori/MoriSerious2.png", horizontal=True)
    image Mori Serious3 = im.Flip("Sprites/Mori/MoriSerious3.png", horizontal=True)
    image Mori Sigh1= im.Flip("Sprites/Mori/MoriSigh1.png", horizontal=True)
    image Mori Sigh2= im.Flip("Sprites/Mori/MoriSigh2.png", horizontal=True)
    image Mori Smile1= im.Flip("Sprites/Mori/MoriSmile1.png", horizontal=True)
    image Mori Smile2= im.Flip("Sprites/Mori/MoriSmile2.png", horizontal=True)
    image Mori Nervous1= im.Flip("Sprites/Mori/MoriNervous1.png", horizontal=True)
    image Mori Hap1 = im.Flip("Sprites/Mori/MoriHappy1.png", horizontal=True)
    
    #Yamane Sprites
    image Yamane Neutral = "Sprites/Yamane/Yamane.png"
    
    #Closed space variants
    image clouds CS = im.MatrixColor("id_clouds.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    
    image bg SchoolEntranceLeft CS = im.MatrixColor("Backgrounds/SchoolEntranceLeft.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image bg SchoolOutside1 CS = im.MatrixColor("Backgrounds/SchoolOutside1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image bg hallway CS = im.MatrixColor("Backgrounds/hallway.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image bg ClubHallLeft CS = im.MatrixColor("Backgrounds/ClubHallLeft.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image bg ClubroomFullNight CS = im.MatrixColor("Backgrounds/ClubroomFullNight.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image ClubroomFullNight Glow = im.MatrixColor("Backgrounds/ClubroomFullNight.png",
        im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(.35))
# 
#     
    image Kyon CS Ser1 = im.MatrixColor("Sprites/Kyon/KyonSerious1.png",
         im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ser2 = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ser3 = im.MatrixColor("Sprites/Kyon/KyonSerious3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh1 = im.MatrixColor("Sprites/Kyon/KyonSigh1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh2 = im.MatrixColor("Sprites/Kyon/KyonSigh2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh3 = im.MatrixColor("Sprites/Kyon/KyonSigh3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh4 = im.MatrixColor("Sprites/Kyon/KyonSigh4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral1 = im.MatrixColor("Sprites/Kyon/KyonNeutral1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral2 = im.MatrixColor("Sprites/Kyon/KyonNeutral2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral3 = im.MatrixColor("Sprites/Kyon/KyonNeutral3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral4 = im.MatrixColor("Sprites/Kyon/KyonNeutral4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang1 = im.MatrixColor("Sprites/Kyon/KyonAngry1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang2 = im.MatrixColor("Sprites/Kyon/KyonAngry2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang3 = im.MatrixColor("Sprites/Kyon/KyonAngry3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang4 = im.MatrixColor("Sprites/Kyon/KyonAngry4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Pain1 = im.MatrixColor("Sprites/Kyon/KyonPained1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Pain2 = im.MatrixColor("Sprites/Kyon/KyonPained2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile1 = im.MatrixColor("Sprites/Kyon/KyonSmile1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile2 = im.MatrixColor("Sprites/Kyon/KyonSmile2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile3 = im.MatrixColor("Sprites/Kyon/KyonSmile3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile4 = im.MatrixColor("Sprites/Kyon/KyonSmile4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile5 = im.MatrixColor("Sprites/Kyon/KyonSmile5.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Worry1 = im.MatrixColor("Sprites/Kyon/KyonWorry1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Worry2 = im.MatrixColor("Sprites/Kyon/KyonWorry1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Puzzle1 = im.MatrixColor("Sprites/Kyon/KyonPuzzled1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sup1 = im.MatrixColor("Sprites/Kyon/KyonSurprised1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sup2 = im.MatrixColor("Sprites/Kyon/KyonSurprised2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap1 = im.MatrixColor("Sprites/Kyon/KyonUnhappy1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap2 = im.MatrixColor("Sprites/Kyon/KyonUnhappy2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap3 = im.MatrixColor("Sprites/Kyon/KyonUnhappy3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap4 = im.MatrixColor("Sprites/Kyon/KyonUnhappy4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap5 = im.MatrixColor("Sprites/Kyon/KyonUnhappy5.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
#     
#         
    image Haruhi CS Sup1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sup2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sup3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang4 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang5 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry5.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap4 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy4.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Pout1 = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Pout2 = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Eyeroll1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideEyeroll1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Eyeroll2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideEyeroll2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Quest1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideQuestion1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Quest2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideQuestion2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Grin1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideGrin1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Grin2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideGrin2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Worry1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideWorry1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Worry2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideWorry2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy2.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy3.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Focus1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideFocus1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Neutral1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideNeutral1.png",
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Neutral2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideNeutral2.png",    
        im.matrix.saturation(.2) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
#     
    
    # "Stakes" for stake rain in Asakura capture scene.
    image stake1:
        "Sprites/Effects/stake.png"
        rotate -6
        
    image stake3:
        "Sprites/Effects/stake.png"
        rotate 6
        
    image stake2:
        "Sprites/Effects/stake.png"
        rotate -12
    
    image stake4:
        "Sprites/Effects/stake.png"
        rotate 12
    
    image SpikeFlick:
        "Sprites/Effects/NetSpike5(old).png"
        easein 2.0 alpha 0.3
        pause 5.0
        easeout 2.0 alpha 1.0
        pause 0.3
        repeat
    
    # Title cards
    image creds 0 = Text("Presented by:\n\nBig Damn VN Brigade\n\nAgasa\nalethiophile\nFilraen\nOroboro\nPax Empyrean\nJason Ulloa\nZer0Null\n\n\nMany thanks to:\n\njonbob\nSpecular", text_align=0.5)
    image creds 1 = Text("Special thanks to:\n\nBrian Randall\nauthor of Kyon: Big Damn Hero\n\nand\n\nNagaru Tanigawa\nauthor of Suzumiya Haruhi series", text_align=0.5)
    image creds 2 = Text("Disclaimer: This production makes use\nof intellectual property belonging to\nBrian Randall, Nagaru Tanigawa \nand others. No disrespect is intended.\n\nNeither Kyon: Big Damn Hero \nnor Suzumiya Haruhi and related \ncharacters are owned by anyone \nassociated with Big Damn VN", text_align=0.5)

    # have to have different image tags so can show them staggered
    image screds0 = Text("Big Damn VN Brigade presents:", text_align=0.5, size=30)
    image screds1 = Text("based on the work by\nBrian Randall", text_align=0.5, size=30)
    image screds2 = Text("in turn based on the\nSuzumiya Haruhi series by\nNagaru Tanigawa", text_align=0.5, size=30)

    # "Image" showing the date
    # image eyeDate = DynamicDisplayable(show_date)
    image eyeDate 1 = DynamicDisplayable(show_date1)
    image eyeDate 2 = DynamicDisplayable(show_date2)
    
    image eyebg = ConditionSwitch("ecbg == 'white'", "#fff", "True", "#000")
    
    # Most likely needs {font=fancyfont.ttf}magic{/font} to pull off properly...
    image BDVNlogo = Text("{size=80}{b}{k=3}KYON:\n{/k}{/b}{/size}{size=40}{k=-1.0}Big Damn Hero{/k}{/size}", color="#3cf")
    
    # Title cards, i.e chapter-opening quotes
    image title 000 = Text("{space=500}{b}{size=+1}Thursday, June 2, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Don't Just SAY You Have a Bad Feeling, DO Something About It!\"\n\n\"...but I digress. When you get that feeling, you know the one, in the back of your head? The one that makes you think something is off about the situation? It may be right. Granted, you may also be tumbling headlong into a fit of paranoia that will end terribly for you and everyone you love. But what if you're NOT? Remember, if you're aware of things, you know most people think you're crazy anyway. Is it going to hurt that much more to overreact rather than just label something a false alarm?\"\n\n\"Practical Heroism and You: Awareness\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 001 = Text("{space=500}{b}{size=+1}Sunday, April 17, 2011{/size}{/b}\n\n\n\n\"Chapter One: The Truth is the Greatest Weapon\"\n\n\"...of dozens of issues with maintaining a 'masquerade' scenario. Generally, unless it's absolutely required, it's a bad idea. There will be fallout. If it must be done, the truth is still going to be the ultimate weapon — plan accordingly, and make sure it's a weapon that will serve you, and not any enemies. Barring that, make fast friends with someone who can BS better than you.\"\n\n\"Cover\" — Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 002 = Text("{space=500}{b}{size=+1}Monday, April 18, 2011{/size}{/b}\n\n\n\n\"Chapter Ten: Time Travel\"\n\n\"This is the one you absolutely cannot afford to mess up. The most important thing is to pay attention, and not over think things. But mostly, it's about paying attention; the worst thing you can do is assume that just because time travel is involved, you cannot fail.\"\n\n\"Practical Heroism and You: Awareness\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 003 = Text("{space=500}{b}{size=+1}Monday, April 18, 2011{/size}{/b}\n\n\n\n\"Chapter One: Expect the Unexpected\"\n\n\"...aside from them, however, there aren't many who can genuinely expect all things and calculate accordingly. So in a practical situations what it really means is: don't be so expectant of something happening, that any other result is a surprise. That's probably the best you can do, anyway.\"\n\n\"Roll With the Punches\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 004 = Text("{space=500}{b}{size=+1}Tuesday, April 19, 2011{/size}{/b}\n\n\n\n\"Chapter Twelve: As in Training, As in Life\"\n\n\"...but just as in the training world, you will inevitably take some blows.\nThat's the purpose of practice, isn't it? Perfection may be a myth, but success is not. So train to be good enough, and most importantly, when you get hit, learn to take it.\"\n\n\"Roll With the Punches\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 005 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"Chapter Seven: Practical Considerations for the Apocalypse\"\n\n\"...if that happens, and there's nothing else to be done, the next question is going to be survival. There are things more important than food, water, or even reasonable shelter. There's no reason to try and survive alone, unless you're just a die-hard, and even then you're still probably clinging to hope. So make sure you're not alone, or else there's not much reason to keep on going.\"\n\n\"Clearing the Event Horizon: How Close is Too Close?\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)

init python:
    #basechar = Character(None, kind=nvl)
    basechar = Character(None, kind=nvl, what_outlines = [(1, "#000", 0, 0)])
    kyon = Character("Kyon", kind=basechar, color="#777755")
    sister = Character("Nonoko", kind=basechar, color="#999977")
    yuki = Character("Nagato Yuki", kind=basechar, color="#aaaaff")
    narrator = Character(None, kind=basechar)
    irisoutfast = CropMove(0.2, "irisout")
    slowfadein = Fade(1.0, 0.5, 5)
    fastfadein = Fade(0.5, 0.5, 0.5)
    wipeleftfast = CropMove(0.3, "wipeleft")
    wiperightfast = CropMove(0.3, "wiperight")
    wipeupslow = CropMove(2, "wipeup")
    wipeupfast = CropMove(0.3, "wipeup")
    teleport = ImageDissolve("id_teleport.png", 2.0, 0)
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
    slowflashbulb = Fade(1.0, 0.5, 2.0, color='#fff')
    slowdissolve = Dissolve(1.0)
    fastdissolve = Dissolve(0.15)
   
    circleirisout = ImageDissolve("id_circleiris.png", 1.0, 8)
    circleirisin = ImageDissolve("id_circleiris.png", 1.0, 8, reverse=True)
    
    circleirisoutfast = ImageDissolve("id_circleiris.png", 0.75, 8)
    circleirisinfast = ImageDissolve("id_circleiris.png", 0.75, 8, reverse=True)
    
    renpy.music.register_channel("sound2", "sfx", 0)
    _preferences.set_volume("sfx", 0.5)
    
    renpy.music.register_channel("sfxloop", "sfx", 1)
    _preferences.set_volume("sfx", 0.5)
    
    # positions on the (imaginary) screen situated directly left of one shown.
    osl_left = Position(xanchor=0.5, yalign=1.0, xpos=-0.75) 
    osl_center = Position(xanchor=0.5, yalign=1.0, xpos=-0.5)
    osl_right = Position(xanchor=0.5, yalign=1.0, xpos=-0.25)
    # positions on the (imaginary) screen situated directly right of one shown.
    osr_center = Position(xanchor=0.5, yalign=1.0, xpos=1.5)
    osr_left = Position(xanchor=0.5, yalign=1.0, xpos=1.25)
    osr_right = Position(xanchor=0.5, yalign=1.0, xpos=-1.75) 
    
    # position of the energy net, lower than truecenter, to cover Ryoko better.
    spike_net_pos = Position(xalign=0.5, ycenter=0.65)
    
    # position of title cards, i.e chapter-opening quotes.
    card_pos = Position(xalign=0.5, yanchor=0.0, ypos=10)
    
    # position for dates in eyecatches.
    date_pos = Position(xanchor=1.0, yanchor=0.0, xpos=790, ypos=10)  
    
    fast_move = MoveTransition(0.2)
    
    # Screen shake effect.
    sshake = Shake((0, 0, 0, 0), 1.0, dist=30)
    
    adj = ui.adjustment()
    music_need = True
    ecbg = "black"
    
    # Faux movie announcer voice
    style.movie = Style(style.default)
    # Comment everything with "style.movie." below to disable the {=movie}{/=movie} tag effects
    # # style.movie.font = "DejaVuSansMono.ttf"
    if persistent.text_styling == "Extra":
        style.movie.font = "DejaVuSerif.ttf"
    # # style.movie.size = 23
    # # style.movie.kerning = 1
    
    # Loud voice
    style.loud = Style(style.default)
    # Comment everything with "style.loud." below to disable the {=loud}{/=loud} tag effects
    if persistent.text_styling == "Extra":
        style.loud.size = 24
    
    # Shouting voice
    style.shout = Style(style.default)
    # Comment everything with "style.shout." below to disable the {=shout}{/=shout} tag effects
    if persistent.text_styling == "Extra":
        style.shout.size = 32
    
    # Quieter voice
    style.quiet = Style(style.default)
    # Comment everything with "style.quiet." below to disable the {=quiet}{/=quiet} tag effects
    # if persistent.text_styling == "Extra":
        # style.quiet.size = 20
    
    # Whispering voice
    style.whisper = Style(style.default)
    # Comment everything with "style.whisper." below to disable the {=whisper}{/=whisper} tag effects
    if persistent.text_styling == "Extra":
        style.whisper.size = 15
        
    renpy.register_style_preference("text", "Extra", style.movie, "font", "DejaVuSerif.ttf")
    renpy.register_style_preference("text", "Extra", style.loud, "size", 24)
    renpy.register_style_preference("text", "Extra", style.shout, "size", 32)
    renpy.register_style_preference("text", "Extra", style.whisper, "size", 15)
    
    renpy.register_style_preference("text", "Vanilla", style.movie, "font", "DejaVuSans.ttf")
    renpy.register_style_preference("text", "Vanilla", style.loud, "size", 22)
    renpy.register_style_preference("text", "Vanilla", style.shout, "size", 22)
    renpy.register_style_preference("text", "Vanilla", style.whisper, "size", 22)
    
    centered = Character(None, what_slow_cps=0, what_size = 27, what_outlines = [(1, "#000", 0, 0)],
                        what_layout="subtitle", what_xalign=0.5, what_text_align=0.5,
                        window_background=None, window_yminimum=0, window_xfill=False, 
                        window_xalign=0.5, window_yalign=0.5) 

    if config.developer:
        config.keymap['skip'].remove('K_LCTRL')
        config.keymap['skip'].remove('K_RCTRL')
        config.keymap['skip'].append('K_LALT')
        config.keymap['skip'].append('K_RALT')
        config.keymap['hide_windows'].append('K_BACKSPACE')
        config.keymap['reload_game'].append('r')
        config.keymap['inspector'].append('i')
        config.keymap['developer'].append('d')
        config.keymap['toggle_music'].append('m')
        config.keymap['toggle_music'].append('M')
    
        
transform center_left:
    xalign 0.1 yalign 1.0

transform TopRight:
    xalign 1.0 yalign 0.0
transform TopLeft:
    xalign 0.0 yalign 0.0      
transform HalfRight:
    xalign 0.75 yalign 1.0
transform HalfLeft:
    xalign 0.25 yalign 1.0
    
transform TenthRight:
    xalign 0.90 yalign 1.0
transform TenthLeft:
    xalign 0.10 yalign 1.0
    
transform KyonRightFast:
    xalign -0.5 yalign 1.0
    linear 0.2 xalign 2.0
transform PanScene_LeftToRight:
    # xpos 0.0
    linear 0.15 xpos -1.0
transform PanScene_LeftToRightSlow:
    # xpos 0.0
    linear 1.5 xpos -1.0
transform PanScene_LeftToCenter:
    # xpos 0.0
    linear 0.15 xpos -0.5
transform PanScene_CenterToLeft:
    xpos -0.5
    linear 0.15 xpos 0.0
transform PanScene_RightToLeft:
    xpos -1.0 
    linear 0.15 xpos 0.0
transform PanScene_RightToLeftSlow:
    xpos -1.0 
    linear 1.5 xpos 0.0
transform PanScene_RightToCenter:
    xpos -1.0
    linear 0.15 xpos -0.5
transform PanScene_CenterToRight:
    xpos -0.5    
    linear 0.15 xpos -1.0
transform PanScene_SetToRight:
    xpos -1.0    
transform PanScene_SetToLeft:
    xpos 0.0    
transform left_RightScreen:
    xpos 1.0 yalign 1.0    
transform center_RightScreen:
    xpos 1.37 yalign 1.0 # xalign 0.5 yalign 1.0    
transform right_RightScreen:
    xpos 1.65 yalign 1.0    
transform TopRight_RightScreen:
   xpos 1.71 yalign 0.0
transform HalfRight_RightScreen:
   xpos 1.6 yalign 1.0    
transform UnderLegs_RightScreen:
    xalign 1.563 yalign 2.2    
    
    
init -1 python:
    # def show_date(st, at):
        # return Text("[date]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf"), None
    def show_date1(st, at):
        return Text("[date1]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf"), None
    def show_date2(st, at):
        return Text("[date2]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf"), None
        
    if persistent.text_styling == None:
        persistent.text_styling = "Extra"
    
    chapters = [
        ("In Media Res Prologue:\n\"Exactly What it Says on the Tin\"", "prologue"),
        ("Obligatory Anachronic Order \nExplanation Arc - Chapter One:\n\"Scene Twelve, the Ninth Big Fight\"", "AO1_1"),
        ("Obligatory Anachronic Order \nExplanation Arc - Chapter Two:\n\"Clear as Mud\"", "AO2"),
        ("Straightforward Flashback \nand Exposition Arc - Chapter Three:\n\"It Goes To Eleven\"", "SF1"),
        ("Straightforward Flashback \nand Exposition Arc - Chapter Four:\n\"Epileptic Plot Tree\"", "SF2"),
        ("Straightforward Flashback \nand Exposition Arc - Chapter Five: \n\"The Requisite Haruhi-and-Kyon \nin Closed Space Together Again Part \n(You Know The One)\"", "SF3"),
        ("Label a scene you're working on test and use this", "Test"),
        # ("-----", "backtomain"),
               
        ("Credits", "credits"),
        ("Another testbed, Eyecatchies", "test_Z0_eye"),
        ("Another testbed, Title cards", "test_Z0_titles"),]
        
    ecbg = "black"

label backtomain:
    return

label start:
    # Z0 : intro. 
    stop music
    scene black
    show screds0 with dissolve:
        xalign 0.5
        yalign 0.2
    pause
    $ renpy.pause(0.1, hard=True)
    show screds1 with dissolve:
        xalign 0.5
        yalign 0.4
    pause
    $ renpy.pause(0.1, hard=True)
    show screds2 with dissolve:
        xalign 0.5
        yalign 0.72
    pause
    # show Text("{color=#00a}{size=60}KYON:{/size}\n{size=40}Big Damn Hero{/size}{/color}") at truecenter with dissolve
    scene black
    show BDVNlogo at truecenter with coatin
    pause
    hide BDVNlogo with coatout
    jump prologue

    
    
label credits:
    # Done with special character (and one Text() "image" to show both ways.)
    # Text() way supports transitions (and positioning) easily, but *needs* pauses. Character way is straight-up.
    stop music
    # play music "Music/ItsumoReprise.mp3"
    scene black with fade
    # The hardpause calls are necessary because otherwise Ren'py wants to skip over all the pause statements on a single press of the key.
    # show Credits0 with dissolve
    show creds 0 at truecenter with Dissolve(1.0)
    pause
    $ renpy.pause(.1, hard=True)
    # show Credits1 with dissolve
    show creds 1 with Dissolve(1.0)
    pause
    $ renpy.pause(.1, hard=True)
    # show Credits2 with dissolve
    show creds 2 with Dissolve(1.0)
    pause
    $ renpy.pause(.1, hard=True)
    # show Credits3 with dissolve
    # # Maybe a graphic logo here?
    hide creds with Dissolve(1.0)
    show BDVNlogo at truecenter with Dissolve(2.0)
    pause
    stop music
    return
    

# Generic eyecatch routine with single date to show.
label eyecatch(date="", pause_time=3.0, r=0, ecbg="black"):
    scene eyebg with Dissolve(1)
    # call eyecatch_coatinout(date, date, pause_time) from eyecatch_generic
    call eyecatch_random(date, date, pause_time, r) from eyecatch_generic
    scene black with Dissolve(0.5)
    return

# Generic eyecatch routine with two dates to show, second replacing first.
label eyecatch2(date1="", date2="", pause_time=3.0, r=0, ecbg="black"):
    scene eyebg with Dissolve(1)
    # call eyecatch_coatinout(pause_time) from eyecatch_generic
    call eyecatch_random(date1, date2, pause_time, r) from eyecatch_generic2
    scene black with Dissolve(0.5)
    return

    
label eyecatch_simple(date1="", date2="", pause_time=2.0):
    # Simple version
    $ pause2 = pause_time/2
    # scene black with Dissolve(1)
    show BDVNlogo at truecenter
    show eyeDate 1 at date_pos
    with Dissolve(2.0)
    pause pause2
    show eyeDate 2 at date_pos
    with dissolve
    pause pause2
    scene black with Dissolve(2.0)
    centered "{nw}"
    return

label eyecatch_coatinout(date1="", date2="", pause_time=2.0):
    # Uses kickass coatin-coatout transition
    $ pause2 = pause_time/2
    # scene black with Dissolve(1)
    show BDVNlogo at truecenter
    show eyeDate 1 at date_pos
    with coatin
    pause pause2
    show eyeDate 2 at date_pos with dissolve
    pause pause2
    hide BDVNlogo
    hide eyeDate at date_pos
    with coatout
    centered "{nw}"
    return
        
label eyecatch_darken1(date1="", date2="", pause_time=2.0):
    # Darkening, for tension buildup (or so I was told), v1
    $ pause2 = pause_time/2
    show almostblack one at truecenter with dissolve
    show almostblack two at truecenter
    show BDVNlogo at truecenter
    show eyeDate 1 at date_pos
    with Dissolve(2.0)
    pause pause2
    show eyeDate 2 at date_pos with dissolve
    pause pause2
    scene black with Dissolve(1)
    centered "{nw}"
    return
    
label eyecatch_darken2(date1="", date2="", pause_time=2.0):
    # Darkening, for tension buildup (or so I was told), v2
    $ pause2 = pause_time/2
    show almostblack two at truecenter with Dissolve(1)
    show BDVNlogo at truecenter
    show eyeDate 1 at date_pos
    with Dissolve(2.0)
    pause pause2
    show eyeDate 2 at date_pos with dissolve
    pause pause2
    scene black with Dissolve(1)
    centered "{nw}"
    return
    
    
label eyecatch_random(date1="", date2="", pause_time=2.0, r=0):
    # randomly choses the way logo appears and disappears with every call
    $ pause2 = pause_time/2
    # scene black with Dissolve(1)
    if r == 0 or r > 5:
        $ r = renpy.random.randint(1, 5)
        
    if r == 1:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with moveinright
        pause pause2
        show eyeDate 2 at date_pos with wiperight
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with moveoutleft
        # $ renpy.pause(.01, hard=True)
    elif r == 2:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with moveinleft
        pause pause2
        show eyeDate 2 at date_pos with wipeleft
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with moveoutright
        # $ renpy.pause(.01, hard=True)
    elif r == 3:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with moveintop
        pause pause2
        show eyeDate 2 at date_pos with dissolve
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with moveoutbottom
        # $ renpy.pause(.01, hard=True)
    elif r == 4:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with moveinbottom
        pause pause2
        show eyeDate 2 at date_pos with dissolve
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with moveouttop
        # $ renpy.pause(.01, hard=True)
    else:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with coatin
        pause pause2
        show eyeDate 2 at date_pos with dissolve
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with coatout
        # $ renpy.pause(.01, hard=True)
    # Works just as well as hardpause in prevesting skipping the fade, but does not block the rollback
    centered "{nw}"
    return

    
    
label test_Z0_eye:
    scene bg MorningSky
    show TownHillLeftMorning
    # show Kyon Sigh1 at right
    show Asakura Unhap1 at center
    show stake1 at Position(xanchor=0.5, yanchor=1.0, xpos=450, ypos=0)
    show stake2 at Position(xanchor=0.5, yanchor=1.0, xpos=500, ypos=0)
    show stake3 behind Asakura at Position(xanchor=0.5, yanchor=1.0, xpos=370, ypos=0)
    show stake4 behind Asakura at Position(xanchor=0.5, yanchor=1.0, xpos=300, ypos=0)
    play sound "SE/netlaunch.mp3"
    pause (1)
    play sound "SE/stake1.mp3"
    show stake2 at Position(xanchor=0.5, yanchor=1.0, xpos=600, ypos=1.2)
    with MoveTransition(0.08)
    play sound2 "SE/stake2.mp3"
    show stake1 at Position(xanchor=0.5, yanchor=1.0, xpos=500, ypos=1.2)
    with MoveTransition(0.08)
    play sound "SE/stake3.mp3"
    show stake3 behind Asakura at Position(xanchor=0.5, yanchor=1.0, xpos=330, ypos=1.2)
    with MoveTransition(0.08)
    play sound "SE/stake1.mp3"
    show stake4 behind Asakura at Position(xanchor=0.5, yanchor=1.0, xpos=190, ypos=1.2)
    with MoveTransition(0.08)
    pause(0.1)
    show SpikeFlick at center
    "\"{=loud}You opened{/=loud} it already, {=shout}I see{/=shout}.\""
    "[style.movie.font] - [style.loud.size] - [style.shout.size] - [style.whisper.size]"
    $ style.shout.size = 10
    "\"{=loud}You opened{/=loud} it already, {=shout}I see{/=shout}.\""
    "!S[style.movie.font] - [style.loud.size] - [style.shout.size] - [style.whisper.size]"
    nvl clear
    # call the eyecatch routine, supply the date (text) to show and pause time if needed, specify the unique "from"
    call eyecatch2("Sample date", "Another date", 10.0, ecbg="white") from test_Z0_p0001
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    "\"Well, of course! Doesn't make any sense to me, though. I probably wouldn't have opened it if you hadn't told me it wouldn't make any sense to me."
    show Haruhi Quest1 at left
    "\"Why did you want me to give you a letter from yourself, though?\""
    show Kyon Sigh2 at right
    "\n\n\n\n\n\n\nThe skies were clear of rain, if gray, so he sighed and pulled the letter out of the envelope while proceeding up the hill."
    # call the eyecatch routine, supply the date (text) to show, specify the unique "from"
    call eyecatch_darken1("December -1, 0000", "December -2, 0001") from test_Z0_p0002
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    nvl clear
    "And now, eyecatch vDarken2!"
    # call the eyecatch routine, supply the date (text) to show, specify the unique "from"
    call eyecatch_darken2("Marthober 32, 9999", "Marthober 33, 0000") from test_Z0_p0003
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    "And now, one random eyecatch!"
    # call the eyecatch routine, supply the date (text) to show, specify the unique "from"
    call eyecatch_random("February 30, 1999", "February 30, 1999") from test_Z0_p0004
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Kyon Sigh1 at right
    with dissolve
    "And another one. (but effect may be the same. Randomness, y'know)"
    # call the eyecatch routine, can supply nothing if nothing needs to be changed, specify the unique "from"
    call eyecatch_random("Febtober 3.14, 1592", "Febtober 2.71828, 1592") from test_Z0_p0005
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    "Thats all!"
    # If you specify the names of arguments, you don't have to worry about positions
    call eyecatch(pause_time=3.0, r=5) from test_Z0_p0006
    return


label test_Z0_titles:
    scene black
    show title 000 at card_pos with slowfadein
    pause
    show title 001 at card_pos with slowfadein
    pause
    show title 002 at card_pos with slowfadein
    pause
    show title 003 at card_pos with slowfadein
    pause
    show title 004 at card_pos with slowfadein
    pause
    show title 005 at card_pos with slowfadein
    pause
