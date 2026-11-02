## Chapter 1, after the club - The Valentine's choice
##
## Five routes:
##   Kara    -> she's still in the lab. She lives. Goes straight to the Kara ending.
##   Yuri    -> two choices decide whether you get back together.
##   Natsuki -> two choices decide whether her hidden crush comes out.
##   Sayori  -> one choice decides whether she lives. The wrong one: she dies Friday morning.
##   Monika  -> instant rejection. You can still go to the lab, but it's too late.
##
## Kara waited in the lab from 4:10 to 5:40 (see note_kara_page in ch2).

label ch1_after_club:
    scene bg club_day
    with dissolve_scene_full
    play music t9 fadeout 2.0

    "Everyone starts packing up."
    "The letter is in my jacket. I can feel the corners of it every time I breathe."
    "{i}If you like me back... find me? You'll know where.{/i}"
    "The science lab is on the second floor. If Kara's waiting, she's waiting there."

    show natsuki 2t zorder 2 at t11
    n "Gate. Five minutes. It's Thursday, dummy, don't make me wait."
    hide natsuki
    with dissolve

    "Sayori leaves without saying goodbye."
    "Sayori never leaves without saying goodbye."

    "Monika is at the teacher's desk, stacking the poems into a neat pile."

    show yuri 3o zorder 2 at t11
    y "[player]..."
    y 3p "C-could you stay a minute? Please? I won't keep you long."

    menu:
        "Where do I go?"

        "Go to the science lab. Find Kara.":
            $ vday_pick = "kara"
            call ch1_route_kara from _call_ch1_route_kara

        "Stay with Yuri.":
            $ vday_pick = "yuri"
            call ch1_route_yuri from _call_ch1_route_yuri

        "Catch up with Natsuki at the gate.":
            $ vday_pick = "natsuki"
            call ch1_route_natsuki from _call_ch1_route_natsuki

        "Go after Sayori.":
            $ vday_pick = "sayori"
            call ch1_route_sayori from _call_ch1_route_sayori

        "Ask Monika if the letter was from her.":
            $ vday_pick = "monika"
            call ch1_route_monika from _call_ch1_route_monika

    return

########################################################################
## Too late - the lab after 5:40
########################################################################
label ch1_too_late_choice:
    menu:
        "It's almost dark out."

        "Go to the science lab anyway.":
            call ch1_lab_late from _call_ch1_lab_late

        "Just go home.":
            "{i}Tomorrow,{/i} I tell myself. {i}I'll talk to her tomorrow.{/i}"
    return

label ch1_lab_late:
    scene bg science_lab
    with wipeleft_scene
    play music t9

    "I take the stairs two at a time. My watch says 5:44."
    "The lab door is unlocked. The lights are on."
    "Nobody's here."
    "Our bench by the window is wiped clean. Her stool is pushed in."
    "No. Not pushed in."
    "It's still turning. Very slowly. Like somebody just stood up from it."
    "On my side of the bench there's a fresh lab label. Blank. Just my name in her neat handwriting, and a tiny blue flower in the corner."
    "The ink's still wet."
    "I stand there for a long time, listening to the lights hum."
    "Almost a B-flat."
    $ went_lab_late = True
    stop music fadeout 3.0
    return

