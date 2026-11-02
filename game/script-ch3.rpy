## Chapter 3 - Monday, February 18th
##
## Kara is back in the science lab as if nothing happened.
## Signs of a cover-up: attendance changed, the notebook page gone,
## the council drop box and logbook page taken, men in gray suits with government badges.

label ch3_main:
    call day_card("Monday, February 18th") from _call_day_card_ch3
    call ch3_morning from _call_ch3_morning
    call ch3_first_period from _call_ch3_first_period
    call ch3_hallway from _call_ch3_hallway
    return

########################################################################
## Morning - picking up Natsuki
########################################################################
label ch3_morning:
    if sayori_dead:
        jump ch3_morning_grief

    scene bg natsuki_house_day
    with dissolve_scene_full
    play music t2

    if sayori_got_help:
        "Sayori texted at 7:02 to say her mom's driving her today, because of the doctor. Then: {i}medium day!!{/i} Then a frog emoji."
    else:
        "Sayori texted at 7:02 to say she was running late and to go without her. Then at 7:04: a single crying emoji."
    "So I swing by Natsuki's."

    if partner == "yuri":
        "The weekend was good. Really good. Bartholomew turned out to be a very large orange cat who sat on Yuri's lap the entire time and glared at me like I was a threat to the throne."
        "Yuri held my hand under the table. She cried a little when I gave her a book. In a good way."
    elif partner == "natsuki":
        "The weekend was good. Really good. Natsuki beat me at every game in the arcade and then won me a stuffed shark from the claw machine and said it was \"a pity shark.\""
        "When I walked her home she held my hand for the last block. Neither of us said anything about it."
    elif partner == "sayori":
        "The weekend was good. Sayori's mom made pancakes shaped like hearts and then cried into the batter, a little, and hugged us both."
        "Saturday was a medium day. Sunday was a good one."

    show natsuki 1k zorder 2 at t11
    if partner == "natsuki":
        n 1o "You're early. Why are you early. Did you think about this? Is this a boyfriend thing?"
        mc "It's a Monday thing."
        n 1s "...Okay. Good. Mondays are allowed."
    else:
        n "Why are you here? You don't walk me on Mondays."
        mc "Sayori's not coming."
        n 2g "So I'm the backup."
        mc "You're the upgrade."
        n 2s "...Okay, nice save."

    show natsuki 1a zorder 2 at t11
    n 1c "I finished your lighthouse book."
    n 1i "The ending, when she finally sees the sunrise and it's not what she thought it would be..."
    n 1j "I didn't cry. For the record. ...I cried a lot."

    if have_natsuki_charm:
        "Halfway there, I catch her looking at the little felt cupcake clipped to my backpack."
        n 1y "...You kept it on."
        mc "Of course I kept it on."
        n 4x "W-whatever! Good! It'd be a waste of forty stab wounds otherwise!"
        "She walks a little closer to me after that."

    "Monday. First period."
    "I've got Kara's letter in my jacket again. I'm going to tell her thank you, and I'm going to tell her the truth."

    stop music fadeout 2.0
    return

label ch3_morning_grief:
    scene bg residential_day
    with dissolve_scene_full
    play music t9

    "I walk past Sayori's house without looking at it."
    "I've been practicing that all weekend. Walking past without looking."
    "Somebody's left flowers on her porch. A lot of flowers. And a stuffed frog."
    "I look anyway."

    show natsuki 1n zorder 2 at t11
    "Natsuki is waiting at the corner. She's never waited at the corner before. It's the wrong direction from her house."
    n "My mom drove me. I told her I'm walking with you. Every day, for a while. Don't argue."
    mc "I wasn't going to."
    n 1u "...Did you sleep?"
    mc "Some."
    n 1n "Liar."
    if have_natsuki_charm:
        "She looks at the little felt cupcake on my backpack. She doesn't say anything about it. She just hooks her finger through my backpack strap and holds on."
    "The funeral is Thursday. My mom says I don't have to go to school today."
    "I'm going anyway. I don't know what else to do with myself."
    "Kara's letter is still in my jacket. I found it again this morning. I'm going to tell her the truth. It feels like the only thing left I can still do right."

    stop music fadeout 2.0
    return

