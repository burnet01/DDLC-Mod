## Chapter 2 - Friday, February 15th
##
## Kara is absent. [player] thinks nothing of it.
## Branches on who [player] ended Thursday with (partner) and on sayori_dead.
## Sayori route, wrong answer: [player] finds her Friday morning and never goes to school.
## Both deaths are shown as story: what is seen, heard and felt. Never the method.

init python:
    note_kara_page = Note(
        title = "Thursday",
        text = "\n".join([
            "4:10. Club's probably still going. That's okay. I can wait.",
            "",
            "4:35. The lights are humming. I told him about that. I wonder if he remembers.",
            "",
            "5:00. Mr. Hale came by and asked if I needed anything. I said I was finishing the lab write-up. I already finished it.",
            "",
            "5:20. It's getting dark.",
            "",
            "5:40. I don't think he's coming.",
            "",
            "That's okay. It really is. I said it was okay in the letter, so it has to be.",
            "",
            "I hope somebody makes him happy.",
            "",
            "I hope somebody does.",
        ])
    )

label ch2_main:
    call day_card("Friday, February 15th") from _call_day_card_ch2
    if sayori_dead:
        call ch2_sayori_found from _call_ch2_sayori_found
        call ch2_sayori_day from _call_ch2_sayori_day
    else:
        call ch2_morning from _call_ch2_morning
        call ch2_first_period from _call_ch2_first_period
        call ch2_choir from _call_ch2_choir
        call ch2_lunch from _call_ch2_lunch
        call ch2_club from _call_ch2_club
        call ch2_evening from _call_ch2_evening
    call ch2_kara from _call_ch2_kara
    return

########################################################################
## Sayori route, bad answer - Friday morning
########################################################################
label ch2_sayori_found:
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    "6:45 AM."
    "I'm up before my alarm. I said I'd come get her every morning. That's my job now."
    "I even put on a clean shirt. That's how serious I am about it."

    scene bg residential_day
    with wipeleft_scene
    "Her house is twenty steps from mine. I've counted."
    "Her mom's car is already gone. She works early on Fridays."
    "I knock. Nothing."
    "I knock again."
    mc "Sayori! Rule number one! Nobody's allowed to be late on a Friday!"
    "Nothing."
    stop music fadeout 2.0
    "The door's unlocked. It's always unlocked. Her mom says it's a safe street."

    scene bg house
    with wipeleft_scene
    "The house is very quiet."
    "Her backpack is on the stairs. Her shoes are by the door. Both of them. She didn't forget them this time."
    mc "Sayori? You up?"
    "Up the stairs. Her door is closed. There's a sticker on it from when we were seven. A smiling raincloud."
    mc "Okay, I'm coming in. If you're in your pajamas, that's your fault."
    "I open the door."

    $ quick_menu = False
    $ renpy.music.set_volume(1.0, channel="sound")
    play sound "sfx/s_kill_glitch1.ogg"
    scene black
    show s_kill_bg zorder 1 at s_kill_bg_start
    show s_kill zorder 2 at s_kill_start
    pause 4.0
    play music hb
    show s_kill_bg_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill_bg2_zoom zorder 1
    show s_kill2_zoom zorder 3
    pause 1.5

    "..."
    "Sayori."
    "No."
    "No, no, no, no, no."
    "This isn't real. This is a dream. I'm still in bed. My alarm is going to go off."
    "Her eyes are open."
    "Her hands are cold."
    "My alarm doesn't go off."
    "{i}I'll make you happy. Every day. That's my job now.{/i}"
    "{i}You shouldn't have to. It's not your job to fix me.{/i}"
    "She told me. She told me, and I made it about me. I told her I would fix it, like it was something I could fix by trying hard."
    "And she smiled, so I stopped listening."

    stop music
    scene black
    with dissolve_scene_full
    pause 2.0
    $ quick_menu = True
    return

