## Chapter 1 - Thursday, February 14th (Valentine's Day)
##
## Kara is only ever seen in the science lab.
## Periods: 1st science lab (Kara), 2nd choir (all-boys choir, every day; Monika
## walks in and delivers the letter + Hershey's Kisses in front of everyone),
## 3rd-4th (blur), hallway (Natsuki), 5th lunch (free roam), after school club (Yuri).
##
## Monika delivering the letter is a one-off favor, not a school event.
## Someone left it in the student council drop box on Monday morning.

# Choices that change later scenes
default told_cassian = False         # ch1 choir -> Cassian brings a clue on Monday
default asked_natsuki_gift = False   # ch1 hallway -> Natsuki gives you her gift on the walk home
default have_natsuki_charm = False   # ...and you still have it Monday
default left_note_kara = False       # ch2 lab -> something answers it on Monday
default invited_zach = False         # ch2 lunch -> Zach brings a clue on Monday
default clues = 0                    # how much [player] has pieced together by the end of ch3

# Lunch choices (free roam, two visits before the bell)
default ch1_lunch_natsuki = False
default ch1_lunch_yuri = False
default ch1_lunch_council = False
default ch1_lunch_lab = False

# The Valentine's letter
init python:
    note_valentine = Note(
        title = "To [player],",
        text = "\n".join([
            "Okay. I've started this letter like eleven times, so this is the twelfth one and I am NOT starting over again no matter what!!",
            "",
            "I like you.",
            "",
            "Like... LIKE like you. Not just \"oh, he's nice\" (even though you ARE really nice).",
            "",
            "I notice stuff about you. Like how you hum when you're concentrating. You don't even know you're doing it, and it's honestly so cute. And how you always let me hold stuff even when we both know I'm gonna drop it, and you never laugh at me. Not even once.",
            "",
            "You probably don't think about me that much. That's okay! But I think about our mornings a lot. They're my favorite part of the whole week. Thursdays especially. <3",
            "",
            "If you like me back... find me? You'll know where.",
            "",
            "I'm not brave enough to sign this.",
            "",
            "- Anonymous",
        ])
    )

label ch1_main:
    call day_card("Thursday, February 14th") from _call_day_card_ch1
    call ch1_morning from _call_ch1_morning
    call ch1_first_period from _call_ch1_first_period
    call ch1_choir from _call_ch1_choir
    call ch1_hallway from _call_ch1_hallway
    call ch1_lunch from _call_ch1_lunch
    call ch1_club from _call_ch1_club
    call ch1_after_club from _call_ch1_after_club
    call ch1_walk_natsuki from _call_ch1_walk_natsuki
    return

########################################################################
## Morning
########################################################################
label ch1_morning:
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    "Valentine's Day."
    "In middle school it meant a cardboard box of candy hearts that tasted like chalk, and a teacher making everyone give a card to everyone so nobody felt left out."
    "In high school, apparently, it means war."
    "Half the people on this street are carrying something pink. One guy from the second year walks past me holding an entire bouquet like it's a weapon."
    "I'm fourteen. I'm a freshman. I am carrying a backpack, a granola bar, and absolutely no plan."

    s "[player]! Waaait!"

    show sayori 4p zorder 2 at t11
    s "You were gonna leave without me!"
    mc "You were still in your pajamas when I knocked."
    s 4r "That's what running is for!"
    s 1c "Ehehe... okay, I also forgot my shoes the first time. Don't tell anyone."
    mc "Your secret's safe."

    show sayori 1l zorder 2 at t11
    s "Sooo. It's Valentine's Day."
    mc "I've heard."
    s 1x "Are you giving anybody anything?"
    mc "...No."
    s 1b "Are you {i}getting{/i} anything?"
    mc "Sayori."
    s 4r "I'm just asking! As your neighbor! It's my neighborly duty!"

    "She bounces along next to me for a while, humming."
    "Then, more quietly than usual:"

    s 1t "Hey... you've been kind of quiet since winter break."
    s 1g "Since... you know. You and Yuri."
    mc "I'm fine."
    s 1u "You say that a lot."
    mc "Because I'm fine a lot."

    "She doesn't push. That's the thing about Sayori. She knows exactly how hard to push, which is almost never."

    s 1q "Okay! Then today is gonna be a good day. I've decided."
    s 4r "Valentine's Day rule number one: nobody's allowed to be sad!"
    mc "Who made that rule?"
    s 4l "Me! Just now!"

    "I can't help it. I laugh."
    "Maybe she's right. Maybe it'll be a good day."

    stop music fadeout 2.0
    return

