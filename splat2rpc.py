try:
    import time
    import sys
    import os
    import random
    from json import loads

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
        devmode = False
        currqueue = ''
        currmap = ''
        currmode = ''
        presets = {
            "example":["details","state","large_image","large_text","small_image","small_text"],
            "square":["In Menus","Inkopolis Square","splatoon2-colour","Playing Splatoon 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "octo":["Octo Expansion","Deepsea Metro","octo","Playing Splatoon 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-1":["Hero Mode","Tentakeel Outpost","tentakeel","Sector 1","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-2":["Hero Mode","Suction-Cup Lookout","suction","Sector 2","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-3":["Hero Mode","Beaker's Depot","beakers","Sector 3","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-4":["Hero Mode","Slimeskin Garrison","slimeskin","Sector 4","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"],
            "single-5":["Hero Mode","Cephalon HQ","cephalon","Sector 5","maxic","Running splat2rpc v" + x.ver + " by maxic#9999! Download it at https://git.io/splat2 😊"]
        }

    def fillSpaces(orig):
        maxlen = 21
        toadd = maxlen - len(orig)
        for i in range(toadd):
            orig = orig + " "
        return orig

    def setStatus(clear,queue='',mode='',map=''):
        if clear == 1:
            status.currmode = ''
            status.currmap = ''
            status.currqueue = ''
        else:
            status.currmode = mode
            status.currmap = map
            status.currqueue = queue

    def clearPresence():
        try:
            dp.clear()
            setStatus(1)
        except Exception as e:
            print(c.fail + "Couldn't clear your presence! :(")
            print(c.fail + "Please report this error at https://git.io/s2issues: " + str(e))
            sys.exit(1)
        print(c.success + "Your presence has been cleared! Discord may take a few seconds to update.")

    def getSchedules(mode):
        if mode == "main":
            return requests.get(s.main_schedule).json()
        elif mode == "salm":
            return requests.get(s.salm_schedule).json()
        elif mode == "splf":
            return requests.get(s.splf_schedule).json()
        else:
            print(c.fail + "Something's gone wrong! Please report this issue at https://git.io/splat2 and let me know what you were doing when you got here.")
            print(c.warn + "You should be able to try again. Restart this program then try doing whatever you were doing again.")

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

        setStatus(0,details,state,large_text)

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
            print(c.success + "Updating presence to " + status.currqueue + ": " + status.currmode + " - " + status.currmap + ".")
        else:
            pass

    def setMulti(loop=0):
        splfschedule = getSchedules("splf")

        if "times" in splfschedule:
                if int(time.time()) > int(splfschedule['start']) or int(time.time()) < int(splfschedule['end']):
                    print(c.fail + "There's a Splatfest going on right now! Come back later.")
                    return

        jsonschedule = getSchedules("main")
        # {regular:[mode,mode-key,map-a,map-a-key,map-b,map-b-key]}
        schedule = {
            "regular": {
                "mode": jsonschedule['regular']['rule']['name'],
                "mode-key": jsonschedule['regular']['rule']['key'],
                "map-a": jsonschedule['regular']['stage_a']['name'],
                "map-a-id": str(jsonschedule ['regular']['stage_a']['id']),
                "map-b": jsonschedule['regular']['stage_b']['name'],
                "map-b-id": str(jsonschedule ['regular']['stage_b']['id'])
            },
            "ranked": {
                "mode": jsonschedule['gachi']['rule']['name'],
                "mode-key": jsonschedule['gachi']['rule']['key'],
                "map-a": jsonschedule['gachi']['stage_a']['name'],
                "map-a-id": str(jsonschedule ['gachi']['stage_a']['id']),
                "map-b": jsonschedule['gachi']['stage_b']['name'],
                "map-b-id": str(jsonschedule ['gachi']['stage_b']['id'])
            },
            "league": {
                "mode": jsonschedule['league']['rule']['name'],
                "mode-key": jsonschedule['league']['rule']['key'],
                "map-a": jsonschedule['league']['stage_a']['name'],
                "map-a-id": str(jsonschedule ['league']['stage_a']['id']),
                "map-b": jsonschedule['league']['stage_b']['name'],
                "map-b-id": str(jsonschedule ['league']['stage_b']['id'])
            }
        }

        if loop == 0:
            print(c.success + "Got the current modes! Here are your options...")

        print(c.warn + "Regular Battle (" + schedule['regular']['mode'] + ")")
        print(c.info + "1. In Queue " + "| 2. " + fillSpaces(schedule['regular']['map-a']) + " | 3. " + fillSpaces(schedule['regular']['map-b']))
        print(c.warn + "Ranked Battle (" + schedule['ranked']['mode'] + ")")
        print(c.info + "4. In Queue " + "| 5. " + fillSpaces(schedule['ranked']['map-a']) + " | 6. " + fillSpaces(schedule['ranked']['map-b']))
        print(c.warn + "League Battle (" + schedule['league']['mode'] + ")")
        print(c.info + "7. In Queue " + "| 8. " + fillSpaces(schedule['league']['map-a']) + " | 9. " + fillSpaces(schedule['league']['map-b']))
        print(c.info + "0. Cancel   | Enter any other character to refresh maps and modes.")
        option = ''
        while option == '':
            try:
                if status.currqueue == '':
                    option = int(input(c.ask + "Select an option: "))
                else:
                    option = int(input(c.ask + "Select an option (currently set to " + status.currqueue + ": " + status.currmode + " - " + status.currmap + "): "))
            except Exception as e:
                print(c.success + "Refreshing...")
                return 0
            if option == 1:
                setPresence(None,details="Regular Battle",state="In Queue",large_image="splatfest",large_text="In Queue",small_image=schedule['regular']['mode-key'],small_text=schedule['regular']['mode'])
            elif option == 2:
                setPresence(None,details="Regular Battle",state=schedule['regular']['mode'],large_image=schedule['regular']['map-a-id'],large_text=schedule['regular']['map-a'],small_image=schedule['regular']['mode-key'],small_text=schedule['regular']['mode'])
            elif option == 3:
                setPresence(None,details="Regular Battle",state=schedule['regular']['mode'],large_image=schedule['regular']['map-b-id'],large_text=schedule['regular']['map-b'],small_image=schedule['regular']['mode-key'],small_text=schedule['regular']['mode'])
            elif option == 4:
                setPresence(None,details="Ranked Battle",state="In Queue",large_image="splatfest",large_text="In Queue",small_image=schedule['ranked']['mode-key'],small_text=schedule['ranked']['mode'])
            elif option == 5:
                setPresence(None,details="Ranked Battle",state=schedule['ranked']['mode'],large_image=schedule['ranked']['map-a-id'],large_text=schedule['ranked']['map-a'],small_image=schedule['ranked']['mode-key'],small_text=schedule['ranked']['mode'])
            elif option == 6:
                setPresence(None,details="Ranked Battle",state=schedule['ranked']['mode'],large_image=schedule['ranked']['map-b-id'],large_text=schedule['ranked']['map-b'],small_image=schedule['ranked']['mode-key'],small_text=schedule['ranked']['mode'])
            elif option == 7:
                setPresence(None,details="League Battle",state="In Queue",large_image="splatfest",large_text="In Queue",small_image=schedule['league']['mode-key'],small_text=schedule['league']['mode'])
            elif option == 8:
                setPresence(None,details="League Battle",state=schedule['league']['mode'],large_image=schedule['league']['map-a-id'],large_text=schedule['league']['map-a'],small_image=schedule['league']['mode-key'],small_text=schedule['league']['mode'])
            elif option == 9:
                setPresence(None,details="League Battle",state=schedule['league']['mode'],large_image=schedule['league']['map-b-id'],large_text=schedule['league']['map-b'],small_image=schedule['league']['mode-key'],small_text=schedule['league']['mode'])
            elif option == 0:
                print(c.success + "Cancelling...")
                setPresence("square_silent")
                return 1
            else:
                print(c.success + "Refreshing...")
                return 0
            return 0

    def setSalmon():
        jsonschedule = getSchedules("salm")
        if "weapons" not in jsonschedule:
            print(c.fail + "Salmon Run is closed right now! Come back soon.")
            return

        schedule = {
            "start": jsonschedule['start_time'],
            "end": jsonschedule['end_time'],
            "map": jsonschedule['stage']['name'],
            "map-key": jsonschedule['stage']['name'].lower().replace("'","").replace(" ","")
        }

        setPresence(None,details="Salmon Run",state=schedule['map'],large_image=schedule["map-key"],large_text=schedule['map'],small_image="salmon_run",small_text="Grizzco")

        setStatus(0,"Salmon Run","Salmon Run",schedule['map'])


    def setSplatfest():
        jsonschedule = getSchedules("splf")

        if ("times" not in jsonschedule) or ("active" in jsonschedule and "false" in jsonschedule):
            print(c.fail + "The next Splatfest hasn't started yet! Come back soon.")
            return

        schedule = {
            "start": str(jsonschedule[0]['times']['start']),
            "end": str(jsonschedule[0]['times']['end']),
            "phrases": jsonschedule[0]['names']
        }

        if int(time.time()) < int(schedule['start']) or int(time.time()) > int(schedule['end']):
            print(c.fail + "The next Splatfest hasn't started yet! Come back soon.")
            return

        np = ''
        while np == '':
            print(c.info + "Are you playing Normal or Pro mode?")
            print(c.info + "1. Normal | 2. Pro")
            try:
                np = int(input(c.ask))
            except Exception as e:
                print(c.warn + "Invalid input!")
                print("Exception")
                np = ''
                continue
            if np == 1:
                np = "Normal"
            elif np == 2:
                np = "Pro"
            else:
                print(c.warn + "Invalid input!")
                option = ''
                continue


        print(c.warn + "Here are the options for this Splatfest!")
        print(c.info + "1. " + schedule['phrases']['alpha_long'])
        print(c.info + "2. " + schedule['phrases']['bravo_long'])
        option = ''
        while option == '':
            print(c.info + "Which team are you supporting?")
            try:
                option = int(input(c.ask))
            except Exception as e:
                print(c.warn + "Invalid input!")
                option = ''
                continue
            if option == 1:
                setPresence(None,details="Splatfest Battle (" + np + ")",state="Team " + schedule['phrases']['alpha_short'],large_image="splatfest",large_text="Shifty Station",small_image="turf_war",small_text="Turf War")
            elif option == 2:
                setPresence(None,details="Splatfest Battle (" + np + ")",state="Team " + schedule['phrases']['bravo_short'],large_image="splatfest",large_text="Shifty Station",small_image="turf_war",small_text="Turf War")
            else:
                print(c.warn + "Invalid input!")
                option = ''
                continue

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
            print(c.warn + "Something's wrong! The latest version on GitHub is " + str(onlver) + " and you're on " + x.ver + ".")
        else:
            print(c.success + "You're up-to-date! Thanks for using the latest version.")
        print(c.warn + "Questions? Comments? Feature requests? Head to https://git.io/splat2!")
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
                print(c.success + "Enabled development mode. Your presence has been set to Inkopolis Square.")
                setPresence("square_silent")
            else:
                print(c.success + "Disabled development mode. Your presence has been set to Inkopolis Square.")
                setPresence("square_silent")

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
            print(c.info + "!multiloop - Set multiplayer presence then automatically start again - a great option if you're going to be queuing for a while.")
            print(c.info + "!salmon - Set Salmon Run presence.")
            print(c.info + "!splatfest - Set Splatfest presence.")
            print(c.info + "!private - Set Private Battle presence.")
            print(c.info + "!clear - Set your presence to Inkopolis Square/In Menus.")
            print(c.info + "!fullclear - Fully remove your presence from Discord.")

        elif command.startswith("!quit") or command.startswith("!exit"):
            print(c.success + "Quitting...")
            sys.exit(0)

        elif command.startswith("!schedule"):
            print(c.warn + "This command is currently not working. Please use !multi to see multiplayer rotations or !salmon to see the Salmon Run schedule.")

        elif command.startswith("!hero"):
            params = command.split()
            if len(params) == 1:
                print(c.warn + "You didn't add which sector you're in! Do !hero <sector>, for example if you're in Cephalon HQ, use !hero 5.")
            else:
                if params[1] not in ["1","2","3","4","5"]:
                    print(c.warn + "That's not a valid option.")
                else:
                    setPresence("single-" + params[1])

        elif command.startswith("!octo"):
            setPresence("octo")

        elif command.startswith("!multiloop"):
            endloop = 0
            try:
                while endloop != 1:
                    endloop = setMulti(loop=1)
            except KeyboardInterrupt:
                print("\n" + c.success + "Cancelling...")
                endloop = 1
                setStatus(1)
                continue

        elif command.startswith("!multi"):
            setMulti()

        elif command.startswith("!salmon"):
            setSalmon()

        elif command.startswith("!splatfest"):
            setSplatfest()

        elif command.startswith("!private"):
            setCustom()

        elif command.startswith("!clear"):
            setPresence("square")

        elif command.startswith("!fullclear"):
            clearPresence()

        elif command.startswith("!checkvars"):
            if status.devmode == 0:
                print(c.fail + "You must be in developer mode for this command.")
                continue
            print(c.info + "Mode (details): " + status.currqueue)
            print(c.info + "Mode (state): " + status.currmode)
            print(c.info + "Mode (large_text): " + status.currmap)

        else:
            print(c.fail + "Couldn't find that command! Do !help or check the documentation at https://git.io/splat2.")
        continue


except KeyboardInterrupt:
    print("\n" + c.warn + "CTRL+C detected! Quitting...")
    sys.exit(0)
