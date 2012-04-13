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
    $ _window = True;
    "The first year student started, realizing where she was, then scurried beneath the table and clung to one of Kyon's legs. {nw}"
    # show Kanae Wince2:
    show Kanae Worry1:
        xalign 0.2 yalign 2.2
    with move
    extend "\"Sempai!\" she whimpered. \"Save me!\""
    nvl clear
    show Kyon Neutral2 at left
    "Placing another stone at the board, Kyon remarked, \"I'm threatening your piece, Koizumi; atari.\" Bending to look at the shivering girl who had grabbed onto him, he added, \"I don't think we've been introduced properly yet.\""
    show Kyon Neutral3 at left
    nvl clear
    "He took a moment to study her features, while she shivered in fright, clinging to him. Her brown hair was shoulder-length, and very curly just at the tips — fairly distinctive, he thought. She was probably as tall as Yuki, but with an even slighter frame, not quite gangly, but not yet grown into her height. Her dark eyes stared up at him pleadingly."
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Hap2 at left
    show Koizumi Think Ser3 at right
    "\"That all but confirms it,\" Haruhi declared, clapping her hands together and standing guard at the locked door. \"Okay, initiate, state your name and let go of the vice commander, {nw}"
    show Haruhi Crossed Hap4 at left
    extend "or I will issue a severe penalty!\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral3 at left
    show Mikuru Maid Unhap1 at right
    show MBlush1 Maid at right
    show Kanae Wince1:
        xalign 0.2 yalign 2.2
    "\"I-I really shouldn't,\" the girl stuttered. \"Sempai! Why aren't you helping me?\""
    nvl clear
    show Kyon Neutral2 at left
    "\"Alright,\" Kyon relented. \"I'll help you out, but I need to know who you are, first.\""
    show Kyon Neutral3 at left
    show Kanae Sad1:
        xalign 0.2 yalign 2.2
    "\"Um! I'm Michikyuu Kanae,\" she said. \"What's going on here?\""
    show Kyon Sigh2 at left
    "\"It's my fault,\" Kyon said, sighing. \"Haruhi asked me what was up with you, and I said you probably knew alternate universe versions of us from sliding through dimensions.\""
    nvl clear
    "\"You already know!?\" the girl yelped, trying to jump away from Kyon, {nw}"
    show Kanae Wince1:
        xalign 0.2 yalign 2.0
        linear 0.4 yalign 2.2
    play sound "SE/impact.mp3"
    pause 0.8
    hide MBlush1
    show Mikuru Think Maid Sup1 at right
    extend "but only smacking her head and jolting the table, scattering all the pieces across the board."
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Smile1 at left
    show Koizumi Shrug Sigh1 at right
    "\"Just as well,\" Koizumi said with a shrug. \"I don't think a six stone advantage was going to help me much.\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Sup1 at left
    show Ksweat at left
    show Mikuru Think Maid Sup1 at right
    show Kanae Wince1:
        xalign 0.2 yalign 2.2
    "\"Wait, you mean you're really a slider?\" Kyon asked, eyes widening in surprise. \"I was joking!\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Point Amuse1 at left
    show Koizumi Crossed Neutral1 at right
    "\"Kyon, Kyon, Kyon,\" Haruhi chastised him, her grin even wider as she shook her head. \"Shame on you! You really thought that kind of thing would be a throwaway comment?\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Sup1 at left
    show Ksweat at left
    show Mikuru Maid Quest1 at right
    show Kanae Wince1:
        xalign 0.2 yalign 2.2
    $ _window = False
    "\"...ow,\" Kanae moaned. \"My head....\""
    hide Ksweat
    show Kyon Sigh1 at left
    "\"Okay, this is very quickly getting out of hand,\" Kyon decided. \"Nagato?\""
    nvl clear
    show Kyon Sigh3 at left
    show YBook at TopRight behind Mikuru
    with dissolve
    "The quiet girl had watched everything without remark so far, so contributed, \"Quantum displacement agent. Through the accumulation of distortions through the fabric of space-time, she can create a ripple and then ride the wavefront of that ripple into alternate, similar realities.\""
    show Kyon Ser3 at left
    "\"So, that means slider?\""
    show Kyon Ser1 at left
    "\"Yes.\""
    nvl clear
    hide YBook
    show Kyon Neutral2 at left
    "\"Okay. Michikyuu-san, come out from the table and take a seat. I'll try and keep Haruhi from molesting you. Since you're a slider, please allow me to introduce you to the SOS Brigade,\" he said, gesturing to the others. \"It seems Haruhi has already decided that you've joined the club. Obviously, you're in good company, with one possible exception.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Hap2 at left
    show Koizumi Crossed Smile1 at right
    "\"But don't hold him being a normal person against him,\" Haruhi added quickly."
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Sigh2 at left
    show Mikuru Maid Smile1 at right
    show Kanae Wince1:
        xalign 0.2 yalign 2.2
    "\"Yes. That was precisely the exception I was thinking,\" he deadpanned."
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
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
    hide Mikuru with moveoutright
    show Mikuru Maid Smile1
    show MTray Maid
    with moveinright
    "Mikuru poured a cup of tea and set it at the table, {nw}"
    $ _window = True
    show Mikuru Maid Smile1 at right
    show MTray Maid at right
    show Kanae Worry3:
        xalign 0.5 yalign 1.0
    with move
    $ _window = False
    extend "while Kanae slid a chair next to Kyon and huddled in it, trying to hide behind him from Haruhi's line of sight. \"U...um....\" she whimpered. \"Y...you're not supposed to know who I am so easily! I only meant to tell Sempai.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Eyeroll1 at left
    show Koizumi Crossed Smile1 at right
    "\"Hmm. You must be very close with Kyon in your world,\" Haruhi remarked, eyes narrowing. {nw}"
    show Koizumi Crossed Uneasy1 at right
    extend "Koizumi gave an uncomfortable twitch."
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Kanae Sup2:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile1 at right
    "\"Eh? Yes! Of course! In every world I've been to, Sempai is always willing to help me when I'm in trouble, even if he doesn't believe my story! And he's always very polite, and so kind....\" She coughed, nervously picking up her tea and sipping at it. {nw}"
    show Kanae Sad3:
        xalign 0.5 yalign 1.0
    extend "After a taste, she said, \"I'm, um, not usually so impolite. I'm just a bit on edge....\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Worry1 at left
    show Koizumi Crossed Neutral1 at right
    stop music fadeout 3
    "\"'Every world'?\" Haruhi echoed, her eyes suddenly turning sympathetic as she stepped away from the door and sat next to Koizumi, opposite the younger girl. \"Do you mean, you're lost, Kanae-chan?\""
    nvl clear
    play music "Music/Fuyunoashioto.mp3"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Kanae Worry2:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Sad1 at right
    "Kanae nodded, frowning. \"That's right,\" she agreed. \"And I'm still trying to find my way home. I've been through over a hundred worlds by now, ever since before middle school! But Sempai almost always tells me that it's big trouble for you to know I'm a slider, even when he doesn't believe me.\" {nw}"
    show Kanae Quest1:
        xalign 0.5 yalign 1.0
    extend "Turning to Kyon, she asked, \"Sempai, why is it okay for her to know this time?\""
    nvl clear
    show Kyon Puzzle1 at left
    "\"I told her yesterday,\" he said, considering. \"Michikyuu-san, are you telling me that in alternate realities, I went to middle school with Haruhi?\""
    nvl clear
    show Kyon Neutral4 at left
    show Mikuru Maid Smile2 at right
    show Kanae Hap1:
        xalign 0.5 yalign 1.0
    "\"Yes, sometimes,\" Kanae agreed, smiling. \"And sometimes junior high school as well. Mostly in those realities, I think it was because of a zoning change that had one or another of the schools you usually go to removed. Sorry, after so many worlds, I tend to pay more attention to where you are than why you're there. But please, call me Kanae-chan, Sempai.\""
    show Kyon Neutral1 at left
    "\"Huh,\" he mused. \"There really was a slider.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Hap4 at left
    show Koizumi Crossed Smile1 at right
    "\"There sure is!\" Haruhi agreed. \"I guess you lose the 'honorary slider' title. {nw}"
    show Haruhi Hap1 at left
    extend "Hmm, even though we can help her get home, I'm reluctant to give her up so soon after finding her.\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Kanae Sup2:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile2 at right
    "\"Y...you can?\" Kanae asked, surprised. \"B...but, I can't go home yet,\" she said, shaking her head quickly. {nw}"
    show Kanae Worry3:
        xalign 0.5 yalign 1.0
    extend "\"Um, see, I'm not the only slider ... and the others don't like me much.\""
    nvl clear
    show Kyon Neutral2 at left
    "\"I think this is the first time anyone's shown up that hasn't done so specifically to investigate Haruhi,\" Kyon said thoughtfully."
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Hap1 at left
    show Koizumi Crossed Smile1 at right
    "\"She's not just a client who's also a slider,\" Haruhi warned. {nw}"
    show Haruhi Unhap1 at left
    extend "\"Until it's safe for her to go home, she's a member of the brigade! I'm serious about this.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral2 at left
    show Kanae Neutral1:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile2 at right
    "\"Hmm. Nagato, how many queued programs from Haruhi?\""
    show YBook at TopRight behind Mikuru
    with dissolve
    "\"Eighty seven items in queue currently.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Ang1 at left
    show Koizumi Crossed Neutral1 at right
    "\"It's less than a hundred!\" Haruhi protested, her expression switching to a scowl. \"And just because you control my power doesn't mean you get to dictate brigade policy! You're a vice commander, not the commander! {nw}"
    show Haruhi Crossed Hap2 at left
    extend "Oh, speaking of which, Koizumi, where's the armband?\""
    nvl clear
    show Koizumi Shrug Sigh1:
        xalign 2.3 yalign 1.0
    "\"I lost it,\" he said with a friendly smile. \"My apologies.\""
    show Koizumi Crossed Smile1 at right
    show Haruhi Hap1 at left
    "\"No problem,\" she said, shrugging, moving to the desk with the computer and pulling another red armband from the drawer. \"If you do find it, either give it to Kyon, or burn it — that's a unique badge of office!\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Kanae Worry3:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile2 at right
    "\"I feel more lost than usual,\" Kanae murmured, looking anxiously at Haruhi, {nw}"
    show Kanae Smile1:
        xalign 0.5 yalign 1.0
    extend "then hopefully at Kyon. \"You'll take care of me, won't you, Sempai?\""
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Hap4 at left
    show Koizumi Think Smile1 at right
    "\"Of course he will,\" Haruhi replied absently, writing out the characters for 'vice commander' in permanent marker. \"He's totally a sucker for you calling him 'Sempai' all the time. Look at that goofy expression!\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Sigh1 at left
    show Kanae Smile1:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile1 at right
    "Kyon sighed and hung his head. \"No respect,\" he muttered. {nw}"
    show Kyon Ser3 at left
    extend "\"Michikyuu-san, I'm sorry to put this on hold so abruptly, but there's something that Koizumi and I need to discuss with Haruhi.\""
    show Kyon Ser1 at left
    show Kanae Hap2:
        xalign 0.5 yalign 1.0
    "\"That's fine, Sempai!\" she agreed. \"But, please, call me Kanae-chan.\""
    nvl clear
    show Kyon Ser3 at left
    "\"Nagato, Asahina-san, would you mind watching over Michikyuu-san for a bit?\" he asked."
    show YBook at TopRight behind Mikuru
    with dissolve
    show Kyon Ser1 at left
    show Kanae Unhap1:
        xalign 0.5 yalign 1.0
    "\"It's Kanae-chan, Sempai!\""
    show Mikuru Maid Neutral2 at right
    "\"No problem,\" Yuki agreed, while Mikuru offered a more hesitant nod."
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Ang1 at left
    show Koizumi Think Grin1 at right
    "\"You think you've got something that's going to pull me away from finally getting a question in edgewise to a slider?\" Haruhi asked Kyon skeptically."
    "Koizumi grinned, ducking his head apologetically as he stowed the go board and pieces. {nw}"
    show Koizumi Think Grin2 at right
    extend "\"Well,\" he said, \"it does concern the destruction of our world.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Ser3 at left
    show Kanae Unhap3:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Neutral2 at right
    "\"Obviously, we're interested in preventing that,\" Kyon added. \"I'm hoping you're on the same page.\""
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Tsun2 at left
    show Koizumi Think Grin1 at right
    "\"Of course I am; what do you take me for?\" Haruhi groused. {nw}"
    show Haruhi Crossed Hap1 at left
    extend "\"But I meant what I said, Kanae-chan! You're part of the brigade now, and that means it's not just Kyon, but all of us who will watch out for you! {nw}"
    show Haruhi Point Hap1 at left
    extend"So come to this clubroom every day after class, or there will be a penalty!\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Smile1 at left
    show Kanae Hap3:
        xalign 0.5 yalign 1.0
    show Mikuru Maid Smile1 at right
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
    "Haruhi heaved a sigh, watching him walk away. \"Kyon,\" she said, quietly, \"I'm trying not to be upset about this. Because that just makes more trouble.\"" 
    show Haruhi Worry1 at TenthLeft
    "\"But more and more, this 'power' I've got really seems to suck! It's too dangerous to use, and just for having it, I endanger the world?\""
    nvl clear
    show Haruhi Pout1 at TenthLeft
    "\"Everything I looked for hid from me until you made them show themselves?\""
    nvl clear
    show Kyon Ser3 at right
    "\"Don't get too down,\" he told her. \"Remember, closed spaces result from your frustration. All you need to do to make Koizumi's job easier is be happy.\""
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
    show Haruhi Smile1 at TenthLeft
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
    
    call eyecatch2("December 200X","Monday, April 18") from SF1_sc003
    
