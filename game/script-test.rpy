## Test chapter: a short scene with one choice.
## Its job is to prove the pipeline works (backgrounds, music,
## character sprites, dialogue, a menu, and a branch). Replace it once the
## real story starts.

# Remembers which branch the player picked, so later scenes can react.
default test_choice = None

label test_chapter:
    stop music fadeout 2.0

    scene bg club_day
    with dissolve_scene_full
    play music t2

    "The clubroom is quiet today. Just one person here so far."

    show sayori 1a zorder 2 at t11
    s "Oh! You made it!"
    s 1b "I was starting to think everyone forgot about the meeting."
    mc "I said I'd come, didn't I?"
    s 4r "You did! But you also said you'd walk me to school, and..."
    mc "...Okay, fair."

    s 1a "Anyway! I need help deciding something important."
    s 1b "Should I bring cookies or cupcakes to the next meeting?"

    menu:
        s "Which one?"

        "Cookies.":
            $ test_choice = "cookies"
            jump test_chapter_cookies

        "Cupcakes.":
            $ test_choice = "cupcakes"
            jump test_chapter_cupcakes

        "...Donuts?":
            $ test_choice = "donuts"
            jump test_chapter_donuts

label test_chapter_cookies:
    s 4r "Cookies it is! Easy to share, hard to drop."
    mc "That second part sounds like experience talking."
    s 1l "...Maybe."
    jump test_chapter_end

label test_chapter_cupcakes:
    s 4b "Cupcakes! Ooh, with frosting!"
    mc "Just don't let Natsuki find out you bought them from a store."
    s 1k "I'll keep it a secret. Ehehe~"
    jump test_chapter_end

label test_chapter_donuts:
    s 4h "Donuts?! That wasn't even one of the options!"
    mc "Who says it has to be one of the options?"
    s 4r "You're right! Rules are just suggestions when donuts are involved!"
    s 1k "I'm getting the ones with sprinkles. Lots of sprinkles."
    jump test_chapter_end

label test_chapter_end:
    show sayori 1a zorder 2 at t11
    s "Thanks for helping! See you tomorrow?"
    mc "See you tomorrow."

    hide sayori
    with dissolve
    "(If you can read this, the mod is working.)"
    return
