#Chapter 8, Filler Arc

label Fi1:
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 008 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
    scene bg YukiRoomCenter with fade
    play music "Music/NagatoTheme.mp3"
    show Yuki Side2 at left 
    show Mikuru Cower Casual Sigh1 at TenthRight 
    show Kanae Night Worry1 at right behind Mikuru 
    with dissolve
    "Kyon woke on the floor again, peering up into the eyes of a familiar girl. This was practically becoming a habit, he decided, sitting up and glancing around Yuki's apartment. Mikuru was wearing pajamas, dazedly wobbling in a sitting position while Kanae patted her back. Yuki simply tracked his eyes with her typical level expression, though he thought he caught a hint of some concern in her gaze."
    nvl clear
    show Kyon Smile6 at center with dissolve
    show Mikuru Cower Casual Sigh2
    show Kanae Night Unhap3
    "He raised a hand to his right eyebrow, but unsurprisingly the injury had been fixed, the stitches already gone. \"Thanks, Nagato,\" he told her earnestly."
    show Kyon Smile1
    show Yuki Talk1
    "\"You were under the influence of a consciousness-altering drug,\" she said, blinking. \"When you did not respond to phone calls, I undertook emergency procedures and brought you here.\""
    nvl clear
    show Yuki Side1
    show Kyon Sigh1
    "\"Yeah, sorry about that,\" he said, grimacing. \"Ah, some trouble— I'll explain later. {nw}"
    show Kyon Neutral2
    extend "Thanks again for taking care of my injuries.\""
    show Kyon Neutral3
    show Yuki Side2
    "She paused, seeming on the verge of saying something ... but merely nodded."
    show Kyon Neutral1
    "\"You alright, Nagato?\""
    nvl clear
    show Kyon Neutral4
    show Yuki Talk1
    "\"I am fine,\" she answered smoothly. He was starting to suspect that she would say that no matter what the truth was, so gave her a considering stare."
    show Yuki Side1
    show Kyon Puzzle1
    "\"Are you sure?\""
    nvl clear
    show Kyon Worry1
    show Yuki SadTalk1
    "Her mouth opened, {nw}"
    show Yuki Sad1
    extend "then closed, and her head lowered slightly, the faintest furrowing of her brows showing deeper consideration. {nw}"
    show Yuki SadTalk2
    extend "\"...uncertain,\" she finally allowed."
    show Yuki Sad2
    show Kyon Neutral2
    "\"Do you want to talk about it?\""
    show Kyon Neutral3
    show Yuki Side Blink
    nvl clear
    "She blinked, straightening up and giving a minuscule nod. "
    show Yuki Talk2
    extend "\"Error-correction session is prepared. A higher than usual amount of junk-data was created earlier today.\" She paused, her pupils dilating the tiniest amount before she blinked again, adding, \"Error is likely to occur within five minutes. The session will also take longer to resolve.\""
    nvl clear
    show Yuki Side2
    show Kyon Neutral2
    "\"Fine,\" he said quickly. \"But, Nagato, I don't like the way you patiently wait for my okay to take care of yourself. This is important! If you need it to happen, I'm always willing to help you! I owe you much more than you ever let on....\""
    nvl clear
    show Kyon Neutral3
    show Yuki Side Blink
    "She blinked, and though she didn't physically react otherwise, he was certain some small amount of tension drained from her. "
    show Kyon Neutral2
    show Yuki Side1
    extend "\"Kanae-chan?\" he asked, looking at the other two girls. \"Asahina-san? Do you agree?\""
    show Kyon Neutral3
    show Kanae Night Hap2
    "\"Absolutely!\" Kanae replied without hesitation."
    nvl clear
    show Kanae Night Smile1
    show Mikuru Cower Casual Sup1
    "Mikuru blinked snapping out of her daze. \"Oh! Er, yes, of course!\" she agreed, looking a bit bewildered. \"Anything!\""
    show Mikuru Cower Casual Quest1
    show Yuki Talk1
    "\"...understood,\" Nagato allowed, the tiniest, nearly invisible hints of a smile touching the corners of her mouth before reality exploded away yet again."
    show Yuki Side1
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Thursday, April 21", "Friday, April 22") from Fi1_sc001
    
    scene bg TsuruyaFutonDay with fade
    queue music "Music/Morning.ogg"
    "He woke again, head reeling with the 'extended' session. He didn't want to think how much longer in 'relative time' he'd spent in training with Nagato. If the average session was a 'short' single year...."
    "Blinking, he realized he was staring at the ceiling of another unfamiliar room ... though details began to trickle back into place. Last night, he'd taken a bath with Tsuruya, though the blood loss from his injury kept him from reacting embarrassingly ... except to get very light-headed. He'd tried his best not to stare at the girl, but she was totally unabashed, completely uncaring. True to her words, she had scrubbed his back in return without hesitation, and then carefully washed his hair so he wouldn't get any shampoo or soap in his wound."
    nvl clear
    "After that, she'd led him to her room, where two futons had been set up side-by-side. He was wearing a light robe, one that matched Tsuruya's ... and evidently in the middle of the night at some point, she'd rolled over onto his futon and wrapped her arms around him. She slept with her hair done up in a pair of buns on either side of her head, probably so she wouldn't pull her hair when she shifted about."
    nvl clear
    "As he stared at her in bewilderment, his eyes tracking down to where her robe was left open by her slumbering movements— He quickly looked away, fighting down a surge of panic. Okay, light-headed from blood loss and following his future self's orders was one thing ... but this ... {i}this{/i} was the kind of thing that would cause Haruhi to level most of the city, and that was probably before closed space or her powers came into the picture."
    nvl clear
    #show Tsuruya Robe
    "\"Nyaa~!\" Tsuruya drawled, stretching, rubbing her cheek against his chest as she woke up. \"Mmm!\" she enthused, tilting her head up and languidly blinking at him with her eternally-present smile. \"G'mornin', Kyon-kun!\""
    nvl clear
    "\"Er.... Um, good morning, Tsuruya-kun,\" he managed as she sat up, releasing him. What should he say in this situation!? 'Thank you for last night?' Maybe something flattering? The words that actually spilled from his mouth were, \"Did you rest well?\""
    nvl clear
    "\"Pretty good!\" she said, pulling her robe closed the rest of the way and climbing to her feet to stretch again. \"Though, I had a funny thought that Kyon-kun suddenly vanished last night.\" She frowned, touching one fingertip to her lower lip and pondering. \"Maybe a dream— Ah! Kyon-kun! Your bandage is gone!\""
    nvl clear
    "\"Er, I'm a quick healer,\" he assured her, touching a fingertip to where the stitches had been and climbing to his own feet."
    "\"Ooh!\" she enthused, grinning brightly and leaning close to stare at the spot where his injury was. \"Mega-awesome healing factor,\" she cheered. \"I'm glad! I'd feel all kinds of bad if you got really hurt taking care of mes!\""
    nvl clear
    "\"Aha,\" he chuckled, scratching the back of his head before he was nearly doubled-over by a sharp pain and a simultaneous gurgling noise from his stomach. \"Ugh,\" he wheezed, wincing. \"So ... hungry....\""
    nvl clear
    "\"No problem!\" Tsuruya said, as brightly as ever. She traipsed to the door and slid it open a crack, calling out, \"Heyas, make a nice big breakfast for me and Kyon-kun, okies? Ooh, also, are his clothes clean?\""
    nvl clear
    "She nodded at someone he couldn't see through the doorway and took a bundle of cloth into her arms, sliding the door shut with one foot then spinning around and presenting it to him. He accepted it, realizing it was his school uniform. Humming to herself, Tsuruya went to one of the seemingly identical panels around the room and slid it to one side, revealing a dresser. She nonchalantly collected her underclothes and school uniform for the day and dropped her robe to the floor."
    nvl clear
    "He quickly spun away, too self-conscious to do the same, pulling his boxer shorts on before dropping the robe to the floor and dressing. To his surprise, even his tie had been washed. He spent a long moment consulting the emergency reference card he left in his wallet to correctly re-knot the tie, and turned around just as Tsuruya was letting her hair down. She glanced back at him, smiling as he finished adjusting his tie."
    nvl clear
    "\"Onwards to breakfast!\" she declared, seizing his wrist and hauling him through the doorway, into the rest of the house."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22") from Fi1_sc002
    
    scene bg TsuruyaKitchen with fade
    queue music "Music/MegassaKoukishin.mp3"
    show Tsuruya Hap1 at right 
    show Kyon Neutral3 Flip at TenthLeft 
    with dissolve
    "After eating enough sumptuous fare to feel like a total glutton, Kyon was somewhat surprised to see that Tsuruya had eaten just as eagerly. \"Ah, good, good,\" she decided, leaning back and patting her stomach. \"Mmm, school isn't for a bit, did you want to walk the grounds with me before it starts?\""
    nvl clear
    show Tsuruya Smile5 
    show Kyon Neutral4 Flip 
    "He thought back to the flower viewing ... the Tsuruya estate did have some very nice trees; he could only imagine it took an army of gardeners to manage. {nw}"
    show Kyon Unhap1 Flip
    extend "\"Actually,\" he realized with a wince, \"I'm supposed to meet with Haruhi at the clubroom early — I need to study for a test today.\""
    show Tsuruya Hap5
    "\"Okies!\" she said brightly. \"I'll go with yous! Sound good, nyoro~?\""
    nvl clear
    show Tsuruya Smile2
    show Kyon Neutral2 Flip
    "\"Shouldn't be a problem,\" he agreed after mulling it over. She beamed him a smile and they left her estate together on foot after she had summoned a pair of bentos as though by magic, snapping her fingers and having a maid scurry into the room to offer them."
    scene bg TsuruyaHouseDay with fade
    show Kyon Puzzle1 at TenthLeft with dissolve
    nvl clear
    "\"You know, Tsuruya-kun,\" he remarked with a sidelong glance at her, \"I'm worried Haruhi might get the wrong idea if she hears that I stayed with you last night.\""
    show Kyon Worry1
    show Tsuruya Laugh1 at right with dissolve
    "\"Ah, Haru-nyan's not going to mind,\" she replied cheerfully. \"You were a perfect gentleman, and I'll gladly tell her sos!\""
    nvl clear
    show Tsuruya Smile4
    show Kyon Unhap1
    "\"Um,\" he managed, wincing. {nw}"
    show Kyon Neutral2 
    extend "\"Well, Haruhi aside, while we've got some relatively private time, do you mind if I ask you something?\""
    show Kyon Neutral3
    show Tsuruya Quest1
    show TBlush at right
    "\"Ooh?\" Tsuruya mused, blinking quickly, her cheeks taking on a pink tinge. \"What's that, Kyon-kun?\""
    nvl clear
    stop music fadeout 1
    scene bg TownLeft with fade
    show Kyon Neutral3 at TenthLeft
    show Tsuruya Quest2 at right
    show TBlush at right
    with dissolve
    show Kyon Puzzle1
    queue music "Music/MysteryTime.mp3"
    "\"Those yakuza saw us yesterday ... and they seem pretty mad about last Sunday. So, we're probably going to see more of them — and that's really going to hurt us.\" He shook his head. \"I'm not sure about myself, but Manabe said your name, too. Since we just left them all behind, he probably told them everything he knows about us.\""
    nvl clear
    show Kyon Worry1
    hide TBlush
    show Tsuruya Neutral1
    "\"That's true,\" Tsuruya murmured, gazing upward thoughtfully, her blush fading. \"Well, yous should be okay; they won't get anything but your nickname, anyway. As for me, well, I've got Kyon-kun right now! But what's the question?\""
    nvl clear
    show Tsuruya Neutral2
    show Kyon Ser3 
    "\"This is the yakuza,\" Kyon said, shaking his head. \"My mom's giving me grief just because she thinks I'm behaving like a delinquent anyway ... I think her speech was about letting the police handle things like they were supposed to, and staying out of trouble when I can. I don't want to be a quitter, but do you think we should maybe ... leave this to the professionals?\""
    nvl clear
    show Kyon Ser1
    show Tsuruya Sad1 
    "Tsuruya's smile vanished as she slowed to a halt, staring at her feet. \"I'm not allowed to give up,\" she said quietly. \"Um.... I'm not really supposed to talks about things like this, but I trust Kyon-kun, so....\" {nw}"
    show Tsuruya Ser1
    extend "She looked up and fixed her eyes upon his sharply. \"I can't ask you to keep going if you needs to stop. I didn't mean for Kyon-kun to be hurt, or get in trouble....\" "
    nvl clear
    show Tsuruya Ser2
    "She bit her lower lip, her extended fang making the expression a tiny bit silly. {nw}"
    show Tsuruya Ser1
    extend "\"So.... My family is ninkyo dantai, too.\" He blinked, vaguely recognizing the term that he had once heard yakuza called themselves, which literally meant, 'chivalrous organization'."
    nvl clear
    show Tsuruya Neutral1 
    "Clearing her throat, she gazed upwards and added, \"The police call us 'boryokudan'.\" He nodded, recognizing that to mean, 'violence group'. \"I thinks my family is ninkyo dantai ... but those fellows from Sunday and last night ... they're part of the Sumiyoshi-rengo, and I thinks of them as boryokudan."
    nvl clear
    "\"My family is part of the Yamaguchi-gumi.\" {nw}"
    show Tsuruya Sigh2
    extend "She lowered her gaze to meet his before looking down and giving a solemn bow. {nw}"
    show Tsuruya Sigh1
    extend "\"Sorries, I don't let people knows about this, usually, but you deserve the truth.\""
    nvl clear
    show Tsuruya Sigh2
    show Kyon Worry1 
    "\"I see,\" he said, nodding hesitantly. Admittedly, his first thought on seeing Tsuruya's home was to wonder what kind of crimes her family must commit.... {nw}"
    show Kyon Neutral5 
    extend "\"Er, but, that doesn't change my perception of you, Tsuruya-kun,\" he added quickly. \"The Yamaguchi-gumi are the ones responsible for most of the relief and aid efforts after the Kobe earthquake, right? I agree with you; that's absolutely much more ninkyo dantai!\""
    nvl clear
    show Kyon Neutral4
    show Tsuruya Smile5 
    "Her smile returned easily, but more weakly. {nw}"
    show Tsuruya Hap8
    extend "\"This is my trials,\" she said, apologetically. \"To see if I'm a worthy heir.\""
    show Tsuruya Smile5
    show Kyon Neutral1 
    "Kyon blinked, realizing the severity of the seemingly innocent request the maid had relayed from the Tsuruya family head, and its genuine implications. \"You're not allowed to get help from within your family?\" he asked."
    nvl clear
    show Kyon Neutral4
    show Tsuruya Neutral1
    "She shook her head, her hair swaying behind her. \"Kasai was helping me,\" she said ruefully. \"Um, but don't you worries! I'll be okay!\""
    nvl clear
    show Tsuruya Neutral2
    show Kyon Neutral1
    "\"Well....\" He hesitated. Getting involved with organized crime ... his mother would {i}love{/i} to hear about that, he was certain. {nw}"
    show Kyon Neutral2
    extend "\"You'll be as okay as I can help you be,\" he decided. His future self had {i}still{/i} seen fit to get him involved. \"I never said I wanted to abandon you to face this on your own; I just said we might both consider getting out together. If that's not an option, well....\" What kind of man would he be to make her face this alone, advice from the future or not?"
    nvl clear
    show Kyon Neutral3
    show Tsuruya Laugh1 
    "Tsuruya's eyes lit up and she dropped her schoolbag, {nw}"
    show Tsuruya Laugh1 behind Kyon:
        xalign 0.52 yalign 1.0
    with fast_move
    show Kyon Sup3 Flip
    extend "flinging herself at him in a big hug. {nw}"
    show Kyon Neutral3 Flip
    extend "\"I'm so glad!\" she enthused, as he reflexively hugged her back. \"I'm not allowed to ask for helps for me, but I'll make sure your family is okay — even if I have to yell and scream, okies?\""
    nvl clear
    show Tsuruya Smile4
    "He glanced around at the other occasional passers-by, thankfully no other students from their school. {nw}"
    show Tsuruya Smile4 at HalfRight
    with move
    show Kyon Smile6 Flip
    extend "Patting her on the back as she released him, beaming a brighter smile than usual, he admitted, \"I wish I could say that you shouldn't do that ... but I don't want my family, or anyone else from the brigade to get caught up in this if we can help it, so ... thank you very much, Tsuruya-kun.\""
    nvl clear
    show Kyon Smile4 Flip
    show Tsuruya Hap7
    "\"Absolutely,\" she agreed, nodding. {nw}"
    show Tsuruya Quest1
    extend "\"Sos, in that case, would you be willing to come with me and meet my father?\" she asked, traces of anxiety showing in her eyes. \"Um, today after school, maybes, so we can make sure your family is safe?\""
    nvl clear
    show Tsuruya Quest2
    show Kyon Neutral1 Flip
    "\"Yes,\" he agreed, remembering his future self's message. What an idiot he was to assume it meant to take a {i}bath{/i} with Tsuruya; no wonder his future self was amused at how stupidly he had reacted. \"Of course, Tsuruya-kun.\" He prayed silently that it wouldn't involve abandoning Haruhi, especially after how his mother had shaken the girl up the previous day...."
    nvl clear
    show Kyon Neutral3 Flip
    show Tsuruya Neutral1 
    "\"Is that why your wushuu was weaker?\" Tsuruya mused. \"You couldn't fights because you were worried about your family?\""
    show Kyon Smile6 Flip
    show Tsuruya Neutral2
    "\"Er, that's not ... quite it,\" he said, giving a weak smile of his own. \"But, I feel confident that I'll be much better at it the next time I have to fight.\""
    show Kyon Smile4 Flip
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22") from Fi1_sc003
    
    scene bg SchoolEntranceLeft with fade
    queue music "Music/Itsumo(Movie).mp3"
    show Haruhi Crossed Ang2 at right with dissolve
    "\"You're late,\" Haruhi growled, her expression dark. \"I've been waiting for you for five minutes already!\""
    show Haruhi Crossed Ang3 with None
    show Kyon Neutral5 Flip at center
    show Tsuruya Smile2 Flip at left 
    with dissolve
    "\"Sorry,\" he said, hanging his head. \"Um, something came up.\""
    show Kyon Neutral4 Flip
    show Tsuruya Hap5 Flip
    "\"Totally not Kyon-kun's fault!\" Tsuruya chirped from his side. \"I was keeping him with top secret research for our investigation!\""
    nvl clear
    show Tsuruya Smile2 Flip
    show Haruhi Crossed Quest1
    "\"What are you two doing together so early in the morning?\" Haruhi wondered, leading the way towards the school building."
    show Haruhi Crossed Worry2
    show Tsuruya Hap3 Flip
    "\"Oh! Kyon-kun helped me out last night for our investigation,\" Tsuruya explained, grinning. \"He got a bit beat up — my fault! More pushy fellows. I made him stay over to mend his wounds.\""
    nvl clear
    show Tsuruya Smile2 Flip
    "That made perfect sense, Haruhi thought. Then realization struck her. {nw}"
    show Haruhi Sup2 Flip
    extend "\"Kyon!\" she yelped, spinning to face him. \"What about your mother!? She'll flip out if—\""
    show Kyon Smile6 Flip
    show Haruhi Unhap2 Flip
    "\"Asahina-san helped me on that count,\" he said, shaking his head. \"My, uh ... uncle ... stayed in my room last night anyway. So, really, Tsuruya-kun was just helping me keep my mom from seeing how banged up I got.\""
    nvl clear
    show Kyon Smile4 Flip
    show Haruhi Unhap1 Flip
    "\"And you're not hurt?\" she asked anxiously, looking him over for obvious bandages."
    show Haruhi Unhap2 Flip
    show Kyon Puzzle1 Flip
    "\"Yeah, Nagato took care of that,\" he mumbled, glancing at Tsuruya worriedly."
    show Kyon Worry1 Flip
    show Tsuruya Hap2 Flip 
    "\"You know,\" Tsuruya mused, seemingly oblivious, \"Kyon-kun's uncle has the exact sames voice? It's neat when families have hereditary traits!\""
    nvl clear
    show Tsuruya Smile2 Flip
    show Kyon Neutral2 Flip
    "\"Yeah, I was told I look just like my grandfather when he was my age,\" Kyon agreed. {nw}"
    show Kyon Neutral1 Flip
    extend "He suddenly grimaced, muttering, \"I hope that doesn't mean anything.\""
    show Kyon Neutral4 Flip
    show Haruhi Sigh1
    "Haruhi shook her head. \"Well, right now,\" she said, leading the way again, \"my primary concern is making sure that Kyon passes his test and stays in the brigade! So while I don't want to shut the investigation down, the test is more important.\""
    nvl clear
    show Haruhi Sigh3
    show Tsuruya Hap4 Flip 
    "\"Ooh! I wish I could help with that,\" Tsuruya said, shaking her head. \"Hum.... Well! I'll stay out of your ways for now! Haru-nyan, do you mind if I borrow Kyon-kun again today?\""
    show Tsuruya Smile2 Flip
    show Haruhi Unhap1 
    "\"Again?\" Haruhi asked, grimacing. \"Hmm.... The math test is after lunch, so I'd really like to make sure that he spends that time studying. I suppose after school should be alright, though I hope this doesn't keep up much longer.\""
    nvl clear
    scene bg LockersDayLeft with fade
    show Tsuruya Hap7 Flip at left with dissolve
    "\"Okies! I thinks we can finish our investigation by tomorrow ... maybe it might take a day or two longer?\" she pondered, gazing at the sky thoughtfully. \"Anyways, we're making really great progress! You'll be {i}mega{/i} happy with what we'll have for you when it's over, nyoro~!\" She blinked, turning her attention to Haruhi before they parted ways for their respective shoe lockers. \"Oopsie, I forgot to tell you where Kyon-kun and I met up for your receipt!\""
    nvl clear
    show Tsuruya Smile4 Flip with None
    show Kyon Neutral1 at right with dissolve
    show Haruhi Neutral1 Flip at center with dissolve
    "\"Receipt?\" Kyon asked, glancing at Haruhi {nw}"
    show Kyon Smile7
    extend "and smirking. \"Ah, don't worry, Tsuruya-kun, I'll tell her.\""
    show Kyon Smile4
    show Tsuruya Hap6 Flip 
    "\"Ah! Thankie, Kyon-kun!\" Tsuruya cheered, waving brightly before she twirled, her hair flaring behind her as she dashed away."
    hide Tsuruya with dissolve
    nvl clear
    show Haruhi Neutral2 
    "\"So—\" Haruhi asked, breaking off when she saw Kyon furtively try to hide a note from his shoe locker in his blazer pocket. {nw}"
    show Haruhi Quest1
    extend "\"Ah! What's that?!\""
    show Haruhi Quest2
    show Kyon Puzzle1 
    "\"Nothing,\" he lied quickly, pushing a small box deeper into his shoe locker and dropping his shoes to the floor."
    nvl clear
    show Kyon Worry1 
    show Haruhi Neutral1 Flip
    "\"Oh, okay,\" she said, nodding, then turning away to change her shoes. She calculated the few seconds it would take him to stash the box in his pocket, since his schoolbag was nowhere in sight, gambling that whatever it was, he wouldn't leave it behind where someone else might find it."
    show Kyon Smile2 
    show Haruhi Neutral1
    nvl clear
    "By the time she had changed her shoes and turned back, he had the almost-concealed smug expression of managing to pull one over on her. She pursed her lips, resisting the urge to smirk and give herself away."
    nvl clear
    
    scene bg ClubHallLeft with fade
    show Haruhi Hap2 at TenthLeft with dissolve
    "\"Anyway,\" she said, walking by his side on the way to the club room, \"what happened with Tsuruya-san yesterday? And when did she become 'Tsuruya-kun' to you?\""
    nvl clear
    show Kyon Smile7 at right with dissolve
    "\"Yesterday,\" he said, relaxing, one hand patting his left pocket. Well, that suggested her guess about where the box had gone was accurate. \"Or ... technically the day before. Part of the investigation; she said we should be more of equals, instead of sempai and kohai.\""
    nvl clear
    show Haruhi Hap1
    "\"And...?\" she prompted, poking his back with a fingertip."
    show Kyon Neutral1
    "He twisted away from the prod and gave her a sidelong glance. \"And what?\" he asked. \"I already met up with you after that. It's classified.\""
    show Haruhi Hap3
    "\"Just give me some non-essential details,\" she pressed. \"I'm dying to know what's going on!\""
    show Kyon Sigh1
    nvl clear
    "He shook his head resolutely. \"No,\" he insisted. \"You solved the mystery that Koizumi came up with last Winter with minimal clues.\""
    show Haruhi Unhap1
    "\"Bah! Well, you still need to tell me where you were yesterday.\""
    nvl clear
    show Kyon Neutral1
    "\"I do?\""
    show Haruhi Smile3 
    "She nodded vigorously. \"Of course you do,\" she insisted. \"Tsuruya-san is under strict orders to account for all of her Kyon usage until this investigation is complete!\""
    show Kyon Puzzle1
    nvl clear
    "\"Um.... Well, we went to a really bad section of town and had a ... dispute with four....\" He trailed off, squinting, {nw}"
    show Kyon Smile3
    extend "then smiled, nodding. \"Four very pushy fellows. Yeah, that's how she would put it.\""
    show Haruhi Neutral3
    "\"Where did she meet you?\" she pressed."
    show Kyon Sigh2
    nvl clear
    "\"Downtown,\" he said with a shrug. \"I got a voice mail to help her out just after we split up at the train station.\""
    nvl clear
    
    scene bg ClubroomRightDay with fade
    show Kyon Sigh2 at right 
    show Haruhi Hap4 at TenthLeft
    with dissolve
    "She nodded, then unlocked the door to the clubroom, swinging it open and gesturing him in. After she had set her bag on the table, she glanced back and frowned. \"I forgot to close the door,\" she noted, \"take care of that, huh?\""
    nvl clear
    show Kyon Sigh3
    stop music fadeout 1
    play music "Music/YareYare.mp3"
    "He scowled, halfway lowered into his seat, but nodded and rose, heading to the portal.  {nw}"
    play sound "SE/Impact.mp3"
    extend "With one swift lunge, she swept a kick at the back of his shins, causing him to stumble.  {nw}"
    show Kyon Sup1
    extend " \"What the hell—\" he tried to protest, before she shoved him to the ground  {nw}"
    hide Kyon with dissolve
    play sound "SE/Impact.mp3"
    show Haruhi Hap4 at center
    extend "and leapt atop him, straddling his back and wrestling to get at his blazer pocket."
    nvl clear
    show Haruhi Point Hap1
    "\"Fork it over!\" she demanded, unable to keep from grinning while she used her power to make {nw}"
    play sound "SE/doorclose.mp3"
    extend "the door slam shut."
    "\"Why— You— Haruhi!\""
    nvl clear
    "He was much more purposeful when he struggled, rolling his arms and shoulders, twisting about and trying to evade her grip. He'd gotten surprisingly stronger, too! Not that it mattered; she could tell he couldn't bring himself to use his full force against her. It was kind of cute, really, but still an easily exploitable weakness. His skill was troublesome though, so she found herself laying flat on his back, one arm snaking beneath him to wend into his blazer pocket."
    nvl clear
    show Haruhi Point Amuse1
    "\"You think you can keep something {i}else{/i} hidden from me?\" she growled."
    "She knew she was fighting a bit dirty, her breath tickling the back of his neck so he dare not jerk his head back and hit her face. When his lower body began to twist further, she managed to tangle her legs around his, though she felt the motion slide her skirt up ... well, that was why she had closed the door, and it wasn't like {i}he{/i} could see anything but the floor."
    nvl clear
    "\"Damn it, Haruhi! Let me go! It's none of your business!\" She rolled the tangled pair of them to one side to give herself better access to his pocket,  {nw}"
    play sound "SE/dooropenslow"
    extend "just as the door swung open again."
    show Mikuru Hap2 at right with dissolve 
    "Mikuru backed into the room, humming to herself and carrying a large box with a plastic handle across the top with both hands. \"Hello? Is someone here—\"  {nw}"
    show Mikuru Think Sup1
    extend "she began cautiously, turning around after she set down the box, her eyes widening in shock as she saw the tangled duo."
    nvl clear
    show Haruhi Point Hap1
    "Before she could yelp and run away as she had last time,  {nw}"
    play sound "SE/doorclose.mp3"
    extend "Haruhi made the door slam shut and demanded, \"Help me, Mikuru-chan! Come here immediately!\""
    show Mikuru Cower Nervous2
    "The time traveler boggled, slipping back a half step before the order reached her, and she shook her head. \"Y.... But.... What?\" she whimpered."
    nvl clear
    "\"Don't listen to her!\" Kyon pleaded, desperately grabbing Haruhi's wrist as it thrust towards the note, stopped so close her fingertips could touch the edge of the envelope. \"Help me, Asahina-san! Call in the J.S.D.F., or the police! I'm being assaulted! Get me pepper spray, a stun gun — {i}anything{/i}!\""
    nvl clear
    show Haruhi Point Scold2
    "\"Come here!\" Haruhi insisted, struggling, but unable to drive her right hand deeper into Kyon's pocket. Her left hand was flat against the floor, providing her leverage and balance. Kyon grunted and managed to roll to one side, able to bring both hands to bear against Haruhi, leaving their noses centimeters apart, her hand slowly being forced from its goal."
    show Mikuru Cower Nervous2 at TenthRight with fast_move
    nvl clear
    "With tiny, mincing steps, as though she had been ordered into a bonfire, Mikuru crept closer, flinching with each change in the struggle."
    "\"Don't ... let her ... get it,\" Kyon grated out, Haruhi's right wrist captured in his left hand. His right hand was on her shoulder, slowly lifting her up off him."
    nvl clear
    show Haruhi Point Ang1
    "\"No ... you ... don't,\" Haruhi growled in return, letting him push her completely upright as Mikuru drew in range, then grabbing the upperclassman's wrist and hauling her unceremoniously to collapse onto Kyon."
    hide Mikuru
    nvl clear
    "\"Kya~!\" Mikuru wailed, thrashing aimlessly, her chest mashed into Kyon's face. He struggled mightily, legs kicking, hands flailing as he was uncertain where to put them. \"S...Suzumiya-san! Why— AAH! K...Kyon-kun — n...not there — OOH!\""
    nvl clear
    show Haruhi Point Hap1
    "Ignoring the time traveler's protests for the moment, Haruhi reoriented herself and thrust her hand into Kyon's blazer again, fishing out the note with a victorious cheer. \"Haha!\" she cried, leaping away from Kyon and holding it overhead. \"Keep him pinned, Mikuru-chan!\" she encouraged, tearing open the envelope and unfolding the note within quickly."
    nvl clear
    show Haruhi Hap1
    "She scanned the first line with a wide grin: \"Suzumiya-san, this letter isn't for you. Shame!\""
    show Haruhi Unhap2
    "Her smile vanished and she scowled at the paper, which other than those clear words was covered with a sequence of probably meaningful symbols, but all she could decipher was a trail of squiggles, stars, and odd whorls and loops until the last line: \"And you should apologize to that Mikuru!\""
    nvl clear
    show Haruhi Sigh2
    "\"Oh, damn,\" she cursed, hauling Mikuru's whimpering form off Kyon.  {nw}"
    show Haruhi Smile3
    extend "\"Well, good work, Mikuru-chan!\""
    show Mikuru Cower Wince1 at right
    show MBlush Cower at right
    "Collapsing back into a kneeling pile, the upperclassman returned an incomprehensible series of sobs. Kyon sucked in a greedy breath, his eyes unfocused, then coughed, gasping to recover."
    nvl clear
    show Haruhi Worry1
    "\"Sorry,\" Haruhi added after a moment, frowning petulantly. \"It was still worth a try, though.\""
    show Kyon Sigh5 at left
    "\"I might have died happy,\" Kyon managed, dazed."
    show Mikuru Cower Nervous3
    stop music fadeout 1
    queue music "Music/TenderScenery.mp3"
    "Mikuru's crying subsided to mere whimpers. \"S...Suzumiya-san, why do you do this to me?\" she moaned. \"Are you mad at me? Did I do something wrong?\""
    nvl clear
    show Haruhi Neutral2
    "\"Don't be silly,\" Haruhi chastised her. \"It was a last-second plan to try and distract Kyon — you used your moe charms perfectly!\""
    #show Mikuru Cower Blink?
    "With a wide-eyed blink, the time traveler turned to stare at her, eyes still watery."
    nvl clear
    show Haruhi Unhap3
    "\"Ah, okay, okay,\" Haruhi allowed, wincing. \"I'm sorry, Mikuru-chan — but it was Kyon! Not some stranger this time, right?\""
    show Mikuru Cower Smile2
    "\"I...if it was Kyon, I don't mind so much,\" Mikuru agreed hesitantly, though she was still blushing and her face was marked with tears."
    show Haruhi Unhap1
    nvl clear
    "\"Arg! I just don't like being left behind!\" Haruhi stamped one foot angrily on the floor for emphasis. \"I should have known that time travelers wouldn't let me see anything I wasn't supposed to.\""
    show Kyon Unhap2 Flip
    "\"Damn it, Haruhi!\" Kyon protested, seeming to come back to his senses as he sat up and gave her a sharp stare. \"What was that all about!?\""
    nvl clear
    show Haruhi Neutral2
    "\"Oh, why are you complaining?\" she retorted. \"You had two very attractive girls all over you {i}and{/i} you got a face full of Mikuru-chan's bountiful assets!\"  {nw}"
    show Haruhi Eyeroll2
    extend "She narrowed her eyes and leaned towards Kyon. \"What, you think that was bad, or something?\""
    nvl clear
    show Kyon Neutral1 Flip
    "\"Er, well,\" he managed, suddenly deflated, before he shook his head and gave her a stern look.  {nw}"
    show Kyon Ser2 Flip
    extend "\"What about Asahina-san's feelings? Doesn't that strike you as being thoughtless to her?\""
    show Mikuru Cower Worry1
    nvl clear
    "\"It's ... okay,\" Mikuru managed, hunching in on herself where she sat on the floor. Her face reddened further and she stared intently at the space between her knees. \"Um, if it's Kyon-kun....\""
    show Kyon Neutral4 Flip
    "He stared at her, confused, obviously trying to puzzle things out."
    nvl clear
    show Haruhi Hap4
    "\"Right, see?\" Haruhi said insistently. \"Anyway, Kyon, you and {i}I{/i} were much closer than that.\" Which reminded her.... She spent a moment smoothing her skirt back down. \"Now, what's this letter mean, anyway?\" she asked, handing it to the boy."
    nvl clear
    show Kyon Neutral2 Flip
    "He remained sitting on the floor, puzzling over it briefly, then shook his head. \"It's not for you and one of us should apologize to Asahina-san,\" he told her."
    show Haruhi Eyeroll1
    "\"Well, I know {i}that{/i}. I want to know what the squiggles mean!\""
    nvl clear
    show Kyon Worry1 Flip
    "Shrugging, he offered the note to Mikuru. \"Um, Asahina-san, I'm really sorry about that,\" he added."
    "\"Notes,\" Haruhi declared, turning her attention to her schoolbag, while Mikuru hesitantly accepted the paper and scanned the message. Her notes were in the top, neatly organized, so she got those out. Where was Kyon's schoolbag, anyway? Had he brought nothing but a bento with him?"
    show Mikuru Quest1
    nvl clear
    "Mikuru hesitantly said, \"Um, I'm not certain, Kyon-kun ... it says you should go to the usual place you read your messages? Something will be waiting for you there? And you should take the box with you? What box?\""
    show Haruhi Unhap1
    "\"Make it quick,\" Haruhi ordered. \"You've still got to study!\""
    nvl clear
    show Kyon Sigh2 Flip
    "\"Yeah, yeah,\" he groused, rising to stand and helping Mikuru to her feet before striding into the hallway. \"Don't worry; I've got the box ... as long as it wasn't crushed earlier.\""
    hide Kyon with moveoutleft
    show Haruhi Unhap3
    play sound "SE/doorclose.mp3"
    nvl clear
    "\"Quick!\" she demanded again, as he closed the door. \"Man,\" she sighed, shaking her head and turning to Mikuru. \"That guy!\""
    nvl clear
    show Mikuru Sad2
    "\"He's ... not bad,\" Mikuru said hesitantly from her spot on the floor, looking up with watery eyes. \"Not at all!\""
    show Haruhi Sup1
    "\"Ack, turn the moe down!\" Haruhi protested. \"I have no idea how Kyon manages to keep himself from running off with you, but if you don't get that under control, I'll do it myself!\""
    nvl clear
    show Mikuru Cower Nervous1
    "Mikuru squeaked, leaping to her feet and rubbing at her eyes with her handkerchief quickly. \"N...no, no,\" she said quickly, shaking her head. \"I'll be good! I'm not getting in your way! Y...you shouldn't go too far like that!\""
    show Haruhi Unhap2
    "\"I hate that quitter's attitude,\" Haruhi grumbled, shaking her head, then glancing to the box that the older girl had left by the doorway.  {nw}"
    show Haruhi Quest1
    extend "\"Anyway, what's in the box, Mikuru-chan?\""
    nvl clear
    show Mikuru Hap2
    "\"Oh!\" Mikuru said, smiling already. \"Um, yesterday afternoon, Kyon-kun met me, um, hmm.... Not long after class got out, was it? He was waiting by the train station when I got off and he asked if I needed help with anything! I'd been putting it off for a while, but I decided that since Kyon-kun was there I'd get a new sewing machine!\""
    nvl clear
    show Haruhi Eyeroll1
    "Haruhi stared at Mikuru. \"You didn't think about the fact that he was supposed to be talking with his parents?\" she asked, pulling out her cell phone and texting Kyon."
    show Mikuru Quest1
    "\"Well...\" Mikuru began."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22") from Fi1_sc004
    
    scene bg hallway with fade
    queue music "Music/Nanika.mp3"
    "Kyon's 'usual spot' for reading notes found in the shoe locker was the boy's bathroom — last stall. If Mikuru didn't remember leaving him the note, it was obviously the older Mikuru who had left it. And the box that he hadn't found the time to open. He was just contemplating opening it when his cell notified him of an incoming text: \"You meet with Mikuru yesterday at her train station after school. You owe me big time!\""
    nvl clear
    scene bg SchoolBathroom with fade
    show Kyon Neutral2 Flip at left with dissolve
    "\"Thanks, Haruhi,\" he muttered at the message as he stepped into the unlocked stall, almost mashing his face into a very familiar chest again."
    show MikuruBig Hap3 at right with dissolve
    "\"I thought you said mine were bigger?\" the older Mikuru asked with a pout, undoing the top two buttons of her shirt. \"And look, the star-shaped mole — she doesn't have one of those, does she?\""
    nvl clear
    show Kyon Worry3 Flip
    "He blinked, staring at the cleavage in question before forcing his eyes up to meet hers. She was amused despite the pout, eyes narrowed in mirth, still dressed in the white blouse and miniskirt, though she was wearing outdoor shoes. His own indoor shoes were going to be ruined soon, he deduced. {nw}"
    show Kyon Sigh2 Flip
    extend "\"Lately,\" he said without preamble, \"it seems that every other thing that happens to me is right out of the pages of a poorly plotted ero manga.\""
    nvl clear
    show MikuruBig Quest1
    "She blinked at him in confusion. \"Ah ... I think we should start this conversation over?\""
    show Kyon Unhap6 Flip
    "He slapped himself, shaking his head to clear it. \"Yes,\" he agreed. \"Sorry. It's been a strange day— Make that week. Even by life-with-Haruhi standards. Um ... I'm guessing it's a critical issue if you're here?\""
    show MikuruBig Grin1
    stop music fadeout 1
    queue music "Music/Nichijou.mp3"
    nvl clear
    "\"A small thing,\" she said in answer, smiling at him again. \"But somewhat critical, yes.\""
    show Kyon Neutral2 Flip
    "\"Where do I start?\" he asked."
    show MikuruBig Smile3
    "She pointed at the box he was holding in his right hand. \"Open it up,\" she said."
    nvl clear
    show Kyon Neutral3 Flip
    "He shrugged and pocketed the cell phone, folding the box's lid back and peering inside. Other than some crumpled paper for padding, the only thing within was a wrist watch with a leather strap. \"Um, thanks,\" he said, lifting it out and staring at it. Who used a watch these days anyway? {nw}" 
    show Kyon Neutral1 Flip
    extend "Everyone could tell time with their cell phones, only children and folks like ... Mikuru.... \"Oh! Is this like the watch you wear?\" He turned his eyes to hers curiously."
    nvl clear
    show MikuruBig Hap3
    "She nodded brightly. \"That's right,\" she told him. \"You know we can't bring things back ... that's forbidden. But these work with modern technology from this era, so I wish it could be nicer, but it should still be useful for you anyway.\""
    nvl clear
    "Nodding, he put it on his left wrist after a moment of consideration, realizing that his cell phone would work for that, too.... Then again, he might need to shut his phone off at times, so having a backup would ultimately be for the best."
    nvl clear
    show MikuruBig Neutral2
    "\"Well, that's the critical thing at the moment,\" she said, nodding. \"Now, will you come with me?\""
    show Kyon Puzzle1 Flip
    "\"Er, okay,\" he agreed, nodding. \"But I'm not sure I understand...?\""
    show MikuruBig Grin2
    "\"Don't worry about it,\" she said, shaking her head and placing her hands on his shoulders. \"I'll show you. Now, close your eyes?\""
    scene 
    nvl clear
    scene bg Alley2Evening with fade
    show MikuruBig Grin2 at right 
    show Kyon Neutral1 Flip at left 
    with dissolve
    "\"Right....\" That familiar, unsettling lurch of time travel. When he opened his eyes, he was standing in an alley not far from a train station, the position of the sun.... He gave up trying to figure it out, remembering he had been given a watch for just that reason."
    nvl clear
    "\"Now we're back to yesterday, not long after school,\" he observed, marveling at the mechanical hands as they adjusted themselves to the present time, and the small digital display giving the day, month, and year corrected itself as well."
    "\"Exactly right!\""
    nvl clear
    show Kyon Smile3 Flip
    "\"Nice. Thanks, Asahina-san. I appreciate this. Does it do anything else?\" Very likely it let them track him, but considering he had no way to move through time on his own, that didn't bother him."
    show MikuruBig Hap3
    nvl clear
    "\"Hmm, well, this is where I leave you for today,\" she answered with a smile. \"You'll have to ask my younger self any other questions you might have. And I'm afraid that my identity is still classified to her.\" At his sharp look, she ducked her head slightly. {nw}"
    hide Kyon
    hide MikuruBig
    show MKiss
    extend "\"Okay, I'll give you something good to keep that secret....\" She trailed off with a giggle, closing in to plant another electrifying kiss on his lips. \"Now, take good care of that younger Mikuru~!\""
    nvl clear
    hide MKiss
    scene bg Alley2Evening with fade
    show Kyon Neutral5 Flip
    "\"Bwah,\" he managed, recovering his senses after she had gone — again. Some day, he resolved, he was going to point out that they hadn't had whatever first kiss she thought she was following up on."
    "It was a low priority item, but some day."
    "Absolutely."
    nvl clear
    scene bg TrainStation with fade
    show Kyon Neutral3 at center with dissolve
    "Still somewhat dazed, he wandered out of the alley and towards the train station. \"Right,\" he realized, seeing that the next train wouldn't be in for several minutes. He pulled his cell phone from his pocket and frowned. His other self would just be getting off at a different station with Kanae and Haruhi. He hadn't received any calls, but even so...."
    nvl clear
    "Scrolling through his phone history, he made an entry in the address book for Mori, then double-checked Tsuruya's before finding Koizumi and calling the esper up. \"Hello?\" Koizumi answered after a single ring. \"This is Koizumi!\""
    nvl clear
    show Kyon Neutral2
    "\"Hey, Koizumi,\" he greeted the other boy. \"Listen, would it be problematic if I were to call Mori-san and ask for a favor?\""
    "\"I ... don't suppose it would be problematic to speak with her,\" Koizumi said after a moment of thoughtful hesitation. \"But, what kind of favor?\""
    show Kyon Sigh2
    nvl clear
    "Remembering what Mori had mentioned in the car, he explained, \"I'm going to have the Tamaru brothers pulled from watching Asahina-san and moved over to watch Tsuruya-kun; she's going to need it.\""
    nvl clear
    "\"Um ... that's ... very delicate territory for the Organization, as I understand it,\" Koizumi began apologetically. \"I don't know that I could reasonably relay that request.... Er, that is, I can ask for you, but it seems likely that she would refuse to help.\""
    nvl clear
    show Kyon Sigh1
    "\"Hmm, you're probably right,\" he realized with a frown. \"Well, in that case, I have to take care of something else. Sorry for the trouble, but thanks, Koizumi.\""
    "\"No trouble at all!\" the esper assured cheerfully. \"If you need anything else, call me any time!\""
    nvl clear
    "\"I will,\" he promised, realizing that ironically enough, it would happen later that day...."
    "After disconnecting, he pulled up Mori's number and dialed it."
    "\"H...hello?\" she answered, sounding a bit unsettled. \"Sir?\""
    nvl clear
    show Kyon Puzzle1
    "\"Yeah, hey,\" he said, glancing around the train station, where a few other folks were having their own conversations with cell phones. \"This is a bit last minute, but I'm concerned about Tsuruya-kun. I need you to pull the Tamaru brothers from watching Asahina-san and have them keep an eye on Tsuruya-kun for me.\""
    nvl clear
    "\"H...how do you know who's on assignment?!\" she asked in response. \"How did you get this number!?\""
    nvl clear
    show Kyon Neutral2
    "\"Classified,\" he returned, dropping his volume and scanning for eavesdroppers. \"But trust me; if you don't do this, something could happen to damage the Organization's relationship with the most powerful ninkyo dantai family in town. If that's too much for you, just watch her and I'll take care of things myself.\" He reviewed what he had just said, and restrained the urge to slap himself again. Did he just say 'ninkyo dantai' aloud in public?"
    nvl clear
    "\"...very well, Sir,\" she grudgingly agreed. \"But this is all on your head if it goes wrong.\""
    show Kyon Sigh2
    "\"Yep,\" he agreed, hanging up and sighing before shutting off his phone."
    #Mikuru is apparently in her uniform right now, according to chapter 9.
    show Mikuru Quest1 at right with moveinright
    "\"Kyon-kun?\" a familiar voice from behind him asked in surprise."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Thursday, April 21") from Fi1_sc005

    scene bg TrainStation with fade
    queue music "Music/TenderScenery.mp3"
    show Mikuru Quest1 at TenthRight
    show Kyon Sigh2 Flip at left
    with dissolve
    "Mikuru stared in surprise, not expecting to see Kyon there when she reached her train station. She smiled weakly, tilting her head to one side. \"Is something wrong?\" she asked in concern, looking closely at his face. \"I thought you were going to speak with your parents? And what's that mark on one cheek?\""
    show Kyon Neutral1 Flip
    nvl clear
    "\"It's nothing,\" he assured her. \"I, uh ... slipped. Anyway, my father doesn't get home until late this evening, so, judgment has been delayed.\""
    show Mikuru Think Quest2
    "\"What about Suzumiya-san?\" she pressed, worried."
    nvl clear
    show Kyon Smile3 Flip   
    "\"Everything's taken care of,\" he said with a grin. \"Actually, I'm here to see you.\" Her heart gave a tiny excited lurch."
    nvl clear
    show Mikuru Think Sup1
    "\"M...me?\" she managed in reply, unable to meet his eyes. \"W...what's going on? Do we need to go somewhere? And when?\" she asked, looking around the train station. There were far too many people here.... There was a nearby alley that might be subtle enough, but she was a bit scared of the idea of walking into such a place so openly."
    nvl clear
    show Kyon Sigh2 Flip
    "\"Um, nothing like that,\" he said, shaking his head quickly and frowning. \"Man, I'm starting to depend really heavily on everyone.... That can't be good. {nw}"
    show Kyon Sigh5 Flip
    extend "Um, for today, I'm standing in for the Organization folks who usually watch over you,\" he explained, ducking his head slightly. \"I'm not much good at being a shadowy watcher, or whatever, so I thought I'd see if we could walk together, or if there was anything I could help you with.\""
    nvl clear
    show Mikuru Think Quest1
    "She had thought Koizumi's associates might have been tracking her, but she wasn't actually certain before. She tried not to think about it; she had Kyon's attention for the moment, not theirs. \"If Kyon-kun isn't too busy, there is something I could use help with,\" she said hesitantly. \"Um, it's a bit of shopping, if that's not too much trouble...?\""
    nvl clear
    show Kyon Smile3 Flip
    "He spread his arms in a shrug and grinned. \"If that's all you need, no problem,\" he assured her. \"I'd be glad to help you out. What are you looking for?\""
    nvl clear
    scene bg TownLeft with fade
    show Mikuru Smile2 at center
    show Kyon Smile4 Flip at TenthLeft
    with dissolve
    "She smiled softly and turned away, beckoning him to follow. He fell into step at her side with no hesitation, hands in his pockets casually. Trying to be a bit subtle about it, she looked at him sidelong. His uniform was nearly immaculate, as though he'd put it on and not even sat down for a day of school. Lately, he had seemed drained of energy, due to their recent late night training sessions with Nagato."
    nvl clear
    "After a minute of study, she realized he was walking slightly differently, shoulders a bit more relaxed, chin slightly higher. Other than the already fading mark across one cheek, he looked ... really good."
    "A part of her hoped that everyone around them got the mistaken impression they were a young couple out on a date."
    nvl clear
    "Her best chances at {i}that{/i} had derailed into a long explanation on her true self and the nature of time-planes, or 'important missions' from her superiors. While she was glad she could be as honest with Kyon as her conditioning allowed, it also bothered her the way his eyes had initially gone distant once she told him it was only because of Haruhi's presence that she was around."
    nvl clear
    "She resisted the temptation to take his arm in hers. At the moment, he seemed relaxed but energetic. She hadn't been feeling {i}quite{/i} as exhausted lately, and Kanae seemed to be holding up better, too.... But Kyon had an awful lot of energy left, for someone who had just finished a full day of school."
    show Mikuru Smile3
    "\"You seem livelier these days,\" she finally judged, giving him a happy smile. \"I'm glad for you!\""
    nvl clear
    show Kyon Sigh5 Flip
    "\"Some days are better than others,\" he agreed, nodding. \"Today might have its difficulties for me, but it's going pretty well for me just now.\""
    show Mikuru Quest1
    "\"I like that! It's very positive. Are you, um, working with Koizumi-kun's Organization, now?\" she asked, as the crowds near them thinned out, granting a small degree of privacy."
    nvl clear
    show Kyon Smile3 Flip
    "He smirked at something and shook his head. \"Not really,\" he replied. \"Some of our goals overlap. I'm all about the SOS Brigade — you know that.\""
    show Mikuru Sigh1
    "\"Really?\" she asked doubtfully."
    nvl clear
    show Kyon Sigh5 Flip
    "He glanced at her and removed his hands from his pockets, spreading them in a helpless shrug. \"Okay, you got me,\" he admitted. \"For me, it's the people who are in the brigade. Call it what you will; I'm a sucker for the anime cliche. You know, friends to the end, that kind of thing?\""
    nvl clear
    show Mikuru Smile1
    "She giggled, shaking her head. \"That sounds better,\" she agreed. \"What's wrong with that?\""
    show Kyon Neutral1 Flip
    "\"Mmm, nothing, I guess.\""
    nvl clear
    show Mikuru Neutral1
    "She shook her head again, giving him a smile before gesturing to a large storefront. The outside windows were filled with swaths of cloth, sewing supplies, and layouts of do-it-yourself clothing patterns. \"Um, I'd like to get some things from here.\""
    nvl clear
    scene bg FabricShop with fade
    show Kyon Neutral2 Flip at TenthLeft
    show Mikuru Neutral1 at TenthRight
    with dissolve
    "He raised an eyebrow, scanning around as they stepped inside. High shelves were covered with full bolts of cloth, and at a glance, he was the only remotely male figure in the entire store, aside from a mannequin in a heavy winter coat, obviously still up from the last sale, and overdue to be redressed or put into storage. \"Sure,\" he said, shrugging. \"This is stuff you know much better than I do, so I hope you don't mind if I just carry things for you?\""
    nvl clear
    show Mikuru Hap1
    "Embarrassingly enough, that was what she had wanted his help for more than anything else. \"That's no trouble!\" she assured him, leading the way to the back, where the sewing machines were. \"Do you think Suzumiya-san will mind if I keep a sewing machine in the club room? I wanted to get an over-locking sewing machine to make things faster than I can by hand, but my place is a bit crowded....\""
    nvl clear
    show Kyon Neutral5 Flip
    "He scratched his head, looking around at the display models. \"As long as you used it, I think she'd most likely approve of it,\" he said slowly. \"But, keep in mind, she'll also probably take it as an excuse to have you make even more costumes!\""
    show Mikuru Smile2
    "\"T...that's okay,\" she said, turning to examine one of the more compact designs. \"Um.... I'm ... allowed to learn all about current techniques for sewing, cooking ... that sort of thing.\""
    nvl clear
    show Kyon Neutral1 Flip
    "\"Allowed?\" he mused. {nw}"
    show Mikuru Sad2
    extend "She winced; that probably should have been classified. \"So, it's research for your superiors?\""
    show Mikuru Sigh1
    "\"A bit,\" she admitted, moving to the next model. \"They don't ... really think it's that important, but it's one of the things I'm allowed to do.\""
    nvl clear
    show Kyon Ser3 Flip
    "\"I don't like the way that sounds,\" he said after a moment. \"I understand that you have to be careful to make sure that predetermined events aren't altered, and things like that.... But at the extent where you can't do anything on your own?\""
    show Mikuru Ser2
    "\"The future can be very delicate,\" she mumbled, repeating the rhetoric she had been given herself so often. \"Personal indulgences should never jeopardize causality.\""
    nvl clear
    show Kyon Puzzle1 Flip
    "\"You're more like Nagato than I realized,\" Kyon mumbled, looking away."
    show Mikuru Think Sup1
    "\"What?! I don't....\" She bit her lip, staring at the floor. But he thought highly of the alien, didn't he? Surely he couldn't have meant it as an insult. \"How do you mean?\""
    nvl clear
    show Kyon Sigh2 Flip
    "\"Er, sorry,\" he sighed, rubbing at his temples. \"That was the wrong thing to say. You said once that you thought that Nagato envied you because she knew too much?\""
    show Mikuru Think Quest3
    "Mikuru nodded, finally settling on an economical over-lock sewing machine, and struggling to pull it free from the boxes around it."
    nvl clear
    "\"Let me,\" Kyon insisted, reaching over her and grabbing the plastic handle across the top of one of the boxes, lifting it easily one-handed."
    nvl clear
    show Mikuru Think Quest2
    "\"Ah, thanks,\" she managed. \"Um, even though it's different, I think I can understand why she's anxious. Sometimes, I do know enough about a mission's details, and knowing isn't much help — it can cause a lot of stress. In Nagato-san's case, wouldn't she know ... everything?\""
    nvl clear
    show Kyon Neutral3 Flip
    "\"Maybe, but that's not the point,\" he said, shaking his head. \"She doesn't, anymore. If you had the choice between knowing nothing at all, or knowing everything, and in either case you had to accomplish some goal, which would you prefer?\""
    nvl clear
    show Mikuru Think Quest1
    "\"Actually,\" she said hesitantly, \"I wouldn't mind knowing {i}nothing{/i}, if I was going to accomplish the goal anyway. In that case, wouldn't knowing anything just be a burden? If I was absolutely certain of success, then I would agree that ignorance is bliss. It's the uncertainty that bothers me so much.\""
    nvl clear
    show Kyon Neutral1 Flip
    "He blinked at her, his mouth dropping open slightly."
    show Mikuru Think Sad1
    "\"Ah, that sounds stupid,\" she said fretfully, looking away from his reaction. \"Um, I suppose it would be better to know everything?\""
    nvl clear
    show Kyon Neutral5 Flip 
    "\"N...no, you're absolutely right,\" he said, shaking his head. \"That's.... Wow.\" He shook his head again, then gestured down the aisle. \"That was an insightful and eye-opening observation, Asahina-san.\""
    show Mikuru Think Quest2
    "\"Was it really so helpful?\" she wondered."
    nvl clear
    show Kyon Neutral1 Flip
    "\"Yeah, as a matter of fact. But, anyway, the thing of it is this; you and Nagato are both severely limited by your abilities. Right now, she's separate from the IDSE, so she's got less restrictions than usual, but she's also in a lot of danger. I asked her ... you may remember ... during that endless August, if she'd ever done anything 'fun' for herself during the entire series of time loops.\""
    nvl clear
    show Mikuru Quest1
    "\"Of course she hadn't,\" Mikuru remembered. \"But, how is that like  {nw}"
    show Mikuru Sad1
    extend "... me?\" she managed, the implications sinking in. \"Oh ... well ... that's true, isn't it?\" She sighed, stopping before a bolt of fabric and running her fingers across it without seeing. \"I suppose in a way you're right,\" she said in a small, nervous voice. \"D...did you mean what you told me last Sunday? After Koizumi left and we were alone?\""
    nvl clear
    show Kyon Puzzle1 Flip 
    "He didn't meet her eyes. \"Well, you know me,\" he said, shifting his shoulders. \"After your dizzy spell?\""
    show Mikuru Quest1
    "Her face flushed, and she managed a nod. \"I don't know what came over me,\" she admitted. \"It seemed a familiar sensation, for some reason....\""
    nvl clear
    show Kyon Neutral2 Flip
    "\"Er, probably low blood sugar,\" he reasoned, nodding quickly. \"Best not to dwell on it.\""
    show Mikuru Neutral2
    "\"Perhaps you're right. Um, but I remember what you said, about ... making my own impressions in the world, and I wonder if it can really be done?\""
    nvl clear
    show Kyon Smile3 Flip
    "\"That's absolutely already happened,\" he returned, grinning. \"Say ... when we nailed that can to the ground?\""
    show MBlush1 at TenthRight
    "She nodded, her face heating up again."
    nvl clear
    "\"Well, even if you want to say it was me doing it, I never would have if you hadn't translated those instructions. Even though the initiative may have been provided by the future, without you, that event never could have happened!\""
    nvl clear
    show Kyon Smile4 Flip
    show Mikuru Quest1
    # show Mikuru Sup2
    "Sometimes, she thought, his relative ignorance of the mechanics of temporal physics made him something of an idiot savant. She could think of twelve laws that refuted his explanation, but they were all smashed aside by the reality that as far as she could tell, he was {i}right{/i}."
    nvl clear
    "It should have been impossible for the events that she had participated in last December, too.... Though, that recollection became immediately hazy every time she tried to focus on anything except for Kyon's injuries. And those ... she did not like to focus on at all."
    nvl clear
    show Mikuru Smile2
    "\"That's just what you said last Sunday,\" she said, smiling weakly. \"And, um.... That's what I want! I mean, I'm not ... very helpful, or reliable ... I'm nothing like Nagato-san, or even Koizumi-kun.... I'd like some day to be the Mikuru who rescues you, not the one who ... well.\" {nw}"
    show Mikuru Unhap3
    hide MBlush1
    extend "She sighed and hung her head."
    nvl clear
    show Kyon Sigh1 Flip
    "\"I'm not sure where you're going with this but I can tell you with absolute certainty that you're wrong,\" he said resolutely. \"You're much stronger than you give yourself credit for, especially to handle as much as you do without knowing the reasons behind it.\""
    nvl clear
    show Mikuru Hap2
    "\"You really think so?\" she asked hopefully, bringing her head up and nervously meeting his eyes."
    show Kyon Neutral2 Flip
    "He nodded, looking around the store. \"I know it. Um, anyway, you never seem very happy when you talk about your work. So, sorry if I was bothering you.\""
    nvl clear
    show Mikuru Smile2
    "\"It's no bother!\" she said, giving him a smile she didn't fully feel. \"I'm just always afraid I'll say the wrong thing and only say 'classified information' instead of something genuinely helpful.\""
    show Kyon Neutral1 Flip
    "\"Really?\" he mused. \"Over the last few days, I've come to develop a whole new level of respect for the phrase, to be honest.\""
    nvl clear
    show Mikuru Sigh1
    "\"There is a limit to the novelty,\" she said, shaking her head. \"You can't think it's fun to want to explain something to someone and be forbidden, do you?\""
    show Kyon Pain2 Flip
    "\"No,\" he admitted, grimacing again. \"I didn't think of that. Well, let's talk about something more cheerful?\""
    nvl clear
    show Mikuru Smile2
    "\"Okay,\" she agreed. \"What would you like to discuss?\""
    show Kyon Neutral2 Flip
    "\"Ah ... so, what else are you looking for here?\" he asked, glancing around."
    nvl clear
    show Mikuru Think Quest1
    "\"Um, some pattern paper, maybe?\" she mused. \"I'll need more pins ... and more cloth, for certain....\" She looked around the store again, trying to decide where she would go next. \"Um, or did you want to leave?\" she worried aloud, turning to look at him with concern. Making him spend so long listening to her speak of such things at a sewing supply store ... surely there were things he'd rather be doing with his time."
    nvl clear
    show Kyon Smile3 Flip
    "\"Hey, I asked if there was anything I could help you with,\" he told her, grinning. \"This is better than buying tea because of mysterious instructions or getting into another fight.\" {nw}"
    show Mikuru Sad2
    show Kyon Pain1 Flip
    extend "He winced when he caught her flinch at that remark. \"Ah, nevermind that,\" he said quickly, shaking his head. \"Suffice to say that I don't mind helping you at all.\""
    nvl clear
    show Mikuru Think Quest1
    show MBlush Think at TenthRight
    "She knew she should just thank him politely and finish her shopping, but she just couldn't forget what they had spoken of after parting with Koizumi that fateful Sunday, where Kyon had told Haruhi everything. She spent a long minute struggling with what she should do, feeling her face heat up as she dithered. {nw}"
    hide MBlush Think
    show Mikuru Think Sup1
    show Kyon Neutral1 Flip at center behind Mikuru with move
    extend "She practically leapt in shock when he tapped her shoulder, leaning towards her with concern in his eyes."
    nvl clear
    show Kyon Unhap2 Flip
    "\"You okay?\" he asked. His concern turned to irritation. \"More orders from the future?\""
    show Mikuru Sigh1
    show Kyon Neutral3 Flip at TenthLeft with move
    "\"N...no,\" she managed, shaking her head quickly. He relaxed visibly and she realized she had been running her fingertips over the same piece of cloth over and over for several minutes."
    nvl clear
    show Mikuru Think Quest1 Flip
    show MBlush Think Flip at TenthRight
    "\"J...just thinking,\" she said, taking the bolt — she didn't even know what it was, but if she didn't do something to distract herself from her embarrassment she was going to do something she'd regret. \"Could you carry this for me?\" she asked, not meeting his eyes."
    nvl clear
    show Kyon Smile6 Flip
    "\"Anything for you,\" he agreed. She wished and hoped she could ask him what he meant by that ... what the complete implications were. But she knew it was an impossible dream, and even if it {i}were{/i} possible, with Haruhi...."
    nvl clear
    scene bg TownLeft with fade
    show Mikuru Think Quest4 at TenthRight
    show MBlush Think at TenthRight
    show Kyon Neutral3 Flip at TenthLeft
    with dissolve
    "Mumbling a nervous thanks to the boy, she strolled around the store, unable to bring herself to speak on anything else for fear of causing what she knew would only be trouble later, while he struggled to strike up a conversation about anything. After buying far more cloth than she could ever feasibly need, and further burdening Kyon with it all, they finally left the store."
    nvl clear
    show Kyon Neutral1 Flip
    "\"Where next?\" Kyon asked, glancing at his wristwatch briefly."
    "\"Let's drop this off at my place,\" she said hesitantly."
    nvl clear
    scene bg MikuruRoom with fade
    show Kyon Neutral3 at TenthRight 
    show Mikuru Neutral1 at TenthLeft 
    with dissolve 
    "He nodded and followed her the three blocks to her studio, a single-room apartment not far from the train station. After letting him in, he kicked off his shoes and unburdened himself in the corner she directed, before he took a look around, studying her temporary home. She felt embarrassed, even though everything was neat and orderly. Her futon was folded away, she didn't have a television, and the only furniture of note was her desk and a second-hand kotatsu."
    nvl clear
    show Kyon Neutral1
    "Still, she had managed to behave so far. \"Well,\" he said, when the silence began to drag uncomfortably, only punctuated by a growling stomach, \"is there anything else I can help you with, Asahina-san?\""
    show Mikuru Hap2
    "Her resolve snapped, and she blurted out, \"Let me treat you to dinner to thank you!\""
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Thursday, April 21", "Friday, April 22") from Fi1_sc006

    scene bg ClubroomRightDay with fade
    show Mikuru Think Quest1 at TenthRight
    show Haruhi Neutral1 at TenthLeft 
    with dissolve
    "\"Um.... After he dropped off the sewing machine, he went home to speak with his father,\" Mikuru said, nodding."
    show Haruhi Unhap1
    "Haruhi studied the other girl thoughtfully, catching the nervous hesitation in her answer. She raised an eyebrow. \"Really?\" she asked. \"Is that all?\""
    nvl clear
    "Mikuru nodded quickly again, though Haruhi was certain she saw a sheen of nervous sweat on her forehead. Oh, yes, she decided, narrowing her eyes at the time traveler. Kyon was going to answer for this. The only way he could possibly be in two places at once yesterday was with time travel ... and that meant an abuse of power, despite all of his warnings to her. As soon as she figured out how he had time traveled without letting the brigade's only time traveler know."
    nvl clear
    
    jump Fi2
