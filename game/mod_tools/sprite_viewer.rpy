## Developer sprite viewer.
## Shows every expression code for a character as a face thumbnail, so you can
## pick codes while writing. Click a face to see the full sprite.
## Reachable from the developer menu at the start of a new game (developer mode only).

init python:
    import re

    SV_TAGS = ["kara", "sayori", "monika", "natsuki", "yuri", "cassian", "zach", "oni", "dunn"]
    SV_PER_PAGE = 24
    SV_FACE = (330, 150, 300, 280)  # face region on the 960x960 sprite canvas

    def _sv_sort_key(code):
        m = re.match(r"([a-z]*)(\d+)(.*)$", code)
        if m:
            return (m.group(1), int(m.group(2)), m.group(3))
        return ("~", 0, code)

    def sv_pages(tag):
        """Pages of codes, grouped by outfit prefix + pose, at most SV_PER_PAGE each."""
        codes = [k[1] for k in renpy.display.image.images if k[0] == tag and len(k) == 2]
        codes.sort(key=_sv_sort_key)

        groups = []
        for c in codes:
            m = re.match(r"([a-z]*\d+)", c)
            g = m.group(1) if m else "other"
            if not groups or groups[-1][0] != g:
                groups.append((g, []))
            groups[-1][1].append(c)

        pages = []
        for g, cs in groups:
            for i in range(0, len(cs), SV_PER_PAGE):
                pages.append((g, cs[i:i + SV_PER_PAGE]))
        return pages or [("none", [])]

    def sv_image(tag, code):
        return renpy.display.image.images[(tag, code)]

    def sv_thumb(tag, code):
        return Transform(sv_image(tag, code), crop=SV_FACE, zoom=0.45)

style sv_text is default:
    color "#222"
    outlines []
    size 18

style sv_title is sv_text:
    size 26

screen sprite_viewer():
    modal True
    default tag_i = 0
    default page = 0
    default selected = None

    $ tag = SV_TAGS[tag_i]
    $ pages = sv_pages(tag)
    $ page = min(page, len(pages) - 1)
    $ group, codes = pages[page]
    $ page_label = "pose %s  (page %d/%d)" % (group, page + 1, len(pages))

    add Solid("#f6f0f4")

    # Top bar
    hbox:
        xpos 20 ypos 12 spacing 24
        text "Sprite viewer: [tag]" style "sv_title"
        text page_label style "sv_text" yalign 0.5

    if selected is None:
        # Thumbnail grid: 8 columns
        vbox:
            xalign 0.5 ypos 60 spacing 6
            for row in range(0, len(codes), 8):
                hbox:
                    spacing 10
                    for code in codes[row:row + 8]:
                        button:
                            xysize (135, 150)
                            background None
                            hover_background Solid("#ffd6e8")
                            action SetScreenVariable("selected", code)
                            vbox:
                                add sv_thumb(tag, code)
                                text "[code]" style "sv_text" xalign 0.5
    else:
        add sv_image(tag, selected) xalign 0.5 yalign 1.0 zoom 0.8
        vbox:
            xpos 40 ypos 120 spacing 10
            text "[tag] [selected]" style "sv_title"
            text "show [tag] [selected] zorder 2 at t11" style "sv_text"
            textbutton "Back to grid" action SetScreenVariable("selected", None)

    # Bottom bar
    hbox:
        xalign 0.5 yalign 0.98 spacing 30
        textbutton "< Prev page" action [SetScreenVariable("page", max(0, page - 1)), SetScreenVariable("selected", None)]
        textbutton "Next page >" action [SetScreenVariable("page", min(len(pages) - 1, page + 1)), SetScreenVariable("selected", None)]
        textbutton "Next character" action [SetScreenVariable("tag_i", (tag_i + 1) % len(SV_TAGS)), SetScreenVariable("page", 0), SetScreenVariable("selected", None)]
        textbutton "Close" action Return()

label sprite_viewer:
    $ quick_menu = False
    call screen sprite_viewer
    $ quick_menu = True
    return