label ch2_sayori_day:
    scene bg bedroom
    with dissolve_scene_full
    play music t9 fadein 3.0

    "The rest of Friday comes in pieces."
    "Calling 911 with my hands shaking so badly I dialed it wrong twice."
    "Sitting on the curb while men in uniforms walked in and out of her house."
    "Her mom's car pulling up too fast. The sound she made. I'm never going to forget the sound she made."
    "My mom holding on to me in the kitchen. I don't remember walking home."

    "A police officer with gray hair sat at our kitchen table and asked me questions in a very gentle voice."
    "At the end, she put her hand on my shoulder."
    "\"Son. Listen to me. This is not your fault. Do you hear me? Depression is an illness. It lies to people. It lied to her. Not you.\""
    "I nodded. I didn't believe her."
    "I think I'm going to have to hear it a lot of times before I do."

    "My phone has been buzzing all day. I haven't looked at it."
    "Around six, I do."
    "{i}[player]. I'm outside. I'm not leaving. - Natsuki{/i}"
    "{i}I heard. I'm so sorry. If you need anything at all, at any hour. - Yuri{/i}"
    "{i}The school's sending an email tonight. Counselors all next week. Please talk to one. Please. - Monika{/i}"

    scene bg natsuki_house_night
    with wipeleft_scene
    show natsuki 1n zorder 2 at t11
    "Natsuki is sitting on my front steps in the dark. Her eyes are swollen."
    n "Hey, dummy."
    "She doesn't say anything else. She doesn't have to."
    "She sits next to me on the cold step until my mom makes her go home. She doesn't let go of my sleeve the whole time."
    hide natsuki
    with dissolve

    scene bg bedroom
    with dissolve_scene_full
    "Later, I hang my jacket on the back of my chair, and something crinkles in the inside pocket."
    "A plain white envelope. A tiny blue flower next to \"Anonymous.\""
    "I'd forgotten it was there."
    "I'd forgotten all about it."
    "I put it in my desk drawer without reading it again. {i}Monday,{/i} I think. {i}I'll deal with it Monday.{/i}"
    "I don't sleep."

    stop music fadeout 4.0
    scene black
    with dissolve_scene_full
    pause 2.0
    return

########################################################################
## Morning
########################################################################
label ch2_morning:
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    if partner == "yuri":
        "My phone buzzes at 6:45 AM."
        "{i}Good morning. I'm sorry, is this too early? I wasn't sure what the rules are. - Yuri{/i}"
        "She signs her texts. She's always signed her texts. I forgot how much I liked that."
        "{i}There are no rules. Good morning.{/i}"
        "{i}I'll see you at lunch? - Yuri{/i}"
        "I lie there and grin at the ceiling for a solid five minutes."
    elif partner == "natsuki":
        "My phone buzzes at 6:45 AM."
        "{i}gm{/i}"
        "{i}dont make it weird{/i}"
        "{i}i mean it. dont make it weird at school{/i}"
        "{i}...gm, natsuki{/i}"
        "{i}SEE THATS WEIRD{/i}"
        "I lie there and grin at the ceiling for a solid five minutes."
    elif sayori_got_help:
        "My phone buzzes at 6:30 AM."
        "{i}i told my mom. she cried. i cried. we ate ice cream at 11pm{/i}"
        "{i}ms reyes at 7:15. you said you'd sit outside the door. you still can say no!!{/i}"
        "{i}I'm already putting my shoes on.{/i}"
    else:
        "No texts. Which is normal."
        "I lie in bed for a while and think about yesterday, and then I make myself stop."

    scene bg residential_day
    with wipeleft_scene

    if sayori_got_help:
        show sayori 1t zorder 2 at t11
        "Sayori is waiting on her porch. On time. That's never happened before in recorded history."
        s "Hi."
        mc "Hi."
        s 1u "I'm really scared."
        mc "I know. I'll be right outside."
        "I sit in the plastic chair outside Ms. Reyes' office for forty minutes. I miss most of first period. I don't care."
        "When Sayori comes out, her eyes are red and she's holding a stress ball shaped like a frog."
        s 1y "She says I'm not broken. She says lots of people have rainclouds, and there are actual things that help."
        s 1q "I have to come back Tuesday. And there's a doctor. And I'm allowed to have bad days. That's an actual rule. She wrote it down."
        if partner == "sayori":
            "She takes my hand on the way down the hallway. She doesn't let go until we have to split up for class."
        s 4r "Go! You're missing science!"
        stop music fadeout 2.0
        return

    show sayori 4m zorder 2 at t11
    s "[player]! Good morning!"
    if partner == "yuri":
        s 4r "Yuri told Monika and Monika told me and I'm telling YOU that I KNOW!"
        s 1q "I'm so happy for you. Really, really happy."
        s 1y "You were so sad all winter, and you pretended you weren't, and I pretended I didn't notice you pretending."
    elif partner == "natsuki":
        s 4r "Natsuki texted me in ALL CAPS at nine o'clock last night and then said \"ignore that\" and then didn't say anything else!"
        s 1x "Sooo... is there something you want to tell me? As your neighbor?"
        mc "...Maybe."
        s 4l "I KNEW IT! Third grade! I called it in third grade!"
    else:
        s 1g "How'd it go? The letter thing?"
        mc "It didn't."
        s 1u "Oh..."
        s 1q "Well. Rule number one is still in effect. I'll be extra happy for both of us."

    "It's a cold, bright morning."
    "I almost forget about the other letter."
    "Almost."

    stop music fadeout 2.0
    return