########################################################################
## KARA - she's still there
########################################################################
label ch1_route_kara:
    show yuri 1g zorder 2 at t11
    mc "Yuri, I'm sorry. I can't right now. There's somewhere I have to be."
    y 1h "Oh..."
    y 1u "Of course. I understand. Another time."
    hide yuri
    with dissolve
    "She doesn't look like she understands. I go anyway."

    scene bg corridor
    with wipeleft_scene
    "I take the stairs two at a time."
    "4:51."

    scene bg science_lab
    with wipeleft_scene
    play music t10

    "The lab door is open a crack. The lights are on."
    "The whole room is empty except for one stool, by the window, at our bench."

    show kara 1c zorder 2 at t11
    "Kara is writing in her notebook. Slowly. Like she's been writing the same page for a long time."
    "She looks up."
    "She drops her pen."

    k 1o "..."
    k 1e "[player]?"

    menu:
        "What do I say?"

        "\"It was you. The letter.\"":
            mc "It was you. Wasn't it? The letter."
            k 1t "..."
            k 1u "The flower gave it away. I knew it would. I almost didn't draw it."
            k 1v "And then I thought, if he doesn't notice the flower, then he was never going to notice anyway."

        "\"You said I'd know where.\"":
            mc "You said I'd know where."
            k 1h "..."
            k 1g "And you did."
            k 1u "I didn't actually think you would. I wrote it like a dare. To myself, I mean."

    "I sit down on my stool. The same one I sit on every morning."
    "Her notebook is open between us. I can see the top of the page. Times, written down the margin in her neat handwriting."
    "{i}4:10. 4:35.{/i}"

    k 1a "You don't have to be nice about it."
    k 1h "Whatever you came to say. I'd rather you were honest. I can take honest. It's the not knowing I can't do."

    menu:
        "Be honest."

        "\"I like you too.\"":
            mc "Okay. Honest."
            mc "I like you. I think I've liked you since you told me I carried the two."
            k 1w "..."
            k 1q "That was in {i}November.{/i}"
            mc "I know. I'm slow. Slow is smooth."
            k 1j "Ahaha... that's not what that means."

        "\"I don't know yet. But I came. I want to find out.\"":
            mc "I don't know yet."
            mc "But I didn't go home. I didn't go anywhere else. I came here."
            mc "I think I'd like to find out. If that's okay."
            k 1k "..."
            k 1j "That's the most honest thing anyone's ever said to me."
            k 1q "I think I'd like to find out too."

    "She looks down at her notebook."
    "Then, carefully, she turns it around so I can read it."
    "{i}4:10. Club's probably still going. That's okay. I can wait.{/i}"
    "{i}4:35. The lights are humming. I told him about that. I wonder if he remembers.{/i}"
    "Under that, she'd started writing something else. It's crossed out. Hard. Over and over, until the pen went through the paper."

    show kara 1h zorder 2 at t11
    k "I gave myself until five-forty."
    mc "Until five-forty for what?"
    k 1t "..."
    k 1u "To stop hoping. About you. About... a lot of things."
    k 1v "Things at home are really bad, [player]. They've been bad for a long time. I'm so tired. I'm tired all the time."
    k 1h "I wasn't going to tell anyone that. Ever."

    "The lights hum."
    "I think about what would have happened if I'd stayed in the clubroom. If I'd gone to the gate. If I'd gone home."
    "I think about five-forty."

    menu:
        "What do I say?"

        "\"Will you tell someone? Ms. Reyes, the counselor? I'll go with you.\"":
            $ kara_counselor = True
            mc "Will you tell someone? Not just me. Someone who can actually help."
            mc "Ms. Reyes. The counselor. Her office opens at seven."
            mc "You're here at six-fifty. I'll be here at six-fifty. I'll walk you there."
            k 1t "If my dad finds out..."
            mc "Then it's her job to deal with that. Not yours. You're fourteen."
            k 1u "..."
            k 1g "...Okay. Tomorrow. Six-fifty."
            mc "Six-fifty."

        "\"You don't have to carry it alone anymore.\"":
            mc "You don't have to carry it by yourself anymore. I'm here."
            mc "Every morning. Six-fifty. I'm not going anywhere."
            k 1u "You can't fix it, [player]."
            mc "I know. But you don't have to be alone in it."
            k 1g "..."
            k 1h "Maybe... maybe I'll talk to Ms. Reyes. The counselor. Maybe. Not tomorrow. But maybe."
            mc "I'll walk you there. Whenever."

    show kara 1a zorder 2 at t11
    "Behind her, the clock over the door clicks over."
    "5:40."
    "She sees me looking at it. She turns around and looks at it too."
    k 1p "Oh."
    k 1j "...It's five-forty."
    mc "Yeah."
    k 1k "You're still here."
    mc "I'm still here."

    "She picks up her blue pen. She takes my hand, turns it over, and draws a tiny flower on the back of it."
    k 1q "For luck."
    "Her hands are shaking. So are mine."
    "We sit there until Mr. Hale comes by to lock up and pretends very hard not to notice anything."

    $ kara_saved = True
    $ partner = None
    stop music fadeout 3.0
    return

