# This is a proof-of-concept K:BDH VN.

init:    
    image bg classroom = "Backgrounds/classroom.jpg"
    image bg hallway = "Backgrounds/hallway.png"
    image bg stairwell = "Backgrounds/stairwell.jpg"
    image white = "#ffffff"
    image black = "#000000"
    image yukibackground = "#ccccff"
    image title = "Backgrounds/title1.png"
    image Barrier = "Backgrounds/barrier2.jpg"
    image Bluesword = "Backgrounds/bluesword0.jpg"
    image field = "Sprites/InterdictionField.png"
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
    image Kyon Ser1 = "Sprites/Kyon/KyonSerious1.png"
    image Kyon Ser2 = "Sprites/Kyon/KyonSerious2.png"
    image Kyon Ser2 Bright = im.MatrixColor("Sprites/Kyon/KyonSerious2.png",
                                       im.matrix.brightness(.5))
    image Kyon Sigh1 = "Sprites/Kyon/KyonSigh1.png"
    image Kyon Sigh2 = "Sprites/Kyon/KyonSigh2.png"
    image Kyon Neutral1 = "Sprites/Kyon/KyonNeutral1.png"
    image Kyon Neutral2 = "Sprites/Kyon/KyonNeutral2.png"
    image Kyon Ang1 = "Sprites/Kyon/KyonAngry1.png"
    image Skinsuit = "Sprites/Kyon/KyonSkinsuitTemplate.png"
    image Skinsuit Bright = im.MatrixColor("Sprites/Kyon/KyonSkinsuitTemplate.png",
                                       im.matrix.brightness(.5))
    image Asakura Smile1 = "Sprites/Asakura/AsakuraSmile1.png"
    image Asakura Smile2 = "Sprites/Asakura/AsakuraSmile2.png"
    image Asakura Sup1 = "Sprites/Asakura/AsakuraSurprise1.png"
    image Asakura Frown1 = "Sprites/Asakura/AsakuraFrown1.png"
    image Asakura Frown2 = "Sprites/Asakura/AsakuraFrown2.png"

    python: # TODO: figure out a way to quickly switch on/off the window show/hide statements below.
        basechar = Character(None, kind=nvl)
        kyon = Character("Kyon", kind=basechar, color="#777755")
        sister = Character("Nonoko", kind=basechar, color="#999977")
        yuki = Character("Nagato Yuki", kind=basechar, color="#aaaaff")
        narrator = Character(None, kind=basechar)
        irisoutfast = CropMove(0.2, "irisout")
        slowfadein = Fade(0.5, 0.5, 5)
        wipeleftfast = CropMove(0.3, "wipeleft")
        menu = nvl_menu
        style.nvl_window.background = "nvl_window.png"
        style.nvl_window.xpadding = 55
        style.nvl_window.ypadding = 55
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve

label start:
#    scene black with fade
    scene title with slowfadein
    
    pause
    
