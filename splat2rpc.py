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
            "single-1":["Hero Mode","Tentakeel Outpost","tentakeel","Octo Canyon","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-2":["Hero Mode","Suction-Cup Lookout","suction","Octo Canyon","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-3":["Hero Mode","Beaker's Depot","beakers","Octo Canyon","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-4":["Hero Mode","Slimeskin Garrison","slimeskin","Octo Canyon","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-5":["Hero Mode","Cephalon HQ","cephalon","Octo Canyon","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"]
        }

    def clearPresence():
        try:
            dp.clear()
        except Exception as e:
            print(c.fail + "Couldn't clear your presence! :(")
            print(c.fail + "The error message from pypresence is: " + str(e))
            sys.exit(1)
        print(c.success + "Your presence has been cleared! Discord may take a few seconds to update.")

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

    def setCustom():
        print(c.warn + "Here be dragons!")
        print(c.warn + "This is a more advanced version of the presence selector. The normal ones should be much easier.")
        print(c.warn + "To ignore a line, just leave it blank.")
        print(c.blank)

        options = {
            "details":'',
            "state":'',
            "large_image":'',
            "large_text":'',
            "small_image":'',
            "small_text":''
        }
        print(c.info + '' + "Please enter your top line.")
        options["details"] = input(c.ask)
        print(c.info + '' + "Please enter your bottom line.")
        options["state"] = input(c.ask)
        print(c.info + "Please enter your large image key.")
        options["large_image"] = '' + input(c.ask)
        print(c.info + "Please enter your large image text.")
        options["large_text"] = '' + input(c.ask)
        print(c.info + "Please enter your small image key.")
        options["small_image"] = '' + input(c.ask)
        print(c.info + "Please enter your small image text.")
        options["small_text"] = '' + input(c.ask)

        for option in options:
            if options[option] == '':
                options[option] = None

        if options["large_image"] == None:
            options["large_image"] = "splatoon2-colour"

        setPresence(None,details=options["details"],state=options["state"],large_image=options["large_image"],large_text=options["large_text"],small_image=options["small_image"],small_text=options["small_text"])

    def showGreeting():
        print(c.smile + "Splatoon 2 RPC Client v" + x.ver + " by github.com/maxicc (maxic#9999)")
        print(c.info + "Information used in this app is courtesy of Terax235 (api.splatoon.terax235.me)!")
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

    showGreeting()
    setPresence("square_silent")

    while True:
        if status.devmode == True:
            print(c.warn + "Development mode is enabled. Remember to disable it when you're done!")
        command = input(c.cmd).lower()

        if command.startswith("!") == False:
            print(c.fail + "Syntax error: You need to start every command with an exclamation mark ('!') for it to work.")

        elif command.startswith("!dev"):
            status.devmode = not status.devmode

            if status.devmode == True:
                print(c.success + "Enabled development mode.")
                clearPresence()
            else:
                print(c.success + "Disabled development mode.")
                clearPresence()

        elif command.startswith("!help"):
            showGreeting()
            print(c.warn + "MAINTENANCE COMMANDS")
            print(c.info + "!dev - Toggle development mode on or off.")
            print(c.info + "!help - View this help document.")
            print(c.info + "!quit - Close the program.")
            print(c.blank)
            print(c.warn + "SCHEDULE COMMANDS")
            print(c.info + "!schedule - View the schedule for all in-game events.")
            print(c.blank)
            print(c.warn + "PRESENCE COMMANDS")
            print(c.info + "!hero <1/2/3/4/5> - Set Hero Mode presence. Select the number of the sector you are in.")
            print(c.info + "!octo - Set Octo Expansion presence.")
            print(c.info + "!multi - Set multiplayer presence.")
            print(c.info + "!salmon - Set Salmon Run presence.")
            print(c.info + "!splatfest - Set Splatfest presence.")
            print(c.info + "!private - Set Private Battle presence.")
            print(c.info + "!clear - Remove your presence from Discord.")

        elif command.startswith("!quit"):
            print(c.success + "Quitting...")
            sys.exit(0)

        elif command.startswith("!schedule"):
            getSchedules()

        elif command.startswith("!hero"):
            params = command.split()
            print(params)
            options = ["1","2","3","4","5"]
            if params[1] not in options:
                print(c.warn + "That's not a valid option.")
            else:
                setPresence("single-" + params[1])

        elif command.startswith("!octo"):
            setPresence("octo")

        elif command.startswith("!multi"):
            setMulti()

        elif command.startswith("!salmon"):
            setSalmon()

        elif command.startswith("!splatfest"):
            setSplatfest()

        elif command.startswith("!private"):
            setCustom()

        elif command.startswith("!clear"):
            clearPresence()
        else:
            print(c.fail + "Couldn't find that command! Do !help if you need a refresher, or check out the documentation at https://git.io/splat2.")
        continue


except KeyboardInterrupt:
    print("\n" + c.warn + "CTRL+C detected! Quitting...")
    sys.exit(0)