########################################################################
## YURI
########################################################################
label ch1_route_yuri:
    $ yuri_score = 0
    play music t10 fadeout 2.0
    "I put my bag down."

    show yuri 1g zorder 2 at t11
    y "That poem. Number four."
    mc "I know."
    y 1v "You... you knew it was mine."
    mc "You still dot your i's with tiny circles."
    y 3u "Ah. I suppose I'm not very good at anonymity."

    "She takes the pink envelope out of her book."
    y 1h "I wrote this on Sunday. On Monday I stood in front of your locker holding it until the first bell rang. And then I walked away."
    y 1w "That's why we ended, isn't it? I didn't say anything. I just got quieter and waited for you to notice."
    mc "I did notice. I thought it meant you were done with me. So I got quiet too."
    y 1f "But that's exactly what I thought {i}you{/i} were doing."
    y 1o "We're both very stupid."

    y 1g "Everyone's talking about your letter. The one Monika brought."
    y 1v "It wasn't from me. I wish I'd been that brave."

    menu:
        "The letter in my jacket feels heavy."

        "\"I know it's not from you. I'm still here.\"":
            $ yuri_score += 1
            mc "I know it isn't from you."
            mc "I stayed anyway. I stayed because you asked."
            y 1e "..."
            y 1u "Oh."

        "\"Can we not talk about the letter?\"":
            mc "Can we just... not talk about the letter?"
            y 1h "..."
            y 3v "Of course. We're very good at not talking about things."
            "It comes out sharper than she means it. I can tell, because she looks like she wants to take it back."
            "She doesn't. Neither of us says anything for a long time."

    y 1u "Will you take it? My letter? You don't have to answer. I just want one thing to finally be said out loud. Even if it's on paper."

    menu:
        "She holds out the envelope."

        "\"I don't need to read it. I want to know how the story ends too.\"":
            $ yuri_score += 1
            mc "I don't need to read it."
            y 1g "Oh..."
            mc "Yuri. I'd like to know how the story ends too."

        "\"Read it to me. Out loud.\"":
            $ yuri_score += 1
            mc "Read it to me."
            y 3p "O-out loud? Now?"
            mc "One thing said out loud. You said."
            y 3n "..."
            "She opens it with shaking hands. She reads it so quietly I have to lean in."
            "It's about the clubroom, and October, and the way the light comes in at four o'clock. It's about missing someone who's still in the same room."
            "Her voice breaks on the last line. She keeps going anyway."

        "\"I can't do this right now.\"":
            mc "I'm sorry. I can't do this right now."
            y 1w "..."
            y 1h "I see."

    if yuri_score >= 2:
        show yuri 1v zorder 3 at f11
        y "R-really?"
        mc "Really."
        "She steps closer. She's shaking a little. So am I."
        "The last time we kissed, in October, we were so nervous we bumped noses."
        "This time we don't."
        "It's short and soft, and when we pull apart, she's crying, but she's smiling too."
        y 1c "I missed you. I missed you so much."
        y 1d "Are we..."
        mc "If you want to be."
        y 3s "I want to be."
        $ partner = "yuri"
        "We stand by the window until the sun's almost down."
        "I tell myself I'll talk to Kara tomorrow. I'll be honest and kind, and she'll understand."
        "I don't go to the science lab."
        stop music fadeout 3.0
    elif yuri_score == 1:
        show yuri 1h zorder 2 at t11
        y "I... I think I need it to be slower this time. Is that alright?"
        y 1u "Not no. Just... not today."
        mc "That's alright."
        y 3s "Ask me again sometime. When it's not Valentine's Day, and everyone isn't watching."
        "She tucks the envelope back into her book. She smiles at me on her way out. It's small, but it's real."
        stop music fadeout 3.0
        call ch1_too_late_choice from _call_ch1_too_late_choice_yuri
    else:
        show yuri 1w zorder 2 at t11
        y "I'm sorry. I shouldn't have asked you to stay."
        "She puts the envelope back in her book, picks up her bag, and walks out."
        "The door closes very softly. Yuri always closes doors softly."
        "I sit in the empty clubroom for a long time."
        stop music fadeout 3.0
        call ch1_too_late_choice from _call_ch1_too_late_choice_yuri2

    call ch1_walk_natsuki from _call_ch1_walk_natsuki_yuri
    return