########################################################################
## 1st period - Kara is back
########################################################################
label ch3_first_period:
    scene bg science_lab
    with wipeleft_scene
    play music t3

    "I take the stairs two at a time."
    "When I open the door, the lab is bright and loud and normal. People spinning on stools. Mr. Hale fighting with the projector."
    "And at our bench by the window..."

    show kara 1a zorder 2 at t11
    "Kara."
    "Pale hair in her eyes. Hands folded on the bench. Sitting perfectly straight."

    k 1a "Good morning, [player]."
    mc "Hey! Hey, you're back. Are you feeling better?"
    k 1b "Better?"
    mc "You were out Friday. Mr. Hale said there was a cold going around."
    k 1a "I wasn't out on Friday."
    mc "..."
    mc "Yeah, you were. I did the speed of sound lab by myself."
    k 1e "We did that lab together. You held the tuning fork. I wrote down the numbers."
    k 1a "Don't you remember?"

    "She says it so simply. Like she's reminding me what day it is."

    hale "Okay! Attendance! Let's see who survived the weekend..."
    hale "Kara?"
    k 1d "Here."
    hale "Perfect attendance this semester, Kara. Keep it up."

    "Perfect attendance."
    "I look at Mr. Hale. He's already moved on to the next name. He doesn't look at me. He doesn't look at her either."
    "His hand is shaking a little on the clipboard."
    "Or maybe I'm imagining that."

    show kara 1a zorder 2 at t11
    "I pull open our shared drawer. Her notebook's there. Blue flower on the cover."
    mc "Can I see your notes from Thursday? I want to check something."
    k 1a "Of course."

    "I flip through it. Density columns, Thursday. Her neat handwriting. Honey, soap, water."
    "The speed of sound lab, dated Friday. Her neat handwriting. Every measurement filled in. The numbers are the same as mine. Exactly the same as mine."
    "And between them..."
    "There's a page missing. Torn out so cleanly I almost didn't notice. Just a thin, ragged strip of paper left along the spiral."

    mc "Kara, there's a page missing."
    k 1b "Is there?"
    k 1a "I must have torn it out by accident. I'm very clumsy. You know that."

    if left_note_kara:
        "My note is still tucked inside the front cover, where I left it on Friday."
        "Somebody's unfolded it. Read it. Folded it back up along the same crease."
        "Under my handwriting, in small, neat blue ink, someone has written a reply."
        "{i}It's okay. Really. - K{/i}"
        "And under that, a date."
        "{i}Saturday.{/i}"
        "The school was locked all weekend."
        mc "Kara... when did you write this?"
        k 1a "Write what?"
        "When I look down again, she's turned to a fresh page and started copying the worksheet title. She doesn't look at the note. Not once."
        $ clues += 1

    "She smiles."
    "It's her smile. It's exactly her smile."
    "I take a breath. I came here to do this. I'm going to do it."

    mc "Kara... about the letter."
    if went_lab_late:
        mc "The letter Monika gave me. I know it was from you. I came to find you on Thursday. I was four minutes late. I'm so sorry, I should have come first, I..."
    else:
        mc "The letter Monika gave me. On Valentine's Day. I know it was from you. And I wanted to say thank you, and that I'm really sorry, because I should have come to find you, and I didn't, and..."

    show kara 1b zorder 2 at t11
    "She's just looking at me."
    "She hasn't blinked."

    k 1a "What letter?"
    mc "..."
    k 1a "I didn't send you a letter, [player]."
    k 1a "I've never sent anyone a letter."

    "The lights hum."

    k 1d "We should get started. Mr. Hale's handing out the worksheets."
    k 1a "Slow is smooth, right?"

    "I never told anyone that I said that to her."
    "Thursday was the only time I said it."

    stop music fadeout 2.0
    return