########################################################################
## 1st period - Science lab (Kara)
########################################################################
label ch1_first_period:
    scene bg science_lab
    with wipeleft_scene
    play music t3

    "First period is Earth and Physical Science, with Mr. Hale."
    "It's the only class where the stools spin, so it's automatically the best class."
    "My lab partner is already at our bench when I get there. She always is."

    show kara 1b zorder 2 at t11
    "Kara."
    "Twelve weeks ago, she didn't know I existed. Now she's the first person I see every morning."
    "She's still quiet in the way that makes people forget she's in the room. Long, pale hair that's always in her eyes. Handwriting so neat it looks typed."
    "She's still the smartest person in this building, including Mr. Hale, and she still acts like that's no big deal."
    "And she's still clumsy. Legendarily clumsy. I've caught five beakers for her since November."

    k 1a "Good morning, [player]."
    mc "Morning. You're early again."
    k 1k "It's a good morning. The lights are almost exactly B-flat today."
    mc "Sixty hertz. Alternating current."
    k 1j "You remembered!"
    mc "You've told me like nine times."
    k 1q "Ahaha. Then it's working."

    hale "Alright, settle down! Today we're doing density columns."
    hale "Honey, dish soap, water, oil, rubbing alcohol. If anyone drinks the honey, I will know."

    "Kara gets the labels ready while I get the materials."
    "She writes each one out carefully: HONEY. SOAP. WATER. And in the corner of each label, a tiny flower, drawn in blue pen."
    "She does it on every label. Every lab. She started doing it back in December, on our water cycle project. \"For luck.\" As far as I know, I'm still the only person who's noticed."

    mc "Okay, honey goes first. You want to pour?"
    k 1t "Um... you should probably do it."
    k 1e "We both know how that's going to go if I do it."
    mc "Come on. You've got this. Slow is smooth."

    "She takes the cylinder like it might bite her."
    "The honey goes in slow. Then the soap. Then the water, tinted blue."
    "It doesn't spill. Not even a drop."

    k 1j "I... I didn't spill it!"
    mc "You didn't spill it!"
    k 1w "That's the first time all year!"
    mc "See? Told you. Slow is smooth."

    "She smiles at the column for a long time. Longer than a density column really deserves."
    "Then she looks at me, opens her mouth like she's about to say something..."

    k 1h "Hey, [player]... can I ask you something?"
    mc "Sure."
    k 1u "Do you... um."
    k 1o "..."
    k 1a "Never mind. It's nothing. We should write down the results."

    "She bends over her notebook, hair falling in front of her face."
    "I don't think about it much."
    "Kara says \"never mind\" a lot."

    hale "Clean up your stations! And whoever left a pencil in the eyewash station, I'm begging you, stop."

    show kara 1n zorder 2 at t11
    "When the bell rings, she waves at me with two fingers and stays behind to wipe down the bench."
    "She always stays behind."

    stop music fadeout 2.0
    return

