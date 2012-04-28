# Chapter 5, Straightforward Flashback and Exposition Arc.

label SF3:   
    if music_need:
        $ renpy.music.set_volume(0.2, .5, channel="music")
    stop music fadeout 3
    scene black
    show title 005 at card_pos
    with slowfadein
    pause
    play sound "SE/Pageflip3.mp3"
    nvl clear
    
# Scene moved from Chapter 4 to avoid weird music glitchy... thingy. 
    scene black
    show clouds
    with fade
    "\"Kyon!\"" 
    play sound "SE/heartbeat.mp3"
    show clouds CS with dissolve
    show clouds with dissolve
    pause 1
    play sound "SE/heartbeat.mp3"
    show clouds CS with dissolve
    show clouds with dissolve
    pause 1
    play sound "SE/heartbeat.mp3"
    show clouds CS with dissolve
    show clouds with dissolve
    pause 1
    play music "Music/KyomutekiKuukan.mp3"
    nvl clear
    hide clouds
    scene bg HaruhiCS
    with dissolve
    "Flashes of light, crackling energy dozens of orders of magnitude lower than the ones in the spaces that Yuki had pulled him through with her teleport echoed through his field of vision before his eyes snapped open to see Haruhi kneeling over him. She was wearing her school uniform, and he guessed without checking he was too."
    scene bg SchoolOutside1 CS
    nvl clear
    show Haruhi CS Pout1 at TenthLeft
    show Kyon CS Sigh1 at right
    with dissolve
    "He blearily blinked and sat up, squinting at the gray sky overhead. \"This again?\" he asked, stretching."
    show Haruhi CS Pout2 at TenthLeft        
    show Kyon CS Sigh3 at right
    "\"Sorry,\" she mumbled, unable to meet his eyes. \"I thought I was having a pretty bad day, then ... it got worse.\""
    nvl clear
    
