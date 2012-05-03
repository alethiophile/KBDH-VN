# Anachronic order explanation arc, 1.

label AO1_1:
    # Obligatory Anachronic Order Explanation Arc chapter 1 - "Scene Twelve, the Ninth Big Fight"
    
    # Preparations for Chapter: Replicate the last scene from previous chapter (if it is continued), or show a chapter quote card
    $ _window = True
    nvl clear
    if music_need:
        scene bg stairwell with None:
            size (800,600)
        $ renpy.music.set_volume(0.2, .5, channel="music")
        # copy last 'play music' from the previous chapter (if scene is continued) or start apropriate chapter music
        play music "music/YukiAsakuraFight.mp3" fadein 1
    #Preparation for Chapter end
        show Kyon Ser2 at right
        show Skinsuit at right
        show Coat at right
        with dissolve
    hide Asakura
    show Haruhi Hap3 at left
    "Haruhi bounced on her heels with a wide grin, holding Kyon's cell phone in both hands as she remained in the center of the glowing circle."
    show Haruhi Hap4 at left
    "{=loud}\"I {i}knew{/i} it!\"{/=loud} she cheered.{nw} "
    show Haruhi Hap1 at left
    extend "\"There was {i}something{/i} off about Asakura! What is it?\""
    nvl clear
    hide Kyon
    hide Coat
    hide Skinsuit
    hide Haruhi
    show Asakura Unhap1 at center
    with dissolve
    "\"Um...\" the onetime class representative said, frowning."
    hide Asakura
    show Haruhi Hap1 at left # Z0: to keep scene consistent
    show Kyon Sigh2 at right
    show Skinsuit at right
    show Coat at right
    with dissolve
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
    with dissolve
    # No crossed-arm Asakura sprite = changing the text to not require that.
    # "\"Er,\" Asakura said, crossing her arms beneath her chest."
    "\"Er,\" Asakura said with a slight frown. "
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
    with dissolve
    "\"Blah blah blah,\" Haruhi muttered, crossing her arms over her chest and rolling her eyes."
    show Haruhi Ang1 at left
    "\"Skip the speeches — if I don't know the complete back story, it's all meaningless to me. I think it's about time we get down to business, right?\""
    nvl clear
    hide Haruhi
    window hide
    with dissolve
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
    "Kyon spun on one foot, crying out with a great {=shout}\"Ki-yah!\"{/=shout} {p=1}{nw}"
    play sound "SE/lowswoosh.mp3"
    pause (0.2)
    play sound "SE/impact.mp3"
    #with vpunch
    with sshake
    pause (0.2)
    play sound "SE/glassbreak1.mp3"
    #with hpunch
    # extend and kicking the door halfway across the roof."
    $ nvl_erase()
    "Kyon spun on one foot, crying out with a great \"Ki-yah!\"{fast} and kicking the door halfway across the roof."
    show Haruhi Sup1 at left
    pause (.01)
    show Kyon Ser1 at left behind Haruhi
    show Skinsuit at left behind Haruhi
    show Coat at left behind Haruhi
    with moveinright
    pause (0.5)
    show Kyon Ser1 at osl_left 
    show Skinsuit at osl_left
    show Coat at osl_left
    show Haruhi Sup1 at osl_left
    with moveoutleft
    hide Kyon
    hide Haruhi
    hide Skinsuit
    hide Coat
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
    $ _window = True
    nvl clear
    show Haruhi Pout1 at left
    pause .4
    play sound "SE/Barrier1.mp3"
    show Haruhi Pout1 Bright at left
    show field at left with dissolve
    pause .1
    hide field at left with dissolve
    show Haruhi Pout1 at left with dissolve
    $ _window = False
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
    show Stabby with fastdissolve:
        size (800, 600)
    hide Stabby with fastdissolve    
    
    $ _window = True
    show Asakura Smile3
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
    play sound "SE/touhoudead.mp3"
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
    "\"In the end,\" Asakura remarked, watching his form tumble off the edge of the school building, \"all those toys are pretty silly if you don't actually know how to use them.\""
    show Haruhi Hap1 at left
    "\"You have to give him credit, though,\" Haruhi said, peering very closely at the knives frozen over her barrier, not even glancing back to where Kyon had vanished."
    show Haruhi Grin1 at left
    "\"He comes up with one hell of a distraction ploy, doesn't he?\""
    nvl clear
    show Asakura Sup1 at HalfRight
    "The blue-haired interface cocked her head to one side, blinking."
    "\"What?\""
    nvl clear
    stop music
    hide Haruhi
    hide Asakura
    $ _window = False
    scene bg daysky with fade
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
    stop music
    nvl clear
    # scene title1 with slowfadein
    scene black 
    show title 001 at card_pos 
    with slowfadein
    
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    play music "Music/Nichijou.mp3"
    $ renpy.music.set_volume(0.5, .5, channel="music")
    scene bg KyonKitchenRight with fade
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
    "\"Answer it for me,\" he called back between gulps. \"I'm busy.\""
    nvl clear
    "\"Okaaaaaay,\" she said, before he heard her say, \"Kyon-kun's phone! He's too lazy to answer!\""
    "\"Thanks,\" he muttered under his breath."
    "\"Oh? Okay! I'll tell him. Feel better!\" Then her voice rose from conversational, to an unnecessary bellow, {=loud}\"Kyon-kun! Yuki-nee-san says she's sick and really wants you to visit her!\"{/=loud}"
    nvl clear
    "He didn't even bother to grab the phone on the way out."
    "\"Can I come with...\" {nw}"
    play sound "SE/doorclose.mp3"
    stop music
    scene bg KyonHouseDay
    extend "she began, before the door slammed shut. Shrugging, she turned back to the game after flipping Kyon's phone closed."
    nvl clear
    # stop music fadeout 1
    play music "Music/Nagato2.mp3"
    "He calculated the ride to Nagato's place as a twenty minute trip, at one point."
    scene bg TownStreetDay1 with wiperight
    pause 1
    scene bg TownStreetDay2 with wiperight
    pause 1
    scene bg YukiApartmentDay with wiperight:
    "When he reached the lobby, barely pausing long enough to lock up his bike, he wondered if he'd beaten his best time, but didn't feel the need to check."
    "Instead, he dashed to the console, still gasping for breath, and fumbled, mis-dialing her room number and needing to hammer the 'cancel' button to dial again."
    "{=loud}\"Nagato!\"{/=loud} he called, the second she picked up. {=loud}\"It's me!\"{/=loud}"
    nvl clear
    "The door opened."
    scene bg YukiRoomCenter with wipeup
    "After taking the elevator to her floor, he slowed his mad pace, seeing her standing outside the doorway to her apartment, waiting for him."
    nvl clear
    show Yuki Side1 at TenthLeft
    "He tried to imagine that he saw some relief around her eyes when he reached her side, but wasn't confident enough to be certain that was the case."
    show Kyon Casual Ser1 at right
    "\"Nagato,\" he said, nodding. \"What's wrong?\""
    nvl clear
    show Yuki Side2
    "She gestured him inside, leading him to the table."
    "He kicked off his shoes and went to the kotatsu, watching her warily."
    "After pouring a cup of tea for each of them in silence, she finally spoke."
    nvl clear
    show Yuki Talk1
    "\"The Integrated Data Sentience Entity has determined that I have become a liability,\" she said in a soft monotone, nearly devoid of inflection."
    show Kyon Casual Sup1 at right
    nvl clear
    "He stared at her for a long minute, blinking. \"What ... do you mean?\""
    show Kyon Casual Sup2 at right
    show Yuki Talk2
    "\"Factors within my makeup have become too unpredictable. It has been calculated that I will commit another error."
    show Yuki Talk1
    "\"To prevent this, deletion has been scheduled in three hours, twenty one minutes, fifteen seconds; I will be replaced with an interface more suited to defending against possible Sky Canopy Domain interference.\""
    nvl clear
    show Kyon Casual Sigh1 at right
    show Yuki Side1
    "After taking a deep breath, he growled, \"There isn't enough milk in the world.\""
    show Yuki Side Blink
    "She blinked several times in response."
    show Kyon Casual Worry2 at right
    "\"How set is this?\" he asked, his hands shaking too much to hold the teacup properly."
    show Yuki Talk2
    "\"It is absolute.\""
    nvl clear
    show Yuki Side1
    show Kyon Casual Sigh1 at right
    "He took another deep breath, then jumped to his feet, nearly upsetting the table, and began pacing back and forth in her living room."
    show Yuki Side2
    "She watched him silently."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"Okay,\" he said, after a moment of thought. \"I'll just—\""
    show Kyon Casual Ser1 at right
    "He broke off, fumbling at his pocket when he realized his phone was still at home."
    show Kyon Casual Worry2 at right
    "Biting off a curse, he asked, \"Can I use your phone, Nagato? I need to call Haruhi and the others.\""
    nvl clear
    show Yuki SideDisappointedTalk1
    "For a moment, mild disappointment flickered around her eyes. \"It is not necessary.\""
    show Yuki Side1
    show Kyon Casual Ser1 at right
    "He stared at her, then shook his head. \"What do you mean?\""
    show Yuki Talk1
    "\"I requested your presence for ... personal reasons,\" she said. \"It was not a request for help.\""
    nvl clear
    show Kyon Casual Ang1 at right
    show Yuki Side1
    "{=shout}\"I don't care!\"{/=shout} he shouted."
    "\"I've always relied on you — now that you need help, I am {i}not{/i} going to just stand by and watch you get taken away from— from us!\""
    show Yuki Side Blink
    "She blinked, considering, then lowered her head slightly in her infinitesimal nod."
    nvl clear
    show Yuki Talk1
    "\"I see,\" she said quietly."
    show Kyon Casual Sigh1 at right
    show Yuki Side1
    "\"So, I need to make some phone calls.\""
    show Yuki Talk2
    "\"Understood.\""
    stop music fadeout 3
    nvl clear
    
    # Calling a generic "eyecatch" routine, with unique "from"
    call eyecatch("Sunday, April 17") from AO1_sc001
    
    scene bg YukiApartmentDay with fade
    play music "Music/Kankyou.mp3"
    "She couldn't imagine what had possessed Kyon to call her, ranting like a lunatic about Yuki being sick. "
    "But he'd done it from {i}her{/i} phone, which meant for whatever reason that he and Yuki were alone together. "
    "She wasn't certain why that bothered her, but it did — so when he demanded her presence, instead of telling him what he could do for trying to order the Brigade leader around, she swore that she'd be there."
    nvl clear
    scene bg YukiRoomCenter with wipeup
    $ _window = True
    "After trekking all the way there, much to her annoyance, she found that she was the last to arrive."
    show Mikuru Cower Casual Nervous1 at left
    show Koizumi Crossed Casual Uneasy1 at center
    show Yuki Side1 at right
    with dissolve
    $ _window = False
    "Mikuru sat at one side of the table, opposite Yuki."
    "Koizumi sat between them, his eternal smile faded to half its normal strength."
    scene bg YukiRoomRight
    show Kyon Casual Ser1 at right
    show Yuki Side2 at left
    with dissolve
    "Kyon himself stood next to her — he was the one who had answered the intercom and let her in."
    nvl clear
    show Haruhi Crossed Casual Eyeroll1 at HalfLeft with moveinright
    "She narrowed her eyes at him and kicked her shoes off, storming into the room to Yuki's side and immediately pressing one palm onto the smaller girl's forehead."
    show Haruhi Crossed Casual Sigh1 at HalfLeft
    "\"You don't feel feverish,\" she finally commented."
    show Haruhi Crossed Casual Worry1 at HalfLeft
    "\"But if you're sick, you shouldn't be up and about anyway.\""
    nvl clear
    show Yuki Talk1 at left
    "\"Not sick,\" Yuki answered."
    show Haruhi Casual Ang3 at HalfLeft
    "When Haruhi turned to Kyon and scowled at him, she corrected, \"Dying.\""
    nvl clear
    show Yuki Side1 at left
    show Haruhi Casual Sup1 at HalfLeft
    "Her irritation at Kyon's practical joke momentarily blew away, like settled dust being disturbed."
    show Haruhi Crossed Casual Sup2 at HalfLeft
    "{=loud}\"Dying!?\"{/=loud} she yelped, turning to stare at the smaller girl."
    "\"What of? {i}How?{/i}\""
    show Yuki Talk1 at left
    "Yuki blinked twice, then answered, \"I am not able to say.\""
    nvl clear
    scene bg YukiRoomCenter
    show Mikuru Cower Casual Nervous1 at left 
    show Koizumi Crossed Casual Uneasy1 at center
    show Haruhi Crossed Casual Quest1 at right
    with dissolve
    "\"Mikuru?\""
    show Mikuru Cower Casual Nervous2 at left 
    "\"Um ... classified.\""
    nvl clear
    show Haruhi Crossed Casual Ang3 at right
    "She scowled at Koizumi, daring him to be a defiant annoyance, too."
    show Koizumi Crossed Casual Uneasy2 at center
    "\"I don't know,\" he said, looking embarrassed and flustered."
    nvl clear
    scene bg YukiRoomRight
    show Haruhi Casual Ang3 at TenthLeft
    show Kyon Casual Ser1 at right
    with dissolve
    "Turning around, she glared at Kyon, letting her irritation return and focus on him full-force."
    show Haruhi Casual Ang2
    "{=loud}\"I am not in the mood for pranks!\"{/=loud} she snapped."
    "\"This better not be a joke!\""
    nvl clear
    show Kyon Casual Ang1 at right
    "\"I wish it was,\" he said back crossly, and she found herself taken aback at the force in his tone."
    scene black with dissolve
    nvl clear
    "She had a mental catalogue of Kyon-like behaviors, and this fell firmly into the category of the seldom-seen, but always feared {i}angry{/i} Kyon."
    "Dour, upset, irked, sarcastic, caustic ... sure. But angry?"
    "Hell, she'd once smashed his head into her desk — entirely on accident — and he was only {i}annoyed{/i}. And it wasn't for hitting his head, it was for disrupting a class!"
    "Nevermind that he had been dozing off before that."
    nvl clear
    "She'd seen him genuinely angry two times."
    "Only once had it been at her."
    "She hated that memory more than anything else she knew about him, but couldn't dare to forget it."
    "Once it had been at — of all things — his unfinished homework over summer break, though that was the lesser of the two displays; also the first."
    "She didn't understand it, but she knew whatever it was, she wanted to be on his side against it."
    "Even then, some small part of her really didn't like the way that when he chose to, he simply seized command of her precious hand-crafted Brigade and, no matter how cute it\nwas—"
    "She firmly suplexed that thought into oblivion."
    nvl clear
    scene bg YukiRoomRight
    show Kyon Casual Ser1 at right
    show Haruhi Casual Quest1 at TenthLeft
    with dissolve
    "\"Alright,\" she said evenly. \"Tell me what's going on.\""
    show Kyon Casual Worry1 at right
    "Kyon ran his hands through his hair and began pacing, not looking at her."
    show Haruhi Casual Sigh1
    "Good; she wasn't the one who had made him mad."
    nvl clear
    show Kyon Casual Sigh1 at right
    "\"Have a seat,\" he said."
    "\"This may take a bit, and I need a promise from you before we start.\""
    $ _window = True
    show Haruhi Casual Ang1 at left with move
    $ _window = False
    "\"I'm not making a blind promise,\" she retorted, though she did take the seat opposite Koizumi, between Mikuru and Yuki."
    nvl clear
    "Yuki wordlessly poured her a cup of tea, which she threw back in a single gulp."
    show Kyon Casual Ser1 at right
    "\"I need you to promise to listen to everything we have to say before leaving,\" he answered."
    nvl clear
    show Haruhi Casual Pout1 at left
    "\"That's stupid,\" she grumbled."
    show Haruhi Casual Ang2 at left
    "\"If Yuki's in danger, what kind of person do you take me for?\""
    "She wasn't {i}that{/i} bad about ignoring the needs of her brigade members."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"Even so.\""
    show Haruhi Casual Sigh1 at left
    "\"Fine,\" she sighed. \"I promise. Now can you get on with it?\""
    nvl clear
    show Kyon Casual Ser1 at right
    "\"Okay,\" he said, pacing around to the window."
    show Kyon Casual Ser3 at right
    "\"Almost a year ago — last May — we ended up going on a city search where no one but you and I showed up.\""
    show Haruhi Casual Eyeroll1 at left
    "\"I remember,\" she said, annoyed."
    "A stupid practical joke on his part ... though, it had given her the idea for the movie."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"I told you that aliens, espers, and time travelers really existed, right?\""
    show Haruhi Casual Ang3 at left
    "\"We're going back to that?\" she asked, raising an eyebrow. \"Really?\""
    show Kyon Casual Sigh2 at right
    "\"Yeah, okay, you remember it, so I don't need to say it again,\" he said with a shrug."
    nvl clear
    show Kyon Casual Ser3 at right
    "\"Koizumi, you promised that if it had to happen, you'd stand next to me when Yuki needed our help. Remember?\""
    scene bg YukiRoomCenter
    show Koizumi Crossed Casual Ser1 at left
    show Haruhi Crossed Casual Ang3 at right
    with dissolve
    "\"Yes,\" the smiling boy said, though his smile had completely vanished. "
    show Koizumi Crossed Casual Ser2
    "\"As much as it scares me.... Suzumiya-san, Kyon-kun is speaking the truth.\""
    show Haruhi Crossed Casual Ang2
    "\"You're an esper?\" she asked him doubtfully."
    nvl clear
    scene black with dissolve
    "He gave a solemn nod, and she internalized a sigh."
    "What, was Kyon just acting?"
    "Was this is unsubtle way of saying he wanted to be a star in the next movie, not just a camera man?"
    "She had to admit, his emotion seemed genuine, but why couldn't he just have asked her? "
    "There was an awful lot he could have just asked for, and never bothered to!"
    "That thought was drop-kicked to fly off next to the last banished thought."
    nvl clear
    scene bg YukiRoomCenter 
    show Haruhi Crossed Casual Grin1 at center
    show Mikuru Cower Casual Nervous1 at left
    with dissolve
    "\"And, Mikuru, you're a time traveler?\" she asked, idly spinning her teacup on the table before her."
    show Mikuru Cower Casual Nervous2
    "\"Um ... that is ... I can't....\""
    show Kyon Casual Ser3 at right 
    "\"Asahina-san,\" Kyon broke in suddenly, \"please ask your supervisor to declassify this for me.\""
    nvl clear
    "Mikuru stared at Kyon, her eyes large and confused."
    show Mikuru Cower Casual Nervous1 at left
    "\"Y...yes,\" she agreed, her glance flickering nervously to Haruhi before she pressed a hand against the side of her face, and her eyes became unfocused."
    show Mikuru Cower Casual Sup1 at left
    nvl clear
    "They abruptly snapped back into focus, though her expression had become comically bewildered \"I ... they said yes!? I don't understand! Kyon-kun, how—\""
    show Kyon Casual Worry1 at right
    "\"That's ... classified,\" he answered, looking away."
    show Kyon Casual Ser1 at right
    "\"Anyway, go ahead and explain it to Haruhi.\""
    nvl clear
    show Mikuru Cower Casual Neutral1 at left
    "\"Oh! Um, Suzumiya-san ... what he says is true! I am a time traveler, though, it's more accurate to say that I'm a visitor from the future who is projected into the past, almost like a two-dimensional image projected into—\""
    show Haruhi Crossed Casual Eyeroll1 at center
    "\"Right, right,\" Haruhi cut her off. \"You're a time traveler. Understood.\""
    nvl clear
    scene black with dissolve
    "Though, Mikuru's acting skills had picked up quite a bit, too...."
    "This better not be a ploy to make Kyon the male lead opposite Mikuru in the next movie!"
    "Saving that thought for later, she turned her gaze to Yuki."
    nvl clear
    scene bg YukiRoomLeft
    show Yuki Side1 at left
    show Haruhi Crossed Casual Quest1 at center
    show Kyon Casual Ser1 at right
    with dissolve
    "\"And you're an alien?\""
    show Yuki Talk1 at left
    "\"The function allowing me to confirm or deny that data has been denied at this juncture in time,\" she answered."
    show Yuki Talk2 at left
    "Turning to Kyon, she added, \"One hour and twenty minutes remain.\""
    nvl clear
    show Kyon Casual Worry2 at right
    "He bit off a curse, running his hands through his hair."
    $ _window = True
    scene bg YukiRoomCenter
    show Kyon Casual Ser1 at right
    show Haruhi Casual Worry1 at TenthLeft
    with dissolve
    $ _window = False
    "Haruhi was taken aback again ... he obviously didn't like getting bad grades or doing poorly on exams, but he almost never got {i}this{/i} stressed about things. "
    "This was starting to become unnerving."
    nvl clear
    show Haruhi Casual Sigh1
    "\"Okay,\" she said, before he could speak."
    show Haruhi Casual Eyeroll1
    "\"Look, this has gone far enough. I get it, alright? Your practical joke ... okay. Fine.\""
    nvl clear
    show Haruhi Casual Ang3
    "\"What are you really after? Producer? Co-director? You want to help write the script for the next movie?"
    show Haruhi Casual Ang2
    "\"Let's just cut to the chase — this isn't really fun, especially since it's at my expense!\""
    nvl clear
    stop music fadeout 3
    show Kyon Casual Ang1 at right
    "{=loud}\"At {i}your{/i} expense—\"{/=loud}"
    show Haruhi Casual Sup1
    "That had done it, she realized, flinching back."
    show Kyon Casual Sigh1 at right
    show Haruhi Casual Worry1
    "Now some of his anger was directed at her, though he quickly controlled it, smacking one palm against his face."
    play music "Music/Ready.mp3"
    show Kyon Casual Ser1 at right
    nvl clear
    "\"Last May,\" he said, \"you came to class with your hair in a ponytail.\""
    show Haruhi Casual Pout1
    show Hblush Casual at TenthLeft
    "She suddenly couldn't meet his eyes, and a previously suplexed thought began to climb back into her awareness."
    nvl clear
    show Haruhi Casual Ang2
    "\"It was hot!\" she said defensively. \"What of it?\""
    show Kyon Casual Ser3 at right
    "\"You had a dream — a nightmare — that night,\" he added."
    show Haruhi Casual Ang1
    "\"So?\""
    nvl clear
    show Haruhi Casual Sigh1
    "She forced her heartbeat to still. "
    "She'd {i}told{/i} him that much, why wouldn't he remember?"
    "She did, after all, even now."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"So, in your dream, you watched giant blue creatures smash apart the school, and you were very excited about abandoning the Brigade — your friends — and leading an exciting new life in whatever world was to come.\""
    nvl clear
    scene bg YukiRoomCenter with dissolve
    show Koizumi Crossed Casual Uneasy1 at center
    show Mikuru Cower Casual Nervous1 at right
    show MBlush Cower at right
    show Yuki Side1 at left
    with dissolve
    "Koizumi looked uncomfortable. Mikuru's face turned red, and she began studying the bottom of her teacup intently."
    "Yuki merely stared at her, unblinking."
    nvl clear
    scene bg YukiRoomCenter
    show Haruhi Casual Pout1 at TenthLeft
    show Kyon Casual Ser1 at right
    with dissolve
    "\"I never told anyone that,\" she mumbled."
    show Kyon Casual Ser2 at right
    "\"In the end, I told you that I wanted to come back to {i}this{/i} world,\" Kyon said."
    show Kyon Casual Ser3 at right
    "\"That it was more interesting than you realized. {nw}"
    show Kyon Casual Ser2 at right
    extend "Do I have to say what I did to wake you up?\""
    nvl clear
    show Hblush Casual at TenthLeft
    "She felt her face color."
    show Haruhi Casual Quest1
    "\"N...no,\" she managed. \"Who— No, {i}what{/i} are you?\""
    show Kyon Casual Sigh2 at right
    "\"I am a normal person,\" he told her, shrugging."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"I happen to have traveled to parallel worlds. I have traveled through time. I've seen some amazing things ... but through it all, I always come back {i}here{/i} to be with my friends.\""
    nvl clear
    scene black with dissolve
    "It was getting very strange, and she didn't know why, but the conversation was starting to make her uncomfortable."
    "Maybe the knowledge of her dream was just an expert analysis based on her personality? The refusal to mention the kiss specifically was because they didn't {i}know{/i}?"
    "But she wasn't certain she wanted to hear him say it {i}was{/i} a kiss, here, right now...."
    "And she'd promised she would listen."
    nvl clear
    scene bg YukiRoomCenter
    show Haruhi Casual Quest1 at TenthLeft
    show Kyon Casual Ser1 at right
    with dissolve
    "\"You're claiming that you're a slider?\" she asked, blinking, buying herself some time to think."
    show Kyon Casual Sup2 at right
    show Ksweat at right
    "He was momentarily startled by the question, then exchanged a glance with Koizumi, who shrugged. "
    $ _window = True
    hide Haruhi
    hide Kyon
    with dissolve
    show Koizumi Crossed Casual Smile1 at center
    with dissolve
    nvl clear
    $ _window = False
    "\"Actually, Kyon-kun, you may be,\" the supposed esper said, smiling."
    show Koizumi Crossed Casual Smile2 at center
    "\"That would explain why one never seemed to appear; it was you!\""
    nvl clear
    $ _window = True
    hide Koizumi
    with dissolve
    show Kyon Casual Sigh1 at right
    show Haruhi Casual Worry1 at TenthLeft
    with dissolve
    $ _window = False
    "\"Nevermind that!\" he said quickly, shaking his head."
    show Kyon Casual Ser3 at right
    "\"Haruhi, there's something I have to tell you, something I think will make you believe me.\""
    show Haruhi Casual Quest1
    "\"What's that?\" She couldn't think of anything else to say or ask."
    nvl clear
    show Kyon Casual Ser1 at right
    "\"Tanabata last year was the first time I traveled back in time,\" he began, his expression solemn."
    show Kyon Casual Ser3 at right
    "\"I went to a night three years earlier. That would be Tanabata four years ago."
    show Kyon Casual Ser1 at right
    "\"While I was there, I was sent to East Middle school, carrying Asahina-san on my back.\""
    nvl clear
    show Haruhi Casual Sup2
    "\"Y...you're...\" she gasped, her eyes widening as the world around her spun, the amazing, simultaneously horrifying and delightful realization that he was speaking the truth was making her dizzy."
    nvl clear
    show Kyon Casual Ser2 at right
    "\"And I met a younger version of yourself, and wrote the message, 'I am here' on the school grounds, following your instructions. You asked who I was, and I told you that I went by ..."
    nvl clear
    show Kyon Casual Ser1 at right
    "\"John Smith.\""
    nvl clear
    show Haruhi Casual Sup3
    "{=loud}\"{i}You're{/i} John Smith!\"{/=loud}"
    $ _window = True
    # show Haruhi Casual Hap3 at HalfRight with MoveTransition(.2) 
    show Haruhi Casual Hap3
    show Haruhi Casual Hap3 at HalfRight with fast_move
    pause(0.0)
    show Kyon Casual Ser1 at osr_center
    show Haruhi Casual Hap3 at osr_center 
    with fast_move 
    play sound "SE/impact.mp3" 
    show Haruhi Casual Hap3 at osr_center with sshake
    "She wasn't aware of getting up from the table, uncertain if she had moved around or just jumped over it — she just knew that she had flung herself at him, tackling him to the floor and grabbing on tightly."
    "{=shout}\"I {i}knew{/i} it!\"{/=shout} she yelled."
    nvl clear
    $ _window = False
    scene black with dissolve
    stop music fadeout 5
    "{=loud}\"I {i}knew{/i} I'd find you again!\"{=loud}"
    nvl clear
    
    # Calling a generic "eyecatch" routine
    call eyecatch2("Sunday, April 17", "Thursday, June 2") from AO1_sc002
    
    jump prologue2


