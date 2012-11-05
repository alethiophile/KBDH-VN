#Sprites needed: Okabe, Yanagimoto, better Yamane sprites, Tanaka, and Hoshino.


label HAB4:
    scene bg ClubHallLeft with fade
    stop music fadeout 1
    queue music "Music/suspicion.ogg"
    show Yuki Right Neutral1 at right
    show Kyon Unhap4:
        xalign 0.85 yalign 1.0
    show Tsuruya Ang1 at center
    #show Yanagimoto at HalfLeft
    "Yanagimoto led the way to the far end of the old clubhouse, and the idol research clubroom. Tsuruya stood just behind her, Kyon and Yuki side-by-side behind her. She wasn't sure how she should feel about leading members of Haruhi's club against someone who was an ally only an hour ago ... but her misgivings vanished when she considered the pictures that Haruhi had shown her."
    nvl clear
    "Haruhi might have been many things — a depraved pervert among them — but she wasn't the type to use subterfuge. Subtlety was a force she didn't understand very well. Which suited Yanagimoto just fine at the moment; if Kyon was half the delinquent she had been claiming, Yamane would get some well-deserved facial reconstruction."
    nvl clear
    #show Yanagimoto Hap1
    "She took a quick breath to steel herself, then put on her most cheerful syrupy-sweet voice. The one she had previously only used on Taniguchi to try and turn him against Haruhi. \"Yamane-kun,\" she called, rapping on the door. \"It's Yanagimoto~! Do you have a free minute?\""
    nvl clear
    play sound "SE/Creak1.wav"
    "The quartet listened to the creak of his chair as he rose, {nw}"
    play sound "SE/Step1.wav"
    extend "then the tap of his footsteps across the room before the door unlocked and opened. {nw}"
    show Yamane Grin2 at left with dissolve
    play sound "SE/dooropenfast.wav"
    extend "Yamane's expression shifted from something quite near a leer to {nw}"
    show Yamane Terror1
    extend "raw alarm when he saw Kyon. Before he could slam the door shut, {nw}"
    play sound "SE/impact.mp3"
    hide Yamane with dissolve
    extend "Kyon gave it a hard kick, sending the edge of the door flying into the boy's face, knocking his glasses off and sending him stumbling back."
    nvl clear
    scene bg IdolClubDark with fade:
       size (800,600)    
    #stop music fadeout 1
    #queue music "Music/FootstepsOfDestruction.mp3"
    #show Yanagimoto at center
    show Yuki Right Neutral1 at right
    with dissolve
    "Yanagimoto was a tiny bit unnerved by the way that Tsuruya strode past her and into the room, standing over Yamane's form with arms crossed over her chest, and both Yuki and Kyon seemed to just flow around her. The supposed delinquent gestured her in, and she hesitantly joined the group, {nw}"
    play sound "SE/doorclose.mp3"
    extend "before Yuki shut the door behind them, locking it once more."
    nvl clear
    show Yamane Lost Cool1 at left with dissolve
    "\"Ow!\" Yamane protested, rubbing his nose, his eyes tearing as he fumbled for his glasses. \"What the hell!? Yanagimoto-san — I thought we were friends!\""
    #show Yanagimoto Ang4/Livid1
    "\"So did I,\" she spat, glaring as he put his spectacles back in place and gave her a sad gaze. \"Haruhi showed me the pictures you took!\""
    nvl clear
    hide Yuki
    #hide Yanagimoto
    show Kyon Ang1 at center
    show Tsuruya Grin6 at right
    with dissolve
    "\"Things are about to become very, very uncomfortable for you,\" Kyon said, using the informal form of the word. He crouched near the boy and stared at him dully. Tsuruya chuckled, her grin ominous."
    nvl clear
    "Yuki slowly turned around and studied the room. It was dark at the moment, only the red lighting of a film- development closet active at the moment. The short girl walked to the window and pulled the curtain open, {nw}"
    play sound "SE/Curtain.wav"
    extend "flooding the room with brighter light."
    nvl clear
    scene bg IdolClubLight with fade:
       size (800,600)
    hide Kyon
    hide Tsuruya
    #show Yanagimoto at center
    show Yuki Right Neutral2 at right
    show Yamane Lost Cool1 at left
    "\"Hey!\" Yamane protested again."
    "Yanagimoto realized that every surface of the room was plastered in pictures cut out of idol magazines, or full-page prints downloaded from the internet. She couldn't recognize a fraction of them. Near the far end, just before the window, was a desk with a computer on it, very similar to the setup in Haruhi's club room, only without the long table in the center."
    nvl clear
    #show Yamane
    "\"What the hell is going on here?\" Yamane whined."
    hide Yuki
    #hide Yanagimoto
    show Tsuruya Ang4 at right
    show Kyon Unhap5 at center
    with dissolve
    "Tsuruya gave him a cool look. \"Do you knows who I am?\" she asked, quirking an eyebrow higher."
    show Yamane Lost Cool2
    "\"Tsuruya Haruka,\" he answered, glaring at her. \"Third year student. What did I ever do to you?\""
    nvl clear
    show Tsuruya Grin6
    "Tsuruya chuckled, showing her teeth to the boy. \"Do you know who my family is?\""
    #show Yamane Yell1
    "\"I don't care!\" Yamane said defiantly. \"Whatever big shot you're related to, nothing gives you the right to break into my clubroom and assault me!\""
    nvl clear
    show Kyon Ang3
    "Kyon cracked his knuckles loudly, then reached down and pulled Yamane to his feet by the collar of his coat. \"I very strongly advise that you start talking,\" he warned. \"Because right now, most of the rumors you've been trying to spread about me are true. And if you don't start talking, well....\""
    nvl clear
    show Yamane Grin1
    "\"Well {i}what{/i}?\" Yamane sneered, unshaken."
    show Tsuruya Hap7
    "\"Then he gives you to me,\" Tsuruya said cheerfully. \"'Cause he's the {i}nice{/i} one!\""
    nvl clear
    show Yamane Terror2 #Yamane plead1
    "Yamane's eyes went wildly between the pair, then turned to Yanagimoto, silently beseeching her for help."
    hide Kyon
    hide Tsuruya
    hide Yamane
    #show Yanagimoto Ang2 at center
    with dissolve
    "\"Come clean, you piece of filth. You think I'm going to help {i}you{/i}?\" she snarled, copying Kyon's derogatory use of the term. \"After what I found out!?\""
    nvl clear
    #hide Yanagimoto
    #show Yamane Plead2 at left
    show Tsuruya Hap7 at right
    show Kyon Unhap5 at center
    with dissolve
    "\"You're being played!\" Yamane tried desperately. \"I was framed! This ... this is all Suzumiya's plan to— {nw}"
    #show Yamane
    play sound "SE/impact.mp3"
    extend "UGH!\" He coughed, short on breath, hunching over the fist that Tsuruya had driven into his stomach."
    show Tsuruya Ang3
    "\"Haru-nyan is a much better planner than that,\" Tsuruya informed him stiffly. \"And she's not the one here.\""
    nvl clear
    #show Yamane
    "He gasped, struggling to breathe, held up only by Kyon's grip on his coat. \"Okay,\" he wheezed. \"Whatever.... Just ... don't hurt me....\""
    show Kyon Ang4
    show Tsuruya Grin1
    "\"Let's start by getting us into that computer,\" Kyon said, releasing the boy's coat and pushing Yamane towards the desk."
    nvl clear
    #show Yamane
    "\"Y...yeah, okay,\" the bespectacled boy said shakily, wobbling towards the seat. Yuki watched him impassively as he paused, leaning on the edge of the desk and panting, then turned her attention away, approaching one of the filing cabinets near the door and opening it."
    nvl clear
    "Yanagimoto wondered what the girl was up to, but couldn't look away from the revenge she had wished on Yamane."
    #show Yamane
    "\"Gonna open a window,\" he said, \"need ... some air.\""
    nvl clear
    show Kyon Unhap5
    show Tsuruya Grin2
    "Kyon grunted wordlessly, glancing at Tsuruya. The eternally-cheerful girl was still smiling, her eyes fixed on Yamane, except to flicker to Kyon every so often for the briefest moments. Was the rumor that Yanagimoto had tried to help spread true? Was there something going on between them? Yamane paused once the window was opened, just standing still and breathing."
    nvl clear
    play sound "SE/WestminsterChimeShort.mp3"
    "The chime sounding the end of lunch rang out, but Yanagimoto decided she'd wait and be late to class. For this...."
    nvl clear
    show Tsuruya Ang2 at center
    show Kyon at right
    with dissolve
    #show Yamane
    "Tsuruya grumbled, marching to Yamane's side and raising a fist in warning. He scurried to the computer, cowed, and frantically began typing. \"I'll log in, and you can see—\" He broke off, and Yanagimoto realized his ploy too late, too shocked to react to what he'd done. When Tsuruya had moved towards him, she stood next to the window."
    nvl clear
    stop music fadeout 0.1
    queue music "Music/FootstepsOfDestruction.mp3"
    play sound "SE/GlassBreak1.mp3"
    show Kyon Sup2
    show Tsuruya Laugh Pain2 Flip
    show Yamane Grin3
    hide Tsuruya with dissolve
    "With a desperate shove, he pushed her to a three-story drop to a concrete walkway. She felt a horrified shriek build in her own throat as Tsuruya's eyes widened, and her hands windmilled frantically, one catching momentarily on the glass edge of the window before it shattered, sending a blossoming aura of glimmering shards exploding outward behind her."
    nvl clear
    hide Kyon with dissolve
    "A bare instant before the girl vanished from sight, Kyon had somehow gotten there, grabbing her other flailing hand and being pulled after her all the way to his shoulder, {nw}" 
    play sound "SE/Hit1.wav"
    extend "his knees slamming to the floor loudly."
    nvl clear
    show Yuki Ang1 Flip at center
    #show Yanagimoto at right
    hide Yamane
    with dissolve
    "Just as quick as Kyon was, somehow Yuki was there, too. Before Yamane could try and shove Kyon as well, the shorter girl seized the back of Yamane's coat and — improbably — plucked him up with one hand, hurling him head-over-heels through the air, sending the boy flying past Yanagimoto faster than she could turn to look."
    nvl clear
    play sound "SE/Hit2.wav"
    "The paneling of the wall crunched from the impact — at least, part of Yanagimoto hoped it was only the paneling. The boy made a retching sound and collapsed face-first on the floor after bouncing off the now-dented wall."
    nvl clear
    hide Yuki
    #hide Yanagimoto
    with dissolve
    "\"I've got you,\" Kyon managed, his voice strained. Yanagimoto scrambled to try and help. All of Tsuruya's weight was dragging down on Kyon's arm, driving the narrow edge of the windowsill up beneath his armpit; she couldn't imagine how painful that must be. Before Yanagimoto even reached his side, Yuki leaned out the window and helped haul Tsuruya back up and into the room."
    nvl clear
    show Tsuruya Laugh Pain1 Flip at left
    show Kyon Worry3:
        xalign 0.55 yalign 1.0
    show Yuki Right Neutral1 at right
    with dissolve
    "The tall green-haired girl was shaking uncontrollably, her eyes streaming tears as she collapsed into Kyon, who himself knelt on the floor. Tsuruya's right hand was slashed and bleeding from the shattered windowpane. Her left shirt sleeve over her wrist, where Kyon had grabbed her, was bloodied with a large and expanding stain. Her arms were limp, her hands shaking worse than she was."
    show Tsuruya Laugh Pain4 Flip
    "\"S...stitches tore open,\" she whimpered. \"H...hurts....\""
    nvl clear
    show Kyon Unhap2
    "Kyon swore something guttural, clutching the girl to his chest. \"Okay,\" he said quickly, snapping his gaze to Yanagimoto. \"One thing at a time. Yanagimoto, make sure Yamane's still down — keep an eye on him.\" She nodded shakily, glad to follow orders and not think about things too heavily."
    nvl clear
    #show Yanagimoto at center
    hide Kyon
    hide Tsuruya
    hide Yuki
    with dissolve
    "Behind her, Kyon continued, \"Tsuruya-kun, it's going to be okay. You trusted me with your secrets, so we're going to trust you with this. Nagato....\" She couldn't hear the rest of his words, but realized that ultimately, she didn't {i}want{/i} to. Whatever world she'd gotten involved in, she was happier being as uninvolved as possible. Revenge on Yamane was one thing, but this.... This...."
    nvl clear
    #show Yanagimoto Ang1
    "How had she judged so badly that the person she despised had garnered such trustworthy allies, while she herself had been deceived by someone as despicable as Yamane!? She was seriously contemplating kicking the boy while he was down to vent her frustration before Kyon was at her side."
    nvl clear
    #hide Yanagimoto
    show Tsuruya Laugh Sad1 Flip at left
    show Yuki Right Neutral1 at center
    with dissolve
    "\"Ah,\" she managed, looking up at him nervously. \"Is Tsuruya-sempai....\" She trailed off and looked over her shoulder. Though she looked very tired, the upperclassman seemed alright, catching her breath in Yamane's chair."
    nvl clear
    hide Tsuruya
    hide Yuki
    show Kyon Unhap3 at center
    #show Yanagimoto at right
    with dissolve
    "Maybe it had been a trick of the light, or Yamane's imagination? There was a smudge of blood on the girl's right hand, but her left shirt sleeve was completely unstained, now. Kyon leaned down and collected the boy's glasses, somehow still in place, only slightly askew. \"Yeah, Nagato took care of her. Hold these for me,\" he said, thrusting them at her as he straightened."
    nvl clear
    "She numbly accepted them."
    show Kyon Unhap2
    "\"Nagato, is Yamane alright?\""
    show Yuki Talk1 at left with dissolve
    "\"Minimal reasonable force was used,\" the girl stated calmly. \"No permanent damage should result.\""
    nvl clear
    show Kyon Smile7
    "He smiled at her. \"Thank you. Now, we don't need any interruptions, could you secure the door?\""
    show Yuki Talk2
    "\"Understood,\" Yuki replied, {nw}"
    hide Yuki with dissolve 
    extend "stepping away from Tsuruya's side to place one hand against the door and stare at it intently."
    nvl clear
    show Yamane Terror1 at left
    show Kyon Unhap4
    "Bending down again, Kyon grabbed Yamane's collar and dragged him to the window, hauling the boy upright before slapping him awake. \"W...wha—\" Yamane sputtered, just before Kyon shoved him out the window."
    nvl clear
    scene bg ClubHallOutside with fade:
       size (800,600)
    "But not to fall, as she'd initially thought. Grabbing first by Yamane's belt, and then lowering him further, so that Yamane was suspended by only one ankle, Kyon let the boy dangle. Yanagimoto was stunned, but no so much she couldn't be impressed by the fact that Kyon was holding the boy with what seemed minimal effort."
    "\"Rise and shine!\" Kyon yelled with fierce cheer, jerking the ankle and shaking the other boy. \"How you doing, Yamane?\""
    nvl clear
    "\"L...let me go!\" Yamane yelped."
    "\"Classic poor choice of words,\" Kyon remarked. \"Do you {i}really{/i} want that?\""
    "Yamane wailed, then screamed, \"Help! Help! Someone — I'm being murdered!\""
    nvl clear
    "\"Nonsense,\" Kyon said, shaking Yamane again. \"I'm trying to save you. But, see, I recently strained this arm ... not sure how much longer I can hold you up!\""
    "\"You're never going to get away with this!\""
    "\"You think? So, maybe I should just drop you, since I'm damned anyway? How does that saying go ... 'if you're going to do the time, may as well do the crime'?\""
    nvl clear
    scene bg IdolClubLight with fade:
       size (800,600)
    #show Yanagimoto at center
    show Kyon Unhap4 at right
    "Yanagimoto stared in morbid fascination. Was Kyon {i}actually{/i} going to drop the boy...?"
    hide Kyon
    #hide Yanagimoto
    show Yuki Side1 at center
    with dissolve
    play sound "SE/impact.mp3"
    "The door to the clubroom shook with a muffled yell and a frantic slam, but didn't budge. Yuki stared at it fixedly, one hand holding it shut. Then again ... she had somehow hurled Yamane the length of the clubroom with one hand."
    nvl clear
    hide Yuki
    show Tsuruya Ang3 Flip at left
    show Kyon Unhap4 at right
    with dissolve
    "Tsuruya gave a small shudder, recovering slightly and rising from the chair. \"Escalation is an ugly game, Yamane,\" she warned. \"And it's not one you're going to win todays. I don't get mad much, but you badmouthed my friend, you tried to murder me, and you shamed almost every girl in this school."
    nvl clear
    show Tsuruya Ang4 Flip
    "Believe me, if Kyon-kun lets you have a three-story french-kiss with the pavements below, that's a mercy compared to the world of hurt I could introduce you to!\""
    "\"Let me go!\" Yamane wept. \"Please!\""
    show Tsuruya Ang3 Flip
    "\"Password for your computers,\" Tsuruya demanded, producing a notepad and paper from one pocket. \"Names of your accomplices — {i}all{/i} of them.\""
    nvl clear
    show Kyon Ang3
    "\"And make it quick,\" Kyon added, shaking the boy, his arms trembling. \"You've got some people watching you down there.\""
    "\"M...my password is 'Tenshi',\" Yamane cried. He then wept a litany of names, which she also studiously wrote."
    nvl clear
    show Tsuruya Grin5 at right
    show Kyon Unhap4 at center
    with dissolve
    "\"Good,\" Tsuruya murmured, once the names were all recorded. She then turned to the computer, tapping a few keys. \"Okies, password checks out.\""
    nvl clear
    scene bg ClubHallOutside with fade:
       size (800,600)
    "\"You've got quite an audience, now,\" Kyon grunted, exertion reaching his voice. \"Tell you what, Yamane, since you've been a sport about this so far.... Say hello and wave to the nice people!\""
    "\"Hello!\" Yamane wailed."
    "Yanagimoto anxiously crept to the side of the window furthest from the scene, eyes widening as she realized fully half of the students in the school had flooded the courtyard to stare at the spectacle. The classrooms opposite the club room were full of onlookers, and quite a few were taking pictures with cell phones or cameras."
    nvl clear
    "\"Louder,\" Kyon rasped. \"My arms are getting tired. Since you've got their attention, introduce yourself ... and tell everyone what you were doing in this room!\""
    "\"M...my name is Yamane Jun!\" the terrified boy screamed. \"F...for the last few weeks I've run an illicit photography ring! I've been collecting pictures of all the girls in the school as they changed uniforms! I've been s...selling them to yakuza, or anyone else who will pay me!\" He blubbered wordlessly for a moment, then keened, \"I don't want to die!\""
    nvl clear
    scene bg IdolClubLight with fade:
       size (800,600)
    stop music fadeout 1
    #queue music "Music/"
        #not sure what to play here.
    show Kyon Neutral1 Flip at center
    show Tsuruya Grin1 at right
    with dissolve
    "\"Um, hey, Tsuruya-kun,\" Kyon said, his voice suddenly level. \"Is it me, or did Yamane here just wet himself?\""
    nvl clear
    show Tsuruya Laugh2
    "\"Huh?\" The upperclassman cautiously approached to peer out the window, then exploded into gales of laughter. \"Bwahahaha! Oh, Yamane-chan, that's {i}precious{/i}! I'll make sure one of those pictures of you that's being taken down there now is {i}right{/i} next to the article about this that'll be in the paper!\""
    nvl clear
    show Kyon Unhap4 Flip
    play sound "SE/Hit3.wav"
    "Kyon snorted, hauling the boy into the room and laying him out with a straight punch to the face, stepping away from the widening puddle forming around Yamane."
    nvl clear
    #stop music fadeout 3
    show Kyon Sigh6 Flip
    "The delinquent moved away from the window and stood still for a long minute, just closing his eyes and breathing very deeply."
    show Kyon Puzzle1 Flip
    "When his eyes opened, he raised his hands before him, frowning at their shaking. \"I don't like being angry,\" he muttered."
    nvl clear
    #queue music
    show Tsuruya Sigh4
    show Kyon Worry1 Flip
    "Tsuruya shut the computer down, then walked to his side, pulling his face towards hers, so their foreheads touched, her eyes closed. \"It's okay,\" she soothed quietly. \"You get angry for good reasons. I'm sorry, Kyon-kun.\""
    nvl clear
    show Kyon Puzzle1 Flip
    "\"I'm not,\" he replied, his arms wrapping around Tsuruya. \"You're okay, and we're done with this, right?\""
    show Tsuruya Sigh3
    "\"...almost,\" Tsuruya meekly said, tentatively hugging him back. \"I'm sorry ... he kept records on his system ... he made a sale last nights. If we can get those pictures back before they go onto the internet....\""
    nvl clear
    show Kyon Sigh2 Flip
    "\"Okay,\" he mumbled, shifting his face to one side and burying it in her shoulder. \"When this is over, I need a damn vacation.\""
    show Tsuruya Hap1
    "\"Anything I can do for you,\" she promised him, breaking the embrace to stare into his eyes and nod emphatically."
    nvl clear
    show Kyon Smile6 Flip
    "He gave a shaky grin and rolled his neck, cracking it in several places. \"Hopefully we can get out of this without going to jail, huh?\""
    nvl clear
    hide Kyon
    hide Tsuruya
    #show Yanagimoto at center
    "Yanagimoto swallowed. Whatever was going on between Tsuruya and Kyon ... it was none of her business. But if that scene was anything to go by, the pair needed one-another. And much to her surprise, Yanagimoto realized that if it kept things like Yamane's plot out of her school, she was all for it."
    nvl clear
    "They were involved in life-or-death struggles ... judging by their relatively unshaken demeanors, and how unreasonably fast Tsuruya had recovered from her ordeal, this wasn't {i}that{/i} unusual for them. And here, she had spun pointless drama to make their lives harder?"
    nvl clear
    #hide Yanagimoto
    show Kyon Sup2 at right
    with dissolve
    "\"Nagato,\" Kyon began, turning around to look at Yuki, then cutting off with a choked gasp."
    nvl clear
    #scene
    show Kyon Worry2 at right
    "Following his gaze, Yanagimoto saw a floor-length picture on the back of the door. A familiar girl that she remembered seeing a long time ago.... She was looking over her shoulder, laughing about something as she undid the zipper on the side of her skirt, her long blue hair fanned out behind her. \"I...is that,\" he stuttered, eyes widening in what Yanagimoto thought was horror."
    nvl clear
    show Yuki Talk1 at left with dissolve
    "\"Yes,\" Yuki answered."
    show Kyon Sup1
    "\"S...so this whole thing....\""
    nvl clear
    show Yuki SadTalk2
    "\"A ... long-term plan,\" Yuki said quietly. \"Until seeing the data acquired from Yamane Jun's operation, the mechanisms of this were invisible to me. However, the execution appears to have become ... corrupted.\""
    show Kyon Sup2
    "Swallowing, Kyon gave an uncomfortable nod, muttering the name of the girl in the picture, \"Asakura Ryouko....\""
    nvl clear
    
    scene bg ClubroomCenterDay with fade
    stop music fadeout 1
    #queue music 
    show Koizumi Crossed Smile1 at left
    show Haruhi Crossed Smile1 at right
    with dissolve
    play sound "SE/WestminsterChimeShort.mp3"
    "Haruhi had elected to ignore the chime warning students to return to their classrooms, and Koizumi stayed with her. Mikuru and Kanae, being largely uninvolved, returned before they were late, while Haruhi quickly wrote out a list of notes and considerations for the explanation to the student council."
    nvl clear
    "Packing away the lunch box he had brought to the clubroom, Koizumi glanced out the window, just catching a growing crowd of students looking towards the opposite end of the club building. Haruhi caught it too, glancing over her shoulder before gathering up her papers and narrowing her eyes. \"We'd better check this out,\" she declared, swiftly jogging out of the room."
    nvl clear
    scene bg SchoolTreeRight with fade:
       size (800,600)
    show Haruhi Neutral1 Flip at center
    show Koizumi Crossed Ser1 Flip at right
    with dissolve
    "Shrugging, Koizumi followed, not expecting much of anything spectacular until they reached the courtyard and caught the nearby murmuring students. At a glance, the clubroom furthest from the brigade room, but on the same floor, was the focus of attention. One of the windows had been half-shattered, and a very familiar student was dangling Yamane Jun out the window by his ankles."
    nvl clear
    show Haruhi Sigh2
    "Haruhi's eyes widened, before she smacked her forehead with the heel of one palm. \"Kyon is such an idiot,\" she groaned. \"Koizumi, you work damage control on this end, we'll meet up when we face off against the student council president!\""
    nvl clear
    hide Haruhi with dissolve
    "Koizumi only had time to nod before she dashed off, and he found himself hindered by the thickening crowd. It would take a miracle, or maybe Emiri's tampering to get something of this magnitude passed down to the student council.... It would probably take some doing just to keep Kyon from being expelled. Fights and intimidation were one thing, but such a display in broad daylight...."
    nvl clear
    scene bg ClubHallLeft with fade
    #show Okabe at left
    #show Tanaka at center
    #show Hoshino at right
    #with dissolve
    "Breaking into a jog of his own, Koizumi quickly trotted to the hall outside of the room in question. Okabe and a pair of other teachers were already there, Okabe anxiously slamming one shoulder into the door repeatedly, the other two watching him while trying to call through the door and demand it be opened."
    nvl clear
    "If Yuki were in that room, no teacher would be given access.... Okabe was Kyon and Haruhi's homeroom teacher, and just a normal person, as far as Koizumi knew. The other two were Organization members; Tanaka and Hoshino. Tanaka was a shortish male with plain features in his thirties, and Hoshino was a tallish woman with sharp features in her forties."
    nvl clear
    #show Tanaka
    #show Hoshino
    "Okabe ignored Koizumi's approach, and the other handful of students who had gathered around in the hallway to stare in amazement. The other two caught his eyes and shook their heads slightly. He understood their meaning clearly enough; they didn't have a way to make Okabe look the other way at the moment, which would make smoothing things over more difficult."
    nvl clear
    scene  bg ClubHallLeft with fade
    "Retreating down the hall out of earshot of the crowd, he stopped before the computer clubroom. Their door was open, and the president was leaning out the open window to see what the commotion was. Keeping an eye on the man, Koizumi pulled his phone from his pocket and speed-dialed Mori."
    nvl clear
    "He gave her a terse explanation for the day's activities — not enough time to try and explain the scandals, just the trouble that they would need to get Kyon out of. Once he was done, he caught his breath; Okabe had stopped trying to break down the door for the moment."
    nvl clear
    "Mori finally said, \"Understood. I will get in touch with other school operatives. In the meantime, Kyon is mostly able to look after himself now, I think. So make sure that Suzumiya-san is being covered.\""
    nvl clear
    "She hung up without waiting for him to confirm. He debated internally for a moment, but doubted that he would actually even find Haruhi if he were to search for her. That thought in mind, he strode back towards the teachers, drawing in hearing range just as the door opened, swinging inward easily."
    nvl clear
    scene bg ClubHallFull with fade:
            xpos 0 ypos 0
    $ renpy.layer_at_list([PanScene_SetToLeft])
    #show Yanagimoto at left
    show Yuki Side2 at center
    #show Okabe at right
    #show Tanaka at center_RightScreen
    #show Hoshino at left_LeftScreen
    show Koizumi Crossed Ser1 Flip at right_RightScreen
    with dissolve
    "Yuki was the first student behind the door, stepping back as though she had just unlocked it. Directly behind her was Yanagimoto, and Tsuruya and Kyon were side-by-side behind her. Okabe yelled and made to seize Kyon's shoulder; the physical education teacher was no match for Yuki."
    nvl clear
    #show Okabe
    "The slight girl grabbed Okabe's wrist with just the fingertips of her left hand, quickly spinning the man about and pinning him against the wall in a joint-lock by his own elbow. \"W...what is the meaning of this?\" he protested."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    "Tanaka and Hoshino winced. Once again, the message was clear enough to Koizumi."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Yuki Talk2
    "\"You will not touch him,\" Yuki answered."
    #hide Yanagimoto
    show Kyon Neutral2 Flip at left
    #with dissolve
    show Yuki Side2
    "\"That's enough, Nagato,\" Kyon said, shaking his head. \"Okabe-sensei, we'll go with you. There's no need for force.\""
    nvl clear
    #show Okabe
    "Yuki blinked, then released the teacher, who straightened his arm out and glowered. \"Don't think you're getting off easily!\" he warned, shooting a look that was both amazed and confused at Yuki."
    show Kyon Sigh2 Flip
    "\"No good deed goes unpunished,\" Kyon remarked, shrugging."
    nvl clear
    hide Yuki
    show Tsuruya Ang3 Flip at center
    with dissolve
    "Tsuruya fished in her pocket for a moment, then produced a card. \"This numbers is one of my father's men,\" she said, waving it back and forth. \"He represents my family legally. Further inquiries will need to go through him for myself, Kyon-kun, and Nagato-chi. Any statement taken without our lawyer present is inadmissible! Yanagimoto's just a bystander, though, so she shouldn't be in trouble.\""
    nvl clear
    show Kyon Smile4 Flip
    show Tsuruya Grin2 Flip
    #show Okabe
    show Koizumi Crossed Uneasy2 Flip
    "Okabe growled. Koizumi felt his smile slipping. This was serious! Tsuruya invoking legal protection and treating the entire thing as a crime drama.... This wasn't helping, and neither was Kyon's amused almost-smirk. Especially added to Tsuruya's triumphant grin, and Nagato's utter indifference after a girl one third or less the teacher's mass had easily manhandled him."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    #show Tanaka at center
    "\"Okabe,\" Tanaka said suddenly, when the teacher seemed about to reply. \"Why don't you take care of Yanagimoto and return her to her homeroom? Hoshino and I will bring the others to the principal's office; you can also have the nurse come to take a look at Yamane while we wait for the ambulance.\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    hide Kyon
    #show Yanagimoto at left
    with dissolve
    #show Okabe
    "\"Yes, good,\" Okabe decided, still frowning. \"Yanagimoto, if you're uninvolved, please come with me. We'll stop by the office briefly so you can give a statement, and then return you to class.\""
    #hide Yanagimoto
    #hide Okabe
    show Kyon Smile4 Flip at left
    show Tsuruya Grin2 Flip at right
    with dissolve
    "The girl looked hesitant for the merest moment before she shook her head and slipped past Yuki to follow Okabe without a word."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    #show Tanaka
    "\"You trouble-makers,\" Tanaka said, glancing at the students in the hall, staring at the scene. \"Get out of here and back to class! Oh, except for you, Koizumi-kun. Don't think I'll let one of my own homeroom students gawk like this without reprimand!\""
    nvl clear
    show Koizumi Shrug Sigh1 Flip:
        xalign 7.2 yalign 1.0
    "\"Caught,\" Koizumi chuckled, giving a sad smile and shrugging to the other students in the corridor as they obediently ran away."
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Tsuruya Ang2 Flip
    show Kyon Neutral3 Flip
    "Once they were out of earshot, Tsuruya crossed her arms over her chest and eyed the two Organization teachers suspiciously. Kyon seemed almost as indifferent to them as Yuki."
    nvl clear
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Koizumi Crossed Neutral2 Flip at right_RightScreen
    "\"Tanaka, Hoshino,\" Koizumi began apologetically, \"at this time, Kyon-kun is entirely aware of your role at the school.\""
    #show Tanaka
    #show Hoshino
    "\"He is?\" Tanaka asked, taken aback, eyes widening when they turned to Kyon. Hoshino seemed just as surprised."
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kyon Neutral2 Flip
    show Tsuruya Quest2 Flip
    "\"Organization, right?\" Kyon asked. Tsuruya's stance loosened as she looked at Kyon in confusion."
    $ renpy.layer_at_list([PanScene_LeftToRight])
    #show Hoshino
    "The two teachers nodded hesitantly. \"Still,\" Hoshino said, frowning, \"we're going to completely break with appearances if we don't take you to the faculty offices, and this is quite an event to smooth over....\""
    nvl clear
    $ renpy.layer_at_list([PanScene_RightToLeft])
    show Kyon Sigh2
    "\"And Tsuruya-kun is involved, which makes it awkward for you, right?\" Kyon asked, shaking his head. \"Well, in any case, Koizumi, what do you think we should do?\""
    $ renpy.layer_at_list([PanScene_LeftToRight])
    show Koizumi Crossed Smile3 Flip
    "\"Ah, well ... Hoshino-san should be able to escort you to the office,\" Koizumi suggested. \"Tanaka can watch the club room and keep an eye on Yamane Jun. I'll go with you for the moment, but....\""
    nvl clear
    scene bg ClubHallLeft with fade
    show Kyon Neutral2 Flip at right
    show Koizumi Crossed Neutral1 at center
    show Tsuruya Smile1 Flip at left
    with dissolve
    "\"We can talk on the way,\" Kyon commented, falling into step behind Hoshino, Yuki and Tsuruya following just behind him and to either side. Koizumi hurried ahead, having to walk a bit ahead to keep out of Tsuruya's way."
    nvl clear
    show Koizumi Crossed Sigh1
    "\"Well, this is going to escalate to police involvement, I suspect,\" Koizumi said, grimacing. \"I have a hard time imagining them not being called in.\""
    show Kyon Smile7 Flip
    "\"Between that computer, which we have the password for, and the other evidence that Haruhi's hanging on to, we should be able to prove what they were up to without any trouble,\" Kyon said confidently."
    nvl clear
    show Koizumi Crossed Ser2
    "\"While I believe with all confidence that good will prevail, the bigger issue at the moment is making sure that your own life isn't too badly disrupted,\" Koizumi warned, frowning. \"In other words, you underestimate your importance to Suzumiya-san by allowing yourself to be in a situation like this. Things will become difficult for all of us, I think, if you are suspended.\""
    nvl clear
    show Kyon Unhap6 Flip
    "Kyon winced, shifting his shoulders. \"Crap,\" he muttered. \"And my mom's going to freak out about me 'destroying my future' to become a delinquent again.\""
    show Tsuruya Sup1 Flip
    "\"I'm ... not sure what's going on here,\" Tsuruya noted, glancing between Koizumi and the silent Hoshino. \"But, Kyon-kun, I might be able to help, if you let me know the details?\""
    nvl clear
    show Kyon Puzzle1 Flip
    "\"Yeah ... I guess I owe you an explanation on that one later, Tsuruya-kun,\" Kyon admitted, grimacing. \"Once we've got some relative privacy.\""
    nvl clear
    
    
    #Easy-bit
    
    "After collecting all of the paperwork and contacts that Haruhi thought she would need, she felt a nagging suspicion that she had forgotten something. Dashing all the way back to her clubroom, she was surprised to see the computer research society president standing in the hall, looking back towards the idol research clubroom door."
    nvl clear
    "\"Shouldn't you be in class?\" she reminded him."
    nvl clear
    "He raised an eyebrow as he turned to look at her, before shaking his head. \"You really think that little of me?\" he asked. \"I graduated last year, you know. But the club asked me to stay on as president through this term; I have special permission from the school to be here for that.\" He shook his head. \"I guess you don't talk to your friend Kyon ... he already knows that. Nevermind that, though. Kyon seemed a good sort, and Nagato Yuki absolutely didn't seem like the kind to get herself in trouble. So ... what happened?\""
    nvl clear
    "\"Did you hear Yamane's confession?\" she pressed, frowning. That much had gotten around school, surely the president couldn't have missed it?"
    "\"I heard it,\" he agreed. \"But a confession like that.... I suppose if it's true, even the incredible Nagato-san could be upset enough to be involved. Even so, not much stock will be put into a confession that was extorted.\""
    nvl clear
    "Haruhi grimaced. Kyon, being a hero and leaving her to deal with the logistics and fallout. \"Well, whatever. At a school, I think that most people would be swayed by the confession anyway. The biggest thing to worry about is Kyon's record, and this getting back to his mother!\""
    nvl clear
    "The boy in front of her frowned and crossed his arms over his chest. \"I really don't know anything about that,\" he said, shaking his head. \"Just that your priorities seem strange to me.\""
    nvl clear
    "\"So?\" she challenged him. \"That means nothing! When your club was defeated, you swore allegiance to the SOS Brigade should we need reinforcement against the student council! That time is now, and I expect you to be good for something! I don't know if you have unresolved business with your ex- girlfriend, but that doesn't matter to me. What matters is your support in this issue!\""
    nvl clear
    "\"Alright,\" he agreed after a long moment, frowning. \"Those were your terms. Now, what can I actually do for you? I suppose I at least shouldn't be afraid of being suspended or expelled — I'm a graduate. But I'd like to leave my club members out of it, if possible.\""
    nvl clear
    "Haruhi chewed her lip for a minute. \"You know how to make a good computer presentation? Something I can show on a laptop?\""
    "The man nodded slowly. \"Sure,\" he said, uncrossing his arms to shrug. \"I think I've got a copy of some presentation software lying around. Let's start putting it together, huh?\""
    nvl clear
    "She grinned at him. \"Good,\" she declared. \"Let's get to work!\""
    "He fell into step behind her as she marched back into her own clubroom, before asking, \"What ex-girlfriend, though?\""
    nvl clear
    
    #end of easy bit
    
    
    "Before reaching the principal's office, the delinquent trio, escorted by an Organization teacher, found themselves confronted by a pair of police officers in standard dress. Koizumi gave a small sigh of relief at seeing the pair. If the Tamaru brothers were nearby, that probably meant Mori was already working on things to the best of her ability."
    nvl clear
    "\"Hello,\" Keiichi said, nodding at the group. Behind him, Yutaka checked his wristwatch and glanced around; the hallway was empty for the moment. The older of the pair produced a notepad from one pocket and made as if he were scribbling, but Koizumi knew it for an act. \"We don't have a whole lot of time. Koizumi-kun, what's the situation?\""
    nvl clear
    "Tsuruya made a surprised noise, leaning close to Kyon and staring between the uniformed men and Kyon. Yuki's gaze had drifted to Keiichi's notepad and stuck there. Kyon watched everything with a distant, thoughtful expression."
    nvl clear
    "\"Kyon-kun has uncovered a sinister plot. Evil actions were brought to light, and the school was saved. From a practical standpoint, however, Kyon-kun did hold a fellow student upside down out the window of a three story building and threaten to drop him until he confessed,\" Koizumi said quickly. \"For Suzumiya- san's stability, we need this resolved as quickly as possible, and ideally, without word of it getting back to Kyon-kun's mother.\""
    nvl clear
    "\"Alright,\" Keiichi said, frowning. \"We're just plainclothes officers, not detectives. Is there any evidence on this other student?\""
    "\"Yamane Jun,\" Kyon supplied, nodding. \"Haruhi has some of the evidence, the rest is on the computer in Yamane's club room. He got a bit roughed up, but Nagato says there's no permanent damage, so he should be fine.\""
    nvl clear
    "\"Her definition of permanent might vary from ours,\" Koizumi noted, giving Kyon a pointed stare, which the delinquent ignored."
    "\"Okay. We'll take him into custody and have him brought in for questioning,\" Keiichi said, glancing at his partner. The younger officer nodded thoughtfully. \"Then we'll seize his computer for evidence and hand it over to a detective.\""
    nvl clear
    "\"Will that work, Nagato?\" Kyon asked, turning to look at the shorter girl. She slowly turned to face him and raised her gaze to stare into his eyes. Koizumi personally found her stare coldly unnerving; it never ceased to amaze him that Kyon seemed to be unfazed by it. After a moment of thought, she gave a single nod."
    nvl clear
    "\"In the meantime,\" Yutaka said, glancing at his watch again, \"Mori-san should be waiting at the gate. Kyon-kun, we highly suggest that you avoid school for the rest of the day.\""
    "\"You're telling me to cut classes?\" Kyon asked, mildly surprised."
    nvl clear
    "\"The faculty hasn't met your family,\" Keiichi said pointedly. \"Mori-san stood in as your aunt.\""
    "\"I'm not ditching Tsuruya-kun or Nagato,\" he said flatly."
    nvl clear
    "\"Eh ... don't get what's going on here,\" Tsuruya finally chimed in, scratching the back of her head and giving an apologetic smile. \"But, don't look a gift horse in the mouth, right, Kyon-kun? You should go!\""
    nvl clear
    "\"I'm not leaving without you,\" he said stubbornly, looking between Yuki and Tsuruya. \"And anyway, Haruhi's still here—\""
    "\"I will go with you,\" Yuki said suddenly, lowering her gaze to look at nothing in particular."
    "\"Likewise!\" Tsuruya agreed. \"Let's cut class and ... take care of that one last loose thread, right? You can send Haru-nyan a text!\""
    nvl clear
    "\"This would probably be for the best,\" Koizumi agreed, nodding. One of the school's supposed teachers, his friends, and two supposed police officers were all pointing to Kyon that he should run. Was he that devoted to Haruhi? Koizumi mentally smacked himself. Of course he was; that was a stupid question."
    nvl clear
    "\"I'm not sure,\" Kyon said hesitantly."
    nvl clear
    "\"At this point, all you can do by staying here is saying something you shouldn't, or giving the faculty reason to pass judgment on you before Suzumiya-san can finish her defense of you,\" Koizumi said with a shrug. \"You don't have to text her; I can explain everything to her myself. Now, really, you should run while you can. I will take care of loose ends such as your schoolbags.\" He nodded at Yuki and Tsuruya. \"So, good luck, and hopefully we can meet tomorrow to discuss how things went.\""
    nvl clear
    "\"Right,\" Kyon decided, nodding. \"Thanks, Koizumi. Good luck to you, too. And ... tell Haruhi I'm sorry about things working out like this, alright?\""
    "\"I will,\" he agreed."
    nvl clear
    "Taking a breath, Kyon glanced at Tsuruya, and then Yuki. Without a word, the trio broke into a run towards the shoe lockers. Just as they vanished from sight, Okabe rounded a corner, jogging back towards Koizumi and the other Organization plants."
    nvl clear
    "\"Oh!\" the teacher said, surprised at the uniformed men. \"Where did the delinquents go?\""
    "\"In custody,\" Keiichi answered, shaking his head slightly. \"Now, where is Yamane Jun? We're going to need to bring him in, too.\""
    nvl clear
    "\"This way,\" Okabe said, leading the way back towards the clubhouse. \"Oh, I know it's a lot to ask, but I care about my students, so ... is Kyon going to be in trouble for this?\""
    "\"That's somewhat unavoidable,\" Keiichi answered. \"Still, once the detectives chosen for this case finish looking through the evidence, they'll decide the final outcome.\""
    nvl clear
    "\"Hmm,\" Okabe mused. \"Well, thank you, officer. I suppose I should just give Kyon's mother a call to let her know that I think he's a good student at heart.\""
    "Koizumi stifled an internal sigh."
    nvl clear
    
    
    #The rest of this is pretty easy.
    
    "After hurriedly changing shoes, Kyon dashed to the school gate, unsurprised to see Mori standing there in sharp black business attire. Knee-length pleated skirt, formal jacket, and all. She was even holding a pair of dark glasses in one hand. She quirked an eyebrow up as she saw Tsuruya and Yuki following him, but wordlessly gestured them into the car."
    nvl clear
    "Barring a moment of confusion, when Kyon realized that for some reason both girls wanted to sit in the back with him, there was no trouble. He sat in the middle, Tsuruya to his right, and Yuki to his left. Arakawa was driving, as per the evident standard, while Mori sat in the front passenger seat."
    nvl clear
    "\"So,\" Kyon said, once Arakawa started the car, \"you're pretending to be my aunt?\""
    "\"Yes,\" Mori agreed, nodding and looking over her shoulder at him. \"Only a parent or legal guardian could ask for you to be removed from the school, and that seemed the best way to prevent your mother from being notified.\""
    nvl clear
    "\"Yeah, well ... with my luck it's going to get back to her anyway.\" He turned to Tsuruya, then said, \"I'm sorry about this, Tsuruya-kun.\""
    "\"We've got relative privacy,\" she said brightly. \"So, you said you would explain things? I'm especially curious how Kyon-kun has pre-bribed police officers!\""
    nvl clear
    "\"Well ... this is somewhat complicated,\" Kyon began, frowning. \"Actually, Mori-san ... I think you might explain it better?\""
    "\"Are you sure this is wise, Sir?\" Mori asked, looking very uncomfortable."
    nvl clear
    "\"As long as it doesn't get back to Tsuruya-kun's father until her test is over,\" Kyon answered."
    "\"I want to know!\" Tsuruya said, nodding quickly."
    nvl clear
    "\"Very well,\" Mori grudgingly admitted. \"Ah ... Tsuruya-san ... the organization I represent at this moment is in part funded by your father. However, we were of the understanding that your family did not intend to pry into our agendas and intentions, provided they did not interfere with your family's. Therefore, we likewise also try our best to uninvolved with your family's personal business. In fact, until Kyon pointed it out some days ago, we were uncertain that you were ya... that is ... ninkyo dantai.\""
    nvl clear
    "\"If Kyon-kun said you could be trusted with that,\" Tsuruya allowed warily, narrowing her eyes slightly."
    nvl clear
    "Mori looked uncomfortable. \"A...at any rate, Kyon ... convinced ... us to help him assist you when he claimed it would be required. Which is why I am revealing these things to you now. However, there are a few points of concern. Your family may not approve of us tampering with your activities as directly as we are by assisting you here. Assisting Kyon is well within our allowed scope of operations, but this....\""
    nvl clear
    "\"Well, don't worry about it!\" Tsuruya said cheerfully. \"I skipped schools on my own! Kyon-kun got permission and left with his aunt, who happened to give us a rides to my place! Right?\""
    "\"That would be most convenient for us at this juncture,\" Mori agreed, giving a weak smile to Tsuruya."
    nvl clear
    "\"Okay! So ... what's your organizations all about, anyway?\""
    "Mori looked uncomfortable again. \"It ... may be easier ... if you don't know,\" she said cautiously. \"Sorry to be so vague, but your father was content to remain uninformed.\""
    nvl clear
    "Tsuruya looked thoughtful for a moment, then gave Kyon a questioning glance before her smile bloomed again. \"I want to know more,\" she said with a shrug. \"I've been afraid of letting peoples too close to me because of what my family is and does. But Kyon-kun is tangled up in bigger, stranger things ... and he trusts me. I dragged him into my worlds, so ... I will let Kyon-kun decide!\" She nodded to herself, smile widening to a grin. \"So, Kyon-kun, should I know more?\""
    nvl clear
    "He bit his lip for a moment, and began to turn towards Yuki, as though to ask her advice, but caught himself, shaking his head. Taking a deep breath and closing his eyes, he slowly said, \"Tsuruya-kun ... I don't want to make that decision for you. I believe that you can handle the truth, now. But I don't know if you take this step ... if we explain everything to you ... that you'll ever be able to go back to being 'just a side character' again. I know you said you liked being on the sidelines and making other people laugh.\""
    nvl clear
    "His eyes opened, and he gave a small nod. He continued, \"In fact, knowing about your family, and what they do, I understand why you chose to make yourself a bit separate from the rest of Haruhi's friends. I can see why.... Well. I understand and respect your decision at that time. If you want to change things now, then I want to make sure you understand beforehand that it may be a one-way trip.\""
    nvl clear
    "Tsuruya pursed her lips for a moment, staring back at Kyon with her expression sliding from joy to thoughtful neutrality. Just when the silence began to become uncomfortable, she grinned hugely and gave a decisive nod. \"Okay!\" she cheered. \"I give Kyon an 'S' rank scores for that speech! You're right; if I make Kyon-kun decide for me, I'm running from responsibility. My trial is to learn to {i}take{/i} responsibility, not avoid it. So! Tell me everything.\""
    nvl clear
    "\"Very well,\" Mori said anxiously. \"Arakawa, the temple, if you don't mind? That should be private enough.... Now, I'm afraid I cannot enter closed space myself, and anyway, thanks to Kyon's efforts there isn't any active at the moment. So, please believe what I have to say, even though it will sound quite strange and I cannot give immediate proof....\""
    nvl clear
    
    
    "Something was up. Something suspicious. Something worth investigating."
    nvl clear
    "And as soon as Haruhi finished saving Kyon's career and home life, she was going to get to the bottom of it. But after a few innocent questions turned into intense grilling, the president of the computer research society adamantly insisted he not only had never dated Kimidori Emiri, he didn't recognize the name. He admitted, once she found a picture of the girl, that she looked vaguely familiar, and then in a very defeated tone insisted that he'd never had any girlfriend at all."
    nvl clear
    "Haruhi found that strangely easy to believe. As interesting as this new quirk was, she knew it probably had nothing to do with the situation at hand, so she shelved it for later consideration. Kyon might know more, but if she didn't finish rescuing him, she'd have to brave the storm of his mother's crushing gaze to find out. And that was one prospect she did {i}not{/i} enjoy."
    nvl clear
    "\"Anyway,\" she said, tapping the top of the laptop while the president of the computer club looked irritated and quickly punched keys. \"Nevermind that for now. How much longer until you're done?\""
    nvl clear
    "\"It's finished,\" he said, hitting the last few keys, then turning it around. \"You'll have to add the pictures yourself, since you don't want me to see them—\" At her sharp look, he quickly added, \"Not that I should see them, or anything! So, uh, it's all up to you, then.\""
    nvl clear
    "She nodded, paging through the presentation, which the president of the computer club had set up. He had labeled all of the pages she could add images to with instructions for how to replace them, which would simplify the process."
    nvl clear
    "He rose, shrugging. \"At any rate, that's my contribution. I don't know what else I could bring to your arguments. Still, give my regards to Kyon, and Nagato-san.\" He paused, frowning slightly as he looked at the ceiling, then nodded."
    "\"Is that all?\" Haruhi asked, already flipping through the images taken from the SD cards, glancing at him out of the corner of her eyes."
    nvl clear
    "\"Hmm? Well....\" The man seemed torn, then shook his head and gave a sad smile. \"Ah, she's out of my reach. Tell them I wish them both the best, and good luck. I hope things work out for them.\""
    "She looked up from her work long enough to stare at him questioningly, but he seemed stuck with a melancholy expression."
    nvl clear
    "\"I'll be off,\" he said, shaking his head again. \"Take care, Suzumiya-san.\""
    "\"Yeah,\" she managed, frowning as he opened the door and stepped into the hall, just as Koizumi returned, looking a bit more worn than usual, but his eternal smile intact."
    nvl clear
    "\"Hello,\" Koizumi said cheerfully."
    "\"Back already?\" Haruhi asked, surprised. \"What about Kyon? How's the damage control?\""
    nvl clear
    "\"I've done what I could,\" he said, apologetically. \"Kyon, Tsuruya-san, and Nagato have left school for the moment, and aren't likely to return today. Yamane-san is being taken to a hospital, but the police are watching him. It doesn't seem he's suffering internal bleeding or any broken bones, but he's quite badly bruised. He was too disoriented to give any testimony.\""
    nvl clear
    "\"Good,\" she decided, grinning. \"Is the student council in session?\""
    "\"Yes,\" he said, his smile fading. \"But, without Kyon-kun—\""
    nvl clear
    "\"No, that's perfect,\" she insisted. \"Harder for them to pass judgment on him, Yuki-chan, or Tsuruya-san. Let's go get them before they just make up their minds because he's not been represented.\""
    "\"...of course,\" he allowed, nodding."
    nvl clear
    "She finished moving the last few pictures onto the presentation and then saved it and snapped the laptop shut. \"Let's go!\" she declared, leading the march to the student council room. They reached the door shortly, and Haruhi opened it with her usual care, kicking it violently open to slam against the wall."
    nvl clear
    "Within the room were a somewhat confused looking Okabe, a teacher that Haruhi didn't recognize, the student council president, and in one corner, noticed only because Haruhi thought to look specifically for her, Kimidori Emiri. \"Hello,\" Koizumi said uneasily."
    nvl clear
    "The student council president pursed his lips thoughtfully, not adopting his usual scorn-filled sneer, instead turning his gaze to the teachers. \"You, too, huh?\" Okabe said, breaking the silence and giving Haruhi a calculating gaze. \"Shouldn't the pair of you be in class?\""
    nvl clear
    "\"Ah, I asked Koizumi-kun to come here,\" the unfamiliar teacher said, prompting Okabe to look at him in surprise. \"Koizumi-kun, if you don't mind...?\" the teacher prompted somewhat nervously."
    nvl clear
    "\"Right,\" the esper said quickly, when Haruhi turned an inquisitive gaze at him. \"As instructed, I have brought an account which should explain Kyon-kun, Tsuruya-san, and Nagato's involvement in the ... incident at lunch today.\" Haruhi began to scowl, but he quickly bowed and indicated her. \"As his club president, Suzumiya-san will present it.\""
    nvl clear
    "That was more like it, she decided. \"As I'm sure you've all heard by now,\" she said, setting the laptop on the president's desk, as the teachers reluctantly retreated towards the edges of the room to give her space, \"Kyon and the others were investigating a series of criminal actions.\""
    nvl clear
    "\"Yes,\" the president said dryly, adopting his more familiar sour expression. \"Obviously, this should have been handled by your misfit 'club', and not trained professionals.\""
    nvl clear
    "Haruhi ignored the comment, turning the laptop to face him and showing the first screen. \"The issue was first discovered by Tsuruya-san,\" she explained, \"who asked Kyon for help because of the enormity of the situation.\""
    nvl clear
    "\"You have not addressed the point that this is an activity best left for professionals,\" the president remarked. \"Let us set aside your 'ends justify the means' stance for the moment, and examine that issue, first.\""
    nvl clear
    "Haruhi grimaced. She didn't like the idea of saying that the ends always justified the means, but it seemed in her experience it {i}frequently{/i} did ... a certain incident involving tackling Kyon with Mikuru's aid notwithstanding. \"I didn't say that,\" she retorted. \"Be careful what you try and claim I said! If you put words in my mouth, your fingers will be bitten!\""
    nvl clear
    "The president calmly folded his hands together on the desk before him, sitting up the slightest bit straighter. \"The point, Suzumiya-kun,\" he drawled."
    nvl clear
    "\"Eh, well ... Tsuruya-san discovered this issue and brought it to Kyon. Initially, neither of them even wanted me to know what was going on — and why not?\" She tapped a key on the laptop that was facing away from her, changing to the next slide. \"Would {i}you{/i} want to advertise to everyone in the world that pictures like this were going around, taken in your own school!?\""
    nvl clear
    "For all his stoic demeanor, when presented with the image that Haruhi had chosen for the first example, the student council president could not look away. His expression shifted from coldly arrogant to mildly awed, with tiny hints of concealed mirth. Picking up the laptop and swinging the screen around to Emiri, Haruhi added, \"I would have thought you were too old for character- print underwear, Kimidori-chan. You should come to my club, sometime, though, Kanae-chan is a big fan of Trope-tan, too!\""
    nvl clear
    "The student council secretary's face still bore a serene smile, but Haruhi was positive she saw a flicker of something in her eyes. Something vast and irate. \"I ... see,\" Emiri managed."
    nvl clear
    "Haruhi set the laptop back in front of the president and hit a key for the next screen before he started to enjoy it too much. He'd probably never be able to look at Emiri the same way in any case, but that wasn't her problem. \"This is a list of all of the first year students involved in taking these pictures.\""
    nvl clear
    "\"That....\" The president coughed, looking up from the screen and fixing Haruhi with a dour look. \"I understand the vehemence that such a craven act might instill into someone. But if your entire argument is an appeal to surrenduring to emotions, then you fail completely to understand what a system of law is for.\""
    nvl clear
    "\"Okay, fine,\" she retorted, paging to the next slide. \"In that case, let's say that Tsuruya-san brought her complaints to you directly — that someone at the school was somehow taking pictures of her. What would you do?\""
    nvl clear
    "\"That's not entirely a fair question,\" Okabe objected from where he was leaning against a wall. \"Strange as it is that this issue has been handed down to the student council, that sort of action is more than a violation of school policy — it's criminal. If it {i}were{/i} brought to either the student council, or ourselves, then we would defer it to the police! Where it {i}belongs{/i}.\""
    nvl clear
    "\"Is that completely true?\" Koizumi wondered aloud, shooting the teacher a questioning glance."
    nvl clear
    "\"Nope!\" Haruhi said brightly. \"In fact, just a few days ago, a student left this school. Ryuguu ... something-or-another. It didn't make the news, no police were involved, and according to the attendance office when I asked, even though this student assaulted Kyon with a knife, he was given the chance to quietly withdraw. Word among students says he was expelled, but the official record says he withdrew for ... no reason whatsoever!\""
    nvl clear
    "\"That's not true,\" Okabe protested."
    "The other teacher winced and shook his head. \"Actually,\" he said, looking away, \"it is.\""
    nvl clear
    "\"Is it any question in the face of events like that, or other, interesting 'withdrawals' in the school's past, most coinciding with questionable behavior on the part of a student—\""
    "\"You have evidence to support these allegations?\" the student council president asked, sounding genuinely intrigued."
    nvl clear
    "She nodded, tabbing past a few more example pictures of Emiri until she reached the incident list. \"But, as I was saying,\" she continued, \"is it that surprising that no student trusts the administration enough to come forth? You speak of the law, and order, but where's the justice in a system that sweeps the problem beneath the rug? This school isn't nearly as clean as it wants to claim! How many girls have to endure this humiliation to satisfy this school's pride!?\""
    nvl clear
    "She spread her arms in a helpless gesture, glancing at both teachers, then the student council president. \"And if the police were involved immediately, what would they do? Make the entire thing public first, and then start investigating in their way? Every student and teacher in this school would need to be questioned — in a way, even though he didn't tell me his reasons, Kyon did this school a {i}huge{/i} favor by managing things like this."
    nvl clear
    "\"Now the police only have to question those involved ... and he obtained a signed confession from one of the ringleaders, to say nothing of the other evidence we've amassed! Realistically, this is the smallest amount of publicity you can expect to endure for such an incident....\" Her eyes hardened as she trailed off. \"While still looking out for the interests of the students. Or was {i}this{/i} what your slogan of 'student independence' was supposed to lead to!?\""
    nvl clear
    "The president tilted his head, his glasses shining like mirrors directly into her eyes. She grit her teeth and grinned at him fiercely; she'd never believe it was a coincidence of lighting. He'd obviously watched enough anime to learn to master the effect to conceal his eyes and hide his emotions. That he was hiding behind it now....."
    nvl clear
    "\"What was that,\" he said icily, \"about putting words in the mouths of others?\""
    "\"You're dodging the issue,\" she challenged him."
    nvl clear
    "\"Right, enough, fine,\" Okabe said from the side of the room, his expression sour. \"Suzumiya, if what you're saying is true about incidents being covered in the past to make the school look better, then maybe some small part of why Kyon-kun and the others felt the need to do this themselves is explained. But in any case, it's not right for a student to take matters such as these into their own hands. As has been mentioned before, 'the ends justify the means' is not an acceptable answer, here."
    nvl clear
    "\"Worse, after all is said and done, if we let this pass without reprimand, we send the message to the students that the faculty are incompetent at best, and malicious at worst. We tell every student that the outside world this school is intended to prepare them for is a place where they cannot trust in any strength but their own. I'll even go so far as to say what you suggest would undermine the very society we live in.\""
    nvl clear
    "\"Interesting,\" the president remarked, his mouth a flat line, his eyes hidden behind his lenses. Emiri sat in her chair, dutifully recording everything by hand on her notepad. The other teacher sighed and hung his head, obviously worn out by the process."
    nvl clear
    "\"It is interesting,\" Koizumi noted, speaking again for the first time in several minutes, \"to see that the student body in general thinks very highly of Kyon-kun at just this moment. Certainly, almost all of the girls — in any event, a solid fifty percent of the population, at a minimum. Why wouldn't they look up to Kyon, Tsuruya-san, and Nagato as heroes? They alone protected the virtue of upstanding, innocent students by exposing the unfortunate darkness that lurked within our otherwise upstanding school."
    nvl clear
    "\"If they were to be reprimanded, and punished, that would cement their images as martyrs. At least ... if certain documents linking 'withdrawals' to certain unacceptable mischief were to be circulated. Then it would be seen as fact that the school was untrustworthy, going so far to punish any effort to improve the situation and mask what you are correct to say would be perceived as incompetence.\""
    nvl clear
    "\"A...are you ... {i}threatening{/i} the school?\" Okabe asked, his eyes widening in amazement. Haruhi felt a little stunned herself. She'd dug up the evidence for her report, but hadn't considered how useful it genuinely was as leverage ... anyone who was willing could find the same information from the public record."
    nvl clear
    "Still, coming from Koizumi, who she had seen act genuinely forceful exactly one time ... going back to that horrid memory of the only time she'd seen Kyon genuinely angry at {i}her{/i}.... This was a new face for the boy, she thought. His smile had even lessened, becoming thinner, and much more dangerous."
    nvl clear
    "\"Koizumi-kun,\" Okabe warned, shaking his head as he stood upright, no longer leaning against the wall, \"this is very serious—\""
    nvl clear
    "\"I think our answer here is clear,\" the other teacher cut in, suddenly. \"Okabe-sensei, the administration has already passed this decision down to the student council. I believe I see why. Punishing Kyon and the others would make them martyrs in the eyes of the students. Rewarding them would be going too far the other direction. But doing {i}nothing{/i}, and allowing the students to manage themselves, and the authorities to handle the criminal elements...."
    nvl clear
    "\"And, anyway, that all aside, all we're doing here is undermining the authority of the student council we have in place. Letting them handle it allows the student body to see that they're well represented by their own peers.\""
    nvl clear
    "Okabe looked like he was trying to swallow something particularly bitter, but nodded. \"Fine,\" he grumbled. \"Fine.\""
    "\"On that point,\" the teacher continued, glancing at the students, \"we will let you finish this on your own ... but we naturally will need copies of the meeting notes."
    nvl clear
    "Haruhi grinned, crossing her arms over her chest, as the student council president's head lowered, and she caught his resigned expression. She'd already won, as far as she was concerned. Did Kyon feel that same satisfied victorious surge right now, she wondered? He should be happy, knowing he'd solved the problem for good, and she was covering for him where she'd agreed to."
    nvl clear
    "Yeah, she decided, he had to feel as positive as she did right then."
    nvl clear
    
    "After reaching the largely abandoned temple grounds, they'd had enough privacy for Mori to explain things while they slowly strolled around. Tsuruya had listened to Mori's explanation with only occasional questions. In point of fact, when Mori had seemed to veer off and try to explain the roles of the others involved in Haruhi's life, Tsuruya insisted that Mori remain on topic, since she was concerned with the Organization and their involvement with Haruhi specifically. After hearing it all out, she gave a slow nod."
    nvl clear
    "\"So,\" she said, after an extended, thoughtful silence. \"Kyon-kun, was that thing you asked for from aliens, or time travelers?\""
    "\"Aliens,\" he answered. \"As we understand it, anyway. Ironically enough, it was to try and help them learn to slide to alternate dimensions. But that's not really important right now, I think. I mean ... do you believe it?\""
    nvl clear
    "\"I do!\" she agreed, nodding. \"After all, didn't Kyon-kun somehow vanish while we were sleeping together?\""
    "Mori made a pained, choking noise and nearly fell over. \"What!?\" she protested, horrified."
    nvl clear
    "Kyon ignored the woman. Yuki seemed completely unperturbed by the comment, only glancing at Mori with what seemed to be mild curiosity. \"Yeah,\" he agreed. \"Nagato teleported me to her apartment for ... eh ... it was personal.\""
    "Another strangled noise escaped Mori's throat as she stared with something like raw terror at Kyon. \"S...sir,\" she managed, \"you.... Suzumiya....\""
    nvl clear
    "Tsuruya looked thoughtful, but equally indifferent to Mori. \"Okies!\" she decided. \"Let's wrap up that last bit of trouble with the Sumiyoshi-rengo! I can't do it alone, but if I finish this and pass my trial, then maybe I can help Kyon-kun like the others can!\""
    nvl clear
    "\"Right,\" he agreed, frowning. \"So, kick in the door to their place and fight how many of them?\""
    "\"Can't be more than twenty,\" Tsuruya said, nodding confidently. \"We should be able to handle them!\""
    "\"Oh, gods,\" Mori moaned, one hand rising to cover her eyes. \"Sir! Do you at least use {i}protection{/i}?\""
    nvl clear
    "\"He has not been given any,\" Yuki answered. \"It has not previously been requested.\""
    "\"Use protection!\" Mori demanded, her voice nearly a screech, her hands balled into fists, her entire body shaking. \"You must! Kyon-ku— That is ... Sir! {i}Please{/i}!\""
    nvl clear
    "Why was she suddenly getting so bent out of shape, he wondered. \"You didn't say anything except that I was on my own the last time I went out to do this with Tsuruya-kun,\" he said, mildly reproachful. \"I had to demand assistance from you that time!\""
    nvl clear
    "\"B...but,\" she protested, wincing. \"I ... I didn't {i}know{/i}!\" She cut herself off suddenly and took a deep, calming breath. After a heartbeat, she recovered her seemingly unshakable demeanor. \"In any case,\" she said evenly, \"I will ensure personally that you are adequately supplied with what you need from this point forward.\""
    nvl clear
    "\"Oh?\" he asked, raising an eyebrow. \"Do you have anything with you?\""
    "Mori's face turned beet red. \"No,\" she said stiffly. \"Of course not. I can— I {i}will{/i} get it for you, rather.\" She put her hand to her face and sighed. \"If you don't mind, Sir, I'll go take care of that now.\""
    nvl clear
    "\"It's fine,\" Tsuruya remarked, nodding. \"I'll call my driver and set things up for our next mission.\""
    "Hands still trembling, Mori quickly hurried away down the stairs to where Arakawa waited in the car."
    nvl clear
    "He turned to look at Yuki. \"Oh,\" he said belatedly, frowning. \"Um, we should get you home.\""
    "Yuki shook her head once, moving a half-step closer to him, but not saying anything."
    nvl clear
    "\"You want to come with us?\" he asked in surprise, while Tsuruya barked a string of orders into her cell phone. Yuki's gaze slowly rose to meet his, and she gave a single sharp nod. He was about to protest when he caught himself. This was Yuki, after all ... and even if she didn't have all her powers and abilities, she had to learn the martial arts he'd learned in order to train him. She outmatched him by several orders of magnitude; why wouldn't he want her help against an unknown yakuza?"
    nvl clear
    "Kyon wished he could shake the feeling of impending doom that seemed to hang over him. What protection was Mori going to get, anyway? Maybe he'd be lucky, and it'd be a bulletproof vest — or better. That was worth hoping for ... but he wasn't likely to get it before the next assignment."
    nvl clear
    
