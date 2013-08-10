# K:BDH VN main script file; contains init code and code declarations.

init:
    image almostblack one = "#0008"  #semitransparent foregrounds used in eyecatch.
    image almostblack two = "#000e"  #do not use as background if you don't like checker patterns
        #for a background, use simply "black", defined below as image black = "#000000".

    image bg classroom = "Backgrounds/classroom.jpg"
    image bg hallway = "Backgrounds/hallway.png"
    image bg hallwayFull = "Backgrounds/hallwayFull.png"
    image bg stairwell = "Backgrounds/stairwell.jpg"
    image bg stairwell2 = "Backgrounds/stairwell2.png"
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
    image bg KitaguchiStationOutside_Day = "Backgrounds/KitaguchiStationOutside_Day.png"
    image bg KitaguchiStationOutside_Evening = "Backgrounds/KitaguchiStationOutside_Evening.png"
    image bg KyonRoomLeftClosed = "Backgrounds/KyonRoomLeftClosed.png"
    image bg KyonRoomRightClosed = "Backgrounds/KyonRoomRightClosed.png"
    image bg KyonRoomFullClosed = "Backgrounds/KyonRoomFullClosed.png"
    image bg KyonRoomLeftMorning = "Backgrounds/KyonRoomLeftMorning.png"
    image bg KyonRoomRightMorning = "Backgrounds/KyonRoomRightMorning.png"
    image bg KyonRoomFullMorning = "Backgrounds/KyonRoomFullMorning.png"
    image bg KyonHouseNight = "Backgrounds/KyonHouseNight.png"
    image bg KyonHouseDay = "Backgrounds/KyonHouseDay.png"
    image bg KyonKitchenRight = "Backgrounds/KyonKitchenRight.png"
    image bg KyonKitchenLeft = "Backgrounds/KyonKitchenLeft.png"
    image bg KyonHallway = "Backgrounds/KyonHallway.png"
    image bg KyonLivingRoomDay = "Backgrounds/KyonLivingRoomDay.png"
    image bg KyonLivingRoomEvening = "Backgrounds/KyonLivingRoomEvening.png"
    image bg KyonLivingRoomNight = "Backgrounds/KyonLivingRoomNight.png"
    image bg HaruhiBedroomDay = "Backgrounds/HaruhiBedroomDay.png"
    image bg HaruhiBedroomAfternoon = "Backgrounds/HaruhiBedroomAfternoon.png"
    image bg HaruhiBedroomEvening = "Backgrounds/HaruhiBedroomEvening.png"
    image bg HaruhiBedroomNight = "Backgrounds/HaruhiBedroomNight.png"
    image bg HaruhiKitchenDay = "Backgrounds/HaruhiKitchenDay.png"
    image bg TsuruyaBedroom = "Backgrounds/TsuruyaBedroom.png"
    image bg TsuruyaFutonDay = "Backgrounds/TsuruyaFutonDay.png"
    image bg TsuruyaFutonNight = "Backgrounds/TsuruyaFutonNight.png"
    image bg TsuruyaBath = "Backgrounds/TsuruyaBath.png"
    image bg TsuruyaKitchen = "Backgrounds/TsuruyaKitchen.png"
    image bg TsuruyaHouseDay = "Backgrounds/TsuruyaHouseDay.png"
    image bg TsuruyaHouseNight = "Backgrounds/TsuruyaHouseNight.png"
    image bg TsuruyaMeetingDay = "Backgrounds/TsuruyaMeetingHallDay.png"
    image bg TsuruyaMeetingEvening = "Backgrounds/TsuruyaMeetingHallEvening.png"
    image bg TsuruyaMeetingNight = "Backgrounds/TsuruyaMeetingHallNight.png"
    image bg TownCommercialDistrict_Day = "Backgrounds/TownCommercialDistrict_Day.png"
    image bg TownCommercialDistrict_Evening = "Backgrounds/TownCommercialDistrict_Evening.png"
    image bg TownCommercialDistrict_Night = "Backgrounds/TownCommercialDistrict_Night.png"
    image bg TownStreetEvening1 = "Backgrounds/TownStreetEvening1.png"
    image bg TownStreetEvening2 = "Backgrounds/TownStreetEvening2.png"
    image bg TownStreetEveningFull = "Backgrounds/TownStreetEveningFull.png"
    image bg TownStreetNight1 = "Backgrounds/TownStreetNight1.png"
    image bg TownStreetNight2 = "Backgrounds/TownStreetNight2.png"
    image bg TownStreetDay1 = "Backgrounds/TownStreetDay1.jpg"
    image bg TownStreetDay2 = "Backgrounds/TownStreetDay2.jpg"
    image bg TownStreetDay3 = "Backgrounds/TownStreetDay3.jpg"
    image bg TownFull = "Backgrounds/TownFull.png"
    image bg TownLeft = "Backgrounds/Townleft.png"
    image bg TownRight = "Backgrounds/TownRight.png"
    image bg Elevator = "Backgrounds/ElevatorInterior.png"                                                         
    image bg ClubHallLeft = "Backgrounds/ClubHallLeft.png"                                     
    image bg ClubHallRight = "Backgrounds/ClubHallRight.png"                                     
    image bg ClubHallFull = "Backgrounds/ClubHallFull.png"
    image bg ClubroomCenterDay = "Backgrounds/ClubroomCenterDay.png"
    image bg ClubroomLeftDay = "Backgrounds/ClubroomLeftDay.png"
    image bg ClubroomFullDay ="Backgrounds/ClubroomFullDay.jpg"
    image bg ClubroomRightDay = "Backgrounds/ClubroomRightDay.png"
    image bg ClubroomFullNight = "Backgrounds/ClubroomFullNight.png"
    image bg ClubroomBack = "Backgrounds/ClubBack.png"
    image bg ClubHallOutside = "Backgrounds/ClubHallOutside.png"
    image ClubTable ="Backgrounds/ClubTable.png"
    image bg YukiApartmentDay = "Backgrounds/YukiApartmentDay.png"
    image bg YukiApartmentNight = "Backgrounds/YukiApartmentNight.png"
    image bg YukiRoomLeft = "Backgrounds/YukiRoomLeft.png"
    image bg YukiRoomRight = "Backgrounds/YukiRoomRight.png"
    image bg YukiRoomCenter = "Backgrounds/YukiRoomCenter.jpg"
    image bg SchoolOutside = "Backgrounds/SchoolOutside.png"
    image bg SchoolOutside Night = "Backgrounds/SchoolOutsideNight.png"
    image bg SchoolEntranceLeft = "Backgrounds/SchoolEntranceLeft.png"
    image bg SchoolEntranceRight = "Backgrounds/SchoolEntranceLeft.png"
    image bg SchoolBathroom = "Backgrounds/SchoolBathroom.png"
    image bg SchoolTable = "Backgrounds/SchoolTable.png"
    image bg SchoolTreeFull = "Backgrounds/SchoolTreeFull.png"
    image bg SchoolTreeLeft = "Backgrounds/SchoolTreeLeft.png"
    image bg SchoolTreeRight = "Backgrounds/SchoolTreeRight.png"
    image bg SchoolTreeCenter = "Backgrounds/SchoolTreeCenter.png"
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
    image bg Alley1Day = "Backgrounds/Alley1Day.png"
    image bg Alley1Evening = "Backgrounds/Alley1Evening.png"
    image bg Alley1Night = "Backgrounds/Alley1Night.png"
    image bg Alley2Day = "Backgrounds/Alley2Day.png"
    image bg Alley2Evening = "Backgrounds/Alley2Evening.png"
    image bg Alley2Night = "Backgrounds/Alley2Night.png"
    image bg LivingRoom = "Backgrounds/LivingRoom.png"
    image bg Library = "Backgrounds/Library.jpg"
    image bg LockersDayLeft = "Backgrounds/LockersDayLeft.png"
    image bg LockersDayRight = "Backgrounds/LockersDayRight.png"
    image bg LockersDayFull = "Backgrounds/LockersDayFull.png"
    image bg LockersNightLeft = "Backgrounds/LockersNightLeft.png"
    image bg LockersNightRight = "Backgrounds/LockersNightRight.png"
    image bg LockersNightFull = "Backgrounds/LockersNightFull.png"
    image bg LockersEveningLeft = "Backgrounds/LockersEveningLeft.png"
    image bg LockersEveningRight = "Backgrounds/LockersEveningRight.png"
    image bg LockersEveningFull = "Backgrounds/LockersEveningFull.png"
    image bg TrainStation = "Backgrounds/TrainStation.png"
    image bg WatanabeBaseLeft = "Backgrounds/WatanabeBaseLeft.jpg"
    image bg WatanabeBaseRight = "Backgrounds/WatanabeBaseRight.jpg"
    image bg WatanabeBaseFull = "Backgrounds/WatanabeBaseFull.jpg"
    image bg WatanabeBaseCenter = "Backgrounds/WatanabeBaseCenter.jpg"
    image bg Supermarket = "Backgrounds/Supermarket.png"
    image bg FabricShop = "Backgrounds/FabricShop.png"
    image bg MikuruRoom = "Backgrounds/MikuruRoom.png"
    image bg MikuruApartment = "Backgrounds/MikuruApartment.png"
    image bg MikuruClass = "Backgrounds/MikuruClass.png"
    image bg Udon = "Backgrounds/Udon.png"
    image TownHillLeftMorning =  "Backgrounds/TownHillLeftMorning.png"
    image bg IdolClubDark = "Backgrounds/IdolClubDark.png"
    image bg IdolClubLight = "Backgrounds/IdolClubLight.png"
    
    
    image lowkick1 = im.Alpha("Backgrounds/Effects/lowkick1.png", 0.75)
    image hit1 = "Backgrounds/Effects/hit1.png"
    image punch1 = "Backgrounds/Effects/Punch1.png"
    image punch2 = "Backgrounds/Effects/Punch2.png"
    image punch3 = "Backgrounds/Effects/Punch3.png"
    image transblack = im.Alpha("Backgrounds/Effects/black.png", 0.75)
    image transred = im.Alpha("Backgrounds/Effects/red.png", 0.75)
    image hazered = im.Alpha("Backgrounds/Effects/red.png", 0.25)
    image axekick1 = "Backgrounds/Effects/axekick1.png"
    image kick1 = "Backgrounds/Effects/kick1.png"
    image swipe1 = im.Alpha("Backgrounds/Effects/swipe1.png", 0.75)
    image kick1 Flip = im.Flip("Backgrounds/Effects/kick1.png", horizontal=True)
    
    image white = "#ffffff"
    image black = "#000000"
    image yellow = "#FFFF00"
    image cyan = "#00FFFF"
    image transpwhite = "#ffffffcc"
    image yukibackground = "#ccccff"
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
    image Cut = "Sprites/Effects/cuttest.png"
    
    #Haruhi Sprites
    image Haruhi Sup1 = "Sprites/Haruhi/HaruhiSideSurprised1.png"
    image Haruhi Sup2 = "Sprites/Haruhi/HaruhiSideSurprised2.png"
    image Haruhi Sup3 = "Sprites/Haruhi/HaruhiSideSurprised3.png"
    image Haruhi Ang1 = "Sprites/Haruhi/HaruhiSideAngry1.png"
    image Haruhi Ang2 = "Sprites/Haruhi/HaruhiSideAngry2.png"
    image Haruhi Ang3 = "Sprites/Haruhi/HaruhiSideAngry3.png"
    image Haruhi Ang4 = "Sprites/Haruhi/HaruhiSideAngry4.png"
    image Haruhi Ang5 = "Sprites/Haruhi/HaruhiSideAngry5.png"
    image Haruhi Ang6= "Sprites/Haruhi/HaruhiSideAngry6.png"
    image Haruhi Hap1 = "Sprites/Haruhi/HaruhiSideHappy1.png"
    image Haruhi Hap2 = "Sprites/Haruhi/HaruhiSideHappy2.png"
    image Haruhi Hap3 = "Sprites/Haruhi/HaruhiSideHappy3.png"
    image Haruhi Hap4 = "Sprites/Haruhi/HaruhiSideHappy4.png"
    image Haruhi Hap5 = "Sprites/Haruhi/HaruhiSideHappy5.png"
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
    image Haruhi Grin3 = "Sprites/Haruhi/HaruhiSideGrin3.png"
    image Haruhi Worry1 = "Sprites/Haruhi/HaruhiSideWorry1.png"
    image Haruhi Worry2 = "Sprites/Haruhi/HaruhiSideWorry2.png"
    image Haruhi Worry3 = "Sprites/Haruhi/HaruhiSideWorry3.png"
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
    image Haruhi Neutral3 ="Sprites/Haruhi/HaruhiSideNeutral3.png"
    image Haruhi Neutral4 ="Sprites/Haruhi/HaruhiSideNeutral4.png"
    
    image Haruhi Casual Sup1 = "Sprites/Haruhi/HaruhiSideCasualSurprised1.png"
    image Haruhi Casual Sup2 = "Sprites/Haruhi/HaruhiSideCasualSurprised2.png"
    image Haruhi Casual Sup3 = "Sprites/Haruhi/HaruhiSideCasualSurprised3.png"
    image Haruhi Casual Ang1 = "Sprites/Haruhi/HaruhiSideCasualAngry1.png"
    image Haruhi Casual Ang2 = "Sprites/Haruhi/HaruhiSideCasualAngry2.png"
    image Haruhi Casual Ang3 = "Sprites/Haruhi/HaruhiSideCasualAngry3.png"
    image Haruhi Casual Ang4 = "Sprites/Haruhi/HaruhiSideCasualAngry4.png"
    image Haruhi Casual Ang5 = "Sprites/Haruhi/HaruhiSideCasualAngry5.png"
    image Haruhi Casual Ang6 = "Sprites/Haruhi/HaruhiSideCasualAngry6.png"
    image Haruhi Casual Hap1 = "Sprites/Haruhi/HaruhiSideCasualHappy1.png"
    image Haruhi Casual Hap2 = "Sprites/Haruhi/HaruhiSideCasualHappy2.png"
    image Haruhi Casual Hap3 = "Sprites/Haruhi/HaruhiSideCasualHappy3.png"
    image Haruhi Casual Hap4 = "Sprites/Haruhi/HaruhiSideCasualHappy4.png"
    image Haruhi Casual Hap5 = "Sprites/Haruhi/HaruhiSideCasualHappy5.png"
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
    image Haruhi Casual Grin3 = "Sprites/Haruhi/HaruhiSideCasualGrin3.png"
    image Haruhi Casual Worry1 = "Sprites/Haruhi/HaruhiSideCasualWorry1.png"
    image Haruhi Casual Worry2 = "Sprites/Haruhi/HaruhiSideCasualWorry2.png"
    image Haruhi Casual Worry3 = "Sprites/Haruhi/HaruhiSideCasualWorry3.png"
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
    image Haruhi Casual Neutral3 ="Sprites/Haruhi/HaruhiSideCasualNeutral3.png"
    image Haruhi Casual Neutral4 ="Sprites/Haruhi/HaruhiSideCasualNeutral4.png"
    
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
    image Haruhi Crossed Eyeroll2 = "Sprites/Haruhi/HaruhiCrossedEyeroll2.png"
    image Haruhi Crossed Quest1 = "Sprites/Haruhi/HaruhiCrossedQuestion1.png"
    image Haruhi Crossed Grin1 = "Sprites/Haruhi/HaruhiCrossedGrin1.png"
    image Haruhi Crossed Grin2 = "Sprites/Haruhi/HaruhiCrossedGrin2.png"
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
    image Haruhi Crossed Casual Eyeroll2 = "Sprites/Haruhi/HaruhiCrossedCasualEyeroll2.png"
    image Haruhi Crossed Casual Quest1 = "Sprites/Haruhi/HaruhiCrossedCasualQuestion1.png"
    image Haruhi Crossed Casual Grin1 = "Sprites/Haruhi/HaruhiCrossedCasualGrin1.png"
    image Haruhi Crossed Casual Grin2 = "Sprites/Haruhi/HaruhiCrossedCasualGrin2.png"
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
    image Haruhi Point Scold2 = "Sprites/Haruhi/HaruhiPointScold2.png"
    
    image Haruhi Point Casual Amuse1 = "Sprites/Haruhi/HaruhiPointCasualAmused1.png"
    image Haruhi Point Casual Surpr1 = "Sprites/Haruhi/HaruhiPointCasualSurprised1.png"
    image Haruhi Point Casual Ang1 = "Sprites/Haruhi/HaruhiPointCasualAngry1.png"
    image Haruhi Point Casual Hap1 = "Sprites/Haruhi/HaruhiPointCasualHappy1.png"
    image Haruhi Point Casual Scold1 = "Sprites/Haruhi/HaruhiPointCasualScold1.png"
    image Haruhi Point Casual Scold2 = "Sprites/Haruhi/HaruhiPointCasualScold2.png"
    
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
    image Hblush Hips Casual = "Sprites/Haruhi/HblushHipsCasual.png"
    image Htears ="Sprites/Haruhi/HTearsSide1.png"
    image Htears Casual = "Sprites/Haruhi/HTearsSideCasual1.png"
    image Hblush Crossed = "Sprites/Haruhi/HBlushCrossed copy.png"
    
    image Hblush Flip = im.Flip("Sprites/Haruhi/HaruhiSideBlush1.png", horizontal=True)
    image Hblush Casual Flip = im.Flip("Sprites/Haruhi/HaruhiSideCasualBlush1.png", horizontal=True)
    image Hblush Hips Flip = im.Flip("Sprites/Haruhi/HblushHips.png", horizontal=True)
    image Hblush Hips Casual Flip = im.Flip("Sprites/Haruhi/HblushHipsCasual.png", horizontal=True)
    image Htears Flip = im.Flip("Sprites/Haruhi/HTearsSide1.png", horizontal=True)
    image Htears Casual Flip = im.Flip("Sprites/Haruhi/HTearsSideCasual1.png", horizontal=True)
    image Hblush Crossed Flip = im.Flip("Sprites/Haruhi/HBlushCrossed copy.png", horizontal=True)
    
    #Haruhi image flips
    image Haruhi Ang1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry1.png", horizontal=True)
    image Haruhi Ang2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry2.png", horizontal=True)
    image Haruhi Ang3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry3.png", horizontal=True)
    image Haruhi Ang4 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry4.png", horizontal=True)
    image Haruhi Ang5 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry5.png", horizontal=True)
    image Haruhi Ang6 Flip = im.Flip("Sprites/Haruhi/HaruhiSideAngry6.png", horizontal=True)
    image Haruhi Smile1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSmile1.png", horizontal=True)
    image Haruhi Smile2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSmile2.png", horizontal=True)
    image Haruhi Smile3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSmile3.png", horizontal=True)
    image Haruhi Neutral1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideNeutral1.png", horizontal=True)
    image Haruhi Neutral2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideNeutral2.png", horizontal=True)
    image Haruhi Neutral3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideNeutral3.png", horizontal=True)
    image Haruhi Neutral4 Flip = im.Flip("Sprites/Haruhi/HaruhiSideNeutral4.png", horizontal=True)
    image Haruhi Grin1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideGrin1.png", horizontal=True)
    image Haruhi Grin2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideGrin2.png", horizontal=True)
    image Haruhi Grin3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideGrin3.png", horizontal=True)
    image Haruhi Pout1 Flip = im.Flip("Sprites/Haruhi/HaruhiSidePout1.png", horizontal=True)
    image Haruhi Pout2 Flip = im.Flip("Sprites/Haruhi/HaruhiSidePout2.png", horizontal=True)
    image Haruhi Sigh1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSigh1.png", horizontal=True)
    image Haruhi Sigh2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSigh2.png", horizontal=True)
    image Haruhi Sigh3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSigh3.png", horizontal=True)
    image Haruhi Sup1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSurprised1.png", horizontal=True)
    image Haruhi Sup2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSurprised2.png", horizontal=True)
    image Haruhi Sup3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideSurprised3.png", horizontal=True)
    image Haruhi Hap1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideHappy1.png", horizontal=True)
    image Haruhi Hap2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideHappy2.png", horizontal=True)
    image Haruhi Hap3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideHappy3.png", horizontal=True)
    image Haruhi Hap4 Flip = im.Flip("Sprites/Haruhi/HaruhiSideHappy4.png", horizontal=True)
    image Haruhi Hap5 Flip = im.Flip("Sprites/Haruhi/HaruhiSideHappy5.png", horizontal=True)
    image Haruhi Quest1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideQuestion1.png", horizontal=True)
    image Haruhi Quest2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideQuestion2.png", horizontal=True)
    image Haruhi Unhap1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideUnhappy1.png", horizontal=True)
    image Haruhi Unhap2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideUnhappy2.png", horizontal=True)
    image Haruhi Unhap3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideUnhappy3.png", horizontal=True)
    image Haruhi Eyeroll1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideEyeroll1.png", horizontal=True)
    image Haruhi Eyeroll2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideEyeroll2.png", horizontal=True)
    image Haruhi Worry1 Flip = im.Flip("Sprites/Haruhi/HaruhiSideWorry1.png", horizontal=True)
    image Haruhi Worry2 Flip = im.Flip("Sprites/Haruhi/HaruhiSideWorry2.png", horizontal=True)
    image Haruhi Worry3 Flip = im.Flip("Sprites/Haruhi/HaruhiSideWorry3.png", horizontal=True)
    
    image Haruhi Crossed Sup1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSurprised1.png", horizontal=True)
    image Haruhi Crossed Sup2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSurprised2.png", horizontal=True)
    image Haruhi Crossed Ang1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedAngry1.png", horizontal=True)
    image Haruhi Crossed Ang2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedAngry2.png", horizontal=True)
    image Haruhi Crossed Ang3 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedAngry3.png", horizontal=True)
    image Haruhi Crossed Hap1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedHappy1.png", horizontal=True)
    image Haruhi Crossed Hap2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedHappy2.png", horizontal=True)
    image Haruhi Crossed Hap3 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedHappy3.png", horizontal=True)
    image Haruhi Crossed Hap4 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedHappy4.png", horizontal=True)
    image Haruhi Crossed Pout1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedPout1.png", horizontal=True)
    image Haruhi Crossed Pout1 Bright Flip = im.Flip(im.MatrixColor("Sprites/Haruhi/HaruhiCrossedPout1.png",
                                       im.matrix.brightness(.5)), horizontal=True)
    image Haruhi Crossed Pout2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedPout2.png", horizontal=True)
    image Haruhi Crossed Eyeroll1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedEyeroll1.png", horizontal=True)
    image Haruhi Crossed Eyeroll2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedEyeroll2.png", horizontal=True)
    image Haruhi Crossed Quest1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedQuestion1.png", horizontal=True)
    image Haruhi Crossed Grin1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedGrin1.png", horizontal=True)
    image Haruhi Crossed Grin2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedGrin2.png", horizontal=True)
    image Haruhi Crossed Worry1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedWorry1.png", horizontal=True)
    image Haruhi Crossed Worry2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedWorry2.png", horizontal=True)
    image Haruhi Crossed Smile1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSmile1.png", horizontal=True)
    image Haruhi Crossed Smile2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSmile2.png", horizontal=True)
    image Haruhi Crossed Smile3 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSmile3.png", horizontal=True)
    image Haruhi Crossed Sigh1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSigh1.png", horizontal=True)
    image Haruhi Crossed Sigh2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedSigh2.png", horizontal=True)
    image Haruhi Crossed Tsun1 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedTsun1.png", horizontal=True)
    image Haruhi Crossed Tsun2 Flip = im.Flip("Sprites/Haruhi/HaruhiCrossedTsun2.png", horizontal=True)
   
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
    image Kyon Sigh6 = "Sprites/Kyon/KyonSigh6.png"
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
    image Kyon Smile6 = "Sprites/Kyon/KyonSmile6.png"
    image Kyon Smile7 = "Sprites/Kyon/KyonSmile7.png"
    image Kyon Worry1 = "Sprites/Kyon/KyonWorry1.png"
    image Kyon Worry2 = "Sprites/Kyon/KyonWorry2.png"
    image Kyon Worry3 = "Sprites/Kyon/KyonWorry3.png"
    image Kyon Puzzle1 = "Sprites/Kyon/KyonPuzzled1.png"
    image Kyon Puzzle2 = "Sprites/Kyon/KyonPuzzled2.png"
    image Kyon Sup1 = "Sprites/Kyon/KyonSurprised1.png"
    image Kyon Sup2 = "Sprites/Kyon/KyonSurprised2.png"
    image Kyon Sup3 = "Sprites/Kyon/KyonSurprised3.png"
    image Kyon Sup4 = "Sprites/Kyon/KyonSurprised4.png"
    image Kyon Unhap1 ="Sprites/Kyon/KyonUnhappy1.png"
    image Kyon Unhap2 ="Sprites/Kyon/KyonUnhappy2.png"
    image Kyon Unhap3 ="Sprites/Kyon/KyonUnhappy3.png"
    image Kyon Unhap4 ="Sprites/Kyon/KyonUnhappy4.png"
    image Kyon Unhap5 ="Sprites/Kyon/KyonUnhappy5.png"
    image Kyon Unhap6 ="Sprites/Kyon/KyonUnhappy6.png"
    image Kyon Evil1 ="Sprites/Kyon/KyonEvil1.png"
    
    image Kyon Blink:
        "Sprites/Kyon/KyonSigh6.png"
        0.2
        "Sprites/Kyon/KyonSerious1.png"
    
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
    image Kyon Casual Sigh6 = "Sprites/Kyon/KyonCasualSigh6.png"
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
    image Kyon Casual Smile6 = "Sprites/Kyon/KyonCasualSmile6.png"
    image Kyon Casual Smile7 = "Sprites/Kyon/KyonCasualSmile7.png"
    image Kyon Casual Worry1 = "Sprites/Kyon/KyonCasualWorry1.png"
    image Kyon Casual Worry2 = "Sprites/Kyon/KyonCasualWorry2.png"
    image Kyon Casual Worry3 = "Sprites/Kyon/KyonCasualWorry3.png"
    image Kyon Casual Puzzle1 = "Sprites/Kyon/KyonCasualPuzzled1.png"
    image Kyon Casual Puzzle2 = "Sprites/Kyon/KyonCasualPuzzled2.png"
    image Kyon Casual Sup1 = "Sprites/Kyon/KyonCasualSurprised1.png"
    image Kyon Casual Sup2 = "Sprites/Kyon/KyonCasualSurprised2.png"
    image Kyon Casual Unhap1 ="Sprites/Kyon/KyonCasualUnhappy1.png"
    image Kyon Casual Unhap2 ="Sprites/Kyon/KyonCasualUnhappy2.png"
    image Kyon Casual Unhap3 ="Sprites/Kyon/KyonCasualUnhappy3.png"
    image Kyon Casual Unhap4 ="Sprites/Kyon/KyonCasualUnhappy4.png"
    image Kyon Casual Unhap5 ="Sprites/Kyon/KyonCasualUnhappy5.png"
    image Kyon Casual Unhap6 ="Sprites/Kyon/KyonCasualUnhappy6.png"
    image Kyon Casual Evil1 ="Sprites/Kyon/KyonCasualEvil1.png"
    
    image Ksweat = "Sprites/Kyon/KyonSweat1.png"
    image Skinsuit = "Sprites/Kyon/KyonSkinsuitTemplate.png"
    image Skinsuit Bright = im.MatrixColor("Sprites/Kyon/KyonSkinsuitTemplate.png",
                                       im.matrix.brightness(.5))
    image Coat Bright = im.MatrixColor("Sprites/Kyon/KyonCoat.png",
                                       im.matrix.brightness(.5))
    image Coat = "Sprites/Kyon/KyonCoat.png"
    
    image KTears = "Sprites/Kyon/Ktears.png"
    image KBlush = "Sprites/Kyon/KBlush.png"
    image KBlush Casual = "Sprites/Kyon/KBlushCasual.png"
    image KPaper = "Sprites/Kyon/KyonPaper.png"
    
    image Kcut Clotted = "Sprites/Kyon/cheekcut/clotted.png"
    image Kcut Scar = "Sprites/Kyon/cheekcut/scar.png"
    image Kcut Fresh1 = "Sprites/Kyon/cheekcut/fresh1.png"
    image Kcut Fresh2 = "Sprites/Kyon/cheekcut/fresh2.png"
    image Kcut Running1 = "Sprites/Kyon/cheekcut/running1.png"
    image Kcut Running2 = "Sprites/Kyon/cheekcut/running2.png"
    image Kcut Running3 = "Sprites/Kyon/cheekcut/running3.png"
    image Kcut Running4 = "Sprites/Kyon/cheekcut/running4.png"
    image Kcut Bandage = "Sprites/Kyon/cheekcut/bandage.png"
    
    image KBrow 1 ="Sprites/Kyon/cheekcut/spliteyebrow5.png"
    image KBrow 2 ="Sprites/Kyon/cheekcut/spliteyebrow4.png"
    image KBrow 3 ="Sprites/Kyon/cheekcut/spliteyebrow3.png"
    image KBrow 4 ="Sprites/Kyon/cheekcut/spliteyebrow1.png"
    image KBrow Smudge = "Sprites/Kyon/cheekcut/spliteyebrowsmudge.png"
    image Kbrow Bandage = "Sprites/Kyon/cheekcut/bandage2.png"
    
    image KBrow 1 Flip = im.Flip("Sprites/Kyon/cheekcut/spliteyebrow5.png", horizontal=True)
    image KBrow 2 Flip = im.Flip("Sprites/Kyon/cheekcut/spliteyebrow4.png", horizontal=True)
    image KBrow 3 Flip = im.Flip("Sprites/Kyon/cheekcut/spliteyebrow3.png", horizontal=True)
    image KBrow 4 Flip = im.Flip("Sprites/Kyon/cheekcut/spliteyebrow1.png", horizontal=True)
    image KBrow Smudge Flip = im.Flip("Sprites/Kyon/cheekcut/spliteyebrowsmudge.png", horizontal=True)
    
    image Kcut Clotted Flip =  im.Flip("Sprites/Kyon/cheekcut/clotted.png", horizontal=True)
    image Kcut Fresh1 Flip =  im.Flip("Sprites/Kyon/cheekcut/fresh1.png", horizontal=True)
    image Kcut Fresh2 Flip =  im.Flip("Sprites/Kyon/cheekcut/fresh2.png", horizontal=True)
    image Kcut Running1 Flip =  im.Flip("Sprites/Kyon/cheekcut/running1.png", horizontal=True)
    image Kcut Running2 Flip = im.Flip( "Sprites/Kyon/cheekcut/running2.png", horizontal=True)
    image Kcut Running3 Flip =  im.Flip("Sprites/Kyon/cheekcut/running3.png", horizontal=True)
    image Kcut Running4 Flip =  im.Flip("Sprites/Kyon/cheekcut/running4.png", horizontal=True)
    image Kcut Bandage Flip =  im.Flip("Sprites/Kyon/cheekcut/bandage.png", horizontal=True)
    
    #Kyon image flips
    image Kyon Ang1 Flip = im.Flip("Sprites/Kyon/KyonAngry1.png", horizontal=True)
    image Kyon Ang2 Flip = im.Flip("Sprites/Kyon/KyonAngry2.png", horizontal=True)
    image Kyon Ang3 Flip = im.Flip("Sprites/Kyon/KyonAngry3.png", horizontal=True)
    image Kyon Ang4 Flip = im.Flip("Sprites/Kyon/KyonAngry4.png", horizontal=True)
    image Kyon Neutral1 Flip = im.Flip("Sprites/Kyon/KyonNeutral1.png", horizontal=True)
    image Kyon Neutral2 Flip = im.Flip("Sprites/Kyon/KyonNeutral2.png", horizontal=True)
    image Kyon Neutral3 Flip = im.Flip("Sprites/Kyon/KyonNeutral3.png", horizontal=True)
    image Kyon Neutral4 Flip = im.Flip("Sprites/Kyon/KyonNeutral4.png", horizontal=True)
    image Kyon Neutral5 Flip = im.Flip("Sprites/Kyon/KyonNeutral5.png", horizontal=True)
    image Kyon Sigh1 Flip = im.Flip("Sprites/Kyon/KyonSigh1.png", horizontal=True)
    image Kyon Sigh2 Flip = im.Flip("Sprites/Kyon/KyonSigh2.png", horizontal=True)
    image Kyon Sigh3 Flip = im.Flip("Sprites/Kyon/KyonSigh3.png", horizontal=True)
    image Kyon Sigh4 Flip = im.Flip("Sprites/Kyon/KyonSigh4.png", horizontal=True)
    image Kyon Sigh5 Flip = im.Flip("Sprites/Kyon/KyonSigh5.png", horizontal=True)
    image Kyon Sigh6 Flip = im.Flip("Sprites/Kyon/KyonSigh6.png", horizontal=True)
    image Kyon Sigh7 Flip = im.Flip("Sprites/Kyon/KyonSigh7.png", horizontal=True)
    image Kyon Puzzle1 Flip = im.Flip("Sprites/Kyon/KyonPuzzled1.png", horizontal=True)
    image Kyon Puzzle2 Flip = im.Flip("Sprites/Kyon/KyonPuzzled2.png", horizontal=True)
    image Kyon Smile1 Flip = im.Flip("Sprites/Kyon/KyonSmile1.png", horizontal=True)
    image Kyon Smile2 Flip = im.Flip("Sprites/Kyon/KyonSmile2.png", horizontal=True)
    image Kyon Smile3 Flip = im.Flip("Sprites/Kyon/KyonSmile3.png", horizontal=True)
    image Kyon Smile4 Flip = im.Flip("Sprites/Kyon/KyonSmile4.png", horizontal=True)
    image Kyon Smile5 Flip = im.Flip("Sprites/Kyon/KyonSmile5.png", horizontal=True)
    image Kyon Smile6 Flip = im.Flip("Sprites/Kyon/KyonSmile6.png", horizontal=True)
    image Kyon Smile7 Flip = im.Flip("Sprites/Kyon/KyonSmile7.png", horizontal=True)
    image Kyon Ser1 Flip = im.Flip("Sprites/Kyon/KyonSerious1.png", horizontal=True)
    image Kyon Ser2 Flip = im.Flip("Sprites/Kyon/KyonSerious2.png", horizontal=True)
    image Kyon Ser3 Flip = im.Flip("Sprites/Kyon/KyonSerious3.png", horizontal=True)
    image Kyon Sup1 Flip = im.Flip("Sprites/Kyon/KyonSurprised2.png", horizontal=True)
    image Kyon Sup2 Flip = im.Flip("Sprites/Kyon/KyonSurprised2.png", horizontal=True)
    image Kyon Sup3 Flip = im.Flip("Sprites/Kyon/KyonSurprised3.png", horizontal=True)
    image Kyon Sup4 Flip = im.Flip("Sprites/Kyon/KyonSurprised4.png", horizontal=True)
    image Kyon Unhap1 Flip = im.Flip("Sprites/Kyon/KyonUnhappy1.png", horizontal=True)
    image Kyon Unhap2 Flip = im.Flip("Sprites/Kyon/KyonUnhappy2.png", horizontal=True)
    image Kyon Unhap3 Flip = im.Flip("Sprites/Kyon/KyonUnhappy3.png", horizontal=True)
    image Kyon Unhap4 Flip = im.Flip("Sprites/Kyon/KyonUnhappy4.png", horizontal=True)
    image Kyon Unhap5 Flip = im.Flip("Sprites/Kyon/KyonUnhappy5.png", horizontal=True)
    image Kyon Unhap6 Flip = im.Flip("Sprites/Kyon/KyonUnhappy6.png", horizontal=True)
    image Kyon Worry1 Flip = im.Flip("Sprites/Kyon/KyonWorry1.png", horizontal=True)
    image Kyon Worry2 Flip = im.Flip("Sprites/Kyon/KyonWorry2.png", horizontal=True)
    image Kyon Worry3 Flip = im.Flip("Sprites/Kyon/KyonWorry3.png", horizontal=True)
    image Kyon Pain1 Flip = im.Flip("Sprites/Kyon/KyonPained1.png", horizontal=True)
    image Kyon Pain2 Flip = im.Flip("Sprites/Kyon/KyonPained2.png", horizontal=True)
    image Kyon Evil1 Flip = im.Flip("Sprites/Kyon/KyonEvil1.png", horizontal=True)
    
    image Kyon Casual Ang Flip = im.Flip("Sprites/Kyon/KyonCasualAngry1.png", horizontal=True)
    image Kyon Casual Ang2 Flip = im.Flip("Sprites/Kyon/KyonCasualAngry2.png", horizontal=True)
    image Kyon Casual Ang3 Flip = im.Flip("Sprites/Kyon/KyonCasualAngry3.png", horizontal=True)
    image Kyon Casual Ang4 Flip = im.Flip("Sprites/Kyon/KyonCasualAngry4.png", horizontal=True)
    image Kyon Casual Neutral1 Flip = im.Flip("Sprites/Kyon/KyonCasualNeutral1.png", horizontal=True)
    image Kyon Casual Neutral2 Flip = im.Flip("Sprites/Kyon/KyonCasualNeutral2.png", horizontal=True)
    image Kyon Casual Neutral3 Flip = im.Flip("Sprites/Kyon/KyonCasualNeutral3.png", horizontal=True)
    image Kyon Casual Neutral4 Flip = im.Flip("Sprites/Kyon/KyonCasualNeutral4.png", horizontal=True)
    image Kyon Casual Neutral5 Flip = im.Flip("Sprites/Kyon/KyonCasualNeutral5.png", horizontal=True)
    image Kyon Casual Sigh1 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh1.png", horizontal=True)
    image Kyon Casual Sigh2 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh2.png", horizontal=True)
    image Kyon Casual Sigh3 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh3.png", horizontal=True)
    image Kyon Casual Sigh4 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh4.png", horizontal=True)
    image Kyon Casual Sigh5 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh5.png", horizontal=True)
    image Kyon Casual Sigh6 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh6.png", horizontal=True)
    image Kyon Casual Sigh7 Flip = im.Flip("Sprites/Kyon/KyonCasualSigh7.png", horizontal=True)
    image Kyon Casual Puzzle1 Flip = im.Flip("Sprites/Kyon/KyonCasualPuzzled1.png", horizontal=True)
    image Kyon Casual Puzzle2 Flip = im.Flip("Sprites/Kyon/KyonCasualPuzzled2.png", horizontal=True)
    image Kyon Casual Smile1 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile1.png", horizontal=True)
    image Kyon Casual Smile2 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile2.png", horizontal=True)
    image Kyon Casual Smile3 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile3.png", horizontal=True)
    image Kyon Casual Smile4 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile4.png", horizontal=True)
    image Kyon Casual Smile5 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile5.png", horizontal=True)
    image Kyon Casual Smile6 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile6.png", horizontal=True)
    image Kyon Casual Smile7 Flip = im.Flip("Sprites/Kyon/KyonCasualSmile7.png", horizontal=True)
    image Kyon Casual Ser1 Flip = im.Flip("Sprites/Kyon/KyonCasualSerious1.png", horizontal=True)
    image Kyon Casual Ser2 Flip = im.Flip("Sprites/Kyon/KyonCasualSerious2.png", horizontal=True)
    image Kyon Casual Ser3 Flip = im.Flip("Sprites/Kyon/KyonCasualSerious3.png", horizontal=True)
    image Kyon Casual Sup1 Flip = im.Flip("Sprites/Kyon/KyonCasualSurprised2.png", horizontal=True)
    image Kyon Casual Sup2 Flip = im.Flip("Sprites/Kyon/KyonCasualSurprised2.png", horizontal=True)
    image Kyon Casual Unhap1 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy1.png", horizontal=True)
    image Kyon Casual Unhap2 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy2.png", horizontal=True)
    image Kyon Casual Unhap3 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy3.png", horizontal=True)
    image Kyon Casual Unhap4 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy4.png", horizontal=True)
    image Kyon Casual Unhap5 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy5.png", horizontal=True)
    image Kyon Casual Unhap6 Flip = im.Flip("Sprites/Kyon/KyonCasualUnhappy6.png", horizontal=True)
    image Kyon Casual Worry1 Flip = im.Flip("Sprites/Kyon/KyonCasualWorry1.png", horizontal=True)
    image Kyon Casual Worry2 Flip = im.Flip("Sprites/Kyon/KyonCasualWorry2.png", horizontal=True)
    image Kyon Casual Worry3 Flip = im.Flip("Sprites/Kyon/KyonCasualWorry3.png", horizontal=True)
    image Kyon Casual Pain1 Flip = im.Flip("Sprites/Kyon/KyonCasualPained1.png", horizontal=True)
    image Kyon Casual Pain2 Flip = im.Flip("Sprites/Kyon/KyonCasualPained2.png", horizontal=True)
    image Kyon Casual Evil1 Flip = im.Flip("Sprites/Kyon/KyonCasualEvil1.png", horizontal=True)
    
    image Ksweat Flip = im.Flip("Sprites/Kyon/KyonSweat1.png", horizontal=True)
    
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
    image Yuki Ang1 = "Sprites/Yuki/YukiSideAngry1.png"
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
    image Yuki Casual Ang1 = "Sprites/Yuki/YukiSideCasualAngry1.png"
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
        
    #Yuki Image Flips    
    image Yuki Side1 Flip = im.Flip("Sprites/Yuki/YukiSide1.png", horizontal=True)
    image Yuki Side2 Flip = im.Flip("Sprites/Yuki/YukiSide2.png", horizontal=True)
    image Yuki SideDisappointed1 Flip = im.Flip("Sprites/Yuki/YukiSideDisappointed1.png", horizontal=True)
    image Yuki SideDisappointedTalk1 Flip = im.Flip("Sprites/Yuki/YukiSideDisappointedTalk1.png", horizontal=True)
    image Yuki SideEyesClosed1 Flip = im.Flip("Sprites/Yuki/YukiSideEyesClosed1.png", horizontal=True)
    image Yuki Ang1 Flip = im.Flip("Sprites/Yuki/YukiSideAngry1.png", horizontal=True)
    image Yuki Talk1 Flip = im.Flip("Sprites/Yuki/YukiSideTalk1.png", horizontal=True)
    image Yuki Talk2 Flip = im.Flip("Sprites/Yuki/YukiSideTalk2.png", horizontal=True)
    image Yuki Sad1 Flip = im.Flip("Sprites/Yuki/YukiSideSad1.png", horizontal=True)
    image Yuki Sad2 Flip = im.Flip("Sprites/Yuki/YukiSideSad2.png", horizontal=True)
    image Yuki Sad3 Flip = im.Flip("Sprites/Yuki/YukiSideSad3.png", horizontal=True)
    image Yuki SadTalk1 Flip = im.Flip("Sprites/Yuki/YukiSideSadTalk1.png", horizontal=True)
    image Yuki SadTalk2 Flip = im.Flip("Sprites/Yuki/YukiSideSadTalk2.png", horizontal=True)
    image Yuki SadTalk3 Flip = im.Flip("Sprites/Yuki/YukiSideSadTalk3.png", horizontal=True)
        
    image Yuki Casual Side1 Flip = im.Flip("Sprites/Yuki/YukiSideCasual1.png", horizontal=True)
    image Yuki Casual Side2 Flip = im.Flip("Sprites/Yuki/YukiSideCasual2.png", horizontal=True)
    image Yuki Casual Ang1 Flip = im.Flip("Sprites/Yuki/YukiSideCasualAngry1.png", horizontal=True)
    image Yuki Casual Talk1 Flip = im.Flip("Sprites/Yuki/YukiSideCasualTalk1.png", horizontal=True)
    image Yuki Casual Talk2 Flip = im.Flip("Sprites/Yuki/YukiSideCasualTalk2.png", horizontal=True)
    image Yuki Casual Sad1 Flip = im.Flip("Sprites/Yuki/YukiSideCasualSad1.png", horizontal=True)
    image Yuki Casual Sad2 Flip = im.Flip("Sprites/Yuki/YukiSideCasualSad2.png", horizontal=True)
    image Yuki Casual Sad3 Flip = im.Flip("Sprites/Yuki/YukiSideCasualSad3.png", horizontal=True)
    image Yuki Casual SadTalk2 Flip = im.Flip("Sprites/Yuki/YukiSideCasualSadTalk2.png", horizontal=True)
    image Yuki Casual SadTalk3 Flip = im.Flip("Sprites/Yuki/YukiSideCasualSadTalk3.png", horizontal=True)
    
    image Yuki Chair1 Flip = im.Flip("Sprites/Yuki/YukiChair1.png", horizontal=True)
    image Yuki Chair2 Flip = im.Flip("Sprites/Yuki/YukiChair2.png", horizontal=True)
    image Yuki Chair3 Flip = im.Flip("Sprites/Yuki/YukiChair3.png", horizontal=True)
    image Yuki Chair4 Flip = im.Flip("Sprites/Yuki/YukiChair4.png", horizontal=True)
    
    image Yuki Right Neutral1 Flip = im.Flip("Sprites/Yuki/YukiRightNeutral1.png", horizontal=True)
    image Yuki Right Neutral2 Flip = im.Flip("Sprites/Yuki/YukiRightNeutral2.png", horizontal=True)
    image Yuki Right Talk1 Flip = im.Flip("Sprites/Yuki/YukiRightTalk1.png", horizontal=True)
    image Yuki Right Talk2 Flip = im.Flip("Sprites/Yuki/YukiRightTalk2.png", horizontal=True)
    
    image Yuki Right Casual Neutral1 = im.Flip("Sprites/Yuki/YukiRightCasualNeutral1.png", horizontal=True)
    image Yuki Right Casual Neutral2 = im.Flip("Sprites/Yuki/YukiRightCasualNeutral2.png", horizontal=True)
    image Yuki Right Casual Talk1 = im.Flip("Sprites/Yuki/YukiRightCasualTalk1.png", horizontal=True)
    image Yuki Right Casual Talk2 = im.Flip("Sprites/Yuki/YukiRightCasualTalk2.png", horizontal=True)
        
        # Mikuru Sprites 
    image Mikuru Hap1 = "Sprites/Mikuru/MikuruHappy1.png"
    image Mikuru Hap2 = "Sprites/Mikuru/MikuruHappy2.png"
    image Mikuru Neutral1 = "Sprites/Mikuru/MikuruNeutral1.png"
    image Mikuru Neutral2 = "Sprites/Mikuru/MikuruNeutral2.png"
    image Mikuru Neutral3 = "Sprites/Mikuru/MikuruNeutral3.png"
    image Mikuru Sad1 = "Sprites/Mikuru/MikuruSad1.png"
    image Mikuru Sad2 = "Sprites/Mikuru/MikuruSad2.png"
    image Mikuru Sad3 = "Sprites/Mikuru/MikuruSad3.png"
    image Mikuru Sigh1 = "Sprites/Mikuru/MikuruSigh1.png"
    image Mikuru Sigh2 = "Sprites/Mikuru/MikuruSigh2.png"
    image Mikuru Ser1 = "Sprites/Mikuru/MikuruSerious1.png"
    image Mikuru Ser2 = "Sprites/Mikuru/MikuruSerious2.png"
    image Mikuru Ser3 = "Sprites/Mikuru/MikuruSerious3.png"
    image Mikuru Smile1 = "Sprites/Mikuru/MikuruSmile1.png"
    image Mikuru Smile2 = "Sprites/Mikuru/MikuruSmile2.png"
    image Mikuru Smile3 = "Sprites/Mikuru/MikuruSmile3.png"
    image Mikuru Sup1 = "Sprites/Mikuru/MikuruSurprised1.png"
    image Mikuru Quest1 = "Sprites/Mikuru/MikuruQuestion1.png"
    image Mikuru Quest2 = "Sprites/Mikuru/MikuruQuestion2.png"
    image Mikuru Unhap1 = "Sprites/Mikuru/MikuruUnhappy1.png"
    image Mikuru Unhap2 = "Sprites/Mikuru/MikuruUnhappy2.png"
    image Mikuru Unhap3 = "Sprites/Mikuru/MikuruUnhappy3.png"
    image MBlush1 = "Sprites/Mikuru/MBlush1.png"
  
    image Mikuru Casual Hap1 = "Sprites/Mikuru/MikuruCasualHappy1.png"
    image Mikuru Casual Hap2 = "Sprites/Mikuru/MikuruCasualHappy2.png"
    image Mikuru Casual Neutral1 = "Sprites/Mikuru/MikuruCasualNeutral1.png"
    image Mikuru Casual Neutral2 = "Sprites/Mikuru/MikuruCasualNeutral2.png"
    image Mikuru Casual Neutral3 = "Sprites/Mikuru/MikuruCasualNeutral3.png"
    image Mikuru Casual Sad1 = "Sprites/Mikuru/MikuruCasualSad1.png"
    image Mikuru Casual Sad2 = "Sprites/Mikuru/MikuruCasualSad2.png"
    image Mikuru Casual Sad3 = "Sprites/Mikuru/MikuruCasualSad3.png"
    image Mikuru Casual Sigh1 = "Sprites/Mikuru/MikuruCasualSigh1.png"
    image Mikuru Casual Sigh2 = "Sprites/Mikuru/MikuruCasualSigh2.png"
    image Mikuru Casual Ser1 = "Sprites/Mikuru/MikuruCasualSerious1.png"
    image Mikuru Casual Ser2 = "Sprites/Mikuru/MikuruCasualSerious2.png"
    image Mikuru Casual Ser3 = "Sprites/Mikuru/MikuruCasualSerious3.png"
    image Mikuru Casual Smile1 = "Sprites/Mikuru/MikuruCasualSmile1.png"
    image Mikuru Casual Smile2 = "Sprites/Mikuru/MikuruCasualSmile2.png"
    image Mikuru Casual Smile3 = "Sprites/Mikuru/MikuruCasualSmile3.png"
    image Mikuru Casual Sup1 = "Sprites/Mikuru/MikuruCasualSurprised1.png"
    image Mikuru Casual Quest1 = "Sprites/Mikuru/MikuruCasualQuestion1.png"
    image Mikuru Casual Quest2 = "Sprites/Mikuru/MikuruCasualQuestion2.png"
    image Mikuru Casual Unhap1 = "Sprites/Mikuru/MikuruCasualUnhappy1.png"
    image Mikuru Casual Unhap2 = "Sprites/Mikuru/MikuruCasualUnhappy2.png"
    image Mikuru Casual Unhap3 = "Sprites/Mikuru/MikuruCasualUnhappy3.png"
    image MBlush1 Casual = "Sprites/Mikuru/MBlushCasual1.png"
    
    image Mikuru Maid Hap1 = "Sprites/Mikuru/MikuruMaidHappy1.png"
    image Mikuru Maid Hap2 = "Sprites/Mikuru/MikuruMaidHappy2.png"
    image Mikuru Maid Neutral1 = "Sprites/Mikuru/MikuruMaidNeutral1.png"
    image Mikuru Maid Neutral2 = "Sprites/Mikuru/MikuruMaidNeutral2.png"
    image Mikuru Maid Neutral3 = "Sprites/Mikuru/MikuruMaidNeutral3.png"
    image Mikuru Maid Sad1 = "Sprites/Mikuru/MikuruMaidSad1.png"
    image Mikuru Maid Sad2 = "Sprites/Mikuru/MikuruMaidSad2.png"
    image Mikuru Maid Sad3 = "Sprites/Mikuru/MikuruMaidSad3.png"
    image Mikuru Maid Sigh1 = "Sprites/Mikuru/MikuruMaidSigh1.png"
    image Mikuru Maid Sigh2 = "Sprites/Mikuru/MikuruMaidSigh2.png"
    image Mikuru Maid Ser1 = "Sprites/Mikuru/MikuruMaidSerious1.png"
    image Mikuru Maid Ser2 = "Sprites/Mikuru/MikuruMaidSerious2.png"
    image Mikuru Maid Ser3 = "Sprites/Mikuru/MikuruMaidSerious3.png"
    image Mikuru Maid Smile1 = "Sprites/Mikuru/MikuruMaidSmile1.png"
    image Mikuru Maid Smile2 = "Sprites/Mikuru/MikuruMaidSmile2.png"
    image Mikuru Maid Smile3 = "Sprites/Mikuru/MikuruMaidSmile3.png"
    image Mikuru Maid Sup1 = "Sprites/Mikuru/MikuruMaidSurprised1.png"
    image Mikuru Maid Quest1 = "Sprites/Mikuru/MikuruMaidQuestion1.png"
    image Mikuru Maid Quest2 = "Sprites/Mikuru/MikuruMaidQuestion2.png"
    image Mikuru Maid Unhap1 = "Sprites/Mikuru/MikuruMaidUnhappy1.png"
    image Mikuru Maid Unhap2 = "Sprites/Mikuru/MikuruMaidUnhappy2.png"
    image Mikuru Maid Unhap3 = "Sprites/Mikuru/MikuruMaidUnhappy3.png"
    image MBlush1 Maid = "Sprites/Mikuru/MBlushMaid1.png"
    image MTray Maid ="Sprites/Mikuru/MTrayMaid.png"
    
    image Mikuru Think Quest1 = "Sprites/Mikuru/MikuruThinkQuestion1.png"
    image Mikuru Think Quest2 = "Sprites/Mikuru/MikuruThinkQuestion2.png"
    image Mikuru Think Quest3 = "Sprites/Mikuru/MikuruThinkQuestion3.png"
    image Mikuru Think Quest4 = "Sprites/Mikuru/MikuruThinkQuestion4.png"
    image Mikuru Think Sad1 = "Sprites/Mikuru/MikuruThinkSad1.png"
    image Mikuru Think Sad2 = "Sprites/Mikuru/MikuruThinkSad2.png"
    image Mikuru Think Sad3 = "Sprites/Mikuru/MikuruThinkSad3.png"
    image Mikuru Think Sad4 = "Sprites/Mikuru/MikuruThinkSad4.png"
    image Mikuru Think Sad5 = "Sprites/Mikuru/MikuruThinkSad5.png"
    image Mikuru Think Sup1 = "Sprites/Mikuru/MikuruThinkSurprised1.png"
    image Mikuru Think Sup2 = "Sprites/Mikuru/MikuruThinkSurprised2.png"
    
    image Mikuru Think Casual Quest1 = "Sprites/Mikuru/MikuruThinkCasualQuestion1.png"
    image Mikuru Think Casual Quest2 = "Sprites/Mikuru/MikuruThinkCasualQuestion2.png"
    image Mikuru Think Casual Quest3 = "Sprites/Mikuru/MikuruThinkCasualQuestion3.png"
    image Mikuru Think Casual Quest4 = "Sprites/Mikuru/MikuruThinkCasualQuestion4.png"
    image Mikuru Think Casual Sad1 = "Sprites/Mikuru/MikuruThinkCasualSad1.png"
    image Mikuru Think Casual Sad2 = "Sprites/Mikuru/MikuruThinkCasualSad2.png"
    image Mikuru Think Casual Sad3 = "Sprites/Mikuru/MikuruThinkCasualSad3.png"
    image Mikuru Think Casual Sad4 = "Sprites/Mikuru/MikuruThinkCasualSad4.png"
    image Mikuru Think Casual Sad5 = "Sprites/Mikuru/MikuruThinkCasualSad5.png"
    image Mikuru Think Casual Sup1 = "Sprites/Mikuru/MikuruThinkCasualSurprised1.png"
    image Mikuru Think Casual Sup2 = "Sprites/Mikuru/MikuruThinkCasualSurprised2.png"
    
    image Mikuru Think Maid Quest1 = "Sprites/Mikuru/MikuruThinkMaidQuestion1.png"
    image Mikuru Think Maid Quest2 = "Sprites/Mikuru/MikuruThinkMaidQuestion2.png"
    image Mikuru Think Maid Quest3 = "Sprites/Mikuru/MikuruThinkMaidQuestion3.png"
    image Mikuru Think Maid Quest4 = "Sprites/Mikuru/MikuruThinkMaidQuestion4.png"
    image Mikuru Think Maid Sad1 = "Sprites/Mikuru/MikuruThinkMaidSad1.png"
    image Mikuru Think Maid Sad2 = "Sprites/Mikuru/MikuruThinkMaidSad2.png"
    image Mikuru Think Maid Sad3 = "Sprites/Mikuru/MikuruThinkMaidSad3.png"
    image Mikuru Think Maid Sad4 = "Sprites/Mikuru/MikuruThinkMaidSad4.png"
    image Mikuru Think Maid Sad5 = "Sprites/Mikuru/MikuruThinkMaidSad5.png"
    image Mikuru Think Maid Sup1 = "Sprites/Mikuru/MikuruThinkMaidSurprised1.png"
    image Mikuru Think Maid Sup2 = "Sprites/Mikuru/MikuruThinkMaidSurprised2.png"
    image MTears Think = "Sprites/Mikuru/MTearsThink1.png"
    image MBlush Think = "Sprites/Mikuru/MBlushThink1.png"
    
    image Mikuru Think Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkQuestion1.png", horizontal=True)
    image Mikuru Think Quest2 Flip = im.Flip("Sprites/Mikuru/MikuruThinkQuestion2.png", horizontal=True)
    image Mikuru Think Quest3 Flip = im.Flip("Sprites/Mikuru/MikuruThinkQuestion3.png", horizontal=True)
    image Mikuru Think Casual Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkCasualQuestion1.png", horizontal=True)
    image Mikuru Think Casual Quest2 Flip = im.Flip("Sprites/Mikuru/MikuruThinkCasualQuestion2.png", horizontal=True)
    image Mikuru Think Casual Quest3 Flip = im.Flip("Sprites/Mikuru/MikuruThinkCasualQuestion3.png", horizontal=True)
    image Mikuru Think Maid Quest1 Flip = im.Flip("Sprites/Mikuru/MikuruThinkMaidQuestion1.png", horizontal=True)
    image Mikuru Think Maid Quest2 Flip = im.Flip("Sprites/Mikuru/MikuruThinkMaidQuestion2.png", horizontal=True)
    image Mikuru Think Maid Quest3 Flip = im.Flip("Sprites/Mikuru/MikuruThinkMaidQuestion3.png", horizontal=True)
    image MBlush Think Flip = im.Flip("Sprites/Mikuru/MBlushThink1.png", horizontal=True)
    
    image Mikuru Cower Nervous1 = "Sprites/Mikuru/MikuruCowerNervous1.png"
    image Mikuru Cower Nervous2 = "Sprites/Mikuru/MikuruCowerNervous2.png"
    image Mikuru Cower Nervous3 = "Sprites/Mikuru/MikuruCowerNervous3.png"
    image Mikuru Cower Neutral1 = "Sprites/Mikuru/MikuruCowerNeutral1.png"
    image Mikuru Cower Sup1 = "Sprites/Mikuru/MikuruCowerSurprised1.png"
    image Mikuru Cower Sigh1 = "Sprites/Mikuru/MikuruCowerSigh1.png"
    image Mikuru Cower Sigh2 = "Sprites/Mikuru/MikuruCowerSigh2.png"
    image Mikuru Cower Wince1 = "Sprites/Mikuru/MikuruCowerWince1.png"
    image Mikuru Cower Quest1 = "Sprites/Mikuru/MikuruCowerQuestion1.png"
    image Mikuru Cower Smile1 ="Sprites/Mikuru/MikuruCowerSmile1.png"
    image Mikuru Cower Smile2 ="Sprites/Mikuru/MikuruCowerSmile2.png"
    image Mikuru Cower Unhap1 = "Sprites/Mikuru/MikuruCowerUnhappy1.png"
    image Mikuru Cower Worry1 = "Sprites/Mikuru/MikuruCowerWorry1.png"
    
    image MBlush Cower = "Sprites/Mikuru/MikuruCowerBlush.png"
    image MBlush Cower Casual = "Sprites/Mikuru/MikuruCowerCasualBlush.png"
    image MBlush Cower Towel = "Sprites/Mikuru/MblushCowerTowel.png"
    image MTears = "Sprites/Mikuru/MTearsCower1.png"
    
    image Mikuru Cower Casual Nervous1 = "Sprites/Mikuru/MikuruCowerCasualNervous1.png"
    image Mikuru Cower Casual Nervous2 = "Sprites/Mikuru/MikuruCowerCasualNervous2.png"
    image Mikuru Cower Casual Nervous3 = "Sprites/Mikuru/MikuruCowerCasualNervous3.png"
    image Mikuru Cower Casual Neutral1 = "Sprites/Mikuru/MikuruCowerCasualNeutral1.png"
    image Mikuru Cower Casual Sup1 = "Sprites/Mikuru/MikuruCowerCasualSurprised1.png"
    image Mikuru Cower Casual Sigh1 = "Sprites/Mikuru/MikuruCowerCasualSigh1.png"
    image Mikuru Cower Casual Sigh2 = "Sprites/Mikuru/MikuruCowerCasualSigh2.png"
    image Mikuru Cower Casual Wince1 = "Sprites/Mikuru/MikuruCowerCasualWince1.png"
    image Mikuru Cower Casual Quest1 = "Sprites/Mikuru/MikuruCowerCasualQuestion1.png"
    image Mikuru Cower Casual Smile1 ="Sprites/Mikuru/MikuruCowerCasualSmile1.png"
    image Mikuru Cower Casual Smile2 ="Sprites/Mikuru/MikuruCowerCasualSmile2.png"
    image Mikuru Cower Casual Unhap1 = "Sprites/Mikuru/MikuruCowerCasualUnhappy1.png"
    image Mikuru Cower Casual Worry1 = "Sprites/Mikuru/MikuruCowerCasualWorry1.png"
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
    
    image Mikuru Cower Towel Wince1 = "Sprites/Mikuru/MikuruCowerTowelWince1.png"
    image Mikuru Cower Towel Quest1 = "Sprites/Mikuru/MikuruCowerTowelQuest1.png"
    image Mikuru Cower Towel Nervous1 = "Sprites/Mikuru/MikuruCowerTowelNervous1.png"
    image Mikuru Cower Towel Nervous3 = "Sprites/Mikuru/MikuruCowerTowelNervous3.png"
    image Mikuru Cower Towel Sup2 = "Sprites/Mikuru/MikuruCowerTowelSurprised2.png"
    image Mikuru Cower Towel Unhap1 = "Sprites/Mikuru/MikuruCowerTowelUnhappy1.png"
    image Mikuru Cower Towel Worry1 = "Sprites/Mikuru/MikuruCowerTowelWorry1.png"
    image Mikuru Cower Towel Smile2 ="Sprites/Mikuru/MikuruCowerTowelSmile2.png"
    
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
    image MikuruBig Quest2 = "Sprites/MikuruBig/MikuruBigQuestion2.png"
    image MikuruBig Sad1 = "Sprites/MikuruBig/MikuruBigSad1.png"
    image MikuruBig Sad2 = "Sprites/MikuruBig/MikuruBigSad2.png"
    image MikuruBig Ser1 = "Sprites/MikuruBig/MikuruBigSerious1.png"
    image MikuruBig Ser2 = "Sprites/MikuruBig/MikuruBigSerious2.png"
    image MikuruBig Sigh1 = "Sprites/MikuruBig/MikuruBigSigh1.png"
    image MikuruBig Smile1 = "Sprites/MikuruBig/MikuruBigSmile1.png"
    image MikuruBig Smile2 = "Sprites/MikuruBig/MikuruBigSmile2.png"
    image MikuruBig Smile3 = "Sprites/MikuruBig/MikuruBigSmile3.png"
    image MikuruBig Sup1 = "Sprites/MikuruBig/MikuruBigSurprised1.png"
    image MikuruBig Sup2 = "Sprites/MikuruBig/MikuruBigSurprised2.png"
    image MikuruBig Sup3 = "Sprites/MikuruBig/MikuruBigSurprised3.png"
    image MikuruBig Worry1 = "Sprites/MikuruBig/MikuruBigWorry1.png"
    image MikuruBig Worry2 = "Sprites/MikuruBig/MikuruBigWorry2.png"
    
    image MBigBlush1 = "Sprites/MikuruBig/MBigBlush1.png"
    
    image MSew = "Sprites/Mikuru/MikuruSew.png"
    
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
    image Tsuruya Ang3 = "Sprites/Tsuruya/TsuruyaAngry3.png"
    image Tsuruya Ang4 = "Sprites/Tsuruya/TsuruyaAngry4.png"
    image Tsuruya Grin1 = "Sprites/Tsuruya/TsuruyaGrin1.png"
    image Tsuruya Grin2 = "Sprites/Tsuruya/TsuruyaGrin2.png"
    image Tsuruya Grin3 = "Sprites/Tsuruya/TsuruyaGrin3.png"
    image Tsuruya Grin4 = "Sprites/Tsuruya/TsuruyaGrin4.png"
    image Tsuruya Grin5 = "Sprites/Tsuruya/TsuruyaGrin5.png"
    image Tsuruya Grin6 = "Sprites/Tsuruya/TsuruyaGrin6.png"
    image Tsuruya Hap1 = "Sprites/Tsuruya/TsuruyaHappy1.png"
    image Tsuruya Hap2 = "Sprites/Tsuruya/TsuruyaHappy2.png"
    image Tsuruya Hap3 = "Sprites/Tsuruya/TsuruyaHappy3.png"
    image Tsuruya Hap4 = "Sprites/Tsuruya/TsuruyaHappy4.png"
    image Tsuruya Hap5 = "Sprites/Tsuruya/TsuruyaHappy5.png"
    image Tsuruya Hap6 = "Sprites/Tsuruya/TsuruyaHappy6.png"
    image Tsuruya Hap7 = "Sprites/Tsuruya/TsuruyaHappy7.png"
    image Tsuruya Hap8 = "Sprites/Tsuruya/TsuruyaHappy8.png"
    image Tsuruya Hap9 = "Sprites/Tsuruya/TsuruyaHappy9.png"
    image Tsuruya Laugh1 = "Sprites/Tsuruya/TsuruyaLaugh1.png"
    image Tsuruya Laugh2 = "Sprites/Tsuruya/TsuruyaLaugh2.png"
    image Tsuruya Quest1 = "Sprites/Tsuruya/TsuruyaQuestion1.png"
    image Tsuruya Quest2 = "Sprites/Tsuruya/TsuruyaQuestion2.png"
    image Tsuruya Sigh1 = "Sprites/Tsuruya/TsuruyaSigh1.png"
    image Tsuruya Sigh2 = "Sprites/Tsuruya/TsuruyaSigh2.png"
    image Tsuruya Sigh3 = "Sprites/Tsuruya/TsuruyaSigh3.png"
    image Tsuruya Sigh3 = "Sprites/Tsuruya/TsuruyaSigh3.png"
    image Tsuruya Sigh4 = "Sprites/Tsuruya/TsuruyaSigh4.png"
    image Tsuruya Sigh5 = "Sprites/Tsuruya/TsuruyaSigh5.png"
    image Tsuruya Smile1 = "Sprites/Tsuruya/TsuruyaSmile1.png"
    image Tsuruya Smile2 = "Sprites/Tsuruya/TsuruyaSmile2.png"
    image Tsuruya Smile3 = "Sprites/Tsuruya/TsuruyaSmile3.png"
    image Tsuruya Smile4 = "Sprites/Tsuruya/TsuruyaSmile4.png"
    image Tsuruya Smile5 = "Sprites/Tsuruya/TsuruyaSmile5.png"
    image Tsuruya Smile6 = "Sprites/Tsuruya/TsuruyaSmile6.png"
    image Tsuruya Sup1 = "Sprites/Tsuruya/TsuruyaSurprised1.png"
    image Tsuruya Worry1 = "Sprites/Tsuruya/TsuruyaWorry1.png"
    image Tsuruya Worry2 = "Sprites/Tsuruya/TsuruyaWorry2.png"
    image Tsuruya Worry3 = "Sprites/Tsuruya/TsuruyaWorry3.png"
    image Tsuruya Neutral1 = "Sprites/Tsuruya/TsuruyaNeutral1.png"
    image Tsuruya Neutral2 = "Sprites/Tsuruya/TsuruyaNeutral2.png"
    image Tsuruya Susp1 = "Sprites/Tsuruya/TsuruyaSuspicious1.png"
    image Tsuruya Susp2 = "Sprites/Tsuruya/TsuruyaSuspicious2.png"
    image Tsuruya Ser1 = "Sprites/Tsuruya/TsuruyaSerious1.png"
    image Tsuruya Ser2 = "Sprites/Tsuruya/TsuruyaSerious2.png"
    image Tsuruya Sad1 = "Sprites/Tsuruya/TsuruyaSad1.png"
    
    image Tsuruya Casual Ang1 = "Sprites/Tsuruya/TsuruyaCasualAngry1.png"
    image Tsuruya Casual Ang2 = "Sprites/Tsuruya/TsuruyaCasualAngry2.png"
    image Tsuruya Casual Ang3 = "Sprites/Tsuruya/TsuruyaCasualAngry3.png"
    image Tsuruya Casual Ang4 = "Sprites/Tsuruya/TsuruyaCasualAngry4.png"
    image Tsuruya Casual Grin1 = "Sprites/Tsuruya/TsuruyaCasualGrin1.png"
    image Tsuruya Casual Grin2 = "Sprites/Tsuruya/TsuruyaCasualGrin2.png"
    image Tsuruya Casual Grin3 = "Sprites/Tsuruya/TsuruyaCasualGrin3.png"
    image Tsuruya Casual Grin4 = "Sprites/Tsuruya/TsuruyaCasualGrin4.png"
    image Tsuruya Casual Grin5 = "Sprites/Tsuruya/TsuruyaCasualGrin5.png"
    image Tsuruya Casual Grin6 = "Sprites/Tsuruya/TsuruyaCasualGrin6.png"
    image Tsuruya Casual Hap1 = "Sprites/Tsuruya/TsuruyaCasualHappy1.png"
    image Tsuruya Casual Hap2 = "Sprites/Tsuruya/TsuruyaCasualHappy2.png"
    image Tsuruya Casual Hap3 = "Sprites/Tsuruya/TsuruyaCasualHappy3.png"
    image Tsuruya Casual Hap4 = "Sprites/Tsuruya/TsuruyaCasualHappy4.png"
    image Tsuruya Casual Hap5 = "Sprites/Tsuruya/TsuruyaCasualHappy5.png"
    image Tsuruya Casual Hap6 = "Sprites/Tsuruya/TsuruyaCasualHappy6.png"
    image Tsuruya Casual Hap7 = "Sprites/Tsuruya/TsuruyaCasualHappy7.png"
    image Tsuruya Casual Laugh1 = "Sprites/Tsuruya/TsuruyaCasualLaugh1.png"
    image Tsuruya Casual Laugh2 = "Sprites/Tsuruya/TsuruyaCasualLaugh2.png"
    image Tsuruya Casual Quest1 = "Sprites/Tsuruya/TsuruyaCasualQuestion1.png"
    image Tsuruya Casual Quest2 = "Sprites/Tsuruya/TsuruyaCasualQuestion2.png"
    image Tsuruya Casual Sigh1 = "Sprites/Tsuruya/TsuruyaCasualSigh1.png"
    image Tsuruya Casual Sigh2 = "Sprites/Tsuruya/TsuruyaCasualSigh2.png"
    image Tsuruya Casual Sigh3 = "Sprites/Tsuruya/TsuruyaCasualSigh3.png"
    image Tsuruya Casual Sigh4 = "Sprites/Tsuruya/TsuruyaCasualSigh4.png"
    image Tsuruya Casual Smile1 = "Sprites/Tsuruya/TsuruyaCasualSmile1.png"
    image Tsuruya Casual Smile2 = "Sprites/Tsuruya/TsuruyaCasualSmile2.png"
    image Tsuruya Casual Smile3 = "Sprites/Tsuruya/TsuruyaCasualSmile3.png"
    image Tsuruya Casual Smile4 = "Sprites/Tsuruya/TsuruyaCasualSmile4.png"
    image Tsuruya Casual Smile5 = "Sprites/Tsuruya/TsuruyaCasualSmile5.png"
    image Tsuruya Casual Smile6 = "Sprites/Tsuruya/TsuruyaCasualSmile6.png"
    image Tsuruya Casual Sup1 = "Sprites/Tsuruya/TsuruyaCasualSurprised1.png"
    image Tsuruya Casual Worry1 = "Sprites/Tsuruya/TsuruyaCasualWorry1.png"
    image Tsuruya Casual Worry2 = "Sprites/Tsuruya/TsuruyaCasualWorry2.png"
    image Tsuruya Casual Worry3 = "Sprites/Tsuruya/TsuruyaCasualWorry3.png"
    image Tsuruya Casual Neutral1 = "Sprites/Tsuruya/TsuruyaCasualNeutral1.png"
    image Tsuruya Casual Neutral2 = "Sprites/Tsuruya/TsuruyaCasualNeutral2.png"
    image Tsuruya Casual Susp1 = "Sprites/Tsuruya/TsuruyaCasualSuspicious1.png"
    image Tsuruya Casual Ser1 = "Sprites/Tsuruya/TsuruyaCasualSerious1.png"
    image Tsuruya Casual Sad1 = "Sprites/Tsuruya/TsuruyaCasualSad1.png"
    
    image Tsuruya Wave Grin1 = "Sprites/Tsuruya/TsuruyaWaveGrin1.png"
    image Tsuruya Wave Grin2 = "Sprites/Tsuruya/TsuruyaWaveGrin2.png"
    image Tsuruya Wave Grin3 = "Sprites/Tsuruya/TsuruyaWaveGrin3.png"
    image Tsuruya Wave Hap1 = "Sprites/Tsuruya/TsuruyaWaveHappy1.png"
    image Tsuruya Wave Hap2 = "Sprites/Tsuruya/TsuruyaWaveHappy2.png"
    image Tsuruya Wave Hap3 = "Sprites/Tsuruya/TsuruyaWaveHappy3.png"
    image Tsuruya Wave Hap4 = "Sprites/Tsuruya/TsuruyaWaveHappy4.png"
    image Tsuruya Wave Hap5 = "Sprites/Tsuruya/TsuruyaWaveHappy5.png"
    image Tsuruya Wave Hap6 = "Sprites/Tsuruya/TsuruyaWaveHappy6.png"
    image Tsuruya Wave Hap7 = "Sprites/Tsuruya/TsuruyaWaveHappy7.png"
    image Tsuruya Wave Quest1 = "Sprites/Tsuruya/TsuruyaWaveQuestion1.png"
    image Tsuruya Wave Quest2 = "Sprites/Tsuruya/TsuruyaWaveQuestion2.png"
    image Tsuruya Wave Smile1 = "Sprites/Tsuruya/TsuruyaWaveSmile1.png"
    image Tsuruya Wave Smile2 = "Sprites/Tsuruya/TsuruyaWaveSmile2.png"
    image Tsuruya Wave Sigh1 = "Sprites/Tsuruya/TsuruyaWaveSigh1.png"
    image Tsuruya Wave Ser1 = "Sprites/Tsuruya/TsuruyaWaveSerious1.png"
    image Tsuruya Wave Ser2 = "Sprites/Tsuruya/TsuruyaWaveSerious2.png"
    
    image Tsuruya Kimono Grin1 = "Sprites/Tsuruya/TsuruyaKimonoGrin1.png"
    image Tsuruya Kimono Grin2 = "Sprites/Tsuruya/TsuruyaKimonoGrin2.png"
    image Tsuruya Kimono Grin3 = "Sprites/Tsuruya/TsuruyaKimonoGrin3.png"
    image Tsuruya Kimono Hap1 = "Sprites/Tsuruya/TsuruyaKimonoHappy1.png"
    image Tsuruya Kimono Hap2 = "Sprites/Tsuruya/TsuruyaKimonoHappy2.png"
    image Tsuruya Kimono Hap3 = "Sprites/Tsuruya/TsuruyaKimonoHappy3.png"
    image Tsuruya Kimono Hap4 = "Sprites/Tsuruya/TsuruyaKimonoHappy4.png"
    image Tsuruya Kimono Hap5 = "Sprites/Tsuruya/TsuruyaKimonoHappy5.png"
    image Tsuruya Kimono Hap6 = "Sprites/Tsuruya/TsuruyaKimonoHappy6.png"
    image Tsuruya Kimono Hap7 = "Sprites/Tsuruya/TsuruyaKimonoHappy7.png"
    image Tsuruya Kimono Quest1 = "Sprites/Tsuruya/TsuruyaKimonoQuestion1.png"
    image Tsuruya Kimono Quest2 = "Sprites/Tsuruya/TsuruyaKimonoQuestion2.png"
    image Tsuruya Kimono Smile1 = "Sprites/Tsuruya/TsuruyaKimonoSmile1.png"
    image Tsuruya Kimono Smile2 = "Sprites/Tsuruya/TsuruyaKimonoSmile2.png"
    image Tsuruya Kimono Sigh1 = "Sprites/Tsuruya/TsuruyaKimonoSigh1.png"
    image Tsuruya Kimono Ser1 = "Sprites/Tsuruya/TsuruyaKimonoSerious1.png"
    image Tsuruya Kimono Ser2 = "Sprites/Tsuruya/TsuruyaKimonoSerious2.png"
    
    image Tsuruya Laugh Ang1  = "Sprites/Tsuruya/TsuruyaLaughAngry1.png"
    image Tsuruya Laugh Ang2  = "Sprites/Tsuruya/TsuruyaLaughAngry2.png"
    image Tsuruya Laugh Unhap1  = "Sprites/Tsuruya/TsuruyaLaughUnhapp1.png"
    image Tsuruya Laugh Pain1 = "Sprites/Tsuruya/TsuruyaLaughPain1.png"
    image Tsuruya Laugh Pain2 = "Sprites/Tsuruya/TsuruyaLaughPain2.png"
    image Tsuruya Laugh Pain3 = "Sprites/Tsuruya/TsuruyaLaughPain3.png"
    image Tsuruya Laugh Pain4 = "Sprites/Tsuruya/TsuruyaLaughPain4.png"
    image Tsuruya Laugh Sad1 = "Sprites/Tsuruya/TsuruyaLaughSad1.png"
    
    image Tsuruya Laugh Casual Ang1  = "Sprites/Tsuruya/TsuruyaLaughCasualAngry1.png"
    image Tsuruya Laugh Casual Ang2  = "Sprites/Tsuruya/TsuruyaLaughCasualAngry2.png"
    image Tsuruya Laugh Casual Unhap1  = "Sprites/Tsuruya/TsuruyaLaughCasualUnhappy1.png"
    image Tsuruya Laugh Casual Pain1 = "Sprites/Tsuruya/TsuruyaLaughCasualPain1.png"
    image Tsuruya Laugh Casual Pain2 = "Sprites/Tsuruya/TsuruyaLaughCasualPain2.png"
    image Tsuruya Laugh Casual Pain3 = "Sprites/Tsuruya/TsuruyaLaughCasualPain3.png"
    image Tsuruya Laugh Casual Pain4 = "Sprites/Tsuruya/TsuruyaLaughCasualPain4.png"
    image Tsuruya Laugh Casual Sad1 = "Sprites/Tsuruya/TsuruyaLaughCasualSad1.png"
   
    image TBlush = "Sprites/Tsuruya/TBlush.png"
    image Tsweat = "Sprites/Tsuruya/Tsweat.png"
    image Tsweat Casual = "Sprites/Tsuruya/TsweatCasual.png"
    
    image Tsweat Laugh = "Sprites/Tsuruya/TsweatLaugh.png"
    image Tsweat Laugh Casual = "Sprites/Tsuruya/TsweatLaughCasual.png"
    
    #Tsuruya image flips
    image Tsuruya Grin1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin1.png", horizontal=True)
    image Tsuruya Grin2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin2.png", horizontal=True)
    image Tsuruya Grin3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin3.png", horizontal=True)
    image Tsuruya Grin4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin4.png", horizontal=True)
    image Tsuruya Grin5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin5.png", horizontal=True)
    image Tsuruya Grin6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaGrin6.png", horizontal=True)
    image Tsuruya Smile1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile1.png", horizontal=True)
    image Tsuruya Smile2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile2.png", horizontal=True)
    image Tsuruya Smile3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile3.png", horizontal=True)
    image Tsuruya Smile4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile4.png", horizontal=True)
    image Tsuruya Smile5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile5.png", horizontal=True)
    image Tsuruya Smile6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSmile6.png", horizontal=True)
    image Tsuruya Quest1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaQuestion1.png", horizontal=True)
    image Tsuruya Quest2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaQuestion2.png", horizontal=True)
    image Tsuruya Ser1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSerious1.png", horizontal=True)
    image Tsuruya Ser2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSerious2.png", horizontal=True)
    image Tsuruya Sigh1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSigh1.png", horizontal=True)
    image Tsuruya Sigh2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSigh2.png", horizontal=True)
    image Tsuruya Sigh3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSigh3.png", horizontal=True)
    image Tsuruya Sigh4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSigh4.png", horizontal=True)
    image Tsuruya Sigh5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSigh5.png", horizontal=True)
    image Tsuruya Sup1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSurprised1.png", horizontal=True)
    image Tsuruya Worry1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaWorry1.png", horizontal=True)
    image Tsuruya Worry2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaWorry2.png", horizontal=True)
    image Tsuruya Worry3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaWorry3.png", horizontal=True)
    image Tsuruya Neutral1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaNeutral1.png", horizontal=True)
    image Tsuruya Neutral2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaNeutral2.png", horizontal=True)
    image Tsuruya Hap1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy1.png", horizontal=True)
    image Tsuruya Hap2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy2.png", horizontal=True)
    image Tsuruya Hap3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy3.png", horizontal=True)
    image Tsuruya Hap4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy4.png", horizontal=True)
    image Tsuruya Hap5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy5.png", horizontal=True)
    image Tsuruya Hap6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy6.png", horizontal=True)
    image Tsuruya Hap7 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy7.png", horizontal=True)
    image Tsuruya Hap8 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy8.png", horizontal=True)
    image Tsuruya Hap9 Flip = im.Flip("Sprites/Tsuruya/TsuruyaHappy9.png", horizontal=True)
    image Tsuruya Ang1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaAngry1.png", horizontal=True)
    image Tsuruya Ang2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaAngry2.png", horizontal=True)
    image Tsuruya Ang3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaAngry3.png", horizontal=True)
    image Tsuruya Ang4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaAngry4.png", horizontal=True)
    image Tsuruya Susp1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSuspicious1.png", horizontal=True)
    image Tsuruya Susp2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaSuspicious2.png", horizontal=True)
    
    image Tsuruya Casual Grin1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin1.png", horizontal=True)
    image Tsuruya Casual Grin2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin2.png", horizontal=True)
    image Tsuruya Casual Grin3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin3.png", horizontal=True)
    image Tsuruya Casual Grin4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin4.png", horizontal=True)
    image Tsuruya Casual Grin5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin5.png", horizontal=True)
    image Tsuruya Casual Grin6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualGrin6.png", horizontal=True)
    image Tsuruya Casual Smile1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile1.png", horizontal=True)
    image Tsuruya Casual Smile2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile2.png", horizontal=True)
    image Tsuruya Casual Smile3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile3.png", horizontal=True)
    image Tsuruya Casual Smile4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile4.png", horizontal=True)
    image Tsuruya Casual Smile5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile5.png", horizontal=True)
    image Tsuruya Casual Smile6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSmile6.png", horizontal=True)
    image Tsuruya Casual Quest1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualQuestion1.png", horizontal=True)
    image Tsuruya Casual Ser1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSerious1.png", horizontal=True)
    image Tsuruya Casual Ser2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSerious2.png", horizontal=True)
    image Tsuruya Casual Sigh1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSigh1.png", horizontal=True)
    image Tsuruya Casual Sigh2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSigh2.png", horizontal=True)
    image Tsuruya Casual Sigh3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSigh3.png", horizontal=True)
    image Tsuruya Casual Sigh4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSigh4.png", horizontal=True)
    image Tsuruya Casual Sup1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualSurprised1.png", horizontal=True)
    image Tsuruya Casual Worry1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualWorry1.png", horizontal=True)
    image Tsuruya Casual Worry2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualWorry2.png", horizontal=True)
    image Tsuruya Casual Worry3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualWorry3.png", horizontal=True)
    image Tsuruya Casual Neutral1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualNeutral1.png", horizontal=True)
    image Tsuruya Casual Hap1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy1.png", horizontal=True)
    image Tsuruya Casual Hap2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy2.png", horizontal=True)
    image Tsuruya Casual Hap3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy3.png", horizontal=True)
    image Tsuruya Casual Hap4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy4.png", horizontal=True)
    image Tsuruya Casual Hap5 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy5.png", horizontal=True)
    image Tsuruya Casual Hap6 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy6.png", horizontal=True)
    image Tsuruya Casual Hap7 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualHappy7.png", horizontal=True)
    image Tsuruya Casual Ang1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualAngry1.png", horizontal=True)
    image Tsuruya Casual Ang2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualAngry2.png", horizontal=True)
    image Tsuruya Casual Ang3 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualAngry3.png", horizontal=True)
    image Tsuruya Casual Ang4 Flip = im.Flip("Sprites/Tsuruya/TsuruyaCasualAngry4.png", horizontal=True)
    
    image Tsuruya Laugh Ang1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughAngry1.png", horizontal=True)
    image Tsuruya Laugh Ang2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughAngry2.png", horizontal=True)
    image Tsuruya Laugh Unhap1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughUnhappy1.png", horizontal=True)
    image Tsuruya Laugh Pain1 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughPain1.png", horizontal=True)
    image Tsuruya Laugh Pain2 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughPain2.png", horizontal=True)
    image Tsuruya Laugh Pain3 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughPain3.png", horizontal=True)
    image Tsuruya Laugh Pain4 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughPain4.png", horizontal=True)
    image Tsuruya Laugh Sad1 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughSad1.png", horizontal=True)
    
    image Tsuruya Laugh Casual Ang1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualAngry1.png", horizontal=True)
    image Tsuruya Laugh Casual Ang2 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualAngry2.png", horizontal=True)
    image Tsuruya Laugh Casual Unhap1 Flip = im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualUnhappy1.png", horizontal=True)
    image Tsuruya Laugh Casual Pain1 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualPain1.png", horizontal=True)
    image Tsuruya Laugh Casual Pain2 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualPain2.png", horizontal=True)
    image Tsuruya Laugh Casual Pain3 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualPain3.png", horizontal=True)
    image Tsuruya Laugh Casual Pain4 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualPain4.png", horizontal=True)
    image Tsuruya Laugh Casual Sad1 Flip =  im.Flip("Sprites/Tsuruya/TsuruyaLaughCasualSad1.png", horizontal=True)
    
    image Tsweat Flip = im.Flip("Sprites/Tsuruya/Tsweat.png", horizontal=True)
    image Tsweat Casual Flip = im.Flip("Sprites/Tsuruya/TsweatCasual.png", horizontal=True)
    
    image Tsweat Laugh Flip = im.Flip("Sprites/Tsuruya/TsweatLaugh.png", horizontal=True)
    image Tsweat Laugh Casual Flip = im.Flip("Sprites/Tsuruya/TsweatLaughCasual.png", horizontal=True)
    
    #Kanae Sprites
    image Kanae Hap1 = "Sprites/Kanae/KanaeHappy1.png"
    image Kanae Hap2 = "Sprites/Kanae/KanaeHappy2.png"
    image Kanae Hap3 = "Sprites/Kanae/KanaeHappy3.png"
    image Kanae Hap4 = "Sprites/Kanae/KanaeHappy4.png"
    image Kanae Neutral1 = "Sprites/Kanae/KanaeNeutral1.png"
    image Kanae Quest1 = "Sprites/Kanae/KanaeQuestion1.png"
    image Kanae Quest2 = "Sprites/Kanae/KanaeQuestion2.png"
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
    
    image Kanae Night Hap1 = "Sprites/Kanae/KanaeNightHappy1.png"
    image Kanae Night Hap2 = "Sprites/Kanae/KanaeNightHappy2.png"
    image Kanae Night Hap3 = "Sprites/Kanae/KanaeNightHappy3.png"
    image Kanae Night Hap4 = "Sprites/Kanae/KanaeNightHappy4.png"
    image Kanae Night Neutral1 = "Sprites/Kanae/KanaeNightNeutral1.png"
    image Kanae Night Quest1 = "Sprites/Kanae/KanaeNightQuestion1.png"
    image Kanae Night Quest2 = "Sprites/Kanae/KanaeNightQuestion2.png"
    image Kanae Night Sad1 = "Sprites/Kanae/KanaeNightSad1.png"
    image Kanae Night Sad2 = "Sprites/Kanae/KanaeNightSad2.png"
    image Kanae Night Sad3 = "Sprites/Kanae/KanaeNightSad3.png"
    image Kanae Night Sad4 = "Sprites/Kanae/KanaeNightSad4.png"
    image Kanae Night Sad5 = "Sprites/Kanae/KanaeNightSad5.png"
    image Kanae Night Smile1 = "Sprites/Kanae/KanaeNightSmile1.png"
    image Kanae Night Smile2 = "Sprites/Kanae/KanaeNightSmile2.png"
    image Kanae Night Smile3 = "Sprites/Kanae/KanaeNightSmile3.png"
    image Kanae Night Sup1 = "Sprites/Kanae/KanaeNightSurprised1.png"
    image Kanae Night Sup2 = "Sprites/Kanae/KanaeNightSurprised2.png"
    image Kanae Night Unhap1 = "Sprites/Kanae/KanaeNightUnhappy1.png"
    image Kanae Night Unhap2 = "Sprites/Kanae/KanaeNightUnhappy2.png"
    image Kanae Night Unhap3 = "Sprites/Kanae/KanaeNightUnhappy3.png"
    image Kanae Night Wince1 = "Sprites/Kanae/KanaeNightWince1.png"
    image Kanae Night Wince2 = "Sprites/Kanae/KanaeNightWince2.png"
    image Kanae Night Worry1 = "Sprites/Kanae/KanaeNightWorry1.png"
    image Kanae Night Worry2 = "Sprites/Kanae/KanaeNightWorry2.png"
    image Kanae Night Worry3 = "Sprites/Kanae/KanaeNightWorry3.png"
    
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
    image Koizumi Think Smile2 = "Sprites/Koizumi/KoizumiThinkSmile2.png"
    image Koizumi Think Sigh1 = "Sprites/Koizumi/KoizumiThinkSigh1.png"
    image Koizumi Think Sigh2 = "Sprites/Koizumi/KoizumiThinkSigh2.png"
    image Koizumi Think Worry1 = "Sprites/Koizumi/KoizumiThinkWorry1.png"
    
    image Koizumi Think Casual Ser1 = "Sprites/Koizumi/KoizumiThinkCasualSerious1.png"
    image Koizumi Think Casual Ser2 = "Sprites/Koizumi/KoizumiThinkCasualSerious2.png"
    image Koizumi Think Casual Ser3 = "Sprites/Koizumi/KoizumiThinkCasualSerious3.png"
    image Koizumi Think Casual Ser4 = "Sprites/Koizumi/KoizumiThinkCasualSerious4.png"
    image Koizumi Think Casual Grin1 = "Sprites/Koizumi/KoizumiThinkCasualGrin1.png"
    image Koizumi Think Casual Grin2 = "Sprites/Koizumi/KoizumiThinkCasualGrin2.png"
    image Koizumi Think Casual Sup1 = "Sprites/Koizumi/KoizumiThinkCasualSurprised1.png"
    image Koizumi Think Casual Smile1 = "Sprites/Koizumi/KoizumiThinkCasualSmile1.png"
    image Koizumi Think Casual Smile2 = "Sprites/Koizumi/KoizumiThinkCasualSmile2.png"
    image Koizumi Think Casual Sigh1 = "Sprites/Koizumi/KoizumiThinkCasualSigh1.png"
    image Koizumi Think Casual Sigh2 = "Sprites/Koizumi/KoizumiThinkCasualSigh2.png"
    image Koizumi Think Casual Worry1 = "Sprites/Koizumi/KoizumiThinkCasualWorry1.png"
    
    image Koizumi Crossed Hap1 = "Sprites/Koizumi/KoizumiCrossedHappy1.png"
    image Koizumi Crossed Hap2 = "Sprites/Koizumi/KoizumiCrossedHappy2.png"
    image Koizumi Crossed Ser1 = "Sprites/Koizumi/KoizumiCrossedSerious1.png"
    image Koizumi Crossed Ser2 = "Sprites/Koizumi/KoizumiCrossedSerious2.png"
    image Koizumi Crossed Smile1 = "Sprites/Koizumi/KoizumiCrossedSmile1.png"
    image Koizumi Crossed Smile2 = "Sprites/Koizumi/KoizumiCrossedSmile2.png"
    image Koizumi Crossed Smile3 = "Sprites/Koizumi/KoizumiCrossedSmile3.png"
    image Koizumi Crossed Smile4 = "Sprites/Koizumi/KoizumiCrossedSmile4.png"
    image Koizumi Crossed Uneasy1 = "Sprites/Koizumi/KoizumiCrossedUneasy1.png"
    image Koizumi Crossed Uneasy2 = "Sprites/Koizumi/KoizumiCrossedUneasy2.png"
    image Koizumi Crossed Uneasy3 = "Sprites/Koizumi/KoizumiCrossedUneasy3.png"
    image Koizumi Crossed Sigh1 = "Sprites/Koizumi/KoizumiCrossedSigh1.png"
    image Koizumi Crossed Sigh2 = "Sprites/Koizumi/KoizumiCrossedSigh2.png"
    image Koizumi Crossed Sigh3 = "Sprites/Koizumi/KoizumiCrossedSigh3.png"
    image Koizumi Crossed Sigh4 = "Sprites/Koizumi/KoizumiCrossedSigh4.png"
    image Koizumi Crossed Neutral1 = "Sprites/Koizumi/KoizumiCrossedNeutral1.png"
    image Koizumi Crossed Neutral2 = "Sprites/Koizumi/KoizumiCrossedNeutral2.png"
    
    image Koizumi Crossed Casual Hap1 = "Sprites/Koizumi/KoizumiCrossedCasualHappy1.png"
    image Koizumi Crossed Casual Hap2 = "Sprites/Koizumi/KoizumiCrossedCasualHappy2.png"
    image Koizumi Crossed Casual Ser1 = "Sprites/Koizumi/KoizumiCrossedCasualSerious1.png"
    image Koizumi Crossed Casual Ser2 = "Sprites/Koizumi/KoizumiCrossedCasualSerious2.png"
    image Koizumi Crossed Casual Smile1 = "Sprites/Koizumi/KoizumiCrossedCasualSmile1.png"
    image Koizumi Crossed Casual Smile2 = "Sprites/Koizumi/KoizumiCrossedCasualSmile2.png"
    image Koizumi Crossed Casual Smile3 = "Sprites/Koizumi/KoizumiCrossedCasualSmile3.png"
    image Koizumi Crossed Casual Smile4 = "Sprites/Koizumi/KoizumiCrossedCasualSmile4.png"
    image Koizumi Crossed Casual Uneasy1 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy1.png"
    image Koizumi Crossed Casual Uneasy2 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy2.png"
    image Koizumi Crossed Casual Uneasy3 = "Sprites/Koizumi/KoizumiCrossedCasualUneasy3.png"
    image Koizumi Crossed Casual Sigh1 = "Sprites/Koizumi/KoizumiCrossedCasualSigh1.png"
    image Koizumi Crossed Casual Sigh2 = "Sprites/Koizumi/KoizumiCrossedCasualSigh2.png"
    image Koizumi Crossed Casual Sigh3 = "Sprites/Koizumi/KoizumiCrossedCasualSigh3.png"
    image Koizumi Crossed Casual Sigh4 = "Sprites/Koizumi/KoizumiCrossedCasualSigh4.png"
    image Koizumi Crossed Casual Neutral1 = "Sprites/Koizumi/KoizumiCrossedCasualNeutral1.png"
    image Koizumi Crossed Casual Neutral2 = "Sprites/Koizumi/KoizumiCrossedCasualNeutral2.png"
    
    #Koizumi image flips
    image Koizumi Shrug Sigh1 Flip = im.Flip("Sprites/Koizumi/KoizumiShrugSigh1.png", horizontal=True)
    image Koizumi Shrug Smile1 Flip = im.Flip("Sprites/Koizumi/KoizumiShrugSmile1.png", horizontal=True)
    
    image Koizumi Think Ser1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSerious1.png", horizontal=True)
    image Koizumi Think Ser2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSerious2.png", horizontal=True)
    image Koizumi Think Ser3 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSerious3.png", horizontal=True)
    image Koizumi Think Ser4 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSerious4.png", horizontal=True)
    image Koizumi Think Grin1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkGrin1.png", horizontal=True)
    image Koizumi Think Grin2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkGrin2.png", horizontal=True)
    image Koizumi Think Sup1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSurprised1.png", horizontal=True)
    image Koizumi Think Smile1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSmile1.png", horizontal=True)
    image Koizumi Think Smile2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSmile2.png", horizontal=True)
    image Koizumi Think Sigh1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSigh1.png", horizontal=True)
    image Koizumi Think Sigh2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkSigh2.png", horizontal=True)
    image Koizumi Think Worry1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkWorry1.png", horizontal=True)
    
    image Koizumi Think Casual Ser1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSerious1.png", horizontal=True)
    image Koizumi Think Casual Ser2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSerious2.png", horizontal=True)
    image Koizumi Think Casual Ser3 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSerious3.png", horizontal=True)
    image Koizumi Think Casual Ser4 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSerious4.png", horizontal=True)
    image Koizumi Think Casual Grin1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualGrin1.png", horizontal=True)
    image Koizumi Think Casual Grin2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualGrin2.png", horizontal=True)
    image Koizumi Think Casual Sup1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSurprised1.png", horizontal=True)
    image Koizumi Think Casual Smile1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSmile1.png", horizontal=True)
    image Koizumi Think Casual Smile2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSmile2.png", horizontal=True)
    image Koizumi Think Casual Sigh1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSigh1.png", horizontal=True)
    image Koizumi Think Casual Sigh2 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualSigh2.png", horizontal=True)
    image Koizumi Think Casual Worry1 Flip = im.Flip("Sprites/Koizumi/KoizumiThinkCasualWorry1.png", horizontal=True)
    
    image Koizumi Crossed Hap1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedHappy1.png", horizontal=True)
    image Koizumi Crossed Hap2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedHappy2.png", horizontal=True)
    image Koizumi Crossed Ser1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSerious1.png", horizontal=True)
    image Koizumi Crossed Ser2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSerious2.png", horizontal=True)
    image Koizumi Crossed Smile1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSmile1.png", horizontal=True)
    image Koizumi Crossed Smile2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSmile2.png", horizontal=True)
    image Koizumi Crossed Smile3 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSmile3.png", horizontal=True)
    image Koizumi Crossed Smile4 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSmile4.png", horizontal=True)
    image Koizumi Crossed Uneasy1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedUneasy1.png", horizontal=True)
    image Koizumi Crossed Uneasy2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedUneasy2.png", horizontal=True)
    image Koizumi Crossed Uneasy3 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedUneasy3.png", horizontal=True)
    image Koizumi Crossed Sigh1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSigh1.png", horizontal=True)
    image Koizumi Crossed Sigh2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSigh2.png", horizontal=True)
    image Koizumi Crossed Sigh3 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSigh3.png", horizontal=True)
    image Koizumi Crossed Sigh4 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedSigh4.png", horizontal=True)
    image Koizumi Crossed Neutral1 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedNeutral1.png", horizontal=True)
    image Koizumi Crossed Neutral2 Flip = im.Flip("Sprites/Koizumi/KoizumiCrossedNeutral2.png", horizontal=True)
    
    #Taniguchi Sprites
    image Taniguchi Grin1 = "Sprites/Taniguchi/TaniguchiGrin1.png"
    image Taniguchi Grin2 = "Sprites/Taniguchi/TaniguchiGrin2.png"
    image Taniguchi Sup1 = "Sprites/Taniguchi/TaniguchiSurprised1.png"
    image Taniguchi Sup2 = "Sprites/Taniguchi/TaniguchiSurprised2.png"
    image Taniguchi Smile1 = "Sprites/Taniguchi/TaniguchiSmile1.png"
    image Taniguchi Hap1 = "Sprites/Taniguchi/TaniguchiHappy1.png"
    image Taniguchi Hap2 = "Sprites/Taniguchi/TaniguchiHappy2.png"
    image Taniguchi Ser1 = "Sprites/Taniguchi/TaniguchiSerious1.png"
    image Taniguchi Ser2 = "Sprites/Taniguchi/TaniguchiSerious2.png"
    image Taniguchi Ser3 = "Sprites/Taniguchi/TaniguchiSerious3.png"
    image Taniguchi Ser4 = "Sprites/Taniguchi/TaniguchiSerious4.png"
    image Taniguchi Sigh1 = "Sprites/Taniguchi/TaniguchiSigh1.png"
    image Taniguchi Sigh2 = "Sprites/Taniguchi/TaniguchiSigh2.png"
    image Taniguchi Unhap1 = "Sprites/Taniguchi/TaniguchiUnhappy1.png"
    image Taniguchi Unhap2 = "Sprites/Taniguchi/TaniguchiUnhappy2.png"
    image Taniguchi Quest1 = "Sprites/Taniguchi/TaniguchiQuestion1.png"
    
    #Kunikida Sprites
    image Kunikida Neutral1 = "Sprites/Kunikida/KunikidaNeutral1.png"
    image Kunikida Neutral2 = "Sprites/Kunikida/KunikidaNeutral2.png"
    image Kunikida Neutral3 = "Sprites/Kunikida/KunikidaNeutral3.png"
    image Kunikida Smile1 ="Sprites/Kunikida/KunikidaSmile1.png"
    image Kunikida Smile2 ="Sprites/Kunikida/KunikidaSmile2.png"
    image Kunikida Smile3 ="Sprites/Kunikida/KunikidaSmile3.png"
    image Kunikida Ser1 = "Sprites/Kunikida/KunikidaSerious1.png"
    image Kunikida Ser2 = "Sprites/Kunikida/KunikidaSerious2.png"
    image Kunikida Sad1 = "Sprites/Kunikida/KunikidaSad1.png"
    image Kunikida Sigh1 = "Sprites/Kunikida/KunikidaSigh1.png"
    image Kunikida Sigh2 = "Sprites/Kunikida/KunikidaSigh2.png"

    #Nonoko Sprites
    image Nonoko Ang1 = "Sprites/Nonoko/NonokoAngry1.png"
    image Nonoko Smile1 = "Sprites/Nonoko/NonokoSmile1.png"
    image Nonoko Sup1 = "Sprites/Nonoko/NonokoSurprised1.png"
    image Nonoko Pout1 = "Sprites/Nonoko/NonokoPout1.png"
    image Nonoko Pout2 = "Sprites/Nonoko/NonokoPout2.png"
    image Nonoko Hap1 = "Sprites/Nonoko/NonokoHappy1.png"
    image Nonoko Quest1 = "Sprites/Nonoko/NonokoQuestion1.png"
    image Nonoko Laugh1 = "Sprites/Nonoko/NonokoLaughing1.png"
    image Nonoko Yell1 = "sprites/Nonoko/NonokoYell1.png"
    image Nonoko Worry1 = "sprites/Nonoko/NonokoWorry1.png"
    image Nonoko Worry2 = "sprites/Nonoko/NonokoWorry2.png"
    
    #Mori Sprites
    image Mori Neutral1 = "Sprites/Mori/MoriNeutral1.png"
    image Mori Neutral2 = "Sprites/Mori/MoriNeutral2.png"
    image Mori Neutral3 = "Sprites/Mori/MoriNeutral3.png"
    image Mori Neutral4 = "Sprites/Mori/MoriNeutral4.png"
    image Mori Ser1 = "Sprites/Mori/MoriSerious1.png"
    image Mori Ser2 = "Sprites/Mori/MoriSerious2.png"
    image Mori Ser3 = "Sprites/Mori/MoriSerious3.png"
    image Mori Sigh1= "Sprites/Mori/MoriSigh1.png"
    image Mori Sigh2= "Sprites/Mori/MoriSigh2.png"
    image Mori Smile1= "Sprites/Mori/MoriSmile1.png"
    image Mori Smile2= "Sprites/Mori/MoriSmile2.png"
    image Mori Nervous1= "Sprites/Mori/MoriNervous1.png"
    image Mori Hap1 = "Sprites/Mori/MoriHappy1.png"
    
    image Mori Neutral1 Flip = im.Flip("Sprites/Mori/MoriNeutral1.png", horizontal=True)
    image Mori Neutral2 Flip = im.Flip("Sprites/Mori/MoriNeutral2.png", horizontal=True)
    image Mori Neutral3 Flip = im.Flip("Sprites/Mori/MoriNeutral3.png", horizontal=True)
    image Mori Neutral4 Flip = im.Flip("Sprites/Mori/MoriNeutral4.png", horizontal=True)
    # image Mori Ser1 Flip = im.Flip("Sprites/Mori/MoriSerious1.png", horizontal=True)
    image Mori Ser1 Flip = im.Flip("Sprites/Mori/MoriSerious1v2.png", horizontal=True)
    # image Mori Ser2 Flip = im.Flip("Sprites/Mori/MoriSerious2.png", horizontal=True)
    image Mori Ser2 Flip = im.Flip("Sprites/Mori/MoriSerious2v2.png", horizontal=True)
    image Mori Ser3 Flip = im.Flip("Sprites/Mori/MoriSerious3.png", horizontal=True)
    image Mori Sigh1 Flip = im.Flip("Sprites/Mori/MoriSigh1.png", horizontal=True)
    image Mori Sigh2 Flip = im.Flip("Sprites/Mori/MoriSigh2.png", horizontal=True)
    image Mori Grin1 Flip = im.Flip("Sprites/Mori/MoriGrin1.png", horizontal=True)
    image Mori Smile1 Flip = im.Flip("Sprites/Mori/MoriSmile1.png", horizontal=True)
    image Mori Smile2 Flip = im.Flip("Sprites/Mori/MoriSmile2.png", horizontal=True)
    image Mori Smile3 Flip = im.Flip("Sprites/Mori/MoriSmile3.png", horizontal=True)
    image Mori Nervous1 Flip = im.Flip("Sprites/Mori/MoriNervous1.png", horizontal=True)
    image Mori Hap1 Flip = im.Flip("Sprites/Mori/MoriHappy1.png", horizontal=True)
    
    #Sakanaka Sprites
    image Sakanaka Neutral1 = "Sprites/Sakanaka/SakanakaNeutral1.png"
    image Sakanaka Neutral2 = "Sprites/Sakanaka/SakanakaNeutral2.png"
    image Sakanaka Ser1  = "Sprites/Sakanaka/SakanakaSerious1.png"
    image Sakanaka Ser2  = "Sprites/Sakanaka/SakanakaSerious2.png"
    image Sakanaka Smile1 = "Sprites/Sakanaka/SakanakaSmile1.png"
    image Sakanaka Smile2 = "Sprites/Sakanaka/SakanakaSmile2.png"
    image Sakanaka Smile3 = "Sprites/Sakanaka/SakanakaSmile3.png"
    image Sakanaka Uneasy1 = "Sprites/Sakanaka/SakanakaUneasy1.png"
    image Sakanaka Uneasy2 = "Sprites/Sakanaka/SakanakaUneasy2.png"
    image Sakanaka Unhap1 = "Sprites/Sakanaka/SakanakaUnhappy1.png"
    image Sakanaka Unhap2 = "Sprites/Sakanaka/SakanakaUnhappy2.png"
    
    #Yamane Sprites
    image Yamane Lost Cool1 = "Sprites/Yamane/YamaneLostCool1.png"
    image Yamane Lost Cool2 = "Sprites/Yamane/YamaneLostCool2.png"
    image Yamane Grin1 = "Sprites/Yamane/YamaneGrin1.png"
    image Yamane Grin2 = "Sprites/Yamane/YamaneGrin2.png"
    image Yamane Grin3 = "Sprites/Yamane/YamaneGrin3.png"
    image Yamane Terror1 = "Sprites/Yamane/YamaneTerror1.png"
    image Yamane Terror2 = "Sprites/Yamane/YamaneTerror2.png"
    
    #Ryo Sprites
    image Ryo Ang1 = "Sprites/Ryo/RyoAngry1.png"
    image Ryo Ang2 = "Sprites/Ryo/RyoAngry2.png"
    image Ryo Attack1 = "Sprites/Ryo/RyoAttack1.png"
    image Ryo Attack2 = "Sprites/Ryo/RyoAttack2.png"
    image Ryo Grin1 = "Sprites/Ryo/RyoGrin1.png"
    image Ryo Grin2 = "Sprites/Ryo/RyoGrin2.png"
    image Ryo Neutral1 = "Sprites/Ryo/RyoNeutral1.png"
    image Ryo Shifty1 = "Sprites/Ryo/RyoShifty1.png"
    image Ryo Shifty2 = "Sprites/Ryo/RyoShifty2.png"
    image Ryo Shifty3 = "Sprites/Ryo/RyoShifty3.png"
    
    image Ryo Band Ang1 = "Sprites/Ryo/RyoBandAngry1.png"
    image Ryo Band Ang2 = "Sprites/Ryo/RyoBandAngry2.png"
    image Ryo Band Attack1 = "Sprites/Ryo/RyoBandAttack1.png"
    image Ryo Band Attack2 = "Sprites/Ryo/RyoBandAttack2.png"
    image Ryo Band Grin1 = "Sprites/Ryo/RyoBandGrin1.png"
    image Ryo Band Grin2 = "Sprites/Ryo/RyoBandGrin2.png"
    image Ryo Band Neutral1 = "Sprites/Ryo/RyoBandNeutral1.png"
    image Ryo Band Shifty1 = "Sprites/Ryo/RyoBandShifty1.png"
    image Ryo Band Shifty2 = "Sprites/Ryo/RyoBandShifty2.png"
    image Ryo Band Shifty3 = "Sprites/Ryo/RyoBandShifty3.png"
    image Ryo Band Sneer1 = "Sprites/Ryo/RyoBandSneer1.png"
    
    image Ryo Ang1 Flip = im.Flip("Sprites/Ryo/RyoAngry1.png", horizontal=True)
    image Ryo Ang2 Flip = im.Flip("Sprites/Ryo/RyoAngry2.png", horizontal=True)
    image Ryo Attack1 Flip = im.Flip("Sprites/Ryo/RyoAttack1.png", horizontal=True)
    image Ryo Attack2 Flip = im.Flip("Sprites/Ryo/RyoAttack2.png", horizontal=True)
    image Ryo Grin1 Flip = im.Flip("Sprites/Ryo/RyoGrin1.png", horizontal=True)
    image Ryo Grin2 Flip = im.Flip("Sprites/Ryo/RyoGrin2.png", horizontal=True)
    image Ryo Neutral1 Flip = im.Flip("Sprites/Ryo/RyoNeutral1.png", horizontal=True)
    image Ryo Shifty1 Flip = im.Flip("Sprites/Ryo/RyoShifty1.png", horizontal=True)
    image Ryo Shifty2 Flip = im.Flip("Sprites/Ryo/RyoShifty2.png", horizontal=True)
    image Ryo Shifty3 Flip = im.Flip("Sprites/Ryo/RyoShifty3.png", horizontal=True)
    
    image Ryo Band Attack1 Flip = im.Flip("Sprites/Ryo/RyoBandAttack1.png", horizontal=True)
    image Ryo Band Attack2 Flip = im.Flip("Sprites/Ryo/RyoBandAttack2.png", horizontal=True)
        