label AO1_2:
    nvl clear
    play music "Music/Morning.ogg"
    scene bg KyonRoomLeftClosed:
        size (800,600)
    with fade   
    "Kyon hadn't had time to think about things before." 
    "Part of that was from a certainty that if he had let himself think about things, it could easily become too late to do anything."
    "Part of it was his desire to make sure he could find his way back to his own world."
    "But most of it was the fact that he could deal with the world going away, as long as he could keep the Brigade intact, regardless of his position in it."
    nvl clear
    scene bg KyonRoomLeftMorning with dissolve
    "Though, that thought in mind, when he awoke, he stared out the window after rising before his younger sister yet again."
    "This habit was probably going to wear him out, he thought."
    "Still, by the time he had finished washing up, just in time to watch her prance out of her room, he couldn't help but smile. "
    "Her face fell when she realized that the era of deadly wake-up elbow-slams was probably at an end."
    "He busied himself making breakfast while mulling over the likely consequences of his impulsive decision." 
    "And there would be consequences, he had no doubts of that at all."
    nvl clear
    "Serving his curious sister a piece of toast with a fried egg on it, he set about preparing one for himself." 
    nvl clear
    stop music fadeout 2
    $ _window = True
    scene black  with dissolve
    "Now Haruhi, as she understood it, believed that she could change reality...."
    $ _window = False
    nvl clear
    # scene black with dissolve
    # $ renpy.pause(.2, hard=True)
    # show BDVNlogo at truecenter with Dissolve(2.0)
    # pause 5
    
    # Calling a generic "eyecatch" routine, with unique "from"
    call eyecatch2("Monday, April 18", "Sunday, April 17") from AO1_sc003

    play music "Music/GnossiennesDai3.mp3"
    scene bg YukiRoomCenter
    show Haruhi Casual Unhap1 at left
    show Htears Casual at left
    with fade
    "\"But you're saying, I have a {i}power{/i} I don't even know about?\" Haruhi asked, now pacing anxiously back and forth."
    show Haruhi Casual Unhap2 at left
    "\"Why would you have kept this a secret from me?! Even more than the fact that you're the people I've been looking for, the fact that I can do things!\""
    show Haruhi Casual Unhap1 at left
    "She looked on the verge of tears and laughter at the same time."
    nvl clear
    hide Haruhi
    hide Htears
    show Koizumi Crossed Casual Ser1 at center
    with dissolve
    "\"That was the decision of my superiors,\" Koizumi offered, frowning."
    show Koizumi Crossed Casual Ser2 at center
    "\"It was believed that ... there could be unfortunate consequences.\""
    nvl clear
    hide Koizumi
    show Mikuru Cower Casual Nervous1 at center
    with dissolve
    "\"And you,\" she continued, peering at Mikuru, \"also followed your instructions?\""
    show Mikuru Cower Casual Nervous2 at center
    "\"U...um,\" Mikuru said, shrinking into herself slightly."
    show Mikuru Cower Casual Nervous3 at center
    "\"I...it's not a matter of choice for me ... literally, I can't talk about classified information when it's classified. If I try to, then classified info...\""
    show Mikuru Cower Casual Sigh1 at center
    "She hung her head with a weary sigh. \"Sorry.\""
    nvl clear
    hide Mikuru 
    show Yuki Side1
    with dissolve
    "\"And you?\" she pressed, turning her gaze to Yuki, who sat at the table, staring at the teacups."
    show Yuki Talk1
    "\"Focus is on preventing my imminent deletion,\" the interface finally answered. \"Limited resources.\""
    nvl clear
    hide Yuki
    show Haruhi Casual Unhap2 at left
    show Kyon Casual Ser1 at right
    show Htears Casual at left
    with dissolve
    "\"So, all along, the lowliest ranking member of the SOS Brigade is the only one who ever actually tried to tell me the truth,\" Haruhi grumbled."
    show Kyon Casual Sigh1 at right
    "\"That aside,\" Kyon said, shifting his shoulders, \"we can talk about this later. I'm sorry, but I'm really worried about Nagato. Since you believe us, or at least, I think you do...\""
    nvl clear
    show Haruhi Casual Unhap1 at left
    "\"I don't,\" she countered. \"I believe {i}you{/i}. Because you {i}tried{/i}. But....\" She trailed off and shrugged, gesturing to the other three."
    show Haruhi Casual Ang4 at left
    "\"The people who wormed their way into my good graces were working against me! How can I trust them?\""
    hide Haruhi
    hide Kyon
    hide Htears
    nvl clear
    show Mikuru Cower Casual Wince1 at right
    show MTears Casual at right
    show Koizumi Crossed Casual Uneasy3 at center
    show Yuki Side1 at left
    with dissolve
    "Mikuru said nothing, just sniffling as tears trickled down her cheeks."
    "Koizumi's eternal smile had withered to a pained shadow of its normal impenetrability." 
    "Yuki continued staring at her."
    nvl clear
    hide Mikuru
    hide MTears
    hide Koizumi
    hide Yuki
    show Kyon Casual Ser3 at right
    show Haruhi Casual Unhap2 at left
    with dissolve
    "\"Because I do,\" Kyon said, breaking the uncomfortable silence."
    nvl clear
    scene bg MemoryYuki with fade
    "\"I don't know if we can believe everything, but I know that Nagato is a humanoid interface.\"" 
    nvl clear
    scene bg MemoryMikuru with dissolve
    "\"I've traveled through time with Asahina-san.\""
    nvl clear
    scene bg MemoryKoizumi with dissolve
    "\"Koizumi's shown me the places where he and the other espers of his kind fight....\""
    scene bg YukiRoomCenter
    show Kyon Casual Ser2 at right
    show Haruhi Casual Unhap2 at left
    with fade
    nvl clear
    "\"And in every case, all three of them couldn't tell you because their bosses {i}told{/i} them not to.\""
    nvl clear
    show Haruhi Casual Ang4 at left
    "\"What about {i}your{/i} boss,\" she snapped, turning to eye Kyon with suspicion. \"What does that person say?\""
    show Kyon Casual Sigh1 at right
    "\"Right now she's asking me if she has any reason to trust her closest friends,\" he answered."
    show Kyon Casual Worry1 at right
    "\"And I'm begging her to, because that may be the only way to save Nagato's life.\""
    nvl clear
    show Haruhi Casual Eyeroll1 at left
    "\"I.... I'm your boss?\" she asked, narrowing her eyes in suspicion. \"You don't work for anyone else?\""
    show Kyon Casual Ser1 at right
    "\"Thankfully,\" he agreed, nodding. "
    nvl clear
    show Kyon Casual Sigh2 at right
    "\"I suppose I have done things for Asahina-san and her superiors."
    show Kyon Casual Sigh1 at right
    "\"I know my actions have benefited Koizumi's Organization."
    show Kyon Casual Ser3 at right
    "\"But I've only ever done things because I felt it was important for you, or for the sake of the entire world.\""
    nvl clear
    show Haruhi Casual Worry1 at left
    "\"The entire world?\" she pressed, struggling to contain all the new information. \"You've saved the world?\""
    show Kyon Casual Sigh1 at right
    "\"Technically, {i}you{/i} did,\" he said, shaking his head. \"I just convinced you to do it ... but we already went over that.\""
    nvl clear
    show Haruhi Casual Quest1 at left
    "\"So you're some kind of undercover hero without any of his own special abilities that fights to take care of me, and to save the world?\" she asked."
    hide Haruhi
    hide Kyon
    show Yuki Side1 at left
    show Mikuru Cower Casual Smile1 at right
    with dissolve
    "\"Yes,\" Mikuru said quickly, nodding. \"He absolutely does! I don't know if you'll believe me, but it's the truth!\""
    show Yuki Talk1 at left
    "\"When this reality was overwritten with a reality where you had no powers, and none of our factions existed,\" Yuki contributed suddenly, \"he found a way to restore this reality once more, actually creating a parallel universe.\""
    nvl clear
    hide Mikuru
    hide Yuki 
    show Haruhi Casual Sigh1 at left
    show Kyon Casual Ser1 at right
    with dissolve
    "\"Then I'll believe that,\" she allowed, as strange as it seemed."
    "But he must be ... it made sense that John Smith was Kyon if he was a normal person who called in favors from others."
    nvl clear
    show Haruhi Casual Worry1
    "But still...."
    "\"Okay. Things are going to change, right now. Kyon, you want me to save Yuki, right?\""
    show Kyon Casual Sup2
    show Ksweat at right
    "\"You mean, you don't?\" he asked, aghast."
    show Haruhi Casual Pout1 at left
    "She winced. \"Of course I do! But I want your opinion!\""
    hide Ksweat
    show Kyon Casual Ang1 at right
    "\"Absolutely! Haven't I been clear enough!?\""
    nvl clear
    show Haruhi Casual Ang3 at left
    "\"Okay, then,\" Haruhi decided. \"But no more running around behind my back! Anyone who can't do this is out of the Brigade.\""
    hide Haruhi
    hide Kyon
    show Haruhi Point Casual Ang1 at center
    with dissolve
    "\"Everyone who really wants to help me out, and stay in the Brigade ...{w=0.8} everyone who wants to prove to me that this is true and earn my forgiveness for the whole stupid masquerade ...{w=0.8} has to accept {i}me{/i} as a boss, just like Kyon!\""
    nvl clear
    "She nodded decisively, {nw}"
    show Haruhi Point Casual Surpr1 at center
    extend "then her eyes widened slightly\nin realization. {nw}"
    show Haruhi Point Casual Scold1 at center
    extend "\"Oh, and Koizumi? You're demoted. Kyon's obviously more trustworthy as a vice commander, since you already report to him anyway. Everyone got it? We're the bosses ... not your 'Organizations' or 'Thought Entities' or mysterious future 'superiors' who somehow control your minds!\""
    nvl clear
    hide Haruhi
    show Yuki Talk1 at left
    show Koizumi Crossed Casual Ser1 at center
    show Mikuru Cower Casual Nervous3 at right
    show MTears Casual at right
    with dissolve
    "\"Understood,\" Yuki replied quietly. \"Permissions change indexed. Awaiting transfer.\""
    show Yuki Side1 at left
    show Koizumi Crossed Casual Ser2 at center
    "\"I promised this already,\" Koizumi agreed shakily. \"Very well.\""
    show Koizumi Crossed Casual Ser1 at center
    show Mikuru Cower Casual Wince1 at right
    "\"I.... I can't,\" Mikuru whimpered. \"I'm not even allowed to try! Oh, Suzumiya-san, I would, but I can't...\" "
    hide MTears
    show Mikuru Cower Casual Sup1 at right
    nvl clear
    "Mikuru's eyes widened as she looked up, blinking away her tears."
    "\"I ... I'm getting a message?\" she asked. {w}\"I ... I am allowed to do whatever Kyon-kun asks? B...but not you? I don't understand! I'm sorry, those are just my instructions!\""
    nvl clear
    hide Mikuru
    hide Koizumi
    show Haruhi Casual Eyeroll1 at left
    show Kyon Casual Ser1 at right
    show Yuki Side2 at center
    with dissolve
    "\"Well, fine,\" Haruhi grumbled, narrowing her eyes. \"I can trust {i}him{/i}.\""
    show Kyon Casual Ser2 at right
    "\"Right,\" Kyon said, looking at the interface at the table. \"Nagato, how much time is left?\""
    show Yuki Talk2 at center
    show Kyon Casual Ser1 at right
    "\"Thirty two minutes, fifteen seconds,\" she said."
    nvl clear
    show Haruhi Casual Worry1 at left
    show Yuki Side1 at center
    "\"So ... how do we do this?\" Haruhi asked, biting her lip. \"How do I use my power?\""
    nvl clear
    show Kyon Casual Ser3 at right
    "\"Your power is very dangerous,\" Kyon warned her. \"If it's used incorrectly, you might accidentally destroy the universe. But Nagato can use that power safely. {w}So, my idea is that you can become her boss and replace the Integrated Data Sentience Entity for her, and hopefully we won't have to destroy them. {w}If we have to, then they have to go ... that's all there is to it. But if we can avoid that ... well. Nagato, can you do what I'm thinking of?\""
    nvl clear
    show Kyon Casual Ser1 at right
    show Yuki Talk1 at center
    "Yuki blinked several times, then said, \"A memetic link can be formed between myself and Suzumiya Haruhi, such that all created data is cached within an internal buffer for analysis to await approval or disapproval. This will require the permissions of Suzumiya Haruhi, and an additional password carrier.\" Her eyes fixed on Kyon. \"That carrier shall be you. Is this acceptable?\""
    nvl clear
    show Haruhi Casual Sigh1 at left
    "\"If that's how it has to be done,\" Haruhi agreed with a shrug. \"I don't want you to die, Yuki.... Kyon?\""
    show Kyon Casual Ser2 at right
    "\"Yeah,\" he said, nodding quickly. \"Let's do it.\""
    nvl clear
    $ _window = True
    show Yuki Side1 at HalfLeft with move
    $ _window = False
    show Haruhi Casual Worry1 at left
    "Rising from her seat, the smaller girl reached both hands out and placed her fingertips across the sides of Haruhi's head. "
    show Yuki Talk1 at HalfLeft
    "\"Link established,\" she declared after a minute of silent staring into the taller girl's eyes."
    show Yuki Talk2 at HalfLeft
    "\"Awaiting data creation.\""
    nvl clear
    # show Haruhi Casual Quest1 at left
    show Haruhi Casual Ang1 at left
    "\"Data creation?\" Haruhi asked, frowning. \"What does that {i}mean{/i} exactly?\""
    $ _window = True
    scene bg YukiRoomCenter
    show Koizumi Crossed Casual Smile1 at center
    with dissolve
    "\"It has to do with how ... what she is views our world,\" Koizumi supplied helpfully. \"From our point of view, think of it as the ability to create new aspects of reality. I believe she is prepared for you to try and use your powers.\""
    nvl clear
    scene bg YukiRoomCenter
    show Haruhi Casual Ang1 at left
    show Kyon Casual Ser1 at right
    show Yuki Side1 at center
    with dissolve
    "\"Yeah, but ... how do I do that?\""
    show Kyon Casual Ser2 at right
    "\"Try and believe something,\" Kyon suggested. \"Believe that Yuki is going to be fine, and will report to you from now on.\""
    nvl clear
    show Haruhi Casual Focus1 at left
    "Haruhi shifted her gaze to the smaller girl before her, then took a deep breath and closed her eyes, concentrating."
    show Haruhi Casual Sigh1 at left
    "\"Yuki works for me,\" she muttered. \"She's a real alien ... but she's going to break away from her bosses and work for {i}me{/i}....\""
    nvl clear
    show Yuki Talk2 at center
    "\"Program loaded,\" Yuki said. Turning her eyes to Kyon, she asked, \"Permission to proceed?\""
    show Kyon Casual Ser3 at right
    stop music fadeout 3
    "\"Granted,\" he said without hesitation."
    nvl clear
    # scene black with dissolve
    # $ renpy.pause(.2, hard=True)
    # show BDVNlogo at truecenter with Dissolve(2.0)
    # pause 5

    # Calling a generic "eyecatch" routine, with unique "from"
    call eyecatch2("Sunday, April 17", "Monday, April 18") from AO1_sc004
    
    play music "Music/Itsumo(Movie).mp3"
    scene bg MorningSky
    show TownHillLeftMorning
    $ music_need = False
    show Kyon Neutral3 at right
    with fade
    "After finishing his breakfast and heading to school, he was startled to run into Haruhi at the train station at the bottom of the hill ... {nw}"
    show Haruhi Hap4:
        xalign 0.0 yalign 1.0
        linear 0.1 xalign 0.6
    play sound "SE/impact.mp3"
    extend "literally." 
    
    "The girl shot out from behind one of the pillars supporting the heavy structure keeping rainwater off the train platform, nearly plowing him over as she launched herself, arms wrapping around him as she swung around with her momentum, crying out, \"YES!\""
    nvl clear
    "Struggling and only barely managing to keep his balance, he eyed all of the other Kitago students around them, watching with raised eyebrows and open smirks."
    show Kyon Sigh3 at right
    "\"Hey,\" he managed, remembering his new role as the vice commander, and everything they had discussed the previous night."     
    show Kyon Smile1 at right
    "\"What's going on?\""
    nvl clear
    $ _window = True
    show Haruhi Hap3 at left with move
    $ _window = False
    "She released him with a huge grin."
    show Haruhi Hap4 at left
    "\"Yesterday, after I went home, was so cool!\" she squealed."
    show Haruhi Hap2 at left
    "\"I never knew you could do all those things! I mean, I suspected, since you were the best member of the Brigade next to myself and everything, but that was {i}amazing!{/i}\""
    nvl clear
    show Haruhi Smile3 at left
    play sound "Pageflip3.mp3"
    "Her smile not fading in the slightest, she handed him an envelope, the seal already broken."
    show Haruhi Hap2 at left
    "\"You said I should give this to you,\" she added. "
    show Haruhi Hap4 at left
    "\"You said to put it in your shoe locker, but why wait? What's so great about messages in shoe lockers?\""
    nvl clear
    show Kyon Sigh2 at right
    "\"They pretty much never go well for me,\" he sighed, taking the envelope and eyeing the broken seal. "
    "It was just a sticker, something that looked like it might have been stolen from one of his sister's collections. "
    show Kyon Sigh1 at right
    "\"You opened it already, I see.\""
    nvl clear
    show Haruhi Smile3 at left
    "\"Well, of course! Doesn't make any sense to me, though. I probably wouldn't have opened it if you hadn't told me it wouldn't make any sense to me."
    show Haruhi Quest1 at left
    "\"Why did you want me to give you a letter from yourself, though?\""
    show Kyon Sigh2 at right
    nvl clear
    "The skies were clear of rain, if gray, so he sighed and pulled the letter out of the envelope while proceeding up the hill."
    show Kyon Neutral3 at right
    "\"I'm guessing,\" he said mildly, \"that since I just went home last night, I'm going to be time traveling back to yesterday relatively soon.\""
    show Haruhi Smile3 at left
    nvl clear
    "\"Hmm...\" she mused, considering. \"Can I go with you?\""
    show Kyon Smile2 at right
    "\"'No, she can't',\" he quoted the first line of the note, scrawled hastily in his own handwriting. \"Well, seems that future me is a bit of a smart-ass.\""
    show Haruhi Crossed Tsun1 at left
    "\"Humph! I could have told you that.\""
    nvl clear
    show Kyon Sigh2 at right
    "He eyed her, then shook his head. He'd brought this upon himself."
    "Maybe, with luck, Nagato could act as a controlling agent and keep Haruhi in line. "
    "Maybe, he told himself. "
    # nvl clear
    "If this was what it took to save Nagato...."  
    nvl clear
    
    # Always place "jump credits" at the (current) end. Credits ARE important! ^___^
    jump AO2
    #jump credits