########################################################################
## 1st period - Kara is absent
########################################################################
label ch2_first_period:
    scene bg science_lab
    with wipeleft_scene
    play music t3

    if sayori_got_help:
        "I make it to first period with twenty minutes left."
    else:
        "First period. I rehearsed it the whole way up the stairs."
    "{i}Kara, I got your letter. Thank you. Really. It meant a lot...{/i}"
    if went_lab_late:
        "{i}I came to find you. I was four minutes late. I'm sorry.{/i}"
    "Every version sounded terrible. I decided I'd just be honest and hope it came out right."

    "Our bench is empty."
    "Her stool is pushed in. Her side of the bench is wiped clean, the way she always leaves it."

    hale "[player]! Kara's out today, so you're flying solo. Try not to blow anything up."
    mc "Is she okay?"
    hale "Didn't say. Office just has her down as absent. There's a cold going around."

    "A cold."
    "Honestly, the first thing I feel is relief. Which I'm not proud of."
    "One more weekend to figure out what to say."

    "I do the lab alone. It's measuring the speed of sound with a tuning fork and a tube of water, and it's weirdly quiet without her."
    "Her notebook is in our shared drawer. Spiral-bound. Little blue flower on the cover."
    "I almost open it. I don't. It's hers."

    menu:
        "Should I leave her something?"

        "Leave a note in her notebook.":
            $ left_note_kara = True
            "I tear a sheet off my own notebook and write on it, slowly, so my handwriting is at least readable."
            "{i}Kara - Did the speed of sound lab without you. It was boring. Hope you feel better. I got your letter. Can we talk on Monday? - [player]{/i}"
            "I tuck it inside the front cover of her notebook, where she'll see it first thing."

        "Leave it alone.":
            $ left_note_kara = False
            "I'll tell her it was here on Monday. I'll tell her everything on Monday."

    hale "Clean up! It's Friday, so I'm legally required to say: have a good weekend, make good choices."
    "On the way out I look back at her empty stool."
    "Then I go to second period, and I don't think about it again."

    stop music fadeout 2.0
    return