#Starting Chapter 5 proper.
    show Haruhi CS Pout1 at TenthLeft
    show Kyon CS Sigh1 at right
    "\"It happens,\" he said casually, seeming unconcerned. Glancing at their surroundings, he observed, \"I don't see any Shinjin. Back in the school again?\""
    show Haruhi CS Sigh2 at TenthLeft
    show Kyon CS Sigh3 at right
    "\"I don't even understand how you can see this and not be alarmed,\" she said with a sigh, looking up at the sky with him. \"So ... you said that this happened last time when I got too frustrated, and then I accidentally almost destroyed the world?\""
    nvl clear
    show Haruhi CS Unhap3 at TenthLeft
    show Kyon CS Neutral2 at right
    "\"That's what I've been told,\" he agreed. \"But we've got a little time, I think.\""
    show Haruhi CS Neutral2 at TenthLeft
    show Kyon CS Neutral3 at right
    "\"I can't help but feel a bit simple-minded if all it took for you to snap me out of this last time was....\"" 
    show Haruhi CS Pout2 at TenthLeft
    show Kyon CS Worry1 at right
    nvl clear
    "She trailed off and looked away. \"That wasn't an invitation,\" she added in warning when he lowered his gaze to study her."
    show Haruhi CS Pout1 at TenthLeft
    show Kyon CS Sigh4 at right
    "He raised an eyebrow at her and said nothing before he shrugged, leading the way into the school building." 
    scene bg SchoolEntranceLeft CS
    show Kyon CS Neutral3 at right
    show Haruhi CS Neutral1 at TenthLeft
    with fade
    nvl clear
    "He moved to the same locked door he had smashed the window of last time, but she stopped him with a shake of her head. Didn't he understand? This was the world she was constructing ... not even meaning to ... and he'd gone and told her what she was, here." 
    show Haruhi CS Neutral2 at TenthLeft
    "\"I have the keys,\" she said, willing them to appear in her skirt pocket."
    play sound "SE/DoorOpenFast.wav"
    scene bg hallway CS
    show Kyon CS Neutral3 at right
    show Haruhi CS Neutral1 at TenthLeft
    with fade
    nvl clear
    "Naturally, they did, and he followed her, nonplussed. After a moment, she realized he was holding one hand out, very slightly towards her, though he didn't actually look at her directly." 
    show Haruhi CS Smile1:
        xalign 0.3 yalign 1.0
    show Kyon CS Smile1:
        xalign 0.7 yalign 1.0
    with move   
    "Fighting her own hesitation down, she took his hand in her own, and they walked together to the club room."
    scene bg ClubHallLeft CS
    show Kyon CS Smile4:
        xalign 0.7 yalign 1.0
    show Haruhi CS Smile1:
        xalign 0.3 yalign 1.0    
    with fade    
    nvl clear
    "\"You can take my arm,\" he suggested, just like the last time they had been in this strange space. \"It makes for a better mood.\""
    play sound "SE/dooropenfast.wav"
    scene bg ClubroomFullNight CS
    show Haruhi CS Neutral1 at TenthLeft
    show Kyon CS Neutral3 at right
    with fade
    nvl clear
    "She shook her head at that, then unlocked the door, wondering why she had bothered with keys ... she could just have willed the door open, after all."
    play sound "SE/lightswitch.mp3"
    scene bg ClubroomFullNight
    show Haruhi Neutral1 at TenthLeft
    show Kyon Neutral3 at right
    with dissolve
    "He flipped on the light after releasing her hand and went to the window, gazing outside." 
    play sound "SE/doorclose.mp3"
    show Haruhi Quest1 at TenthLeft
    nvl clear
    "\"Well?\" she asked, breaking the silence and closing the door behind her. \"I'm sure you've got something to say.\""
    show Haruhi Quest2 at TenthLeft
    show Kyon Ser3 at right
    "\"I could say I'm sorry,\" he told her, shaking his head. \"Would that be enough?\""
    show Haruhi Sigh1 at TenthLeft
    show Kyon Ser1 at right
    "\"It's not your fault,\" she sighed. \"I'm just ... really stressed out.\""
    show Haruhi Sigh3 at TenthLeft
    show Kyon Neutral2 at right
    nvl clear
    "He shrugged, turning around and fiddling with the tea kettle for a minute. \"My tea still sucks,\" he warned her. \"It may not be deadly, but I can't promise anything.\""
    show Haruhi Neutral2 at TenthLeft
    show Kyon Neutral3 at right
    "\"You have to change the leaves,\" she observed." 
    nvl clear
    show Haruhi Unhap1 at TenthLeft
    "Then she shook her head again. \"Are you serious? Here we are on the verge of me destroying the world — again! — and all you can think to do is make tea?! Gods, if aliens arrived, what would you do, apologize for being out of crumpets and discuss the Hanshin Tigers?\""
    nvl clear
    show Haruhi Unhap2 at TenthLeft
    show Kyon Sigh1
    stop music fadeout 10
    "He snorted, carelessly dumping the old leaves into the trash and eyeballing a replacement fill of tea leaves from one of the metal cannisters that Mikuru had bought. \"I'm not actually a fan of the Hanshin Tigers.\""
    nvl clear
    show Kyon Sigh2 at right
    stop music
    play music "Music/GodKnowsMusicBox.mp3"
    "\"Setting aside the aliens we've already met.... After dealing with some of the things I have ... last February, I guess it was? Anyway, a while back I told the universe, though in more words, that it could bring any trouble it wanted,\" he said resolutely, his attention focused on the kettle as it heated up." 
    show Kyon Ser3 at right
    nvl clear
    "\"As long as we had the brigade together, I'd be able to handle it. With you in front of me, the others at our sides, and Tsuruya behind us ... I could deal with the smirking bastard, the Sky Canopy Domain.... Whatever the world brings, as long as we're a brigade, what did any of that matter?\""
    show Haruhi Pout2 at TenthLeft
    show Kyon Ser1 at right
    "\"But you get to have {i}fun{/i},\" she protested. \"And all I do is make {i}trouble{/i}. That's not fair for either of us!\""
    show Haruhi Pout1 at TenthLeft
    show Kyon Ser3 at right
    nvl clear
    "\"Now you're being too hard on yourself,\" he said, straightening up with a frown. \"And that's not like you. Maybe I made a mistake telling you what I did.\""
    show Haruhi Crossed Pout2 at TenthLeft
    show Kyon Ser1 at right
    "\"And you only did it because of Yuki,\" she muttered, turning away." 
    nvl clear
    $ _window = True
    show ClubroomFullNight Glow behind Haruhi with dissolve
    $ _window = False
    "A glowing figure appeared on the distant skyline, and she focused her will on it, desperately wishing it would go away.{nw}" 
    $ _window = True
    hide ClubroomFullNight with dissolve
    $ _window = False
    extend " After a shuddering heartbeat, it did, vanishing into motes of light. Kyon seemed not to notice, though he was watching her."
    show Kyon Ser3 at right
    nvl clear
    "\"I would have done the same thing for Asahina-san or Koizumi,\" he returned levelly. \"And if I thought I could help, Tsuruya-san and Kanae-chan as well, even though we've only just met her.\""
    show Haruhi Pout2 at TenthLeft
    show Kyon Ser1 at right
    nvl clear
    "\"What about me?\" she asked quietly. \"I understand that I'm the leader of the brigade, but does that mean that I'm just that?\""
    show Haruhi Pout1 at TenthLeft
    show Kyon Worry1 at right
    "\"That question,\" he said darkly, grimacing. \"You have no idea how long I've struggled with it. I asked myself last May, 'what is Haruhi to me?' You ... probably remember the answer I came up with.\""
    show Haruhi Crossed Pout1 at TenthLeft
    show Hblush Crossed at TenthLeft
    nvl clear
    "She felt her face color and nodded stiffly, turning away again." 
    show Haruhi Crossed Tsun2 at TenthLeft
    "\"And that's what's bothering me,\" she admitted. \"I guess I can't keep it bottled up, or I'll blow up the world as we know it. But reality bends itself the way I want it to. It's not right that {i}you{/i} do, too. How can I feel I'm achieving anything, if I'm cheating without even meaning to?\""
    nvl clear
    show Haruhi Crossed Tsun1 at TenthLeft
    show Kyon Ser1 at right
    "He said nothing for a long minute, pouring the water into the teapot over the tea leaves and ruminating." 
    show Kyon Sigh2 at right
    "\"You're still being too hard on yourself,\" he decided, when pouring was complete. \"If I could only pick one thing to blame myself for, it would be for revealing things to you that changed who you were so much.\"" 
    nvl clear
    show Kyon Puzzle1 at right
    "\"That, honestly, I do regret. I don't regret saving Nagato. I don't regret being honest with you. But causing you pain because of what you know.... That, I never wanted at all. Please believe that, if nothing else.\""
    show Kyon Worry1 at right
    show Haruhi Pout2 at TenthLeft
    hide Hblush
    "\"I still don't know why you're so nice to me,\" she mumbled, staring at the floor."
    show Haruhi Pout1 at TenthLeft
    show Kyon Sigh5 at right
    nvl clear
    "\"I am an endless fountain of support,\" he agreed heartily. \"Telling you when I think your ideas are stupid, being unhelpful when you're starting to drag us into problems, sabotaging baseball tournaments you haphazardly coerce us to join even when I risk destroying the world by intentionally antagonizing you.... That's me, alright! An all around great guy.\"" 
    show Kyon Ser3 at right
    nvl clear
    "He shook his head with a roll of his eyes. \"I'm not sure what's gotten into you, Haruhi, but I'm not as perfect as you act right now, and you're nowhere {i}near{/i} the villain you make yourself out to be at the moment.\""
    show Kyon Ser1 at right
    show Haruhi Neutral1 at TenthLeft
    "She stood up straighter and looked at him closely. Seemingly unconcerned, he filled two cups with tea and handed one to her." 
    nvl clear
    show Haruhi Smile1 at TenthLeft
    "\"You are unreasonably reasonable,\" she accused, unable to keep a tiny smile from forming on her lips."
    show Kyon Neutral3 at right
    "He inclined his head to her very slightly in acknowledgement as he took his seat."
    nvl clear
    show Haruhi Sigh1 at TenthLeft
    "\"Alright, mighty philosopher Kyon,\" she decided, \"riddle me this: what do I do now? I'm stressed out because of all this power I have that's too dangerous to play with, and the idea that I'm forcing people around me against their will — if I'm not outright breaking it. If there were a flaw that you could point out that I needed to fix, what would it be?\""
    nvl clear
    show Haruhi Sigh3 at TenthLeft
    show Kyon Ser3 at right
    "\"You should seek happiness,\" he said without hesitation, sipping at the tea and making a face." 
    show Kyon Unhap1 at right
    "\"Ugh. And don't drink that tea, I think it turned out pretty nasty.\""
    show Haruhi Hips Ang1 at TenthLeft
    nvl clear
    "\"I'm trying to be serious here!\" she yelled. \"This is the end of the world as we know it!\""
    show Haruhi Hips Ang2 at TenthLeft
    show Kyon Smile4 at right
    "\"And I feel fine,\" he said back in a sing-song tone, smirking."
    show Kyon Sigh2 at right
    nvl clear
    "\"Come on, Haruhi. I mean it; you should seek what makes you happy. As far as your flaws, well, I could whine all {i}day{/i}, but to be honest, the one big thing you do is have no real respect for other people's feelings. No empathy.\"" 
    show Kyon Ser3 at right
    "He raised a hand to forestall her protest and added, \"Even so, you've come a {i}very{/i} long way since we first met on that count, so who am I to judge?\""
    nvl clear
    show Haruhi Pout2 at TenthLeft
    show Kyon Ser1 at right
    "\"Oh,\" she replied, deflating."
    show Haruhi Pout1 at TenthLeft
    show Kyon Sigh1 at right
    "\"What, you wanted the boxed shoujou-romance answer of, 'Never change, you're perfect the way you are'?\" he asked, dropping his hand to the table."
    nvl clear
    show Kyon Ser2 at right
    "\"Well, we're real people in the real world, not characters in a television drama or manga. I know you'd be happier with {i}me{/i} if I had more energy and got better grades. None of us are perfect.\""
    show Haruhi Smile1 at TenthLeft
    show Kyon Ser1 at right
    nvl clear
    "\"You sure aren't,\" she retorted, smiling again as she took her seat at the desk and sipped her tea."
    show Haruhi Unhap1 at TenthLeft
    "\"Ugh! You're right, next flaw, your tea is terrible.\""
    show Haruhi Unhap2 at TenthLeft
    show Kyon Sigh2 at right
    "\"I warned you,\" he said gravely, shrugging and sipping his tea anyway. \"Truth in advertising, right?\""
    show Haruhi Crossed Pout2 at TenthLeft
    show Hblush Crossed at TenthLeft
    show Kyon Sigh4 at right
    nvl clear
    "\"Yeah, well,\" she said, crossing her arms over her chest. \"I don't like ... not knowing where we stand with one another. I guess that's selfish.... Damn it, I want....\" She struggled for words, unable to meet his eyes."
    show Haruhi Crossed Pout1 at TenthLeft
    show Kyon Puzzle1 at right
    "\"You want to be in charge?\" he asked, leaning his face on one hand. \"You are the brigade leader, you know.\""
    nvl clear
    show Haruhi Tsun2 at TenthLeft
    show Kyon Worry1 at right
    "\"Yeah, but....\" Shifting her shoulders, she said, \"I'm not happy being a tsundere character. Just like you said, we're real people ... right?\""
    show Haruhi Tsun1 at TenthLeft
    show Kyon Ser3 at right
    "He nodded, frowning slightly. \"I did say that, but I don't know what 'tsundere' means.\""
    show Kyon Ser1 at right
    show Haruhi Quest1 at TenthLeft
    hide Hblush
    nvl clear
    "\"Stereotypical anime relationship?\" she asked. \"Girl likes boy, boy likes girl? Girl hits boy, boy mouths off to girl? You could change the order of operation, but it all works out the same.\""
    show Haruhi Quest2 at TenthLeft
    show Kyon Sigh1 at right
    "\"Oh ... well, that's not a real relationship,\" he agreed. \"Just a mechanic to let the viewers know that a relationship exists while artificially keeping it from developing, since it's a minor point at best in the role of the show. Should have known you'd know the proper term for it.\""
    show Haruhi Grin2 at TenthLeft
    show Kyon Sigh3 at right
    nvl clear
    "\"Don't give me that!\" she snapped playfully. \"I bet you can name a dozen more characters that fit the stereotype than I could!\""
    show Haruhi Grin1 at TenthLeft
    show Kyon Neutral2 at right
    "\"Probably true,\" he acquiesced. \"But I think we're both avoiding the main issue here. That's not us; you don't intentionally cause me trouble, and you listen when I complain. Sometimes, anyway.\""
    show Haruhi Neutral2 at TenthLeft
    show Kyon Neutral3 at right
    nvl clear
    "\"W...well.... I'm not satisfied with your suggestion to make myself happy,\" she said, her smile fading. \"I mean, I know I {i}could{/i}. Just,\" she snapped the fingers of her right hand, \"{i}make{/i} ... things perfect. Clouds of sakura petals on demand, constant appropriate music somehow always surrounding us, no misunderstandings ever....\""
    show Haruhi Neutral1 at TenthLeft
    show Kyon Sigh2 at right
    "\"You'd get so bored of that,\" he said with a sigh, shaking his head. \"Actually, probably so would I.\""
    nvl clear
    show Haruhi Sigh1 at TenthLeft
    show Kyon Sigh4 at right
    "\"Or, I could,\" she snapped her fingers again, \"{i}make{/i} myself happy with whatever happened, so that I was just satisfied all the time no matter what happened.\""
    show Haruhi Sigh3 at TenthLeft
    show Kyon Ser3 at right
    "\"I don't buy that,\" he disagreed, sipping his tea again. \"It'd be just as true of your last suggestion, but the person who looked like you would not be Haruhi if you did that.\""
    show Haruhi Quest1 at TenthLeft
    show Kyon Ser1 at right
    nvl clear
    "\"Wouldn't it be better for the world, though?\""
    show Haruhi Quest2 at TenthLeft
    show Kyon Sigh2 at right
    "\"Honestly? I can't say that for certain,\" he said, shrugging."
    show Kyon Puzzle1 at right
    nvl clear
    "\"Look, I was given ... advice before I came here. And I don't mean to make you feel like this is less important than it actually is, but ... I haven't become the future self that travels back in time to last Sunday, yet." 
    show Kyon Ser3 at right
    "\"As strange as it all may sound, I'm confident that we get through this alright. Even without that knowledge, I'd still believe it to be true, though.\""
    show Haruhi Pout2 at TenthLeft
    show Hblush at TenthLeft
    show Kyon Ser1 at right
    nvl clear
    "\"I ... want to be the person who can make you happy,\" she mumbled, her face coloring. \"I want to be able to draw you into the mysteries around us, and explore all of the fun things that happen ... but {i}together{/i}.\""
    show Haruhi Pout1 at TenthLeft
    show Kyon Smile1 at right
    "He nodded. \"Okay,\" he agreed. \"That sounds fine to me. There's no conspiracy trying to keep things hidden from you, anymore.\""
    nvl clear
    show Haruhi Pout2 
    "\"What I really wanted,\" she said softly, \"was to some day be the ... girl that ... you would confess to.\""
    show Kyon Puzzle1 at right
    show KBlush at right
    "Looking away with a grimace, he sighed. \"I get that,\" he said quietly. \"And don't think it hadn't crossed my mind. But ... and don't take this the wrong way, but what could myself, who has never had an actual girlfriend, offer to someone with your confidence? Your dating history?\""
    show Kyon Worry1 at right
    show Haruhi Hips Ang3 at TenthLeft
    show Hblush Hips at TenthLeft
    nvl clear
    "\"I'll have you know that our first kiss in May was my first kiss,\" she protested hotly, her face turning red. She felt Shinjin forming, smashing apart distant buildings, and struggled to disperse them. \"I wanted to {i}meet{/i} people, I am {i}not{/i} that kind of girl! Hell — you didn't even {i}ask me for permission{/i}!\""
    show Kyon Worry2 at right
    show Haruhi Hips Ang4 at TenthLeft
    nvl clear
    "He winced, ducking his head. \"Sorry; I didn't think you were! I just meant ... you know about relationships and how they're supposed to work."
    show Kyon Puzzle1 at right
    "\"You show almost unlimited confidence. What am I able to or supposed to bring to the table? It's not that I wouldn't like to try, but....\"" 
    show Kyon Worry1 at right
    nvl clear
    "\"What do I do when I fail you? When it's not enough? I want to try my best, but I {i}am{/i} just a normal person with extraordinary friends. Being dragged along behind you while weakly protesting is one thing ... but being rejected because you're bored with me....\"" 
    show KTears at right
    nvl clear
    "He trailed off and looked away, his face displaying a raw vulnerability she didn't think she had seen on it before. His eyes were shining, as though...."
    nvl clear
    hide Hblush
    show Haruhi Unhap2 
    "He wasn't so great an actor that he could be faking it; he might maintain an impassive facade at times, but assuming some other emotion? She spent a long time mulling over what he said, studying that expression before she forced herself to act." 
    show Haruhi Sigh1 at TenthLeft
    nvl clear
    "\"Okay,\" she acquiesced, nodding. \"I guess ... I can see your point of view. So,\" she said, her voice shaking a little bit, \"I need to forget about my power.\""
    hide KTears
    hide KBlush
    show Haruhi Sigh3 at TenthLeft
    show Kyon Neutral4 at right
    "He blinked at her, taken aback."
    nvl clear
    show Haruhi Pout2 at TenthLeft
    "\"Or, not entirely forget, but ... um ... rewrite how I remember it a bit. I want to have a power, but I want something I can have fun with that doesn't mean destroying the universe on an accidental whim.\"" 
    show Haruhi Focus1 at TenthLeft
    nvl clear
    "She closed her eyes and took a deep breath. \"Here it goes,\" she decided. \"I trust you, Kyon ... if I can't trust you, I can't trust anyone. So ... I'm going to have a minor power to affect things ... objects, anything more, I'll need Yuki-chan's help with, until I can learn to be responsible with that power.\""
    show Kyon Sup2 at right
    nvl clear
    "\"Haruhi,\" he said, with the sound of his chair scraping across the floor as though he were standing up, \"you don't need to do this—\""
    show Haruhi Sigh2 at TenthLeft
    nvl clear
    "\"Shut up,\" she ordered tersely. \"My power's going to be more limited so I {i}can{/i} play with it without hurting or scaring people. I'm going to make myself ... a tiny bit more open-minded ... with regards to you. Don't say a word! You will thank me for this later! And then, um, I'm going to believe that if we all work together, like you believe, we can make the world a better place.\""
    nvl clear
    show Haruhi Pout2 at TenthLeft
    "She nodded decisively, then opened her eyes. \"B...because I trust you, I'm going to try not to remember this when I wake up,\" she added. \"And ... you can tell me you're John Smith again if you need me to know everything, for some reason.\" He was standing close to her, one hand on her desk as he peered at her intently."
    show Haruhi Pout1 at TenthLeft
    show Kyon Worry2 at right
    nvl clear
    "\"You're sure about this?\" he asked anxiously. \"You're ... still going to be the same Haruhi I know?\""
    show Haruhi Neutral2 at TenthLeft
    show Kyon Worry3 at right
    "\"More than I have been lately,\" she agreed, nodding. \"I hope, anyway. Why else would I be giving you an emergency reset codeword? I may not have a mind like Yuki's, but I can still think ahead!\""
    nvl clear
    $ _window = True
    show Haruhi Smile1 at center with move
    show Hblush at center
    $ _window = False
    "She rose from her seat smoothly, still gazing up into his face. \"So ... just in case I get this wrong, I want you to do what we did last time, so I'll have a good note to go out on.\""
    show Kyon Smile1 at right
    show KBlush at right
    "He stared at her for a moment before a slow smile spread across his face. \"I'm going to do my best, Haruhi,\" he promised her, his hands rising to her shoulders, then sliding up to gently cup her cheeks." 
    nvl clear
    scene bg Kiss with slowdissolve
    "She let her eyes drift shut as her head tilted back and her lips pursed, the last thought through her mind as everything turned into light that he would probably notice the small change she had made in him, as well.... But he probably wouldn't mind too much."
    nvl clear
    stop music fadeout 8
    
    call eyecatch("Thursday, April 21") from SF3_sc001
    
    play music "Music/Nichijou.mp3"
    scene bg KyonRoomRightMorning with fade
    play sound "SE/impact.mp3"
    "Kyon leapt out of bed with a handspring, landing in a crouch before the opening door and lunging instantly into the forbidden little-sister-submission-tickle-strike, completely foiling her attempt to sneak in and wake him up first. Only after he had reduced her to a shrieking, laughing pile, and his mother was tiredly staring up at the pair of them from the bottom of the stairs did he relent."
    show Kyon Neutral3 at right
    show Nonoko Laugh1 at TenthLeft 
    with dissolve
    "\"T...tickle-ninja!\" his sister protested, her face red from laughter. \"No fair!\" "   
    nvl clear
    show Kyon Smile3 at right with dissolve
    "\"When you wake up with as much energy as I do,\" he told her sternly, \"no surprise attack is going to be effective enough.\" "
    "He grabbed his sister's wrists and hauled her upwards, leaving her to dangle a few centimeters over the floor before gently lowering her to stand and releasing her. She stuck her tongue out at him, giggling, then ran down the stairs to their mother."
    nvl clear
    scene bg KyonHouseDay with fade
    show Nonoko Sup1 at TenthLeft 
    show Kyon Smile1 at right 
    with dissolve
    "\"Mom!\" she yelled. \"Kyon-kun had his brain eaten by a pod-person! The alien that's replaced him wakes up in the morning without needing help!\" "
    show Nonoko Smile1 at TenthLeft
    "\"That's very nice, dear,\" he heard his mother say as she bustled back into the kitchen. \"Maybe he'll get good grades, too. Now wash up before breakfast.\" "
    nvl clear
    show Kyon Worry1 at right
    "\"Hmm,\" he mused, his smile fading as his dream and the vague, uncertain memory of Yuki's 'training' session replayed themselves in his mind. The training was a headache, and he had thought oddly draining.... Maybe Yuki just hadn't perfected it, the first time? Even so, it was hard to grin when he considered what Haruhi might have done to herself that night."
    nvl clear
    "Even if his future self would evidently find nothing worth mentioning to him via the letter he had passed to Haruhi, or a hidden message elsewhere. {nw}"     
    show Kyon Neutral2 at right    
    extend "After washing, gobbling down everything his mother put in front of him and still feeling hungry, he told his mother and sister, \"There's a math test tomorrow; I'm headed in early to study.\" "
    show Nonoko Yell1 at TenthLeft
    "\"Pod-person!\" his sister yelled, as he left the house."
    nvl clear
