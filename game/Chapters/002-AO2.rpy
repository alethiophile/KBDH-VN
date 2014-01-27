# Chapter AO2, 2 overall.

label AO2:
    # Also doing double duty to check if we need to set the background.
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
        play music "Music/ItsumoNoFuukei.mp3"
        scene bg MorningSky
        show TownHillLeftMorning
    show Haruhi Quest1 at left    
    "\"Anyway,\" Haruhi said, glancing at Kyon again as they topped the hill, \"what's it all mean?\""
    show Haruhi Quest2
    show Kyon Ser3 at right
    "\"I'm not entirely sure,\" he admitted, scanning his eyes across the other two lines before folding the letter back up and stuffing it into a pocket. \"I'm guessing it'll make sense when it happens.\""
    nvl clear
    
    scene black 
    show title 002 at card_pos 
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
    scene bg SchoolEntranceLeft with fade
    show Haruhi Neutral2 at left
    show Mikuru Neutral1 at center
    show Kyon Neutral3 at right
    with dissolve
    "\"So, you're good at time travel?\" she asked, nodding as Mikuru drew in range."
    show Haruhi Neutral1
    show Mikuru Cower Nervous2
    "\"Ah!\" the upperclassman yelped, wincing. \"S...Suzumiya-san, you can't talk about it so carelessly! People might overhear!\""
    show Mikuru Cower Nervous1
    show Haruhi Eyeroll1
    "\"What do I care?\" she asked, rolling her eyes. \"It's real, so I don't see a reason to hide it!\""
    nvl clear
    show Haruhi Eyeroll2
    show Kyon Sigh1
    "\"Because if you're careless, you might end up causing a paradox,\" Kyon said patiently."
    show Kyon Sigh3
    show Mikuru Ser2
    "Mikuru nodded furiously in agreement. \"If the timeplane is shattered,\" she whispered in a quiet, conspiratorial voice, \"then multiple realities could result. A break in the timeline could classified information!\""
    show Mikuru Sad2
    "Her face fell again. \"Ooh....\""
    nvl clear
    show Mikuru Unhap1
    show Haruhi Sigh1
    show Kyon Neutral3
    "\"Geez, that's gotta be annoying,\" Haruhi conceded. \"Well, you can tell me if he's good at it, right? Time travel, I mean.\""
    show Haruhi Smile1
    show Mikuru Sigh1
    "\"He's better at it than I am,\" Mikuru said with a crestfallen sigh."
    show Mikuru Sad2
    "\"I'm supposed to be a professional! But sometimes it feels like I was sent here to learn from him.\""
    nvl clear
    show Mikuru Unhap1
    show Haruhi Hap4
    "\"Hah! Okay, I'll admit, I had my doubts before. Mikuru the time traveler? Silly. Mikuru the cute and hilariously inept time traveler, relying on Kyon for support? Entirely plausible!\""
    nvl clear
    show Haruhi Hap5
    show Kyon Ser3
    $ _window = True
    "\"Be nice,\" Kyon said, shooting Haruhi a mild scowl. \"If it weren't for Asahina-san and her bosses helping us out ... things might be a lot worse right now.\"{nw}"
    show Mikuru Smile1
    pause
    show Kyon Ser1
    show Haruhi Sigh1
    $ _window = False
    "\"Alright,\" Haruhi allowed, smothering the irritation that arose when Mikuru's face lit up at Kyon's comment. \"But this doesn't get you out of mascot duty!\""
    nvl clear
    scene bg hallway with wipeup
    show Kyon Neutral3 at right
    show Haruhi Smile1 at left
    with dissolve
    "As she had expected, Kyon only shrugged at that. Mikuru broke away after they entered the school's front hall, moving to the third year students' shoe lockers." 
    "She and Kyon changed their shoes, then she sidled up to him on the walk to class." 
    nvl clear
    show Haruhi Quest1
    "\"But, seriously, is that why you're always seeming so tired and lazy, and your grades tend to suck?\" she asked in a soft tone."
    nvl clear
    show Haruhi Quest2
    show Kyon Ser3
    "He looked at her sharply. \"Only sometimes,\" he said. \"Uh ... the week of February — you remember when I called you in a panic to say Asahina-san had been kidnapped?\""
    show Kyon Ser1
    show Haruhi Worry1
    "She nodded, remembering it vaguely. \"Except, she was with me. I thought you said it was a really lousy prank call?\""
    show Kyon Ser2
    show Haruhi Quest2
    "\"A version of her from a week in the future was with me,\" he said in a low voice. \"And she {i}was{/i} kidnapped.\"" 
    nvl clear
    show Kyon Ser3
    show Haruhi Sup1
    "\"I spent that entire week running around making excuses to you so I could try and follow some set of obscure instructions from the future. It's not usually so bad ... that's why I did panic and called you, even though it was probably stupid.\""
    show Kyon Sigh2
    "\"Of course, you didn't believe me anyway.\" He shrugged, sliding open the door to the classroom."
    nvl clear
    scene bg classroom with wiperight:
        size (800,600)
    show Kyon Unhap4 at right
    show Haruhi Smile1 at left
    with dissolve
    "She watched the way his eyes tracked to Taniguchi, the other boy smirking widely. Kyon almost immediately adopted a scowl."
    show Haruhi Pout2
    "\"Well,\" she mumbled, \"you didn't tell me you were John Smith. If you {i}had{/i}....\""
    show Haruhi Pout1
    show Kyon Sigh2
    stop music fadeout 3
    "He sighed, nodding. \"Let's talk about that later,\" he suggested, taking his seat."
    show Kyon Sigh4
    nvl clear
    
    play sound "SE/WestminsterChimeShort.mp3"
    # Calling a generic "eyecatch" routine with date (first argument in (), "" to nhow no date) and custom pause time (second argument in ()), with unique "from"
    call eyecatch_fancy("Monday, April 18") from AO2_sc001
    stop sound fadeout 2
    
    play music "Music/Nanika.mp3"
    scene bg classroom: 
        size (800,600)
    show Kunikida Neutral1 at HalfLeft
    show Taniguchi Hap1 at HalfRight
    show Kyon Neutral3 at right
    show Haruhi Ang5 at left
    with fade
    "\"So,\" Taniguchi said with a huge grin, approaching Kyon's desk during the first break. \"I hear that things between you and Suzumiya are getting ... closer?\""
    show Taniguchi Grin1
    show Kyon Sigh1
    "Kunikida and Kyon exchanged a look, then turned to the other boy. \"Why don't you ask her?\" Kyon asked, jerking a thumb over his shoulder to point to the girl in question."
    nvl clear
    show Kyon Sigh3
    show Taniguchi Sup1
    "\"Eh!? Suzumiya?\" Taniguchi asked, stunned. \"But, it's break! Why are you still in the classroom?\""
    show Haruhi Ang6
    show Taniguchi Unhap2
    "\"Why is that any of your business?\" she asked him coolly, her eyes narrowing into sharp lines."
    show Taniguchi Sup2
    show Haruhi Ang3
    "\"I just remembered somewhere else I had to be,\" {nw}"
    $ _window = True
    hide Taniguchi Sup2 with moveoutright
    $ _window = False
    extend "he blurted out, charging out of the classroom."
    nvl clear
    show Kyon Sigh2
    "Kyon sighed, shaking his head."
    show Kyon Sigh4
    $ _window = True
    show Kunikida Smile3 at center with move
    $ _window = False
    "\"Well,\" Kunikida said, shrugging and offering a placating smile. \"It's none of my business either. But I thought I'd pass on that pretty much the entire school has caught on by now ... I wouldn't be terribly surprised if a teacher were to ask you about it, either.\""
    nvl clear
    show Kunikida Smile1
    show Haruhi Ang1
    "\"Ask us about what?\" Haruhi asked, her voice falsely innocent. \"We're just ordinary high school students!\""
    show Kunikida Neutral3
    show Haruhi Ang5
    "\"Er ... that is....\" Kunikida bowed his head slightly and shifted his gaze to stare out the window. \"Your ... 'display' at the train station.\""
    nvl clear
    show Kunikida Neutral1
    show Kyon Unhap1
    "Kyon groaned and lowered his head to his desk."
    show Haruhi Ang2
    "\"Well, the answer is still going to be that it's none of their business! Absolutely none!\""
    show Haruhi Ang5
    show Kunikida Neutral2
    "\"Aha ... well ... I'll leave the two of you to yourselves, then,\" {nw}"
    $ _window = True
    show Kunikida Neutral2 at right with move
    hide Kunikida with moveoutright
    extend "Kunikida said, bowing slightly as he drew away."
    nvl clear
    show Kyon Ser1
    "Straightening up once his friend had gone, Kyon turned in his chair to face Haruhi. {nw}"
    show Kyon Ser3
    extend "\"Do you understand the need to be somewhat subtle with all these things?\" he asked."
    show Kyon Ser1
    show Haruhi Ang1
    "\"You told me yesterday,\" she said in annoyance."
    show Haruhi Ang5
    show Kyon Sigh4
    "He blinked, then pulled the letter he had written himself from the future from his pocket and scribbled a note on it."
    nvl clear
    show Haruhi Eyeroll1
    "\"I'll be careful ... even if it is {i}boring{/i}. But it's not like it's {i}that{/i} outlandish for a girl to be close to a guy. At our age, it's practically expected."
    show Haruhi Ang6
    "\"Isn't that what Greaseball McGee over there,\" she said, nodding at Taniguchi as he slunk back into the classroom, \"is all about?\""
    nvl clear
    show Haruhi Ang4
    "\"Aside from which, people are stupid and think that 'something' is going on between us anyway. "
    show Haruhi Sigh2
    "\"If anyone asks, I'm tutoring you because your grades suck so bad. If they draw other conclusions on their own, they're obviously idiots and we shouldn't care.\""
    nvl clear
    show Haruhi Eyeroll1
    show Kyon Worry1
    "He flinched back from her gaze as her eyes lit up with intensity, adding, \"So, unless you've got some other girlfriend I should {i}know{/i} about, maybe Miyochiki—\""
    show Haruhi Eyeroll2
    show Kyon Ser2
    "\"Miyokichi,\" he corrected her flatly. \"And it's a real compliment to me that you seriously consider an eleven year old girl to be my only valid romantic prospect.\""
    nvl clear
    show Kyon Ser1
    show Haruhi Ang4
    "\"Whatever!\" she snapped, her face darkening. \"If not her, maybe that ... that Sasaki—\""
    show Haruhi Ang5
    show Kyon Sigh1
    "\"Ugh,\" he interjected again, this time with a small shudder. \"She's a friend, but I really can't stand who she chooses to associate with these days.\""
    nvl clear
    show Kyon Sigh3
    show Haruhi Sigh1
    "For some reason, Haruhi calmed substantially at that. \"Anyway,\" she said more smoothly, \"if you're not actually dating anyone, then you have no actual girlfriend to get jealous of our studying together."
    show Haruhi Smile2
    "\"And since you're some kind of action hero looking out for me, you can just consider it to be your cover.\""
    nvl clear
    show Kyon Puzzle1
    "\"So, you're okay with the entire school thinking that we're dating?\" he asked, unconvinced."
    show Haruhi Sigh1
    show Kyon Worry1
    "\"Well,\" she said quickly, looking away out the window again. \"No, I mean, we're obviously not. But hey, if they jump to that conclusion, what do we care? We can set anyone who asks straight.\""
    nvl clear
    show Haruhi Sigh3
    show Kyon Smile1
    "He allowed his lips to quirk very slightly into a smile."
    show Haruhi Hap1
    "\"Plus,\" she added, still staring out the window, \"you've got to give authorization for all of my powers, so there's no way in hell I'm letting you further out of reach than I have to.\""
    show Kyon Unhap1
    show Haruhi Smile3
    stop music fadeout 3
    "Sighing, he lowered his head to the desk again."
    nvl clear
    
    # scene black with dissolve
    # $ renpy.pause(.2, hard=True)
    # show BDVNlogo at truecenter with Dissolve(2.0)
    # pause 2.0
    
    # Calling a generic "eyecatch" routine, with unique "from"
    call eyecatch_fancy("Monday, April 18", "Sunday, April 17") from AO2_sc002
    
    play music "Music/Kokuhaku.mp3"
    scene bg YukiRoomCenter
    show Haruhi Casual Worry1 at left
    show Yuki Side1 Flip at HalfLeft
    show Kyon Casual Ser1 at right
    with fade
    "\"So,\" Haruhi asked, her back to the large window of Yuki's living room, \"did it work?\""
    show Haruhi Casual Quest2
    show Yuki Side1 Flip at center with move
    show Yuki Talk1 Flip
    "Yuki removed her fingertips from Haruhi's head and said, \"Yes.\""
    show Kyon Casual Puzzle1
    show Yuki Side1 Flip
    "\"You're not going to die?\" Kyon asked quickly."
    nvl clear
    show Kyon Casual Worry1
    show Yuki Talk2
    "Turning to face him, Yuki gave a small nod. \"I am no longer connected or accessible to the Integrated Data Sentience Entity,\" she said. \"They will not be able to delete me remotely.\""
    show Yuki Side2
    show Kyon Casual Sigh1
    "\"Good,\" he sighed, relaxing. "
    show Kyon Casual Smile6
    extend "\"Thank you, Haruhi.\""
    nvl clear
    show Kyon Casual Smile4
    show Haruhi Casual Pout2
    "\"I already told you,\" she grumbled, \"I'm not about to let\na brigade member get into trouble. And hurting Yuki because.... {nw}"
    show Haruhi Casual Quest1
    extend "Hey, actually, come to think of it, what was their reason?\""
    show Kyon Casual Neutral3
    show Haruhi Casual Quest2
    show Yuki Talk1
    "\"To prevent me from committing errors,\" Yuki answered. \"My makeup had been determined to destabilize, and I was scheduled for deletion prior to this error occurring.\""
    nvl clear
    show Yuki Side1
    show Haruhi Casual Worry1
    "\"What's this error, then?\""
    show Haruhi Casual Quest2
    show Yuki Talk2
    "\"Unknown.\""
    show Yuki Side2
    show Haruhi Casual Quest1
    "\"Is it going to happen?\""
    show Yuki Talk1
    show Haruhi Casual Quest2
    "\"Unknown.\""
    nvl clear
    show Yuki Side1
    show Haruhi Casual Unhap1
    "\"Hmm.... Hey, Kyon, you've always known Yuki best.\" Haruhi turned to look at him sternly. \"What's it all mean?\""
    show Haruhi Casual Unhap2
    show Kyon Casual Ser1
    "He frowned thoughtfully, his attention already focused on the smaller girl. {nw}"
    show Kyon Casual Ser3
    extend "\"Is this something on the scale of the incident from December?\" he asked."
    show Kyon Casual Ser1
    show Yuki Side Blink
    "The pale-haired girl blinked. \"Possibly.\""
    nvl clear
    show Yuki Side1
    show Kyon Casual Puzzle1
    "\"Is there any way we can try and prevent that from happening?\" he asked, shifting his shoulders."
    show Kyon Casual Worry1
    show Haruhi Casual Ang6
    "\"I don't like being left in the dark,\" Haruhi said crossly. \"So, what's this 'incident' about?\""
    show Haruhi Casual Ang3
    show Yuki Side Blink
    "Yuki blinked, then passed her eyes over everyone in the room in turn, lingering on Kyon and Haruhi before saying, \"I would like to speak of this privately.\""
    nvl clear
    show Yuki Side2
    show Kyon Casual Sigh2
    "\"Alright,\" Kyon agreed, shrugging his shoulders. \"I already remember, so I can respect that. Ah ... I know that this is a lot to take in, Haruhi, so is it okay if we talk about it later? Maybe at the brigade meeting tomorrow?\""
    show Kyon Casual Sigh4
    show Haruhi Casual Quest1
    "She hesitated a moment, then nodded. \"I suppose that you want me to stay here?\" she asked Yuki."
    nvl clear
    show Haruhi Casual Quest2
    show Yuki Side1
    "The quiet girl offered a nod of her own in return."
    show Haruhi Casual Unhap1
    "\"Well, alright then.\" In a warning tone, Haruhi added, \"The rest of you aren't off the hook yet, you know!\""
    nvl clear
    scene bg YukiRoomCenter
    show Koizumi Crossed Casual Ser2 at left
    show Mikuru Casual Neutral2 at right
    with dissolve
    "\"Of course,\" Koizumi said, nodding. \"I understand. In that case, Nagato-san, Suzumiya-san ... we shall take our leave?\""
    show Koizumi Crossed Casual Ser1
    show Mikuru Casual Quest1
    "\"Y...yes,\" Mikuru agreed, nodding as well. \"See you tomorrow.\""
    nvl clear
    scene bg Elevator with wiperight
    show Mikuru Casual Neutral1 at center
    show Kyon Casual Ser1 at right
    show Koizumi Crossed Casual Ser1 at left
    with dissolve
    "Kyon waved wordlessly, stepping through the door to the hall outside of Yuki's apartment last."    
    show Kyon Casual Sigh1
    "Once the three of them were in the elevator, heading down, Kyon said, \"I'm going to guess that you've got a small encyclopedia worth of questions for me, Koizumi.\""
    show Koizumi Crossed Casual Ser2
    show Kyon Casual Sigh3
    "\"My greatest question,\" the esper replied without hesitation, \"is if this was all necessary.\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Mikuru Casual Sad2
    "\"It was,\" Mikuru mumbled, her head bowed as the elevator stopped and the door opened. \"This was a predetermined event.\""
    show Koizumi Crossed Casual Sigh1
    show Mikuru Casual Unhap1
    "\"Is that so?\" Shaking his head, Koizumi added, \"I rushed over and missed lunch. I suspect you must have, as well. I think we have a lot to discuss ... so why don't we go to our usual cafe? My treat.\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Sigh2
    "\"That sounds fine by me,\" Kyon said with a shrug. The group stepped out of the elevator, only Kyon glancing at the snoozing supervisor in the lobby office. \"Asahina-san?\""
    show Mikuru Casual Quest1
    show Kyon Casual Sigh4
    "\"Um. Yes, okay,\" the time traveler agreed. \"But ... maybe we could go somewhere closer? Suzumiya-san might call and want to speak with us after ... um.\""
    nvl clear
    show Mikuru Casual Neutral2
    show Koizumi Crossed Casual Neutral2
    "\"Fine,\" Koizumi agreed, gesturing to the building entrance and leading the way."
    nvl clear
    scene bg YukiApartmentDay with wipeleft
    show Mikuru Casual Neutral1 at center
    show Kyon Casual Neutral2 at right
    show Koizumi Crossed Casual Ser1 at left
    with dissolve
    "Once they stepped out of the tall apartment building, Kyon asked, \"Is closed space still a concern?\""
    show Kyon Casual Neutral3
    show Koizumi Crossed Casual Sigh1
    "\"Right now, Suzumiya-san is more bewildered than anything else,\" the esper said, shaking his head. {nw}"
    show Koizumi Crossed Casual Ser2
    extend "\"But even though I requested this discussion, I still need a few minutes to order my thoughts.\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Ser2
    "\"Okay. Asahina-san, I know I requested your superiors back me up on explaining who you are to Haruhi, but I'm still not clear on why they suddenly decided that it was okay for you to do ... whatever I said,\" Kyon said, shifting his shoulders."
    show Kyon Casual Puzzle1
    "\"Was there anything else in that message?\""
    show Kyon Casual Worry1
    show Mikuru Casual Unhap1
    show MBlush1 Casual at center
    "\"Um, no,\" she answered, her face turning pink, her eyes looking away."
    nvl clear
    show Kyon Casual Sigh2
    show Koizumi Crossed Casual Sigh2
    "Both boys exchanged a glance, then shrugged."
    show Kyon Casual Sigh4
    show Koizumi Crossed Casual Sigh4
    nvl clear
    $ _window = False
    stop music fadeout 3

    # scene black with dissolve
    # $ renpy.pause(.2, hard=True)
    # show BDVNlogo at truecenter with Dissolve(2.0)
    # pause 5
    
    # Calling a generic "eyecatch" routine, with dates and unique "from"
    call eyecatch_fancy("Sunday, April 17","Monday, April 18") from AO2_sc003
    
    play music "Music/Yuuutsu.mp3"
    scene bg classroom with fade: 
        size (800,600)
    show Kyon Neutral3 at right
    show Haruhi Smile1 at left
    with dissolve
    show Haruhi Neutral2
    "\"Let's have lunch in the clubroom,\" Haruhi decided, the second the chime rang."
    show Haruhi Neutral1
    show Kyon Sigh2
    "Kyon blinked at her, then shrugged. \"Why not?\" he asked, shaking his head."
    nvl clear
    scene bg hallway with wiperight
    show Haruhi Quest1 at left
    show Kyon Neutral3 at right
    with dissolve
    "Once they reached the hallway, Haruhi looked around to ensure no other students were nearby, and asked, \"So, how long am I going to have put up with you and Yuki being in charge of me using my powers?\""
    show Haruhi Quest2
    show Kyon Smile7
    "\"I was thinking forever,\" he said with a slight smile."
    nvl clear
    show Kyon Smile5
    show Haruhi Ang4
    "She shot him a glower. \"Stop joking,\" she snapped. \"Seriously! If it's for Yuki's safety, then that's how it has to be — like I said yesterday." 
    show Haruhi Pout2
    "\"But it can't be {i}permanent{/i}, can it? I mean, can't I just fix it so that Yuki doesn't need to rely on me?\""
    nvl clear
    show Haruhi Pout1
    show Kyon Sigh2
    "\"Then once you can be responsible with your power,\" he said, shrugging. \"It's not like I've asked Asahina-san to let me go back and give myself notes on tests I did poorly on."
    show Kyon Neutral2
    "\"Or I've come back from the future to warn myself about upcoming pop quizzes. Really, while it's useful to have access to that kind of power, well.... With great power comes—\""
    nvl clear
    show Kyon Neutral3
    show Haruhi Ang4
    "\"Don't even try and quote that movie at me,\" she warned him."
    show Haruhi Ang5
    show Kyon Puzzle1
    "\"Er ... where it's from doesn't make it any less true,\" he countered."
    nvl clear
    show Kyon Worry1
    show Haruhi Crossed Ang1
    "\"Bah! I never wanted that! Espers with the duty to save the world, aliens with important research missions, time travelers who are only here to work — the goal was to have {i}fun{/i}.\""
    nvl clear
    scene bg stairwell2 with wipeup:
         size (800,600)
    show Kyon Ser3 at right
    show Haruhi Unhap2 at left
    with dissolve
    "They reached the stairs to the old club building, and he said, \"So, speaking of movies.... Now, I don't blame you for this personally, but using your power responsibly? Do you remember the movie we made? Your 'Mikuru beam'?\""
    scene bg ClubHallLeft with wiperight
    nvl clear
    show Haruhi Eyeroll1 at left
    show Kyon Ser1 at right
    with dissolve
    "\"Like I'd forget! What about it?\" She paused at the top of the stairs, not far from the clubroom door, musing. {nw}"
    show Haruhi Quest1
    extend "\"Does she really have one?\""
    nvl clear
    show Haruhi Quest2
    show Kyon Sigh2
    "\"Throughout the movie, she had several,\" he said, shrugging. \"The very first one would have killed me if Nagato hadn't saved my life.\""
    show Kyon Sigh4
    show Haruhi Sup1
    "She blanched at that. \"B...but....\""
    show Kyon Sigh1
    "\"And you didn't even {i}know{/i},\" he added, shaking his head.{nw} "
    show Kyon Ser2
    extend "\"So, yeah. Once you can be responsible with your power, we can worry about that.\""
    nvl clear
    show Kyon Ser1
    show Haruhi Pout2
    "\"I can be plenty responsible,\" she grumbled, following him as he opened the clubroom door."
    nvl clear
    play sound "SE/dooropenslow.mp3"
    stop music fadeout 3

    scene bg ClubroomLeftDay with slowflashbulb
    play music "Music/Aruame.mp3"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
        linear 8.0 xpos -800 ypos 0
    pause 8
    scene bg ClubroomRightDay with dissolve
    show Yuki Side1 at center
    show Kyon Neutral3 at right
    show Haruhi Smile2 at left
    with dissolve
    "Sitting oddly stiffly in her usual seat, Yuki stared forward, turning her face towards the pair as they entered."
    nvl clear
    show Haruhi Hap4
    "\"Oh!\" Haruhi said brightly. \"Perfect! I was hoping you'd be here so we could talk about things!\""
    show Haruhi Hap5
    show Kyon Ser1
    "\"Hmm,\" Kyon mused, setting his lunch box down and frowning. After a moment of peering at Yuki intently, he asked, {nw}"
    show Kyon Ser3
    extend "\"What's wrong, Nagato?\""
    nvl clear
    show Kyon Ser1
    show Yuki Side Blink
    "\"Four hundred and seventy three requests in queue,\" she answered, blinking."
    show Yuki Side1
    show Haruhi Sup1
    "Haruhi choked on what she'd been eating and Kyon glanced at her, scowling when he realized she'd helped herself to his lunch. "
    show Kyon Ser3
    extend "\"Really?\" he asked."
    nvl clear
    show Kyon Ser1
    show Yuki Talk1
    show Haruhi Quest2
    play music "Music/KouchouKouchou.mp3"
    "\"Program one goal: Cause dinnerware to levitate.\""
    show Yuki Side1
    show Kyon Ser2 
    "\"Denied. Haruhi, I think this is a perfectly good example of what I was talking about.\""
    show Haruhi Sigh1
    show Kyon Ser1
    "\"That one was on purpose,\" Haruhi mumbled, shrugging her shoulders. \"I just wanted to see if I could use my power.\""
    nvl clear
    show Haruhi Sigh3
    show Yuki Talk2
    "\"Program two goal: Cause parents to increase allowance.\""
    show Kyon Sigh1
    show Yuki Side1
    "\"Denied. Your powers are a gift, but not a toy,\" he said sternly, shaking his head."
    nvl clear
    show Kyon Sigh3
    show Yuki Talk2
    "\"Program three goal: Grant Suzumiya Haruhi the power to read minds.\""
    show Kyon Sup2
    show Ksweat at right
    show Yuki Side1
    "\"Oh, gods, what a terrifying thought. Denied!\""
    show Haruhi Ang1
    "\"Aw, come on!\" Haruhi protested. \"You're not going to let me have any fun, are you?\""
    nvl clear
    show Haruhi Ang5
    show Yuki Talk1
    "\"Program four goal: Replace actor in nighttime television drama with rabid wolverine.\""
    hide Ksweat
    show Kyon Ang1
    show Yuki Side1
    "\"Denied. What's fun for you isn't necessarily fun for other people! And it really seems that you have no concept of the fact that there are consequences for your actions.\""
    show Haruhi Ang4
    show Kyon Ser1
    "\"It's not like I couldn't just fix it! I'd have that ability, you know! Plus, that would only make the plot of Lost better.\""
    nvl clear
    show Haruhi Ang5
    show Yuki Talk2
    "\"Program five goal: Cause Nagato Yuki to stop relying on affection for you to prevent future errors.\""
    show Yuki Side1
    show Kyon Ser3
    "\"Denied. {nw}"
    show Kyon Puzzle1
    extend "Wait, what?\" Kyon turned to stare at Yuki, who had turned her gaze to Haruhi."
    nvl clear
    show Kyon Worry1
    show Yuki Talk1
    "In a very slightly more hurried tone, Yuki continued, {nw}"
    extend "\"Program six goal: Cause you to become more amicable to the suggestions of Suzumiya Haruhi.\"{fast}"
    show Kyon Ang1
    show Yuki Side1
    "\"Denied!\" He turned back to Haruhi and frowned sharply."
    $ _window = True
    show Kyon Ser1
    show Haruhi Pout1
    show Hblush at left with dissolve
    "She looked away, staring out the window while picking at Kyon's bento, her cheeks a bright red."
    nvl clear
    show Yuki Talk2
    "\"Program seven goal: Replace bathing area with larger facility.\""
    show Yuki Side1
    show Kyon Sigh1
    "\"Denied. And stop eating my lunch!\""
    show Kyon Sigh3
    show Haruhi Sup1
    "Haruhi choked again, {nw}"
    show Haruhi Pout2
    extend "her face darkening even further. \"That was when I went to take my bath,\" she mumbled."
    nvl clear
    show Haruhi Pout1
    show Yuki Talk1
    "\"Program eight goal: Cause Asahina Mikuru to stop being loyal to you instead of Suzumiya Haruhi.\""
    show Yuki Side1
    show Kyon Ser3
    "\"Denied. Why are you trying to change who people are, Haruhi?\""
    show Kyon Ser1
    hide Hblush
    show Haruhi Crossed Pout2
    show Hblush Crossed at left
    "\"It's not important,\" she muttered, turning her face away."
    nvl clear
    show Haruhi Crossed Pout1
    show Yuki Talk2
    "\"Program nine goal: Enlarge Suzumiya Haruhi's—{nw}\""
    hide Hblush Crossed
    show Haruhi Sup1
    show Hblush at left
    "{=shout}\"Yuki, that's enough!{/=shout} {=loud}Just forget, um, all of them!\"{/=loud} Haruhi yelled, pushing the remnants of Kyon's lunch across the table."
    show Haruhi Ang1
    show Yuki Side1
    "\"And forget about that one especially! You can't say that kind of thing in front of Kyon!\""
    nvl clear
    show Haruhi Ang5
    show Yuki Side Blink
    "\"Understood,\" Yuki replied. She looked thoughtful for a moment, then suddenly relaxed very slightly, turning her attention to her book."
    nvl clear
    show Yuki Side1
    show Kyon Sigh2
    "\"In the meantime,\" Kyon said, picking through what Haruhi had left him, \"I think my point stands for obvious reasons.\""
    show Kyon Sigh4
    show Haruhi Pout2
    "\"Yeah, yeah,\" Haruhi mumbled. \"I didn't {i}mean{/i} half of those things; they were just idle thoughts. I didn't know it was so sensitive.\""
    nvl clear
    show Haruhi Pout1
    show Kyon Ser3
    "\"I'm sure. But again, my point stands. Try not to give Nagato so much trouble by coming up with a hundred new things you didn't seriously think about before we actually have our club meeting, okay?\"" 
    show Kyon Sigh3
    hide Hblush
    "Disgruntled, and realizing he would have no actual meal, he wrapped his bento back up and turned to look at Yuki."
    show Kyon Neutral2
    nvl clear
    "\"In the meantime, Nagato ... you can safely disregard things that you know are a bad idea. Don't let Haruhi bother you too much; I trust your judgment.\""
    show Kyon Neutral3
    show Yuki Talk1
    "Yuki looked up from her book and regarded Kyon levelly. \"Thank you,\" she said softly."
    nvl clear
    show Yuki Side1
    show Haruhi Sigh1
    "Haruhi's expression shifted moodily before she suddenly stood up straight. \"I'm going to the cafeteria,\" she announced. \"So ... I didn't mean to cause trouble for you two!\""
    show Haruhi Sigh3
    show Kyon Smile6
    "\"I'll go with you,\" Kyon decided before Haruhi could storm out, stowing his bento in the clubroom's refrigerator. If he wanted to eat anything, he would have to buy it."
    nvl clear
    show Kyon Smile1
    show Haruhi Neutral3
    "Haruhi shifted her shoulders, allowing a small bit of tension to fade. \"Um, thanks,\" she mumbled. \"I'll let you buy me a sanshoku bread.\""
    show Haruhi Neutral4
    show Kyon Sigh4
    "He nodded, deciding that silence would be the best course of action for the moment."
    nvl clear
    $ _window = False
    stop music fadeout 2
    
    # Calling a generic "eyecatch" routine, with dates unique "from"
    call eyecatch_fancy("Monday, April 18","Sunday, April 17") from AO2_sc004
    
    play music "Music/suspicion.ogg"
    scene bg Cafe
    show Mikuru Casual Neutral1 at center
    show Kyon Casual Ser1 at right  
    show Koizumi Crossed Casual Ser1 at left
    with fade
    "After settling into a corner of a relatively new cafe, at least, one Kyon didn't recognize immediately, they sat in silence until their drinks were served."
    show Koizumi Crossed Casual Ser2
    "When his latte arrived, Koizumi began, saying, \"It is possible that Nagato-san may curtail the creation of closed space, but my suspicion is that the opposite is more likely to be true.\""
    nvl clear
    "\"That is to say ... with her aware of her abilities, and Nagato-san and yourself being the key to releasing those effects she may desire, Suzumiya-san is likely to create even more closed spaces.\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Ser3
    "\"I think even Haruhi would be reasonable enough to try and stop that once she was aware of it,\" Kyon countered. \"Is there a problem right now?\""
    show Kyon Casual Ser1
    show Koizumi Crossed Casual Sigh1
    "\"At the moment, no,\" Koizumi allowed. \"But we are entering, for all intents and purposes, uncharted territory. We don't know what might happen next, or if Suzumiya-san might even find a way to ... slip free from Nagato's control, as it were.\""
    show Mikuru Casual Sad2
    show Koizumi Crossed Casual Sigh3
    nvl clear
    "\"I don't like thinking of it like that,\" Mikuru mumbled into her glass. \"That sounds like putting a leash on Suzumiya-san.\""
    show Kyon Casual Sigh1
    show Mikuru Casual Unhap1
    "\"Sometimes,\" Kyon said quietly, \"I feel that's what the world needs more than anything else.\""
    nvl clear
    show Kyon Casual Sigh2
    "\"Don't get me wrong ... I don't believe that Haruhi's a terrible person by any stretch, but she's rather careless much of the time. If she has to have power, I think it's best she learn to use it responsibly." 
    show Kyon Casual Worry1
    "\"Or perhaps not at all.\""
    nvl clear
    show Koizumi Think Casual Ser4
    "\"I think you're completely discounting the frustration she's going to feel when it becomes more apparent that she is now limited by yourself and Nagato-san,\" Koizumi countered, rubbing his chin."
    show Koizumi Think Casual Ser2
    "\"I must ask you to take this as seriously as you wish for Suzumiya-san to. That seems only fair.\""
    show Koizumi Think Casual Ser1
    show Mikuru Casual Unhap3
    "Mikuru nodded weakly, looking away."
    nvl clear
    show Kyon Casual Ser2
    "Scowling, Kyon conceded, \"Alright. That's true. So, you think we'll need to let her use her ability as she wishes, now?\""
    show Kyon Casual Ser1
    show Koizumi Crossed Casual Sigh2
    "\"That may be going a bit far,\" Koizumi said, shrugging. \"You are the voice of reason for her, so I am merely asking that you be reasonable as well."
    show Koizumi Crossed Casual Ser2
    "\"Suzumiya-san doesn't seem the type to receive something at no cost and do away with it.\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Sigh2
    "\"Also true.\" Kyon sipped his coffee thoughtfully. \"She'd take a cursed item if she was told it was cursed, and for just that reason.\""
    show Koizumi Crossed Casual Ser2
    show Kyon Casual Sigh4
    nvl clear
    "\"Well, I shall monitor the closed space situation, and if it—{nw}\""
    show Koizumi Think Casual Ser2
    extend " He broke off abruptly, frowning. \"There's one now.... I think I can guess what Nagato-san has just finished explaining to Suzumiya-san.\""
    show Koizumi Think Casual Ser1
    show Mikuru Casual Quest1
    "\"What's that?\" Mikuru asked, glancing at Koizumi sidelong."
    show Mikuru Casual Quest2
    nvl clear
    stop music fadeout 2
    
    call eyecatch_fancy("Sunday, April 17") from AO2_sc005
    
    play music "Music/NagatoTheme.mp3"
    scene bg YukiRoomCenter
    show Haruhi Casual Worry1 at TenthLeft
    show Yuki Right Neutral1 at TenthRight
    with fade
    "\"Okay,\" Haruhi said, eyeing Yuki across the table and trying to put everything together. \"So, you're telling me that you changed the entire world to fit your ideals?\""
    show Yuki Right Talk1
    show Haruhi Casual Unhap2
    "\"In part,\" the stoic girl answered. \"It was also because I believed it was his ideal as well.\""
    show Yuki Right Neutral1
    show Haruhi Casual Quest1
    "\"You made a world where you were just a shy bookworm, and I went to a different school? But, why?\""
    nvl clear
    show Haruhi Casual Quest2
    show Yuki Right Talk2
    "\"It was an error. I was not to act on ... emotions.\" Yuki turned her eyes to the teapot and refilled Haruhi's cup."
    show Yuki Right Neutral2
    show Haruhi Casual Sigh2
    "\"Well, that gives me your cause,\" Haruhi said, frowning. \"But you don't even explain what emotions you had, or what your goals with your changes were.\""
    nvl clear
    show Haruhi Casual Ang3
    show Yuki Right Talk1
    "\"Sympathy.\""
    show Yuki Right Neutral1
    show Haruhi Casual Ang4
    "\"I'd like a bit more than a one word answer!\""
    nvl clear
    show Haruhi Casual Ang5
    show Yuki Right Talk2
    "\"My situation was sympathetic to his.\""
    show Yuki Right Neutral2
    show Haruhi Casual Ang6
    "\"'His'. You never call Kyon by his name ... why not?\""
    nvl clear
    show Haruhi Casual Ang3
    show Yuki Right Talk1
    "\"His name is not Kyon.\" Yuki blinked impassively, her face an unreadable mystery to Haruhi."
    show Yuki Right Neutral1
    show Haruhi Casual Pout2
    "Lifting her teacup to her lips and drinking half of it, Haruhi mumbled, \"Nevermind. Back to the earlier question. Why did you do it all? What 'emotion' compelled you?\""
    nvl clear
    show Yuki Right Talk2
    show Haruhi Casual Pout1
    "Yuki gave a tiny nod, explaining, \"During the summer vacation, you caused time to loop. The events from August 17th to August 31st repeated with some minor variations fifteen thousand, four hundred, ninety eight times. This caused me to become ... frustrated.\""
    show Yuki Right Neutral2
    show Haruhi Casual Sup1
    "\"Five hundred and ninety ... four years of summer vacation?\" Haruhi asked, taken aback. \"I don't remember that!\""
    nvl clear
    show Yuki Right Talk2
    "\"No,\" Yuki agreed. \"Others near you began to experience resonant familiarity with cyclical events. It caused the others to experience some distress, despite your unawareness." 
    show Haruhi Casual Neutral4
    "\"I retained perfect awareness because of memories transfered back to me by the Integrated Data Sentience Entity.\""
    nvl clear
    show Yuki Right Neutral2
    show Haruhi Casual Quest1
    "Haruhi mulled it over. \"So, that's how long you waited before breaking the loop?\""
    show Haruhi Casual Quest2
    show Yuki Right Talk1
    "\"Negative. I was not authorized by the Integrated Data Sentience Entity to interfere, only observe.\""
    show Yuki Right Neutral1
    show Haruhi Casual Worry1
    "That was an uncomfortable thought. \"And you remember it all?\""
    nvl clear
    show Haruhi Casual Quest2
    show Yuki Right Talk2
    "\"I remember it all.\""
    show Yuki Right Neutral2
    show Haruhi Casual Quest1
    "\"Wow. If you didn't do it, how did we get out of being stuck?\""
    show Haruhi Casual Quest2
    show Yuki Right Talk1
    "\"He did it,\" she answered, blinking. \"On the last loop, he did something he had not yet tried in any other iteration.\""
    nvl clear
    show Yuki Right Neutral1
    show Haruhi Casual Pout2
    "Realization dawned in Haruhi's eyes, and she winced. \"Seriously? His {i}homework{/i}? That's what did it?\""
    show Yuki Right Talk2
    show Haruhi Casual Pout1
    "\"It engaged your interest to the point where another loop did not occur,\" Yuki answered tonelessly."
    nvl clear
    show Yuki Right Neutral2
    show Haruhi Casual Pout2
    "\"So,\" she mumbled. \"That's why he was so worked up about it? Well ... I didn't know. If you hadn't been— But I guess, you were only following orders."
    show Haruhi Casual Unhap1
    "\"Well, now I know why you were frustrated. Is that why you made it so you never met me?\""
    nvl clear
    show Haruhi Casual Unhap2
    show Yuki Right Talk2
    "\"After this sequence, filming of the movie began. I observed that events here distressed him again.\""
    show Yuki Right Neutral2
    show Haruhi Casual Sigh2
    "\"Don't I know it!\" Haruhi snapped. \"That one ... I will never forget.\""
    nvl clear
    show Yuki Right Talk2
    show Haruhi Casual Focus1
    "\"In December, when he appeared to exhibit signs of further distress at the announcement of the SOS Brigade Christmas party, I determined the feeling to be mutual. Our situations had become sympathetic." 
    show Yuki Right Talk1
    "\"I incorrectly inferred that he and I shared insights and would both prefer a world where you would cause neither of us distress. Acting on my emotions in this manner was an error.\""
    nvl clear
    show Yuki Right Neutral1
    show Haruhi Casual Quest1
    "\"So, you mean, that time he was in a coma, he was actually in another dimension?\""
    show Haruhi Casual Quest2
    show Yuki Right Neutral2
    "After a heartbeat of hesitation, Yuki nodded."
    nvl clear
    show Haruhi Casual Pout2
    "\"Okay ... I guess. That seems like going overboard, though. Changing the entire world, just because....\" She swallowed and looked away, staring out the window."
    show Haruhi Casual Worry1
    "\"So, Kyon was really that upset with me?\""
    nvl clear
    show Haruhi Casual Quest2
    show Yuki Right Talk2
    "\"Possibly,\" Yuki said. \"I cannot guarantee my assessments are completely accurate. For example, acting on emotion and inferring his desires incorrectly.\""
    show Yuki Right Neutral1
    show Haruhi Casual Sigh1
    "\"Fine. In that case, it's now a priority. What can be done to make sure you won't commit another one of these 'errors'? Remember, I'm your boss now, so don't hold anything back!" 
    nvl clear
    show Haruhi Casual Pout2
    "\"Even if,\" she hesitated, forcing the words out, as uncomfortable and frustrating as it was, \"it means borrowing Kyon a little bit.\""
    show Haruhi Casual Pout1
    nvl clear
    stop music fadeout 2    

    call eyecatch_fancy("Sunday, April 17") from AO2_sc006

    play music "Music/WitchInGoldCenba.ogg"
    scene bg Cafe
    show Mikuru Casual Neutral1 at center
    show Kyon Casual Ser1 at right  
    show Koizumi Shrug Casual Sigh1:
        xalign -1.15 yalign 1.0    
    with fade    
    "\"It is related to what Fearless Leader is trying to avoid admitting to himself,\" Koizumi said, glancing at Mikuru over his drink. "
    show Koizumi Think Casual Grin2 at left
    "\"And perhaps, Suzumiya-san as well. On that count I'm somewhat less certain.\""
    nvl clear
    show Koizumi Think Casual Grin1
    show Mikuru Think Casual Quest1
    "\"Avoid admitting?\" she asked, bewildered, looking between the two. \"What is it?\""
    show Mikuru Think Casual Quest3
    show Kyon Casual Sigh2
    "\"I have no idea what nonsense he's going to spout out right now,\" Kyon grumbled, lowering his face to rest on one hand."
    show Kyon Casual Sigh4
    show Mikuru Casual Quest2
    "\"Um ... what?\""
    nvl clear
    show Mikuru Casual Neutral2
    show Koizumi Think Casual Ser4
    "\"Well, as subordinates,\" Koizumi said suddenly, turning to Mikuru, \"we should work together, shouldn't we?" 
    show Koizumi Think Casual Ser2
    "\"The problem is this; as far as I understand things, Suzumiya-san has a certain ... interest ... in Fearless Leader.\""
    nvl clear
    show Koizumi Think Casual Ser1
    show Kyon Casual Sigh1
    "\"Please,\" Kyon interjected, \"stick with the old nickname.\""
    show Kyon Casual Sigh3
    show Koizumi Think Casual Grin2
    "\"Of course.\""
    nvl clear
    show Koizumi Think Casual Grin1
    show Mikuru Casual Sigh1
    show MBlush1 Casual
    "\"W...well, that's not too surprising,\" Mikuru said. She had trouble looking Kyon in the eyes and her face reddened, but she asked,"
    show Mikuru Think Casual Quest1
    hide MBlush1
    "\"But, Kyon-kun didn't notice when ... Suzumiya-san jumped on him in the clubroom?\""
    nvl clear
    show Mikuru Think Casual Quest3
    show Koizumi Think Casual Sup1
    "Koizumi blinked several times, then turned to stare at Kyon. \"Excuse me?\""
    show Koizumi Think Casual Worry1
    show Kyon Casual Worry2
    "\"Not what you think it was,\" Kyon said in irritation."
    show Kyon Casual Sigh1
    "\"She just wanted the last page of my story for the Literature Club anthology. I had hidden it because—{nw}"
    show Kyon Casual Puzzle1
    extend " You know, that's actually not important. Back to Haruhi?\""
    nvl clear
    show Kyon Casual Worry1
    show Koizumi Crossed Casual Smile3
    show Mikuru Casual Neutral1
    "\"Well, at any rate,\" Koizumi said, relaxing into his usual facial expression, \"I hope you know what you're doing, and I'm putting my faith in you, so please handle things carefully.\""
    nvl clear
    show Koizumi Crossed Casual Smile1
    show Kyon Casual Sigh3
    "Kyon bit back a retort, realizing that the esper was right." 
    show Kyon Casual Ser3
    "Staring into the mouth of the issue he'd been trying to defer, he asked, \"What do you think I should do, then? And please, say something more serious than the advice you gave me about last August.\""
    nvl clear
    show Kyon Casual Ser1
    show Koizumi Crossed Casual Sigh2
    "\"It's troubling,\" Koizumi acknowledged. \"For the time being, I can only ask you to be aware of it and hope that it can be dealt with reasonably." 
    show Koizumi Crossed Casual Ser2
    "\"Moving on slightly and changing the topic to equally pressing, but only partially related matters, how should I proceed with the Organization?\""
    nvl clear
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Ser1
    "Kyon tapped his fingertips on the table thoughtfully, falling silent while the waitress returned, setting down their orders and refreshing his coffee and Mikuru's tea."
    show Kyon Casual Ser2
    "After a bite of his club sandwich, once the waitress had moved on, he said, \"Alright. How much trouble could you really be in with them?\""
    nvl clear
    show Kyon Casual Ser3
    "\"You haven't done anything wrong in their eyes; I would be the problem. As long as things are in control, wouldn't they be okay with it?\""
    show Kyon Casual Ser1
    show Koizumi Think Casual Ser2
    "\"Possibly,\" the other boy allowed, picking at his salad. \"I believe that I will have to write another letter of apology, at the very least. But even so, my 'trouble'....\""
    nvl clear
    show Koizumi Think Casual Ser4
    "He shrugged. \"Being a double-agent seems unwise.\""
    show Koizumi Think Casual Ser3
    show Kyon Casual Sigh2
    "\"How about an official liaison?\" Kyon proposed. \"If events were beyond your control — you were outmaneuvered, effectively — wouldn't it be fine? And this gives your Organization direct access to the brigade.\""
    show Kyon Casual Ser2
    nvl clear
    "\"Being a liaison might remove you from some circles in your Organization to protect various secrets or whatnot." 
    show Kyon Casual Ser3
    "\"That means that Haruhi would be able to see it as you being a part of the brigade more than the Organization, which I think would probably satisfy her.\""
    nvl clear
    show Kyon Casual Ser1
    show Koizumi Think Casual Ser2
    "Koizumi nodded thoughtfully. \"Hmm, she would be happy about having a connection to a shadowy organization, so that may be true enough." 
    show Koizumi Think Casual Smile2
    "\"Well, thank you, vice commander Kyon, I will continue to put my trust in you.\""
    nvl clear
    show Koizumi Think Casual Smile1
    show Kyon Casual Sigh4
    "Nodding, Kyon turned to Mikuru, who had finished half of her pasta and was just toying with the noodles, curling them into complex whorls on the plate."
    show Kyon Casual Neutral2
    "\"Are you alright with this, Asahina-san? Aside from what Haruhi and your superiors say....\""
    nvl clear 
    show Kyon Casual Neutral3
    show Mikuru Casual Quest1
    "\"Ah,\" she gasped, sitting up straight and looking between the two. \"Um, well ... my ... superiors and Koizumi-kun's agency don't always see eye-to-eye,\" she said, shifting her shoulders." 
    show Mikuru Casual Hap1
    "\"But I don't mind working with him; Koizumi-kun is a nice person.\""
    nvl clear
    show Mikuru Casual Smile1
    show Kyon Casual Puzzle1
    show Koizumi Think Casual Grin1
    "Kyon blinked, turning a questioning glance at Koizumi, who chuckled slightly. \"Um, Asahina-san, I think you may have missed the question a bit,\" he said."
    show Kyon Casual Worry1
    show Mikuru Casual Ser1
    "\"Um, no,\" she disagreed, shaking her head. \"I think this is nice. There's more trust between us then there was ... and that's very likable.\""
    nvl clear
    show Mikuru Casual Sad2
    "\"I feel bad that I can't say more myself because of — of things that are classified,\" she said, grimacing." 
    show Mikuru Casual Ser1
    "Shaking her head again, she gave Kyon an earnest look. \"Koizumi-kun wouldn't have been able to speak of things like this so openly in front of me if it weren't for the changes that are happening.\""
    nvl clear
    show Mikuru Casual Ser2
    "\"Even Nagato-san will be able to speak freely if she wants to. Suzumiya-san may be upset now, but I actually believe that once she has some time to come to grips with ... everything we have to show her and talk to her about, she'll forgive us and be quite satisfied!\""
    nvl clear
    show Mikuru Casual Ser3
    show Koizumi Crossed Casual Ser2
    "\"Forgive us,\" Koizumi said, his smile fading. \"I think Kyon's quite ahead in her regard by that measure now.\""
    show Koizumi Crossed Casual Ser1
    show Kyon Casual Sigh1
    "\"First of all, it's not a race,\" Kyon said, pushing his empty plate towards the center of the table."
    nvl clear
    show Kyon Casual Ser3
    "\"Secondly, she gave you the option to stay in the brigade, so I don't think she actually holds anything {i}against{/i} you, no matter how upset she might be at the moment.\" He glanced to Koizumi, raising an eyebrow questioningly."
    nvl clear
    show Kyon Casual Ser1
    show Mikuru Casual Neutral1
    show Koizumi Crossed Casual Smile2
    "\"No more instances of closed space have been created yet,\" the boy said, smiling. \"And to be honest, the severity of the last one doesn't feel too intense yet.\""
    show Koizumi Crossed Casual Smile4
    show Kyon Casual Sigh2
    "\"Right. So, finally, if the vice commander armband means so much to you, you can keep it and tell Haruhi you lost it. It'll save me the humiliation of having to pin that thing to my sleeve during club meetings.\""
    nvl clear
    show Kyon Casual Sigh4
    show Koizumi Think Casual Smile2
    "Koizumi chuckled again, bowing his head to Kyon. \"In that case,\" he said, \"thank you, and I will do as you suggest. Though I think we both know that won't do more than slow her down.\""
    show Koizumi Think Casual Smile1
    show Kyon Casual Puzzle1
    "Kyon nodded his agreement. \"Unfortunately.\""
    nvl clear
    show Kyon Casual Worry1
    show Koizumi Crossed Casual Smile1
    "\"Well, I should be going to meet with my colleagues, and then I imagine I will have a very ... eventful meeting with my superiors,\" Koizumi announced, rising to his feet. \"I'll leave you two to discuss things as you see fit; don't worry about the bill. I'll settle it on my way out.\""
    show Kyon Casual Neutral3
    show Mikuru Casual Neutral1
    $ _window = True
    hide Koizumi with moveoutleft
    $ _window = False
    "Mikuru and Kyon nodded their thanks at the esper as he left, and finished their drinks in silence."
    nvl clear
    show Kyon Casual Neutral2
    "\"Did you want to talk here, or elsewhere?\" he asked her after setting down his empty coffee cup."
    show Kyon Casual Neutral3
    show Mikuru Casual Hap1
    show MBlush1 Casual
    "Smiling shyly, she suggested, \"Ah ... let's go for a walk.\""
    show Mikuru Casual Smile1
    nvl clear
    stop music fadeout 2

    call eyecatch_fancy("Sunday, April 17","Monday, April 18") from AO2_sc007

    play music "Music/ItsumoNoFuukei.mp3"
    scene bg hallway
    show Kyon Neutral3 at right
    show Haruhi Pout2 at TenthLeft
    show Hblush at TenthLeft
    with fade    
    "After class had finished, Haruhi restrained her pace to a sedate walk, keeping in step with Kyon. \"I should say one thing,\" she said quietly. \"I mean, honestly.\""
    show Haruhi Pout1
    show Kyon Neutral2
    "\"Sure,\" he said, not even glancing towards her. \"What's that?\""
    nvl clear
    show Kyon Neutral3
    show Haruhi Pout2
    "\"Um.... I guess, all things considered, I want to say thanks for always sticking with me, even when I caused trouble. I just wish you had told me about it beforehand! I mean, if you\nhad—\""
    nvl clear
    scene bg stairwell2 with wiperight:
        size (800,600)
    show Kyon Neutral3 at right
    show Haruhi Pout1 at TenthLeft
    show Kanae Wince1 at right with moveinright
    play sound "SE/impact.mp3"
    pause(0.01)
    play music "Music/Gekiretsu.mp3"
    show Haruhi Sup1 behind Kyon:
        xalign 0.6 yalign 1.0 
    play sound2 "SE/dashwacky.mp3"    
    show Kyon Unhap1 at left
    show Kanae Sup1:
        xalign 0.2 yalign 1.0 
    with move    
    "She cut off as they reached the stairwell, a smaller first-year student wailing an apology before her compact form slammed into Kyon, nearly throwing him down the stairs."
    show Kyon Ser1 Flip:
        xalign -0.2 yalign 1.0 
    "He spun and lunged, managing to save his balance just barely, hanging onto the semi-collapsed form of the other student."
    nvl clear
    show Kanae Wince2
    "\"Eeep!\" the girl managed, held upright for the moment by his grip. \"S...sorry, I— Oh! Sempai!\""
    show Kanae Wince1
    show Haruhi Ang6
    "\"A friend of yours?\" Haruhi asked dourly, leaning close to peer into Kyon's face. \"You sure seem close!\""
    nvl clear
    show Haruhi Ang3
    show Kyon Ang1 Flip
    "\"We've never met!\" he protested, looking away from the smaller girl's features. Something about her did seem eerily familiar. \"At least, not that I remember.\""
    show Kyon Ser1 Flip
    show Kanae Worry1
    "\"Ah,\" the girl whimpered, eyes fixing on Haruhi. \"Y...you're here, too?\""
    nvl clear
    show Kanae Unhap3
    show Haruhi Crossed Eyeroll2
    "\"Well, Kyon's memory may be bad,\" Haruhi decided, crossing her arms over her chest. \"But mine's not, and I absolutely don't remember meeting you before.\""
    show Haruhi Crossed Eyeroll1
    show Kanae Worry2
    "\"Er, I should go,\" the girl managed, squirming in Kyon's grip, {nw}"
    $ _window = True
    play sound "SE/lowswoosh.mp3"
    show Kyon Ang1 Flip:
        xanchor -0.2 xpos -0.7 yalign 1.0 
    show Kanae Worry2:
        xanchor 0.2 xpos -0.3 yalign 1.0
    with move
    show Haruhi Crossed Sup2
    $ _window = False
    extend "one foot accidentally tripping the boy from his precarious step, sending both hurtling down the stairs headfirst."
    nvl clear
    "Still hanging onto her shoulders, Kyon switched his stance as he fell, throwing himself down the stairs even faster, actually pushing off from the sides of the steps quickly enough to get his lower body underneath him before reaching the bottom."
    play sound "SE/impact.mp3"
    "Unable to stop his rush, he spun in place, clutching the girl to his chest and slamming his back into the wall of the stairwell, smacking his head and barely managing to maintain his grip."
    scene bg hallway with wiperightfast 
    "He collapsed weakly into a sitting position, the first year girl sprawled across his lap."
    nvl clear
    show Kanae Sup1 at center with wipeup
    $ _window = True
    "His wind knocked out, he was unable to keep her there for questioning as she squeaked out another, {nw}"
    hide Kanae with moveoutleft
    extend "\"Sorry, Sempai! I'll tell you later!\" before leaping to her feet and dashing away."
    $ _window = False
    show Kyon Pain1 at right with wipeup
    show Haruhi Worry1 at center with moveinleft
    "\"Hey, you okay?\" Haruhi asked, waving a hand in front of his face as he resumed breathing with a choked gasp. \"Now, what was {i}that{/i} all about?\""
    nvl clear
    show Haruhi Quest2
    show Kyon Sigh1
    "\"Not sure,\" he wheezed. \"Maybe she's a slider and knows different versions of us from a parallel universe.\""
    show Kyon Sigh3
    $ _window = True
    show Haruhi Hap3
    "Haruhi's eyes lit up. {nw}"
    hide Haruhi with moveoutleft
    extend "\"I'll meet you in the clubroom,\" she declared, vanishing after the smaller girl."
    $ _window = False
    nvl clear
    stop music fadeout 3
    show Kyon Sup2
    show Ksweat at right
    "\"I was ... kidding,\" {nw}"
    hide Ksweat
    show Kyon Sigh2
    extend "he groaned, rubbing the back of his head where it had hit the wall. There was no way he would catch up with her while recovering his breath." 
    play sound "SE/doorknock.mp3"
    show Kyon Sigh2 at center with move
    "Sighing, he trudged to the club room, knocking on the door before entering."
    nvl clear
    play sound "SE/dooropenslow.mp3"
    scene bg ClubroomRightDay with slowflashbulb
    play music "Music/Aruame.mp3"
    show Mikuru Maid Hap1 at center
    show MTray Maid at center
    show Kyon Neutral3 at right
    with dissolve
    "Mikuru was already dressed in her maid outfit, and smiled at him as he entered. \"Hello, Kyon-kun!\" she chirped. \"Tea will be just a minute.\""
    show Mikuru Maid Smile1
    show Kyon Smile6
    "\"Ah, thanks, Asahina-san,\" he said, smiling and rubbing at the spot on the back of his head that had hit the wall."
    show Kyon Smile1 with None
    nvl clear
    hide Mikuru
    hide MTray
    show YBook:
        xalign 0.0 yalign 0.0    
    with dissolve
    "He glanced over, glad to see Yuki in her traditional chair, flipping through the pages of another book. He read the title, 'A Stranger in a Strange Land', then took his seat." 
    hide YBook
    show Koizumi Crossed Smile1 at left
    with dissolve
    "Koizumi entered just as Mikuru finished brewing the tea."
    nvl clear
    show Kyon Neutral2
    "At a glance, he didn't seem more tired than usual of late, so Kyon hazarded, \"No new closed space so far today?\""
    show Kyon Neutral3
    show Koizumi Crossed Sigh2
    "\"An incident occurred around the first break period of the day,\" Koizumi replied, shaking his head."
    nvl clear
    show Koizumi Crossed Ser2
    "\"It was rather intense, and the Shinjin emerged rather quickly — but thankfully it was one of the indecisive ones, so we had a relatively easy time of it. I gather that Sasaki was brought up?\""
    nvl clear
    show Koizumi Crossed Ser1
    show Kyon Puzzle1
    "\"Haruhi asked if I was dating her,\" Kyon answered, accepting a cup of tea from Mikuru with a quiet thanks. \"Is it that obvious that mention of Sasaki was involved?\""
    show Kyon Worry1
    show Koizumi Think Ser2
    "\"No, just a likely explanation,\" the esper said, nodding thoughtfully. \"Shall we explain closed space to Suzumiya-san today, then?\" he asked as he turned to the game closet and pulled the go board and stones out."
    nvl clear
    show Koizumi Think Ser1
    show Kyon Ser3
    "\"Yeah. Right now that's the most dangerous thing,\" Kyon agreed. \"I don't think even Haruhi would intentionally try and use that as leverage for us to remove her limitations, so we should bring that up soon.\""
    nvl clear
    show Kyon Ser1
    show Koizumi Think Sup1
    "\"Oh? Was removing her limitations discussed?\" Koizumi's eyebrows shot up questioningly."
    show Koizumi Think Worry1
    show Kyon Neutral2
    "\"That's right. It was at lunch time.\""
    nvl clear
    show Kyon Neutral3
    show Koizumi Think Ser4
    "\"Very curious. I would have expected her to be irritated ... but even though I was paying especially close attention to her mood, I didn't feel any negative emotions at that time.\""
    nvl clear
    show Koizumi Think Ser3
    show Kyon Puzzle1
    "Kyon gave the esper a six stone advantage and raised an eyebrow of his own. \"How does that work?\" he asked."
    show Kyon Neutral2
    "\"I know you mentioned you were aware of her emotional state at one point, but I never learned the specifics.\""
    nvl clear
    show Kyon Neutral3
    show Koizumi Think Smile2
    "\"Only particularly intense emotions are felt,\" he answered, staring at the board and placing his first stone thoughtfully. \"Even then, it's frequently vague ... it doesn't give me any clue as to where she is, for example, just whatever intense emotion is there."
    show Koizumi Shrug Sigh1:
        xalign -1.15 yalign 1.0    
    "\"Naturally, this was quite awkward when I first was granted my powers, but I can usually tell my feelings apart from hers, now.\""
    nvl clear
    show Mikuru Maid Hap1 at center behind Kyon, Koizumi
    show MTray Maid at center behind Kyon, Koizumi
    with dissolve    
    "\"There, there,\" Mikuru said soothingly, patting Koizumi's shoulder consolingly as she set his teacup before him. \"I know how you must feel, Koizumi-kun.\""
    nvl clear
    show Mikuru Maid Smile1
    show Kyon Sigh1
    "Kyon held one hand out, palm facing towards the esper as though to deflect a beam attack. \"Koizumi, in retrospect my question was a mistake." 
    show Kyon Ang1
    "\"Please never clarify that last remark to me,\" he declared, dropping his hand to the board and absently placing a stone of his own."
    nvl clear
    show Kyon Ser1
    show Koizumi Think Smile2 at left
    "\"Haha, if that's your wish,\" Koizumi chuckled. \"Understood, vice commander. Before I forget, I would also like to thank you for your assistance last night, even with your remarkably ... dramatic entrance.\""
    show Koizumi Think Smile1
    show Kyon Neutral3
    "Without batting an eyelash, Kyon whisked the letter from his future self and a mechanical pencil from his bag on the table. {nw}"
    show Kyon Neutral2
    extend "\"What time did I arrive?\""
    nvl clear
    show Kyon Neutral3
    show Koizumi Crossed Neutral2
    "\"Hmm? It would have been at seven forty, almost precisely,\" Koizumi answered. \"How is it that you don't— Ah, a future instance of yourself?\""
    show Koizumi Crossed Neutral1
    show Kyon Sigh2
    "\"Seems I'll be pretty busy yesterday,\" he replied nodding."
    show Kyon Sigh4
    nvl clear
    hide MTray
    show Mikuru Think Maid Quest1
    "\"We're going back to yesterday?\" Mikuru asked, blinking in surprise. \"But yesterday you told me you were getting tired of time travelling!\""
    show Mikuru Think Maid Quest3
    show Kyon Neutral2
    "\"Did I? Just after six o'clock, right?\""
    show Kyon Neutral3
    show Mikuru Maid Quest1
    show MTray Maid at center
    "\"Um, that's right. Er ... is it alright for me to tell you that?\""
    show Mikuru Maid Quest2
    nvl clear
    show Kyon Neutral2
    "He scribbled another note on the paper. \"I should be fine with this,\" he sighed, putting the note away. \"Now, Haruhi ran off in search of—\""
    nvl clear
    play sound "SE/doorclose.mp3"
    play music "Music/YareYare.mp3"
    hide Kyon
    hide Koizumi
    hide Mikuru
    hide MTray
    show Mikuru Maid Quest1 at right
    show MTray Maid at right
    show Haruhi Hap4 at left
    show Kanae Sup1:
        xalign 0.2 yalign 1.0
    with dissolve
    "The door slammed open with a booming crash. {=loud}\"Caught her!\"{/=loud} {nw}" 
    $ _window = True
    show Kanae Sup1:
        xalign 0.8 yalign 1.4
    with move
    play sound "SE/impact.mp3"
    hide MTray
    $ _window = False
    extend "Haruhi cheered, shoving the first year student into Mikuru, who dropped her empty tea tray and barely managed to keep herself and the smaller girl from falling over."
    show Haruhi Hap5
    show Mikuru Think Maid Quest1 at right
    show Kanae Wince1
    "\"Eep,\" the first year girl squeaked, her face pressed into Mikuru's chest. \"Aaugh! I'm in trouble! Someone help me!\""
    nvl clear
    stop music fadeout 3
    
    call eyecatch_fancy("Monday, April 18","Sunday, April 17") from AO2_sc008
    
    play music "Music/MikurunoKokoro.mp3"
    scene bg ParkBench
    show Mikuru Casual Sigh1:
        xanchor 0.5 yanchor 0.5 xpos 0.225 ypos 0.72
        rotate_pad False
        rotate 15
    show Kyon Casual Worry1 at center
    with fade
    "Kyon looked at the slumbering form of Mikuru, leaning heavily against him on their usual park bench, not far from Yuki's apartment. {nw}"
    show Kyon Casual Puzzle1
    extend "\"Asahina-san?\" he called, not to the girl at his side."
    nvl clear
    show Kyon Casual Worry1
    show MikuruBig Smile2 behind Kyon at right with dissolve
    "\"Hehe, am I too predictable?\" the older version of Mikuru asked from behind him."
    show MikuruBig Smile1
    show Kyon Casual Sigh1
    "\"I suppose that may be the case,\" he agreed, shooting an annoyed glance over his shoulder. \"What do I need to do, then?\""
    nvl clear
    show Kyon Casual Sigh3
    show MikuruBig Hap3
    "\"Ah ... come on a walk with me,\" Mikuru said. \"A friend is waiting to take care of her as soon as we go.\""
    show MikuruBig Smile3
    show Kyon Casual Neutral2
    "\"Someone I trust?\" he asked."
    show Kyon Casual Neutral3
    show MikuruBig Hap1
    "\"I shouldn't say,\" she answered, smiling mischievously."
    nvl clear
    show MikuruBig Grin2
    show Kyon Casual Sigh2
    "\"Lovely,\" he sighed, climbing to his feet. \"Lead the way then, Asahina-san.\""
    nvl clear
    scene bg ParkPath with wiperight
    show MikuruBig Sad2 at Position(xanchor=0.5, xpos=0.33, yalign=1.0)
    show Kyon Casual Neutral3 at right
    with dissolve
    "Her smile faded a bit, and she frowned worriedly. \"Is Kyon-kun angry with me?\" she asked, seemingly to herself as she walked down the street, back towards the cafe he had just recently vacated."
    show MikuruBig Sad1
    show Kyon Casual Puzzle1
    "\"I just don't like how you treat your younger self,\" he muttered, falling into step beside Mikuru as they walked away."
    nvl clear
    show Kyon Casual Worry1
    show MikuruBig Ser2
    "\"I have to act within the guidelines exemplified by IATT bulletin 1147 concerning similarly important persons of significance,\" she answered, frowning. \"And respectfully, Kyon-kun, if my younger self didn't experience what she did, she could not have grown into me.\""
    show MikuruBig Ser1
    show Kyon Casual Smile7
    nvl clear
    "He jolted suddenly, looking at her sidelong and allowing a sad smile to come to his face. \"I never thought about that,\" he admitted."
    show Kyon Casual Sigh2
    "\"I suppose it's all predetermined events to you, then. And if no one else can....\" He sighed, shaking his head. \"Sorry. This probably has nothing to do with why you decided to speak to me.\""
    nvl clear
    show Kyon Casual Sigh4
    show MikuruBig Hap4
    "\"It's part of why I'm here,\" she countered. \"And no, our discussion here isn't predetermined.\""
    show MikuruBig Grin1
    show Kyon Casual Puzzle1
    "\"What does it mean to be predetermined, then?\" he asked, rubbing his chin. \"I'm guessing it's just if it's been recorded? As in, if there's no record, then the 'unknown' automatically becomes undetermined?\""
    nvl clear
    show Kyon Casual Worry1
    show MikuruBig Smile2
    "\"That's absolutely the case! I'm impressed at how quickly you grasped that.\""
    show MikuruBig Smile1
    show Kyon Casual Ser3
    "\"I get bad grades,\" he said flatly. \"I'm not an idiot.\""
    nvl clear
    show Kyon Casual Ser1
    show MikuruBig Hap1
    "Mikuru stuck her tongue out and mimed a blow to her own head. \"I don't mean to say that Kyon-kun isn't smart,\" she said, giggling apologetically." 
    show MikuruBig Hap4
    "\"I mean ... these are complex theories. Some can't even be expressed in words. But you understand the important and practical risks, even when you pretend you don't understand the foundations.\""
    nvl clear
    show MikuruBig Grin1
    show Kyon Casual Puzzle1
    show KBlush Casual at right
    "\"Now you're flattering me,\" he retorted, unable to keep some color from rising to his cheeks at her comment anyway. \"But, thanks.\"" 
    show Kyon Casual Worry1
    "It surprised him that he could easily speak to the adult Mikuru when he stopped to think about it."
    show MikuruBig Hap3
    "\"Anyway, I'm here to explain to you why you have authority over my younger self.\""
    nvl clear
    show MikuruBig Grin1
    hide KBlush
    show Kyon Casual Smile6
    "\"So, it runs out,\" he surmised, smirking at her. \"Since you don't seem to be my subordinate.\""
    show Kyon Casual Smile4
    show MikuruBig Wink
    "\"You're {i}my{/i} subordinate,\" she said with a wide wink."
    show MikuruBig Grin1
    show Kyon Casual Puzzle1
    "\"Am I?\" he asked, surprised. \"I thought we just happened to work together when it was required.\""
    nvl clear
    show Kyon Casual Worry1
    show MikuruBig Grinwink
    "\"Well ... I like to pretend,\" she said, sticking her tongue out again. {nw}"
    show MikuruBig Hap3
    extend "\"Truthfully, despite what my younger self told you, our theory of projection back into time ran into an unexpected complication." 
    nvl clear
    show MikuruBig Neutral2
    "\"That is to say ... if you consider moments to be flat portraits, like frames of animation or film, and we make a projection onto a single frame, it's fleeting, effectively non-existent.\""
    show MikuruBig Neutral1
    show Kyon Casual Sigh2
    "\"Now you've lost me,\" he mumbled."
    nvl clear
    show Kyon Casual Sigh4
    show MikuruBig Neutral2
    "\"After enough time, even a projected image leaves a mark.\""
    show MikuruBig Neutral1
    show Kyon Casual Neutral2
    "\"Like it's burnt into a projector screen?\""
    nvl clear
    show Kyon Casual Neutral3
    show MikuruBig Smile2
    "\"Aha! See? You understand! Even then, there could be other factors, such as Suzumiya-san herself ... but ultimately, even if it doesn't last forever, my younger self makes more of an impression on the timeline than I realized at the time.\""
    nvl clear
    show MikuruBig Hap4
    "\"In fact, it is this act, following your instructions and drawing even further into the local time planes that allow us to develop more advanced theories and better understanding of time travel.\""
    show MikuruBig Grin1
    show Kyon Casual Ser3
    "He nodded soberly. \"I'm not sure I understand that implicitly, but I believe I get the general idea,\" he allowed."
    nvl clear
    show Kyon Casual Ser1
    show MikuruBig Hap3
    "\"And so, I know you're a trustworthy person, and I'd know that even if it weren't predetermined.\""
    show MikuruBig Grin1
    show Kyon Casual Sigh1
    "\"I see,\" he said, frowning. \"I seem to have signed myself up for a lot of responsibilities this time around. Okay, I understand that I help you out ... or I will, at least.\""
    nvl clear
    show Kyon Casual Ser3
    "\"So maybe the 'why' is explained. I even know your motives ... but can you tell me anything about what will require whatever time travel is needed to demonstrate your theory?\""
    nvl clear
    show Kyon Casual Ser1
    show MikuruBig Ser2
    "\"Well ... I can break all kinds of classifications, but I have to say I shouldn't mention anything too specific,\" she said. \"If you do something, and then I tell you what that thing is before you've done it ... that can stress time and damage causality."
    show MikuruBig Neutral2
    "\"But I can tell you a little, something that doesn't break any rules because you've probably considered it already.\""
    nvl clear
    show MikuruBig Neutral1
    show Kyon Casual Neutral2
    "\"Other espers, that smirking bastard, and the Sky Canopy Domain?\" he asked."
    show Kyon Casual Neutral3
    show MikuruBig Worry2
    "\"And of course, Nagato's superiors,\" she added, biting her lower lip. \"There's a {i}very{/i} specific reason for us to disregard so many rules and give you carte blanche with time travel ... and it's not just because you can be trusted.\""
    nvl clear
    "\"Without the ability to define an event as predetermined, our precious discovery may never have come about. Our expanded realization could be taken away from us, because they pursue their own goals.\""
    nvl clear
    show MikuruBig Ser2
    "\"That being said, there's still the possibility of them changing our timeline and moving the future we live in into a parallel track ... something that may as well not even happen." 
    show MikuruBig Sigh1
    "\"So, you're trusted with this power to preserve our hopes and dreams. I apologize for putting so much responsibility on your shoulders.\""
    nvl clear
    show MikuruBig Worry1
    show Kyon Casual Ser2
    "\"It's only half the burden of dealing with Haruhi,\" he answered after a moment. \"But that does explain to me why it was even possible for us to defy them as much as we have. I didn't think they were as stupid as it seemed.\""
    show Kyon Casual Ser1
    show MikuruBig Smile2
    "\"Ah, see? You understand perfectly,\" she said brightly."
    show MikuruBig Smile1
    show Kyon Casual Puzzle1
    "\"Mmm. Is there anything you're allowed to tell me about the smirking bastard?\""
    nvl clear
    show Kyon Casual Worry1
    show MikuruBig Worry2
    "\"Ah ... that person.... He is not likable. But I can't tell you much because I don't {i}know{/i} much. To us, he is a criminal, someone attempting to divert the timestream, much like Nagato's superiors at the moment." 
    show MikuruBig Ser2
    "\"It would be quite troublesome if they were to join forces, but ... I shouldn't speak further of that.\""
    show MikuruBig Ser1
    show Kyon Casual Sigh2
    "\"Well,\" he said, shrugging. \"Is there anything else I {i}should{/i} know?\""
    nvl clear
    show Kyon Casual Sup2 
    play sound "SE/tiresquealFar.mp3"
    pause 1.5
    play sound "SE/CrashFar.mp3"
    "Down a distant street, he heard the squeal of tires on pavement, then a thunderous crash. He turned his head to look, but found his face being turned back by Mikuru's hand." 
    show MikuruBig Sad2
    "\"Pay no mind,\" she said, somewhat sadly. \"I'll give you something nice to go home and forget about this for now. Get plenty of rest tonight, okay?\""
    nvl clear
    hide Kyon
    hide MikuruBig
    show MKiss at center
    with dissolve
    "Before he could answer, she drew closer to him and his sense was swept away with the sensation of her lips touching his." 
    nvl clear
    scene black with fade
    "She released him with a giggle and pointed him down the road to his home, whispering, \"I've missed doing that with you, Kyon-kun.\""
    "By the time his senses recovered enough to try and question her, she had been long gone."
    nvl clear
    
    jump SF1
