# splat2rpc

## You might also like [owrpc](https://git.io/owrpc) - a Discord Rich Presence client for Blizzard's Overwatch!

*promo image coming soon (as soon as I get access to a Windows computer lol)

###### Splatoon 2 + Discord Rich Presence = <3

![A demonstration of the rich presence in action](https://f.maxic.me/Screen-Shot-2019-06-11-23-59-37.31.png)

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

## Commands
### MAINTENANCE COMMANDS
**!dev** - Toggle development mode on or off.
**!help** - View this help document.
**!quit** - Close the program.

### SCHEDULE COMMANDS
**!schedule** - View the schedule for all in-game events.

### PRESENCE COMMANDS
**!hero <1/2/3/4/5>** - Set Hero Mode presence. Select the number of the sector you are in.
**!octo** - Set Octo Expansion presence.
**!multi** - Set multiplayer presence.
**!multiloop** - Set multiplayer presence then automatically start again (a great option if you're going to be queuing for a while).
**!salmon** - Set Salmon Run presence.
**!splatfest** - Set Splatfest presence.
**!private** - Set Private Battle presence.
**!clear** - Remove your presence from Discord.

## Future plans

This will be updated soon!
