try:
    import time
    import sys
    import os
    import random

    try:
        from pypresence import Presence
        import requests
    except Exception as e:
        # Warn the user that the modules can't be imported then exit with error code 1
        print("[!] Error! Couldn't import a module. Did you download the dependencies?")
        print("[!] Check https://git.io/splat2 and make sure, then try running again.")
        sys.exit(1)

    from splat2config import configs as x
    from splat2config import schedules as s
    # If there is a file in this directory called ".nocol"
    if os.path.exists(".nocol") == True:
        # Import a different version of the prefixes module that removes the ANSI colours
        from mansi import nocolours as c
    else:
        # Import the normal colours module
        from mansi import colours as c

    # Define the status class
    class status():
        ingame = 0
        devmode = False
        currmap = ''
        currmode = ''
        presets = {
            "example":["details","state","large_image","large_text","small_image","small_text"],
            "square":["In Menus","Inkopolis Square","splatoon2-colour","Playing Splatoon 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "octo":["Octo Expansion","Deepsea Metro","octo","Playing Splatoon 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-1":["Hero Mode","Tentakeel Outpost","tentakeel","Octo Canyon: Sector 1","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-2":["Hero Mode","Suction-Cup Lookout","suction","Octo Canyon: Sector 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-3":["Hero Mode","Beaker's Depot","beakers","Octo Canyon: Sector 3","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-4":["Hero Mode","Slimeskin Garrison","slimeskin","Octo Canyon: Sector 4","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-5":["Hero Mode","Cephalon HQ","cephalon","Octo Canyon: Sector 5","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"]
        }

    def setPresence(preset,details='',state='',large_image='',large_text='',small_image='',small_text=''):
        """
        This function sets the Discord Rich Presence.
        [details,state,large_image,large_text,small_image,small_text]
        """
        silent = 0
        if preset != None:
            if preset.endswith("_silent"):
                preset = preset[:-7]
                silent = 1

            details = status.presets.get(preset)[0]
            state = status.presets.get(preset)[1]
            large_image = status.presets.get(preset)[2]
            large_text = status.presets.get(preset)[3]
            small_image = status.presets.get(preset)[4]
            small_text = status.presets.get(preset)[5]

        if status.devmode == True:
            details = "DEV MODE | " + str(details)
        try:
            # Update the presence using the details provided when calling the function
            dp.update(details=details,state=state,large_image=large_image,large_text=large_text,small_image=small_image,small_text=small_text,start=int(time.time()))
        except Exception as e:
            # If there is an exception, inform the user then exit with error code 1
            print(c.fail + "Couldn't set your presence properly! :(")
            print(c.fail + "The error message from pypresence is: " + str(e))
            sys.exit(1)
        if silent == 0:
            print(c.success + "Your presence has been updated! Discord may take a few seconds to update.")
        else:
            pass

    def showGreeting():
        print(c.smile + "Splatoon 2 RPC Client v" + x.ver + " by github.com/maxicc (maxic#9999)")
        onlver = requests.get("https://maxicc.github.io/splat2rpc/VERSION.txt").text.rstrip()
        if x.ver != onlver:
            print(c.warn + "You're out-of-date! The latest version on GitHub is " + str(onlver) + " and you're on " + x.ver + ".")
        else:
            print(c.success + "You're up-to-date! Thanks for using the latest version.")
        print(c.info + "Questions? Comments? Feature requests? Head to https://git.io/splat2!")
        print(c.blank + random.choice(["Don't get cooked, stay off the hook!","Staaaay fresh!"]))

    # Initialise the Discord Presence using pypresence then connect to Discord
    dp = Presence(x.client)
    dp.connect()

    print(c.smile + "splat2rpc - v" + x.ver)
    print(c.info + "Information used in this app is courtesy of Terax235 (api.splatoon.terax235.me)!")

    showGreeting()
    setPresence("square_silent")

    while True:
        continue


except KeyboardInterrupt:
    print("[!] CTRL+C detected! Quitting...")
    sys.exit(0)