########################################################################
## MONIKA - instant rejection
########################################################################
label ch1_route_monika:
    show yuri 1g zorder 2 at t11
    mc "Sorry, Yuri. One second."
    y 1h "...Oh. Of course."
    hide yuri
    with dissolve

    show monika 1a zorder 2 at t11
    mc "Monika. The letter. Was it... was it from you?"
    m 1c "..."
    m 1d "No."
    mc "Because if it was, I-"
    m 1e "[player]. No. It wasn't me, and if you're asking because you're hoping it was..."
    m 1f "It's still no. I'm sorry. I don't feel that way about you."
    mc "...Right. Okay. Yeah."
    m 1g "I'm not trying to be mean. I'd just rather be clear than kind and confusing."
    m 1a "Somebody wrote you that letter. Somebody who isn't me. They're probably waiting somewhere right now."
    m 1m "Go find out who."
    hide monika
    with dissolve

    "Yuri is gone when I turn around. I didn't hear her leave."
    "I go out to the front steps and sit down, because my legs don't want to go anywhere."
    "My face is so hot I could cook an egg on it."
    "I sit there until the streetlights flicker on."
    call ch1_too_late_choice from _call_ch1_too_late_choice_monika
    call ch1_walk_natsuki from _call_ch1_walk_natsuki_monika
    return

