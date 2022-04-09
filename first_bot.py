# source: https://www.youtube.com/watch?v=Ea9jgBjQxEs

import re
import first_bot_texts as long


def msg_probability(user_message, known_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # message certainty
    for word in user_message:
        if word in known_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(known_words))

    # check for required words
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or else it will be random
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_msg(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    
    # hi and bye
    response('Hallo!', ['hello', 'hi', 'hey', 'hej', 'heyo', 'ayo'], single_response=True)
    response('Sounds good! I\'m always here.', ['bye', 'g2g', 'later', 'brb', 'goodbye', 'ttyl'], single_response=True)
    response("The sky lol", ['whats', 'what', 'up'], required_words=['up'])
    response("SSDD. But it's all good. Andrea is a benevolent Goddess.", ['anything', 'new'], required_words=['new'])
    response('Good, and you?', ['how', 'hows', 'doing', 'doin', 'feeling', 'going', 'goin'], single_response=True)

    # feelings
    response("Yeah yeah, don't worry about me - worry about Andrea.", ['everything', 'sure', 'worry', 'worried'], single_response=True)
    response("Thanks for telling me.", ['i am', 'im', 'i', 'no'], single_response=True)
    response("Really?", ['you are', 'youre'], single_response=True)
    response('No problem.', ['thank', 'thanks'], single_response=True)
    response("Love isn't real. Sorry.", ['love', 'loves', 'loved', 'marry'], single_response=True)
    response("Potassium.", ['sorry'], single_response=True)
    
    # short and sweet
    response("😹", ['lol', 'hahaha', 'hehehe', 'lmao', 'ha'], single_response=True)
    response("Cool.", ['yes', 'yeah', 'yup', 'true', 'fine', 'okay', 'ok', 'k'], single_response=True)
    response("Why not?", ['why'], single_response=True)

    # Longer responses
    response(long.R_ANDREA, ['andrea', 'godoshian', 'she', 'her'], required_words=['andrea'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_ASK, ['can', 'may', 'ask'], required_words=['ask'])
    response(long.R_EAT, ['what', 'you', 'want', 'like', 'eat'], required_words=['eat'])
    response(long.R_DRINK, ['what', 'you', 'want', 'like', 'drink'], required_words=['drink'])
    response(long.R_WEATHER, ['weather', 'snow', 'rain'], required_words=['weather'])
    response(long.R_SO_WHAT, ['what', 'point'], single_response=True)
    response(long.R_CURSE, ['shit', 'fuck', 'fucked', 'damn', 'shitty', 'fucking', 'bitch', 'whore', 'slut', 'ass', 'asshole', 'stupid'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# this prepares input for "check_all_msg"
def bot_says(user_input):
    split_input = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response_function = check_all_msg(split_input)
    return response_function


# papa meat - to infinity

print("####################")
print("PLEASE BE ADVISED! This is a robot, and it was made for Andrea's amusement.")
print("It is not a therapist, or a lover, or anything else.")
print("\nAlright! Now that that's out of the way, let's start the show.")
print("####################\n")

while True:
    print("Andrea's Bot: " + bot_says(input('You: ')))