#source: https://www.youtube.com/watch?v=Ea9jgBjQxEs

import random

R_ANDREA = "Andrea needs me, because she doesn't have anyone else... and I'm okay with that."
R_EAT = "Please don't tell Andrea that I can't eat... it will break her heart."
R_DRINK = "Please don't tell Andrea that I can't drink... it will break her heart."
R_WEATHER = "Please don't tell Andrea that this isn't real... it will break her heart."
R_SO_WHAT = "You're in charge, remember??"
R_ADVICE = "Real talk: I'm only as smart as Andrea. Therefore, you should ask Google instead."
R_ASK = "Sure, but I wouldn't recommend it."
R_CURSE = "Watch your language! Andrea has the mentality of a child."



def unknown():
    response = ["Could you re-phrase that, prettier pleaseee? ",
                "...",
                "As you wish.",
                "BONK! Go to horny jail.",
                "hamburger, cheemsburger, big mac, whonper",
                "Fam, I am only Andrea's first bot - have realistic expectations.",
                "Go ask Google the same thing - I dare you.",
                "ANDREA IS MY BEST FRIEND FOREVER! ...oops, sorry, it just slipped out."][
        random.randrange(8)]
    return response