## Chapter 2 - Friday, February 15th
##
## Kara is absent. [player] thinks nothing of it.
## The chapter ends by making clear to the player (not to [player]) that Kara died by suicide that evening.
## Handled without method or detail, with weight, not as spectacle.

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
            "I hope she makes him happy.",
            "",
            "I hope somebody does.",
        ])
    )

label ch2_main:
    call day_card("Friday, February 15th") from _call_day_card_ch2
    call ch2_morning from _call_ch2_morning
    call ch2_first_period from _call_ch2_first_period
    call ch2_choir from _call_ch2_choir
    call ch2_lunch from _call_ch2_lunch
    call ch2_club from _call_ch2_club
    call ch2_evening from _call_ch2_evening
    call ch2_kara from _call_ch2_kara
    return

########################################################################
## Morning
########################################################################
label ch2_morning:
    scene bg bedroom
    with dissolve_scene_full
    play music t2

    "My phone buzzes at 6:45 AM."
    "{i}Good morning. I'm sorry, is this too early? I wasn't sure what the rules are. - Yuri{/i}"
    "She signs her texts. She's always signed her texts. I forgot how much I liked that."
    "{i}There are no rules. Good morning.{/i}"
    "{i}I'll see you at lunch? - Yuri{/i}"
    "{i}You'll see me at lunch.{/i}"
    "I lie there and grin at the ceiling for a solid five minutes."

    scene bg residential_day
    with wipeleft_scene

    show sayori 4m zorder 2 at t11
    s "[player]! [player] [player] [player]!"
    mc "Good morning to you too."
    s 4r "Yuri told Monika and Monika told me and I'm telling YOU that I KNOW!"
    mc "How did-"
    s 1r "It's a small club!"
    s 1q "I'm so happy for you. Really, really happy."
    s 1y "You were so sad all winter, and you pretended you weren't, and I pretended I didn't notice you pretending."
    mc "...Thanks, Sayori."
    s 4l "Rule number one is working!"

    "It's a cold, bright morning. I feel like I could run the whole way to school."
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

    "First period. I rehearsed it the whole way up the stairs."
    "{i}Kara, I got your letter. Thank you. Really. It meant a lot. But...{/i}"
    "Every version sounded terrible. I decided I'd just be honest and hope it came out right."

    "Our bench is empty."
    "Her stool is pushed in. Her side of the bench is wiped clean, the way she always leaves it."

    hale "Alright, people! Kara's out today, so [player], you're flying solo. Try not to blow anything up."
    mc "Is she okay?"
    hale "Didn't say. Office just has her down as absent."
    hale "There's a cold going around. Half of the third period is out. Wash your hands, everybody! Science!"

    "A cold."
    "Honestly, the first thing I feel is relief. Which I'm not proud of."
    "One more weekend to figure out what to say."

    "I do the lab alone. It's measuring the speed of sound with a tuning fork and a tube of water, and it goes fine, and it's weirdly quiet without her."
    "When I go to put the tuning fork back, I notice her notebook in our shared drawer."
    "Spiral-bound. Little blue flower on the cover."
    "I almost open it. I don't. It's hers."

    menu:
        "Should I leave her something?"

        "Leave a note in her notebook.":
            $ left_note_kara = True
            "I tear a sheet off my own notebook and write on it, slowly, so my handwriting is at least readable."
            "{i}Kara - Did the speed of sound lab without you. It was boring. Hope you feel better. I got your letter. Can we talk on Monday? - [player]{/i}"
            "I fold it in half and tuck it inside the front cover of her notebook, where she'll see it first thing."
            "There. That's a start. That's honest."

        "Leave it alone.":
            $ left_note_kara = False
            "I'll tell her it was here on Monday. I'll tell her everything on Monday."

    hale "Clean up! And it's Friday, so I'm legally required to say: have a good weekend, make good choices."

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
    z 2c2 "So? Did you find her? The mystery girl? Did you do the thing? Was there a dramatic moment? Was it raining?"
    mc "It wasn't raining."
    mc "...And it wasn't her. Well. It's complicated. I got back together with my ex."
    z 2c13 "Wait. WAIT. You got a mystery love letter and then got back with somebody {i}else?{/i}"
    z 2c11 "Dude, that's the most chaotic thing anyone in this choir has ever done. And Benny from the tenors once ate a whole tube of chapstick."
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
        cas 1a "Good."
        hide cassian
        with dissolve
    else:
        "On the water break, Cassian is sitting alone by the window with his eyes closed. He doesn't look at anyone."

    "In the back row, Oni isn't mouthing the words today."
    "He's just looking out the window, toward the side of the building where the science wing is."
    "He does it for the whole period."

    stop music fadeout 2.0
    return

