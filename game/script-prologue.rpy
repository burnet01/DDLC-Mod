## Prologue - Twelve weeks earlier (Thursday, November 22nd)
##
## How [player] and Kara became lab partners.
## Kara: very smart, down to earth, quiet. Very strict father (never seen).
## She can't give out her number because her dad won't allow it.
## Kara is only ever seen in the science lab.

label prologue_main:
    call day_card("Twelve weeks earlier") from _call_day_card_prologue
    call prologue_partners from _call_prologue_partners
    call prologue_weeks from _call_prologue_weeks
    call prologue_number from _call_prologue_number
    return

########################################################################
## The new lab partner
########################################################################
label prologue_partners:
    scene bg science_lab
    with dissolve_scene_full
    play music t3

    "November."
    "My lab partner for the first three months of high school was a guy named Brent, who mostly used our lab time to see how many pencils he could balance on his upper lip."
    "Then Brent's family moved to Ohio. I hope he's happy there. I hope the pencils are happy too."

    hale "Okay, people. Brent has left us for the Midwest, so we've got an odd number. [player], you're moving."
    hale "Kara, you've been flying solo all semester. You're getting a partner. Try not to scare him with your test scores."

    "Kara."
    "The girl at the bench by the window."
    "I've been in this class with her for three months, and I don't think I've ever heard her voice. She sits alone. She gets the top score on every test, and Mr. Hale reads it out loud every time, and she just looks at her desk like she wishes he wouldn't."
    "She doesn't look up when I sit down."

    show kara 1c zorder 2 at t11
    mc "Hi. I'm [player]."
    k 1b "I know. You sit three rows behind me."
    k 1g "...Hi."

    "That's it. That's the whole conversation."
    "She goes back to her notebook. Her handwriting is so neat it looks typed."

    hale "Today: acids and bases. Litmus paper, vinegar, baking soda. Nobody make a volcano, I'm begging you, it's not that kind of class."

    "I read the instructions. Then I read them again. Then I start working out the dilution ratio in the margin of my worksheet, and I get it wrong, and I don't know I got it wrong."
    "A pencil reaches over and taps my margin. Once. Very lightly."

    k 1t "You carried the two."
    mc "...I did?"
    k 1u "Sorry. That's- I wasn't trying to- it's fine. Everybody does it. I do it all the time."
    mc "You have a hundred and four percent in this class."
    k 1h "The four percent was extra credit. It doesn't count."
    k 1v "...It counts a little."

    "That's the first time I hear her almost laugh."

    "Ten minutes later, she reaches for the vinegar and her sleeve catches the beaker next to it."
    "It tips."
    "I catch it about two inches above the floor. I don't even think about it. My hand is just there."

    k 1o "..."
    "She's frozen. Bracing for something. Like she's waiting for me to laugh."
    "Like people usually laugh."
    mc "Good thing it's just vinegar. If it was the hydrochloric acid, we'd both be in trouble."
    k 1e "We... don't have hydrochloric acid."
    mc "Then we're doing great."
    k 1k "..."
    k 1p "Ahaha... okay. Okay. Thank you."
    k 1a "I'm really clumsy. Sorry in advance. For the rest of the semester."
    mc "I'll stretch."

    stop music fadeout 2.0
    return

########################################################################
## The weeks after
########################################################################
label prologue_weeks:
    scene bg science_lab
    with dissolve_scene_half
    play music t5

    "It turns out Kara talks a lot. Just not to most people."
    "It takes about a week to get started, the way old cars take a minute to warm up in the winter."

    show kara 1a zorder 2 at t11
    k "The lights hum, you know."
    mc "The what?"
    k 1d "The fluorescent lights. They hum at sixty hertz, from the alternating current. It's almost a B-flat."
    k 1e "Nobody notices because it's always there. But once you hear it, you can't stop hearing it."
    mc "How do you know all this?"
    k 1b "I read a lot. I'm not allowed to do much else."
    k 1a "My dad's... strict."

    "She says it the way you'd say \"it's cold out.\" Like a fact about the weather. Nothing to complain about. Just a thing that is."

    "Mondays and Thursdays are lab days."
    "Thursdays are the double lab. Ninety minutes."
    "Thursdays become my favorite day of the week. I don't really notice that's happening until it's already happened."

    show kara 1k zorder 2 at t11
    "Kara knows everything. Not in a show-off way. In a \"did you know octopuses have three hearts\" way, at seven-forty in the morning, while we're waiting for Mr. Hale to find the projector remote."
    "She's funny, too. Dry funny. The kind where you don't realize she made a joke until three seconds later."
    k 1f "If Mr. Hale's remote were an element, it would be the most unstable one on the periodic table. Half-life of about four minutes."
    mc "..."
    mc "...Wait, that's good."
    k 1q "I know. I've been saving it."

    "She's never once acted like she's smarter than me. Even though she is. By a lot."
    "When I get something wrong, she doesn't fix it for me. She just taps the margin with her pencil, once, and waits for me to find it myself."

    hale "Okay, whoever's humming. It's actually on pitch, which I respect, but please stop."
    "Everyone looks around."
    "Kara is looking at her notebook. Very, very hard. She's smiling."
    "It takes me until the bell to realize the humming was me."

    stop music fadeout 2.0
    return

########################################################################
## The number
########################################################################
label prologue_number:
    scene bg science_lab
    with dissolve_scene_half
    play music t9

    "In December, Mr. Hale assigns a partner project. A two-week model of the water cycle. With a written report."

    show kara 1a zorder 2 at t11
    mc "We should probably work on this outside of class. Can I get your number? So we can text about it?"

    show kara 1h zorder 2 at t11
    "She goes very still."
    k 1t "I... can't."
    mc "Oh. That's okay, I didn't mean-"
    k 1u "No, it's not- it's not you. I'm not allowed to give out my number."
    k 1h "To anyone. My dad checks my phone. Every night."
    mc "Every night?"
    k 1u "He reads everything. If there's a number he doesn't know, there's... a conversation."
    k 1v "Especially if it's a boy's number."
    k 1t "I'm sorry. I know it's weird."

    "I don't really know what to say."
    "I've never met her dad. I don't think I ever will. But for a second I can picture him anyway: some huge, cold shape standing behind her, all the time, everywhere except here."

    mc "It's not weird. It's fine. We'll just do it in here."
    k 1g "In here?"
    mc "You're always here early anyway. I can come early too."
    k 1e "...You'd come early? For a water cycle project?"
    mc "It's a really important water cycle project."

    show kara 1j zorder 2 at t11
    k "..."
    k 1j "Okay."
    k 1a "My dad drops me off at six-fifty. Every day. The building's open, but there's nobody here. It's the only time that's... mine."
    k 1d "You can share it. If you want."

    "So I start coming in early."
    "Twenty minutes, every morning, before first period. The lights humming. Kara explaining evaporation like it's the plot of a movie. Me building a terrible cardboard cloud."

    "On the last day of the project, she takes my lab label, the one that says {i}[player]{/i} in my messy handwriting, and in the corner she draws something small in blue pen."
    "A tiny flower."
    mc "What's that for?"
    k 1k "For luck."
    k 1a "I put them on mine. I never told anybody."
    k 1b "...You're the first person who's noticed."

    "We get an A on the water cycle."
    "After that she draws the flower on every label. Every lab. Every Thursday."
    "And I never think about what it means."
    "Not once. Not for twelve weeks."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.0
    return