########################################################################
## 2nd period - Choir (all-boys choir, music room). Monika delivers the letter.
########################################################################
label ch1_choir:
    scene bg music_room
    with wipeleft_scene
    play music t3

    "Second period is choir. Every day."
    "The Boys' Chorus. Twenty-two guys, ages fourteen to eighteen, all crammed into a music room with a drum kit nobody's allowed to touch."
    "I signed up because Sayori said I \"have a nice humming voice.\" I stayed because it turns out I like it. Not that I'd say that out loud in here."

    show dunn a zorder 2 at t11
    dunn "Alright, gentlemen! Spring concert is in six weeks and the tenors still sound like a car alarm. From the top!"

    "Mr. Dunn. Choir director. Beard, glasses, a voice that could fill a stadium without a microphone. He wears the same dark red sweater so often that the seniors think he owns thirty identical ones."
    "We're working on an old folk song about a sailor who keeps promising to come home."
    "I'm a baritone, which mostly means I stand in the middle and try not to get noticed."
    hide dunn
    with dissolve

    "We're halfway through the second run when somebody knocks on the door."

    show dunn d zorder 2 at t11
    dunn "...Come in. Apparently."
    hide dunn

    show monika 1a zorder 2 at t11
    "Monika."
    "Second year. Student Council secretary. President of the Literature Club, which I am somehow also a member of."
    "She's holding a plain white envelope. There's a little clear bag taped to the front of it, tied with a pink ribbon, full of Hershey's Kisses."
    "Twenty-two guys see the envelope. Twenty-two guys see the Kisses."
    "The room goes completely silent in a very, very bad way."

    m 1b "Sorry for interrupting, Mr. Dunn! This'll only take a second."
    m 1d "I'm looking for [player]?"

    "Every head in the room turns to look at me."
    "I would like to evaporate."

    show monika 1a zorder 2 at t11
    "She walks it over to me. Right through the middle of the bass section. Slowly. I think she's trying to be nice about it, and somehow that's worse."

    m 1c "This was in the student council drop box on Monday morning. The one outside our office, for suggestions and lost-and-found."
    m 1d "There was a sticky note on it. It said: {i}Please give this to [player] on Valentine's Day. Please don't read it.{/i}"
    m 1e "So I didn't. I promise. I don't know who it's from."
    m 1m "The council doesn't usually... deliver things. But someone was brave enough to write it. Throwing it away felt wrong."
    m 1a "I'm just the mail carrier today. Happy Valentine's Day, [player]."

    hide monika
    with dissolve
    "She waves at Mr. Dunn and leaves."
    "The door clicks shut."
    "There's about one full second of silence."

    "Then the entire Boys' Chorus loses its mind."

    show zach 1c11 zorder 2 at t11
    z "OHHHHHH!"
    "Zach Moreau. Fellow freshman, fellow baritone, the first person in this room who talked to me in September, and by a wide margin the loudest."
    z 1c4 "[player]!! [player] has a SECRET ADMIRER!! And she sent KISSES!!"
    z 1c10 "Chocolate ones! But still! KISSES!"
    "Somebody in the tenor section starts singing \"Here Comes the Bride.\" Badly. Somebody else wolf-whistles. One of the seniors yells \"READ IT OUT LOUD.\""
    mc "I am not reading it out loud."

    show zach 1c4 zorder 2 at t21
    show dunn b zorder 2 at t22
    dunn "Gentlemen. GENTLEMEN."
    dunn "If I hear one more note that isn't in the sailor song, every one of you is singing the alto part. In falsetto. At the concert."
    "That shuts them up. Mostly."
    dunn "Ten minute water break. [player], read your mail. Everyone else, leave him alone."
    hide dunn
    hide zach
    with dissolve

    "I go sit in the corner by the window, facing the wall, and open it."

    call show_note(note_valentine) from _call_show_note_ch1

    "I read it twice."
    "Then a third time, slower."
    "{i}You hum when you're concentrating.{/i}"
    "{i}You always let me hold stuff even when we both know I'm gonna drop it.{/i}"
    "{i}Our mornings. Thursdays especially.{/i}"
    "And next to \"Anonymous,\" so small I almost missed it: a tiny flower, drawn in blue ink."
    "..."
    "Kara."
    "It has to be Kara."
    "Science is first period. We have the lab Mondays and Thursdays. The flowers on the labels. The beakers."
    "{i}Hey, [player]... can I ask you something?{/i}"
    "{i}Never mind. It's nothing.{/i}"
    "My heart is doing something I don't have a name for yet."

    show zach 1c2 zorder 2 at t11
    "Zach drops into the chair next to me. He lasted about forty seconds of leaving me alone. That's a personal record."
    z "Okay. Okay okay okay. I'm not gonna ask who it's from."
    z 1c3 "...Who's it from."
    mc "It's not signed."
    z 1c13 "Not SIGNED? That's so mysterious. That's like a movie."
    z 1c2 "What's it say? Not like all of it. Just like... the vibe."
    mc "It says I hum when I'm concentrating."
    z 1c10 "Bro. Everybody knows you do that. You were humming the bass line in the hallway this morning. The whole hallway. It's like your whole thing."

    "Everybody knows."
    "...Okay. So maybe it's not the most secret clue in the world. But the rest of it still fits. The flower. The mornings. Thursdays."

    z 1c20 "Can I have one of your kisses?"
    z 1c22 "...That came out SO wrong. I mean the chocolate. Can I have one of the chocolate ones."
    "I give him one. He eats it like it's a sacred object."

    show zach 1c1 zorder 2 at t21
    show cassian 2a zorder 2 at t22
    cas "Zach. Mr. Dunn wants you to help move the risers."
    z 1c12 "Right now? On my water break?"
    cas 2f "Right now."
    z 1c14 "...This is a conspiracy against baritones."
    hide zach
    with dissolve

    show cassian 2a zorder 2 at t11
    "Cassian Hoshino. Senior. Bass section leader. Tall, quiet, and generally treated by the rest of the choir like a weather event: you don't argue with it, you just plan around it."
    "He's said maybe twenty words to me all year."
    "He sits down in Zach's chair."

    cas 2a "Mr. Dunn doesn't need help with the risers."
    mc "...Oh."
    cas 2d "You looked like you needed a minute without twenty-one guys asking about your letter."
    mc "Thanks."
    cas 1a "..."
    cas 1e "You're carrying something heavy. It's on your face. And not the good kind of heavy you'd expect from a bag of chocolate."
    cas 1a "You don't have to tell me. But I'm a decent listener. People don't expect that."

    menu:
        "Should I tell him?"

        "Tell Cassian who I think wrote it.":
            $ told_cassian = True
            mc "I think I know who wrote it. A girl in my science class. Kara."
            mc "She's really nice. And really smart. And I don't know if I feel the same way, and I don't want to hurt her."
            cas 1h "..."
            cas 1c "Then don't leave her waiting."
            cas 1a "Whatever your answer is, give it to her. Soon. In person, if you can."
            cas 1d "Waiting is the worst part. Not knowing is the worst part. Trust me."
            mc "That sounds like experience."
            cas 1n "...Something like that."
            "He doesn't explain. I get the feeling he doesn't explain much."
            cas 1b "If you need anything, I'm usually in here at lunch. It's quiet."

        "Say it's nothing.":
            $ told_cassian = False
            mc "It's nothing, really. It's just a weird day."
            cas 1a "Alright."
            cas 1c "Offer stands, if it ever stops being nothing."
            "He nods once, gets up, and goes back to the bass section like the conversation never happened."

    hide cassian
    with dissolve

    "In the back row, Oni is watching me."
    show oni 1a zorder 2 at t11
    "At least, I think he's watching. It's hard to tell with Oni. His hair covers his eyes completely. I don't know his real name. I'm not sure anyone does. He's a sophomore, and he mouths the words to every song, and I have never once heard him actually sing."
    "He didn't laugh with everyone else when Monika came in. He didn't even turn around."
    "He raises one finger, like he's about to say something."
    "Then he lowers it, and smiles, and looks away."
    hide oni
    with dissolve

    show dunn d zorder 2 at t11
    dunn "Break's over! From bar twelve! [player], I'm watching you!"
    hide dunn
    with dissolve

    "We sing the sailor song again."
    "This time I come in right on time. And for the whole song I think about a girl with pale hair, smiling at a density column."

    "On my way out the door, Oni passes me in the doorway."
    show oni 2b zorder 2 at t11
    oni "Happy Valentine's Day, [player]."
    hide oni
    with dissolve
    "He's never said my name before. I didn't know he knew it."
    "I put the letter in my jacket's inside pocket, and the Kisses in my backpack, and spend third and fourth period not hearing a single word anyone says."

    stop music fadeout 2.0
    return

