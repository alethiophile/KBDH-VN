# The prologue. Joy. Also, I do rather love Ren'py's multi-file mechanism.
# Contains some pieces that are technically part of AO-1, but they're semantically right next to the prologue, so...

label prologue:
    stop music
    scene title0 with slowfadein
    
    pause
    play sound "SE/Pageflip3.mp3" 

    nvl clear
    scene bg classroom with fade:
        size (800,600)
    "Class had started innocently enough that day, but he'd long ago given up on expecting {i}that{/i} to mean anything."
    "With each passing moment after lunch, he grew more and more anxious, stealing glances behind him to make certain that she was still there—{w=.4}still safe."
    "And every time their eyes met, she smirked knowingly and quickly looked outside, trying to pretend eye contact was never made."
    "He was absolutely certain that if his sense of anxiety weren't imagined, she was the one behind it — one way or another." 
    "When the fifth period bell rang, he was prepared."    
    nvl clear
    play music "Music/Gouin.mp3" fadein 1
    $ renpy.music.set_volume(0.2, .5, channel="music")
    "In a way, he'd always wanted to do this; exact that one tiny bit of revenge upon her for all the times she'd done it to {i}him{/i}."
    "So when she rose, turned in one smooth motion, and made to bolt out of the room—"
    nvl clear
    "—he was there first, seizing the decorative ties of her sailor uniform's neckerchief and making for the door at top speed." 
    nvl clear
    scene bg hallway with fade:
        size (800,600)
    # Z0: Added the "pulling" of Hauhi
    show Haruhi Sup1 at osl_center
    show Kyon Ser1 at osl_right
    with None
    show Haruhi Sup1 at left
    show Kyon Ser1 at center
    with fast_move
    $ _window = True
    "\"Bwa!\" she protested, arms waving frantically as she dashed to keep up, or risk the knot being pulled out."
    show Haruhi Ang2 at center
    show Kyon Ser1 at right
    with fast_move
    "\"What the hell do you think you're doing!?\""
    $ _window = False
    show Haruhi Sup1 at center with None
    show Haruhi Sup1 at osr_left
    show Kyon Ser1 at osr_center
    with fast_move
    # Z0: end of "pulling"
    scene bg hallway with None:
        xanchor .5 yanchor .5
        xpos .5 ypos .5
        linear .5 rotate 360
    hide Haruhi
    hide Kyon  
    $ renpy.pause(.5, hard=True)
    nvl clear
    scene bg stairwell with fade:
        size (800,600)
    "Naturally, he said nothing to her during the entire mad dash to the remote stairwell where she had first hauled {i}him{/i} by his own tie, so long ago."
    "He released her at the top of the steps after looking around to ensure that no one else was nearby."
    "Her momentum carried her forward, resulting in him pressing one hand flat against her chest, just below her neck."
    # Z0: Added the "stopping after the dash"

    $ _window = True
    show Kyon Ser1 at osl_right
    show Haruhi Ang3 at osl_center
    with None
    show Kyon Ser1 at center
    show Haruhi Ang3 at center_left
    with fast_move
    #show Kyon Ser1: 
    #    xalign -0.25 yalign 1.0
    #    linear 0.25 center
    #show Haruhi Ang3: 
    #    xalign -0.50 yalign 1.0
    #    linear 0.25 center_left
    # Z0: End of "stopping"
    "Her eyes quickly sharpened, her features fixed into a scowl."
    nvl clear
    show Haruhi Ang3 at center_left
    "\"What the hell, Kyon!?\""
    $ _window = True
    show Kyon Ser1 at right with move
    "He held up one hand and said, \"Something's up.\""
    show Haruhi Hap3 at center_left
    "Her irritation vanished instantly, replaced with wide-eyed excitement. She clapped her hands together and hopped from foot to foot."
    show Haruhi Hap4 at center_left
    "\"Yes!\" she cheered. \"It's been so {i}boring{/i} lately!\""
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
    stop music
    extend " \"Take a step back, I don't want to catch you in the interdiction field again.\""
    show Haruhi Hap4 at center_left
    "She nodded and stepped backwards, against the wall."
    $ _window = True
    show Haruhi Hap4:
        xalign 0.1 yalign 1.0
        linear 0.4 xalign 0.0
    $ renpy.pause(0.4, hard=True)
    nvl clear
    play music "music/YukiAsakuraFight.mp3" fadein 1
    # Set this up EVERY time last 'play music' in chapter is started
    $ music_need = False
    # show Kyon Ser2 at right
    # pause 1
    play sound "SE/DunDun.mp3"
    show Kyon Sigh3 at right
    "{w=1.0}Standing perfectly straight, hands at his sides, he closed his eyes, and began speaking in his best faux movie announcer voice-over."
    # Z0: Emulating a "movie-narration. Could be {font=fancyfont.ttf}stuffs{/font} rather than bold, but that would require said fancyfont...
    show Kyon Ser2 at right
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
    # Z0: Needs to add a weapon here. Simple gunmetal cylinder with shine overlay getting thinner and wider from time to time (or just spinning?)
    "Another cylinder, wider but shorter than the last was released to float next to the first."
    "\"Mid- and short-range crowd-control weaponry is at ... ninety seven percent capacity and charging,\" he continued, squinting at the featureless gunmetal tube."
    nvl clear
    play sound "SE/clink.mp3"
    # Z0: Needs to add a sword here. Pull a sword hilt from later chapters, bopping up and down from time to time (or just spinning?)
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
    "\"God damn it, Kyon, you're so cool when you do this,\" Haruhi gushed, clapping her hands together. \"What is it?\""
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
    window hide
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
    $ renpy.pause(1, hard=True)
    hide Bluesword with dissolve
    show Asakura Frown1 at center
    "\"Y...you....\" she began, before she frowned, blinking, staring at the energy weapon."
    nvl clear
    show Asakura Frown1 at left
    show Kyon Ang1 at right
    show Skinsuit at right
    show Coat at right
    with dissolve
    "\"Long time no see,\" he said, switching stance to the long-sword style, Ni-Ten Ichi Ryu."
    show Asakura Frown2 at left
    "\"Um.... Hm. This is different. You've certainly changed, Kyon-kun.\""
    nvl clear
    show Kyon Ser2 at right
    "\"That's funny, Asakura-san, because you haven't.\""
    
    jump AO1_1


