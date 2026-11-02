## Ending - "For Luck"
##
## [player] went to the lab on Thursday and found Kara before 5:40.
## Nothing happens to her. There's no Friday absence, no Monday, no gray suits.
## Kara is still only ever seen in the science lab.

label ending_kara:
    call day_card("Twelve weeks later") from _call_day_card_kara_end

    scene bg science_lab
    with dissolve_scene_full
    play music t5

    "May."
    "6:50 in the morning. The building's open, but there's nobody here."
    "Except us."

    show kara 1a zorder 2 at t11
    k "You're late."
    mc "It's six-fifty-one."
    k 1q "Exactly. Late."

    "Her dad still drops her off at six-fifty every day. I still meet her here every day."
    "We still don't text. I still don't have her number."

    if kara_counselor:
        "But on Friday, February 15th, at seven in the morning, I walked her to Ms. Reyes' office. I sat outside the door for forty-five minutes."
        "When she came out, her eyes were red, and she said, \"I told her everything.\" Then she said, \"I'm so hungry,\" and we split my granola bar."
        "Things at home aren't fixed. Some people came to her house. There were meetings. There are still meetings."
        k 1d "Ms. Reyes says I'm allowed to lock my door now. It's a rule. A real one. Somebody wrote it down."
        k 1k "I didn't know I was allowed to want that."
    else:
        "It took her six weeks to walk into Ms. Reyes' office. I sat outside the door for forty-five minutes."
        "When she came out, she said, \"I told her almost everything.\" Then, a week later, she went back and told her the rest."
        "Things at home aren't fixed. But she's not carrying it alone."
        k 1d "I still get tired. Ms. Reyes says that's allowed. You just have to tell someone when it's the bad kind."
        k 1k "So I tell you. And her. It's a lot of telling. I'm getting better at it."

    "We're the only two people in the building. The lights hum."
    k 1j "B-flat."
    mc "Almost."

    "Kara writes out today's labels. HYDROGEN PEROXIDE. YEAST. DISH SOAP."
    "A tiny blue flower on every one."
    "And on mine, next to the flower, in very small letters: {i}- Not Anonymous.{/i}"

    mc "..."
    k 1p "Don't make it a whole thing."
    mc "I'm absolutely making it a whole thing."
    k 1w "[player]!"

    "Last week, Monika stopped me in the hallway and asked whether the letter had worked out."
    "I told her yes."
    "She said, \"Good. I didn't want to have delivered a sad one.\" Then she took a Hershey's Kiss out of her blazer pocket, handed it to me, and walked off before I could ask why she had it."

    show kara 1a zorder 2 at t11
    k "Hey, [player]... can I ask you something?"
    mc "Sure."
    k 1u "Do you... um."
    k 1k "..."
    "For a second I think she's going to say \"never mind.\" She always says \"never mind.\""
    "She doesn't."
    k 1h "I love you."
    k 1t "...Do you love me too?"
    "The lights hum. Somewhere downstairs, a door opens. The building's waking up."
    mc "Yeah."
    mc "I love you too, Kara."
    k 1w "..."
    k 1j "Okay. Good."
    k 1q "I was really hoping you'd say that. I didn't have a plan for the other answer."
    mc "You always have a plan."
    k 1k "Not for you. You were never part of the plan."
    "She draws one more tiny blue flower, right on the back of my hand, the way she did on Valentine's Day."
    k 1a "For luck."
    mc "I don't think we need it anymore."
    k 1j "I know. I just like drawing them."

    stop music fadeout 4.0
    scene black
    with dissolve_scene_full
    pause 1.5
    show expression Text("Ending: For Luck", size=36, color="#ffffff", outlines=[]) as endtitle at truecenter
    with Dissolve(1.5)
    pause 3.0
    hide endtitle
    with Dissolve(1.0)

    show expression Text("If things feel too heavy to carry, tell someone.\nIn the US, call or text 988. Elsewhere: findahelpline.com", size=22, color="#ffffff", outlines=[], text_align=0.5) as helpline at truecenter
    with Dissolve(1.0)
    pause 4.0
    hide helpline
    with Dissolve(1.0)
    return