########################################################################
## Hallway with Natsuki
########################################################################
label ch1_hallway:
    scene bg corridor
    with wipeleft_scene
    play music t6

    "After fourth period, in the hallway, somebody grabs my backpack strap and yanks."

    show natsuki 4t zorder 2 at t11
    n "Hey, dummy. You walked right past me."
    "Natsuki."
    "Best friend since third grade, when she punched a kid for stepping on my lunch, and then shared her lunch with me because she felt bad about the punching."
    "She has not changed much."
    mc "Sorry. Distracted."
    n 1k "Oh, I {i}bet{/i} you're distracted."
    n 1p "Monika walked into the {i}choir room{/i} with a {i}love letter{/i} for you? With {i}chocolate kisses{/i} on it? In front of the {i}entire Boys' Chorus?{/i}"
    mc "How do you already know about that?"
    n 2g "[player]. Twenty-two guys saw it. Twenty-two guys have phones. The whole school knew before second period was even over."
    n 2c "Some tenor posted that you went 'red like a fire truck.'"
    mc "...I did not."
    n 2t "You're doing it right now."
    n 2q "So? Who's it from? Show me!"
    mc "It's anonymous."
    n 2s "Anonymous. Right. Sure."
    n 2g "And you totally don't have a guess. With your 'distracted' face on."
    mc "...Maybe I have a guess."

    show natsuki 1u zorder 2 at t11
    "For half a second, something crosses her face that I don't recognize."
    "Then it's gone, and she's rolling her eyes."

    n 2c "Ugh. Whatever. Good for you, I guess."
    n 2f "If it's from someone weird, I'm not helping you hide from them."
    mc "Noted."
    n 1a "..."
    n 1i "...Did you get anything else? Like, from anyone else?"
    mc "Just the one. Why?"
    n 4x "No reason! Jeez! Can't a person ask a question!"

    "That's when I notice she's holding something behind her back. Small. Wrapped in pink paper with a lopsided bow."

    menu:
        "What's behind her back?"

        "Ask her what she's hiding.":
            $ asked_natsuki_gift = True
            mc "What's that behind your back?"
            n 1o "Wh- nothing! It's nothing! It's a- it's a math thing!"
            mc "A math thing. Wrapped in pink paper. With a bow."
            n 1v "IT'S A VERY FESTIVE MATH THING."
            n 2s "...It's for someone, okay? I'll give it to them later. Maybe. If I feel like it."
            mc "Okay."
            n 2q "Stop smiling like that!"

        "Let it go.":
            $ asked_natsuki_gift = False
            "Whatever it is, she clearly doesn't want me to see it."
            "I figure it's for someone else."

    n 2s "Go to class. You're gonna be late, and then you'll blame me."

    hide natsuki
    with dissolve
    "She stomps off down the hallway."

    stop music fadeout 2.0
    return