########################################################################
## 2nd period - Choir
########################################################################
label ch2_choir:
    scene bg music_room
    with wipeleft_scene
    play music t3

    "Second period. Choir."
    "I walk in, and three separate tenors make kissing noises at me."

    show zach 2c4 zorder 2 at t11
    z "Mr. Valentine! He lives!"
    mc "Please don't call me that."
    z 2c10 "Too late. It's in the group chat. It's your name now. Forever."
    z 2c2 "So? Did you find her? The mystery girl? Was there a dramatic moment? Was it raining?"
    if partner == "yuri":
        mc "It wasn't raining. And it's complicated. I got back together with my ex."
        z 2c13 "Wait. You got a mystery love letter and then got back with somebody {i}else?{/i}"
        z 2c11 "Dude, that's the most chaotic thing anyone in this choir has ever done. And Benny from the tenors once ate a whole tube of chapstick."
    elif partner == "natsuki":
        mc "It's complicated. I didn't find her. I... kind of ended up with my best friend."
        z 2c13 "Your BEST FRIEND? The tiny angry one with the pink hair? She threatened me with a stapler in September!"
        z 2c10 "Okay, that's actually adorable. I hate that it's adorable."
    elif partner == "sayori":
        mc "It's complicated. I ended up with my neighbor."
        z 2c13 "The NEIGHBOR? The girl-next-door thing? People actually do that?!"
        z 2c10 "Dude, you're living in a movie. A weird movie. With a secret admirer subplot nobody resolved."
    else:
        if went_lab_late:
            mc "I went to find her. I was too late. She'd already gone."
        else:
            mc "No. I didn't find her."
        z 2c26 "Oh. Dude."
        z 2c5 "That's okay. There's like four billion girls. Statistically one of them is gonna write you another letter."
        z 2c26 "...That was supposed to sound nicer. Sorry."
    hide zach
    with dissolve

    show dunn a zorder 2 at t11
    dunn "Places, gentlemen. Sailor song. And if anyone hums \"Here Comes the Bride\" today, you're running scales until June."
    hide dunn
    with dissolve

    if told_cassian:
        "On the water break, Cassian stops next to my chair. He doesn't sit."
        show cassian 1a zorder 2 at t11
        cas "Did you talk to her?"
        mc "She's out today. Sick, I think."
        cas 1d "..."
        cas 1e "Monday, then. Don't let it go longer than that."
        mc "I won't."
        hide cassian
        with dissolve
    else:
        "On the water break, Cassian is sitting alone by the window with his eyes closed. He doesn't look at anyone."

    "In the back row, Oni isn't mouthing the words today."
    "He's just looking out the window, toward the science wing. He does it for the whole period."

    stop music fadeout 2.0
    return