########################################################################
## 2nd period - The hallway
########################################################################
label ch3_hallway:
    scene bg corridor
    with wipeleft_scene
    play music t7

    if sayori_dead:
        "The morning announcements this morning started with a moment of silence."
        "The principal said Sayori's name. He said she was kind, and bright, and loved. He said counselors would be in the library all week."
        "The whole school was quiet for one minute."
        "He didn't say anything about anyone else."
    "Between first and second period, the first-floor hallway is wrong."
    "The student council drop box is gone. The gray metal one that's been bolted next to the council door since before any of us were born."
    "There are four clean screw holes in the wall where it used to be."
    "And there are two men standing outside the principal's door."
    "Gray suits. Identical gray suits. Visitor lanyards around their necks with a seal I half-recognize from the front of government buildings and tax forms."
    "They're not talking. They're just watching the hallway. Watching everyone who walks by."
    "One of them looks at me. Then down at a folder in his hand. Then back at me."

    suit "Morning, son. Get along to class."

    "I get along to class."
    "Monika catches me at the corner."

    show monika 1f zorder 2 at t11
    m "[player]. Hi."
    mc "Monika, who are those guys?"
    m 1g "The office says it's a routine district audit."
    m 1d "They were in the student council office before school. They took the drop box. Off the wall. With a drill."
    m 1f "And my logbook. The one where I write down everything that comes in."
    m 1g "The principal was standing right there. It didn't seem like asking 'why' was an option."
    mc "Monika... the letter you gave me on Thursday. Do you remember it?"
    m 1c "Of course I remember. Monday morning, seven-fifteen. Plain white envelope, sticky note, your name on it. A little bag of Hershey's Kisses taped to the front."
    m 1d "I wrote it down. It was the only thing in the box that whole week."
    mc "So there's a record. In your logbook."

    "She's quiet for a second."
    "Monika is never quiet for a second."

    m 1h "There was."
    m 1i "They gave the logbook back this morning, before first period. They said they'd finished with it."
    m 1h "The page for last week is gone, [player]. Not torn out. Just... gone. Like it was never in the book."
    m 1i "As of this morning..."
    m 1h "There's no record that anyone left you anything."

    show monika 1g zorder 2 at t11
    m "Be careful, [player]. Okay?"
    m 1a "I'm not saying that as the council secretary. Just as your friend."
    if sayori_dead:
        m 1q "And [player]... about Sayori."
        m 1r "She sat on my desk every lunch and ate my crackers. I keep leaving them out."
        m 1f "It isn't your fault. Whatever you said to her on Thursday. Please hear that from someone."
        mc "..."
        m 1g "Ms. Reyes is in the library. Go today. Promise me."

    hide monika
    with dissolve

    "She walks away."

    if told_cassian:
        "I'm still standing at the corner when someone touches my shoulder."
        show cassian 1d zorder 2 at t11
        cas "[player]."
        "Cassian. He must have come all the way down from the music room to find me before choir. He looks like he hasn't slept."
        cas 1e "The letter you told me about. On Thursday. Was it from Kara? Science class Kara?"
        mc "...How do you know that?"
        cas 1d "I didn't. I guessed. Listen."
        cas 1f "I drive home from the gym on Friday nights. I take Willow Street."
        cas 1g "There were two ambulances outside a house on Willow on Friday night. And a police car. Lights on, no sirens."
        cas 1e "A neighbor was standing on her lawn crying. She said it was a girl who goes here. A freshman."
        cas 1d "I looked it up this weekend. Local news. Nothing. School email. Nothing. I asked Mr. Dunn this morning. He told me to get to class and wouldn't look at me."
        mc "Kara's in first period. I just saw her. She's fine."
        cas 1n "..."
        cas 1a "Then I hope I'm wrong."
        cas 1c "I don't think I'm wrong."
        hide cassian
        with dissolve
        $ clues += 1

    if invited_zach:
        "Zach catches up to me at the stairs, breathless."
        show zach 1c26 zorder 2 at t11
        z "Dude. Weird question. Your weekend. Was it weird?"
        mc "...Why?"
        z 1c5 "My mom works at the district office. Like, the school district. Paperwork stuff. Super boring."
        z 1c26 "She got called in on Saturday. Everybody did. Like an emergency meeting. She came home at like midnight and didn't say anything."
        z 1c27 "She just hugged me. For like a full minute. My mom doesn't hug. She shakes hands with the {i}dog.{/i}"
        z 1c26 "And then those guys in the suits are here today and... I don't know. I'm being dumb. Forget it."
        mc "You're not being dumb."
        z 1c5 "...Yeah?"
        mc "Yeah."
        hide zach
        with dissolve
        $ clues += 1

    "At the end of the hallway, by the place where the drop box used to be, Oni is standing with his hands in his pockets."
    show oni 2g zorder 2 at t11
    "He's facing me. I think. With his hair over his eyes, I can never be sure."
    "He waits until I'm close. Then he says, very quietly, so the men in the suits can't hear:"
    oni 2h "She waited for you, you know."
    oni 2g "In the lab. Until five-forty."
    mc "...What?"
    oni 2a "Happy Valentine's Day, [player]."
    hide oni
    with dissolve
    "And he walks away, and by the time I can move again, the bell's already rung."

    "In my jacket pocket, my hand finds the envelope."
    "It's still there. Plain white. My name on the front in small, careful handwriting."
    "It's still there."

    if clues >= 2:
        "Something happened to Kara on Friday. I'm sure of it now."
        "And whoever is sitting at our bench in first period, smiling her smile, everyone in this building is being very careful not to ask who she is."
    elif clues == 1:
        "Something is wrong. I don't know what yet."
        "But the girl in first period didn't write me that letter. And the girl who did write it..."
        "I don't know where she is."
    else:
        "That's the only thing I'm sure of."

    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    pause 1.5
    show expression Text("To be continued...", size=36, color="#ffffff", outlines=[]) as tbc at truecenter
    with Dissolve(1.5)
    pause 3.0
    hide tbc
    with Dissolve(1.0)
    return