########################################################################
## 5th period - Lunch (free roam)
########################################################################
label ch1_lunch:
    scene bg restaurant
    with wipeleft_scene
    play music t3

    "Fifth period is lunch."
    "Our school doesn't have a normal cafeteria. It has \"Le Menu,\" a café some rich alumni paid for, which is very pink and very fancy and serves chicken nuggets for six dollars."
    "Nobody knows why the menu says the tacos cost six hundred dollars. It's become a school legend."
    "Lunch is forty minutes. Enough time to go two places, maybe, if I'm quick."

    $ ch1_lunch_visits = 0
label ch1_lunch_menu:
    if ch1_lunch_visits >= 2:
        jump ch1_lunch_end

    menu:
        "Where should I go?"

        "Sit with Natsuki at our usual table." if not ch1_lunch_natsuki:
            $ ch1_lunch_natsuki = True
            $ ch1_lunch_visits += 1
            call ch1_lunch_natsuki_scene from _call_ch1_lunch_natsuki_scene

        "Check the clubroom. Yuri sometimes eats there alone." if not ch1_lunch_yuri:
            $ ch1_lunch_yuri = True
            $ ch1_lunch_visits += 1
            call ch1_lunch_yuri_scene from _call_ch1_lunch_yuri_scene

        "Go ask Monika about the letter at the student council office." if not ch1_lunch_council:
            $ ch1_lunch_council = True
            $ ch1_lunch_visits += 1
            call ch1_lunch_council_scene from _call_ch1_lunch_council_scene

        "Go look for Kara at the science lab." if not ch1_lunch_lab:
            $ ch1_lunch_lab = True
            $ ch1_lunch_visits += 1
            call ch1_lunch_lab_scene from _call_ch1_lunch_lab_scene

    jump ch1_lunch_menu

label ch1_lunch_end:
    scene bg corridor
    with wipeleft_scene
    "The bell rings. Lunch is over."
    "Two more periods, and then the club."
    "And then... I guess I find out if I'm right."
    return

label ch1_lunch_natsuki_scene:
    scene bg restaurant
    with wipeleft
    show natsuki 1a zorder 2 at t11
    "Natsuki is at our usual table by the window, defending the second chair from a freshman with her foot."
    n 1l "Finally! I've been fighting off the hordes for you."
    mc "My hero."
    n 2t "Darn right."

    "She shoves half a sandwich at me without asking. She always makes too much. She has always made too much, every single day, since third grade."
    "It took me until about sixth grade to realize she was doing it on purpose."

    n 1c "So. The letter."
    mc "I thought you said 'whatever.'"
    n 2g "I'm allowed to change my mind. It's Valentine's Day. Everybody's being weird."
    n 1k "Are you gonna... like, do something about it?"
    mc "It says to find them if I feel the same."
    n 1u "And do you? Feel the same?"

    "I think about it. Honestly think about it."
    "Kara, smiling at a density column for way too long. Kara, waving with two fingers."
    mc "...I don't know yet. I think I want to talk to her, at least."
    n 1g "Her."
    mc "I think I know who it is."
    n 1i "..."
    n 4c "Cool. Cool cool cool."

    "She takes a really, really big bite of her sandwich."

    n 1q "Mmf. Just, y'know. Be careful, okay?"
    n 1s "You're kind of a pushover. People could take advantage of that."
    mc "Natsuki, are you worried about me?"
    n 4x "No! I'm worried about whoever has to listen to you whine if it goes bad! Which is me! It's always me!"

    "That's fair. It usually is her."
    return