#Kimidori Sprites
    image Kimidori Smile = "Sprites/Kimidori/KimidoriSmile.png"
    image Kimidori Unhap = "Sprites/Kimidori/KimidoriUnhappy.png"
    image Kimidori Sigh = "Sprites/Kimidori/KimidoriSigh.png"
    image Kimidori Neutral = "Sprites/Kimidori/KimidoriNeutral.png"
    image Kimidori Confused = "Sprites/Kimidori/KimidoriConfused.png"
    
    #Image Flips
    image Kimidori Smile Flip= im.Flip("Sprites/Kimidori/KimidoriSmile.png", horizontal=True)
    image Kimidori Unhap Flip = im.Flip("Sprites/Kimidori/KimidoriUnhappy.png", horizontal=True)
    image Kimidori Sigh Flip = im.Flip("Sprites/Kimidori/KimidoriSigh.png", horizontal=True)
    image Kimidori Neutral Flip = im.Flip("Sprites/Kimidori/KimidoriNeutral.png", horizontal=True)
    image Kimidori Confused Flip = im.Flip("Sprites/Kimidori/KimidoriConfused.png", horizontal=True)
    
    
#Shinobu Sprites
    image Shinobu Hap1 = "Sprites/Shinobu/ShinobuHappy1.png"
    image Shinobu Hap2 = "Sprites/Shinobu/ShinobuHappy2.png"
    image Shinobu Neutral1 = "Sprites/Shinobu/ShinobuNeutral1.png"
    image Shinobu Neutral2 = "Sprites/Shinobu/ShinobuNeutral2.png"
    image Shinobu Neutral3 = "Sprites/Shinobu/ShinobuNeutral3.png"
    image Shinobu Pain = "Sprites/Shinobu/ShinobuPain.png"
    image Shinobu Pained = "Sprites/Shinobu/ShinobuPained.png"
    image Shinobu Sad1 = "Sprites/Shinobu/ShinobuSad1.png"
    image Shinobu Sad2 = "Sprites/Shinobu/ShinobuSad2.png"
    image Shinobu Smile1 = "Sprites/Shinobu/ShinobuSmile1.png"
    image Shinobu Sup1 = "Sprites/Shinobu/ShinobuSurprised1.png"
    image Shinobu Sup2 = "Sprites/Shinobu/ShinobuSurprised2.png"
    
    image ShinBlush = "Sprites/Shinobu/ShinobuBlush.png"
    
    #Image flips
    image Shinobu Hap1 Flip = im.Flip("Sprites/Shinobu/ShinobuHappy1.png", horizontal=True)
    image Shinobu Hap2 Flip = im.Flip("Sprites/Shinobu/ShinobuHappy2.png", horizontal=True)
    image Shinobu Neutral1 Flip = im.Flip("Sprites/Shinobu/ShinobuNeutral1.png", horizontal=True)
    image Shinobu Neutral2 Flip = im.Flip("Sprites/Shinobu/ShinobuNeutral2.png", horizontal=True)
    image Shinobu Neutral3 Flip = im.Flip("Sprites/Shinobu/ShinobuNeutral3.png", horizontal=True)
    image Shinobu Pain Flip = im.Flip("Sprites/Shinobu/ShinobuPain.png", horizontal=True)
    image Shinobu Pained Flip = im.Flip("Sprites/Shinobu/ShinobuPained.png", horizontal=True)
    image Shinobu Sad1 Flip = im.Flip("Sprites/Shinobu/ShinobuSad1.png", horizontal=True)
    image Shinobu Sad2 Flip = im.Flip("Sprites/Shinobu/ShinobuSad2.png", horizontal=True)
    image Shinobu Smile1 Flip = im.Flip("Sprites/Shinobu/ShinobuSmile1.png", horizontal=True)
    image Shinobu Sup1 Flip = im.Flip("Sprites/Shinobu/ShinobuSurprised1.png", horizontal=True)
    image Shinobu Sup2 Flip = im.Flip("Sprites/Shinobu/ShinobuSurprised2.png", horizontal=True)
    
    image ShinBlush Flip = im.Flip("Sprites/Shinobu/ShinobuBlush.png", horizontal=True)
    