########################################################################
## 5th period - Lunch
########################################################################
label ch2_lunch:
    scene bg restaurant
    with wipeleft_scene
    play music t5

    "Lunch. I sit at the usual table by the window. Natsuki's already there."

    if partner == "yuri":
        "Then Yuri comes in, holding her tray like a shield, and stops."
        show natsuki 2g zorder 2 at t21
        show yuri 3o zorder 2 at t22
        y "Um... is it alright if I-"
        n 2c "Oh my gosh. Sit down. You're making the whole café nervous."
        "Yuri sits next to me. Close. Our elbows touch."
        n 1t "So. You two are, like, official now? Again?"
        y 1n "I... yes. Is that alright with you?"
        n 1k "Why would it not be alright with me?"
        y 1g "You're his best friend. I thought perhaps you'd want to threaten me."
        n 2f "Fine. Consider yourself threatened. If you make him mope for another three months, I'm putting hot sauce in your tea."
        y 1j "That seems fair."
        "At one point Yuri laughs, really laughs, and Natsuki looks at me."
        "It's a strange look. Soft. Like she's looking at something from a long way off."
        n 2s "What? You have ketchup on your face. Fix it."
        "I don't have ketchup on my face. I check anyway."
    elif partner == "natsuki":
        show natsuki 1o zorder 2 at t11
        "She sees me and goes red all the way to her ears."
        n "This is NOT a date. It's lunch. We always have lunch."
        mc "I didn't say anything."
        n 1s "You were THINKING it!"
        "She shoves half a sandwich at me. Then, after a second, she shoves the other half at me too."
        mc "That's your whole sandwich."
        n 1j "I made too much. On purpose. Like always."
        n 1y "...I don't have to pretend I didn't anymore. That's kind of nice."
    elif partner == "sayori":
        show natsuki 2c zorder 2 at t21
        show sayori 1q zorder 2 at t22
        "Sayori drops in next to me with three cookies and her frog stress ball."
        n 2c "Why do you have a frog."
        s 1y "His name is Gerald. He's for bad days."
        n 1u "...Is today a bad day?"
        s 1q "Nope! Today's a medium day! Medium days get cookies."
        "Natsuki looks at Sayori, then at me, then at our hands, which are touching under the table."
        n 1j "Huh. Okay. Took you two long enough."
    else:
        show natsuki 1g zorder 2 at t11
        "She shoves half a sandwich at me without asking. She always makes too much."
        n 1u "You still look like somebody ran over your dog."
        mc "I'm fine."
        n 1n "You say that a lot."
        "We eat. She talks about a manga for twenty minutes straight, which I'm pretty sure she's doing on purpose, so I don't have to talk."

    "Across the café, Zach is wandering between tables with his tray, looking for a seat like a lost golden retriever."

    menu:
        "Zach looks lost."

        "Wave Zach over to sit with us.":
            $ invited_zach = True
            mc "Zach! Over here!"
            show natsuki 2g zorder 2 at t21
            show zach 2c4 zorder 2 at t22
            z "You're a lifesaver. I was about to eat in the bathroom. Like a villain."
            n 2c "Who's this?"
            z 2c2 "Zach Moreau. Baritone. Tragically single. Big fan of this table."
            n 2t "...He can stay."
            "Zach steals one of my nuggets, starts an argument with Natsuki about whether manga counts as literature, and loses it badly."
            "He seems really happy about losing it."
            z 2c10 "Same time Monday? This is my table now."
            n 2s "It is NOT your table."

        "Let him find his own seat.":
            $ invited_zach = False
            "He finds a spot at the end of a table full of seniors who pretend he isn't there."

    stop music fadeout 2.0
    return

########################################################################
## After school - a normal club day
########################################################################
label ch2_club:
    scene bg club_day
    with wipeleft_scene
    play music t3

    show monika 1b zorder 2 at t11
    m "Okay, everyone! Normal club day today. No holidays, no hats."
    m 2b "Book swap. Bring one book you love, give it to someone in the club, and next week they tell us what they thought."

    "We draw names out of Monika's pencil cup."
    "I get Natsuki. Natsuki gets me."

    show natsuki 4c zorder 2 at t11
    n "Fine. Here."
    "She hands me volume one of {i}Parfait Girls{/i}. It's been read so many times the spine is white."
    n 1i "It's my favorite. So don't bend it. Or get food on it."
    "I give her my book: a sci-fi novel about a lighthouse keeper on a planet where it's always night."
    n 1j "...Is this your favorite?"
    mc "Yeah."
    n 1y "Okay. I'll read it. Carefully."
    hide natsuki

    scene bg club_day
    with dissolve_scene_half
    "The rest of the meeting is just... nice."
    if partner == "yuri":
        "Yuri reads next to me with her shoulder against mine."
    "Sayori tries the pancake recipe in her head, out loud. Natsuki reads my book with a frown of total concentration."
    "It's the kind of afternoon I'll want to remember later. I don't know that yet."

    if partner == "yuri":
        show yuri 1a zorder 2 at t11
        y "[player]... would you like to do something tomorrow? There's a bookstore downtown with a café in it. They have a cat named Bartholomew."
        mc "I would love to meet Bartholomew."
        y 3s "He's very dignified."
    elif partner == "natsuki":
        show natsuki 1s zorder 2 at t11
        n "Arcade. Tomorrow. Noon. Not a date."
        mc "It's a date."
        n 1v "IT'S AN ARCADE."
    elif partner == "sayori":
        show sayori 4r zorder 2 at t11
        s "Pancakes tomorrow! At my house! My mom says you can come! She says she's very proud of us!"
    elif yuri_score == 1:
        show yuri 3s zorder 2 at t11
        "On her way out, Yuri stops by my desk."
        y "It's not Valentine's Day anymore."
        y 3n "...That's all. I just wanted to say that."

    stop music fadeout 3.0
    return

