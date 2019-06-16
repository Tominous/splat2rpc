# splat2rpc

### You might also like [owrpc](https://git.io/owrpc) - a Discord Rich Presence client for Blizzard's Overwatch!

![version](https://img.shields.io/badge/version-1.2.2-yellow.svg)
![made-with-python](https://img.shields.io/badge/Made%20with-Python-informational.svg)
![python-versions](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-critical.svg)
![GPL-license](https://img.shields.io/badge/license-GPLv3-green.svg)
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

*Thanks to [splat2api](https://github.com/splat2api/api) and [@Terax235](https://github.com/Terax235) for providing the data used for this application!*

![Hero image](https://i.imgur.com/tJ7NB4P.png)

###### Splatoon 2 + Discord Rich Presence = <3

![A demonstration of the rich presence in action](https://l.maxic.me/U25UA)

[*Click here to see a video of splat2rpc in action!*](https://l.maxic.me/aO-oT)

## About

This is a Python script that will allow you to set your own Discord Rich Presence for Nintendo's *Splatoon 2*.

The Nintendo Switch currently doesn't (and probably will never) support Discord, so this is a manual solution to the problem. It's pretty simple to use, however; the program will automatically find which maps are in rotation so it's just a couple of simple steps to display your current status!

## Dependencies

- [x] Python 3 *(programmed using 3.6.5)*

- [x] [pypresence](https://github.com/qwertyquerty/pypresence) - install via pip using `pip install pypresence`

- [ ] A functioning brain

- [x] Discord ["Show game activity" enabled](https://i.imgur.com/VBAU5Cg.png)

- [x] Some patience

## How to use

1. Clone the repo with `git clone https://github.com/maxicc/splat2rpc.git` or download the ZIP version from the top of this page.
* *(sidenote: please do not change anything in the config file - you don't need your own Discord client ID or anything!)*
2. Open up a Terminal window in the directory you cloned or downloaded this repo to.
3. Run `pip install pypresence` if you don't already have it installed.
4. Make sure Discord is running, then run `python splat2rpc.py`. You should be greeted by the program!
5. That's it, you're done! 🎉 Now, run `!help` to see what commands are available. Or just, you know, look below.
6. *EXTRA STEP FOR WINDOWS USERS!* When testing this program on Windows, I noticed that the Windows Terminal doesn't, by default, display ANSI colours, instead it will just show the escape code (which makes the console display really ugly)! To get around this, create a file called `.nocol` in the same directory as `splat2rpc.py` - this will disable the colours. You could also use an alternate terminal - I know that [Terminus](https://eugeny.github.io/terminus/) works fine, as may others. Conversely, other platforms that struggle to display ANSI colours can disable them using the `.nocol` file.

## Commands
### MAINTENANCE COMMANDS
* **!dev** - Toggle development mode on or off.
* **!help** - View this help document.
* **!quit** - Close the program.

### SCHEDULE COMMANDS
* **!schedule** - View the schedule for all in-game events.

### PRESENCE COMMANDS
* **!hero <1/2/3/4/5>** - Set Hero Mode presence. Select the number of the sector you are in.
* **!octo** - Set Octo Expansion presence.
* **!multi** - Set multiplayer presence.
* **!multiloop** - Set multiplayer presence then automatically start again (a great option if you're going to be queuing for a while).
* **!salmon** - Set Salmon Run presence.
* **!splatfest** - Set Splatfest presence.
* **!private** - Set Private Battle presence.
* **!clear** - Remove your presence from Discord.

## Future plans

This will be updated soon!
