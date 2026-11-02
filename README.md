# DDLC Test Mod

A Doki Doki Literature Club fan mod, built on the classic
[DDLC Mod Template](https://github.com/Monika-After-Story/DDLCModTemplate) for
**Ren'Py 6.99.12.4**, the engine version DDLC shipped on.

This is not affiliated with Team Salvato. Follow their
[IP Guidelines](IPGuidelines.md): the mod must require the player to own DDLC and
must not redistribute the game's files.

## Setup

1. Own DDLC (free on Steam/itch.io/ddlc.moe).
2. Copy `audio.rpa`, `images.rpa` and `fonts.rpa` from DDLC's `game/` folder into
   this repo's `game/` folder. `tools/run.ps1` does this for you automatically.
   **Never add `scripts.rpa`** — it conflicts with the mod's scripts.
   `*.rpa` files are gitignored and must never be committed.

## Running

From PowerShell in the repo root:

```powershell
.\tools\run.ps1          # play the mod
.\tools\run.ps1 lint     # check for script errors
```

This uses the Ren'Py runtime bundled with your DDLC install, so the SDK isn't needed
for testing. If DDLC isn't at the Steam default path, set `$env:DDLC_DIR` first.

For building a distributable `.zip`, install the
[Ren'Py 6.99.12.4 SDK](https://www.renpy.org/release/6.99.12.4), add this folder as
a project, and use **Build Distributions → DDLC Compatible Mod**. Don't use a newer
SDK: DDLC can't load `.rpyc` files compiled by other versions.

## Layout

| Path | What it is |
| --- | --- |
| `game/script.rpy` | Entry point (`label start`). Game flow only — calls chapter labels. |
| `game/script-test.rpy` | The test chapter: one scene, one choice. |
| `game/options.rpy` | Mod name, version, save folder, build settings. |
| `game/overrides.rpy` | Change DDLC variables without editing the originals. |
| `game/advanced_scripts/` | DDLC's own definitions (sprites, backgrounds, music, transforms, poem game). Look up asset names in `definitions.rpy`. |
| `game/mod_assets/` | Put your own images/music here. |
| `game/splash.rpy` | Splash and the required fan-mod disclaimer. |

## Writing cheatsheet

```renpy
scene bg club_day              # backgrounds: bg club_day, bg class_day, bg residential_day, bg corridor, bg kitchen ...
play music t2                  # t1..t10 etc., see definitions.rpy
show sayori 1a zorder 2 at t11 # sprite pose+expression; t11 = 1 char centered, t21/t22 = 2 chars, t31..t33, t41..t44
s 4r "Line with an expression change."
mc "Player's line."
"Narration / inner thoughts."
menu:
    "Option A":
        jump label_a
```

Characters: `s` Sayori, `m` Monika, `n` Natsuki, `y` Yuri, `mc` the player.