label prologue2:
    # Still the part of ch001__AO_1
    $ renpy.music.set_volume(0.2, .5, channel="music")
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
    # Z0: NEEDS a CG of Asakura being hit with beam(s). Current beams do not follow the text.
    # Better yet, "sprite" of a beam. Then show scene black, Asakura in pain (zoomed in some?) at the center and the show beams hitting her at center and slightly lower
    "The shrill buzz of a brilliant energy beam licked out from the roof of the tiny structure that housed the stairwell."
    show Asakura Pain1 at center
    "Ryouko was struck in the chest dead-center of mass, her entire body glowing white for a second before she\nstaggered—"
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Barrier1.mp3"
    scene bg BeamOrange5
    show Asakura Pain2 Bright at center
    with flashbulb
    "Instantly, another beam shot out from the same location, lighting slightly to one side, near the girl's left shoulder."
    nvl clear
    play sound "SE/Laser1.mp3"
    play sound2 "SE/Slash3.mp3"
    scene bg BeamOrange4
    show Asakura Pain2 Bright at center
    with flashbulb
    "A third, though not as brightly glowing shot was somewhat lower, near her stomach, {nw}"
    $ _window = True
    scene bg roofclose
    show Asakura Pain1
    play sound "SE/impact.mp3"
    with dissolve
    extend "and Ryouko dropped to her knees, eyes widened."
    $ _window = False
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
    # make a weapon sprite and show in here, then rotate it behind Kyon's back
    "The end of his weapon was glowing orange with discharge, the shape changed from a simple cylinder to a much thinner meter-long construction of sturdy rails and curving hand guards."
    #  then rotate it behind Kyon's back
    "He slung it over his shoulder and ignored it, pulling the second cylinder from his coat and leaping the twenty meter distance between himself and Ryouko."
    play sound "SE/lowswoosh.mp3"
    # Z0: Let Kyon "leap" on her ^_~
    show Kyon Ser1 at osl_right
    show Skinsuit at osl_right
    show Coat at osl_right
    with fast_move
    scene bg roofclose with wiperightfast
    nvl clear
    show Asakura Unhap1 at center
    pause (0.3)
    play sound "SE/guncock.mp3"
    "Beneath him, a widening circle of dust marked where he leapt from, and while in midair he flipped over, a sequence of touch-points converting the unadorned cylinder into a stocky, blunt, two-handed gun."
    # Maybe replace circles with vertically descending rain of spikes and make net as a cocoon around Ryoko?
    play sound "SE/netlaunch.mp3"
    pause (1)
    play sound "SE/stake1.mp3"
    show Spike1 at spike_net_pos #center
    pause (0.1)
    play sound "SE/stake2.mp3"
    show Spike2 at spike_net_pos #center
    pause (0.1)
    play sound "SE/stake3.mp3"
    show Spike3 at spike_net_pos #center
    pause (0.1)
    play sound "SE/stake1.mp3"
    show Spike4 at spike_net_pos #center
    pause (0.5)
    hide Spike1
    hide Spike2
    hide Spike3
    hide Spike4
    show Spike5 at spike_net_pos #center
    play sound "SE/elec1.mp3"
    "It fired with a rasping cough, launching a ring of metallic spikes to burrow into the rooftop around Ryouko, and then a grid of crackling brissant energy raked between each of the spikes, snaring the girl in a glowing, shuddering net."
    nvl clear
    "\"Ah,\" she said, her voice disappointed as Kyon's repulsor and gravimetric systems flared his momentum and spread it evenly across the entire rooftop, landing him near Haruhi, at Ryouko's side."
    show Asakura Sigh1 at center
    "\"I failed again.\""
    $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    nvl clear
    hide Asakura
    hide Spike5
    scene bg roof
    show Haruhi Ang1 at left
    show Kyon Ser2 at right
    show Skinsuit at right
    show Coat at right  
    "\"Is that going to hurt her?\" Haruhi asked, crossing her arms over her chest and raising an eyebrow at Kyon in concern."
    play music "Music/circulation.ogg"
    nvl clear
    "\"Hurt her?\" he asked, somewhat indignantly."
    show Kyon Ang1 at right
    "\"Haruhi, she's tried to kill me. Three times, now, and you just saw one of them! Your primary concern is that I not hurt her?\""
    show Kyon Sigh1 at right
    play sound "SE/Guncock.mp3"
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
    #stop music fadeout 1
    nvl clear
    scene bg roofclose
    show Asakura Sup1 at center
    show Spike5 at spike_net_pos #center
    "\"What?\" Ryouko asked, still trapped in the containment field. "
    show Asakura Smile3 at center
    extend "\"He just abandoned me here with you?\""
    #play music "Music/NagatoTheme.mp3"
    scene bg roofright
    pause (0.5)
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    with moveinbottom
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
    show Spike5 at spike_net_pos #center
    show Yuki Side1 at HalfLeft with moveinleft
    "While Nagato knelt to examine Ryouko, Haruhi dashed to Kyon's side and helped him stand."
    nvl clear
    $ _window = True
    scene bg roofright
    show Kyon Pain2 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center with moveinleft
    "\"How bad was it, anyway? Future-you seemed to think you weren't very tough, and that you were hurt pretty badly.\""
    $ _window = False
    show Kyon Pain1 at right
    "\"I think I've got some internal bleeding,\" he said, wincing,\none hand pressed to his abdomen. "
    show Kyon Pain2 at right
    extend "\"And some of my gear is messed up from the impact and overload. While this is fun for you, I wouldn't mind some medical assistance.\""
    nvl clear
    show Haruhi Hap3 at center
    "\"Sure!\" she said cheerfully, clapping one hand on his\nshoulder. "
    play sound "SE/impact.mp3"
    show Kyon Pain1 at right
    extend "\"Happy, healing, all-better thoughts!\""
    scene bg roofclose
    show Asakura Sigh1 at center
    show Spike5 at spike_net_pos #center
    show Yuki Talk1 at HalfLeft
    "\"Medical program loaded,\" Nagato added helpfully from\nwhere she was studying the other interface. "
    show Yuki Talk2 at HalfLeft
    extend "\"Permission to proceed?\""
    nvl clear
    scene bg roofright
    show Kyon Pain1 at right
    show Skinsuit at right
    show Coat at right
    show Haruhi Worry1 at center
    "\"Granted.\" Kyon said, {nw}"
    $ _window = True
    play sound "SE/heal1.wav"
    show healfield at right
    show Kyon Ser2 Bright at right
    show Skinsuit Bright at right
    show Coat Bright at right
    with dissolve
    pause .1
    hide healfield at right
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    with dissolve
    $ _window = False
    extend "straightening up as a sparkle of green and white lights suffused up from the rooftop beneath him, flowing through his body and undoing the damage."
    nvl clear
    show Kyon Smile1 at right
    "\"Oh, that feels so much better! Thank you; that probably saved my life."
    show Kyon Neutral2 at right
    "\"And for future reference, you can probably assume that I'm okay with that one being used.\""
    "\"Acknowledged,\" Nagato agreed."
    nvl clear
    $ _window = True
    show Haruhi Smile2 at left with move
    "\"Hmm, hey, Kyon, you know, you're going to have to really step up your game,\" Haruhi said suddenly, tossing his cell phone back to him."
    show Kyon Ser1 at right
    play sound "SE/woosh.mp3"
    hide Skinsuit with wipedown
    play sound "SE/CloakOn.mp3"
    hide Coat with coatout
    $ _window = False
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
    show Spike5 at spike_net_pos #center
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
    nvl clear
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
    show Spike5 at spike_net_pos #center
    show Yuki Side1 at HalfLeft
    "Nagato stared intently at Ryouko, then gave a decisive nod. "
    show Yuki Talk1 at HalfLeft
    extend "\"Awaiting program,\" she announced."
    nvl clear
    stop music fadeout 3
    $ _window = True
    show Haruhi Ang3 at left with moveinleft
    show Kyon Ser1 at right with moveinright
    show Yuki Side1
    $ _window = False
    "\"Hmm,\" Haruhi mused, narrowing her eyes and peering intently at Ryouko, who merely watched back curiously."
    show Haruhi Ang2 at left
    play music "Music/Oi.mp3"
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
    #show Asakura Frown3 at center
    #pause (0.4)
    #show Asakura Frown1 at center
    show Asakura Blink1 at center
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
    nvl clear
    scene black with dissolve
    $ renpy.pause(.2, hard=True)
    show BDVNlogo at truecenter with Dissolve(2.0)
    pause 5
    # Approx. 21 minutes of reading at this point.
    jump AO1_2