label ch1_lunch_yuri_scene:
    scene bg club_day
    with wipeleft
    play music t6 fadeout 1.0
    "The clubroom is quiet. Sunlight, dust in the air, the smell of old books."
    "And Yuri, in the corner by the window, reading with a lunch she hasn't touched."

    show yuri 1g zorder 2 at t11
    y "Oh..."
    y 3o "[player]. I wasn't... I didn't think anyone would come here."
    mc "Sorry. I can go."
    y 1h "N-no! Please. You don't have to go."
    y 1u "It's your clubroom too, after all."

    "We broke up three months ago."
    "It wasn't a big fight or anything. It was worse than a fight. It was quiet."
    "She started pulling away, and I thought she was bored of me. So I pulled away too, so I wouldn't be the one who got left. And then one day we just... weren't together anymore."
    "Neither of us ever actually said it out loud."

    mc "What are you reading?"
    y 1b "Oh, it's... a collection of letters. Real ones. Between two poets, in the eighteen hundreds."
    y 1s "They wrote to each other for eleven years. They only met in person twice."
    mc "That sounds lonely."
    y 3n "I suppose. But I think... sometimes it's easier to be honest on paper."
    y 3q "When you don't have to watch the other person's face while they read it."

    "She's not looking at me when she says it."
    "There's a pink envelope tucked into the back of her book like a bookmark. I can see the edge of it."

    mc "Is that a valentine?"
    y 3p "Wh- this? It's nothing! It's a bookmark! I-it's..."
    y 3v "..."
    y 1w "...It's a letter I didn't send."
    mc "Oh."
    y 1v "Please don't ask who it's for."

    "I don't."
    "We sit together until the bell. She reads. I eat. It's the most comfortable silence I've had in three months."
    return

label ch1_lunch_council_scene:
    scene bg corridor
    with wipeleft
    "The student council office is at the end of the first-floor hallway. The drop box is bolted to the wall next to the door: a gray metal box with a slot, older than everyone in this building."
    "The door's open. Monika's inside, eating lunch over a stack of budget forms. Sayori is sitting on the desk, \"helping,\" which seems to mean eating Monika's crackers."

    show monika 1a zorder 2 at t21
    show sayori 4r zorder 2 at t22
    s "[player]! Did you come to visit us?! Nobody ever visits the council office! It's very lonely in here!"
    m 1k "You've been here for twenty minutes, Sayori."
    s 1h "It's very lonely in here {i}with crackers.{/i}"

    mc "I wanted to ask about the letter. From this morning."
    m 1c "Ah."
    m 1d "[player], I really don't know who sent it. I wasn't just saying that."
    mc "Is there any way to find out? Like, does anyone keep track of what goes in the box?"
    m 2d "I do, sort of. I write everything down in the logbook when I empty it. Date, time, what it was. Habit."
    m 1a "But just what it {i}was.{/i} Not who left it. The box doesn't exactly have a security camera."
    m 1e "If it helps, it was there when I opened up on Monday. Seven-fifteen in the morning. Before anyone else was even in the building."
    m 1j "Someone was very eager."

    "Monday morning. Before school."
    "Kara gets to school early. Kara likes it when it's quiet."

    s 1x "Ooooh, [player] has a secret admirer!"
    mc "Sayori..."
    s 4r "Rule number one! Nobody's allowed to be sad! And you look {i}very{/i} not sad right now!"

    "I guess I do."
    return

label ch1_lunch_lab_scene:
    scene bg science_lab
    with wipeleft
    play music t9 fadeout 1.0
    "The science lab is locked during lunch."
    "I press my face to the little window in the door anyway."
    "The lights are off. Empty stools. The density columns from this morning are lined up on the windowsill, still perfectly layered."
    "Our bench is the one by the window. Somebody's left a notebook in the shared drawer. I can see the corner sticking out."
    "There's no one in there."
    "{i}If you like me back... find me? You'll know where.{/i}"
    "Not now, I guess. Maybe after school."
    "For some reason I stand there for a long time anyway, listening to the lights hum."
    "She was right. They do hum."
    play music t3 fadeout 1.0
    return

