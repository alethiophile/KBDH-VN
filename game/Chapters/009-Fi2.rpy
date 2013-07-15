#Chapter 9, Filler Arc

label Fi2:
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 009 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
    scene bg MikuruRoom with fade
    queue music "Music/MikurunoKokoro.mp3" 
    show Kyon Neutral3 at TenthRight
    show Mikuru Unhap2 at TenthLeft
    with dissolve
    "Kyon looked at Mikuru sidelong. She'd been acting a bit nervous the entire time they had been together ... which seemed mostly to be in keeping from the first time he had thought she had asked him out on a 'date', but too anxious for the week in February that two of her had existed simultaneously."
    nvl clear
    "It would have been nicer if she'd offered to cook for him, but given the relatively cramped conditions of her apartment, he could understand her reluctance to do so."
    show Kyon Neutral5
    "\"Um, sure,\" he said, rolling his shoulders and then stretching his arms, a bit stiff after all of the lugging he had done for her. Then he shook his head, \"No, wait — why do you have to treat me? Let me treat you.\""
    nvl clear
    show Mikuru Sad2
    "\"But....\" She sighed, looking downcast. \"That's no different than usual,\" she mumbled. \"So, um, please, let me treat you?\""
    show Kyon Sigh3
    "\"What do you mean it's no different?\" he asked, furrowing his brow."
    nvl clear
    show Mikuru Sad1
    "\"Er, that is ... um ... well, you always have to treat all of us,\" she explained, ducking her head. \"So, that doesn't seem fair. Please?\""
    show Kyon Sigh5
    "He loosed a weak chuckle and nodded. \"Alright,\" he agreed. \"If it's important to you, then I can't say no. Well, where should we go, then?\""
    nvl clear
    show Mikuru Quest2
    "\"Ah....\" She stared at him blankly, {nw}"
    show Mikuru Hap1
    extend "then giggled in embarrassment. \"I didn't even think of that, but, um ... do you like udon?\""
    show Kyon Smile3
    "\"Udon's good,\" he agreed. A bowl of noodles would hit the spot, even though from his perspective, it would be just before lunch ... had he not unexpectedly been taken back in time most of an entire day. \"You know a good place around here?\""
    nvl clear
    show Mikuru Hap2
    "She nodded brightly. \"I do! Ariyake-san has a shop just down the street, and I try and go at least once a week!\""
    show Kyon Smile6
    "\"Sounds good,\" he agreed, checking his watch. {nw}"
    show Kyon Neutral1
    extend "\"Um, did you want me to wait outside so you could change, or...?\""
    show Mikuru Smile1
    "\"You're in your uniform, too, so it should be fine, right?\" she asked, shaking her head."
    nvl clear
    show Kyon Smile4
    "\"True enough.\" He really had to stop getting caught in his uniform so much.... Even with the amazing bloodstain removal skills of Tsuruya's servants, something else that he tried not to think about too hard, he was going to wear it out long before the year was over. Possibly even before it was time to switch to summer uniforms, at the current rate."
    nvl clear
    # scene bg TownStreetEvening1 with fade
    scene bg TownCommercialDistrict_Evening with fade
    $ _window = True
    "He stepped out of the apartment first, and she closed and locked it behind them before giving him a bright smile and leading the way down the street towards a noodle stall."
    # scene bg Udon
    # with fade
    show Kyon Smile4 at TenthRight
    show Mikuru Smile1 at TenthLeft
    with dissolve
    $ _window = False
    "After they had taken seats on the stools beneath the curtain, the elderly proprietor greeted the girl like a long-lost granddaughter. She cheerfully introduced him by his nickname."
    nvl clear
    show Kyon Neutral3
    "\"Ah, is this the boy I've heard so much about?\" the old man asked, a dangerous glint in his eyes as he turned his gaze towards Kyon."
    show Mikuru Neutral1
    show MBlush1 at TenthLeft
    "\"Um, yes,\" she admitted, her face turning red as she looked down, unable to meet either gaze."
    nvl clear
    show Kyon Worry3
    "The old man gave a friendly chuckle, but his eyes looked even more menacing towards Kyon. \"Well, I'm sure he'll take good care of you!\" he said cheerfully, mouthing a silent, \"or else\" at the end. \"Now, what can I get you, Asahina-chan? And yourself, Kyon-san?\""
    show Mikuru Hap2
    "\"Um, my usual, please,\" she said, looking up. \"Oh, Kyon-kun, you should try the seafood udon — it's quite good, but usually too much for me!\""
    nvl clear
    show Kyon Neutral2
    "\"That sounds great,\" he managed in response, watching the old man warily. Not that he didn't understand the urge to protect Mikuru at any expense himself, but the old man didn't need to be creepy about it...."
    "\"Right away,\" the old man agreed. Before he set to work, he set a small tray of freshly steamed buns on the counter between them, adding, \"On the house for you and your date, Asahina-chan!\""
    nvl clear
    show Kyon Smile4
    "Kyon smiled, restraining the urge to cringe away from Mikuru's inevitable correction that they weren't on a date. {nw}"
    show Mikuru Hap1
    extend "\"Thank you!\" she said, her cheeks still pink with a blush as she gave Kyon a shy smile of her own."
    show Kyon Worry3
    "She was able to read the confusion on his face and leaned a little towards him when the old man turned away, whispering, {nw}"
    show Mikuru Hap2
    extend "\"I...it's okay to pretend just this once, right?\""
    nvl clear
    show Kyon Smile6
    "\"More than just this once would be fine with me,\" he said. He bit his tongue, then realized that his slip would be harmless; Haruhi would be eating with his past self at that moment."
    "No chance she would stumble across this! He was half tempted to add a comment that she didn't need to pretend, either, but she was so nervous there was no reason to alarm her."
    nvl clear
    show Mikuru Hap1
    "She brightened even further. \"I'm glad!\" she cheered. \"It only seems right that I pay you back for all the work you did for me today!\""
    show Kyon Smile4
    show Mikuru Smile2
    "He nodded thoughtfully, taking one of the still-warm buns and sampling it cautiously. No filling, but they were well-made, he decided."
    nvl clear
    "He watched the old man on the other side of the counter hum as he stirred and mixed various ingredients, and absently reached for another bun, freezing when he realized that Mikuru was doing the same, and their hands touched. {nw}"
    show Kyon Smile3
    extend " \"Ah, sorry,\" he said, chuckling."
    nvl clear
    show Mikuru Smile3
    "\"N...no problem,\" she assured him. For a heartbeat, it seemed as though she was going to say something else, before—"
    show Mikuru Ser3
    show Kyon Smile4
    "\"Your orders,\" the old man said abruptly, breaking the moment before it could progress and setting an over-sized bowl before each of them."
    "Why did Mikuru look briefly annoyed at the old man, Kyon wondered, as he offered his thanks and prepared to eat."
    nvl clear
    
    # scene bg TrainStation with fade
    scene black with fade
    "After walking Mikuru back to her apartment, Kyon agreed to meet with her again in the morning to help carry the sewing machine to school."
    "He wasn't certain how it would end up working out that she didn't seem to realize there were, at least temporarily, two of him at school at the same time."
    "...But it did let him correct the oversight of forgetting that while he had stayed at Tsuruya's — a haven for the temporally displaced — he had forgotten his schoolbag at home."
    nvl clear
    scene bg KitaguchiStationOutside_Evening with fade
    "He took a train back to Kitaguchi station, checked the watch that Mikuru's older self had given him and turned his cell phone on, pulling up his voice mail and leaving himself the well-remembered message from the previous night."
    "After a few minutes he figured out how to flag the message as 'new', and shut the phone off again. Another few minutes waiting in a dark alley with a reasonable view of the train station let him see his past-self swear loudly."
    "He couldn't help but chuckle at his past self's cursing when the voice mail was checked. \"I guess I can see why she does it,\" he said aloud, shaking his head. \"Still....\""
    nvl clear
    "Once he was certain his past self had turned the phone off, he turned his phone back on. Now he just had to go home, face his father's wrath, and take advantage of the extra time to study for tomorrow's test."
    "It was nice not needing to worry about fighting the yakuza that his past self would successfully deal with, or think too hard about the bath and bed he would share with Tsuruya."
    "Hard-earned, and well deserved, after all. He walked back home, hands in his pockets, wondering if he actually would receive any phone calls. He wouldn't need to make any, at least ... not until he had to call Tsuruya, anyway."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Thursday, April 21") from Fi2_sc001

    scene bg KyonKitchenLeft with fade
    stop music fadeout 1
    queue music "Music/Kokuhaku.mp3"
    #show Akane at left
    #show KyonDad at Right
    #with dissolve
    "His good mood was crushed almost instantly by the oppressive atmosphere inside the house when he opened the door."
    "After kicking his shoes off and hiding them, so his parents wouldn't ask why he was walking around in his indoor school shoes, he walked into the dining room, where his father was just finishing his dinner."
    nvl clear
    "Looking a bit worn from an arduous day at the office, the tired salaryman pushed the plate with the last few bites left on it away from himself."
    #show Akane _
    "Kyon's mother sat in the seat to his father's side, her eyes meeting his briefly in warning. \"Well,\" she said abruptly, rising from her seat. \"I'll leave you two to discuss things.\""
    nvl clear
    "With that, she strode to the stairway, causing his little sister to squeak in alarm as her eavesdropping location was discovered. Kyon's father took a deep breath and stepped back from the table, gesturing Kyon to follow him as he slowly walked back outside."
    nvl clear
    scene bg KyonHouseNight with fade
    #show KyonDad at left
    show Kyon Neutral3 at right
    with dissolve
    "Kyon obediently followed, maintaining a careful distance as his father glanced at the house's windows and then fished a pack of cigarettes from one pocket of his suit jacket. After lighting one of the sticks, the man gave his son a level gaze. \"So,\" he asked, \"is she worth it?\""
    nvl clear
    "For a long minute, he could only stare at his father and the glowing tip of the brand in his mouth. Was who worth it? Tsuruya, who had gotten him into the investigation? Kanae, who was just a bystander? Mikuru, who controlled the time travel that let him get into such a mixed up situation? Yuki, maybe, who had given him the training he needed to win the fight?"
    nvl clear
    "Or maybe Haruhi, who everything was centered around even if she wasn't — for once — really involved herself?"
    show Kyon Ser3
    "He didn't even know which girl it was about ... but then he realized it didn't matter; he already had the answer in every case. \"Absolutely,\" he swore."
    nvl clear
    show Kyon Neutral3
    "His father grunted wordlessly, then knelt and stubbed the remains of the cigarette out. \"Good,\" he decided. \"Okay, you just need to understand your mother's concern. She doesn't honestly demand much of you ... reasonable grades and a clean record. If you're going to get into trouble at school, you'd better make sure that your grades are a lot better.\""
    show Kyon Neutral1
    "He nodded. That wasn't terribly different from what his mother had said anyway. \"I understand.\""
    nvl clear
    show Kyon Neutral3
    "\"It's not too hard to make her happy,\" his father continued, putting his hands into his pockets and staring up at the sky. \"There's no way you could come home from school one day and announce that you had, say, rescued an heiress from rampant hoodlums and secured a position at her father's company. So, her point of view is that there's no future in fighting.... Well.\" The man shrugged."
    nvl clear
    show Kyon Neutral5
    "\"But it wasn't anything like that!\" Kyon protested. \"Ryuguu was attacking Kanae-chan — he pulled a knife on me! What was I supposed to do? I swear, I'm not going around looking for trouble.\""
    nvl clear
    show Kyon Neutral3
    "The man's eyes drifted down from the dim sky, and one eyebrow quirked up. \"Kyon-kun ... you're not a martial artist, or a samurai. I think it's good that you stood up for your classmate, don't get me wrong. But at the same time ... you can easily get in over your head.\""
    nvl clear
    "\"Neither your mother nor myself want to see you get hurt. And like any parents, we want you to be safe and happy. That may mean being a bit more cautious now, but when you're older and capable of having a real career, it will all be for the best, won't it?\""
    nvl clear
    show Kyon Puzzle1
    "\"I understand,\" Kyon said slowly."
    "His father snorted. \"But?\""
    show Kyon Neutral1
    "\"Well.... Uncle Keiichi never even went to college, and from his stories he was a real troublemaker in school, too, but he's got a career.\""
    nvl clear
    show Kyon Neutral3
    "\"Eh ... yes, but your uncle Keiichi also married a shrine maiden and most of his 'career' is funded by a Yakuza family,\" the man countered."
    "\"No offense to him, but your mother wouldn't have been born if it weren't for the fact his parents thought they could raise a better-behaved and more responsible child. He's a very eccentric character, and that's not a standard the rest of us should hold ourselves to.\""
    nvl clear
    show Kyon Sigh4
    "Even if uncle Keiichi lived in the country, Kyon couldn't help but think that he was probably one of the most popular people in his village; the townspeople routinely called him 'the magician of words'."
    "Obviously his grandparents on his mother's side didn't know what they were talking about. Weren't they both novelists? They probably spent more time paying attention to their writing than the world immediately around them."
    nvl clear
    show Kyon Puzzle1
    "\"I'm not sure I'm happy giving up the possibility of doing things differently and still being successful,\" he finally told his father."
    nvl clear
    show Kyon Worry1
    "The man grunted at that, nodding slowly. \"Fair enough,\" he allowed. \"Even so ... the point of this is that while you may pursue some slim chance, a solid education is a sure thing. Since it's not possible to know the future, your mother's primary concern is that you at least keep that one reasonable goal in sight, regardless of whatever else you do.\""
    nvl clear
    show Kyon Sigh4
    "Kyon sighed. Probably best not to mention the fact that he {i}had{/i} rescued a wealthy heiress, he was {i}already{/i} involved with a ninkyo dantai family, and as a matter of fact, at least until some time tomorrow morning, he {i}did{/i} know the future because he'd already {i}been{/i} there."
    nvl clear
    show Kyon Neutral5
    "\"So, if I'm like Haruhi and place first in testing this term, I can cause any trouble I want as long as it doesn't get me expelled?\" he said instead."
    nvl clear
    show Kyon Neutral3
    "His father blinked languidly, his lips quirking in a smile. \"I'm not sure about that,\" he said. \"But, if you place in the top ten, I'll help you get your license over summer break. How about that?\""  
    nvl clear
    show Kyon Smile6
    "He smiled weakly, realizing that the offer was only made because of a certainty that he would fall short. \"I'll hold you to it,\" he said, nodding. He may as well just ask Arakawa or Yuki for the lesson."
    show Kyon Smile4
    "\"So, we're understood that you'll keep your mother happy, or at least try your best?\""
    show Kyon Smile6
    "\"I'll try my best,\" he promised."
    nvl clear
    show Kyon Smile4
    "\"Good,\" the man said, reaching forward and clapping one hand on his shoulder firmly. \"Good. I'm glad we had this talk, Kyon-kun. Oh, also, since you brought your uncle up, your aunt Rika wanted to know if you'd be going up to visit for Golden Week.\""
    nvl clear
    show Kyon Sigh2
    "\"Better known as being strong-armed into day-care services,\" Kyon mumbled. {nw}"
    show Kyon Neutral2
    extend "\"I'm not sure yet.\" What would Haruhi have planned for the vacation?"
    show Kyon Neutral3
    "\"Well, if your grades go down, your mother will send you off anyway,\" the man warned. \"With nothing but study guides to keep you company. Good luck!\""
    nvl clear
    "Kyon nodded as his father went back into the house, then sat down on the porch and pulled his cell phone from his pocket. How long had he spent fighting the yakuza with Tsuruya? When had he passed out in the back of her limousine? He should have paid closer attention, he realized. Deciding it was close enough, he called and left himself another voice mail, then went inside to use the house's phone to call Tsuruya."
    nvl clear
    scene bg KyonHallway with fade
    show Kyon Smile6 at right
    show Nonoko Worry1 at left
    "Just after he hung up, he heard his sister's footsteps on the stairs, and she peeked at him cautiously around the corner. \"Hey,\" he said to her, realizing he hadn't actually seen her in over a day, from his perspective. He turned off his cell phone and flopped onto the couch. \"What's up?\""
    show Nonoko Worry2
    "\"Is Kyon-kun in trouble?\" she asked worriedly."
    nvl clear
    show Kyon Smile3
    "\"No more than usual,\" he assured her. \"I just got this really tough undercover job saving the world.\""
    show Nonoko Worry1
    "She padded into the living room to give him a skeptical stare."
    show Kyon Smile7
    "\"Haruhi's idea,\" he added. \"For Tsuruya-kun.\""
    nvl clear
    show Nonoko Hap1
    "Her skepticism faded, and she gave him a look of fierce determination, clenching one fist and nodding. \"Kyon-kun can do it!\" she said with complete conviction. \"For Haru-nee-san and Tsuru-nee-san, you'd better!\""
    show Kyon Sigh2
    "\"Don't I know it,\" he sighed, leaning forward to ruffle her hair."
    nvl clear
    show Nonoko Quest1
    "\"You took care of Yuki-nee-san when she was sick, right? Is she doing better now?\""
    show Kyon Neutral2
    "\"Yeah, actually. Well, anyway, enough relaxing for me. I've got a test to study for tomorrow.\" And he had to leave early to meet with Mikuru and help her carry the new sewing machine...."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Thursday, April 21", "Friday, April 22") from Fi2_sc002

    scene bg MikuruApartment with fade
    queue music "Music/Itsumo(Movie).mp3"
    show Mikuru Smile2 at TenthLeft
    show Kyon Smile4 at right
    with dissolve
    "After a night of rest that felt oddly unusual for not involving one of Yuki's training scenarios, he left early to reach Mikuru's place. According to his wristwatch he was exactly on time, and reached her apartment door just as she opened it, greeting him with another of the shy smiles she had adopted lately. What exactly was he going to say to her next Sunday, anyway?"
    nvl clear
    show Mikuru Hap2
    "\"Good morning, Kyon-kun,\" she said cheerfully. \"You don't think we'll be too early?\""
    show Kyon Puzzle1
    show Mikuru Smile2
    "He bit his tongue, remembering what Mikuru would be subjected to the second she reached the clubroom. \"Not too early,\" he managed."
    nvl clear
    scene bg TownStreetDay1 with wiperight
    show Kyon Smile4 at right
    show Mikuru Smile1 at TenthLeft
    with dissolve
    "They traded bags, her carrying his schoolbag, and him carrying the sewing machine and the large, heavier bag of cloth and assorted other sewing supplies. After they got off the train, walking up the hill, she added, {nw}"
    show Mikuru Smile3
    extend "\"It's nice to walk to school together, Kyon-kun. Thank you for helping me out.\""
    nvl clear
    show Kyon Smile6
    show Mikuru Smile2
    "\"No problem at all.\""
    show Mikuru Smile3
    "She pointed at an intersection as they passed it, remarking, \"I would usually meet Tsuruya-san there, if we walked together.\""
    nvl clear
    show Kyon Puzzle1
    "\"She's a good person,\" he replied, glancing at his watch and frowning. \"I'm glad she looks out for you.\""
    show Mikuru Quest1
    show Kyon Worry1
    "Mikuru gave him a puzzled smile. \"Are you okay?\" she finally asked. \"You've been acting worried all morning.\""
    nvl clear
    show Kyon Puzzle2
    show Mikuru Neutral2
    "\"Ah, well,\" he started, glancing up the hill and seeing Tsuruya's familiar hair swaying in the distance. Next to her, a boy without a schoolbag, just rounding a bend in the road.... And Haruhi would ambush them at the gates, followed by a brief chat at the shoe lockers. No doubt about it; he had to come up with a stalling tactic. What could he say?"
    nvl clear
    show Kyon Puzzle1
    "He stopped, setting down the sewing machine and the bag, then turning to face Mikuru. Her attention was nervously riveted to him, and while he still wasn't certain what he was going to do last Sunday, he was grateful for it. \"Listen,\" he said, without preamble, \"about Haruhi?\""
    nvl clear
    show Mikuru Sad2
    show Kyon Worry1
    "Her expression dropped. \"I haven't heard anything yet,\" she said, shaking her head with a vague one-handed gesture. \"Is something wrong?\""
    show Kyon Puzzle1
    show Mikuru Unhap1
    "\"Um, it's just.... When Haruhi goes too far, it's okay to tell her so.\""
    nvl clear
    show Mikuru Quest2
    show Kyon Worry1
    "She looked at him oddly and gave a dubious nod. \"I don't really understand, but I believe you, so okay,\" she agreed."
    "Somehow, that only made him feel worse."
    nvl clear
    scene bg LockersDayLeft
    show Kyon Neutral1 at right
    show Mikuru Neutral2 at TenthLeft
    with dissolve
    "After delaying her a short while, he stopped at the shoe lockers, still wearing his indoor shoes. He set down the sewing machine and said, \"I need to check for something in my classroom. I'll meet you back with the extra cloth here, or the clubroom. Is it okay if I leave the sewing machine here?\""
    nvl clear
    show Mikuru Smile3
    "\"Ah, you carried it all the way up the hill,\" she said, shaking her head. \"Um, I can carry it the rest of the way!\" She handed him his schoolbag, and he nodded his head in thanks to her before dashing immediately to the first floor washroom, just catching sight of the older Mikuru ducking inside."
    hide Kyon with moveoutright
    stop music fadeout 1
    queue music "Music/YareYare.mp3"
    scene bg SchoolBathroom with wiperightfast
    show MikuruBig Neutral1 at TenthRight with None
    show Kyon Neutral3 Flip at left with moveinleft
    show MikuruBig Sup3
    "She squeaked in alarm, still cute to his eyes when he understood her motives better."
    nvl clear
    show MikuruBig Sup2
    "With her wide eyes and balled fists held together beneath her chin, he still felt that urge to protect her. \"W...what...\" she began, looking confused. \"You shouldn't be here yet!\""
    show Kyon Neutral2 Flip
    "\"Long story,\" he told her, checking his wristwatch. \"Okay, so ... we have a few minutes?\""
    nvl clear
    show MikuruBig Worry2
    "\"How....\" She frowned. \"My past self remembers you being in the clubroom when she entered it. There shouldn't be two of you!\""
    nvl clear
    show Kyon Sigh2 Flip
    "\"Well, somehow it's become a predetermined event,\" he said with an apologetic shrug. \"You take me back to yesterday afternoon to meet your past self at the train station; this ends up sparing me a lot of trouble from my parents involving a fight with some yakuza, so I really don't mind.\""
    nvl clear
    stop music fadeout 3
    queue music "Music/MikurunoKokoro.mp3"
    show MikuruBig Ser2
    "\"The slow path?\" she mused, frowning. Her eyes went distant as she tilted her head slightly to one side, then sighed with a smile. \"It must be so!\" she decided, shaking her head a bit."
    nvl clear
    show MikuruBig Grin2
    "\"Um ... I don't have time to explain it right now, and it would be a bit suspicious for you to ask my younger self. Ah, I hate to ask you to rely on her even more, but perhaps Nagato-san could explain it to you?\""
    show Kyon Neutral1 Flip
    "\"Explain what?\""
    nvl clear
    show MikuruBig Hap3
    "\"Temporal displacement,\" she answered. \"Time travelers normally have a way to monitor their deviation from standard, but you're more of a passenger, so without your own TPDD to monitor such things....\""
    nvl clear
    "\"A...anyway! Since you're here, now, there's one thing I should tell you. Um ... this may be a lot to ask, but please don't rush back to Suzumiya-san?\"" 
    show MBigBlush1 at TenthRight
    "Her face took on a blush and she suddenly couldn't meet his eyes. \"It would be, um, awkward if you were to overhear certain things.... And it would go against the way I remembered events.\""
    nvl clear
    show MikuruBig Sup1
    "Her eyes suddenly widened. \"Oh, my! I hope that means you don't eavesdrop!\""
    show Kyon Sigh1 Flip
    "He wanted to face-palm, but instead made himself check his watch. Less than a minute; his past self was probably already in the hall headed towards them. \"Sometimes it sounds like you really want me to misbehave,\" he noted. \"It might be easier for both of us if you were more careful, Asahina-san.\""
    nvl clear
    hide MBigBlush1
    show MikuruBig Quest1
    "She adopted a clearly feigned look of surprise. \"You really think so?\" she asked."
    show Kyon Neutral2 Flip
    "\"You'll see in less than a minute,\" he answered dryly, stepping into a free stall and closing the door."
    nvl clear
    hide MikuruBig 
    hide Kyon 
    with dissolve
    show Kyon Neutral2 at right
    with dissolve
    "He heard Mikuru's older self hum thoughtfully as she stepped into the appointed meeting stall, and he held his breath when he heard his past self mutter about Haruhi."
    nvl clear
    show Kyon Smile2
    "There was no resisting the smirk at Mikuru's reaction to his past self's line regarding ero manga, though he spared a moment to despair his past self's ignorance. What if someone {i}else{/i} were hiding in the room? Mikuru's older self had only just arrived, after all, she hadn't had time to check either. After the unnerving clunking noise that signified his past-self's departure, he checked the other stalls ... but of course, they were empty."
    nvl clear
    scene bg ClubHallLeft with fade
    "In any case, he realized he wasn't likely to do such a thing again; he now knew to check. After glancing at his wristwatch again, he hustled quickly to the clubroom, still hauling the large bag of cloth for Mikuru. Was he supposed to eavesdrop, he wondered? Was that Mikuru's unsubtle hint? Pondering, his footsteps slowed as he approached the clubroom door."
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22", "Friday, April 22") from Fi2_sc003

    scene bg ClubroomRightDay
    stop music fadeout 1
    queue music "Music/HigekiNoHeroine.mp3"
    show Haruhi Eyeroll2 at TenthLeft
    show Mikuru Unhap2 at TenthRight
    with dissolve
    "\"Alright,\" Haruhi grumbled, after listening to Mikuru's rushed explanation of her meeting with Kyon. \"Alright, fine. So, Kyon offered to help you out, you dragged him with you to go shopping, used him as a pack-mule, and that's {i}it{/i}?\" she asked."
    show Mikuru Sad1
    "Mikuru nodded nervously. \"That's exactly it,\" she agreed. \"T...that's all!\""
    nvl clear
    show Haruhi Pout2
    "\"I'm disappointed in you,\" Haruhi told her upperclassman. \"Really, you told me that you {i}liked{/i} Kyon. And when the oblivious wonder drops a golden opportunity straight into your lap, you assign him to heavy lifting?! It's like you're not even trying!\""
    show Mikuru Think Sup1
    "\"T...trying?\" Mikuru asked, her eyes wide and confused. \"What?\""
    nvl clear
    show Haruhi Sigh1
    show Mikuru Think Quest3
    "\"Seriously,\" Haruhi chided her, \"if we're going to be any kind of romantic rivals, you should leap at a chance like that! Drag him with you to dinner, then go for a nice walk somewhere after! Your moe powers are wasted settling for what you did. Completely wasted!\""
    nvl clear
    show Mikuru Think Sup1
    "Mikuru opened her mouth and struggled for words, but all she could do was stare and work her jaw silently before she tilted her head slightly to one side and stared at Haruhi as though the younger girl had suddenly gone mad. Which, Haruhi realized, she might think from her perspective."
    nvl clear
    show Haruhi Worry1
    "\"Mikuru-chan,\" she said, shaking her head, \"you told me that you 'couldn't' have a relationship in this time, right?\""
    show Mikuru Think Sad5
    "\"R...right,\" the time traveler agreed. \"I told you I wasn't a threat! Please believe me, Suzumiya-san—\""
    nvl clear
    show Haruhi Ang2
    show Mikuru Think Sad2
    "\"Oh, shut up about that,\" she snapped. \"Seriously! 'I'm not a threat'? That sounds like a recipe for misery! Especially since you have your own feelings anyway! There's a very obvious solution, Mikuru-chan. You should have seen it by now!\""
    show Mikuru Cower Sup1
    "\"T...there is?\" Mikuru looked mystified and more than a little scared, but Haruhi caught the flash of hope in her eyes anyway. \"What is it?\""
    nvl clear
    stop music fadeout 1
    queue music "Music/YareYare.mp3"
    show Haruhi Point Scold2
    show Mikuru Cower Quest1
    "\"If you {i}really{/i} believe that you can't have a relationship, then why not try anyway?\" Haruhi asked. \"Consider it a practice run! If you're going to give up and tell yourself it'll never work out, what do you stand to lose by trying your best, anyway?\""
    nvl clear
    show Mikuru Cower Sup1
    "\"Y...you {i}want{/i} me to be your romantic rival?\" Mikuru managed, boggling."
    show Haruhi Sup1
    show Hblush at TenthLeft
    "\"Who said anything about romance?\" Haruhi threw back, her face reddening."
    show Mikuru Cower Nervous2
    "\"You did, just a minute ago!\""
    nvl clear
    show Haruhi Pout2
    "Her blush deepened. \"Well,\" she managed, looking away. \"Yeah, okay. I guess I did. Anyway, it's not like I want us to compete ... but if you're so adamant it'll never work out, what about the things you could learn from at least trying!? What you need to do is give it your best shot anyway! Kyon's a nice enough guy, even if he is a bit clueless.\""
    nvl clear
    "\"I guess I can't blame you for liking him.... But I {i}will{/i} blame you for sitting by the sidelines without even trying and making yourself unhappy because you're too scared to do anything about it! Trying to think of it as a competition with me will let you see what you can really do when you find someone you {i}can{/i} be with!\""
    nvl clear
    "Mikuru continued to stare, seemingly stunned by the barrage of words."
    show Haruhi Crossed Sigh1 Flip
    show Hblush Crossed Flip at TenthLeft
    "\"It's not like I'd be happy about it,\" Haruhi continued, crossing her arms over her chest. \"But I like that you {i}act{/i} dojikko and moe for the club. It won't actually help you in the long run to {i}be{/i} that way. You have to have more confidence!\""
    nvl clear
    show Mikuru Think Sad5
    "\"U...um....\" Mikuru swallowed nervously, and Haruhi watched the older girl slowly gather herself together, straightening up from her cringing. \"What's 'dojikko' mean?\""
    nvl clear
    hide Hblush
    show Haruhi Crossed Sup1 Flip    
    show Mikuru Think Sad3
    "Haruhi stared. \"If we were in a comedy anime, that line would cause a face-fault,\" she deadpanned. \"Am I the only person who reads— {nw}"
    show Haruhi Crossed Sigh1 Flip
    extend "Never mind!\" She shook her head, banishing the complaint."
    nvl clear
    show Haruhi Crossed Quest1 Flip
    "\"Okay, look, dojikko characters are clumsy and harmless, they're part of the cast to evoke a 'big-brother' instinct, or play up the role of fan service. Don't get me wrong, it's pretty awesome that you have those characteristics!\""
    "\"But while it's fine for an anime character, real people need more depth! So let's work on making your dojikko moe-factor something you use to appeal to a guy you like, not just the extent of who you truly {i}are{/i}.\""
    nvl clear
    show Mikuru Think Sad5
    "Mikuru blinked several times at Haruhi. \"...I don't think I understand,\" she finally admitted, giving an apologetic smile. \"You can't really want me to get in your way, can you?\""
    show Haruhi Sigh2
    "Sighing deeply, Haruhi shook her head. \"Try harder for Kyon,\" she said. Surely that would be clear enough? \"I'm just saying that if you can't really get anywhere, it won't hurt you to learn as much as you can in the meantime!\""
    nvl clear
    stop music fadeout 1
    queue sound "SE/DoorKnock.mp3"
    queue sound "SE/DoorOpenFast.wav"
    show Mikuru at right
    show Haruhi Neutral1 at center
    with dissolve
    show Kyon Puzzle1 Flip at left with moveinleft
    queue music "Music/Yuuutsu.mp3"
    "A knock sounded at the door, cutting off further discussion before Kyon pulled it open. \"I'm back,\" he said, looking troubled."
    show Mikuru Smile3
    "\"Oh!\" Mikuru managed, turning to look at him, her smile returning. \"Was everything okay?\""
    nvl clear
    show Kyon Sigh6 Flip
    "\"Classified,\" he answered with a grimace. \"But it's taken care of.\""
    show Mikuru Quest1
    "Mikuru looked confused, but shook her head and moved to pick up her new sewing machine. \"Um, is it okay if I leave this here, Suzumiya-san?\" she asked."
    nvl clear
    show Haruhi Hap1
    show Kyon Neutral3 Flip
    show Mikuru Neutral1
    "Haruhi looked at the box, then considered the free space in the club room. Things could be shuffled around to fit it, she was certain. \"It shouldn't be a problem,\" she said, nodding. Could Mikuru make new costumes? That would certainly save her a bit of money on getting a new outfit for Mikuru every so often ... or even one for herself. \"We should talk about that at lunch,\" she decided."
    nvl clear
    show Haruhi Ang1
    "\"In the meantime....\" She turned her attention to Kyon as he set his schoolbag on the tabletop, and another bag full of cloth near Mikuru. \"You need to study!\""
    show Kyon Sigh2 Flip
    "\"Yay,\" Kyon said flatly. \"Is there any greater joy?\""
    nvl clear
    show Haruhi Grin2
    "\"Getting a good grade for your hard work and staying in the brigade?\""
    show Kyon Smile6 Flip
    "He blinked, smirking at her as he took a seat. \"Well played, brigade chief. Well played.\""
    show Haruhi Hap5
    "\"Naturally,\" she agreed, shuffling the flashcards they had made the night before. \"That's why you're just the vice commander.\""
    nvl clear
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22", "Friday, April 22") from Fi2_sc004
    
    stop music fadeout 1
    queue music "Music/Tanzaku no Mukou ni.mp3"

    scene bg MikuruClass with fade
    nvl clear
    "Lessons were very difficult for Mikuru to follow in the wake of Haruhi's bizarre announcement. It didn't help when she took into account further confusion about what a message specifically encoded for her meant for Kyon."
    "He seemed to have dealt with it without trouble, and she knew he lacked her conditioning and the other tools that she had been given specific for her duty as a time traveler. Even so, that didn't slow him down in the slightest."
    "But that didn't mean she could simply ignore it. She was supposed to be studying phenomena surrounding Haruhi, so why had the sudden shift to follow Kyon's orders even come about? Not the she minded ... but it did make her feel remarkably incompetent that he seemed both better informed and better equipped to handle things."
    nvl clear
    "Then again, it wasn't as though she could expect him to be given his own TPDD or conditioning ... to say nothing of the training requirements."
    "Could Yuki fill those requirements for Kyon? Come to think of it, with Haruhi's help, could he be given everything else he needed to just leave her completely behind?"
    "She sighed, lowering her head and pondering the notebook paper before her. It was one thing to try and be helpful, but she was wondering if she really was even that."
    "She had taken Kyon back in time for something she got light-headed even thinking about, and she hadn't done anything {i}but{/i} ferry him back in time."
    nvl clear
    "It wouldn't have bothered her nearly so much, except for the fact that the mysterious note had given her orders to relay verbal instructions to him, and then ... she was out of the loop."
    "As if that weren't problem enough, it was immediately followed by Haruhi insisting that she torture herself with a pursuit she was destined to fail, and the order to become more confident?"
    "There was a certain temptation to throw aside her orders from her superiors and do what Haruhi said. She was already skirting dangerously close to the lines by having dinner and a shopping session with Kyon, as far from her ideal date as those events had been."
    "She was reasonably sure he wasn't even supposed to know where she lived, to say nothing of her inviting him into her apartment, however briefly!"
    nvl clear
    show Tsuruya Hap5 at TenthRight with moveinright
    "If she didn't get her act together, and soon, she was likely to be recalled. She was roused from her contemplation by Tsuruya poking her elbow. \"Helloooo~!\" the taller girl called, peering at her intently, smirking. \"What's gotcha distracted, Mikuru-chan?\""
    nvl clear
    $ _window = True
    show Mikuru Neutral3 at TenthLeft with dissolve
    $ _window = False
    "\"Ah, oh, just things,\" she answered, shaking her head and climbing to her feet. On to the clubroom, then, where she would have to figure out some way to satisfy Haruhi and simultaneously keep herself in control."
    nvl clear
    show Tsuruya Neutral1
    "\"Okies,\" Tsuruya said, raising one eyebrow. \"Well, I gots to escort Kanae-chan, like I promised, so see you soonish!\""
    $ _window = True
    show Mikuru Neutral2
    hide Tsuruya with easeoutright
    $ _window = False
    "With that, the green-haired girl whirled and sped off."
    nvl clear
    "Alone, Mikuru walked slowly to the club room, not entirely surprised that Kanae and Tsuruya caught up with her as she reached the door.{nw}" 
    
    $ _window = True
    scene black with dissolve
    stop music fadeout 1
    queue music "Music/Aruame.mp3"
    scene bg ClubroomFullDay:
        xpos 0 ypos 0
    show Kyon Neutral3 Flip at center_RightScreen
    show Haruhi Neutral1 Flip at right_RightScreen
    show Kanae Neutral1 at left_RightScreen behind Kyon
    show Koizumi Crossed Smile4:
        xalign 0.6 yalign 1.0
    show Yuki Side1:
        xalign 0.3 yalign 1.0
    with dissolve
    $ renpy.layer_at_list([PanScene_SetToLeft])
    $ _window = False
    extend " She opened it to let the other girls in first, only to see Kyon and Haruhi already sitting at the table, with Koizumi and Yuki across from them."
    nvl clear
    "Yuki tapped the keys of one of the laptops, an empty bento at her side. Koizumi picked at his own bento, studying the couple sitting opposite him."
    $ renpy.layer_at_list([PanScene_LeftToRightSlow])
    "Haruhi was grilling Kyon with questions for the upcoming math test. The really unusual thing was the fact that Kyon had — for some reason — three bento boxes next to him, and was evidently just finishing the last one."
    nvl clear
    show Kanae Quest1
    "Haruhi glanced at the stack of empty boxes, but Mikuru was positive that the three closest to Kyon were his ... everyone else had their own. \"Wow,\" Kanae said, peering in. \"You must be really hungry, Sempai!\""
    nvl clear
    show Kanae Neutral1
    show Haruhi Neutral2 Flip at right_RightScreen
    "\"His mom's starving him as some strange form of punishment,\" Haruhi explained, rolling her eyes. \"Sure, tuna is supposed to be 'brain food', because it's high in protein, but just fish and rice?\""
    nvl clear
    show Tsuruya Smile3 Flip at right behind Koizumi
    "Tsuruya looked thoughtful, eying the lunch boxes before closing the door and taking a seat next to Koizumi. Kanae had already claimed the space on Kyon's other side, so Mikuru was left with the choice of sitting next to Yuki or Haruhi."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Neutral2 at left with dissolve
    "She resolved to rush to the club room more quickly next time, and debated internally before choosing to sit next to Yuki. For her part, the impassive girl didn't react, merely tapping a few more keys out."
    nvl clear
    "Unable to resist, Mikuru stole a glance at the laptop, seeing nothing more than a text editor. Able to sense the gaze, Yuki's eyes snapped immediately towards her as the text file was minimized, and a splash screen for The Day of Sagittarius III appeared."
    nvl clear
    "Mikuru quickly looked away, receiving the unspoken message without any trouble. To her surprise, however, Yuki turned to look towards Koizumi, then adjusted the laptop so that the esper couldn't see the screen — but Mikuru could. Maybe Yuki thought that Mikuru was trustworthy enough not to peek, and the esper wasn't?"
    nvl clear
    "That offered a tiny bit of encouragement. She respectfully avoided looking at the screen, though the sudden shift in color to the white background of the text editor let her know that Yuki was back to her original project. She unwrapped her lunch and ate it, watching the other club members."
    nvl clear
    show Tsuruya Hap4 Flip
    show Koizumi Crossed Smile1
    "Tsuruya quickly engaged Kanae in a conversation over an anime they were both watching, and Koizumi observed the pair with his usual smile, looking slightly more amused than usual."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToCenter])
    stop music fadeout 1
    queue music "Music/KouchouKouchou.mp3"
    show Tsuruya Neutral1 Flip
    "\"No, no,\" Tsuruya said, shaking her head. \"Trope-tan doesn't do thats! Sounds a bit out-of-character, don't it?\""
    show Kanae Quest1
    "\"Er,\" Kanae managed, frowning. \"Maybe I'm remembering it wrong? I mean ... doesn't every episode end with her using the Chekhov Beam to stop the monster of the week?\""
    nvl clear
    show Tsuruya Hap1 Flip
    "\"Usually,\" Tsuruya agreed, chuckling. \"Unless it's one of those 'power of heart' episodes. But Uncyclo-tan is the big bad! They're not on the same sentai team.\""
    show Kanae Unhap1
    "\"I thought Ae-tan was the main villain,\" Kanae said with a pout. \"Wasn't Uncyclo-tan just her minion?\""
    nvl clear
    show Tsuruya Quest1 Flip
    "\"Who's Ae-tan? Is that a nickname for Wikipe-tan?\""
    show Kanae Unhap2
    "Kanae tapped her lower lip with a frown. \"Um ... maybe ... I'm thinking of a different series?\""
    nvl clear
    show Tsuruya Hap2 Flip
    show Kyon Unhap4
    "\"Maybe,\" Tsuruya agreed with a shrug. \"Okies! It was nice having lunch with you, but I gots to do some more investigation work—\" She cut off with a giggle at Kyon's sharp look, quickly adding, \"Nothing dangerous right now, Kyon-kun!\""
    nvl clear
    $ renpy.layer_at_list([PanScene_CenterToRight])
    show Kanae Neutral1
    show Kyon Smile6
    "\"Well, call me if that changes, Tsuruya-kun,\" Kyon warned, before being smacked over the head by Haruhi's stack of flashcards. {nw}"
    show Kyon Sup1
    show Haruhi Ang1 Flip
    extend "\"Ow! {nw}"
    show Kyon Sup1 Flip
    extend "Hey! I thought you didn't like tsundere characters!\""
    nvl clear
    show Kyon Sup2 Flip
    show Haruhi Ang2 Flip
    hide Koizumi
    "\"I don't,\" Haruhi groused, looking at him oddly. \"But I don't think I mentioned that to you. Anyway, it was a stack of cards! Are you saying it really hurt?\""
    hide Tsuruya
    show Kyon Worry1 Flip
    show Mikuru:
        xalign 0.3 yalign 1.0        
    show Yuki:
        xalign 0.65 yalign 1.0        
    # show Koizumi at right
    "\"No,\" he admitted as Tsuruya left. \"Just.... Nevermind.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Think Quest4
    "After putting away her own empty bento, Mikuru pondered what to do with her remaining free time. She brightened when she recalled the pattern paper. That would be a nice distraction from things."
    "She could make something for Kyon — that should satisfy Haruhi's demands without making her own life more difficult than she needed to."
    nvl clear
    "She spent a long minute thinking of what to make before she finally settled on a heavy coat. Kyon's last coat had gotten fairly worn after the last winter, and even if the season were warming up.... Well, it was something."
    nvl clear
    "One of the bolts of cloth she had picked up with Kyon was treated to be water resistant — the one she had grabbed because she didn't want to seem completely unaware of the outside world. She couldn't imagine what else she would make with it for Kyon."
    "He really didn't seem the type to wear an apron, and a tablecloth didn't seem very personal, so a coat was the answer."
    nvl clear
    "The clubroom's table was large enough for her to unroll a huge sheet of the stuff, but she would have to ask someone else to move, and she thought she'd be better off designing on the small- scale, first."
    "She pulled a notepad from the bookshelf behind her and began sketching rough dimensions and designs. There was rather a lot of that cloth, so she could make a full-length coat."
    nvl clear
    "An image from a recent television drama she had seen came to mind — it was a bit militaristic, but she thought Kyon would look quite dashing in a greatcoat, so decided to style her design after that."
    show Mikuru Think Quest3
    "She'd only roughed out the basic features — pockets, buttons she'd need to pick up later, a rain flap that could be flipped over into a hood — when she felt Yuki's unsettling gaze on her."
    nvl clear
    show Yuki Talk2
    "She looked up in alarm, but the contact-purposed interface merely commented, \"Interesting,\" {nw}"
    $ _window = True
    show Yuki Side1 at TenthRight with dissolve
    $ _window = False
    hide Kanae
    extend "before turning back to whatever she was writing."
    show Haruhi Quest1 Flip:
        xpos 1050
    $ renpy.layer_at_list([PanScene_LeftToRight])
    hide Yuki
    stop music fadeout 1
    queue music "Music/Gekiretsu.mp3"
    "\"What's that, then?\" Haruhi asked, her interest piqued. She glanced at the sketch before her eyes widened. {nw}"
    show Haruhi Sup1 Flip 
    extend "\"You're making that for Kyon?\" she added, flashcards forgotten for the moment."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Mikuru Think Quest1
    "\"I...I was thinking of it,\" Mikuru agreed, nodding. \"Is something wrong?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral4
    show Haruhi Crossed Grin1
    "Haruhi raised an eyebrow thoughtfully, while Kyon tried to crane his neck to see the sketch from his seat. The brigade chief snatched the paper out of Mikuru's hands, hiding it from Kyon's sight and shoving the flashcards at Koizumi."
    nvl clear
    show Haruhi Ang1 at left with dissolve
    $ renpy.layer_at_list([PanScene_RightToLeft])    
    "\"Keep studying,\" she ordered, walking around the table to sit at Mikuru's side, studying the image intently."
    nvl clear
    show Kyon Unhap4 at right_RightScreen
    #Not moving Kyon to fit better, as Kyon at left_RightScreen puts him at the very center of the scene for some reason, and xalign 1.3 yalign 1.0  puts him at the same spot. center_RightScreen is offscreen, and TenthLeft_RightScreen creates an error.
    show Koizumi Crossed Smile3 at left_RightScreen
        # xpos 1050
    $ renpy.layer_at_list([PanScene_LeftToRight])
    "Kyon looked irritated, but Koizumi obligingly continued the study session."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Haruhi Eyeroll1
    "One eye watching Kyon closely, Haruhi explained, \"I've seen.... Um, maybe....\" {nw}"
    show Haruhi Hap1
    extend "She grinned and nodded decisively, setting the sketch between the two of them. \"It needs pockets on the inside,\" she said in a conspiratorial whisper."
    nvl clear
    "\"In the sleeves, too, and I think it should have ties so that the sleeves can be rolled back and buttoned into place. And make it ... I think about seven centimeters longer. Yeah, that's right. It's going to be tan colored, right?\""
    show Mikuru Think Quest3
    "She nodded, feeling another tiny surge of irritation that — once again — everyone but her seemed to know what was going on. She tried to banish the feeling."
    nvl clear
    "Knowing nothing shouldn't bother her, knowing everything was too stressful ... but knowing just enough to feel really clueless ... that wasn't any fun at all."
    show Haruhi Hap3
    "\"Okay,\" Haruhi whispered, her grin widening. \"Don't let Kyon know about it until it's done. How long do you think it'll take?\""
    nvl clear
    show Mikuru Think Quest1
    "Keeping it hidden from Kyon would require him to avoid the clubroom, or her to haul the heavy machine back to her already cramped apartment. \"A few days, probably,\" she answered, frowning thoughtfully. \"Maybe Sunday if I come in while class isn't in session.... Otherwise, Kyon-kun might see me working on it.\""
    nvl clear
    show Haruhi Hap1
    "\"Not a problem,\" Haruhi decided. \"If Tsuruya's keeping him occupied anyway, then you should have plenty of time.\""
    nvl clear
    
    
    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22", "Friday, April 22") from Fi2_sc005
    
    stop music fadeout 1
    queue music "Music/Tanzaku no Mukou ni.mp3"

    
    scene bg Cab with fade
    #show Kyon Suit at center with dissolve
    "It was strange, Kyon mused, to feel uncomfortable in a suit. He wore his school uniform enough that he had assumed he would be completely at home wearing a suit and tie, but sitting in the back of Tsuruya's limousine headed towards her estate ... he felt awkward. Tsuruya herself wasn't there, sending the driver to fetch him from his house and meet at her estate."
    nvl clear
    "The last time he had been there, he'd been a bit too badly injured to really care about the surroundings, so he found himself nervously checking the back seat for bloodstains or other proof of the battle. Evidently the car was cleaned by the same people who had gotten the blood out of his school uniform, as there wasn't a trace left in sight."
    nvl clear
    "He tried to relax, but there wasn't much comforting to think about. Haruhi's study sessions had given him a headache, but he was also surprised at how confident he was in his test scores. They wouldn't find out until tomorrow for certain, and it was possible he would miss the mark and fall below the critically required ninety.... But he felt sure that he had done much better than usual."
    nvl clear
    scene bg TsuruyaHouseNight with fade
    #show Kyon Suit at left with dissolve
    "After pulling through the gates to the Tsuruya estate, the vehicle stopped. Even though he was fairly certain that he was supposed to wait for the driver to open his door, he let himself out, scanning around for Tsuruya."
    "He spotted her quickly, standing on the path between the driveway and the house wearing a very elaborate kimono, her hair done up in an intricate bun."
    nvl clear
    show Tsuruya Kimono Smile2 at right with dissolve
    "She waved, and he walked to meet her, bowing his head as he approached. \"I hope I'm not under-dressed,\" he commented, adjusting his tie and glancing at the dark blue suit he was wearing, which was quite plain in contrast to her outfit."
    show Tsuruya Kimono Hap1
    "\"Looks good on you,\" she assured him, smirking. \"Okies, come on a walk with me?\""
    nvl clear
    #show Kyon Suit
    show Tsuruya Kimono Smile1
    "It felt more like an insistence than a question, but he agreed, falling into step just behind her as she leisurely strolled towards the garden. \"I don't want to make a mistake and upset your father, or embarrass you,\" he commented, glancing at the surroundings, but too worried to really enjoy the view."
    nvl clear
    show Tsuruya Kimono Hap5
    "\"You should be fine,\" she assured him. \"You'll talks with my father, and I'll explain what we want from him.\""
    show Tsuruya Kimono Smile2
    "He nodded at that, looking at the girl out of the corner of his eyes. She seemed completely absorbed with a distant cherry tree, the last few petals slowly drifting to the ground."
    nvl clear
    show Tsuruya Kimono Hap1
    "\"I won't be embarrassed by Kyon-kun,\" she said after a moment. \"And my father's a mega understanding guy, nyoro~!\""
    #show Kyon Suit
    show Tsuruya Kimono Smile1
    "\"I hope so,\" he agreed."
    nvl clear
    show Tsuruya Kimono Quest1
    "\"Mmm. Hey, Kyon-kun, has Mikuru-chan seemed a bit down lately to you?\""
    #show Kyon Suit
    show Tsuruya Kimono Quest2
    "That was a sudden shift in conversation, he thought. \"Distracted, for sure,\" he agreed. \"I don't know about 'down', though.... You think she's upset?\""
    nvl clear
    show Tsuruya Kimono Sigh1
    "Tsuruya nodded quickly. \"Yeah, yeah.... In class todays she was all kinds of distracted and moody. Like she's pining for some guy! But I don't know what guy Mikuru-chan likes.\" {nw}"
    show Tsuruya Kimono Quest1
    extend "She turned a questioning glance at Kyon. \"What do you think?\""
    nvl clear
    #show Kyon Suit
    show Tsuruya Kimono Quest2
    "\"I don't know; I hadn't thought about it,\" he admitted, grimacing. He wasn't anyone to judge, but there was a real rush of jealousy as soon as the girl at his side brought it up."
    #show Kyon Suit
    "Damn it, anyone who thought about laying a hand on Mikuru was going to have to go through him! Then again.... \"I don't think I should ask her about that. Wouldn't it be, er ... her own personal business?\""
    nvl clear
    show Tsuruya Kimono Grin2
    "Tsuruya's glance was very shrewd. She poked him firmly in the shoulder. \"Kyon- kun never considered that he might be the guy she's pining for?\" she mused. \"I'm not sures if that's noble or dense!\""
    nvl clear
    #show Kyon Suit
    "\"H...hey!\" he protested, frowning. \"I wish that Asahina-san were interested in me like that! What healthy male wouldn't? But....\" He trailed off, frowning."
    #show Kyon Suit
    "Wasn't her older self always taking advantage of her visits to kiss him? But what did {i}that{/i} mean? \"Well, with Haruhi,\" he began lamely, before sighing and shaking his head."
    nvl clear
    show Tsuruya Kimono Hap3
    "\"You're a popular guy,\" Tsuruya acquiesced, smirking. {nw}"
    show Tsuruya Kimono Hap7
    extend "\"Okies! I'll talk with her tomorrow mornings, and find out what's going on!\""
    #show Kyon Suit
    show Tsuruya Kimono Hap5
    "\"Anything you can do to cheer her up,\" he agreed. \"I don't like seeing her unhappy, either.\""
    nvl clear
    show Tsuruya Kimono Quest1
    #show KBlush at left
    "She blinked and turned another questioning gaze on him. He studiously looked away, remembering his conversation with Tsuruya's maid as his face colored."
    nvl clear
    show Shinobu Neutral2 Flip at left with dissolve
    "Just as the silence was becoming awkward, a maid — possibly the same one, he couldn't tell them apart — stepped out from behind a tree on the path ahead of them. \"Haruka-san, Kyon-dono,\" she said, bowing. \"Tsuruya-sama is ready to speak with the two of you now.\""
    show Tsuruya Kimono Hap1
    "\"Okies,\" Tsuruya said, giggling a bit. \"This way, Kyon-kun!\""
    nvl clear
    scene bg TsuruyaMeetingNight with fade
    #Tsuruya - Tsuruya-sama - center - Kyon - Shinobu
    "He followed the girl into the sprawling mansion, as she led him down a maze of twisting hallways before finally entering a large meeting hall."
    "Most of the Tsuruya estate was a single floor, baring any scary basements Kyon was happy not to know about, but he saw that this room had a raised ceiling, which suggested that one of the few parts of the house that seemed to be higher was merely to provide a wider open area like they one they entered."
    nvl clear
    "The room was ten meters wide at least, and probably twice that in length. Banners and well preserved Tsuruya family heirlooms adorned the walls, ranging from a picture of an ancestor seemingly from just before World War Two, to a cracked and re-lacquered woodcut that looked like it was straight out of the fifteenth century — and probably was."
    "Ancient weapons hung here and there, presumably keepsakes of prominent familial figures. The far end of the room was a raised platform, reminding Kyon of a dais."
    nvl clear
    "The far wall of the room was covered with a floor-length and wall-wide sheet of cloth bearing the symbol he guessed was the Tsuruya family kumon, the ancient crest from their family's founding. The stylized classic shapes of five cranes in a wheel formation beneath the peaked roof of a great house."
    nvl clear
    "Below that, on a large cushion was a man that seemed small only compared to the massive regalia behind him. If the large figure of the Tsuruya family patriarch wasn't imposing enough, the identically dressed and immaculate men in blue suits lining the sides of the room in orderly rows were enough to make him even more nervous."
    nvl clear
    "He counted twenty other men in the room in two rows of ten, facing the entryway as he tried to keep from stumbling, following in Tsuruya's composed, poised wake."
    #show TsuruyaSama:
    #    xalign 0.3 yalign 1.0   
    #with dissolve
    "The Tsuruya family patriarch was as tall as Kyon while sitting cross-legged on a thin cushion atop the dais, sporting neatly groomed short green hair — identical in shade to the girl's, while his amused, knowing smirk betrayed an identical fang as well."
    "Despite the fact that every other man was wearing a suit in the room, the patriarch managed to make all of the others look under-dressed, wearing only a green robe, less formal than the girl's, with the family crest patterned all across it."
    nvl clear
    "Moreover, he had one arm free of the robe, baring half his chest and revealing the complex and detailed tattoos adorning him. Kyon tried not to gawk; it must have taken real courage and quite some time to have the vivid image of a fierce crane fishing a dragon from the heavens tattooed. It looked so lifelike, he practically expected it to leap off the man with one flexed muscle."
    nvl clear
    show Shinobu Neutral1 at left with dissolve
    "Nervously searching for something familiar to comfort him in this madness, Kyon spotted a maid in the customary outfit kneeling just below the dais on the man's right side, holding a tray before her, eyes downcast. Was she the same one that had spoken to him and asked that he watch over Tsuruya? The same one — somehow — that had met them on the path through the gardens? There was still no way to be sure."
    nvl clear
    #show KyonSuit
    #   xalign 0.7 yalign 1.0
    show Tsuruya Kimono Ser1:
         xalign -0.3 yalign 1.0
    hide Shinobu
    with dissolve
    "Tsuruya strode to within a few paces of the patriarch, then knelt and bowed deeply, her forehead almost touching the floor. Stopping a step short of the girl, Kyon followed suit without hesitation. \"Rise,\" the man chuckled. \"Dearest daughter, have you called mes back here to report on your trial?\""
    nvl clear
    #show Kyon Suit
    show Tsuruya Kimono Ser2
    "Kyon fought to restrain a hilarious snicker, remaining bowed even when Tsuruya rose. They shared the speech impediment as well as the fang. \"Progress is good,\" she said, \"but I called you here to ask aid for a strong ally!\""
    #show TsuruyaSama
    show Tsuruya Kimono Ser1
    "\"A strong ally needs aid?\" The patriarch's voice now lacked amusement. \"Explains, daughter.\""
    nvl clear
    show Tsuruya Kimono Ser2
    "\"Um! Tsuruya-sama!\" she said, her voice unshaken. \"I have engaged in battles with others, and this brothers here has saved me from attack not once, but twice!\""
    nvl clear                                                                                                                
    #show Kyon Suit
    "Kyon rose slightly when he heard the other men around the room murmur with subdued voices, exchanging dire looks with one-another behind their dark glasses. \"Others?\" the patriarch mused, rubbing his chin thoughtfully with the hand that was not within his robe. \"Explain further.\""
    nvl clear
    show Tsuruya Kimono Sigh1
    "\"I don't know everything yet,\" Tsuruya said with another deep, apologetic bow. \"I believes they are Sumiyoshi-rengo.\""
    #show TsuruyaSama
    "\"I see. And how strongs is this ally of yours, then?\""
    nvl clear
    show Tsuruya Kimono Ser2
    "\"This brother defeated twelve mens by himself, all in the same fight that left Kasai in the hospital,\" she explained. \"And yesterday, another four.\""
    show Tsuruya Kimono Ser1
    "The gasp from the surrounding enforcers this time was not subdued at all."
    nvl clear
    #show TsuruyaSama
    "The patriarch raised one hand and all other conversation stilled. Hardened green eyes turned to Kyon. \"Then,\" he said, \"this is not my daughter asking for my assistances at all, is it? This is him wishing his family be kept safe so that he can continue to serve you?\""
    nvl clear
    #show Kyon Suit
    "Kyon nodded, not trusting himself to speak."
    #show TsuruyaSama
    "\"Good,\" the man judged. \"I like a man who values his family.\" He snapped his fingers. \"Tell us your name, then.\""
    nvl clear
    #show Kyon Suit
    show Tsuruya Kimono Quest1
    #show TsuruyaSama
    "Barely able to keep his voice from hitching, Kyon gave his full name to the Tsuruya patriarch. The girl at his side blinked and looked at him sidelong, her eyes widening; even the patriarch looked impressed. He found it a bit unnerving that they seemed to care so much for his name, when he was cursed with that stupid nickname all the time...."
    nvl clear
    #show TsuruyaSama
    "\"A strong name,\" the patriarch allowed, eyebrows raised. \"Then, just like the stories of Sadamitsu and Raiko, you acts as my daughter's retainer?\""
    #show Kyon Suit
    show Tsuruya Kimono Ser1
    "\"Yes,\" he agreed, wondering how much trouble this was all going to get him into. Still, it would keep his family safe, so that much would be worth it."
    nvl clear
    #show TsuruyaSama
    show Shinobu Neutral1:
         xalign 1.2 yalign 1.0
    "The man nodded as the maid rose, shuffling before him and holding out the tray. With brisk, efficient movements, the patriarch poured three small dishes of sake, mixing in salt and something glittery that Kyon couldn't quite make out. He took a dish, and the tray was moved to the girl. She took a dish as well, and then the tray was before Kyon."
    nvl clear
    show Shinobu Neutral3
    "In a soft voice that Kyon was sure no one else could hear, the maid instructed him, \"Drink exactly half, in three small sips.\" He nodded minutely, amazed his hand wasn't shaking as he took the last dish."
    nvl clear
    #show TsuruyaSama
    show Tsuruya Kimono Grin1
    #show Kyon Suit
    show Shinobu Neutral1
    "\"For family,\" the man announced, taking a sip. Tsuruya sipped as well, so Kyon followed suit; he was reasonably sure it was sake, but it had the taste of strong salt, and glittering flakes of ... something ... were floating within. \"For justice,\" and a second sip. \"For honor,\" with a final sip."
    nvl clear
    show Shinobu Neutral3
    "The maid then exchanged the girl's cup with her father's, and whispered to Kyon, \"Hold still and wait.\""
    "This time, the girl spoke the words, she and her father drinking a sip at each invocation. When it was done, the maid took Kyon's cup and exchanged it with Tsuruya's. \"Now you,\" the maid whispered quietly."
    nvl clear
    show Shinobu Neutral1
    #show Kyon Suit
    "\"For family,\" Kyon said, sipping from the dish. The girl at his side sipped with him; the patriarch did not. \"For justice,\" he said, wondering how the girl's stomach was holding up after this much of the strange ceremonial drink. Finally, he completed, \"For honor.\""
    nvl clear
    #show TsuruyaSama
    "\"Good,\" the patriarch said, nodding approval as the maid silently collected all of the dishes. \"Very good! All shall know then that this, our brother, is a kobun! Everyone, welcome your new foster brother to the Tsuruya branch of the Yamaguchi-gumi!\""
    nvl clear
    show Tsuruya Kimono Smile2
    "The men on the edges of the room suddenly swarmed him, and he was swept up in a tide of cheering ninkyo dantai pounding his back and welcoming him to the family. As bewildered as he was, he still saw the relief in the girl's face, the tiny sparkling tears of what he prayed was happiness in her eyes."
    nvl clear
    scene black with dissolve
    "Yeah, Haruhi was going to love hearing about this."
    nvl clear

    stop music fadeout 3
    call eyecatch_fancy("Friday, April 22", "Friday, April 22") from Fi2_sc006

    scene bg KyonHallway with fade
    #show Akane at left
    #show KyonSuit at right
    #with dissolve
    "\"So,\" his mother said, when he finally returned home, eyeing his choice of outfit when he walked through the door. \"Trying to cultivate a respectable image?\""
    "\"Yep,\" he answered, still musing over his somewhat unexpected initiation, fingering the pin with the Tsuruya family crest that he had been given."
    nvl clear
    "\"It wasn't a special occasion?\""
    "\"Ah, just met up with a classmate, chatted with her family a bit.\""
    show Nonoko Laugh1 at TenthRight with moveinright:
        .1
    "His sister charged down the stairs and flung herself at him. \"Change out of that suit and play with me!\" she demanded. \"I finished my homework!\""
    nvl clear
    "He patted her on the head. \"Alright,\" he agreed."
    "\"Well, as long as you're through with being a delinquent,\" his mother decided."
    "Snorting, he ruffled his sister's hair until she let go of him. \"Yeah, delinquency wasn't working out, so I just skipped straight to joining the Yamaguchi-gumi.\""
    nvl clear
    #hide KyonSuit with moveoutright:
    #    .1
    "He walked up the stairs to change his clothes, while his mother stared, eyes narrowed. \"That's not funny!\" she yelled up after him."
    show Nonoko Quest1
    "A chuckle escaped him as he heard his sister ask, \"What's a 'Yamaguchi-gumi'?\""
    
    jump HAB3