########################################################################
## NATSUKI - the walk home
########################################################################
label ch1_route_natsuki:
    $ natsuki_score = 0
    show yuri 1g zorder 2 at t11
    mc "Sorry, Yuri. Natsuki's waiting for me."
    y 1h "Oh... yes. Of course. Thursdays."
    hide yuri
    with dissolve

    scene bg natsuki_house_dusk
    with wipeleft_scene
    play music t8

    "Natsuki is at the gate. She says she wasn't waiting for me. She was waiting for \"the weather.\""
    "We always walk home together on Thursdays. Her house is on the way to mine, sort of, if you take the long way. I always take the long way."

    show natsuki 1a zorder 2 at t11
    n "Huh. You actually came."
    n 1g "Shouldn't you be off finding your mystery girl? Following your little love letter?"

    menu:
        "Why am I here?"

        "\"I'd rather walk with you.\"":
            $ natsuki_score += 1
            mc "I'd rather walk with you."
            n 1o "..."
            n 1v "Wh- that's- you can't just SAY stuff like that!"
            mc "Why not?"
            n 1s "Because! It's Valentine's Day! It sounds weird!"
            "She walks faster. Her ears are bright red."

        "\"Was it you? The letter?\"":
            mc "Was it you? The letter?"
            n 1k "..."
            n 1g "No, dummy. It wasn't me."
            n 2c "Not everything is about your stupid letter."
            "She walks faster. She doesn't look at me for two blocks."

    "We're at her gate."
    "She stands there with her hand on it for a second, not opening it."
    "The little pink package is in her hand. I don't think she even realizes she took it out."

    show natsuki 1i zorder 2 at t11
    n "Why'd you really come, [player]? Tell me the truth."

    menu:
        "Tell her the truth."

        "\"Because I think it's always been you.\"":
            $ natsuki_score += 1
            mc "Because I think it's always been you."
            mc "Since third grade. Since you punched a kid for stepping on my lunch."
            n 1p "..."
            n 1u "That's- you don't-"

        "\"Because it's Thursday. We always walk on Thursdays.\"":
            mc "Because it's Thursday. We always walk home on Thursdays."
            n 1u "..."
            n 1j "Yeah. Yeah, we do."
            "Something in her face closes, very gently, like a door."

    if natsuki_score >= 2:
        n 1w "I've liked you since sixth grade, you idiot."
        n 1v "Every sandwich. I made too much every single day. On {i}purpose.{/i}"
        mc "I know. I figured that out in sixth grade."
        n 1o "And you didn't SAY anything?!"
        mc "I'm saying it now."
        "She shoves the package at my chest. Inside is a keychain: a tiny felt cupcake, hand-stitched, with a little extra frosting heart on the side."
        n 1s "Took me three weeks. I stabbed myself like forty times. Don't lose it."
        "I clip it onto my backpack. Before I can say anything, she goes up on her toes and kisses my cheek, really fast, like she's stealing something."
        n 4x "GOOD NIGHT!"
        "She's inside with the door slammed before I can blink."
        "A second later, an upstairs curtain moves."
        $ partner = "natsuki"
        $ have_natsuki_charm = True
    elif natsuki_score == 1 or asked_natsuki_gift:
        n 1y "Here. The festive math thing. It's a {i}friend{/i} thing."
        "A keychain: a tiny felt cupcake with a little extra frosting heart on the side."
        n 1n "Ask me the other question when you actually mean it, dummy."
        "I clip it onto my backpack. She watches me do it like she's memorizing it."
        $ have_natsuki_charm = True
    else:
        n 1n "Go home, [player]."
        "She puts the package back in her bag and goes inside."
        "She doesn't wave."

    stop music fadeout 3.0
    return

########################################################################
## SAYORI - the walk home
########################################################################
label ch1_route_sayori:
    show yuri 1g zorder 2 at t11
    mc "Sorry, Yuri. I have to catch Sayori."
    y 1h "...Of course."
    hide yuri
    with dissolve

    scene bg residential_day
    with wipeleft_scene
    play music t2

    "I catch up with her two blocks from school. She's walking slowly, with her hands in her sleeves."
    show sayori 1g zorder 2 at t11
    s "[player]? What are you doing here? Shouldn't you be off with your secret admirer?"

    menu:
        "Why did I come?"

        "\"Was the letter from you?\"":
            mc "Was it you? The letter?"
            s 1t "Ehehe..."
            s 1u "No. It wasn't me. Sorry."
            s 1g "Is that why you came? Because you thought it might be me?"
            mc "...Partly."
            s 1t "That's okay."

        "\"You left without saying goodbye. You never do that.\"":
            mc "You left without saying goodbye. You never do that."
            s 1u "Oh. I didn't think anyone would notice."
            mc "I noticed."
            s 1t "..."

    "We walk. She's quiet for a whole block. Sayori is never quiet for a whole block."
    show sayori 1u zorder 2 at t11
    s "Hey, [player]? Can I tell you something? And you won't be weird about it?"
    mc "I promise."
    s 1t "Rule number one. Nobody's allowed to be sad."
    s 1u "I didn't make it up for you. I made it up for me. Because some mornings I can't get out of bed. Not because I'm lazy. I just... can't."
    s 1g "There's like a raincloud. All the time. Everyone thinks I'm the happy one, so I have to be the happy one, or else what am I?"
    s 1t "I'm so tired, [player]."

    menu:
        "What do I say?"

        "\"Then I'll make you happy. Every day. That's my job now.\"":
            mc "Then I'll make you happy. I'll come get you every morning. Every day. That's my job now."
            s 1u "..."
            s 1t "Ehehe. That's really sweet."
            s 1g "But you shouldn't have to. It's not your job to fix me."
            mc "I want to."
            s 1u "...Okay."
            "She smiles."
            "I don't notice that it doesn't reach her eyes."

        "\"Have you told anyone? Your mom? Ms. Reyes? I'll go with you.\"":
            $ sayori_got_help = True
            mc "Have you told anyone? Your mom? Ms. Reyes, the counselor?"
            s 1g "No... I don't want to bother anyone with it."
            mc "You're not a bother. This is what she's there for. I can't fix it, Sayori. I wish I could. But somebody who knows how can help."
            mc "I'll go with you tomorrow morning. I'll sit outside the door the whole time."
            s 1u "..."
            s 1t "...You'd do that?"
            mc "I'd do that. And you should tell your mom tonight."
            s 1y "Okay. Okay. I'll try."
            "She wipes her eyes on her sleeve. It's not a fix. But it's something."

    show sayori 1t zorder 2 at t11
    s "Can I ask you something else? A scary one?"
    s 1u "Do you like me? Like... like-like?"

    menu:
        "Do I?"

        "\"Yes.\"":
            mc "Yes."
            s 1v "..."
            "She hugs me. Hard. Right in the middle of the sidewalk. She's crying and laughing at the same time."
            if sayori_got_help:
                $ partner = "sayori"

        "\"You're my best friend. I don't know yet.\"":
            mc "You're my best friend. I don't know yet. I'm sorry."
            s 1y "Don't be sorry! That's an honest answer. I like honest."
            s 1t "Ehehe... best friends is still pretty good."

    if not sayori_got_help:
        $ sayori_dead = True

    "We get to our street. Her house, then mine."
    s 4r "Thanks for walking me, [player]. See you in the morning!"
    "She waves until she's inside."

    stop music fadeout 3.0
    return