########################################################################
## After school - Literature Club
########################################################################
label ch1_club:
    scene bg club_day
    with wipeleft_scene
    play music t3

    "After school, the Literature Club."
    "It's five of us: Monika, Sayori, Natsuki, Yuri, and me. Monika started it last year. Sayori dragged me into it in September. Natsuki joined two weeks later and claims it was \"for the snacks.\""
    "Yuri was already here when I joined."
    "That's how we met, actually."

    show monika 2b zorder 2 at t11
    m "Okay, everyone! Happy Valentine's Day!"
    m 2a "In honor of the holiday, today's activity is a little different."

    show monika 1b zorder 2 at t11
    m "Everyone writes a short poem. Five lines or less. It has to be about love. Any kind of love, it doesn't have to be romantic."
    m 1k "Then we put them all in a hat, I read them out loud, and nobody has to say which one is theirs."
    m 1j "Anonymous love letters. Very Valentine's Day, don't you think?"

    show monika 1a zorder 2 at t31
    show natsuki 4t zorder 2 at t32
    show sayori 1q zorder 2 at t33
    n "Before that! Before the poems!"
    n 4l "I made cupcakes. Obviously. Because it's a holiday and I'm the only one who does anything around here."
    s 4m "CUPCAKES!!"
    n 2t "Don't touch them yet! There's one for each person!"

    "They're heart-shaped, with pink frosting, and each one has a name piped onto it in icing."
    "MONIKA. SAYORI. YURI. And mine, which says my name and has a little extra frosting heart on the side that none of the others have."
    mc "How come mine has an extra heart?"

    show natsuki 1o zorder 3 at f32
    n "I- I ran out of room on the other ones! The extra frosting had to go somewhere! It's a {i}frosting distribution issue!{/i}"
    s 1r "Awww, Natsuki loves [player]~"
    n 1v "SAYORI, I SWEAR-"
    m 1l "Ahaha... okay! Okay! Poems!"

    show natsuki 2s zorder 2 at t32
    "Natsuki sits down hard, arms crossed, and doesn't look at me for the next ten minutes."
    "The cupcake is really, really good, though."

    scene bg club_day
    with dissolve_scene_half
    "We all write."
    "I stare at my blank paper for a long time. I think about the letter in my jacket. About Kara."
    "And then, without really deciding to, I look across the room at Yuri, and she's already looking at me, and we both look away."
    "I write something. I don't let myself think too hard about it."

    show monika 1a zorder 2 at t11
    m "Alright! I have all five. Let's go!"
    m 1b "Number one..."
    m 1d "\"Cupcakes are love. Cupcakes are life. If you don't like cupcakes, you can fight me.\""
    m 1l "...That's three lines, and I have a guess."
    show natsuki 4y zorder 2 at t22
    n "It's anonymous! You can't guess!"
    hide natsuki
    m 1b "Number two: \"My best friend lives next door, and every morning I am late, and every morning they wait.\""
    m 1e "Aww."
    "I don't look at Sayori. Sayori doesn't look at me. We're both smiling."

    m 1b "Number three... \"Love is a thing you choose, again and again, even on the days it's hard to.\""
    m 1j "Mine. Obviously. I'm not even going to pretend."

    m 1d "Number four."
    m 1c "..."
    m 1o "Oh. This one's... very good."

    "She reads it slowly."

    m 1q "\"We ended in silence, like a book with the last page torn out.\""
    m 1r "\"I have read every other page a hundred times since.\""
    m 1q "\"I still don't know how the story ends.\""
    m 1r "\"I think I'd like to.\""

    "Nobody says anything for a second."
    "I know that handwriting. I'd know it anywhere. It used to be on notes in my locker."
    "I don't look at Yuri. I can't."

    m 1a "...And number five."
    m 1d "\"I got a letter today. It said: find me. I don't know yet who I'm looking for.\""
    m 1e "Ooh. Mysterious."
    show sayori 4x zorder 2 at t33
    s "Hmmmmmmm."
    mc "It's anonymous, Sayori."
    s 4r "I didn't say anything!"
    hide sayori

    m 1k "Okay! That's the meeting, everyone. Happy Valentine's Day. Go home, eat chocolate, be nice to each other."

    stop music fadeout 3.0
    return

########################################################################
## After the club - Yuri
########################################################################
label ch1_after_club:
    scene bg club_day
    with dissolve_scene_full

    "Everyone starts packing up."
    "The letter is still in my jacket."
    "{i}If you like me back... find me? You'll know where.{/i}"
    "The science lab is on the second floor. If Kara's waiting, she's waiting there. I'm almost sure of it."
    "I pick up my bag and head for the door."

    y "[player]."

    show yuri 3o zorder 2 at t11
    play music t10 fadeout 2.0
    "Yuri is standing by the window. Everyone else is already gone. I didn't even notice them leave."
    y 3p "C-could you... stay a minute? Please?"
    y 3n "I won't keep you long. I know you probably have somewhere to be."

    "I do."
    "I put my bag down anyway."

    y 1g "That poem. Number four."
    mc "I know."
    y 1v "You... you knew it was mine."
    mc "You still dot your i's with tiny circles. You've done that since September."
    y 1w "..."
    y 3u "Ah. I suppose I'm not very good at anonymity."

    "She takes the pink envelope out of her book. The one from lunch. Or the one I saw her with, anyway."
    y 1h "I wrote it on Sunday. On Monday morning I walked to your locker to leave it there, and I stood in front of it holding this until the first bell rang."
    y 1v "And then I walked away, because I was a coward."
    y 1w "I'm always a coward. That's... that's why we ended, isn't it? Because I didn't say anything. I just got quieter and quieter and waited for you to notice."
    mc "I did notice. I thought it meant you were done with me."
    y 1e "Done with you?"
    mc "So I got quiet too. I figured if I left first, it wouldn't hurt as much."
    y 1f "But that's... that's exactly what I thought {i}you{/i} were doing."
    mc "..."
    y 1o "We're both very stupid."
    mc "Yeah."

    "And she laughs. Just a little. The first time I've heard her laugh in three months."

    y 1u "Will you read it? The letter? You don't have to answer. I just... I want you to have it. I want one thing to finally be said out loud. Even if it's on paper."

    "She holds it out."
    "In my jacket, the other letter is pressing against my chest."
    "{i}Find me.{/i}"
    "Kara. Kara is maybe waiting right now, on a spinning stool, in a room where the lights hum."
    "..."
    "But Yuri is right here."
    "And I realize I've been waiting three months for her to say something. Anything. And here she is, saying it."
    "I take the envelope."
    "I don't open it."

    mc "I don't need to read it."
    y 1g "Oh..."
    mc "Yuri. I'd like to know how the story ends too."

    show yuri 1v zorder 3 at f11
    y "..."
    y 1w "R-really?"
    mc "Really."

    "She steps closer. She's shaking a little. So am I."
    "I've kissed exactly one person in my life, and it was her, in this room, in October, and we were both so nervous we bumped noses."
    "This time we don't."
    "It's short and soft, and when we pull apart, she's crying, but she's smiling too."

    y 1c "I missed you. I missed you so much."
    mc "I missed you too."
    y 1d "Is this... are we..."
    mc "If you want to be."
    y 3s "I want to be."

    "We stand there, by the window, until the sun's almost down."
    "I tell myself I'll talk to Kara tomorrow. I'll find her in first period and I'll be honest, and kind, and it'll be awkward, but she'll understand."
    "That's the right thing to do. Tomorrow."
    "I don't go to the science lab."

    stop music fadeout 3.0
    return