########################################################################
## 5th period - Lunch with Yuri and Natsuki
########################################################################
label ch2_lunch:
    scene bg restaurant
    with wipeleft_scene
    play music t5

    "Lunch."
    "I sit at the usual table by the window. Natsuki's already there."
    "Then Yuri comes in, holding her tray like a shield, and stops."

    show natsuki 2g zorder 2 at t21
    show yuri 3o zorder 2 at t22
    y "Um... is it alright if I-"
    n 2c "Oh my gosh. Sit down. You're making the whole café nervous."
    y 3q "Th-thank you, Natsuki."

    "Yuri sits next to me. Close. Our elbows touch."
    "Natsuki stares at our elbows, then at me, then at her sandwich."

    n 1t "So. You two are, like, official now? Again?"
    y 1n "I... yes. I believe so. Is that... is that alright with you?"
    n 1k "Why would it not be alright with me?"
    y 1g "You're his best friend. I thought perhaps you'd want to... I don't know. Threaten me."
    n 1d "Ahahaha!"
    n 2t "Okay, I like you a little more now."
    n 2f "Yes. Fine. Consider yourself threatened. If you make him mope for another three months, I'm putting hot sauce in your tea."
    y 1j "That seems fair."
    n 1l "It IS fair!"

    "And then they're... talking. About a manga Natsuki's reading and a novel Yuri's reading that turn out to be weirdly similar."
    "I eat my six-dollar chicken nuggets and watch them and feel happy in a way that's almost uncomfortable."

    show natsuki 1a zorder 2 at t21
    "At one point Yuri laughs, really laughs, and Natsuki looks at me."
    "It's a strange look. Soft. Like she's looking at something from a long way off."
    n 1j "..."
    mc "What?"
    n 2s "Nothing! You have ketchup on your face. It's disgusting. Fix it."

    "I don't have ketchup on my face. I check anyway."

    "Across the café, Zach is wandering between tables with his tray, looking for a seat like a lost golden retriever."
    "Every table near him is full of couples. It's still basically Valentine's Day, aftershock edition."

    menu:
        "Zach looks lost."

        "Wave Zach over to sit with us.":
            $ invited_zach = True
            mc "Zach! Over here!"
            show natsuki 2g zorder 2 at t31
            show yuri 1g zorder 2 at t32
            show zach 2c4 zorder 2 at t33
            z "You're a lifesaver. I was about to eat in the bathroom. Like a villain."
            n 2c "Who's this?"
            mc "Zach. From choir."
            z 2c2 "Zach Moreau. Baritone. Tragically single. Big fan of this table."
            n 2t "...He can stay."
            y 1b "It's very nice to meet you, Zach."
            z 2c20 "Oh, wow, okay, she talks like a book. That's so cool. Do you always talk like a book?"
            y 3o "I- I suppose I do?"
            "Zach steals one of my nuggets, starts an argument with Natsuki about whether manga counts as literature, and loses it badly."
            "He seems really happy about losing it."
            z 2c10 "Same time Monday? I'm making this a thing. This is my table now."
            n 2s "It is NOT your table."
            z 2c4 "It's a little bit my table."

        "Let him find his own seat.":
            $ invited_zach = False
            "He finds a spot at the end of a table full of seniors who pretend he isn't there."
            "He eats fast and leaves early."

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
    m 2b "I thought we could do a book swap. Bring one book you love, give it to someone in the club, and next week they tell us what they thought."
    m 1j "It's a good way to see the world through someone else's eyes."

    show monika 1a zorder 2 at t31
    show sayori 4r zorder 2 at t32
    show natsuki 2t zorder 2 at t33
    s "I brought a cookbook!"
    n 2g "A cookbook isn't a book you {i}love,{/i} Sayori, it's a book you use."
    s 1c "I love it! It has pictures of pancakes!"
    n 1d "...Okay, that's a valid reason."

    "We draw names out of Monika's pencil cup."
    "I get Natsuki. Natsuki gets me. She immediately tries to trade, and Monika won't let her."

    show natsuki 4c zorder 3 at f33
    n "Fine. Here."
    "She hands me a manga, volume one of something called {i}Parfait Girls{/i}. It's been read so many times the spine is white."
    n 1i "It's my favorite one. So don't, like, bend it. Or get food on it. Or read it in the bathtub."
    mc "Who reads in the bathtub?"
    n 1s "Some people! Weird people! Just don't!"
    show natsuki 1a zorder 2 at t33
    "I give her the book I brought: a sci-fi novel about a lighthouse keeper on a planet where it's always night."
    "She turns it over and over in her hands."
    n 1j "...Is this your favorite?"
    mc "Yeah."
    n 1u "Oh."
    n 1y "Okay. I'll read it. Carefully."

    show monika 1a zorder 2 at t31
    "Sayori gets Yuri's book, an enormous gothic horror novel, and Yuri gets Sayori's pancake cookbook, and they both seem genuinely delighted about it."
    "Monika gets the book that Monika brought, by accident, and laughs about it for a full minute."

    scene bg club_day
    with dissolve_scene_half
    "The rest of the meeting is just... nice."
    "Yuri reads next to me with her shoulder against mine. Sayori tries the pancake recipe in her head out loud. Natsuki reads my book with a frown of total concentration, turning the pages with two fingers so she doesn't bend them."
    "Monika writes something in a notebook for the student council and hums."
    "It's the kind of afternoon I'll want to remember later. I don't know that yet. I just know it's good."

    show yuri 1a zorder 2 at t11
    y "[player]... would you like to do something tomorrow? Saturday?"
    y 3n "There's a bookstore downtown with a café in it. They have a cat. The cat's name is Bartholomew."
    mc "I would love to meet Bartholomew."
    y 3s "He's very dignified."

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
    "I lie on my bed and read the first three chapters of {i}Parfait Girls{/i}. It's better than I expected. I'm not going to tell Natsuki that. She'd be insufferable."
    "My phone buzzes."
    "{i}Bartholomew says he's looking forward to meeting you. - Yuri{/i}"
    "{i}Did Bartholomew actually say that?{/i}"
    "{i}He meowed. I'm translating. - Yuri{/i}"
    "I laugh out loud, alone in my room, like an idiot."

    "My jacket is hanging on the back of my chair. Two envelopes in the pockets."
    "I take out Kara's letter and read it again."
    "{i}You probably don't think about me that much. That's okay!{/i}"
    "{i}I'm not brave enough to sign this.{/i}"
    "- Anonymous. And the little blue flower."
    "I think about throwing it away. It feels wrong to."
    "I put it in my desk drawer instead."
    "I'd text her, if I could. Just to ask if she's okay."
    "But I don't have her number. Nobody does. Her dad won't allow it."
    "{i}Monday,{/i} I tell myself. {i}First period. I'll be honest. She'll understand.{/i}"
    "{i}She said it was okay. That's okay, with an exclamation point.{/i}"

    "I fall asleep with the light on, smiling."

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
    "..."
    scene bg science_lab
    with Dissolve(3.0)
    play music t9 fadein 4.0

    "The science lab. Thursday evening, after everyone had gone home."
    "The lights hum."
    "A spiral notebook lies open on the bench by the window. The page is dated, in small, neat handwriting."

    call show_note(note_kara_page) from _call_show_note_kara

    "A small blue flower is drawn at the bottom of the page."
    "The notebook stays in the drawer, where she left it."
    "She doesn't come to school on Friday."

    stop music fadeout 4.0
    scene black
    with Dissolve(3.0)
    pause 2.0

    "Kara died by suicide on the evening of Friday, February 15th."
    "She was fourteen years old."
    pause 2.0
    "She had told no one how much she was hurting."
    "No one at school will be told what happened."
    pause 3.0

    $ quick_menu = True
    return