#    window show
    
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
    #play sound "dashwacky.wav"
    show Haruhi Sup1 at left
    show Kyon Ser1 at center
    "\"Bwa!\" she protested, arms waving frantically as she dashed to keep up, or risk the knot being pulled out." 
    show Haruhi Ang2 at left
    "\"What the hell do you think you're doing!?\""
    show Haruhi Sup1 at left
    scene bg hallway with None:
        xanchor .5 yanchor .5
        xpos .5 ypos .5
        linear .3 rotate 360

    hide Haruhi
    hide Kyon 
    with fade    
    
    pause 1.0
    nvl clear
    scene bg stairwell with fade:
        size (800,600)
    "Naturally, he said nothing to her during the entire mad dash to the remote stairwell where she had first hauled him by his own tie, so long ago."
    "He released her at the top of the steps after looking around to ensure that no one else was nearby."
    "Her momentum carried her forward, resulting in him pressing one hand flat against her chest, just below her neck."
    "Her eyes quickly sharpened, her features fixed into a scowl."
    nvl clear
    show Haruhi Ang3 at left
    "\"What the hell, Kyon!?\""
    show Kyon Ser1 at right
    "He held up one hand and said, \"Something's up.\""
    show Haruhi Hap3 at left
    "Her irritation vanished instantly, replaced with wide-eyed excitement. She clapped her hands together and hopped from foot to foot."
    show Haruhi Hap4 at left
    "\"Yes!\" she cheered. \"It's been so boring lately!\""
    nvl clear
    "\"This better not be your fault!\""
    show Kyon Sigh1 at right
    "He shook his head in irritation, then patted his left coat pocket. Then right, then both pants pockets, then the back of each hand."
    "After that, he traced the fingertips of his right hand above his ear, eyes distant, and pulled his cell phone from one pocket."
    nvl clear
    show Haruhi Ang1 at left
    "\"What is it?\" she asked, when he spent a long minute studying the screen."
    show Kyon Neutral1 at right
    "\"Maybe a false alarm,\" he admitted, shifting his shoulders.{nw}"
    $ nvl_erase()
    "\"Maybe a false alarm,\" he admitted, shifting his shoulders. {fast}\"Are you messing with me?\""
    show Kyon Ang1 at right
    show Haruhi Ang2 at left
    "\"I should be asking you that! But whatever! You hauled me all the way out here—by my shirt, I might add!—so tongues are going to wag! If you're going to do this, then you know what I want!\""
    show Haruhi Hap1 at left
    nvl clear
    show Kyon Sigh2 at right
    "\"Haruhi....\""
    show Haruhi Hap2 at left
    "\"Do it!\" she said, bouncing on the balls of her feet in excitement. \"I want to see it!\""
    show Kyon Neutral2 at right
    "\"Is now really the time? Break's going to be over soon—\""
    show Haruhi Hap3 at left
    "\"Get it out now! I want to see!\""
    nvl clear
    show Kyon Sigh1 at right
    "Heaving the sigh of the eternally doomed, he put his phone away and muttered underneath his breath."
    show Haruhi Hap4 at left
    "\"Do that voice, too! You know the one? Like from a movie voice-over guy? I love that! Do it! Come on!\""
    show Kyon Ser1 at right
    "\"Fine,\" he grumbled.{nw}"
    $ nvl_erase()
    show Kyon Sigh2 at right
    nvl clear
    "\"Fine,\" he grumbled. {fast}\"But you come up with the excuse for class.\""
    show Haruhi Hap4 at left
    "\"Student council president,\" she said without hesitation. \"Blame him.\""
    show Kyon Sigh2 at right
    "\"Ahem,\" he coughed, shooting her a dark look.{nw}"
    $ nvl_erase()
    show Kyon Ser1 at right
    stop music fadeout 1
    "\"Ahem,\" he coughed, shooting her a dark look. {fast}\"Take a step back, I don't want to catch you in the interdiction field again.\""
    show Haruhi Hap4 at left
    "She nodded and stepped backwards, against the wall."
    nvl clear 
    #This is where all the sound and special effects go!
    play music "music/YukiAsakuraFight.mp3" fadein 1
    show Kyon Ser2 at right
    pause 1
    play sound "SE/DunDun.wav"
    "Standing perfectly straight, hands at his sides, he closed his eyes, and began speaking in his best faux movie announcer voice-over."
    play sound "SE/Sizzle2.wav"
    show Skinsuit at right with dissolve
    "\"Skinsuit active,\" as something that looked like nothing so much as black paint suddenly engulfed his entire body beneath his uniform."
    nvl clear
    play sound "SE/NanoRepair.wav"
    "\"Gravimetric stabilizers and secondary gyrometrics online,\" as ridged metal studs appeared on the back of each knuckle, and beneath his uniform pants, metallic vertical rails were described in the skinsuit."
    nvl clear
    #WTB Custom Greatcoat sprite. =D
    play sound "SE/CloakOff.wav"
    "\"Greatcoat thermoptic and tactile stealth disengaged,\" as a knee-length tan greatcoat coalesced, covering his shoulders with a thick mantle."
    show Haruhi Hap3 at left
    "\"Doesn't that get hot?\" Her smile had only grown, her eyes shining with anticipation."
    nvl clear
    show Kyon Neutral2 at right
    "\"We had environmental conditioning added last night, since the weather's heating up,\" he said in a normal voice."
    show Kyon Ser2 at right
    "Switching back, he said, \"Primary weapons check.\""     
    nvl clear
    play sound "SE/lowswoosh.wav"
    pause .02
    play sound "SE/lowswoosh.wav"
    pause .02
    play sound "SE/lowswoosh.wav"
    "He pulled a fifty centimeter long glittering metal cylinder from within the greatcoat, releasing it to spin on its axis in midair to one side, announcing, \"Long range precision and high yield weaponry is at full charge.\""
    play sound "SE/Barrier2.wav"
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show field at right with dissolve
    pause .1
    hide field at right
    show Kyon Ser2 at right
    show Skinsuit at right
    with dissolve
   # show Barrier with irisoutfast
   # hide Barrier with dissolve    
    "A circle of light appeared on the floor around him, a simple white ring with glittering sparks chasing around in either direction, sending brilliant flashes to streak upwards."
    nvl clear
    "Another cylinder, wider but shorter than the last was released to float next to the first."
    "\"Mid- and short-range crowd-control weaponry is at ... ninety seven percent capacity and charging,\" he continued, squinting at the featureless gunmetal tube."
    nvl clear
    play sound "SE/clink.wav"
    "Pulling a well-crafted sword hilt with no cross-guard or blade from one pocket, he released it horizontally, and it hung before him between the other weapons. \"Beam saber is at full capacity.\""
    show Kyon Ser1 at right
    "After pulling his cell phone from one pocket, he brushed his fingertips over his ear, revealing three dull metal studs in the skinsuit."
    "\"All systems nominal; no proximity alarms—\""
    nvl clear
    show Kyon Ang1 at right
    "He broke off suddenly, scowling. \"Okay,\" he said in his normal voice. \"My mistake. We've got incoming.\""
    show Haruhi Hap4 at left
    "\"God damn it Kyon, you're so cool when you do this,\" Haruhi gushed, clapping her hands together.{nw}"
    $ nvl_erase()
    show Haruhi Hap4 at left
    "\"God damn it Kyon, you're so cool when you do this,\" Haruhi gushed, clapping her hands together. {fast}\"What is it?\""
    nvl clear
    show Kyon Neutral1 at right
    "\"I'm not sure,\" he said, as a cold, familiar chuckle echoed."
    show Kyon Ser1 at right
    "One eyebrow twitched and he stowed his weapons, banishing the ring of light and flinging his phone at Haruhi."
    show Kyon Ser2 at right
    "\"Speed dial two,\" he snapped. \"Stay in the circle.\""
    show Haruhi Pout1 at left
    play sound "SE/Barrier1.wav"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    "She pouted, but did as she was told, the ring of light reappearing on the floor around her this time."
    nvl clear
    hide Kyon Ser2
    hide Skinsuit
    hide Haruhi Pout1
    play sound "SE/footsteps5.wav" 
    pause 5
    show Asakura Smile2 at center with wipeup
    pause 1
    play sound "SE/DunDun.wav"
    show Asakura Smile1 at center
    "\"Kyon-kun~!\" someone caroled up the stairwell, the echoing click of their shoes sounding as they climbed the stairs."
    show Asakura Smile2 at center
    "\"It's been a while, hasn't it?\""
    show Asakura Sup1 at center
    play sound "SE/saberon.wav"
    show Bluesword with wipeleftfast
    pause (1)
    hide Bluesword with dissolve
    "The school bell chimed just as she rounded the landing, and he activated the beam saber. The blade made a crackling, whirring buzz and shed a soft, pale blue light."
    show Asakura Frown1 at center
    "\"Y...you....\" she began, before she frowned, blinking, staring at the energy weapon."
    nvl clear
    show Asakura Frown1 at left
    show Kyon Ang1 at right
    show Skinsuit at right
    "\"Long time no see,\" he said, switching stance to the long-sword style, Ni-Ten Ichi Ryu."
    show Asakura Frown2 at left
    "\"Um.... Hm. This is different. You've certainly changed, Kyon-kun.\""
    nvl clear
    show Kyon Ser2 at right
    "\"That's funny, Asakura-san, because you haven't.\""
    
    scene black with fade
    #nvl clear
    #"Haruhi bounced on her heels with a wide grin, holding Kyon's cell phone in both hands as she remained in the center of the glowing circle."
    #"\"I knew it!\" she cheered.{fast}\"There was something off about Asakura! What is it?\""
    #"\"Um...\" the onetime class representative said, frowning."
    #"\"She's alien,\" Kyon volunteered.{fast}\"From the same place as Yuki-chan and Kimidori, but she tried to kill me once.\""
    #"\"Whaaaat? What did you do to make her mad?\" Haruhi asked, looking at him in bemusement."
    #nvl clear
    #"\"Er,\" Asakura said, crossing her arms beneath her chest."
    #"\"Evidently my information requires an update. I was sent to dispatch Kyon-kun, because he's become an undesirable element for my superiors.\""
    #"\"Really, I'd hoped to see a new state, maybe even provoke it with his death.\""
    #"\"But, those toys seem to say that's already happened! So disappointing ... I suppose if I'd been more patient, I could see it anyway?\""
    #"\"I personally like to see it as a lesson on the effects of randomly stabbing people,\" Kyon muttered."
    #nvl clear
    #"\"Oh, it wasn't random,\" she countered.{fast}\"It was highly specific! I put a whole two hours of thought into it, you know. For us, that's quite a while!\""
    #"\"I'm touched,\" he said dryly."
    #nvl clear
    #"\"Blah blah blah,\" Haruhi muttered, crossing her arms over her chest and rolling her eyes."
    #"\"Skip the speeches -- if I don't know the complete back story, it's all meaningless to me. I think it's about time we get down to business, right?\""
    #nvl clear
    #"\"Happy to oblige!\" Asakura said brightly, as their surroundings pulsed, the window turning into a gunmetal gray steel barrier, strange patterns coalescing across the walls."
    #"The circle on the floor around Haruhi abruptly winked out."
    #nvl clear
    #"\"Now, I've converted the entire space of this stairwell into-\""
    #Kyon spun on one foot, crying out with a great, \"Ki-yah!\" and kicking the door halfway across the roof."
    #"Sparing no more time, he swept Haruhi up in one arm and dashed through the opening."
    #nvl clear
    #"\"Waaah!\" she protested.{fast}\"Why are you running away!?\""
    #"\"Confined spaces,\"he answered, sliding to a halt in the middle of the roof and setting her down.{fast}\"Speed dial two again.\""
    #nvl clear
    #"\"Right, right,\" he mumbled, reactivating the circle of light."
    #"\"So, what's so great about this if she can just turn it off, anyway?\""
    #"\"It's a barrier and emergency help function,\"he answered, reactivating the beam saber and reassuming a defensive stance."
    #"\"Unless she seals this space off --{w=0.5} again -- {w=0.5}she can't disable it.\""
    #nvl clear
    #"Asakura gave a pained sigh as she stepped through the jagged distortion between her controlled dataspace and the rooftop. "
    #"\"You shouldn't be able to manipulate data like that,\"she said reprovingly."
    #"\"I suppose that means it's time to stop holding back.\""
    #nvl clear
    #"She clapped her hands together before her and drew them apart, flinging a fan of dozens of identical knives outward."
    #"Kyon maintained his guard position, his free hand already clenched into a fist, the metal ridges of his skinsuit facing outward."
    #nvl clear
    #"The knives adjusted their course, most homing in on him to suddenly be halted by a semi-circular barrier of glowing blue force before shattering into nothingness, but a handful stopping suddenly in the space over the circle around Haruhi."
    #nvl clear
    #"He opened his mouth to retort, but Asakura was already within his guard, driving yet another blade into his stomach."
    #"The inner carbon-nano-weave of the greatcoat and the force field of the skinsuit beneath it converted the stabbing force into a distributed shock wave, so instead of being pierced, Kyon was merely hit with the force of a speeding minivan, flying clear across the roof with a choked grunt."
    #nvl clear
    #"\"In the end,\" Asakura remarked, watching his form tumble off the edge of the school building,{fast}\"all those toys are pretty silly if you don't actually know how to use them.\""
    #"\"You have to give him credit, though,\" Haruhi said, peering very closely at the knives frozen over her barrier, not even glancing back to where Kyon had vanished."
    #"\"He comes up with one hell of a distraction ploy, doesn't he?\""
    #nvl clear
    #"The blue-haired interface cocked her head to one side, blinking."
    #stop music fadeout 1
    #"\"What?\""
    #nvl clear
    #play music "SE/lowwind.wav" 
    #"The sensation of being hit with a force that would crush a mid-sized car into a work of modern art was not entirely new, but was without a doubt extremely unpleasant."
    #"His skinsuit did what it could to distribute the kinetic force evenly across his body, so the crushing pain was at least perfectly uniform in infliction."
    #The balancing gizmos gave up the ghost on keeping him upright, and struggled to guarantee he wouldn't land wherever he flew head-first."
    #"His gravity manipulation defenses all strained to bleed the inertia of his impact off without even more pain, but the end result was that he didn't slow appreciably until after he passed the edge of the five story rooftop."
    #nvl clear
    #"Not what he'd hoped for by a long shot."
   # "All of the \"toys\" would keep him mobile, even if he was afraid he'd need to be poured out of the skinsuit when it was over."
   # "He'd have to beg Nagato or Haruhi to help him out and repair things later, but there was just too damn much to keep track of with all the attack vectors, defensive capabilities...."
  #  nvl clear
  #  "\"It started off such a nice day, too,\" he mumbled, as his forward momentum was arrested and he began the downward plummet in earnest."
  #  "How had it come to this, anyway...?"
    #This is where we jump back to the past. For now though, I'll be focused on continuing the fight scene.
  #  "\"Hmm,\"Ryouko mused, turning slowly around, to where her sealed space in the stairway had been breached.{w} \"It was broken from the outside, somehow? I wonder--\""
  #  "The shrill buzz of a brilliant energy beam licked out from the roof of the tiny structure that housed the stairwell."
  #  "Ryouko was struck in the chest dead-center of mass, her entire body glowing white for a second before she staggered-- {w}Instantly another beam shot out from the same location, lighting slightly to one side, near the girl's left shoulder."
 #   "A third, though not as brightly glowing shot was somewhat lower, near her stomach, and Ryouko dropped to her knees, eyes widened."
 #   "\"High yield neutron flare?\" she asked. \"Quantum entanglement to disrupt my connection....\""
    
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