########################################################################
## Walking Natsuki home (Yuri and Monika routes)
########################################################################
label ch1_walk_natsuki:
    scene bg natsuki_house_dusk
    with wipeleft_scene
    play music t8

    "Natsuki was waiting at the gate. She said she wasn't waiting for me. She was waiting for \"the weather.\""
    "We always walk home together on Thursdays. I always take the long way."

    if partner == "yuri":
        show natsuki 1a zorder 2 at t11
        n "You're doing a weird face. You've been smiling at nothing for six blocks."
        mc "Yuri and I got back together."
        n 1k "..."
        n 1l "Oh! Wow! That's- that's great! Seriously!"
        n 1d "I knew that poem was hers. Number four. She does that thing with the circles."
        n 1u "So the love letter wasn't from her?"
        mc "No. I'm going to talk to the person who sent it tomorrow."
        n 1n "Good. Somebody put their heart in an envelope, dummy. You don't just leave it there."
    else:
        show natsuki 1g zorder 2 at t11
        n "Whoa. You look like somebody ran over your dog."
        mc "Long day."
        n 1u "...Did the letter thing go bad?"
        mc "I don't really want to talk about it."
        n 1n "Okay."
        "She doesn't push. She just walks a little closer than usual."

    "We're at her gate."
    n 1y "Happy Valentine's Day, [player]."

    if asked_natsuki_gift:
        "She pulls the little pink package out of her bag and shoves it at my chest without looking at me."
        n 1s "Here. The festive math thing. It's a {i}friend{/i} thing!"
        "A keychain: a tiny felt cupcake, hand-stitched, with a little extra frosting heart on the side."
        n 1w "Took me three weeks. I stabbed myself like forty times. Don't lose it, dummy."
        "I clip it onto my backpack right there. She watches me do it like she's memorizing it."
        $ have_natsuki_charm = True

    hide natsuki
    with dissolve
    "When I glance back at the corner, Natsuki's still standing at her gate, watching me go."
    if have_natsuki_charm:
        "After a second, she waves. Small. Like she isn't sure she's allowed to."
    else:
        "She doesn't wave."

    stop music fadeout 3.0
    return