label Test:
    scene bg ClubroomRightDay
    play music "Music/Yuuutsu.mp3"
    show Kyon Neutral3 at left
    show Mikuru Think Maid Sad1 at right
    show MTears Think at right
    show Kanae Worry3:
        xalign 0.5 yalign 1.0
    with fade
    "Mikuru sniffled, listening to the end of Kanae's story. \"That's so sad!\" she whimpered. \"Poor Kanae-chan!\""
    show Mikuru Think Maid Sad2 at right
    show Kanae Hap2:
        xalign 0.5 yalign 1.0
    "\"It's not so bad!\" Kanae said brightly. \"Even though everything changes from world to world, I still have my family! Sometimes I even have friends! And most importantly, I almost always have Sempai.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Worry1 at left
    show Koizumi Think Ser3 at right
    "\"Ouch,\" Haruhi said, taken aback. \"That doesn't sound like a fun power at all.\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral3 at left
    show Mikuru Think Maid Sad2 at right
    show MTears Think at right
    show Kanae Hap2:
        xalign 0.5 yalign 1.0
    "\"I can't let it get me down,\" the small girl declared confidently. \"I've never been to the same world twice, so with so many out there, I'm bound to find what I need, as long as I don't give up!\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Hap4 at left
    show Koizumi Think Grin1 at right
    "\"That's a good attitude! But you don't need to look any further; I'm absolutely sure we can find Kanae-chan's way home and deal with the alien invaders! It'll be easy, won't it? {nw}"
    show Haruhi Hap1 at left
    extend "Yuki-chan, you know everything, so how do we help her find her way home to find out about these enemies?\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral4 at left
    show Mikuru Maid Unhap2 at right
    show Kanae Neutral1:
        xalign 0.5 yalign 1.0
    show YBook at TopRight behind Mikuru
    "\"Unknown,\" Yuki replied without hesitation. \"I am not capable of traversal to other realities; neither is the Integrated Data Sentience Entity. This ability, much like that of Suzumiya Haruhi, can be termed 'unique'. Until the arrival of Michikyuu Kanae, the theory of other realities could not actually be proved, only speculated.\""
    nvl clear
    show Kyon Neutral1 at left
    "\"Would that mean that they also don't know about Michikyuu-san, and they're still in the dark on this one?\" Kyon mused."
    show Kyon Neutral4 at left
    show Kanae Sad2:
        xalign 0.5 yalign 1.0
    "\"It's Kanae-chan, Sempai,\" the underclassman reminded him."
    show Kanae Sad4:
        xalign 0.5 yalign 1.0
    "\"Possibly,\" Yuki allowed. \"Even though it is possible to discern Michikyuu Kanae's method of travel, I am unable to replicate or predict its function.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Hap1 at left
    show Koizumi Think Grin1 at right
    "\"Right,\" Haruhi decided, smacking one fist into her opposing palm. \"Then I just need to fix that, right?\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral2 at left
    show Mikuru Maid Unhap2 at right
    show Kanae Neutral1:
        xalign 0.5 yalign 1.0
    "\"Let's not be too hasty,\" Kyon warned. \"Michikyuu-san, how does your ability work?\""
    nvl clear
    show Kyon Neutral3 at left
    show Kanae Unhap1:
        xalign 0.5 yalign 1.0
    "\"It's Kanae-chan, Sempai,\" the girl replied. {nw}"
    show Kanae Worry3:
        xalign 0.5 yalign 1.0
    extend "\"Um ... it's hard to explain, though. It feels like turning a little to one side and pushing against the world, but not quite like that ... until the barrier that keeps us from falling out of the world gives way and I tumble through. But I can't even find my way back; the surface of reality ripples like a drop of water, so it never feels quite the same.... I wish I knew better! But like Nagato-san says, I've never found another slider who wanted to help me out.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Quest1 at left
    show Koizumi Crossed Neutral1 at right
    "\"You did mention others, though?\" Haruhi asked. \"So, what are these other sliders?\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Neutral3 at left
    show Mikuru Maid Unhap2 at right
    show Kanae Unhap2:
        xalign 0.5 yalign 1.0
    show YBook at TopRight behind Mikuru 
    "\"There's three of them, and they seem to travel together,\" the girl answered, frowning. \"I don't even really know their names, but I know they work with my enemies. One of them is a pretty girl with a completely white face and long, long black hair — like a ghost. Other people aside from her friends and myself don't seem to be able to see her, and she moves so fast....\" She shivered. \"She scares me the most. She's always the last one before the metal shapes come from the sky and I have to run again....\""
    nvl clear
    show Kanae Unhap3:
        xalign 0.5 yalign 1.0
    show Kyon Ser3 at left 
    "\"Suou Kuyou?\" Kyon asked, blinking in surprise, giving Yuki a questioning stare. Yuki said nothing, but to Kyon, her eyes looked troubled."
    nvl clear
    show Kyon Ser1 at left
    show Kanae Unhap2:
        xalign 0.5 yalign 1.0
    "\"Um, another one is a boy about Sempai's age, but he has a very rude manner of speech and gray eyes. His hair is very long for a boy, and he always wears a blue uniform. He uses a very shiny gun of some sort. He hit me with it once before ... it doesn't kill people, I think, but it knocks them out.\""
    nvl clear
    scene bg ClubroomFullDay:
        xpos -800 ypos 0
        linear 0.1 xpos 0 ypos 0
    show Haruhi Crossed Ang1 at left
    show Koizumi Crossed Neutral1 at right
    "\"I don't know who that guy is, but he already pisses me off!\" Haruhi announced, tapping one foot anxiously. \"If he shows his face around us, he's got a big surprise in store for him!\""
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 0.1 xpos -800 ypos 0
    show Kyon Ser3 at left
    show Mikuru Maid Unhap2 at right
    show Kanae Smile1:
        xalign 0.5 yalign 1.0
    show YBook at TopRight behind Mikuru
    "Kyon frowned. \"So, these other sliders are able to follow you, Michikyuu-san?\" he asked."
    nvl clear
    show Kyon Ser1 at left
    show Kanae Hap2:
        xalign 0.5 yalign 1.0
    "\"Ah ... well.... Yes, but I think it's because of the third one.\" Kanae's smile fell as she added, {nw}"
    show Kanae Unhap2:
        xalign 0.5 yalign 1.0
    extend "\"It's also why I like Sempai to call me Kanae-chan.\""
    show Kanae Unhap3:
        xalign 0.5 yalign 1.0
    show Kyon Unhap2 at left
    "\"Hmm? It isn't another version of {i}me{/i}, is it?\" Kyon asked, his eyes darkening."
    nvl clear
    show Kyon Unhap4 at left
    show Kanae Hap2:
        xalign 0.5 yalign 1.0
    "\"Haha, thankfully, no,\" Kanae said, shaking her head quickly. \"I don't know what I'd do if I couldn't rely on Sempai. {nw}"
    show Kanae Sad3:
        xalign 0.5 yalign 1.0
    extend "The other slider ... is another {i}me{/i}.\""
    # "\"Geez,\" Haruhi said with a wince. \"Come on, Kyon, don't be so formal! She's an underclassman, so it's not like people will make anything of it; show some sympathy!\""
    # "\"Er, sorry, Kanae-chan,\" he allowed. \"Well, I can understand you want help. But I'm not certain how much we can really do.\""
    # "\"I told you!\" Haruhi said in annoyance, slapping one palm against the center table. \"Yuki-chan! What program is currently in queue?\""
    # "\"Program one,\" the light-haired girl said. \"Share every lunch with-\""
    # "\"The next one! Not that one!\""
    # "\"Program two: Cause Tanaka-sensei to become more interesting.\""
    # "\"...tempting,\" Kyon allowed. \"But denied. You can ignore that, Nagato. Go ahead and clear out the queue again.\""
    # "\"Understood.\""
    # "\"Erg,\" Haruhi grumbled, grimacing, clenching her eyes shut in concentration. \"Um, Kanae-chan can control her sliding better to find her way home and back again.\" She opened one eye, peeking at Yuki. \"How about now?\""
    # "Yuki blinked, a tiny crease appearing in her brow as her eyebrows drew the slightest bit closer together. \"Unable to process,\" she finally said. \"I cannot determine parameters of dimensional sliding. Because of this, it is not possible to determine the effects of attempting to initiate a change in Michikyuu Kanae's abilities; attempting to alter or tamper with them may cause unforeseen consequences.\""
    # "\"Well, that's okay!\" Kanae said, slumping very slightly. \"I didn't really think it would be that easy....\""
    # "\"I'm trying not to get frustrated,\" Haruhi growled, flinging herself into her seat. \"What do we need to do?\""
    # "Mikuru wordlessly set another cup of tea before the brigade leader."
    # "\"A better understanding of dimensional sliding is required,\" Yuki answered. \"A form of dimensional anchor allowing Michikyuu Kanae to travel away and then return would allow the method to be discerned more completely.\""
    # "\"Eh ... now, where are we going to get such a thing?\" Haruhi wondered."
    # "\"Is it possible that such a thing already exists?\" Mikuru asked, frowning."
    # "Haruhi slumped further in her seat. \"I was hoping you could bring one from the future,\" she mumbled."
    # "\"Eh!? No, no, moving objects like weapons and tools from the future is absolutely forbidden!\" the time traveler said, shaking her head quickly."
    # "\"If even the Integrated Data Sentience Entity wasn't certain that such a thing as alternate realities or dimensions existed ... well, they exist outside of space and time,\" Kyon noted."
    # "\"Correct. Therefore, this does not preclude the creation of tools or theories to interact with unproven facets of reality,\" Nagato said."
    # "Haruhi and Kyon looked at her in surprise. \"You know something?\" she asked."
    # "\"The Integrated Data Sentience Entity is nearly as old as the concept of information. Tools for the purpose of theoretical interactions have been prepared in the past. However, as the entity is a non-physical existence, that data exists at this point unfabricated; millions of years have passed since the last known creation of any such items.\""
    # "\"Millions of years, huh?\" Kyon mused, rubbing his chin. \"Like, as long ago as the cave cricket?\""
    # "Nagato nodded. Haruhi and Kanae looked at him questioningly, while Mikuru shivered, shaking her head again. Kyon looked at the clock and pulled his now very heavily marked note from his future self from his bag. \"Four fifty five,\" he commented, just before the door slammed open."
    # "\"Ya-hoo!\" Tsuruya cheered, waving excitedly. \"Heya, Haru-nyan! Mikuru-chan, Nagato-chi, and, um, girl I don't know yet! Nice to meetchas!\""
    # "He turned his attention to the paper, jotting down some additional quick notes. \"Hey, Tsuruya-san,\" Haruhi replied, smiling back. \"What brings you here today?\""
    # "\"Kyon-kun asked mes!\" Tsuruya said, placing her hands on her hips and throwing her head back to laugh. \"After running into him yesterday, how could I not?\""
    # "\"What time did we meet, exactly?\" Kyon asked, glancing at her sidelong."
    # "\"Hmm?\" Tsuruya answered, her eyes focusing on him, though her smile didn't dim. \"You forgot? Well, I wasn't looking at my phone, but it was a bit after sunset! And thanks for helping me deal with those pushy fellows! Haru-nyan, don't let Kyon-kun get away! He seems quiet and unenthusiastic, but he's a real ace in the hole when it comes to fights! A regular warrior-philosopher!\" She mimed a few boxing jabs, then laughed loudly again. \"With an awesome dynamic entrance! Your wushu is pretty strong, Kyon-kun, so I appreciate your help!\""
    # "\"No problem,\" he muttered, one eyebrow twitching as he added more to his note. \"If it's not too much, did you bring that thing I asked for?\""
    # "\"Yep!\" she cheered. \"At four fifty five sharp, just like you said!\" She reached into her school bag and pulled out a small metal case, which she set on the table."
    # "\"Kyon got in a fight yesterday?\" Haruhi asked, taken aback, then turning an intent gaze on the boy in question. \"Hmm.... I want to hear all about that!\""
    # "\"You should ask him!\" Tsuruya laughed, pointing at Kyon. \"He was there!\" She stopped laughing abruptly and leaned in to peer at Kanae with a broad smile. \"Who's your new friend?\""
    # "\"This is Michikyuu Kanae,\" Haruhi said, indicating the first year girl. \"Our newest member; a first year.\""
    # "\"That makes sense!\" Tsuruya said brightly, nodding. \"She's got the same smell as everyone here but Kyon-kun! Well, nice to meetcha, Kanae-chan!\""
    # "\"U...um, nice to meet you?\" Kanae managed. \"Um, sorry, what's your name?\""
    # "\"Aha, sorry, sorry,\" Tsuruya chuckled. \"I forget to say sometimes! I'm Tsuruya Haruka! Well, I just came by to drop this off, but we'll see each other again soon, I betcha anything! So, take care, everyones, and thankie again, Kyon- kun!\" The excitable green-haired girl left as briskly as she arrived, closing the door behind her with an equally loud crash."
    # "Muttering to himself, Kyon reached for the case, beaten to it by Haruhi as she snatched it across the table, undoing the metal latches and swinging it open. \"What's kept in here, I wonder?\" she mused, blinking in confusion as she pulled a metal rod about twelve centimeters long from a foam recess within. \"Hmm, it looks like it's covered with engravings ... but they're all connected, like circuitry. You asked Tsuruya-san for this yesterday?\""
    # "\"I will,\" he answered her. \"Evidently.\" Turning his attention to Yuki, he asked, \"Titanium cesium alloy?\""
    # "She blinked, then gave a nod. \"Correct,\" she answered. \"Furthermore, this is a lost prototype dimensional anchor.\""
    # "\"Wow,\" Haruhi allowed, turning the item over in her hand and looking at it from all angles. \"How does it work?\""
    # "\"Kanae-chan points it at enemy sliders and says, 'Dimensional Prism Power, Make-up',\" Kyon suggested, smirking."
    # "\"Now you're just being silly,\" Haruhi answered, not even moving her eyes away from the rod."
    # "\"I am uncertain,\" Yuki replied. \"I will investigate.\""
    # "Haruhi handed the rod to the small girl, while Kanae watched breathlessly. \"Is this the answer we were looking for, Sempai?\" she asked him worriedly. \"This will help me find my way home?\""
    # "\"I have no idea, but I'll apparently think so in the future,\" he answered. Turning to Mikuru, he added, \"Also, thank you very much, Asahina-san.\""
    # "\"Um, what for?\" she asked, looking between Kyon and Yuki curiously."
    # "\"You'll know some day,\" he answered, looking bleakly at his note to himself. \"I really, really hope that I get some calm days to focus on some normal things, soon. This is getting really out of hand.\""
    # "\"Yeah,\" Haruhi jibed, rolling her eyes, \"you do love taking notes and paying attention in class. Without a good excuse to pay such weak attention, whatever would you do?\""
    # "\"I beg your pardon?\" he asked, quirking one eyebrow higher. \"I don't have good excuses, I have {i}awesome{/i} excuses.\""
    # "Haruhi grinned very brightly, chuckling. \"That's true,\" she allowed. \"Okay, vice commander, since we're here, and it seems Yuki's going to need some time to figure out the dimensional anchor, let's make sure you at least finish your homework. I'm not about to let your awesome excuses make the brigade look worse with sucky grades.\""
    # "Some day, Kyon realized, he would need to learn to keep his mouth shut."
    
    # "* * *"
    
    # "\"I have determined the function of the anchor,\" Yuki announced, just as Kyon was finishing his last math questions beneath Haruhi's sharp gaze. Mikuru had briefly snuck away to the girl's bathroom to change back into her uniform, and Kanae was curled over the desk, sleeping soundly with her school bag as a pillow."
    # "\"Excellent!\" Haruhi cheered, jolting the first year girl awake."
    # "\"Nya....\" Kanae murmured, sitting up and rubbing her eyes."
    # "\"So,\" Haruhi pressed, looking intently at Yuki, \"we can go to Kanae's home, now?\""
    # "\"Negative,\" Nagato replied, her eyes swinging to focus briefly on Haruhi before locking on Kyon. \"We can begin conducting experiments to discern the nature and limitations of Kanae's ability to traverse realities.\""
    # "Haruhi scowled, shaking her head. \"That's no fun,\" she groused. \"How long will it take?\""
    # "\"Uncertain.\""
    # "\"You know,\" Kyon noted, packing his homework away, \"you're disregarding something here, Haruhi. As I understand it, the Integrated Data Sentience Entity values new data more than anything else. In fact, at times, certain factions of it tried to provoke a response from you ... like the 'ghosts' that Sakanaka-san asked us to investigate.\""
    # "\"Well, it's not like I can 'react' much without you and Yuki-chan approving it, now. Which reminds me.... Let me try another one.\" She clenched her eyes shut, mumbling, \"The hair on my head grows ... five times as fast.\""
    # "\"Hyum?\" Kanae murmured, blinking as Mikuru dabbed at her mouth and wiped away the drool from her unintended nap. \"Oopsie! Thanks, Asahina-san.\""
    # "\"Program loaded,\" Yuki said, blinking."
    # "\"Er ... any side-effects to be aware of?\" Kyon asked."
    # "Yuki turned to Haruhi. \"Are eyebrows to be included in this program?\""
    # "\"Ack, no, I don't want hilariously bushy Asakura-type eyebrows,\" Haruhi said, shaking her head quickly. \"Just my hair ... you know, the part that gets styled regularly?\""
    # "\"Understood. Modifications complete.\" Turning back to Kyon, she asked, \"Permission to proceed?\""
    # "\"Granted,\" he said, shrugging. \"But aside from this amusing digression, the point I was trying to get to is that if we manage to discover data that is new to the Integrated Data Sentience Entity, they may end up willing to work with Nagato in the future in exchange for this data.\""
    # "\"I didn't think of that,\" Haruhi allowed, glancing at Kyon. \"And hey, Yuki- chan ... that's it? There was no tingle, no glowy lights ... powers are supposed to look awesome, not be invisible! Remember that next time.\""
    # "Yuki replied, \"Understood,\" and gave her tiny nod."
    # "\"Good. Now, Kanae-chan, how long does it take for the other sliders to show up and find you?\""
    # "\"Usually three or four weeks,\" the small girl said with a yawn, covering her mouth. \"Mmm. If I jump between worlds very quickly, it seems to take them a bit longer to show up. I'd guess probably four weeks from now? I landed badly the last time I jumped — I was about to call Sempai when I got scared by a loud noise and jumped right away ... so that should give me a bit of extra time.\""
    # "\"Ooh,\" Haruhi realized, grinning. \"Hey, Kyon, if Yuki-chan and Kanae-chan can't figure out how it works together, we can capture the enemy sliders and beat the information out of them! They obviously have a way to track Kanae- chan, don't they?\""
    # "\"And right on their heels, the alien invasion,\" he countered. \"Anyway, it's late; we should be getting out of the school.\""
    # "Haruhi nodded absently, shutting the computer down and gathering her book bag. \"In any case, that gives us a hard cap of around four or five weeks to get it sorted out.\""
    # "The other club members rose and gathered their things, Mikuru offering Kanae a hand when the younger girl wobbled tiredly on her feet. \"Understood,\" Yuki said softly. In the corridor, while Haruhi turned around and locked the club room door, the quiet girl slipped him a note. He pocketed it with a frown. Mikuru studiously pretended not to notice, while Kanae was looking the other way drowsily."

    # "* * *"
    
    # "After parting with the others at the train station, Kyon wasn't entirely surprised to see a familiar black taxicab pull from a side-street, stopping nearby. Koizumi leaned over and opened the back door, so with no hesitation, Kyon climbed in next to him."
    # "\"How did it go?\" he asked, before the esper could volunteer anything."
    # "\"It was a bit rough,\" Koizumi replied, still smiling. \"It could have been much worse, though. As I have mentioned before, one of the most stressful parts about this is simply getting to where the closed space is in a timely manner. Quite fortunately, all the spaces were within the coast of Honshu, so there was no need to travel extremely far.\""
    # "\"I hope it wasn't too much trouble. Hmm, I realize this isn't a critical issue, but out of curiosity, how much does it typically cost to deal with a Shinjin, anyway?\""
    # "\"That's entirely dependant on how much travel time is involved,\" Koizumi replied, shrugging. \"Hokkaido or Okinawa are of course going to be more difficult to reach, while Tokyo is relatively simple, thanks to the bullet train. However, you are correct in that this isn't a critical issue.\" He nodded his head at Arakawa, in the driver's seat, and explained, \"As I am now a liaison, not a full member of the Organization, this has been arranged to give you an update on the progress of closed space, and somewhat more to request an update from you on the events within the brigade meeting after my departure.\""
    # "\"Hey, Arakawa-san,\" Kyon said, nodding slightly. The older man grunted a wordless reply, giving a tiny nod of his own, his eyes fixed on the road. \"I'm a bit surprised that Mori-san isn't here.\""
    # "\"She's still a bit ... um ... intimidated by your last meeting,\" Koizumi said, his smile turning apologetic."
    # "Kyon blinked, wondering what he was going to have to have done. \"Okay,\" he allowed. \"In summary, we discussed Michikyuu Kanae and her abilities as a slider, the fact that she's being pursued by sliders who want to capture her, and that her home world was invaded by aliens. Possibly related to the Sky Canopy Domain.\""
    # "Koizumi paled, shivering. \"My,\" he allowed. \"That's ... less than comforting.\""
    # "\"Yeah. Kanae-chan is also lost, and doesn't have much control over her ability to slide; she's trying to find her way home, and someone who can help deal with the alien invasion. Surprisingly, we also discovered a limit to Haruhi's power. Namely, that she can't affect other worlds reliably, or the ability to travel to them.\""
    # "\"Is it possible that the limitation was Nagato-san's?\" Koizumi asked after a moment."
    # "\"It's possible,\" Kyon agreed, frowning. \"That hadn't occurred to me. On that subject, Nagato also explained that the Integrated Data Sentience Entity doesn't have the ability to travel to or observe alternate realities, either. They made a dimensional anchor, which was lost millions of years ago. Naturally, Nagato is using that to try and help Kanae out. It's my hope that any new data that Nagato discovers with Kanae's help can be used as a bargaining chip to get back on the good side of the entity.\""
    # "\"I see....\""
    # "\"On {i}that{/i} note,\" Kyon added, turning his attention to Arakawa, \"would it be possible to request that the Organization watch over Kanae as well? She's an important person in all of this, too.\""
    # "\"I will pass that request on to Mori-san,\" the older man allowed. \"If you will permit a personal observation, I'm rather surprised you trust us so much.\""
    # "\"Well, you've never threatened to kill Koizumi for displeasing you,\" Kyon said with a shrug. \"You've never intentionally treated him poorly because you thought that's the way things needed to be. As far as I know, anyway."
    # "\"More importantly, you haven't given me a reason not to trust you yet. Sorry if I, um, frightened Mori-san,\" though he boggled at the thought he could intimidate someone with such a smile, \"but after all is said and done, I'd like us to be able to work together. Ultimately, isn't your goal the stability of the world, and the safety of Haruhi and the people important to her?\""
    # "Koizumi worked his jaw for a moment, his smiling masked wiped away in a look of open-eyed astonishment before a real smile came to his lips."
    # "\"I will pass that on as well,\" Arakawa said, nodding."
    # "\"Is there anything else?\" Koizumi asked."
    # "Kyon shook his head, realizing they were only a few blocks from his house. \"Just that I'm sorry for the closed spaces so far. I'll do my best to keep Haruhi in good spirits.\""
    # "\"That is all we can ask for,\" Koizumi said, nodding. \"Thank you very much, vice commander.\""

    # "* * *"

    # "After enduring a haranguing lecture from his mother and missing dinner, Kyon went to his bedroom and checked the note Yuki had given him. It read simply, \"Call me.\""
    # "Shrugging, he picked up the phone and did as he was told, dialing her number from long memory. She answered instantly, her trademark quiet breathing the only response until he spoke. \"What's going on, Nagato?\" he asked."
    # "\"I am in need of assistance,\" she said quietly. \"I am requesting your aid immediately.\""
    # "\"Okay,\" he said, glancing around his room. \"I'll do whatever I can to help. I can be there in twenty minutes, so—\""
    # "\"Acknowledged. Standby for transfer.\""
    # "\"...what?\" he managed, as the world around him violently exploded away, revealing a yawning chasm full of stars, brightly colored gaseous clouds as though from distant nebulae, and myriad bolts of violently crackling energy in every direction. When he came to his senses, he was laying on the floor of Nagato's apartment, staring dazedly up into the girl's eyes."
    # "Looking around, he saw a shell-shocked Mikuru wearing nothing more than a towel about her midsection, and another wrapped around her head, seeming fresh out of the shower, and Kanae, sprawled on the floor near Nagato's table in pajamas and snoring contently."
    # "\"Um,\" he managed, sitting up and turning his eyes away from Mikuru. He wordlessly pushed his jacket at her, since he hadn't even had time to change out of his uniform. \"What's going on, Nagato?\" he added, closing his cell phone."
    # "She set down the receiver of her own phone and said without preamble, \"An error is likely to occur imminently.\""
    # "\"Mmm, Sempai,\" Kanae murmured in her sleep with a quiet giggle."
    # "\"Okay,\" he said, running his hands through his hair and trying not to look at either Mikuru or the sleeping girl who was dreaming about him with a blush on her cheeks. \"We have been relying on you too much. What can I do to help?\""
    # "\"I have already received permission from Suzumiya Haruhi to borrow you,\" the quiet girl said. \"With the help of the dimensional anchor, Michikyuu Kanae's ability to slide, and Asahina Mikuru's ability to traverse time, I will attempt to create a sealed alternate reality where my error can be expressed without causing any damage to the reality we currently dwell in.\""
    # "\"Do we need to bring Haruhi into this?\" he asked. \"I mean, she has to start whatever it is I authorize now, right?\""
    # "\"Negative,\" Nagato answered. \"I have deconstructed all previously queued requests and reassembled them to form data structures that can be executed with your permission. They are 'junk data' that I cannot destroy; I must find a way to execute them to prevent long-term damage or undue stress to the fabric of reality.\""
    # "\"Um, well, I want to help you,\" he said, nodding. \"As long as Asahina-san and Kanae-chan agree, then I can't think of a reason not to.\""
    # "\"Er ... could I ... borrow some clothes, maybe?\" Mikuru asked, her voice strained with embarrassment. \"I don't mind doing whatever Kyon-kun needs, but this is a little.... Erm....\""
    # "\"Hmm?\" Kanae drawled, sitting up. \"Oh? Eh? What's....\" She blinked, looking around with a furrowed brow. \"Did I slide in my sleep?\" she asked curiously. \"Sempai? Asahina-san? Nagato-san?\""
    # "\"Er, Nagato's having some ... trouble,\" Kyon allowed, trying to keep from staring at Mikuru, now wearing his coat and a pair of towels, her face dark red."
    # "\"Can I help?\" Kanae-asked, rubbing one eye sleepily."
    # "Yuki gave a tiny nod in response. \"I will attempt to construct a world based on our collective needs,\" she answered. \"To prevent long-term physical or mental stress, I will initiate an encoded pulse with physical and mental mapping. Estimating forty minutes to error.\""
    # "\"What do you need?\" Kyon asked quickly, rising to his feet."
    # "\"Wrist.\""
    # "Kyon nodded knowingly and presented one hand for Yuki to take before she bit his wrist, injecting him with nanites."
    # "Her attention turned to Kanae, and she repeated the demand. At Kanae's uncertain, questioning glance, he assured her, \"It's fine. If she says it's for our own protection, I believe her.\" Kanae nodded uncertainly and followed suit."
    # "With a whimpering sigh, one hand clutching the coat closed across her chest, Mikuru also offered her wrist. \"State your needs,\" Yuki added, turning her attention to Kyon."
    # "\"Um, needs?\" he asked. \"I don't know ... I guess I need to learn martial arts, according to Tsuruya-san. That and to be able to help you, whatever that ends up requiring.\""
    # "\"I'd like to be able to slide better, and know how to get back!\" Kanae added, offering a tiny smile."
    # "Mikuru winced. \"Really, some clothes would be just great,\" she mumbled."
    # "\"Initializing,\" Yuki replied."
    # "Then the world around Kyon exploded away again, for the second time in the last half hour."