########################################################################
## Evening at home
########################################################################
label ch2_evening:
    scene bg bedroom
    with dissolve_scene_full
    play music t8

    "Friday night."
    "I lie on my bed and read the first three chapters of {i}Parfait Girls{/i}. It's better than I expected. I'm not telling Natsuki that."
    if partner == "yuri":
        "{i}Bartholomew says he's looking forward to meeting you. - Yuri{/i}"
        "{i}He meowed. I'm translating. - Yuri{/i}"
    elif partner == "natsuki":
        "{i}which chapter r u on{/i}"
        "{i}3{/i}"
        "{i}DONT SKIP AHEAD{/i}"
    elif partner == "sayori":
        "{i}goodnight!! medium day!! - sayori & gerald{/i}"

    "My jacket is hanging on the back of my chair."
    "I take out Kara's letter and read it again."
    "{i}You probably don't think about me that much. That's okay!{/i}"
    "- Anonymous. And the little blue flower."
    "I put it in my desk drawer."
    "I'd text her, if I could. Just to ask if she's okay."
    "But I don't have her number. Nobody does. Her dad won't allow it."
    "{i}Monday,{/i} I tell myself. {i}First period. I'll be honest. She'll understand.{/i}"
    "I fall asleep with the light on."

    stop music fadeout 4.0
    scene black
    with dissolve_scene_full
    pause 2.0
    return

########################################################################
## What happened to Kara
########################################################################
label ch2_kara:
    $ quick_menu = False
    $ allow_skipping = False
    $ config.allow_skipping = False
    "..."
    scene bg science_lab
    with Dissolve(3.0)
    play music t9 fadein 4.0

    "The science lab. Thursday evening, after everyone had gone home."
    "The lights hum."
    "A spiral notebook lies open on the bench by the window."

    call show_note(note_kara_page) from _call_show_note_kara

    "A small blue flower is drawn at the bottom of the page."
    "She doesn't come to school on Friday."

    stop music fadeout 3.0
    scene black
    with Dissolve(3.0)
    pause 1.5

    "Friday, February 15th. 8:56 PM."
    "Willow Street."
    if sayori_dead:
        "Across town from a house with a smiling raincloud sticker on an upstairs door."
    "Her phone is on the kitchen counter, where it goes every night before nine."
    "There's nothing on it. There never is. No number he doesn't know."
    "Upstairs, her bedroom door is shut."
    "She isn't allowed to lock it."
    "Tonight it's locked."
    pause 2.0

    "8:59 PM."
    "Footsteps on the stairs. Heavy. The same footsteps every night."
    "A knock."
    "\"Kara. Phone check.\""
    "..."
    "\"Kara.\""
    "The handle turns. It doesn't open."
    "\"Kara, open this door.\""
    "..."
    "\"{i}Kara.{/i}\""
    pause 1.0
    play sound "sfx/s_kill_glitch1.ogg"
    show white zorder 5
    pause 0.15
    hide white
    pause 0.2
    "A sound comes out of him that doesn't sound like a person."
    "Then the door gives."
    pause 2.0

    "In the dark, in a house on Willow Street, the lights hum."
    "Sixty hertz. Almost a B-flat."
    "There's no one in the room left to hear it."
    pause 2.0

    "9:21 PM."
    "Two ambulances and a police car turn onto Willow Street. Lights on. No sirens."
    "A neighbor stands on her lawn in her slippers and cries."
    if sayori_dead:
        "Across town, a boy is lying awake. He won't sleep at all tonight."
        "But he isn't thinking about her. He won't think about her until Monday."
    else:
        "Across town, a boy is asleep with the light on."
    pause 3.0

    "Kara died by suicide on the evening of Friday, February 15th."
    "She was fourteen years old."
    pause 2.0
    "She had told no one how much she was hurting."
    "No one at school will be told what happened."
    pause 3.0

    $ allow_skipping = True
    $ config.allow_skipping = True
    $ quick_menu = True
    return
