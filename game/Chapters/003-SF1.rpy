# Chapter 3, Straightforward Flashback and Exposition Arc.

label SF1: 
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 003 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
     
    scene bg ClubroomRightDay
    play music "Music/Oi.mp3"
    show Kyon Neutral3 at left
    show Mikuru Maid Unhap1 at right
    show MBlush1 Maid at right
    show Kanae Wince1:
        xalign 0.8 yalign 1.4
    with fade    
    "\"P...please get your face out of my chest!\" Mikuru blurted out, her face coloring red."
    show Kanae Sup1
    "The first year student started, realizing where she was, then scurried beneath the table and clung to one of Kyon's legs. {nw}"
    $ _window = True
    show Kanae Worry1:
        xalign 0.2 yalign 2.2
    with move
    $ _window = False
    extend "\"Sempai!\" she whimpered. \"Save me!\""
    nvl clear
    show Kyon Neutral2 at left
    "Placing another stone at the board, Kyon remarked, \"I'm threatening your piece, Koizumi; atari.\" Bending to look at the shivering girl who had grabbed onto him, he added, \"I don't think we've been introduced properly yet.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Worry1:
        xalign 1.563 yalign 2.2
    show Mikuru Maid Unhap1 at right_RightScreen
    show MBlush1 Maid at right_RightScreen
    "He took a moment to study her features, while she shivered in fright, clinging to him. Her brown hair was shoulder-length, and very curly just at the tips — fairly distinctive, he thought. She was probably as tall as Yuki, but with an even slighter frame, not quite gangly, but not yet grown into her height. Her dark eyes stared up at him pleadingly."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Hap2 at left
    show Koizumi Think Ser3 at right
    "\"That all but confirms it,\" Haruhi declared, clapping her hands together and standing guard at the locked door. \"Okay, initiate, state your name and let go of the vice commander, {nw}"
    show Haruhi Crossed Hap4 at left
    extend "or I will issue a severe penalty!\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Mikuru Maid Unhap1 at right_RightScreen
    show MBlush1 Maid at right_RightScreen
    show Kanae Wince1 at UnderLegs_RightScreen
    "\"I-I really shouldn't,\" the girl stuttered. \"Sempai! Why aren't you helping me?\""
    nvl clear
    show Kyon Neutral2 at left_RightScreen
    "\"Alright,\" Kyon relented. \"I'll help you out, but I need to know who you are, first.\""
    show Kyon Neutral3 at left_RightScreen
    show Kanae Sad1 at UnderLegs_RightScreen
    "\"Um! I'm Michikyuu Kanae,\" she said. \"What's going on here?\""
    show Kyon Sigh2 at left_RightScreen
    "\"It's my fault,\" Kyon said, sighing. \"Haruhi asked me what was up with you, and I said you probably knew alternate universe versions of us from sliding through dimensions.\""
    nvl clear
    scene bg ClubroomRightDay
    show Kyon Sigh2 at left
    show Kanae Sad1:
        xalign 0.2 yalign 2.2
    show Mikuru Maid Unhap1 at right
    show MBlush1 Maid at right
    "\"You already know!?\" the girl yelped, trying to jump away from Kyon, {nw}"
    $ _window = True
    show Kanae Wince1:
        xalign 0.2 yalign 2.0
        linear 0.4 yalign 2.2
    play sound "SE/impact.mp3"
    pause 0.8
    $ _window = False
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToRight])
    show Kyon Sigh2 at left_RightScreen
    show Kanae Wince1:
        xalign 1.563 yalign 2.2
    show Mikuru Think Maid Sup1 at right_RightScreen
    extend "but only smacking her head and jolting the table, scattering all the pieces across the board."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Smile1 at left
    show Koizumi Shrug Sigh1 at right
    "\"Just as well,\" Koizumi said with a shrug. \"I don't think a six stone advantage was going to help me much.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Sup1 at left_RightScreen
    show Ksweat at left_RightScreen
    show Mikuru Think Maid Sup1 at right_RightScreen
    show Kanae Wince1 at UnderLegs_RightScreen 
    "\"Wait, you mean you're really a slider?\" Kyon asked, eyes widening in surprise. \"I was joking!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Point Amuse1 at left
    show Koizumi Crossed Neutral1 at right
    "\"Kyon, Kyon, Kyon,\" Haruhi chastised him, her grin even wider as she shook her head. \"Shame on you! You really thought that kind of thing would be a throwaway comment?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Sup1 at left_RightScreen
    show Ksweat at left_RightScreen
    show Mikuru Maid Quest1 at right_RightScreen
    show Kanae Wince1 at UnderLegs_RightScreen
    $ _window = False
    "\"...ow,\" Kanae moaned. \"My head....\""
    hide Ksweat
    show Kyon Sigh1 at left_RightScreen
    "\"Okay, this is very quickly getting out of hand,\" Kyon decided. \"Nagato?\""
    nvl clear
    show Kyon Sigh3 at left_RightScreen
    show YBook at TopRight_RightScreen behind Mikuru
    with dissolve
    "The quiet girl had watched everything without remark so far, so contributed, \"Quantum displacement agent. Through the accumulation of distortions through the fabric of space-time, she can create a ripple and then ride the wavefront of that ripple into alternate, similar realities.\""
    show Kyon Ser3 at left_RightScreen
    "\"So, that means slider?\""
    show Kyon Ser1 at left_RightScreen
    "\"Yes.\""
    nvl clear
    hide YBook
    show Kyon Neutral2 at left_RightScreen
    "\"Okay. Michikyuu-san, come out from the table and take a seat. I'll try and keep Haruhi from molesting you. Since you're a slider, please allow me to introduce you to the SOS Brigade,\" he said, gesturing to the others. \"It seems Haruhi has already decided that you've joined the club. Obviously, you're in good company, with one possible exception.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Hap2 at left
    show Koizumi Crossed Smile1 at right
    "\"But don't hold him being a normal person against him,\" Haruhi added quickly."
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Sigh2 at left_RightScreen
    show Mikuru Maid Smile1 at right_RightScreen
    show Kanae Wince1 at UnderLegs_RightScreen
    "\"Yes. That was precisely the exception I was thinking,\" he deadpanned."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap2 at left
    show Koizumi Crossed Smile1 at right
    "\"Mikuru-chan! Give our newest member a cup of tea and prepare the accords to record the addition of a slider to our ranks!\""
    show Koizumi Think Sigh1 at right
    "Gathering the loose stones from across the table, Koizumi remarked, \"Perhaps we shouldn't record more than her name and that she joined the brigade. We wouldn't want certain information to fall into the hands of others too easily.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Kanae Wince1:
        xalign 0.2 yalign 2.2
    show Mikuru Maid Smile1 at right
    with None
    hide Mikuru with moveoutright
    show Mikuru Maid Smile1 at center
    show MTray Maid at center
    with moveinright
    "Mikuru poured a cup of tea and set it at the table, {nw}"
    $ _window = True
    show Mikuru Maid Smile1 at right
    show MTray Maid at right
    show Kanae Worry3 at center
    with move
    $ _window = False
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Worry3 at center_RightScreen
    show Mikuru Maid Smile1 at right_RightScreen
    show MTray Maid at right_RightScreen
    extend "while Kanae slid a chair next to Kyon and huddled in it, trying to hide behind him from Haruhi's line of sight. \"U...um....\" she whimpered. \"Y...you're not supposed to know who I am so easily! I only meant to tell Sempai.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Eyeroll1 at left
    show Koizumi Crossed Smile1 at right
    "\"Hmm. You must be very close with Kyon in your world,\" Haruhi remarked, eyes narrowing. {nw}"
    show Koizumi Crossed Uneasy1 at right
    extend "Koizumi gave an uncomfortable twitch."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Sup2 at center_RightScreen
    show Mikuru Maid Smile1 at right_RightScreen
    "\"Eh? Yes! Of course! In every world I've been to, Sempai is always willing to help me when I'm in trouble, even if he doesn't believe my story! And he's always very polite, and so kind....\" She coughed, nervously picking up her tea and sipping at it. {nw}"
    show Kanae Sad3 at center_RightScreen
    extend "After a taste, she said, \"I'm, um, not usually so impolite. I'm just a bit on edge....\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Worry1 at left
    show Koizumi Crossed Neutral1 at right
    stop music fadeout 3
    "\"'Every world'?\" Haruhi echoed, her eyes suddenly turning sympathetic as she stepped away from the door and sat next to Koizumi, opposite the younger girl. \"Do you mean, you're lost, Kanae-chan?\""
    nvl clear
    play music "Music/Fuyunoashioto.mp3"
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Worry2 at center_RightScreen
    show Mikuru Maid Sad1 at right_RightScreen
    "Kanae nodded, frowning. \"That's right,\" she agreed. \"And I'm still trying to find my way home. I've been through over a hundred worlds by now, ever since before middle school! But Sempai almost always tells me that it's big trouble for you to know I'm a slider, even when he doesn't believe me.\" {nw}"
    show Kanae Quest1 at center_RightScreen
    extend "Turning to Kyon, she asked, \"Sempai, why is it okay for her to know this time?\""
    nvl clear
    show Kyon Puzzle1 at left_RightScreen
    "\"I told her yesterday,\" he said, considering. \"Michikyuu-san, are you telling me that in alternate realities, I went to middle school with Haruhi?\""
    nvl clear
    show Kyon Neutral4 at left_RightScreen
    show Mikuru Maid Smile2 at right_RightScreen
    show Kanae Hap1 at center_RightScreen
    "\"Yes, sometimes,\" Kanae agreed, smiling. \"And sometimes junior high school as well. Mostly in those realities, I think it was because of a zoning change that had one or another of the schools you usually go to removed. Sorry, after so many worlds, I tend to pay more attention to where you are than why you're there. But please, call me Kanae-chan, Sempai.\""
    show Kyon Neutral1 at left_RightScreen
    "\"Huh,\" he mused. \"There really was a slider.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap4 at left
    show Koizumi Crossed Smile1 at right
    "\"There sure is!\" Haruhi agreed. \"I guess you lose the 'honorary slider' title. {nw}"
    show Haruhi Hap1 at left
    extend "Hmm, even though we can help her get home, I'm reluctant to give her up so soon after finding her.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Sup2 at center_RightScreen
    show Mikuru Maid Smile2 at right_RightScreen
    "\"Y...you can?\" Kanae asked, surprised. \"B...but, I can't go home yet,\" she said, shaking her head quickly. {nw}"
    show Kanae Worry3 at center_RightScreen
    extend "\"Um, see, I'm not the only slider ... and the others don't like me much.\""
    nvl clear
    show Kyon Neutral2 at left_RightScreen
    "\"I think this is the first time anyone's shown up that hasn't done so specifically to investigate Haruhi,\" Kyon said thoughtfully."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap1 at left
    show Koizumi Crossed Smile1 at right
    "\"She's not just a client who's also a slider,\" Haruhi warned. {nw}"
    show Haruhi Unhap1 at left
    extend "\"Until it's safe for her to go home, she's a member of the brigade! I'm serious about this.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral2 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Mikuru Maid Smile2 at right_RightScreen
    "\"Hmm. Nagato, how many queued programs from Haruhi?\""
    show YBook at TopRight_RightScreen behind Mikuru with dissolve
    "\"Eighty seven items in queue currently.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Ang1 at left
    show Koizumi Crossed Neutral1 at right
    "\"It's less than a hundred!\" Haruhi protested, her expression switching to a scowl. \"And just because you control my power doesn't mean you get to dictate brigade policy! You're a vice commander, not the commander! {nw}"
    show Haruhi Crossed Hap2 at left
    hide YBook
    extend "Oh, speaking of which, Koizumi, where's the armband?\""
    nvl clear
    show Koizumi Shrug Sigh1:
        xalign 2.2 yalign 1.0
    "\"I lost it,\" he said with a friendly smile. \"My apologies.\""
    show Koizumi Crossed Smile1 at right
    show Haruhi Hap1 at left
    "\"No problem,\" she said, shrugging, moving to the desk with the computer and pulling another red armband from the drawer. \"If you do find it, either give it to Kyon, or burn it — that's a unique badge of office!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Worry3 at center_RightScreen
    show Mikuru Maid Smile2 at right_RightScreen
    "\"I feel more lost than usual,\" Kanae murmured, looking anxiously at Haruhi, {nw}"
    show Kanae Smile1 at center_RightScreen
    extend "then hopefully at Kyon. \"You'll take care of me, won't you, Sempai?\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap4 at left
    show Koizumi Think Smile1 at right
    "\"Of course he will,\" Haruhi replied absently, writing out the characters for 'vice commander' in permanent marker. \"He's totally a sucker for you calling him 'Sempai' all the time. Look at that goofy expression!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Sigh1 at left_RightScreen
    show Kanae Smile1 at center_RightScreen
    show Mikuru Maid Smile1 at right_RightScreen
    "Kyon sighed and hung his head. \"No respect,\" he muttered. {nw}"
    show Kyon Ser3 at left_RightScreen
    extend "\"Michikyuu-san, I'm sorry to put this on hold so abruptly, but there's something that Koizumi and I need to discuss with Haruhi.\""
    show Kyon Ser1 at left_RightScreen
    show Kanae Hap2 at center_RightScreen
    "\"That's fine, Sempai!\" she agreed. \"But, please, call me Kanae-chan.\""
    nvl clear
    show Kyon Ser3 at left_RightScreen
    "\"Nagato, Asahina-san, would you mind watching over Michikyuu-san for a bit?\" he asked."
    show YBook at TopRight_RightScreen behind Mikuru with dissolve
    show Kyon Ser1 at left_RightScreen
    show Kanae Unhap1 at center_RightScreen
    "\"It's Kanae-chan, Sempai!\""
    show Mikuru Maid Neutral2 at right_RightScreen
    "\"No problem,\" Yuki agreed, while Mikuru offered a more hesitant nod."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Ang1 at left
    show Koizumi Think Grin1 at right
    "\"You think you've got something that's going to pull me away from finally getting a question in edgewise to a slider?\" Haruhi asked Kyon skeptically."
    hide YBook
    "Koizumi grinned, ducking his head apologetically as he stowed the go board and pieces. {nw}"
    show Koizumi Think Grin2 at right
    extend "\"Well,\" he said, \"it does concern the destruction of our world.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser3 at left_RightScreen
    show Kanae Unhap3 at center_RightScreen
    show Mikuru Maid Neutral2 at right_RightScreen
    "\"Obviously, we're interested in preventing that,\" Kyon added. \"I'm hoping you're on the same page.\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Tsun2 at left
    show Koizumi Think Grin1 at right
    "\"Of course I am; what do you take me for?\" Haruhi groused. {nw}"
    show Haruhi Crossed Hap1 at left
    extend "\"But I meant what I said, Kanae-chan! You're part of the brigade now, and that means it's not just Kyon, but all of us who will watch out for you! {nw}"
    show Haruhi Point Hap1 at left
    extend"So come to this clubroom every day after class, or there will be a penalty!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Smile1 at left_RightScreen
    show Kanae Hap3 at center_RightScreen
    show Mikuru Maid Smile1 at right_RightScreen
    "\"Thank you, Sempai! Thank you, Suzumiya-san!\" Kanae cheered. Haruhi's smile slipped a bit."
    nvl clear
    stop music fadeout 3
    
    call eyecatch("Monday, April 18") from SF1_sc001
    
    play music "Music/HaruhiNoOmoi.mp3"    
    scene bg SchoolTable
    show Kyon Ser1 at right
    show Haruhi Pout1 at center
    show Koizumi Crossed Ser1 at left
    with fade
    "After Koizumi had finished explaining his role as an esper, Haruhi nodded quietly, peering into the empty depths of her coffee cup. The three were seated at one of the outdoor tables near the cafeteria."
    nvl clear
    show Koizumi Crossed Sigh2 at left
    "Kyon finished the last sip of his own beverage, and then Koizumi sighed, rising to his feet. \"I apologize if this is troubling for you,\" he said. \"But I'm afraid I must go attend the current closed spaces." 
    show Koizumi Think Ser4 at left
    "\"Hopefully I will be more free tomorrow, and we can discuss what the Organization is and represents.\""
    nvl clear
    show Haruhi Worry1 at center
    "\"Can we go with you and help?\" Haruhi asked. \"If I caused this, then-\""
    show Koizumi Think Ser3 at left
    "\"Right now, that may not be the best idea,\" Koizumi cautioned. \"I am in a small bit of trouble with the Organization, as they're switching me from a full member to a liaison for the SOS Brigade. Ah, I should be off, though; Kyon-kun can explain more to you.\""
    nvl clear
    show Kyon Neutral2 at right
    "\"Good luck, Koizumi,\" Kyon said after a moment, nodding at the esper."
    show Koizumi Think Grin1 at left
    "Koizumi grinned back and bowed. \"You as well, vice commander.\""
    nvl clear
    hide Koizumi with moveoutleft
    pass
    show Kyon Neutral2 at right
    show Haruhi Worry1 at TenthLeft 
    with dissolve
    "Haruhi heaved a sigh, watching him walk away. \"Kyon,\" she said, quietly, \"I'm trying not to be upset about this. Because that just makes more trouble." 
    show Haruhi Worry1 at TenthLeft
    "\"But more and more, this 'power' I've got really seems to suck! It's too dangerous to use, and just for having it, I endanger the world?\""
    nvl clear
    show Haruhi Pout1 at TenthLeft
    "\"Everything I looked for hid from me until you made them show themselves?\""
    nvl clear
    show Kyon Ser3 at right
    "\"Don't get too down,\" he told her. \"Remember, closed spaces result from your frustration. All you need to do to make Koizumi's job easier is be happy."
    show Kyon Sigh1 at right
    "\"As long as you respect the boundaries of other people, I don't see why you can't be that. Especially since you now {i}know{/i} you've got a time traveler, an esper, and an alien in your club. Isn't that what you were looking for?\""
    nvl clear
    show Haruhi Worry2 at TenthLeft
    "\"And a slider,\" Haruhi added, struggling to force a smile."
    show Haruhi Pout1 at TenthLeft
    "\"It's like my wishes were granted by a literal genie who was looking for the wording loophole to keep me in the dark ... I mean, honestly, I'm a bit jealous. It seems that you got to do all the fun things while I was unaware!\""
    nvl clear
    show Kyon Ser3 at right
    "\"I've said it before, and I'll say it again,\" Kyon insisted. \"The most important thing to me about the brigade is the people in it. "
    show Kyon Sigh1 at right
    "\"There's a lot I don't care about — if we're trying to keep closed space from forming, if we're just hanging out and playing games, if we're working on the anthology.... \""
    nvl clear
    show Kyon Ser1 at right
    "\"What I {i}do{/i} care about is being there with the friends we've formed. Hey, Nagato explained what happened last December, right?\""
    show Haruhi Unhap2 at TenthLeft
    "\"Yeah,\" Haruhi said quietly, frowning. \"I guess Yuki must have been {i}really{/i} mad about me.... She doesn't show much, you know? And of course, something else to be jealous of — she opens up to you, not me.\""
    show Kyon Sigh2 at right
    nvl clear
    "\"That's not it,\" he countered, shaking his head. \"You probably see me as idle and ignorant, but I just try and pay close attention. I think I'd be a terrible person if I didn't pay attention to Nagato after she saved my life so many times." 
    show Kyon Neutral2 at right
    "\"The only person I can never figure out reliably is you.\""
    nvl clear
    show Haruhi Smile3 at TenthLeft
    "She smirked at that. \"Good,\" she decided. \"If you can solve aliens, time travelers, and everything else, at least there's one mystery left for you to focus on, right?\""
    show Kyon Worry1 at right
    "He looked away at the sky. \"Anyway,\" he said after an extended moment of silence, \"I had to leave that world because the people who made the brigade were there, but the brigade itself wasn't.\""
    nvl clear
    show Haruhi Quest1 at TenthLeft
    "\"Yeah, Yuki mentioned that.... Hey, I want to know something about that world — Yuki set it up for you, you know. What was she like? More assertive? I have a hard time imagining her being pushy.\""
    nvl clear
    show Kyon Sigh2 at right
    "\"Eh ... she was more like a regular girl,\" he said, shaking his head. \"She was quiet, just like now ... but more talkative than she usually is.\""
    show Haruhi Unhap2 at TenthLeft
    "\"Was she cute?\" Haruhi pressed, studying the profile of his face as he stared away."
    nvl clear
    show Kyon Smile5 at right
    "\"She looked exactly the same, just with her glasses on again,\" he answered with a shrug. \"Except ... well, she was more expressive. She had a very pretty smile; Nagato doesn't smile, really. That's one of the three main things that stick with me.\""
    show Haruhi Pout2 at TenthLeft
    "\"Hmm,\" she mused, trying to banish the rising frustration she felt. Her own fault for asking these questions, she supposed. \"What are the others?\""
    nvl clear
    show Kyon Worry1 at right
    show KBlush at right
    "\"Er.... Well, your other self in that world went to Kouyouen and hadn't cut her hair, so when we sneaked into Kitago, I asked you— That is, I asked her to put her hair in a ponytail.\" {nw}"
    show Haruhi Grin1 at TenthLeft
    extend "She smirked, seeing the faint coloring of his cheeks."
    show Haruhi Quest1 at TenthLeft
    "\"Oh?\" she asked. \"Hmm, what do you think about me making my longer hair again?\""
    nvl clear
    hide KBlush
    show Kyon Ser3 at right
    "He shook his head, looking at her carefully. \"It'd be a bit obvious,\" he warned her. Then he hesitated, considering, \"But I guess I can't just say 'no' to everything you want to do. Especially since that one sounds reasonable." 
    show Kyon Smile1 at right
    "\"What about toning it down a bit and just making it grow faster? Probably no one will notice if it finishes by the end of, say, summer vacation.\""
    nvl clear
    show Haruhi Sigh1 at TenthLeft
    "She counted the weeks in her head. \"Almost a full term away, huh? Well, I'm holding you to that,\" she decided. Some custodian of her powers he was going to be, if she could play his biases."
    show Kyon Neutral2 at right
    "\"Why do you want your hair longer again, anyway?\""
    nvl clear
    show Haruhi Pout2 at TenthLeft
    show Hblush at TenthLeft
    "She coughed quietly, looking another direction. \"So, what was the other thing that stuck with you?\""
    show Kyon Unhap1 at right
    "He shivered, looking away himself. \"Being stabbed.\""
    nvl clear
    hide Hblush
    show Haruhi Grin1 at TenthLeft
    "\"Wow, that's pretty short of an ideal world,\" Haruhi observed, trying not to snicker. \"You made it out alright, though, didn't you? Any scars?\""
    nvl clear
    show Kyon Sigh2 at right
    "\"Of course not,\" he answered. \"My future self and a future Nagato had to go back and.... Well, things got a bit complicated. Anyway, Nagato healed the injury. But this was when I was supposed to be in a coma. A scar from a stab wound when I 'fell down the stairs' seems a bit odd, don't you think?\""
    show Haruhi Quest1 at TenthLeft
    "\"True enough,\" she agreed. \"Anyway. I suppose we should investigate Kanae-chan's back story?\""
    nvl clear
    stop music fadeout 3
    
    call eyecatch2("Monday, April 18","December 200X") from SF1_sc002
    
    scene black
    play music "Music/Kankyou.mp3"
    "On Michikyuu Kanae's home world, when she was ten years old, a cataclysm had torn a hole in the sky. Strange sleek metallic things had rained down upon the city in her hometown, hatching into gracefully curved reflective metal creatures, no two quite alike, but all very spindly. All very fast, and quite dangerous."
    "Her friends had revealed to her then that she was a locus of power of some kind, and that she had to learn to use her gift and flee from the aliens. They had labored for months to keep her powers secret, even from herself, but with the invasion, there had been no choice. In desperation, not knowing if she could ever come back, she'd finally made the step — her first leap."
    nvl clear
    "Landing awkwardly in an alley in an unfamiliar city, her clothes torn and face smudged, not knowing how far her pursuers were from her, she cried for help ... and was answered. A friendly boy claimed he had known her from their elementary school, even though she didn't recognize him. He cleaned her scrapes and cuts, then led her to an unfamiliar school, where teachers insisted they knew her, and then she waved farewell to that kind older boy and was reunited with the parents who she knew, even though her memories didn't match up with theirs."
    nvl clear
    "Over the following weeks, she finally found out the boy's name, but by then, 'Sempai' had become ingrained in her way of thinking, and when everything else seemed strange, he at least listened. He smiled, sometimes he laughed and shook his head, and she doubted he believed ... but when no one else would, he {i}listened{/i}. So, afraid that those strange, sleek invaders from the sky would appear again, she decided to try and search for someone who could help her find what she needed to save her home, and maybe someone who could help her find her way there."
    nvl clear
    "Sometimes her sempai believed her, and sometimes he didn't. A few times, he told her he was an esper, and they weren't so different. Sometimes, and those were the worst, he wasn't anywhere in the world she could find. A few times, he said he knew aliens, time travelers, and a smaller handful of times, demons and other, stranger things. As the weeks turned into months, and then the months turned into years, she watched as in world by world, his attention shifted to other things, and he warned her away from the strange girl that had appeared by him frequently. In those worlds, he almost always believed her, but said he was powerless to help."
    "She had long ago lost count of how many worlds she'd been in, how many history tests she'd failed for remembering things correctly ... but differently. That didn't matter to her, though; in the end, he {i}always{/i} listened, and because of that, across countless worlds, Sempai was Sempai."
    nvl clear
    stop music fadeout 3
    
    call eyecatch2("December 200X","Monday, April 18") from SF1_sc003
    
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    play music "Music/Yuuutsu.mp3"
    show Haruhi Worry1 at left
    show Mikuru Think Maid Sad1 at right
    show MTears Think at right
    with fade
    "Mikuru sniffled, listening to the end of Kanae's story. \"That's so sad!\" she whimpered. \"Poor Kanae-chan!\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Hap2 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"It's not so bad!\" Kanae said brightly. \"Even though everything changes from world to world, I still have my family! Sometimes I even have friends! And most importantly, I almost always have Sempai.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Worry1 at left
    show Mikuru Think Maid Sad2 at right
    show MTears Think at right
    "\"Ouch,\" Haruhi said, taken aback. \"That doesn't sound like a fun power at all.\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Hap2 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    hide MTears
    "\"I can't let it get me down,\" the small girl declared confidently. \"I've never been to the same world twice, so with so many out there, I'm bound to find what I need, as long as I don't give up!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap4 at left
    show Mikuru Maid Smile2 at right
    "\"That's a good attitude! But you don't need to look any further; I'm absolutely sure we can find Kanae-chan's way home and deal with the alien invaders! It'll be easy, won't it? {nw}"
    show Haruhi Hap1 at left
    extend "Yuki-chan, you know everything, so how do we help her find her way home to find out about these enemies?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"Unknown,\" Yuki replied without hesitation. \"I am not capable of traversal to other realities; neither is the Integrated Data Sentience Entity. This ability, much like that of Suzumiya Haruhi, can be termed 'unique'. Until the arrival of Michikyuu Kanae, the theory of other realities could not actually be proved, only speculated.\""
    nvl clear
    show Kyon Neutral1 at left_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"Would that mean that they also don't know about Michikyuu-san, and they're still in the dark on this one?\" Kyon mused."
    show Kyon Neutral4 at left_RightScreen
    show Kanae Sad2 at center_RightScreen
    "\"It's Kanae-chan, Sempai,\" the underclassman reminded him."
    show Kanae Sad4 at center_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"Possibly,\" Yuki allowed. \"Even though it is possible to discern Michikyuu Kanae's method of travel, I am unable to replicate or predict its function.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Hap1 at left
    show Mikuru Maid Neutral2 at right
    "\"Right,\" Haruhi decided, smacking one fist into her opposing palm. \"Then I just need to fix that, right?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral2 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"Let's not be too hasty,\" Kyon warned. \"Michikyuu-san, how does your ability work?\""
    nvl clear
    show Kyon Neutral3 at left_RightScreen
    show Kanae Unhap1 at center_RightScreen
    "\"It's Kanae-chan, Sempai,\" the girl replied. {nw}"
    show Kanae Worry3 at center_RightScreen
    extend "\"Um ... it's hard to explain, though. It feels like turning a little to one side and pushing against the world, but not quite like that ... until the barrier that keeps us from falling out of the world gives way and I tumble through. But I can't even find my way back; the surface of reality ripples like a drop of water, so it never feels quite the same.... I wish I knew better! But like Nagato-san says, I've never found another slider who wanted to help me out.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Quest1 at left
    show Mikuru Maid Unhap2 at right
    "\"You did mention others, though?\" Haruhi asked. \"So, what are these other sliders?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Unhap2 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"There's three of them, and they seem to travel together,\" the girl answered, frowning. \"I don't even really know their names, but I know they work with my enemies. One of them is a pretty girl with a completely white face and long, long black hair — like a ghost. Other people aside from her friends and myself don't seem to be able to see her, and she moves so fast....\" She shivered. \"She scares me the most. She's always the last one before the metal shapes come from the sky and I have to run again....\""
    nvl clear
    show Kanae Unhap3 at center_RightScreen
    show Kyon Ser3 at left_RightScreen
    "\"Suou Kuyou?\" Kyon asked, blinking in surprise, giving Yuki a questioning stare. Yuki said nothing, but to Kyon, her eyes looked troubled."
    nvl clear
    show Kyon Ser1 at left_RightScreen
    show Kanae Unhap2 at center_RightScreen
    "\"Um, another one is a boy about Sempai's age, but he has a very rude manner of speech and gray eyes. His hair is very long for a boy, and he always wears a blue uniform. He uses a very shiny gun of some sort. He hit me with it once before ... it doesn't kill people, I think, but it knocks them out.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Ang1 at left
    show Mikuru Maid Unhap2 at right
    "\"I don't know who that guy is, but he already pisses me off!\" Haruhi announced, tapping one foot anxiously. \"If he shows his face around us, he's got a big surprise in store for him!\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser3 at left_RightScreen
    show Kanae Smile1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "Kyon frowned. \"So, these other sliders are able to follow you, Michikyuu-san?\" he asked."
    nvl clear
    show Kyon Ser1 at left_RightScreen
    show Kanae Hap2 at center_RightScreen
    "\"Ah ... well.... Yes, but I think it's because of the third one.\" Kanae's smile fell as she added, {nw}"
    show Kanae Unhap2 at center_RightScreen
    extend "\"It's also why I like Sempai to call me Kanae-chan.\""
    show Kanae Unhap3 at center_RightScreen
    show Kyon Unhap2 at left_RightScreen
    "\"Hmm? It isn't another version of {i}me{/i}, is it?\" Kyon asked, his eyes darkening."
    nvl clear
    show Kyon Unhap4 at left_RightScreen
    show Kanae Hap2 at center_RightScreen
    "\"Haha, thankfully, no,\" Kanae said, shaking her head quickly. \"I don't know what I'd do if I couldn't rely on Sempai. {nw}"
    show Kanae Sad3 at center_RightScreen
    extend "The other slider ... is another {i}me{/i}.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Sup1 at left
    show Mikuru Maid Sad1 at right
    "\"Geez,\" Haruhi said with a wince. {nw}"
    show Haruhi Eyeroll1 at left
    extend "\"Come on, Kyon, don't be so formal! She's an underclassman, so it's not like people will make anything of it; show some sympathy!\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser3 at left_RightScreen
    show Kanae Sad5 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"Er, sorry, Kanae-chan,\" he allowed. \"Well, I can understand you want help. But I'm not certain how much we can really do.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Point Ang1 at left
    show Mikuru Think Maid Sup1 at right
    "\"I told you!\" Haruhi said in annoyance, slapping one palm against the center table. \"Yuki-chan! What program is currently in queue?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser1 at left_RightScreen
    show Kanae Sad4 at center_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"Program one,\" the light-haired girl said. \"Share every lunch with-\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Ang4 at left
    show Mikuru Maid Quest2 at right
    "\"The next one! Not that one!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser1 at left_RightScreen
    show Kanae Sad4 at center_RightScreen
    show Yuki Right Talk1 at right_RightScreen
    "\"Program two: Cause Tanaka-sensei to become more interesting.\""
    show Yuki Right Neutral1 at right_RightScreen
    show Kyon Smile1 at left_RightScreen
    "\"...tempting,\" Kyon allowed. {nw}"
    show Kyon Ser3 at left_RightScreen
    extend "\"But denied. You can ignore that, Nagato. Go ahead and clear out the queue again.\""
    show Kyon Ser1 at left_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"Understood.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Focus1 at left
    show Mikuru Maid Quest2 at right
    "\"Erg,\" Haruhi grumbled, grimacing, clenching her eyes shut in concentration. \"Um, Kanae-chan can control her sliding better to find her way home and back again.\" {nw}"
    show Haruhi Quest1 at left
    extend "She opened one eye, peeking at Yuki. \"How about now?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Quest1 at center_RightScreen
    show Yuki Side SmallBlink at right_RightScreen
    "Yuki blinked, a tiny crease appearing in her brow as her eyebrows drew the slightest bit closer together. \"Unable to process,\" she finally said. {nw}"
    show Yuki Talk1 at right_RightScreen
    extend"\"I cannot determine parameters of dimensional sliding. Because of this, it is not possible to determine the effects of attempting to initiate a change in Michikyuu Kanae's abilities; attempting to alter or tamper with them may cause unforeseen consequences.\""
    nvl clear
    show Yuki Side1 at right_RightScreen
    show Kanae Unhap2 at center_RightScreen
    "\"Well, that's okay!\" Kanae said, slumping very slightly. \"I didn't really think it would be that easy....\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Ang1 at left
    show Mikuru Maid Neutral1 at right
    "\"I'm trying not to get frustrated,\" Haruhi growled, flinging herself into her seat. \"What do we need to do?\""
    show Haruhi Crossed Ang3 at left
    hide Mikuru with moveoutright
    show Mikuru Maid Neutral1 at HalfLeft
    show MTray Maid at HalfLeft
    with moveinright
    pause 0.5
    show Mikuru Maid Neutral1 at right
    show MTray Maid at right
    with move
    "Mikuru wordlessly set another cup of tea {nw}"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    show Haruhi Crossed Ang3 at left
    show Mikuru Maid Neutral1 at right
    show MTray Maid at right
    extend "before the brigade leader."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Unhap3 at center_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"A better understanding of dimensional sliding is required,\" Yuki answered. \"A form of dimensional anchor allowing Michikyuu Kanae to travel away and then return would allow the method to be discerned more completely.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    hide MTray
    show Haruhi Quest1 at left
    show Mikuru Think Maid Quest1 at right
    "\"Eh ... now, where are we going to get such a thing?\" Haruhi wondered."
    show Haruhi Smile1 at left
    show Mikuru Maid Quest1 at right
    "\"Is it possible that such a thing already exists?\" Mikuru asked, frowning."
    nvl clear
    show Haruhi Pout2 at left
    show Mikuru Maid Quest2 at right
    "Haruhi slumped further in her seat. \"I was hoping you could bring one from the future,\" she mumbled."
    show Haruhi Pout1 at left
    show Mikuru Think Maid Sup1 at right 
    "\"Eh!? No, no, moving objects like weapons and tools from the future is absolutely forbidden!\" the time traveler said, shaking her head quickly."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral2 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"If even the Integrated Data Sentience Entity wasn't certain that such a thing as alternate realities or dimensions existed ... well, they exist outside of space and time,\" Kyon noted."
    show Kyon Neutral3 at left_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"Correct. Therefore, this does not preclude the creation of tools or theories to interact with unproven facets of reality,\" Nagato said."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Sup1 at left
    show Mikuru Maid Quest2 at right
    "Haruhi and Kyon looked at her in surprise. \"You know something?\" she asked."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Quest1 at center_RightScreen
    show Yuki Right Talk1 at right_RightScreen
    "\"The Integrated Data Sentience Entity is nearly as old as the concept of information. Tools for the purpose of theoretical interactions have been prepared in the past. However, as the entity is a non-physical existence, that data exists at this point unfabricated; millions of years have passed since the last known creation of any such items.\""
    nvl clear
    show Kyon Neutral1 at left_RightScreen
    show Yuki Neutral1 at right_RightScreen
    "\"Millions of years, huh?\" Kyon mused, rubbing his chin. \"Like, as long ago as the cave cricket?\""
    nvl clear
    show Kyon Neutral3 at left_RightScreen
    "Nagato nodded. Haruhi and Kanae looked at him questioningly, while Mikuru shivered, shaking her head again. Kyon looked at the clock and pulled his now very heavily marked note from his future self from his bag. {nw}"
    show Kyon Neutral2 at left_RightScreen
    extend "\"Four fifty five,\" he commented, just before the door slammed open."
    nvl clear
    play sound "SE/doorclose.mp3"
    play music "Music/KouchouKouchou.mp3"
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Sup1 at left
    show Mikuru Think Maid Sup1 at right
    show Tsuruya Wave Hap3 at center with moveinleft
    "\"Ya-hoo!\" Tsuruya cheered, waving excitedly. \"Heya, Haru-nyan! Mikuru-chan, Nagato-chi, and, {nw}"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    show Haruhi Crossed Sup1 at left
    show Mikuru Think Maid Sup1 at right
    show Tsuruya Wave Quest1 at center
    extend "um, girl I don't know yet! {nw}"
    show Tsuruya Wave Hap2 at center
    extend "Nice to meetchas!\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "He turned his attention to the paper, jotting down some additional quick notes. "
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Hap1 at left
    show Tsuruya Wave Smile2 at center
    show Mikuru Maid Smile1 at right
    extend "\"Hey, Tsuruya-san,\" Haruhi replied, smiling back. \"What brings you here today?\""
    nvl clear
    show Haruhi Smile3 at left
    show Tsuruya Hap1 at center
    "\"Kyon-kun asked mes!\" Tsuruya said, placing her hands on her hips and throwing her head back to laugh. \"After running into him yesterday, how could I not?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral2 at left_RightScreen
    show Kanae Neutral1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"What time did we meet, exactly?\" Kyon asked, glancing at her sidelong."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Smile2 at left
    show Tsuruya Hap1 at center
    show Mikuru Think Maid Sup1 at right
    "\"Hmm?\" Tsuruya answered, her eyes focusing on him, though her smile didn't dim. \"You forgot? Well, I wasn't looking at my phone, but it was a bit after sunset! And thanks for helping me deal with those pushy fellows! Haru-nyan, don't let Kyon-kun get away! He seems quiet and unenthusiastic, but he's a real ace in the hole when it comes to fights! A regular warrior-philosopher!\" She mimed a few boxing jabs, then laughed loudly again. \"With an awesome dynamic entrance! Your wushu is pretty strong, Kyon-kun, so I appreciate your help!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Sigh2 at left_RightScreen
    show Kanae Sad2 at center_RightScreen
    show Yuki Right Neutral1 at right_RightScreen
    "\"No problem,\" he muttered, one eyebrow twitching as he added more to his note. {nw}"
    show Kyon Neutral2 at left_RightScreen
    extend "\"If it's not too much, did you bring that thing I asked for?\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Smile2 at left
    show Tsuruya Hap6 at center
    show Mikuru Think Maid Sup1 at right
    "\"Yep!\" she cheered. \"At four fifty five sharp, just like you said!\" She reached into her school bag and pulled out a small metal case, which she set on the table."
    nvl clear
    show Haruhi Crossed Sup2 at left
    show Tsuruya Smile2 at center
    "\"Kyon got in a fight yesterday?\" Haruhi asked, taken aback, then turning an intent gaze on the boy in question. {nw}"
    show Haruhi Crossed Eyeroll1 at left
    extend "\"Hmm.... I want to hear all about that!\""
    show Tsuruya Laugh1 at center
    "\"You should ask him!\" Tsuruya laughed, pointing at Kyon. \"He was there!\" {nw}"
    show Tsuruya Hap2 at center
    extend "She stopped laughing abruptly and leaned in to peer at Kanae with a broad smile. \"Who's your new friend?\""
    nvl clear
    show Haruhi Crossed Hap2 at left
    show Tsuruya Smile3 at center
    show Mikuru Maid Smile2 at right
    "\"This is Michikyuu Kanae,\" Haruhi said, indicating the first year girl. \"Our newest member; a first year.\""
    show Haruhi Crossed Smile1 at left
    show Tsuruya Hap4 at center
    "\"That makes sense!\" Tsuruya said brightly, nodding. \"She's got the same smell as everyone here but Kyon-kun! Well, nice to meetcha, Kanae-chan!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at left_RightScreen
    show Kanae Hap3 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"U...um, nice to meet you?\" Kanae managed. \"Um, sorry, what's your name?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Crossed Smile1 at left
    show Tsuruya Laugh2 at center
    show Mikuru Maid Smile1 at right
    "\"Aha, sorry, sorry,\" Tsuruya chuckled. \"I forget to say sometimes! {nw}"
    scene bg ClubroomLeftDay
    show Haruhi Crossed Smile1 at left
    show Mikuru Maid Smile1 at right
    show Tsuruya Hap3 at center
    extend "I'm Tsuruya Haruka! Well, I just came by to drop this off, but we'll see each other again soon, I betcha anything! "
    show Tsuruya Wave Hap6 at center
    extend "So, take care, everyones, and thankie again, Kyon-kun!\" {nw}"
    $ _window = True
    hide Tsuruya with moveoutleft
    $ _window = False
    play sound "SE/doorclose.mp3"
    extend "The excitable green-haired girl left as briskly as she arrived, closing the door behind her with an equally loud crash."
    nvl clear
    show Haruhi Grin1 at right
    show Mikuru Maid Quest2 at center
    with move
    "Muttering to himself, Kyon reached for the case, beaten to it by Haruhi as she snatched it across the table, undoing the metal latches and swinging it open. {nw}"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    show Haruhi Quest1 at right
    show Mikuru Maid Quest2 at center
    extend "\"What's kept in here, I wonder?\" she mused, blinking in confusion as she pulled a metal rod about twelve centimeters long from a foam recess within. \"Hmm, it looks like it's covered with engravings ... but they're all connected, like circuitry. {nw}"
    show Haruhi Worry1 at right
    extend "You asked Tsuruya-san for this yesterday?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Ser3 at left_RightScreen
    show Kanae Quest1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"I will,\" he answered her. \"Evidently.\" Turning his attention to Yuki, he asked, \"Titanium cesium alloy?\""
    show Kyon Ser1 at left_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "She blinked, then gave a nod. \"Correct,\" she answered. \"Furthermore, this is a lost prototype dimensional anchor.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Maid Quest2 at center
    show Haruhi Sup2 at right
    "\"Wow,\" Haruhi allowed, turning the item over in her hand and looking at it from all angles. {nw}"
    show Haruhi Quest1 at right
    extend "\"How does it work?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Smile3 at left_RightScreen
    show Kanae Quest1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"Kanae-chan points it at enemy sliders and says, 'Dimensional Prism Power, Make-up',\" Kyon suggested, smirking."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Think Maid Quest2 at center
    show Haruhi Eyeroll1 at right
    "\"Now you're just being silly,\" Haruhi answered, not even moving her eyes away from the rod."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Smile1 at left_RightScreen
    show Kanae Smile1 at center_RightScreen
    show Yuki Right Talk2 at right_RightScreen
    "\"I am uncertain,\" Yuki replied. \"I will investigate.\""
    scene bg ClubroomRightDay
    $ _window = True
    show Kyon Smile1 at left
    show Kanae Smile1 at center
    show Yuki Right Neutral2 at right
    show Haruhi Smile1 at HalfRight with moveinleft
    pause 0.5
    hide Haruhi with moveoutleft
    "Haruhi handed the rod to the small girl, while Kanae watched breathlessly. {nw}"
    $ _window = False
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToRight])
    show Kyon Smile1 at left_RightScreen
    show Kanae Unhap2 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    extend "\"Is this the answer we were looking for, Sempai?\" she asked him worriedly. \"This will help me find my way home?\""
    nvl clear
    show Kyon Neutral2 at left_RightScreen
    show Kanae Unhap3 at center_RightScreen
    "\"I have no idea, but I'll apparently think so in the future,\" he answered. Turning to Mikuru, he added, \"Also, thank you very much, Asahina-san.\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Think Maid Quest1 Flip at center
    show Haruhi Smile1 at right
    "\"Um, what for?\" she asked, looking between Kyon and Yuki curiously."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral2 at left_RightScreen
    show Kanae Unhap3 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"You'll know some day,\" he answered, looking bleakly at his note to himself. \"I really, really hope that I get some calm days to focus on some normal things, soon. This is getting really out of hand.\""
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Maid Smile2 at center
    show Haruhi Grin2 at right
    "\"Yeah,\" Haruhi jibed, rolling her eyes, \"you do love taking notes and paying attention in class. Without a good excuse to pay such weak attention, whatever would you do?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Smile3 at left_RightScreen
    show Kanae Smile1 at center_RightScreen
    show Yuki Right Neutral2 at right_RightScreen
    "\"I beg your pardon?\" he asked, quirking one eyebrow higher. \"I don't have good excuses, I have {i}awesome{/i} excuses.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Maid Smile1 at center
    show Haruhi Hap4 at right
    "Haruhi grinned very brightly, chuckling. \"That's true,\" she allowed. {nw}"
    show Haruhi Hap1 at right 
    extend "\"Okay, vice commander, since we're here, and it seems Yuki's going to need some time to figure out the dimensional anchor, let's make sure you at least finish your homework. {nw}"
    show Haruhi Point Amuse1 at right
    extend "I'm not about to let your awesome excuses make the brigade look worse with sucky grades.\""
    nvl clear
    scene black with dissolve
    "Some day, Kyon realized, he would need to learn to keep his mouth shut."
    nvl clear
    stop music fadeout 3
    
    call eyecatch("Monday, April 18") from SF1_sc004

    play music "Music/moon.ogg"    
    scene bg ClubroomFullDay:
        xpos -400 ypos 0
    show Kyon Ser1:
        xalign 1.25 yalign 1.0
    show Haruhi Unhap2 at left
    show Yuki Right Talk1 at HalfRight
    show Kanae Smile2:
        xalign 0.4 yalign 1.2
    with fade    
    "\"I have determined the function of the anchor,\" Yuki announced, just as Kyon was finishing his last math questions beneath Haruhi's sharp gaze. Mikuru had briefly snuck away to the girl's bathroom to change back into her uniform, and Kanae was curled over the desk, sleeping soundly with her school bag as a pillow."
    show Yuki Right Neutral1 at HalfRight
    show Haruhi Hap4 at left
    show Kanae Sup2:
        xalign 0.4 yalign 1.2
        linear 0.1 yalign 1.0
    "\"Excellent!\" Haruhi cheered, jolting the first year girl awake."
    show Kanae Worry2:
         xalign 0.4 yalign 1.0
    "\"Nya....\" Kanae murmured, sitting up and rubbing her eyes."
    show Haruhi Worry1 at left
    nvl clear
    "\"So,\" Haruhi pressed, looking intently at Yuki, \"we can go to Kanae's home, now?\""
    show Yuki Right Talk1 at HalfRight
    "\"Negative,\" Nagato replied, her eyes swinging to focus briefly on Haruhi before locking on Kyon. \"We can begin conducting experiments to discern the nature and limitations of Kanae's ability to traverse realities.\""
    nvl clear
    show Haruhi Eyeroll1 at left
    "Haruhi scowled, shaking her head. \"That's no fun,\" she groused. \"How long will it take?\""
    show Yuki Right Talk2 at HalfRight
    "\"Uncertain.\""
    nvl clear
    show Yuki Right Neutral1 at HalfRight
    show Kyon Ser2:
        xalign 1.25 yalign 1.0
    "\"You know,\" Kyon noted, packing his homework away, \"you're disregarding something here, Haruhi. As I understand it, the Integrated Data Sentience Entity values new data more than anything else. In fact, at times, certain factions of it tried to provoke a response from you ... like the 'ghosts' that Sakanaka-san asked us to investigate.\""
    nvl clear
    show Haruhi Unhap2 at left
    show Kyon Ser1:
        xalign 1.25 yalign 1.0
    "\"Well, it's not like I can 'react' much without you and Yuki-chan approving it, now. Which reminds me.... Let me try another one.\"" 
    show Haruhi Focus1 at left
    "She clenched her eyes shut, mumbling, \"The hair on my head grows ... five times as fast.\""
    nvl clear
    show Kanae Worry3:
        xalign 0.4 yalign 1.0
    "\"Hyum?\" Kanae murmured, blinking as Mikuru dabbed at her mouth and wiped away the drool from her unintended nap.{nw}"
    show Kanae Smile1:
        xalign 0.4 yalign 1.0
    "\"Oopsie! Thanks, Asahina-san.\""
    show Yuki Right Talk1 at HalfRight
    "\"Program loaded,\" Yuki said, blinking."
    show Kyon Worry1:
        xalign 1.25 yalign 1.0
    "\"Er ... any side-effects to be aware of?\" Kyon asked."
    nvl clear
    show Yuki Right Talk2 at HalfRight
    "Yuki turned to Haruhi. \"Are eyebrows to be included in this program?\""
    show Haruhi Sigh2 at left
    "\"Ack, no, I don't want hilariously bushy Asakura-type eyebrows,\" Haruhi said, shaking her head quickly. \"Just my hair ... you know, the part that gets styled regularly?\""
    show Yuki Right Talk1 at HalfRight
    "\"Understood. Modifications complete.\" Turning back to Kyon, she asked, \"Permission to proceed?\""
    nvl clear
    show Kyon Sigh2:
        xalign 1.25 yalign 1.0
    "\"Granted,\" he said, shrugging. \"But aside from this amusing digression, the point I was trying to get to is that if we manage to discover data that is new to the Integrated Data Sentience Entity, they may end up willing to work with Nagato in the future in exchange for this data.\""
    nvl clear
    show Haruhi Worry1 at left
    "\"I didn't think of that,\" Haruhi allowed, glancing at Kyon. \"And hey, Yuki-chan ... that's it? There was no tingle, no glowy lights ... powers are supposed to look awesome, not be invisible! Remember that next time.\""
    show Yuki Right Talk2 at HalfRight
    "Yuki replied, \"Understood,\" and gave her tiny nod."
    nvl clear
    show Haruhi Quest1 at left
    show Yuki Right Neutral2 at HalfRight
    "\"Good. Now, Kanae-chan, how long does it take for the other sliders to show up and find you?\""
    show Kanae Wince2:
        xalign 0.4 yalign 1.0
    "\"Usually three or four weeks,\" the small girl said with a yawn, covering her mouth."
    nvl clear
    show Kanae Sad3:
        xalign 0.4 yalign 1.0
    "\"Mmm. If I jump between worlds very quickly, it seems to take them a bit longer to show up. I'd guess probably four weeks from now? I landed badly the last time I jumped — I was about to call Sempai when I got scared by a loud noise and jumped right away ... so that should give me a bit of extra time.\""
    nvl clear
    show Haruhi Grin1 at left
    "\"Ooh,\" Haruhi realized, grinning. \"Hey, Kyon, if Yuki-chan and Kanae-chan can't figure out how it works together, we can capture the enemy sliders and beat the information out of them! They obviously have a way to track Kanae-chan, don't they?\""
    nvl clear
    show Kyon Ser2:
        xalign 1.25 yalign 1.0
    "\"And right on their heels, the alien invasion,\" he countered. \"Anyway, it's late; we should be getting out of the school.\""
    show Haruhi Sigh2 at left
    show Kyon Ser1:
        xalign 1.25 yalign 1.0
    "Haruhi nodded absently, shutting the computer down and gathering her book bag. \"In any case, that gives us a hard cap of around four or five weeks to get it sorted out.\""
    nvl clear
    "The other club members rose and gathered their things, Mikuru offering Kanae a hand when the younger girl wobbled tiredly on her feet. \"Understood,\" Yuki said softly. In the corridor, while Haruhi turned around and locked the club room door, the quiet girl slipped him a note. He pocketed it with a frown. Mikuru studiously pretended not to notice, while Kanae was looking the other way drowsily."
    nvl clear
    scene black with dissolve
    stop music fadeout 2
    
    call eyecatch("Monday, April 18") from SF1_sc005

    play music "Music/MysteryTime.mp3"
    scene bg SchoolEntranceLeft with fade
    "After parting with the others at the train station, Kyon wasn't entirely surprised to see a familiar black taxicab pull from a side-street, stopping nearby. Koizumi leaned over and opened the back door, so with no hesitation, Kyon climbed in next to him."
    play sfxloop "SE/CarBackgroundLong.mp3"
    scene bg Cab
    show Kyon Ser3 at right
    show Koizumi Crossed Smile1 at left
    with fade
    nvl clear
    "\"How did it go?\" he asked, before the esper could volunteer anything."
    show Koizumi Crossed Smile2 at left
    show Kyon Ser1 at right
    "\"It was a bit rough,\" Koizumi replied, still smiling. \"It could have been much worse, though. As I have mentioned before, one of the most stressful parts about this is simply getting to where the closed space is in a timely manner.\" "
    nvl clear
    show Koizumi Think Smile1 at left
    "\"Quite fortunately, all the spaces were within the coast of Honshu, so there was no need to travel extremely far.\""
    show Kyon Puzzle1 at right
    "\"I hope it wasn't too much trouble. Hmm, I realize this isn't a critical issue, but out of curiosity, how much does it typically cost to deal with a Shinjin, anyway?\""
    nvl clear
    show Kyon Neutral3 at right
    show Koizumi Shrug Sigh1:
        xalign -1.12 yalign 1.0
    "\"That's entirely dependant on how much travel time is involved,\" Koizumi replied, shrugging."
    show Koizumi Think Grin1 at left
    "\"Hokkaido or Okinawa are of course going to be more difficult to reach, while Tokyo is relatively simple, thanks to the bullet train. However, you are correct in that this isn't a critical issue.\""
    show Koizumi Think Ser4 at left
    nvl clear
    "He nodded his head at Arakawa, in the driver's seat, and explained, \"As I am now a liaison, not a full member of the Organization, this has been arranged to give you an update on the progress of closed space, and somewhat more to request an update from you on the events within the brigade meeting after my departure.\""
    nvl clear
    show Kyon Sigh2 at right
    "\"Hey, Arakawa-san,\" Kyon said, nodding slightly. The older man grunted a wordless reply, giving a tiny nod of his own, his eyes fixed on the road. \"I'm a bit surprised that Mori-san isn't here.\""
    nvl clear
    show Kyon Sigh4 at right
    show Koizumi Shrug Smile1:
        xalign -1.12 yalign 1.0
    "\"She's still a bit ... um ... intimidated by your last meeting,\" Koizumi said, his smile turning apologetic."
    show Kyon Sigh3 at right
    "Kyon blinked, wondering what he was going to have to have done." 
    nvl clear
    show Kyon Ser3 at right
    "\"Okay,\" he allowed. \"In summary, we discussed Michikyuu Kanae and her abilities as a slider, the fact that she's being pursued by sliders who want to capture her, and that her home world was invaded by aliens. Possibly related to the Sky Canopy Domain.\""
    nvl clear
    show Koizumi Think Sup1 at left
    show Kyon Ser1 at right
    "Koizumi paled, shivering. \"My,\" he allowed. \"That's ... less than comforting.\""
    show Kyon Worry1 at right
    "\"Yeah. Kanae-chan is also lost, and doesn't have much control over her ability to slide; she's trying to find her way home, and someone who can help deal with the alien invasion.\""
    nvl clear
    show Kyon Neutral1 at right
    "\"Surprisingly, we also discovered a limit to Haruhi's power. Namely, that she can't affect other worlds reliably, or the ability to travel to them.\""
    show Koizumi Think Ser4 at left
    show Kyon Neutral4 at right
    "\"Is it possible that the limitation was Nagato-san's?\" Koizumi asked after a moment."
    show Kyon Ser1 at right
    nvl clear
    "\"It's possible,\" Kyon agreed, frowning. \"That hadn't occurred to me. On that subject, Nagato also explained that the Integrated Data Sentience Entity doesn't have the ability to travel to or observe alternate realities, either."
    nvl clear
    show Kyon Ser3 at right
    "\"They made a dimensional anchor, which was lost millions of years ago. Naturally, Nagato is using that to try and help Kanae out. It's my hope that any new data that Nagato discovers with Kanae's help can be used as a bargaining chip to get back on the good side of the entity.\""
    show Koizumi Think Ser3 at left
    "\"I see....\""
    nvl clear
    show Kyon Neutral2 at right
    "\"On {i}that{/i} note,\" Kyon added, turning his attention to Arakawa, \"would it be possible to request that the Organization watch over Kanae as well? She's an important person in all of this, too.\""
    show Kyon Neutral3 at right
    "\"I will pass that request on to Mori-san,\" the older man allowed. \"If you will permit a personal observation, I'm rather surprised you trust us so much.\""
    nvl clear
    show Kyon Sigh2 at right
    "\"Well, you've never threatened to kill Koizumi for displeasing you,\" Kyon said with a shrug. \"You've never intentionally treated him poorly because you thought that's the way things needed to be. As far as I know, anyway.\""
    show Kyon Worry1 at right
    nvl clear
    "\"More importantly, you haven't given me a reason not to trust you yet. Sorry if I, um, frightened Mori-san,\" though he boggled at the thought he could intimidate someone with such a smile, \"but after all is said and done, I'd like us to be able to work together. Ultimately, isn't your goal the stability of the world, and the safety of Haruhi and the people important to her?\""
    nvl clear
    show Koizumi Think Sup1 at left
    "Koizumi worked his jaw for a moment, his smiling mask wiped away in a look of open-eyed astonishment before a real smile came to his lips."
    show Koizumi Think Grin1 at left
    "\"I will pass that on as well,\" Arakawa said, nodding."
    nvl clear
    show Koizumi Crossed Smile1 at left
    "\"Is there anything else?\" Koizumi asked."
    show Kyon Sigh2 at right
    "Kyon shook his head, realizing they were only a few blocks from his house. \"Just that I'm sorry for the closed spaces so far. I'll do my best to keep Haruhi in good spirits.\""
    show Koizumi Think Smile1 at left
    "\"That is all we can ask for,\" Koizumi said, nodding. \"Thank you very much, vice commander.\""
    nvl clear
    stop sfxloop
    stop music fadeout 3
    
    call eyecatch("Monday, April 18") from SF1_sc006
    

    play music "Music/Nichijou.mp3"
    scene bg KyonRoomLeftClosed with fade
    "After enduring a haranguing lecture from his mother and missing dinner, Kyon went to his bedroom and checked the note Yuki had given him. It read simply, \"Call me.\""
    "Shrugging, he picked up the phone and did as he was told, dialing her number from long memory. She answered instantly, her trademark quiet breathing the only response until he spoke. \"What's going on, Nagato?\" he asked."
    "\"I am in need of assistance,\" she said quietly. \"I am requesting your aid immediately.\""
    "\"Okay,\" he said, glancing around his room. \"I'll do whatever I can to help. I can be there in twenty minutes, so—\""
    "\"Acknowledged. Standby for transfer.\""
    nvl clear
    stop music
    play sound "SE/ShieldLaunch.wav"
    scene bg Space:
        xpos 0 ypos 0
    with circleirisoutfast
    "\"...what?\" he managed, as the world around him violently exploded away, revealing a yawning chasm full of stars, brightly colored gaseous clouds as though from distant nebulae, and myriad bolts of violently crackling energy in every direction." 
    play sound "SE/Laser1.mp3" 
    #play sound "SE/elec1.mp3"
    scene bg Space:
        xpos 0 ypos 0
        linear 0.5 xpos -800 ypos -1200
    scene bg YukiRoomCenter with circleirisinfast
    play music "Music/circulation.ogg"
    show Yuki Side1 at left
    show Kyon Sigh3 at right
    with dissolve
    nvl clear
    
    "When he came to his senses, he was laying on the floor of Nagato's apartment, staring dazedly up into the girl's eyes."
    show Mikuru Cower Towel Sup2 behind Kyon:
         xalign 1.3 yalign 1.2
    show Kanae Night Smile2:
        xalign 0.3 yalign 1.9
    with dissolve
    show Kyon Sup2 at right
    "Looking around, he saw a shell-shocked Mikuru wearing nothing more than a towel about her midsection, and another wrapped around her head, seeming fresh out of the shower, and Kanae, sprawled on the floor near Nagato's table in pajamas and snoring contently."
    nvl clear
    show Kyon Worry1 at right
    show KBlush at right
    show Mikuru Cower Towel Nervous1:
        xalign 1.3 yalign 1.2
    show MBlush Cower Towel behind Kyon:
        xalign 1.3 yalign 1.2
    "\"Um,\" he managed, sitting up and turning his eyes away from Mikuru. He wordlessly pushed his jacket at her, since he hadn't even had time to change out of his uniform. \"What's going on, Nagato?\" he added, closing his cell phone."
    show Yuki Talk1 at left
    "She set down the receiver of her own phone and said without preamble, \"An error is likely to occur imminently.\""
    nvl clear
    show KABlush:
        xalign 0.3 yalign 1.9
    show Yuki Side1 at left
    "\"Mmm, Sempai,\" Kanae murmured in her sleep with a quiet giggle."
    show Kyon Sigh2 at right
    "\"Okay,\" he said, running his hands through his hair and trying not to look at either Mikuru or the sleeping girl who was dreaming about him with a blush on her cheeks. \"We have been relying on you too much. What can I do to help?\""
    show Yuki Talk2 at left
    nvl clear
    "\"I have already received permission from Suzumiya Haruhi to borrow you,\" the quiet girl said. \"With the help of the dimensional anchor, Michikyuu Kanae's ability to slide, and Asahina Mikuru's ability to traverse time, I will attempt to create a sealed alternate reality where my error can be expressed without causing any damage to the reality we currently dwell in.\""
    nvl clear
    hide KBlush
    show Kyon Ser3 at right
    "\"Do we need to bring Haruhi into this?\" he asked. \"I mean, she has to start whatever it is I authorize now, right?\""
    show Yuki Talk1 at left
    show Kyon Ser1 at right
    "\"Negative,\" Nagato answered. \"I have deconstructed all previously queued requests and reassembled them to form data structures that can be executed with your permission. They are 'junk data' that I cannot destroy; I must find a way to execute them to prevent long-term damage or undue stress to the fabric of reality.\""
    nvl clear
    show Yuki Side1 at left
    show Kyon Neutral2 at right
    "\"Um, well, I want to help you,\" he said, nodding. \"As long as Asahina-san and Kanae-chan agree, then I can't think of a reason not to.\""
    show Kyon Neutral3 at right
    show Mikuru Cower Towel Nervous3:
        xalign 1.3 yalign 1.2
    "\"Er ... could I ... borrow some clothes, maybe?\" Mikuru asked, her voice strained with embarrassment. \"I don't mind doing whatever Kyon-kun needs, but this is a little.... Erm....\""
    nvl clear
    hide KABlush
    show Kanae Night Worry1:
        xalign 0.3 yalign 1.2
    with move    
    "\"Hmm?\" Kanae drawled, sitting up. \"Oh? Eh? What's....\" She blinked, looking around with a furrowed brow. \"Did I slide in my sleep?\" she asked curiously. \"Sempai? Asahina-san? Nagato-san?\""
    show Kyon Worry1 at right
    "\"Er, Nagato's having some ... trouble,\" Kyon allowed, trying to keep from staring at Mikuru, now wearing his coat and a pair of towels, her face dark red."
    nvl clear
    "\"Can I help?\" Kanae-asked, rubbing one eye sleepily."
    show Yuki Talk2 at left
    "Yuki gave a tiny nod in response. \"I will attempt to construct a world based on our collective needs,\" she answered. \"To prevent long-term physical or mental stress, I will initiate an encoded pulse with physical and mental mapping. Estimating forty minutes to error.\""
    nvl clear
    show Kyon Ser2 at right
    "\"What do you need?\" Kyon asked quickly, rising to his feet."
    show Yuki Talk1 at left
    show Kyon Ser1 at right
    "\"Wrist.\""
    show Yuki Side1 at left
    "Kyon nodded knowingly and presented one hand for Yuki to take before she bit his wrist, injecting him with nanites."
    nvl clear
    show Kyon Sigh1 at right
    "Her attention turned to Kanae, and she repeated the demand. At Kanae's uncertain, questioning glance, he assured her, \"It's fine. If she says it's for our own protection, I believe her.\" Kanae nodded uncertainly and followed suit."
    show Mikuru Cower Towel Nervous1:
        xalign 1.3 yalign 1.2
    "With a whimpering sigh, one hand clutching the coat closed across her chest, Mikuru also offered her wrist. {nw}"
    show Yuki Talk1 at left
    extend "\"State your needs,\" Yuki added, turning her attention to Kyon."
    nvl clear
    show Kyon Puzzle1 at right
    show Yuki Side1 at left
    "\"Um, needs?\" he asked. \"I don't know ... I guess I need to learn martial arts, according to Tsuruya-san. That and to be able to help you, whatever that ends up requiring.\""
    show Kanae Night Smile1:
        xalign 0.3 yalign 1.2
    show Kyon Neutral3 at right
    "\"I'd like to be able to slide better, and know how to get back!\" Kanae added, offering a tiny smile."
    show Mikuru Cower Towel Wince1:
        xalign 1.3 yalign 1.2
    "Mikuru winced. \"Really, some clothes would be just great,\" she mumbled."
    nvl clear
    show Yuki Talk2 at left
    "\"Initializing,\" Yuki replied."
    play sound "SE/ShieldLaunch.wav"
    scene bg Space:
        xpos 0 ypos 0
    with circleirisoutfast
    "Then the world around Kyon exploded away again, for the second time in the last half hour."
    scene black with fade
    nvl clear
    
    jump SF2