#Thug Sprites
    image ThugHead 1 = "Sprites/Thug/ThugHead1.png"
    image ThugBody 1 = "Sprites/Thug/ThugBody1.png"
    
    image Thug1 = im.Composite(
    (519, 480),
    (0, 0), "Sprites/Thug/ThugBody1.png",
    (0, 0), "Sprites/Thug/ThugHead1.png"
    ) 
        
    #Closed space variants
    image clouds CS = im.MatrixColor("id_clouds.png",
        im.matrix.saturation(.15) * im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(-.35))
    
    image Kyon CS Sigh1 = im.MatrixColor("Sprites/Kyon/KyonSigh1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Pout2 = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    
    image Haruhi CS Pout1 = im.MatrixColor("Sprites/Haruhi/HaruhiSidePout1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    
    image bg SchoolOutside CS = im.MatrixColor("Backgrounds/SchoolOutside.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    
    image bg SchoolOutside Night CS = im.MatrixColor("Backgrounds/SchoolOutsideNight.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.05))
    
    image bg SchoolEntranceLeft CS = im.MatrixColor("Backgrounds/SchoolEntranceLeft.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    
    image bg hallway CS = im.MatrixColor("Backgrounds/hallway.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image bg ClubHallLeft CS = im.MatrixColor("Backgrounds/ClubHallLeft.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image bg ClubroomFullNight CS = im.MatrixColor("Backgrounds/ClubroomFullNight.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image ClubroomFullNight Glow = im.MatrixColor("Backgrounds/ClubroomFullNight.png",
        im.matrix.tint(.75, .75, 1.0) * im.matrix.brightness(.35))
#     
    image Kyon CS Ser1 = im.MatrixColor("Sprites/Kyon/KyonSerious1.png",
         im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ser2 = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ser3 = im.MatrixColor("Sprites/Kyon/KyonSerious3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh2 = im.MatrixColor("Sprites/Kyon/KyonSigh2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh3 = im.MatrixColor("Sprites/Kyon/KyonSigh3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sigh4 = im.MatrixColor("Sprites/Kyon/KyonSigh4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral1 = im.MatrixColor("Sprites/Kyon/KyonNeutral1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral2 = im.MatrixColor("Sprites/Kyon/KyonNeutral2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral3 = im.MatrixColor("Sprites/Kyon/KyonNeutral3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Neutral4 = im.MatrixColor("Sprites/Kyon/KyonNeutral4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang1 = im.MatrixColor("Sprites/Kyon/KyonAngry1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang2 = im.MatrixColor("Sprites/Kyon/KyonAngry2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang3 = im.MatrixColor("Sprites/Kyon/KyonAngry3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Ang4 = im.MatrixColor("Sprites/Kyon/KyonAngry4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Pain1 = im.MatrixColor("Sprites/Kyon/KyonPained1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Pain2 = im.MatrixColor("Sprites/Kyon/KyonPained2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile1 = im.MatrixColor("Sprites/Kyon/KyonSmile1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile2 = im.MatrixColor("Sprites/Kyon/KyonSmile2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile3 = im.MatrixColor("Sprites/Kyon/KyonSmile3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile4 = im.MatrixColor("Sprites/Kyon/KyonSmile4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Smile5 = im.MatrixColor("Sprites/Kyon/KyonSmile5.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Worry1 = im.MatrixColor("Sprites/Kyon/KyonWorry1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Worry2 = im.MatrixColor("Sprites/Kyon/KyonWorry1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Puzzle1 = im.MatrixColor("Sprites/Kyon/KyonPuzzled1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sup1 = im.MatrixColor("Sprites/Kyon/KyonSurprised1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Sup2 = im.MatrixColor("Sprites/Kyon/KyonSurprised2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap1 = im.MatrixColor("Sprites/Kyon/KyonUnhappy1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap2 = im.MatrixColor("Sprites/Kyon/KyonUnhappy2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap3 = im.MatrixColor("Sprites/Kyon/KyonUnhappy3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap4 = im.MatrixColor("Sprites/Kyon/KyonUnhappy4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Kyon CS Unhap5 = im.MatrixColor("Sprites/Kyon/KyonUnhappy5.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
#         
    image Haruhi CS Sup1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sup2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sup3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSurprised3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang4 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Ang5 = im.MatrixColor("Sprites/Haruhi/HaruhiSideAngry5.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Hap4 = im.MatrixColor("Sprites/Haruhi/HaruhiSideHappy4.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Eyeroll1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideEyeroll1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Eyeroll2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideEyeroll2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Quest1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideQuestion1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Quest2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideQuestion2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Grin1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideGrin1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Grin2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideGrin2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Worry1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideWorry1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Worry2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideWorry2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Smile3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSmile3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Sigh3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideSigh3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy2.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Unhap3 = im.MatrixColor("Sprites/Haruhi/HaruhiSideUnhappy3.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Focus1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideFocus1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Neutral1 = im.MatrixColor("Sprites/Haruhi/HaruhiSideNeutral1.png",
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    image Haruhi CS Neutral2 = im.MatrixColor("Sprites/Haruhi/HaruhiSideNeutral2.png",    
        im.matrix.saturation(.15) * im.matrix.tint(.80, .80, 1.0) * im.matrix.brightness(-.35))
    
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
    
    # Text for simple Credit Roll. Needs editing. And {font=fancyfont.ttf}magic{/font}...
    # image credroll = Text("\n{size=+5}Presented by:{/size}\n\nBig Damn VN Brigade:\n\nAgasa\nalethiophile\nFilraen\nOroboro\nZfish9\nJason Ulloa\nZero Null\n\n\nMany thanks to:\n\njonbob\nSpecular\nPax_Empyrean\neternaleye\n\n\n\n\n\n\n{size=+5}Special thanks to{/size}:\n\n{b}Brian Randall{/b}\nauthor of Kyon: Big Damn Hero\n\nand\n\n{b}Nagaru Tanigawa{/b}\nauthor of Suzumiya Haruhi series\n\n\nAnd,\n\n\n{b}Banpresto{/b}:\nfor \"Suzumiya Haruhi no Tomadoi\" VN,\nwith all its sprites and BGs,\n\n\n{b}Haruhi Suzumiya series\nProduction Committee{/b}:\nfor anime and movie OSTs\n\n\n{b}07th Expansion & Alchemist{/b}:\nfor \"Umineko no {color=#f00}Na{/color}ku Koro ni\" VNs\n(PC&PS3 ver) with its sprites, BG and OST\n\n\n{b}Saotome Mirai{/b},\nfor the model for certain character's sprite's hair\n\n\nAnd of course, {b}PyTom{/b}\nfor this awesome Ren'Py VN engine\nthis kinetic novel is powered by.\n\n\n\n\n\nDisclaimer: This production makes use\nof intellectual property belonging to\nBrian Randall, Nagaru Tanigawa \nand others. No disrespect is intended.\n\nNeither Kyon: Big Damn Hero \nnor Suzumiya Haruhi and related \ncharacters are owned by anyone \nassociated with Big Damn VN\n", text_align=0.5, size=30)
    image credroll = Text("\n{size=+5}Presented by:{/size}\n\nBig Damn VN Brigade:\n\nAgasa\nalethiophile\nFilraen\nOroboro\nZfish9\nJason Ulloa\nZero Null\n\n\nMany thanks to:\n\njonbob\nSpecular\nPax_Empyrean\neternaleye\n\n\n\n\n\n\n{size=+5}Special thanks to{/size}:\n\nBrian Randall\nauthor of Kyon: Big Damn Hero\n\nand\n\nNagaru Tanigawa\nauthor of Suzumiya Haruhi series\n\n\nAnd,\n\n\nHaruhi Suzumiya series\nProduction Committee\n\n\nBanpresto:\nfor \"Suzumiya Haruhi no Tomadoi\"\nVisual Novel,\n\n\n07th Expansion & Alchemist:\nfor \"Umineko no {color=#f00}Na{/color}ku Koro ni\"\nVisual Novel series\n\n\nSaotome Mirai:\nfor the inspiration for\ncertain character's sprite's hairstyle\n\n\nYasunori Mitsuda:\nfor composing \"Morning Sunlight\"\n\n\nniconico user \"prince\":\nfor the Music Box version of \"God Knows\"\n\n\nniconico user \"Nikuman\":\nfor the Metal version of \"God Knows\"\n\n\nAnd of course, PyTom:\nfor the Ren'Py Visual Novel engine.\n\n\n\n\n\nDisclaimer: This production makes use\nof intellectual property belonging to\nBrian Randall, Nagaru Tanigawa \nand others. No disrespect is intended.\n\nNeither Kyon: Big Damn Hero \nnor Suzumiya Haruhi and related \ncharacters are owned by anyone \nassociated with Big Damn VN\n", text_align=0.5, size=30)
    
    #A quick next episode preview
    image Popen = Text("Next time on Kyon: Big Damn Hero", text_align=0.5, size=30)
    image Popen2:
        Text("Next time on Kyon: Big Damn Hero", text_align=0.5, size=35, outlines=[(2, "#000", 0, 0)])
        rotate -15
    image P1 = "Backgrounds/P1.jpg"
    image P2 = "Backgrounds/P2.jpg"
    image P3 = "Backgrounds/P3.jpg"
    image P4 = "Backgrounds/P4.jpg"
    image P5 = "Backgrounds/P5.jpg"
    image Pexit = Text("See you again!", text_align=0.5, size=30)
    
    # "Image" showing the date
    # image eyeDate = DynamicDisplayable(show_date)
    image eyeDate 1 = DynamicDisplayable(show_date1)
    image eyeDate 2 = DynamicDisplayable(show_date2)

    image eyeDateColor 1 = DynamicDisplayable(lambda st, at: [Text("[date1]", font="DejaVuSerif-Italic.ttf", size=25, color=ecfg, outlines=[(1, "#000", 2, 1)]), None])
    image eyeDateColor 2 = DynamicDisplayable(lambda st, at: [Text("[date2]", font="DejaVuSerif-Italic.ttf", size=25, color=ecfg, outlines=[(1, "#000", 2, 1)]), None])
    
    image KBDHLogoWhite = "Backgrounds/KBDHLogo-White.png"
    image KBDHLogoColor = DynamicDisplayable(KBDH_Color)
    
    image eyeSolidBackground = DynamicDisplayable(lambda st, at: [ecbg, None])
    
    image eyebg = ConditionSwitch("ecbg == 'white'", "#fff", "True", "#000")
    
    # Most likely needs {font=fancyfont.ttf}magic{/font} to pull off properly...
#    image BDVNlogo = Text("{size=80}{b}{k=3}KYON:\n{/k}{/b}{/size}{size=40}{k=-1.0}Big Damn Hero{/k}{/size}", color="#3cf", outlines=[(1, "#000", 4, 3)])
    image BDVNlogo = Text("{font=praetorianacad.ttf}{size=115}KYON\n{/size}{size=40}Big Damn Hero{/size}{/font}", color="#3cf", outlines=[(1, "#000", 4, 3)])
    image SOSlogoborder = "Backgrounds/eyecatchlogos.png"
    image BDVNlogoBlack = Text("{size=80}{b}{k=3}KYON:\n{/k}{/b}{/size}{size=40}{k=-1.0}Big Damn Hero{/k}{/size}", color="#000")
    image WaitForInputBlinking:
        Text("{size=40}►  \n{/size}", color="#fff", outlines=[(1, "#000", 4, 3)])
        0.8
        Text("{size=40}\n{/size}", color="#fff", outlines=[(1, "#000", 4, 3)])
        0.8
        repeat

    # Title cards, i.e chapter-opening quotes
    image title 000 = Text("{space=500}{b}{size=+1}Thursday, June 2, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Don't Just SAY You Have a Bad Feeling, DO Something About It!\"\n\n\"...but I digress. When you get that feeling, you know the one, in the back of your head? The one that makes you think something is off about the situation? It may be right. Granted, you may also be tumbling headlong into a fit of paranoia that will end terribly for you and everyone you love. But what if you're NOT? Remember, if you're aware of things, you know most people think you're crazy anyway. Is it going to hurt that much more to overreact rather than just label something a false alarm?\"\n\n\"Practical Heroism and You: Awareness\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 001 = Text("{space=500}{b}{size=+1}Sunday, April 17, 2011{/size}{/b}\n\n\n\n\"Chapter One: The Truth is the Greatest Weapon\"\n\n\"...of dozens of issues with maintaining a 'masquerade' scenario. Generally, unless it's absolutely required, it's a bad idea. There will be fallout. If it must be done, the truth is still going to be the ultimate weapon — plan accordingly, and make sure it's a weapon that will serve you, and not any enemies. Barring that, make fast friends with someone who can BS better than you.\"\n\n\"Cover\" — Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 002 = Text("{space=500}{b}{size=+1}Monday, April 18, 2011{/size}{/b}\n\n\n\n\"Chapter Ten: Time Travel\"\n\n\"This is the one you absolutely cannot afford to mess up. The most important thing is to pay attention, and not over think things. But mostly, it's about paying attention; the worst thing you can do is assume that just because time travel is involved, you cannot fail.\"\n\n\"Practical Heroism and You: Awareness\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 003 = Text("{space=500}{b}{size=+1}Monday, April 18, 2011{/size}{/b}\n\n\n\n\"Chapter One: Expect the Unexpected\"\n\n\"...aside from them, however, there aren't many who can genuinely expect all things and calculate accordingly. So in a practical situations what it really means is: don't be so expectant of something happening, that any other result is a surprise. That's probably the best you can do, anyway.\"\n\n\"Roll With the Punches\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 004 = Text("{space=500}{b}{size=+1}Tuesday, April 19, 2011{/size}{/b}\n\n\n\n\"Chapter Twelve: As in Training, As in Life\"\n\n\"...but just as in the training world, you will inevitably take some blows.\nThat's the purpose of practice, isn't it? Perfection may be a myth, but success is not. So train to be good enough, and most importantly, when you get hit, learn to take it.\"\n\n\"Roll With the Punches\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 005 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"Chapter Seven: Practical Considerations for the Apocalypse\"\n\n\"...if that happens, and there's nothing else to be done, the next question is going to be survival. There are things more important than food, water, or even reasonable shelter. There's no reason to try and survive alone, unless you're just a die-hard, and even then you're still probably clinging to hope. So make sure you're not alone, or else there's not much reason to keep on going.\"\n\n\"Clearing the Event Horizon: How Close is Too Close?\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 006 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"Chapter One: Crossing the Threshold\"\n\n\"...eventually, this means that you can reach a point where words no longer suffice. Civility is all well and good, but sometimes the simple message of overpowering force is the one that the situation requires. Use your judgment on when this moment is, but keep in mind that I call it a last resort for a reason; once you initiate violence, you're committed until victory or failure.\"\n\n\"The Last Resort: Violence and You\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 007 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Excuses\"\n\n\"If you can't come up with a legitimate excuse, you have two fall-back options. First, you can take refuge in audacity and say something so outlandish you're dismissed (bonus points if you tell the truth with a straight face). And if that doesn't work, place the burden of justifying your whereabouts on someone else. If neither of these options pan out, run far, run fast.\"\n\n\"Cover\" — Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 008 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"File K:3419.8.19/2011.4.21\"\n\n\"...so, I think, maybe, sometimes it might be okay to be a little selfish, as long as you don't jeopardize anything. That's the really hard part, though ... how can you ever tell? I suppose that means erring on the side of caution ... no matter how it hurts. But sometimes ... just a little bit ... it's nice to be selfish.\"\n\n\"[[CLASSIFIED]\" -- Peraea Mons T.E.S.A. Dataplume", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 009 = Text("{space=480}{b}{size=+1}Thursday, April 21, 2011{/size}{/b}\n\n\n\n\"File K:3453.3.5/2011.4.22\"\n\n\"...then push the stack representing the focus shift in prio research target. Due to the complexity of interaction with this particular model, an automated property will top your stack every two minutes if you do not pop or [[CLASSIFIED]. Do not attempt to adjust this; it is for your own safety! For the remainder of this lesson, you will need to utilize your augmented reality context-tags, or relay queries to me. Oh! And before this comes up? No, I will not ask [[CLASSIFIED] to autograph anything for you.\"\n\n\"[[CLASSIFIED]\" -- Peraea Mons T.E.S.A. Dataplume", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 010 = Text("{space=500}{b}{size=+1}Friday, April 22, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Asking for Help\"\n\n\"Not everyone can handle an entire project single-handedly. Remember why you have allies in the first place! Achieving something on your own is great, but if the cost of failure is high, swallow your pride and spread the load around.\"\n\n\"Methods of Victory\" -- 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 011 = Text("{space=500}{b}{size=+1}Friday, April 22, 2011{/size}{/b}\n\n\n\n\"Chapter Eight: Overbearing\"\n\n\"In a confrontation that is either physical or verbal, when possible, completely overwhelm your enemy from the outset. If it's a serious fight, there's no reason to hold back, no purpose to pulling punches. If it's not a serious fight, you're reading the wrong book!\"\n\n\"Methods of Victory\" -- 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 012 = Text("{space=480}{b}{size=+1}Saturday, April 23, 2011{/size}{/b}\n\n\n\n\"Chapter Five: Disguises\"\n\n\"A good disguise is useful for infiltration, escape, or just plain taking a day off without being recognized. Care is required in selecting your disguise, of course, and going with your natural intuition for what disguise would serve you best is not always a good idea. Chances are, people who know you have a much better idea of what would make you look like someone else than you do - if they make a suggestion, think about it seriously.\"\n\n\"Cover\" - Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 013 = Text("{space=480}{b}{size=+1}Thursday, April 23, 2011{/size}{/b}\n\n\n\n\"Title: Admirable\"\n\n\"He says it is 'like'\n\"No absolute value, there\n\"A strange inference\n\n\"Understanding is not full\n\"But to call it 'like' and know\n\n\"Incomplete knowledge\n\"With partial understanding\n\"Yet still sufficient\"\n\n\"Snow, Verses: A Compilation\" - Committed to record: 2011.4.23", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 014 = Text("{space=500}{b}{size=+1}Monday, April 25, 2011{/size}{/b}\n\n\n\n\"File K:3419.8.19/2011.4.25\"\n\n\"Even as an observer, sometimes it's nice to be ignorant about some things. At least until after the fact. I suppose that doesn't sound very good, does it? Maybe I shouldn't record this...\"\n\n\"[[CLASSIFIED]\" - Paraea Mons T.E.S.A. Dataplume", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 015 = Text("{space=500}{b}{size=+1}Friday, April 29, 2011{/size}{/b}\n\n\n\n\"Chapter One: Threats and Allies\"\n\n\"Not every threat is physical. Really, it's the more subtle ones that are the scariest ... but maybe they shouldn't be. If you can't handle it yourself, and you're tired of running away (who wouldn't be!), then you need to find good allies and stick with them! At least, you'd have to find one really solid ally, and then make sure you're there for them enough so that they can be there for you too! It's not optional - so do it!\"\n\n\"Mirror, Mirror\" - T.K.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 016 = Text("{space=480}{b}{size=+1}Saturday, April 30, 2011{/size}{/b}\n\n\n\n\"Chapter Two: More Training\"\n\n\"...so, yes, congratulations for finishing your first regimen successfully. But now that you've acquired those skills, you must retain them, while also refining new skills. The purpose of training is improvement, after all.\"\n\n\"Training and You: the Eternal Nightmare\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 017 = Text("{space=480}{b}{size=+1}Wednesday, May 4, 2011{/size}{/b}\n\n\n\n\"Title: Relations\"\n\n\"Sun, sea, sky, river\n\"Energy links to matter\n\"Clearly connected\n\n\"Established by nature, not:\n\"Structures formed by consciousness\n\n\"'Family' networks\n\"Need not follow clear order\n\"Ghost, friend; relative\"\n\n\"Snow, Verses: A Compilation\" - Comitted to record:2011.5.5", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 018 = Text("{space=500}{b}{size=+1}Thursday, May 5, 2011{/size}{/b}\n\n\n\n\"Chapter One: Listen\"\n\n\"...but just in case you do need a reminder: You're reading this book because you're interested in the advice that other people can give! Written suggestions are great, but the most applicable wisdom you're probably going to get is going to be from the people around you; the ones who've done and seen it before! So, when they speak, listen.\"\n\n\"Methods of Victory\" - T.H.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 019 = Text("{space=500}{b}{size=+1}Saturday, May 7, 2011{/size}{/b}\n\n\n\n\"Fragment: Clan Annals (unverified)\"\n\n\"Entry for 5.11.2011:\nThe laughter stopped, today; I ponder revenge. Would he be okay with that? \n- Tsu-Oyabun # 108\"\n\n\"[[Undecipherable]\" - Recovered From Primary T.E.S.A. Archive", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 020 = Text("{space=460}{b}{size=+1}Wednesday, May 11, 2011{/size}{/b}\n\n\n\n\"Chapter Four: Delegation\"\n\n\"...so that means, if you're leading, you have to lead. That sometimes means delegating things you can do yourself, so you can lead others. Don't get this mixed up with 'not getting your hands dirty'; you should be capable, but know when to let people better suited to handling the situation do so.\"\n\n\"Methods of Victory\" - T.H.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 021 = Text("{space=480}{b}{size=+1}Thrusday, May 12, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Friends and Enemies\"\n\n\"There's an old quote that goes, 'keep your friends close, and your enemies closer'. Personally, I think that's about the dumbest thing I've ever heard. Don't ignore your enemies, if you've got any, but at no point should your vision and focus be so clouded by anything that you forget to pay attention to your friends.\"\n\n\"Practical Heroism and You: Awareness\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 022 = Text("{space=480}{b}{size=+1}Thursday, May 12, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Fight or Flight\"\n\n\"Running away is just buying time, not solving a problem. You may not be able to solve every problem on your own, but if you just run from everything ... then you never solve anything at all.\"\n\n\"Mirror, Mirror\" - T.K.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 023 = Text("{space=500}{b}{size=+1}Friday, May 13, 2011{/size}{/b}\n\n\n\n\"Chapter Five: So, You Got Away\"\n\n\"Are you sure? I mean, really, really, really sure? It could just be the calm before the storm, as they say. Check, double-check, check again, and then, once you're done, don't get overconfident or cocky.\"\n\n\"Clearing the Event Horizon: How Close is Too Close?\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 024 = Text("{space=500}{b}{size=+1}Monday, May 16, 2011{/size}{/b}\n\n\n\n\"Fragment: Clan Annals (unverified)\"\n\n\"Entry for 5.16.2011:\nCivility is the prized, fading, heart of proper criminals. But there's this bad impression that somehow, it just won't work as neatly as it feels it should have.\n- Tsu-Oyabun # 108\"\n\n\"[[Undecipherable]\" - Recovered From Primary T.E.S.A. Archive", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 025 = Text("{space=500}{b}{size=+1}Monday, May 16, 2011{/size}{/b}\n\n\n\n\"File K:3453.3.1/2011.4.17\"\n\n\"I probably raised more questions than answers. Maybe that's for the best, though? An inquisitive mind is a prepared mind, and that's desirable ... I think... But, saying that, I have the impression that he understands the situation better than I do, ultimately. Why would that be?\"\n\n\"[[CLASSIFIED]\" - Paraea Mons T.E.S.A. Dataplume", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 026 = Text("{space=500}{b}{size=+1}Sunday, April 17, 2011{/size}{/b}\n\n\n\n\"Chapter Two: The Showy Entrance\"\n\n\"Don't underestimate it! The dramatic, dynamic, explosive entrance - if you can pull it off - may actually allow you to avoid combat. It could also make you look really silly if you flub it. Find a smooth blend of action to showmanship, dependant on the situation. Flying kicks are all well and good, but sometimes, a straight punch is really dynamic enough.\"\n\n\"The Last Resort: Violence and You\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 027 = Text("{space=480}{b}{size=+1}Tuesday, May 17, 2011{/size}{/b}\n\n\n\n\"Title: Connected\"\n\n\"Undetected routes\n\"Bridging the distance between\n\"You, and you, and I\"\n\n\"Snow, Verses: A Compilation\" - Committed to record: 2011.5.18", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 028 = Text("{space=480}{b}{size=+1}Thursday, May 19, 2011{/size}{/b}\n\n\n\n\"Fragment: Clan Annals (unverified)\"\n\n\"Entry for 5.19.2011:\nSometimes, just sometimes ... being a slave to tradition has its perks. And those can make it worth it the rest of the time.\n- Tsu-Oyabun # 108\"\n\n\"[[Undecipherable]\" - Recovered From Primary T.E.S.A. Archive", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 029 = Text("{space=500}{b}{size=+1}Friday, May 20, 2011{/size}{/b}\n\n\n\n\"File K:3419.8.19/2011.5.20\"\n\n\"Selfishness in small degrees may be okay, but breaking the [[CLASSIFIED] is right out. So how is it possible that someone could use [[CLASSIFIED], cross their own temporal path, and interfere so incautiously? Wouldn't any T.E.S.A. official or [[CLASSIFIED] monitor for it in advance? Unless ... somehow ... such a thing were pre-determined? But if rules like that can be, well, not broken, but bent...\"\n\n\"[[CLASSIFIED]\" - Paraea Mons T.E.S.A. Dataplume", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 030 = Text("{space=500}{b}{size=+1}Friday, May 21, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Strike While the Iron is Hot\"\n\n\"Living explosion-to-explosion is all well and good, but remember that you should be living, not just surviving. There is a difference. So, for better or worse, recognize when you can steal a moment to relax, and do it. If such moments cannot be found, on occasion, you must make them.\"\n\n\"Roll With the Punches\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 031 = Text("{space=480}{b}{size=+1}Saturday, May 21, 2011{/size}{/b}\n\n\n\n\"Chapter Four: Capability\"\n\n\"Of particular concern is the possibility that you project an image that is too confident for your ability, and then are called upon to do something you are not qualified or capable of doing. It's better to be underestimated than overestimated, in the long term. Otherwise, you're just bluffing, and when the bluff is called...\"\n\n\"Cover\" - Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 032 = Text("{space=480}{b}{size=+1}Saturday, May 21, 2011{/size}{/b}\n\n\n\n\"Title: Fallible\"\n\n\"A mistake is made,\n\"errors perpetuated:\n\"personal failure.\n\n\"Apology is denied;\n\"judgment, refused.\n\n\"His analysis:\n\"'it's fine, no one is perfect';\n\"a comforting thought.\"\n\n\"Snow, Verses: A Compilation\" - Committed to record: 2011.5.21", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 033 = Text("{space=500}{b}{size=+1}Sunday, May 22, 2001{/size}{/b}\n\n\n\n\"Chapter Ten: Loyalty\"\n\n\"The thing is to remember that loyalty is earned, not just given. And if you want to be given loyalty, you tend to need to earn it. If you've already done that, just make sure you deserve that loyalty!\"\n\n\"Methods of Victory\" - 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 034 = Text("{space=480}{b}{size=+1}Tuesday, May 24, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Field Training\"\n\n\"Once you've established your basic level of competence, there's nothing to remind you of how far you have to go quite like trying to do something by yourself.\"\n\n\"Training and You: The Eternal Nightmare\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 035 = Text("{space=480}{b}{size=+1}Thursday, May 26, 2011{/size}{/b}\n\n\n\n\"Chapter Seven: Gaining Strength\"\n\n\"When you devote yourself to getting stronger and more able to do things ... don't forget to practice being careful with your new powers, too...\"\n\n\"Mirror, Mirror\" - T.K.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 036 = Text("{space=500}{b}{size=+1}Sunday, May 29, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Reliability\"\n\n\"Ideally, you'll know what everyone who answers to you is reliable for, and what the people who depend on you rely on. Everyone has different strengths, after all!\"\n\n\"Methods of Victory\" - 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 037 = Text("{space=500}{b}{size=+1}Monday, May 30, 2011{/size}{/b}\n\n\n\n\"Chapter Four: The Words You Didn't Want to Hear\"\n\n\"Occasionally, the stability of your environment and circumstances may become compromised by new information that has always been true, simply unknown. Whatever action you take in response, information control and caution are your watchwords. No matter how bad that makes you feel.\"\n\n\"Clearing the Event Horizon: How Close is Too Close?\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 038 = Text("{space=500}{b}{size=+1}Monday, May 30, 2011{/size}{/b}\n\n\n\n\"Chapter Four: The Ambush (II)\"\n\n\"...effectively, this is going to work just like the last chapter, except this time, the other guy gets all the advantages. I can guess what you're thinking, but this is actually even less fun than it sounds. As mentioned in the opening chapter of the previous book in this series, Roll With the Punches...\"\n\n\"The Last Resort: Violence and You\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 039 = Text("{space=460}{b}{size=+1}Wednesday, June 1, 2011{/size}{/b}\n\n\n\n\"Chapter Nine: Reciprocation\"\n\n\"Sometimes, it may feel like there's nothing you can do to pay back the people who help you. But if they want to help you, they're your friends - so just do your best for them, like they do for you!\"\n\n\"Mirror, Mirror\" - T.K.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 040 = Text("{space=460}{b}{size=+1}Wednesday, June 1, 2011{/size}{/b}\n\n\n\n\"Title: Unity\"\n\n\"A strange agenda\n\"with the hopeful result that\n\"'they' become 'we'.\n\n\"Factors are concealed from him;\n\"Does subtrefuge belong here?\"\n\n\"Snow, Verses: A Compilation\" - Committed to record: 2011.6.1", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 041 = Text("{space=500}{b}{size=+1}Thursday, June 2, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Don't Just SAY You Have a Bad Feeling, DO Something About It!\"\n\n\"...but I digress. When you get that feeling, you know the one, in the back of your head? The one that makes you think something is off about the situation? It may be right. Granted, you may also be tumbling headlong into a fit of paranoia that will end terribly for you and everyone you love. But what if you're NOT? Remember, if you're aware of things, you know most people think you're crazy anyway. Is it going to hurt that much more to overreact rather than just label something a false alarm?\"\n\n\"Practical Heroism and You: Awareness\" — Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 042 = Text("{space=500}{b}{size=+1}Thursday, June 2, 2011{/size}{/b}\n\n\n\n\"Entity One: Analysis\"\n\n\"In order to function in your new environment, be sure to follow all of your new interaction cues; these encourage behaviors that will be useful later. At the same time, be watchful for 'noise' input, or interactions which it is best to disregard as useful for integration.\"\n\n\"Adaptation\" - LP-K:AR Datastream Segment (-working translation-)", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 043 = Text("{space=500}{b}{size=+1}Monday, June 6, 2011{/size}{/b}\n\n\n\n\"Chapter Seven: Walking Into the Trap\"\n\n\"To put it simply, as you know you are walking into a trap, any time you feel very confident about your ability to handle it is the ideal time to reconsider.\"\n\n\"Roll With the Punches\" - Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 044 = Text("{space=500}{b}{size=+1}Monday, June 6, 2011{/size}{/b}\n\n\n\n\"Chapter One: Faith\"\n\n\"Faith is an odd thing, insofar as the idea is entirely unscientific, yet simultaneously, so vastly appealing. Is it some missed quirk of evolution, imbuing us with something we do not need? Or is that egotism, and it's foolish to think we've evolved beyond whatever gifts this idea has to offer us so soon? Drawing from Pascal's Wager ... does the risk of having faith outweigh the reward?\"\n\n\"Tending the Flame\" - [[The author's name has been charred from the document]", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 045 = Text("{space=500}{b}{size=+1}Saturday, June 4, 2011{/size}{/b}\n\n\n\n\"First Chorus: Scale\"\n\n\"The smallest orbits are string that spin; the largest are perfect circles. Between, memetic structures orbit in a profound variety of minute differences, invisible from both the smallest and the largest perspectives. A wide harmonic band with the potential to carry a multitude of frequencies that do not escape observation, but are still difficult to perceive from within.\"\n\n\"Perspective\" - LP-MK:SK Memetic String (-working translation-)", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 046 = Text("{space=500}{b}{size=+1}Monday, June 6, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Foundations\"\n\n\"At the end of the day, if you've nothing beneath your pretenses, then when they're swept away, there's nothing left. If that happens, the only thing left to rely on are your alliances and friendships ... so make sure that your masks don't put so much distance between you that they won't do it.\"\n\n\"Cover\" - Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 047 = Text("{space=500}{b}{size=+1}Tuesday, June 7, 2011{/size}{/b}\n\n\n\n\"Chapter Twelve: Limitations\"\n\n\"Sometimes, if you want something done right, you have to do it yourself. Sometimes, though, it's good to admit that the 'hands-on' approach may not be the best way to go. Overconfidence leads to many problems, so be sure you know where you really stand.\"\n\n\"Methods of Victory\" -- 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 048 = Text("{space=500}{b}{size=+1}Tuesday, June 7, 2011{/size}{/b}\n\n\n\n\"Second Chorus: Intensity\"\n\n\"Intensity is a measure that can indicate when scale has slipped control and the force being applied to the situation has exceeded or diminished beyond the proper volumes. Misunderstanding this can have severe repercussions.\"\n\n\"Perspective\" -- LP-MK:SK Memetic String (-working translation-)", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 049 = Text("{space=500}{b}{size=+1}Tuesday, June 7, 2011{/size}{/b}\n\n\n\n\"Fragment: Clan Annals (unverified)\"\n\n\"Entry for 6.7.2011: \nThere's something rewarding about being able to pass wisdom down to someone who reminds you so much of yourself at their age.... \n-- Tsu-Oyabun # 108\"\n\n\"[[Undecipherable]\" -- Recovered From Primary T.E.S.A. Archive", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 050 = Text("{space=500}{b}{size=+1}Tuesday, June 7, 2011{/size}{/b}\n\n\n\n\"Chapter Eight: Information Control\"\n\n\"Careful release of information, both true and false, can be a powerful tool in maneuvering the actions of others, both friend and foe. An important point to remember, however, is that once that information is out of your control, it can turn on you in ways you don't expect.\"\n\n\"Cover\" -- Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 051 = Text("{space=480}{b}{size=+1}Thursday, June 9, 2011{/size}{/b}\n\n\n\n\"Chapter Twelve: Moderation\"\n\n\"It really is possible to have too much of a good thing. Don't add too much fuel to the fire, unless you're prepared to deal with the consequences....\"\n\n\"Tending the Flame\" -- [[The author's name has been scratched out here]", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 052 = Text("{space=500}{b}{size=+1}Friday, June 10, 2011{/size}{/b}\n\n\n\n\"Entity Two: Sympathy\"\n\n\"When subjected to a system for observation, it is impossible to observe without having influence on it. Conversely, observations will also have influence over the observer. Sympathy does not exist to be observed alone without participation.\"\n\n\"Adaptation\" -- LP-TK:AR Datastream Segment (-working translation-)", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 053 = Text("{space=480}{b}{size=+1}Saturday, June 11, 2011{/size}{/b}\n\n\n\n\"Fragment: Clan Annals (unverified)\"\n\n\"Entry for 6.12.2011:\nIt is tragically easy to do harm when good is intended; a bridge built is easily burned. Hopefully, this gap can be mended.... \n-- Tsu-Oyabun # 108\"\n\n\"[[Undecipherable]\" -- Recovered From Primary T.E.S.A. Archive", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 054 = Text("{space=500}{b}{size=+1}Sunday, June 12, 2011{/size}{/b}\n\n\n\n\"Chapter Five: Owning Up\"\n\n\"No one is perfect. No one at all! If you think you're an exception, put this book down and read something else! When you make a mistake -- and you will -- don't bother trying to deny it or smooth it over. Just admit it and do your best to fix it. After all, if you're leading by example, how would you like the people who look up to you to behave?\"\n\n\"Methods of Victory\" -- 'T.H.'", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 055 = Text("{space=460}{b}{size=+1}Wednesday, June 15, 2011{/size}{/b}\n\n\n\n\"Chapter Two: Trust\"\n\n\"Like the previous subject -- faith -- trust is a concept that can have significant impact on your perceptions. Trust is probably easier to establish than faith, as it's something you can apply to people you know instead of vague concepts. At the same time, you can both 'have faith' in someone and 'trust' someone. However, the truth of the matter is that they are not the same thing; you can trust someone you have no faith in. Except ... if you do, and it's rewarded enough ... does that trust become faith?\"\n\n\"Tending the Flame\" -- [[The author's name is too faded from age to be read]", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 056 = Text("{space=460}{b}{size=+1}Wednesday, June 15, 2011{/size}{/b}\n\n\n\n\"Title: Unseen\"\n\n\"Every burden;\n\"he would carry them alone.\n\"But we are here too.\"\n\n\"Snow, Verses: A Compilation\" -- Committed to record:2011.6.16", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 057 = Text("{space=480}{b}{size=+1}Thursday, June 16, 2011{/size}{/b}\n\n\n\n\"Chapter Eight: The Limits of Responsibility\"\n\n\"Realistically, while you always need to do your best, there are moments when the right thing to do is nothing. That doesn't mean 'idly stand by' -- you have to be there for your friends -- but sometimes people can handle their own problems, and it's best to let them do that.\"\n\n\"Practical Heroism and You: Awareness\" -- Tadamichi Kyousuke", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 058 = Text("{space=500}{b}{size=+1}Friday, June 17, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Conflicts\"\n\n\"When you trust someone, and they ask you to believe something you cannot, there is a conflict. The solution isn't to put one over the other, but to take both in stride. Keep your own beliefs in mind, but give those you trust the benefit of the doubt. You've already decided they were trustworthy, haven't you?\"\n\n\"Tending the Flame\" -- [[the author's name is illegible due to a streak of ash]", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 059 = Text("{space=500}{b}{size=+1}Friday, June 17, 2011{/size}{/b}\n\n\n\n\"Chapter Three: Understanding and Perspective\"\n\n\"It's easy when you're overwhelmed to feel alone. But there's a good chance that there's someone out there that understands what you've been through, better than you might believe was possible! This person could be a friend, or an ally, and they could be easy to miss! But they might know what you've been through better than you can think -- so if you find someone like that, listen to their words closely!\"\n\n\"Mirror, Mirror\" -- T.K.", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 060 = Text("{space=480}{b}{size=+1}Saturday, June 18, 2011{/size}{/b}\n\n\n\n\"Chapter Six: Discretion\"\n\n\"...at times this may result in having information that is difficult to explain in a considerate or pleasant manner. While there may be something for bluntness when required, knowing when to bite your tongue and wait for the right moment is not without its benefits, either.\"\n\n\"Cover\" -- Author Unknown", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)
    image title 061 = Text("{space=500}{b}{size=+1}Sunday, June 19, 2011{/size}{/b}\n\n\n\n\"Third Chorus: Focus\"\n\n\"Carrier waves projecting memetic information on a wide spectrum abound and can easily become overwhelming, even with persistent observation. The inherent limitations of this can be bypassed by restricting attention to harmonic resonances beyond the most critical elements within the observational scope.\"\n\n\"Perspective\" -- LP-MK:SK Memetic String (-working translation-)", font="DejaVuSerif-Italic.ttf", size=18, line_leading=3, justify=True, xmaximum=750)

init python:
    config.layers.insert(1, 'upper')
    
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
    teleportfaster = ImageDissolve("id_teleport.png", 1.0, 0)
    coatin = ImageDissolve("id_clouds.png", 1.0, 0)
    coatout = ImageDissolve("id_clouds.png", 1.0, 0, reverse=True)
    logosin = ImageDissolve("logosfade.png", 2.0, 0)
    cutright = ImageDissolve("id_leftright.png",0.2, 0)
    rightleft = ImageDissolve("id_rightleft.png",0.2, 0)
    down = ImageDissolve("id_down.png",0.2, 0)
    up = ImageDissolve("id_up.png",0.2, 0)
    menu = nvl_menu
    style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
#    renpy.music.set_volume(0.4, .5, channel="music")
    flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    slowflashbulb = Fade(1.0, 0.5, 2.0, color='#fff')
    slowdissolve = Dissolve(1.0)
    fastdissolve = Dissolve(0.15)
    fasterdissolve = Dissolve(0.075)
   
    circleirisout = ImageDissolve("id_circleiris.png", 1.0, 8)
    circleirisin = ImageDissolve("id_circleiris.png", 1.0, 8, reverse=True)
    
    circleirisoutfast = ImageDissolve("id_circleiris.png", 0.75, 8)
    circleirisinfast = ImageDissolve("id_circleiris.png", 0.75, 8, reverse=True)
    
    renpy.music.register_channel("sound2", "sfx", 0)
    
    renpy.music.register_channel("sfxloop", "sfx", 1)
    if persistent.volume_set == None:
        _preferences.set_volume("sfx", 0.5)
        persistent.volume_set = True
    
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
    
    slow_move = MoveTransition(1.0)
    fast_move = MoveTransition(0.2)
    rapid_move = MoveTransition(0.1)
    
    # Screen shake effect.
    sshake = Shake((0, 0, 0, 0), 1.0, dist=30)
    
    # Viewport adjustements. Each screen needs its own adj!
    # adj = ui.adjustment(adjustable = True)
    # adjttn = ui.adjustment()
    # adjTC = ui.adjustment()
    # adjAch = ui.adjustment()
    
    music_need = True
    ecbg = "black"
    ecfg = "fff"
    # Faux movie announcer voice
    style.movie = Style(style.default)
    # Comment everything with "style.movie." below to disable the {=movie}{/=movie} tag effects
    # # style.movie.font = "DejaVuSansMono.ttf"
    # if persistent.text_styling == "Extra":
    #     style.movie.font = "DejaVuSerif.ttf"
    # # style.movie.size = 23
    # # style.movie.kerning = 1
    
    # Loud voice
    style.loud = Style(style.default)
    # Comment everything with "style.loud." below to disable the {=loud}{/=loud} tag effects
    # if persistent.text_styling == "Extra":
    #     style.loud.size = 24
    
    # Shouting voice
    style.shout = Style(style.default)
    # Comment everything with "style.shout." below to disable the {=shout}{/=shout} tag effects
    # if persistent.text_styling == "Extra":
    #     style.shout.size = 32
    
    # Quieter voice
    style.quiet = Style(style.default)
    # Comment everything with "style.quiet." below to disable the {=quiet}{/=quiet} tag effects
    # if persistent.text_styling == "Extra":
        # style.quiet.size = 20
    
    # Whispering voice
    style.whisper = Style(style.default)
    # Comment everything with "style.whisper." below to disable the {=whisper}{/=whisper} tag effects
    # if persistent.text_styling == "Extra":
    #     style.whisper.size = 15
        
    renpy.register_style_preference("text", "Vanilla", style.movie, "font", "DejaVuSans.ttf")
    renpy.register_style_preference("text", "Vanilla", style.loud, "size", 22)
    renpy.register_style_preference("text", "Vanilla", style.shout, "size", 22)
    renpy.register_style_preference("text", "Vanilla", style.whisper, "size", 22)
    
    renpy.register_style_preference("text", "Extra", style.movie, "font", "DejaVuSerif.ttf")
    renpy.register_style_preference("text", "Extra", style.loud, "size", 24)
    renpy.register_style_preference("text", "Extra", style.shout, "size", 32)
    renpy.register_style_preference("text", "Extra", style.whisper, "size", 15)

    centered = Character(None, what_slow_cps=0, what_size = 27, what_outlines = [(1, "#000", 0, 0)],
                        what_layout="subtitle", what_xalign=0.5, what_text_align=0.5,
                        window_background=None, window_yminimum=0, window_xfill=False, 
                        window_xalign=0.5, window_yalign=0.5) 
    
    ## Filraen's note: this is for allowing personal use of left Alt-Tab, as someone else
    ## said once he used Alt instead of Cntrl to skip (forgot who)
    filraen = False
    try:
        with open(r"C:\Users\Alex\.gitconfig", "r") as outfile:
            filraen = True
    except IOError:
        pass
    
    if config.developer:
        if not filraen:
            config.keymap['skip'].remove('K_LCTRL')
            config.keymap['skip'].remove('K_RCTRL')
            config.keymap['skip'].append('K_LALT')
            config.keymap['skip'].append('K_RALT')
        config.keymap['reload_game'].append('r')
        config.keymap['inspector'].append('i')
        config.keymap['developer'].append('d')
        config.keymap['toggle_music'].append('m')
        config.keymap['toggle_music'].append('M')
        
        # config.keymap['viewport_up'].append('K_KP9')
        # config.keymap['viewport_down'].append('K_KP3')
        
    config.keymap['viewport_up'].append('K_PAGEUP')
    config.keymap['viewport_down'].append('K_PAGEDOWN')
    config.keymap['rollback'].append('K_KP9')
    config.keymap['rollforward'].append('K_KP3')
    config.keymap['hide_windows'].append('K_BACKSPACE')
    
    for action in config.keymap.keys():
        if 'K_UP' in config.keymap[action]:
            config.keymap[action].append('K_KP8')
        if 'K_DOWN' in config.keymap[action]:
            config.keymap[action].append('K_KP2')
        if 'K_LEFT' in config.keymap[action]:
            config.keymap[action].append('K_KP4')
        if 'K_RIGHT' in config.keymap[action]:
            config.keymap[action].append('K_KP6')
        if 'K_PAGEUP' in config.keymap[action]:
            config.keymap[action].append('K_KP9')
        if 'K_PAGEDOWN' in config.keymap[action]:
            config.keymap[action].append('K_KP3')
    
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

transform PanScene_SetToRight:
    xpos -1.0    
transform PanScene_SetToLeft:
    xpos 0.0

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
transform PanScene_LeftToOffCenterL:
    # xpos 0.0
    linear 0.15 xpos -0.3
transform PanScene_LeftToOffCenterR:
    # xpos 0.0
    linear 0.15 xpos -0.7
transform PanScene_OffCenterLToLeft:
    xpos -0.3
    linear 0.15 xpos 0.0
transform PanScene_OffCenterLToOffCenterR:
    xpos -0.3
    linear 0.15 xpos -0.7
transform PanScene_OffCenterRToLeft:
    xpos -0.7
    linear 0.15 xpos 0.0
transform PanScene_OffCenterRToOffCenterL:
    xpos -0.7
    linear 0.15 xpos -0.3
transform PanScene_RightToOffCenterL:
    xpos -1.0
    linear 0.15 xpos -0.3
transform PanScene_RightToOffCenterR:
    xpos -1.0
    linear 0.15 xpos -0.7
transform PanScene_OffCenterLToRight:
    xpos -0.3   
    linear 0.15 xpos -1.0
transform PanScene_OffCenterRToRight:
    xpos -0.7  
    linear 0.15 xpos -1.0
transform PanScene_CenterToOffCenterL:
    xpos -0.5    
    linear 0.15 xpos -0.3
transform PanScene_CenterToOffCenterR:
    xpos -0.5    
    linear 0.15 xpos -0.7
    
transform left_RightScreen:
    xpos 1.0 yalign 1.0    
transform center_RightScreen:
    # xpos 1.367 yalign 1.0
    xpos 1.5 yalign 1.0 xanchor 0.5 # xalign 0.5 yalign 1.0    
transform right_RightScreen:
    xanchor 1.0 xpos 2.0 yalign 1.0
    # xpos 1.712 yalign 1.0    
transform TopRight_RightScreen:
   xpos 1.71 yalign 0.0
transform HalfRight_RightScreen:
   xpos 1.6 yalign 1.0    
transform HalfLeft_RightScreen:
    xpos 1.3 yalign 1.0
transform UnderLegs_RightScreen:
    xalign 1.563 yalign 2.2    

    
transform pretr1_kyonpos:
    xanchor 0.5 xpos 0.7 yalign 1.0
    
transform pretr1_mikurupos:
    xanchor 0.5 xpos 0.9 yanchor 1.0 ypos 1.0
    
transform pretr1_kanaepos1:
    xanchor 0.5 xpos 0.37 yanchor 1.0 ypos 1.3
    
transform pretr1_kanaepos2:
    xanchor 0.5 xpos 0.37 yanchor 1.0 ypos 1.1
    
init -1 python:
    # def show_date(st, at):
        # return Text("[date]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf"), None
    def show_date1(st, at):
        return Text("[date1]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf", outlines=[(1, "#000", 2, 1)]), None
    def show_date2(st, at):
        return Text("[date2]", font="DejaVuSerif-Italic.ttf", size=25, color="#3cf", outlines=[(1, "#000", 2, 1)]), None
        
    def color_matrix (c):
        color_tuple = color(c)
        return [ color_tuple[0]/255.0,                      0,                      0,                      0, 0, 
                                      0, color_tuple[1]/255.0,                      0,                      0, 0, 
                                      0,                      0, color_tuple[2]/255.0,                      0, 0, 
                                      0,                      0,                      0, color_tuple[3]/255.0, 0 ]
    def KBDH_Color(st, at):
        return im.MatrixColor("Backgrounds/KBDHLogo-White.png", color_matrix(ecfg)), None

    if persistent.text_styling == None:
        persistent.text_styling = "Vanilla"
    
    if persistent.eyecatch_styling == None:
        persistent.eyecatch_styling = "Dissolves"
    
    if persistent.preview_adv == None:
        persistent.preview_adv = True
        
    chapters = [
        [
            ("In Media Res Prologue:\nExactly What it Says on the Tin", "prologue", True)
        ],
        [
            ("Obligatory Anachronic Order Explanation Arc", "", False),
            ("Chapter One: Scene Twelve,\nthe Ninth Big Fight", "AO1_1", True),
            ("Chapter Two: Clear as Mud", "AO2", True)
        ],
        [
            ("Straightforward Flashback and Exposition Arc", "", False),
            ("Chapter Three: It Goes To Eleven", "SF1", True),
            ("Chapter Four: Epileptic Plot Tree", "SF2", True),
            ("Chapter Five: The Requisite Haruhi-and-Kyon in Closed Space Together Again Part (You Know The One)", "SF3", True)
        ],
        [   ("Volume II prologue", "Vol02_start", True),
            ("Heroic Antics Begin Arc - 1", "", False),
            ("Chapter Six: Finally, Some Action", "HAB1", True),
            ("Chapter Seven: Rise To Delinquency; Requisite Angst Spots", "HAB2", True),
        ],
        [
            ("Filler Arc - 1", "", False),
            ("Chapter Eight: Relationship Building", "Fi1", True),
            ("Chapter Nine: Family Matters", "Fi2", True),
        ],    
        [   ("Heroic Antics Begin Arc - 2", "", False),
            ("Chapter Ten: School of Hard Knocks", "HAB3", True),
            ("Chapter Eleven: Yeah, It Went There", "HAB4", True),
        ],
        [
            ("Label a scene you're working on test and use this", "Test", True),
            # ("-----", "backtomain"),
                   
            ("Credits", "credits", True),
            ("Credits (rolling)", "credits_roll", True),
            ("Another testbed, Eyecatchies", "test_Z0_eye", True),
            ("Another testbed, Title cards", "test_Z0_titles", True),
            ("Another testbed, Time-Travel Notes", "test_Z0_TTN", True),
            ("Another testbed, Cheatzz!!11", "test_Z0_likeaboss", True),
            ("Trope Collection System Test!", "test_hyperlinks", True),
            ("A test!", "test2", True)
            ],
        ]
        
#    style.hyperlink_text = style.default
    
    
    Xtras_DB_Dossiers = [
            ('SOS Brigade', 'XDBD_sos'),
            ('Affiliates', 'XDBD_frnd'),
            ('Adversaries', 'XDBD_enmy'),
            ('Other', 'XDBD_rest'),
        ]
    
    
    if persistent.unlocks == None:
        persistent.unlocks = {}
        persistent.unlocks["db-ttn"] = {"name":"Kyon's Time-travel list", "price":5, "state":False}
    
    _unlocks = {}
    _unlocks["name"] = "db-ttn"
    _unlocks["back"] = "Database"
    
    
    if persistent.ttnotes == None:
        persistent.ttnotes = []
    
    if persistent.ttnmode == None:
        persistent.ttnmode = 'order'
    
    ttnmode = persistent.ttnmode
    
    # Appends the TTnote with destination = first arg and description = second arg  to TODO list,
    #  if there were no entry with exactly the same contents. Third arg can be left out in most cases.
    def TTN_append(destination = (00, 00), descr = 'Testing', pending = True):
        if {'dest':destination, 'descr':descr, 'pending':True} in persistent.ttnotes:
            return False
        if {'dest':destination, 'descr':descr, 'pending':False} in persistent.ttnotes:
            return False
        persistent.ttnotes.append({'dest':destination, 'descr':descr, 'pending':pending})
        # persistent.ttnotes2 = 
        
    # Marks TTN entry with id (its position in Extras when "shown as added", starting with 0) as filfulled
    def TTN_markDone(id = 0):
        if id < len(persistent.ttnotes):
            persistent.ttnotes[id]['pending'] = False
            return True
        else:
            return False
    
    # Given tuple of (DayOfMonth, Month), returns string "Monthname Day'th"
    def tupledest2date(tupledest = (0, 0)):
        monthlist = ['Zerober', 'January', 'February', 'Marth', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Notmonthber']
        if tupledest[1] >= len(monthlist):
            return False
        month = monthlist[tupledest[1]]
        if tupledest[0] == 1:
            day = '1st'
        elif tupledest[0] == 2:
            day = '2nd'
        elif tupledest[0] == 3:
            day = '3rd'
        else:
            day = str(tupledest[0]) + 'th'
        if len(tupledest) == 3:
            return str(month + ' ' + day + ', ' + str(tupledest[2]))
        else:
            return str(month + ' ' + day)

    # Given tuple (DayOfMonth, Monthname), returns tuple of (DayOfMonth, Month)
    def tupledate2dest(tupledest = (32, 'Zerober')):
        monthlist = ['Zerober', 'January', 'February', 'Marth', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Notmonthber']
        if tupledest[1] not in monthlist:
            return False
        month = monthlist.index(tupledest[1])
        day = tupledest[0]
        if len(tupledest) == 3:
            return (month, day, tupledest[2])
        else:
            return (month, day)

    # Key function for sorting the TTN list by destination date
    def ttndestkey(e):
        return e['dest']
    
    
    if persistent.unlockedAchievs == None:
        persistent.unlockedAchievs = []
     
    achievements = []
    
    # Achievement['Name of the achievement', 'Achievement description', reward for earning it]
    # Achievements are displayed in the order they are registered.
    achievements.append(['The Beginning', 'Started reading from the very beginning', 2])
    achievements.append(['The Narrator', 'Mastered the best faux movie announcer voice-over', 1])
    achievements.append(['The Call', 'Responded to The Call ... from the Yuki', 1])
    achievements.append(['Stab The Stab', 'Took down the Asakura', 1])
    achievements.append(['The Awakening', 'Awakened the Goddess', 3])
    
    # Given the name of the achievement return its ID (number)
    def getAchievID(name):
        i_i = 0
        for iter in achievements:
            if iter[0] == name:
                return i_i
            else:
                i_i += 1
        return -1
    
    # To unlock the achievement either call "$ UnlockAchiev('Name of the achievement')"
    # or "$ UnlockAchiev(id=achievenemt_ID)"    (without " of course)
    def UnlockAchiev(name='~!default~!', id='~!default~!'):
        global persistent
        if id == '~!default~!':
            if name == '~!default~!':
                return False
            id = getAchievID(name)
            if id != -1:
                if id not in persistent.unlockedAchievs:
                    persistent.balance += achievements[id][2]
                    persistent.unlockedAchievs.append(id)
                return True
            else:
                return False
        else:
            if id < len(achievements):
                if id not in persistent.unlockedAchievs:
                    persistent.balance += achievements[id][2]
                    persistent.unlockedAchievs.append(id)
                return True
            else:
                return False
    
    if persistent.balance == None:
        persistent.balance = 0
    
    # Set this to the maximum number of tropes one can get
    max_tropes = 10
    
    xtras_origin = ""
    
    if persistent.collected_tropes == None:
        persistent.collected_tropes = {}

    def clicked_func(x):
        renpy.sound.play("SE/block.mp3")
        if not x in persistent.collected_tropes.keys():
            persistent.collected_tropes[x] = True
            persistent.balance += 1
        return None

    style.default.hyperlink_functions = (
        lambda x: style.default,
        clicked_func,
        lambda x: None
        )
    ecbg = "black"
    ecfg = "fff"

label backtomain:
    return

label start:
    # Z0 : intro. 
    stop music
    scene black
    $ UnlockAchiev(id=0)
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
    #stop music
    play music "Music/GodKnowsMetal(edit).ogg"
    scene black with fade
    # The hardpause calls are necessary because otherwise Ren'py wants to skip over all the pause statements on a single press of the key.
    # show Credits0 with dissolve
    show creds 0 at truecenter with Dissolve(3.0)
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
    stop music fadeout 2
    jump Preview
    
label credits_roll:
    play music "Music/GodKnowsMetal(edit).ogg"
    scene black with dissolve
    show credroll at Position(xalign=0.5, yanchor=0.0, ypos=1.0) with None
    show KBDHLogoWhite at Position(xalign=0.5, yanchor=0.5, ypos=1.5) with None
    show credroll at Position(xalign=0.5, yanchor=1.0, ypos=1.0) with MoveTransition(34)
    show KBDHLogoWhite:
        linear 8 ypos 0.5
    show credroll:
        linear 8 ypos 0.0
    ## MoveTrasition to Linear rate is seems to be 4:1 + couple of seconds to MT
    # show BDVNlogo at Position(xalign=0.5, yanchor=0.5, ypos=1.5) with None
    # show BDVNlogo:
        # linear 5 ypos 0.5
    # show credroll:
        # linear 5 ypos 0.0
    # show WaitForInputBlinking:
        # alpha 0.0 right
        # linear 5 pass
        # alpha 1.0
    pause
    stop music fadeout 1
    hide BDVNlogo with coatout
    jump Preview2
    
label Preview:
    play music "Music/Bouken(Credits).mp3"
    scene P1:
        size (800,600)
    show Popen at truecenter
    with fade
    #pause
    $ renpy.pause(3.0, hard=True)
    scene P2 with dissolve:
        size (800,600)
    #pause
    $ renpy.pause(3.0, hard=True)
    scene P3 with dissolve:
        size (800,600)
    #pause
    $ renpy.pause(3.0, hard=True)
    scene P4 with dissolve:
        size (800,600)
    #pause
    $ renpy.pause(3.0, hard=True)
    scene P5 with dissolve:
        size (800,600)
    $ renpy.pause(3.0, hard=True)    
    scene black with fade
    hide Popen
    show Pexit at truecenter
    with dissolve
    stop music
    #pause
    $ renpy.pause(3.0, hard=True)
    return
    
label Preview2:
    play music "Music/Bouken(Credits).mp3"
    # scene black with dissolve
    show P1 at truecenter:
        size (800,600)
    show Popen2 at Position(xanchor=0.5, xpos=0.55, yanchor=0.5, ypos=0.75) onlayer upper
    if persistent.preview_adv:
        pause 3.0
        $ renpy.pause(0.1, hard=True)
    else:
        pause
    show P2 at Position(xanchor=0.5, xpos=1.5, yalign=0.5):
        size (800,600)
    show P2 at truecenter with moveinleft:
        size (800,600)
    hide P1
    if persistent.preview_adv:
        pause 3.0
        $ renpy.pause(0.1, hard=True)
    else:
        pause
    show P3 at Position(xanchor=0.5, xpos=-0.5, yalign=0.5):
        size (800,600)
    show P3 at truecenter with moveinright:
        size (800,600)
    hide P2
    if persistent.preview_adv:
        pause 3.0
        $ renpy.pause(0.1, hard=True)
    else:
        pause
    show P4 at Position(yanchor=0.5, ypos=-0.5, xalign=0.5):
        size (800,600)
    show P4 at truecenter with moveintop:
        size (800,600)
    hide P3
    if persistent.preview_adv:
        pause 3.0
        $ renpy.pause(0.1, hard=True)
    else:
        pause
    # show P5 at Position(yanchor=0.5, ypos=-0.5, xalign=0.5):
        # size (800,600)
    show P5 at truecenter with moveinright:
        size (800,600)
    hide P4
    if persistent.preview_adv:
        pause 3.0
        $ renpy.pause(0.1, hard=True)
    else:
        pause 
    hide Popen2 onlayer upper  
    scene black with dissolve
    show Pexit at truecenter
    with dissolve
    stop music
    #pause
    $ renpy.pause(3.0, hard=True)
    return

# White eyecatch routine with single date to show.
# label white_eyecatch_single(date="", pause_time=3.0, r=0, ecbg="black"):
#     #scene eyebg with Dissolve(1)
#     $ date = "\n\n\n\n" + date
#     show SOSlogoborder with logosin
#     show transpwhite behind SOSlogoborder with slowdissolve
#     # call eyecatch_coatinout(date, date, pause_time) from eyecatch_generic
#     call eyecatch_dissolves(date, date, pause_time) from white_eyecatch_s
#     scene black with Dissolve(0.5)
#     return

# White eyecatch routine with two dates to show, second replacing first. Default
# values are a wonderful thing.
label eyecatch_fancy(date1="", date2="", pause_time=3.0, r=0, ecbg="black"):
    #scene eyebg with Dissolve(1)
    python:
        if date2 == "":
            date2 = date1
    $ nw = _window
    $ _window = False
    $ date1 = "\n\n\n\n" + date1
    $ date2 = "\n\n\n\n" + date2
    show SOSlogoborder with logosin
    show transpwhite behind SOSlogoborder with slowdissolve
    # call eyecatch_coatinout(date, date, pause_time) from eyecatch_generic
    call eyecatch_dissolves(date1, date2, pause_time, r) from white_eyecatch_d
    scene black with Dissolve(0.5)
    $ _window = nw
    return

# Generic eyecatch routine with single date to show.
label eyecatch(date="", pause_time=3.0, r=0, ecbg="black"):
    scene eyebg with Dissolve(1)
    # call eyecatch_coatinout(date, date, pause_time) from eyecatch_generic
    if persistent.eyecatch_styling == "Moves":
        call eyecatch_random(date, date, pause_time, r) from eyecatch_genericM
    else:
        call eyecatch_dissolves(date, date, pause_time, r) from eyecatch_genericD
    scene black with Dissolve(0.5)
    return

# Generic eyecatch routine with two dates to show, second replacing first.
label eyecatch2(date1="", date2="", pause_time=3.0, r=0, ecbg="black"):
    scene image(ecbg) with Dissolve(1)
    # call eyecatch_coatinout(pause_time) from eyecatch_generic
    if persistent.eyecatch_styling == "Moves":
        call eyecatch_random(date1, date2, pause_time, r) from eyecatch_genericM2
    else:
        call eyecatch_dissolves(date1, date2, pause_time, r) from eyecatch_genericD2
    scene image(ecbg) with Dissolve(0.5)
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
    
label eyecatch_dissolves(date1="", date2="", pause_time=2.0, r=0):
    # randomly choses the way logo appears and disappears with every call
    # uses dissolve and coatin/coatout.
    $ pause2 = pause_time/2
    # scene black with Dissolve(1)
    if r == 0 or r > 5:
        $ r = renpy.random.randint(1, 5)
        
    if r == 1:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with Dissolve(1.0)
        pause pause2
        show eyeDate 2 at date_pos with wiperight
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with Dissolve(1.0)
    elif r == 2:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with coatin
        pause pause2
        show eyeDate 2 at date_pos with wipeleft
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with coatout  
    elif r == 3:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with coatout
        pause pause2
        show eyeDate 2 at date_pos with wiperight
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with coatin   
    elif r == 4:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with teleportfaster
        pause pause2
        show eyeDate 2 at date_pos with wipeleft
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with teleportfaster  
    else:
        show BDVNlogo at truecenter
        show eyeDate 1 at date_pos
        with circleirisout
        pause pause2
        show eyeDate 2 at date_pos with dissolve
        pause pause2
        hide BDVNlogo
        hide eyeDate
        with circleirisin
    # Works just as well as hardpause in prevesting skipping the fade, but does not block the rollback
    centered "{nw}"
    return

label eyecatch_random(date1="", date2="", pause_time=2.0, r=0):
    # randomly choses the way logo appears and disappears with every call
    $ pause2 = pause_time/2
    # scene black with Dissolve(1)
    if r < 1 or r > 5:
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

label eyecatch_white(date="", pause_time=3.0, r=0, ecbg="black"):
    scene white with Dissolve(1)
    # call eyecatch_random(date, date, pause_time, r)
    $ pause2 = pause_time/2
    $ date1 = date
    $ date2 = date
    show BDVNlogoBlack at truecenter
    show eyeDate 1 at date_pos
    with coatin
    pause pause2
    show eyeDate 2 at date_pos with dissolve
    pause pause2
    hide BDVNlogoBlack
    hide eyeDate
    with coatout
    scene white with Dissolve(0.5)
    return    

label eyecatch_generic(date1="", date2="", pause_time = 3.0, r = 0, ecbg = "900", ecfgcolor = "fff"):
    
    $ ecfg = ecfgcolor
    # Define transitions
    if r < 1 or r > 5:
        $ r = renpy.random.randint(1, 5)

    $ eyecatch_transition_in = [moveinright, moveinleft, moveintop, moveinbottom, coatin][r-1]
    $ eyecatch_transition_out = [moveoutleft, moveoutright, moveoutbottom, moveouttop, coatout][r-1]
    
    scene eyeSolidBackground with Dissolve(1)
    show KBDHLogoColor at truecenter
    show eyeDateColor 1 at date_pos
    with eyecatch_transition_in
    pause (pause_time * 0.3)
    show eyeDateColor 2 at date_pos with wiperight
    pause (pause_time * 0.7)
    centered "{nw}" # If it skips over the out transitions, then it really messes up the rolling credits later. Don't ask me why.
    hide KBDHLogoColor
    hide eyeDateColor
    with eyecatch_transition_out
    show eyeSolidBackground
    return

label test_hyperlinks:
    scene bg MorningSky
    "This is test text for {a=Ordinary High School Student}hyperlinks{/a}!"
    return

label Ordinary_High_School_Student:
    "Text!"
    return
    
label test_Z0_eye:
    # Silly test is silly
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    # $ ttnt = len(persistent.ttnotes)
    "Now a new spiffy eyecatch with white screenage!"
    # $ TTN_append((32, 4), "Test Mikuru's time travelling gear")
    call eyecatch_fancy("Febtober 3.14, 1592") from test_Z0_p1006
    scene bg MorningSky
    show TownHillLeftMorning
    # show Kyon Sigh1 at right
    show Asakura Unhap1 at center
    show SpikeFlick at center
    # $ ttnt = len(persistent.ttnotes)
    "\"{=loud}You opened{/=loud} it already, {=shout}I see{/=shout}.\""
    "[style.movie.font] - [style.loud.size] - [style.shout.size] - [style.whisper.size]"
    call eyecatch2(pause_time=3.0, "Date 1", "Second one") from test_Z0_p0000
    "Testing \"Dissolves\" eyecatch style"
    call eyecatch_dissolves("Date 1", "Second one", r=1) from test_Z0_p0100
    call eyecatch_dissolves("Date 1", "Second one", r=2) from test_Z0_p0101
    call eyecatch_dissolves("Date 1", "Second one", r=3) from test_Z0_p0102
    call eyecatch_dissolves("Date 1", "Second one", r=4) from test_Z0_p0103
    call eyecatch_dissolves("Date 1", "Second one", r=5) from test_Z0_p0104
    "Testing \"Moves In-Out\" eyecatch style"
    call eyecatch_random("Date 1", "Second one", r=1) from test_Z0_p0110
    call eyecatch_random("Date 1", "Second one", r=2) from test_Z0_p0111
    call eyecatch_random("Date 1", "Second one", r=3) from test_Z0_p0112
    call eyecatch_random("Date 1", "Second one", r=4) from test_Z0_p0113
    call eyecatch_random("Date 1", "Second one", r=5) from test_Z0_p0114
    "!S[style.movie.font] - [style.loud.size] - [style.shout.size] - [style.whisper.size]"
    # $ TTN_append((19, 1), "Once again, test Mikuru's time travelling gear")
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
    # $ TTN_markDone(0)
    # call the eyecatch routine, supply the date (text) to show, specify the unique "from"
    call eyecatch_random("February 30, 1999", "February 30, 1999") from test_Z0_p0004
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Kyon Sigh1 at right
    with dissolve
    "And another one. (but effect may be the same. Randomness, y'know)"
    # call the eyecatch routine, can supply nothing if nothing needs to be changed, specify the unique "from"
    call eyecatch_random("Febtober 3.14, 1592", "Febtober 2.7, 1828") from test_Z0_p0005
    # activate the next scene with dissolve (or whatever else).
    scene bg MorningSky
    show TownHillLeftMorning
    show Haruhi Smile3 at left
    with dissolve
    scene bg Library with dissolve
    "Call to eyecatch with custom foreground and background colors. Using a placeholder image (image should be white on transparent background)"
    call eyecatch_generic("starting", "well... not anymore", 3.0, 0, "#ddd", "#222")
    "Thats all!"
    # If you specify the names of arguments, you don't have to worry about positions
    call eyecatch(pause_time=3, r=5) from test_Z0_p0007
    
    # $ persistent.ttnotes = persistent.ttnotes[0:-2]
    
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
    show title 006 at card_pos with slowfadein
    pause
    show title 007 at card_pos with slowfadein
    pause
    show title 008 at card_pos with slowfadein
    pause
    show title 009 at card_pos with slowfadein
    pause
    show title 010 at card_pos with slowfadein
    pause
    show title 011 at card_pos with slowfadein
    pause
    return

label test_Z0_TTN:
    scene bg MorningSky
    show TownHillLeftMorning
    "Adding a TTN with destination of April, 34th and description: \"Test Mikuru-chan's time travelling gear.\"."
    $ TTN_append((34, 4), "Test Mikuru's time travelling gear.")
    "You can check the Extras now, and note that previous command does not add a TTN if there is one with exact same contents in the list."
    "Adding a TTN with destination of February, 1st and description: \"Now, test Asahina-san's time travelling gear.\"."
    $ TTN_append((1, 2), "Now, test Asahina-san's time travelling gear.")
    "You can check the Extras for second entry."
    "And now, marking first entry as done."
    $ TTN_markDone(0)
    "Thats all"
    return
    
label test_Z0_fragTTN:
    "Voiding TTN list..."
    $ persistent.ttnotes = []
    extend "Done!"
    return
    
label test_Z0_likeaboss:
    menu:
        "Pick your poison"
        "UUDDLRLRBA":
            $ persistent.balance = persistent.balance + 10
            "You feel power rushing through your very core! +10 Þ ...What a let-down."
        "Negate above":
            $ persistent.balance = persistent.balance - 10
            "You feel you wallet lightening a bit. -10 Þ ...What kind of a cheat is that!"
        "Frag yourself":
            $ persistent.ttnotes = []
            "You feel your memories of a thing you need to done leave you. Time-travel notes voided."
        "Lock everything up":
            python:
                for e in persistent.unlocks.keys():
                    persistent.unlocks[e]["state"] = False
            "You feel like you just lost access to all the extra you had unlocked so far..."
    "Done!"
    return
    
