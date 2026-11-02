## Minor speakers and story helpers.

# Science teacher (1st period). No sprite.
define hale = Character("Mr. Hale", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# The visitors who show up on Monday. No sprite.
define suit = Character("Man in a gray suit", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

########################################################################
## Handwritten notes/letters on DDLC's poem paper.
##   call show_note(note_valentine)
########################################################################
init python:
    class Note(object):
        def __init__(self, title, text):
            self.title = title
            self.text = text

        def render(self):
            # Fill in the player's name (screen text only interpolates one level deep).
            s = self.title + "\n\n" + self.text
            return s.replace("[player]", store.player).replace("[", "[[")

style note_text:
    font "gui/font/Halogen.ttf"
    size 30
    color "#26265a"
    outlines []
    line_spacing 6

screen note(n):
    style_prefix "poem"
    vbox:
        add "paper"
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        vbox:
            null height 40
            text n.render() style "note_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

label show_note(n):
    play sound page_turn
    window hide
    show screen note(n)
    with Dissolve(1)
    $ pause()
    hide screen note
    with Dissolve(.5)
    window auto
    return

########################################################################
## Day title cards:  call day_card("Thursday, February 14th")
########################################################################
label day_card(title):
    $ quick_menu = False
    scene black
    with dissolve_scene_full
    show expression Text(title, size=40, color="#ffffff", outlines=[]) as day_title at truecenter
    with Dissolve(1.0)
    pause 2.0
    hide day_title
    with Dissolve(1.0)
    $ quick_menu = True
    return
