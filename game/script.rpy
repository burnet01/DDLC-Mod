# Entry point
# Keep this file to game flow only: set up state, then call chapter labels.
# Story content lives in script-*.rpy files.
label start:

    # ID of this playthrough
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    # Developer shortcut menu (only appears when running from source).
    if config.developer:
        menu:
            "Play from the start":
                pass
            "[[Dev] Sprite viewer":
                call sprite_viewer from _call_sprite_viewer
                return

    call prologue_main from _call_prologue_main
    call ch1_main from _call_ch1_main

    # Found Kara in the lab on Thursday: she lives, and the story ends here.
    if kara_saved:
        call ending_kara from _call_ending_kara
        call endgame from _call_endgame_kara
        return

    call ch2_main from _call_ch2_main
    call ch3_main from _call_ch3_main

    call endgame from _call_endgame
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