label test2:
    stop music fadeout 1
    scene almostblack two with fade
    queue music "Music/Aruame.mp3"
    "She woke up, staring at the ceiling of her room and blinking. She'd had a dream.... She knew it was important, but the details kept slipping just out of her reach. She got out of bed and went about her morning routine, concentrating on the hazy recollections. Kyon was there ... and it was at school."
    "Something had been different about it, she was certain, but all she could remember was the kiss. And she'd had {i}that{/i} dream before. Before Kyon's revelation to her that she had a power. Remembering that she could do such things, and ensuring no parents were around to witness it, she closed one eye and pointed at a toothbrush, pleased as it wobbled unsteadily out of the holder and drifted to her hand."    
    nvl clear
    "Good, she thought. {i}That{/i} hadn't been a dream ... even if kissing Kyon had been. She felt her face warm up as she remembered the conversation she had with Yuki and Mikuru the day before. Even Kanae had some input, despite her relative newness to the group."
    "\"I said I'd help him with his homework,\" she realized aloud, hurrying her pace and rushing to the kitchen. No parents around, still, which was good for today. That meant she could cheat. He always gave her a long-suffering sigh and mumbled about responsibility when she did, but what he didn't know, he couldn't whine about."
    nvl clear
    "So, under her dutiful eye, she watched utensils and ingredients dance across the kitchen, laboring as intently as a quartet of herself ... or a single eight-armed girl, she supposed, but that thought caused her control to wander. Focusing more intently, she watched as preparations finished, then spent an annoying ten minutes combing through every cupboard and pantry door in the house until she found her old bento and the spare. \"He'd better appreciate this,\" she mumbled, wrapping them both after packing them unreasonably full."
    "That done, she tucked the packages into her bag and settled on stuffing the remaining portion of rice and assorted bento ingredients into a single tupperware. Inelegant, but she could eat while drilling him on his homework. She hurried out the door and to school."
    nvl clear
    stop music fadeout 1
    scene bg SchoolEntranceLeft
    queue music "Music/ItsumoNoFuukei.mp3"
    show Haruhi Neutral1 at TenthLeft with dissolve
    "Stopping just before the gates, she realized she hadn't thought so specify where he was to meet her, so flipped her phone open and called him."
    show Haruhi Ang4 at TenthLeft
    "\"Kyon!\" she barked, the second he picked up. \"Why aren't you here yet?\""
    show Kyon Smile2 at right with dissolve
    "He said nothing in response, merely stepping from behind the gatepost he had been leaning against with a raised eyebrow."
    nvl clear
    show Haruhi Grin2 at TenthLeft
    "\"Well-played,\" she allowed, flipping her phone closed. \"For once, you dodge a penalty!\""
    show Kyon Smile3 at right
    "\"You're in a good mood,\" he said, rubbing his chin thoughtfully as he closed and pocketed his own phone. \"Have a good dream last night?\""
    nvl clear
    $ _window = True
    hide Haruhi with moveoutright
    $ _window = False
    "She fought to keep her face from coloring, and quickly jogged past him so he couldn't see her expression. \"Wouldn't {i}you{/i} like to know,\" she said with a chuckle. \"Come on, let's study in the club room.\""   
    nvl clear
    
    stop music fadeout 1
    scene bg ClubroomCenterDay with fade
    queue music "Music/Nanika.mp3"
    
    show Haruhi Ang2 at TenthLeft
    show Kyon Sigh1 at right
    with dissolve
    "\"Pathetic,\" Haruhi told him between bites of her delayed breakfast, observing Kyon's progress through his homework."    
    show Kyon Sigh2 at right
    "\"Thanks for the morale boost,\" he grumbled, struggling with another answer.{nw}"    
    show Kyon Ser2 at right    
    extend "\"Okay,\" he declared, finishing one of the many problems he had remaining. \"I'm not going to make it. I'll focus on the classes that happen before lunch, and finish the rest later. Math's an afternoon class, so....\""    
    nvl clear    
    show Haruhi Focus1 at TenthLeft    
    "She nodded dubiously, then turned around and put something in the club room's mini-fridge. He flipped through the history notes she had written, paying special attention to where she had underlined specific dates or names. History was defeated quickly, thanks to the accuracy of Haruhi's notes, and the sketchy grammar notes she had left were more than enough to bolster his own knowledge in that regard. It may not have been much, but at least he had one good subject...."
    nvl clear    
    "\"You hungry?\" she asked."    
    show Kyon Neutral2 at right
    "He nodded, glancing briefly at her before turning back to his homework. \"A bit,\" he admitted. \"Just don't feel like I'm getting enough these days. Constantly ravenous.... And I slept through dinner last night.\" He sighed, breaking from his homework to stretch his arms overhead. \"I really need to stop doing that.\""
    nvl clear
    show Haruhi Grin2 at TenthLeft
    "\"Nighttime heroics?\" she teased him, smirking. {nw}" 
    show Haruhi Hap4 at TenthLeft
    extend "\"Alright. If you finish your homework for the periods before lunch, I'll let you have my leftovers during break. It's a good deal, you know! But the brigade chief can't just hand out rewards with no rhyme or reason, so, be sure to earn it!\""
    nvl clear
    show Kyon Smile4 at right
    "\"Sure thing,\" he agreed, finishing up the last few lines he needed before he was done. \"Lucky there's no essay,\" he added, clenching and unclenching his right hand to relieve the writer's cramp he'd started to develop. After a glance at the clock, he started packing his homework and the notes Haruhi had made for him into his schoolbag. \"But, seriously Haruhi ... thanks for helping me out with my homework.\""
    nvl clear
    show Haruhi Sup1 at TenthLeft
    "Her face colored very slightly, {nw}"
    show Hblush at TenthLeft
    show Haruhi Hap2 at TenthLeft
    extend "but she puffed out her chest and lifted her nose to sniff imperiously. \"I told you once, and I'll say it again,\" she insisted, \"no vice commander of mine is going to settle for bad grades when they can obviously earn better!\" She relaxed her stance a bit, stealing her own glance at the clock but not moving to collect her bag."
    nvl clear
    show Haruhi Pout1 at TenthLeft
    "\"But....\" After a brief hesitation, she blurted out, \"I'd help you even if you weren't the vice commander,\" without meeting his eyes. \"I'd do it for any member of the brigade ... you're just the only one that doesn't do well.\""
    nvl clear
    show Kyon Unhap1 at right
    "He winced, realizing that it was true.... Koizumi was smart enough that he was placed by his own merit, not Organization manipulation. Yuki's average was only short of being perfect by the four percent of answers she simply didn't bother completing. Mikuru struggled for her grades, but diligently did her homework despite brigade duties." 
    nvl clear
    "Haruhi, naturally, was Haruhi. So he had no real excuse for poor grades except for being unintelligent. His head sank, considering that. He couldn't even think to try and seek solace in Kanae's grades, whatever they were. It just didn't seem right to judge himself against an underclassman."
    "\"Yeah,\" he allowed after a moment. \"It's a bit sad being the dumb one.\""
    nvl clear
    hide Hblush
    show Haruhi Unhap1 at TenthLeft
    "\"You're not dumb,\" Haruhi retorted with an instant roll of her eyes, snickering. \"You quote string theory and ancient philosophy offhand. I've seen your grades for grammar — and English. Obviously, your issue is motivation. You don't {i}really{/i} need my help with your homework ... it just seems that if I don't help you, you don't {i}do{/i} it.\""
    nvl clear
    show Kyon Smile2 at right
    "She had him there, he realized, grimacing. \"Touche,\" he allowed, smirking. He decided to take a stab at something, unsure what Haruhi had let herself remember of the 'dream' the night before. \"Hey, can I ask you something?\""
    show Haruhi Sigh1 at TenthLeft
    "\"Sure,\" she said quickly, nodding at him. \"But, we should head to class.\""
    nvl clear
    show Kyon Puzzle1 at right
    "He rose from his seat and hefted his bag, while she shoved her own collection of papers into her bag. \"Haruhi, if I can ask you to be honest about this ... when you say you would do it for anyone in the brigade ... don't you really mean any of your friends?\""
    nvl clear
    show Haruhi Sup1 at TenthLeft
    "She made a choking noise, dropping the tupperware container on the floor. It remained sealed, and she hid her expression from him while she stooped to collect it. \"W...well, if you're going to be so blunt about it,\" she managed, her face dark with a blush. {nw}" 
    show Hblush at TenthLeft
    show Haruhi Unhap2 at TenthLeft
    extend "She stomped one foot on the floor and waved the tupperware menacingly. \"Why are you asking me this now?!\""
    show Kyon Worry1 at right
    "\"It was something Kanae-chan mentioned the other day,\" he said with a shrug, opening the clubroom door. {nw}" 
    play sound "SE/dooropenfast.wav"
    extend"\"She said she was occasionally 'lucky enough to have friends'. I just sometimes worry that you forget that your fellow brigade members are friends, too, not only subordinates in the club.\""
    nvl clear
    show Haruhi Ang4 at TenthLeft
    "\"Man,\" Haruhi grumbled, closing the door then hurrying to Kyon's side, \"you make it sound like I can't stand having equals!\""
    hide Hblush
    show Haruhi Hap4 at TenthLeft
    play sound "SE/impact.mp3"
    "She playfully punched him in the shoulder, though he was surprised that it didn't sting in the slightest, even though he felt it. \"What, do you think that just because you're getting your homework done, now, I've turned stupid on you? Or weak? You know, if you had the chutzpa for it, you could have formed the SOS Brigade and I would have followed....\""
    nvl clear
    scene bg stairwell with fade:
        size (800,600)
    #play sound "SE/footsteps13.mp3"
    show Kyon Smile3 at right
    "He glanced at her sidelong as they stepped into the stairwell. \"Really?\" he asked, raising one eyebrow. \"I find it hard to imagine....\""
    show Haruhi Grin2 at TenthLeft
    "\"That's because you're laaaazy,\" she said, drawing out the sound and sticking her tongue out at him. \"If you had actually made the club instead of just giving me the idea.... But that's also why you're not an idiot, even if you do dumb things sometimes.\""
    nvl clear
    scene bg hallway with fade
    show Kyon Smile2 at right
    "\"Sing on sweet angel;\" Kyon retorted with a roll of his eyes, \"mine ears ache for thy faint praise; damning though it be.\""
    show Haruhi Grin1 at TenthLeft
    "She snickered at him, narrowing her eyes as though she knew something he didn't. \"Oh, and now the refuge in sarcasm,\" she chided him. \"Sometimes, you are sooooo predictable. Hey, when did you pick up poetic verses, anyway? The haiku is kind of new.\""
    nvl clear
    show Kyon Sigh4 at right
    "\"Felt a little left behind when you and Tsuruya were passing back and forth those poems you memorized a while back,\" he admitted. \"I read up on the style, but didn't feel like destroying precious brain cells to memorize anything.\""
    show Haruhi Unhap1 at TenthLeft
    play sound "SE/dooropenfast.wav"
    "\"That's exactly what I'm saying!\" Haruhi protested, stomping one foot on the floor as he slid open the door to the classroom. \"You're {i}lazy{/i}.\""
    nvl clear
    scene bg classroom with fade:
       size (800,600)
    "She fell silent at the sight of the classroom, all other students already seated, glancing over their shoulders at the pair. Everyone quickly looked away, though at a glance, Okabe-sensei hadn't arrived yet either. Shrugging, Kyon closed the door after Haruhi stepped through and went to his desk."
    "\"Anyway,\" Haruhi continued in a semi-hushed tone, eyeing the other students in the room, \"what's going on, here?\""
    "\"No idea,\" he tossed back just as quietly. His eyes scanned across Kunikida and Taniguchi, but both of them kept their eyes oriented directly forward. \"Seems a bit odd, though.\""
    "\"Eh,\" Haruhi mused, tapping a fingertip on her desk thoughtfully. \"Well, I'm sure it's nothing ... probably.\""
    "Kyon nodded, getting out his homework for the next period as well as the detested, unfinished math. If there was no teacher around...."
    nvl clear
    
    stop music fadeout 1
    scene bg classroom with fade:
       size (800,600)
    play sound "SE/WestminsterChimeShort.mp3"
    pause 4
    queue music "Music/Yuuutsu.mp3"
    "After the first period chime rang, Haruhi leaned back in her seat, sticking her feet out straight off the floor to stretch her calf muscles, and extended her arms over her head, balancing precariously. She felt something in her lower back pop into place and smiled slightly, turning her head to Kyon as she leaned forward, her toes touching the floor once more. Before she could speak, she saw Sakanaka rise from her seat two desks to the right and pad cautiously towards the door, beckoning Haruhi to follow."
    "After only a moment of consideration towards Kyon, who seemed to be behaving by working on his math homework, she tapped his shoulder and handed him the tupperware of leftovers. \"Keep up the good work, subordinate,\" she encouraged him, climbing to her feet and striding into the hallway to see what Sakanaka wanted."
    nvl clear
    scene bg hallway with fade
    show Haruhi Hap1 at TenthLeft with dissolve
    "\"Hey,\" she said to the other girl, once they were in the hallway and out of earshot from the other students. \"What's up, Sakanaka-san? Is JJ still okay?\" She made a mental note to try and visit Sakanaka sometime relatively soon ... since Yuki had fixed the problem of 'haunted' dogs, Haruhi hadn't had a chance to play with the terrier."
    nvl clear
    "\"He's fine,\" Sakanaka replied, smiling weakly. \"Um, Suzumiya-san, I don't mean to alarm you ... but ... um.... W...well, I feel I owe you honesty after everything you did for Rousseau. I'm sorry to be the one who bears this news to you, but....\""
    nvl clear
    show Haruhi Neutral1 at TenthLeft
    "\"Well?\" Haruhi asked, restraining the urge to tap one foot through sheer will alone. What news could Sakanaka have that would be important or critical? Given the powers of the SOS Brigade, what could even really be a concern? Though, she made herself realize, there was no way anyone outside of the SOS Brigade could know that."
    "Unable to meet her eyes, Sakanaka blurted out, \"Suzumiya-san, there's a rumor going around that Kyon-kun is two-timing you with Tsuruya-sempai!\""
    nvl clear
    show Haruhi Sigh3 at TenthLeft 
    show Haruhi Neutral2 at TenthLeft
    "Haruhi blinked, staring at her classmate, and tried to suppress the smirk she felt forming. \"Really?\" she asked. \"That's ... pretty funny. So, where did this rumor start from?\""
    "\"Er ... that is....\" Sakanaka visibly deflated, staring at the floor. \"Tsuruya-sempai said it herself. R...really, I wouldn't believe a rumor spread about you offhand. But, others may, and.... Well, I feel you should know the truth!\""
    nvl clear
    show Haruhi Sup2 at TenthLeft
    "\"She....\" Haruhi blinked and waved a hand dismissively. \"What {i}exactly{/i} did Tsuruya-san say?\""
    "\"I ... don't really trade in rumors, so I only overheard it from Yanagimoto- kun,\" Sakanaka allowed. \"But she insists that she verified it with Tsuruya- sempai herself.\""
    show Haruhi Neutral1 at TenthLeft
    "\"Yanagimoto,\" Haruhi murmured, concentrating. \"Oh, yeah, I remember her from when I joined the rhythmic gymnastics club. She sits in front of Goto-kun, right?\""
    nvl clear
    "\"Right,\" Sakanaka agreed. \"I don't ... want to cause trouble. I just thought you should know.\""
    show Haruhi Sigh3 at TenthLeft
    "\"Well, it's a misunderstanding,\" Haruhi said with a shrug. \"Last I heard, Kyon trashed some goons who were giving Tsuruya-san some trouble.\" Though, he was time traveling at the time, and technically, hadn't done it {i}yet{/i}. \"On Sunday, right?\""
    nvl clear
    "\"Um, maybe that's it,\" Sakanaka agreed with a weak shrug, trying to smile. \"There is ... another thing about Kyon-kun....\""
    show Haruhi Quest2 at TenthLeft
    "Haruhi raised an eyebrow. \"What else is it? And who's spreading all these rumors?\" she asked."
    nvl clear
    "\"Aside from him ... um ... spending time with Tsuruya-sempai yesterday, he got into a fight with Ryuguu-san from class 3-4,\" Sakanaka added in a very hushed tone. \"No one is certain why, but, um, Ryuguu-san hasn't come back to school yet today. This fighting ... Kyon-kun's gathering a bit of a reputation as a delinquent.\""
    nvl clear
    show Haruhi Neutral2 at TenthLeft
    "\"Seems kind of sudden for him,\" Haruhi mused. \"But, hey, as long as he doesn't get in trouble with the school, what does it matter?\""
    "Sakanaka blinked, her eyes wide. \"Y...you don't care that he could be a violent person?\" she asked, astounded. \"That he spends time with other girls?\""
    nvl clear
    show Haruhi Sigh3 at TenthLeft
    "Haruhi shrugged, shaking her head. \"Nah, I'll give him a stern talking to, let him know he should watch his reputation,\" she said in answer. \"Him spending time with other girls {i}would{/i} bother me ... but Tsuruya-san's an honorary member of the SOS Brigade. How can I get mad at him for taking care of brigade business with her?\""
    nvl clear
    "\"I'm glad,\" Sakanaka decided, giving Haruhi a bright smile. \"I worried for nothing, then; sorry to trouble you, Suzumiya-san!\""
    show Haruhi Hap1 at TenthLeft
    "\"No trouble at all,\" Haruhi returned, nodding at the other girl. \"Thanks for the update anyway. It's good to know where the brigade stands in the scheme of things....\" She glanced down the hallway, where their next teacher was approaching. \"Well, maybe we can chat later; I want to give Kyon a few choice words before class.\""
    nvl clear
    scene bg classroom with fade:
       size (800,600)
    "She hurried back in and took her seat, unsurprised to see Kunikida and Taniguchi shoulder-to-shoulder at the side of Kyon's desk. Watching quietly, she caught the tail end of whatever conversation they were having, Taniguchi shooting her a nervous look before saying, \"Anyway, Kyon ... I'm just saying you should watch yourself.\""
    "Kunikida gave a matching solemn nod with his taller, more perverted counterpart, then both boys moved back to their own desks. Kyon shook his head, watching them leave, then hurriedly shoveled the last few bites of leftovers into his mouth as the teacher strode into the classroom. While the teacher was setting up his notes, and the other students' final murmurs began to die down, she whispered, \"Kyon!\""
    nvl clear
    "\"Yeah?\" he asked, not quite turning around."
    "\"Take note! You're going to go back to yesterday and help Tsuruya out with something after school.\""
    "\"I gathered,\" he sighed, taking a fresh sheet of paper and writing notes to himself."
    "Haruhi nodded thoughtfully, though he wouldn't be able to see the motion. It was a real pity she couldn't time travel herself, but at least she could be a significant contributor to Kyon's efforts in that regard."
    nvl clear

    stop music fadeout 1
    queue music "Music/Itsumo(Movie).mp3"
    scene bg hallway with fade
    show Haruhi Smile1 at left with dissolve
    show Mikuru Neutral1 at right with dissolve
    show Tsuruya Hap6 at center with dissolve
    "After the lunch chime rang, Haruhi ordered Kyon to report to the clubroom, then immediately took off in search of Tsuruya. She skidded to a halt in the corridor before the girl's class, watching her walk out of her room with Mikuru just behind her. \"Oh! Haru-nyan!\" Tsuruya said cheerfully, waving the hand that wasn't carrying her lunch. \"Good to see you!\""
    nvl clear
    show Haruhi Hap1 at left
    "Haruhi smiled back, unable to keep her cheer down. \"Good to see you too, Tsuruya-san,\" she agreed. \"Oh, a bento? You and Mikuru-chan should come have lunch with us in the brigade room!\""
    show Tsuruya Laugh1 at center
    "\"Yeah!\" Tsuruya agreed, nodding vigorously. \"I wanted to thank Kyon-kun for his help yesterday!\""
    show Haruhi Smile2 at left
    "Haruhi grinned, turning her attention to Mikuru, who seemed less tired than the previous day. \"Feeling better rested, Mikuru-chan?\""
    nvl clear
    show Mikuru Think Quest1 at right
    "\"Yes,\" the time traveler agreed hesitantly, looking around at the surrounding students. Haruhi was annoyed to realize that the other students had gathered around, defining a circle around the trio, almost as though they expected Haruhi and Tsuruya to fight. \"Um ... what's everyone looking at us for?\""
    show Haruhi Smile3 at left
    "\"Jealous over our good looks,\" Haruhi replied without hesitation, ratcheting her grin wider. \"Anyway, off to the clubroom!\""
    nvl clear
    "The sensation of excitement thwarted from the other students was practically palpable. {nw}" 
    show Haruhi Unhap2 at left    
    extend "\"Idiots,\" Haruhi grumped, once they were underway to the clubroom, out of earshot."
    show Tsuruya Quest1 at center
    "\"Eh? Goons giving you a hard time too?\" Tsuruya asked sympathetically."
    show Haruhi Unhap3 at left
    "\"Huh? Oh, just ... there's some rumors going around,\" Haruhi said with a grimace. \"Stupid stuff. Evidently some people are saying that Kyon is two- timing me with you.\""
    nvl clear
    show Tsuruya Hap6 at center
    "\"Haha! That's not right!\" Tsuruya said with a chuckle. \"I'm borrowing him for my investigation! Oh, he said you were okay with it, but I never got to ask you.... You don't mind, I hope?\""
    show Haruhi Neutral2 at left
    "\"Doesn't bother me,\" Haruhi replied."
    show Mikuru Think Sup1 at right
    "\"T...two-timing!?\" Mikuru yelped belatedly, realization settling in. \"N...no! Suzumiya-san, Kyon-kun would never—\""
    nvl clear
    show Haruhi Hap1 at left
    "\"Actually, Mikuru-chan,\" Haruhi overrode the time traveler, \"we'd need to be {i}dating{/i} for him to cheat on me. So if he would or wouldn't doesn't even matter — technically, he {i}can't{/i}.\""
    show Mikuru Think Sad2 at right
    "\"W...well...\" Mikuru tried to begin. \"Um, even so....\""
    show Tsuruya Hap1 at center
    "\"I think I agree with what Mikuru-chan is trying to say,\" Tsuruya said, shrugging helplessly, still grinning. \"Kyon-kun wouldn't do that to you, Haru- nyan.\""
    nvl clear
    show Haruhi Smile1 at left
    "\"That's entirely not the point,\" Haruhi countered, though she couldn't help the little glow she felt inside at the reassurances. \"Moving away from {i}those{/i} rumors, I'm more interested in the ones about Kyon behaving like a delinquent.\""
    show Mikuru Think Sup1 at right
    "\"Eh!?\" Mikuru protested, her eyes wide. \"Kyon-kun?\""
    show Tsuruya Laugh1
    "\"Delinquent?\" Tsuruya followed, actually clapping one hand over her mouth to stifle the laughter. \"Him!?\""
    nvl clear
    "\"I know, right?\" Haruhi said, smirking as they topped the stairs to the clubhouse and she reached for the doorknob. She wrenched it open as she usually did, catching part of a conversation between Koizumi and Kyon, both seated at the table. Yuki was seated in the corner, flipping through yet another book silently."
    nvl clear
    
    play sound "SE/dooropenfast.wav"
    stop music fadeout 1
    queue music "Music/Unzari da.mp3"
    scene bg ClubroomFullDay with slowflashbulb:
        xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    show Koizumi Crossed Smile1 at center with dissolve
    "\"...greater self-contro— Ah, sorry,\" Koizumi said, breaking off with a grin, turning to look at her. \"Hello, everyone! Are we going to be meeting for lunch regularly, now?\""
    show Haruhi Point Hap1 at left with dissolve
    "\"Not a bad idea,\" she agreed, closing the door once everyone else was in. \"Hmm, where's Kanae-chan? Ah! Kyon, once you finish eating, go find her, will you?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Kyon Neutral3 at center_RightScreen with dissolve
    "\"Yeah, yeah,\" he replied with his standard lack of enthusiasm, bolting his last few bites away. \"You happen to know her classroom?\""
    show Mikuru Neutral2 at right_RightScreen with dissolve
    "\"Um, 1-7,\" Mikuru offered helpfully, taking a seat at the table."
    hide Kyon
    show Tsuruya Hap4 at center_RightScreen
    with dissolve
    "Kyon rose and nodded, while Tsuruya slipped into the seat he had only just vacated. \"Thankie again for yesterday, Kyon-kun!\" the cheerful girl called out."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kyon Smile1 at right
    "\"No problem,\" he replied, heading towards the door. He paused with one hand on the knob and added, \"Though, if you want to update Haruhi on the situation, that'd save me some work.\""
    hide Kyon Smile1 with dissolve
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Tsuruya Hap3 at center_RightScreen
    "\"You got it!\" Tsuruya said brightly, grinning. Once Kyon was out the door, she turned to face Haruhi and asked, \"Did he tell you what he did on Sunday?\""
    show Haruhi Quest1 at left_RightScreen with dissolve
    nvl clear
    "\"You mentioned it,\" Haruhi said, pulling a bento from the refrigerator and pushing her chair around the desk to sit at the table with the others. \"But I was helping Kyon with his homework, so we didn't have a lot of time to discuss it. Why?\""
    nvl clear

    stop music fadeout 1
    queue music "Music/SeishuniiJanaiKatsuNoVocal.mp3"
    show Tsuruya Neutral1 at center_RightScreen
    "\"Well,\" Tsuruya said, her eyes narrowing as she peered around. \"There's a dark conspiracy underway,\" she said in a very quiet voice. \"Some peoples are doing unsavory things in the background! Naturally, I tried to investigate them so that I could takes care of them!"
    show Tsuruya Ang1 at center_RightScreen
    "But unsavory things are done by unsavory peoples, so ... on Sunday I found out the peoples responsible, but they were a bit rougher than the kind you can talk things out with! They outnumbered me and Kasai, and I thought I was in big trouble for sure when they knocked him down!\""
    show Haruhi Quest2 at left_RightScreen
    "\"Kasai?\" Haruhi asked."
    nvl clear
    show Tsuruya Neutral1 at center_RightScreen
    "\"Yeah! My bodyguard,\" Tsuruya said, nodding quickly. \"Anyway, Kyon-kun saved the day, so Kasai is goings to make it, though I was worried for a bit! That would be very bad, to have him be permanently injured for a little investigations on my part ... it'd make me look bad, too!\"" 
    show Tsuruya Laugh1 at center_RightScreen
    "She mimed a jabbing motion with one fist, grinning. \"I gots some training, but Kyon-kun was like a can of carbonated Bruce Lee and Jackie Chan that got all shook up! Bam! Pow! No joke, Haru-nyan, there were twelve of those bad guys still standing when Kyon came in, and there were none when he was done!\""
    nvl clear
    show Haruhi Quest1 at left_RightScreen
    "Haruhi raised one eyebrow. How much had Kyon actually learned from Yuki? At a glance, the girl in the corner only turned the pages in her book, nearly silently, not even looking up."
    show Mikuru Think Sup1 at right_RightScreen
    "\"K...Kyon-kun ... fought people?\" Mikuru asked, her face turning pale. \"W...was he in danger? Wait! Tsuruya-san — were {i}you{/i} in danger!?\""
    nvl clear
    show Tsuruya Laugh2 at center_RightScreen
    "\"I'm fine, Mikuru-chan! Kyon-kun was there!\" Tsuruya said brightly, sticking her tongue out before unwrapping her bento." 
    show Tsuruya Neutral1 at center_RightScreen
    "\"Anyway, after helping me get Kasai to the hospital, Kyon-kun found out about my investigations and said that he wouldn't take no for an answer — he had to help me out with it, especially since Kasai was injured, and I wouldn't haves a bodyguard for the next few weeks while he was recovering.\""
    nvl clear
    show Mikuru Think Sad1 at right_RightScreen
    "\"W...weeks?\" Mikuru managed, wobbling unsteadily in her seat."
    show Koizumi Think Ser4 at center
    $ renpy.layer_at_list([PanScene_RightToLeft])
    "\"I gather that these weren't just random thugs,\" Koizumi murmured, one hand stroking his chin thoughtfully. \"Tsuruya-san, I don't mean to be rude, but were they Yakuza?\""
    show Tsuruya Hap2 at center_RightScreen
    $ renpy.layer_at_list([PanScene_LeftToRight])    
    "\"Ooh! Naturally,\" she agreed, nodding brightly. \"Yous are a sharp one, huh?\""
    nvl clear
    show Mikuru Sigh1 at right_RightScreen
    "\"H...hehe...\" Mikuru wheezed, slumping in her chair in a faint."
    show Haruhi Sigh2 at left_RightScreen
    "\"That girl has got to get some spine,\" Haruhi muttered.{nw}" 
    show Haruhi Quest1 at left_RightScreen
    extend "\"What about yesterday, though?\""
    show Tsuruya Laugh1 at center_RightScreen
    "\"Oh, that,\" Tsuruya said with a chuckle. \"Well, my investigation's still top- secret, so I can't say anythings about it to anyone but Kyon-kun until it's resolved.\""
    nvl clear
    show Haruhi Eyeroll1 at left_RightScreen
    "\"You really think I would be satisfied with that?\" Haruhi asked flatly. \"I could easily revoke your Kyon-borrowing privileges, you know!\""
    $ _window = True
    show YBook at TopRight_RightScreen behind Mikuru with dissolve
    $ _window = False
    "Yuki blinked and raised her eyes from her book, though her expression remained unchanged."
    show Haruhi Neutral1 at left_RightScreen
    "\"Not you, Yuki-chan,\" she added, glancing at the shorter girl."
    "Nodding very slightly, Yuki turned her attention back to the pages before her. Haruhi glanced at the title, 'The Mirror of Her Dreams'."
    $ _window = True
    hide YBook with dissolve
    $ _window = False
    nvl clear
    show Tsuruya Worry1 at center_RightScreen
    "Tsuruya's usual smiling expression had faded to a look of worry. \"Um, please, Haru-nyan, it's very importants, you know.... I made Kyon-kun promise that no matter what, he wouldn't reveal what he knew to anyones — even you — until the investigations was complete!" 
    show Tsuruya Sigh1 at center_RightScreen
    "But don't blame him; I made him promise! I...if you insists that he can't help me anymore, then ... I guess that's SOS Brigade rules, so I can't do much about it.\""
    nvl clear
    show Haruhi Pout1 at left_RightScreen
    "Haruhi grimaced, realizing that very likely, with time travel involved, Kyon made the promise because he had traveled back from some time after Haruhi already {i}knew{/i} what the investigation results were. {nw}"
    show Haruhi Neutral2 at left_RightScreen
    extend "\"Alright,\" she agreed decisively. \"Next time I'd prefer you were more straightforward and brought requests like this to me directly! So I'll allow it this time, but I will need accurately recorded receipts accounting for all times and locations that you're utilizing Kyon in.\""
    nvl clear
    show Tsuruya Laugh1 at center_RightScreen
    "\"Ah, that's no problem,\" Tsuruya said brightly. \"I can even tells you where we were yesterday! I just ... can't says why yet.\""
    show Haruhi Hap1 at left_RightScreen
    "\"So, where, then?\" Haruhi pressed."
    show Tsuruya Hap1 at center_RightScreen
    "\"Yesterday, I met Kyon-kun on the way to your club,\" Tsuruya explained, her smile returning full force. \"I guess he was just leaving; he said he was dismissed for the day and could help me out! Hmm, he didn't mention anything ... is there a rental fee or a deposit for Kyon-kun's help?\""
    nvl clear
    show Haruhi Sigh1 at left_RightScreen
    "Haruhi blinked, then considered. She had suggested renting Yuki to the Computer Research Society once ... Kyon had adamantly vetoed that, but he wasn't here to veto this, and he'd somehow gotten roped into helping Tsuruya out anyway. But, then again...." 
    show Haruhi Smile2 at left_RightScreen
    "\"Well, you're a good friend, so you can skip the deposit,\" she decided. \"I guess it wouldn't be fair to charge you after you shared your winter home with us, and invited us to the flower viewing. Just realize you're getting a great deal!\""
    show Tsuruya Hap3 at center_RightScreen
    "\"For sure, Haru-nyan! Kyon-kun's super handy!\""
    nvl clear                                                                            
    stop music fadeout 1
    queue music "Music/Unzari da.mp3"
    show Koizumi Think Ser4 at left
    $ renpy.layer_at_list([PanScene_RightToLeft])
    with None
    play sound "SE/doorknock.mp3"
    $ _window = True
    pause 1
    play sound "SE/dooropenfast.wav"
    show Kyon Worry1 at right
    show Kanae Worry2 at center
    with dissolve
    $ _window = False
    "After knocking, Kyon opened the door, his expression more sour than usual. A faint line of blood trickled down one cheek, and Kanae stood at his side, holding his free hand and looking downcast." 
    $ _window = True
    show Haruhi Sup3:
        linear 0.3 TenthRight # left_RightScreen
    show Kyon Worry1:
        linear 0.2 pass
        linear 0.2 center_RightScreen
    # with dissolve
    $ _window = False
    $ renpy.layer_at_list([PanScene_LeftToCenter])
    "\"Kyon!\" Haruhi yelped, rushing to his side and peering at the cut — more of a deep scratch, really. Even so, she dragged him to the nearest chair and sat him down. \"What happened?\""
    nvl clear
    $ renpy.layer_at_list([PanScene_CenterToRight])
    show Tsuruya Sup1 at center_RightScreen
    "\"You're still bleeding?\" Tsuruya asked, blinking in surprise. \"But I put a bandage on that for you yesterday!\""
    show Kyon Sigh1 at center_RightScreen
    "\"Long story,\" Kyon said, shaking his head and grimacing."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kanae Worry3 at center
    "\"I'm sorry, Sempai,\" Kanae managed timidly, releasing his hand and taking a seat by Koizumi."
    $ renpy.layer_at_list([PanScene_LeftToRight])    
    show Kyon Neutral2 at center_RightScreen
    "\"Don't worry about it— Haruhi, Asahina-san and I need to take care of something relatively quickly.\""
    nvl clear
    show Mikuru Sad2 at right_RightScreen
    "Mikuru stared, snapped out of her faint only to see the scratch, blood dribbling down Kyon's cheek to run along his chin."
    $ renpy.layer_at_list([PanScene_RightToCenter])
    # with None
    show Mikuru Cower Nervous3:
        linear 0.3 xpos 1.2
    show Kyon Neutral2:
        linear 0.2 pass
        linear 0.1 xpos 1.3
    show Tsuruya Sup1:
        linear 0.3 right_RightScreen
    "\"Wah! Kyon-kun!\" she wailed, dashing to his side and dabbing at the injury with a handkerchief. \"I'll take you to the nurse's office, right away! Please don't die!\""
    nvl clear
    show Haruhi Neutral1 at TenthRight
    "Haruhi nodded, unhappy with how things were playing out, but understanding at least what went on. Time travel really explained quite a bit. \"Mikuru-chan,\" she said, waggling a finger, \"it's just a scratch. Kyon is made of tougher stuff! Now, remember yesterday, while we were in the club meeting. We were all in by ten minutes after class got out, right? Make sure he gets there alright.\""
    show Mikuru Cower Sup1
    "\"W...what?\""
    show Kyon Neutral4
    "\"Ah, got it,\" Kyon said, nodding sagely. \"Anything else?\""
    nvl clear
    show Haruhi Smile1 at TenthRight
    "\"I've agreed to let you help Tsuruya-san out when she asks,\" Haruhi added, drumming her fingertips on the tabletop. \"But I expect a full report from both of you when the 'investigation' is complete!\""
    # $ renpy.layer_at_list([PanScene_RightToLeft])    
    "Kyon nodded again, not reacting much except to look more thoughtful. Well, Haruhi admitted to herself, he really {i}was{/i} good at this time travel stuff.... Sadly, he was probably just the role-model Mikuru needed."
    nvl clear
    show Kyon Neutral2
    "\"Right, I'll see you in class,\" Kyon decided, checking the clock on the wall and climbing back to his feet."
    show Mikuru Ser2
    $ _window = True
    "\"The nurse's office, Kyon-kun,\" Mikuru insisted, taking Kyon's hand and leading him into the corridor, {nw}"
    # $ _window = True
    hide Mikuru 
    hide Kyon
    with dissolve
    $ _window = False
    extend "the boy reaching back to push the door shut behind them."
    $ _window = False
    nvl clear
    show Haruhi Worry1 at TenthRight
    # $ renpy.layer_at_list([PanScene_RightToLeft])      
    "\"Okay!\" Haruhi declared, turning to the downcast Kanae. \"What happened with Kyon? Why did he get cut getting you for lunch?\" And speaking of lunch ... she hadn't even managed to give Kyon the bento she had made! She didn't know who Tsuruya was investigating, but she was certain she'd make them pay!"
    show Kanae Sad3 at center
    show Tsuruya Sup1 at center_RightScreen
    $ renpy.layer_at_list([PanScene_CenterToLeft])      
    "\"I...it's my fault,\" Kanae said meekly, hunching in on herself."
    $ renpy.layer_at_list([PanScene_LeftToRight])
    nvl clear
    "In the corridor, Mikuru yelped something indistinct, moments before there was a strange {nw}"
    play sound "SE/impact.mp3"
    show Tsuruya Smile3 at center_RightScreen
    extend "thudding noise and an eerie silence. \"Lunch with the brigade is exciting,\" Tsuruya decided, while Kanae sniffled meekly and blew her nose on her handkerchief."
    nvl clear
    stop music fadeout 2
    return
