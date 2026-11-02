## Prologue - Twelve weeks earlier (November)
##
## Short on purpose: how [player] and Kara became lab partners.
## Kara: very smart, down to earth, quiet. Very strict father (never seen).
## She can't give out her number because her dad won't allow it.
## Kara is only ever seen in the science lab.

label prologue_main:
    call day_card("Twelve weeks earlier") from _call_day_card_prologue

    scene bg science_lab
    with dissolve_scene_full
    play music t3

    hale "[player], your lab partner moved to Ohio. Kara, you're not flying solo anymore."

    "Kara. The girl at the bench by the window. Top score on every test. I'd never heard her voice."

    show kara 1c zorder 2 at t11
    mc "Hi. I'm [player]."
    k 1b "I know. You sit three rows behind me."

    "Ten minutes later her sleeve catches a beaker. I catch it two inches above the floor."
    "She flinches, like she's waiting for me to laugh. Like people usually laugh."
    mc "Good thing it's not the acid."
    k 1e "We don't have any acid."
    mc "Then we're doing great."
    k 1p "...Ahaha. Okay. Thank you."

    show kara 1d zorder 2 at t11
    "It turns out Kara talks a lot. Just not to most people."
    k "The lights hum, you know. Sixty hertz. It's almost a B-flat."
    k 1b "I read a lot. I'm not allowed to do much else. My dad's... strict."

    "In December we get a partner project. I ask for her number."
    show kara 1h zorder 2 at t11
    k 1u "I can't. He checks my phone every night. Especially for boys' numbers."
    k 1a "But he drops me off at six-fifty. Nobody's here that early. You could come too. If you want."

    "So I start coming early."
    "On the last day of the project, she draws a tiny blue flower on the corner of my lab label."
    k 1k "For luck."
    "After that, there's a flower on every label. Every lab. Every Thursday."
    "I never think about what it means."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.0
    return