########################################################################
## Walking Natsuki home
########################################################################
label ch1_walk_natsuki:
    scene bg natsuki_house_dusk
    with wipeleft_scene
    play music t8

    "Natsuki was waiting at the school gate. She said she wasn't waiting for me. She was waiting for \"the weather.\""
    "We always walk home together on Thursdays. Her house is on the way to mine, sort of, if you take the long way. I always take the long way."

    show natsuki 1a zorder 2 at t11
    n "You're doing a weird face."
    mc "I don't have a weird face."
    n 1t "You have a {i}huge{/i} weird face. You've been smiling at nothing for six blocks. It's creepy."
    mc "..."
    mc "Yuri and I got back together."

    show natsuki 1k zorder 2 at t11
    n "..."
    n 1c "Oh."
    n 1l "Oh! Wow! That's- that's great! Seriously!"
    n 1d "I knew that poem was hers. Number four. I {i}knew{/i} it. She does that thing with the circles."
    mc "That's what I said!"

    "She laughs, and punches my shoulder, and for a second everything is completely normal."

    n 1u "So, the letter. The love letter. Was it from her?"
    mc "...No. I don't think so."
    n 1g "Then who-"
    mc "I'm going to talk to them tomorrow. Explain."
    n 1u "..."
    n 1n "Yeah. You should. That's... somebody put their heart in an envelope, dummy. You don't just leave it there."
    mc "I know."
    n 1a "Okay."

    "We're at her gate."
    "She stands there with her hand on it for a second, not opening it."

    n 1j "Hey, [player]."
    mc "Yeah?"
    n 1i "..."
    n 1y "Happy Valentine's Day. I'm glad you're happy. Like, actually."

    if asked_natsuki_gift:
        n 1i "And, um..."
        "She pulls the little pink package out of her bag and shoves it at my chest without looking at me."
        n 1s "Here. The festive math thing."
        mc "It was for me?"
        n 1o "It's a {i}friend{/i} thing! Best friends give each other stuff! That's a normal, regular thing that friends do!"
        "I unwrap it. It's a keychain: a tiny felt cupcake with pink frosting, hand-stitched. The stitches are a little uneven. There's a little extra frosting heart on the side."
        mc "You made this?"
        n 1w "...Took me three weeks. I stabbed myself like forty times."
        mc "Natsuki. I love it."
        n 1u "..."
        n 1j "Yeah, well. Don't lose it, dummy."
        "I clip it onto my backpack right there. She watches me do it like she's memorizing it."
        $ have_natsuki_charm = True

    n 4x "Now go home before I change my mind about the cupcake! I'll take it back! I'll take it back from your stomach!"

    hide natsuki
    with dissolve
    "I walk the rest of the way home with my hands in my pockets."
    "One pocket has Yuri's letter, unopened."
    "The other has Kara's."
    "When I glance back at the corner, Natsuki's still standing at her gate, watching me go."
    if have_natsuki_charm:
        "After a second, she waves. Small. Like she isn't sure she's allowed to."
    else:
        "She doesn't wave."
        "I wonder, later, whatever happened to that little pink package."

    stop music fadeout 3.0
    return
