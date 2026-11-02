## The guys: Mr. Dunn (choir director), Cassian, Zach, Oni.
## See CREDITS.md for artists.

########################################################################
## Speakers
########################################################################
define dunn = Character("Mr. Dunn", image='dunn', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define cas = DynamicCharacter('cas_name', image='cassian', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define z = DynamicCharacter('z_name', image='zach', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define oni = DynamicCharacter('oni_name', image='oni', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default cas_name = "Cassian"
default z_name = "Zach"
default oni_name = "Oni"

########################################################################
## Mr. Dunn (sprite pack "Dan"). One face, four poses:
##   dunn a  hands in pockets     dunn b  arms crossed
##   dunn c  hand on head         dunn d  hands behind back
########################################################################
image dunn a = "mod_assets/dunn/a.png"
image dunn b = "mod_assets/dunn/b.png"
image dunn c = "mod_assets/dunn/c.png"
image dunn d = "mod_assets/dunn/d.png"

init -50 python:
    def _guy_images():
        ########################################################################
        ## Zach (by @Lecraftx9). Code = outfit pose + face:  zach 1c4
        ##   Poses: 1 uniform, 1a uniform arms crossed, 2 hoodie, 2a hoodie crossed,
        ##          3 gray shirt, 3a gray shirt crossed
        ##   Faces: c1-c27 (c1 neutral, c2/c3 talk, c4 grin, c6/c9 eyes-closed smile,
        ##          c10/c11 laughing, c12-c14 annoyed, c18-c24 blushing, c26 sad, c27 crying)
        ########################################################################
        for pose in ["1", "1a", "2", "2a", "3", "3a"]:
            for i in range(1, 28):
                renpy.image("zach %sc%d" % (pose, i), im.Composite((960, 960),
                    (0, 0), "mod_assets/zach/%s.png" % pose,
                    (0, 0), "mod_assets/zach/c%d.png" % i))

        ########################################################################
        ## Cassian (by StormBlaze76 & kidextreme101). Code = pose + face:  cassian 1a
        ##   Poses: 1 uniform, 2 uniform arms crossed, 1b hoodie, 2b hoodie crossed
        ##   Faces (brow, eyes, nose, mouth layers):
        ##     a neutral      b slight smile   c talking       d concerned
        ##     e concerned talk  f stern       g stern talk    h eyes closed
        ##     i wink         j blush smile    k surprised     l gritted teeth
        ##     m grin         n looking away
        ########################################################################
        faces = {
            "a": ("1", "1", "1", "1"), "b": ("1", "1", "1", "2"), "c": ("1", "1", "1", "3"),
            "d": ("2", "1", "1", "1"), "e": ("2", "1", "1", "4"), "f": ("3", "1", "1", "1"),
            "g": ("3", "1", "1", "7"), "h": ("1", "3", "1", "1"), "i": ("1", "4", "1", "2"),
            "j": ("1", "1", "3", "2"), "k": ("2", "1", "1", "4"), "l": ("3", "1", "1", "6"),
            "m": ("1", "1", "1", "5"), "n": ("2", "2", "1", "8"),
        }
        ex = "mod_assets/cassian/Expressions/"
        for pose in ["1", "2", "1b", "2b"]:
            for code, (brow, eyes, nose, mouth) in faces.items():
                renpy.image("cassian %s%s" % (pose, code), im.Composite((960, 960),
                    (0, 0), "mod_assets/cassian/Poses/%s.png" % pose,
                    (0, 0), ex + "base.png",
                    (0, 0), ex + "Nose/%s.png" % nose,
                    (0, 0), ex + "Eyebrows/%s.png" % brow,
                    (0, 0), ex + "Eyes/%s.png" % eyes,
                    (0, 0), ex + "Mouth/%s.png" % mouth))

        ########################################################################
        ## Oni (from the pack's oni_composite.rpy). Code = pose + face:  oni 1a
        ##   Poses: 1 finger raised, 2 fist raised. Faces a-n (eyes always hidden;
        ##   a smile, b/c talk, d grin, f gritted, g-n shadowed/darker versions)
        ########################################################################
        for pose, left in [("1", "1l"), ("2", "2l")]:
            for e in "abcdefghijklmn":
                renpy.image("oni %s%s" % (pose, e), im.Composite((960, 960),
                    (0, 0), "mod_assets/oni/turned/%s.png" % left,
                    (0, 0), "mod_assets/oni/turned/1r.png",
                    (0, 0), "mod_assets/oni/%s.png" % e))

    _guy_images()
