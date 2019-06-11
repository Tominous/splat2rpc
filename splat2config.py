# splat2config.py | Splatoon 2 RPC Client Configuration
# https://www.github.com/maxicc/splat2rpc

class configs():
    """
    Configurations relating to the program itself.
    Should not be changed by users.
    """

    client = 587656557265682433
    ver = "1.0.2"

class schedules():
    """
    Configurations relating to the schedule API used.
    Should not be changed by users.
    """

    main_schedule = "http://api.splatoon.terax235.me/schedules/current"
    splf_schedule = "http://api.splatoon.terax235.me/festivals/"
    salm_schedule = "http://api.splatoon.terax235.me/coop_schedules/current"
