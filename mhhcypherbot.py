import praw
import config
import time
import csv
from threadposter import post_main_thread
from threadposter import post_voting_thread
from praw.models import MoreComments

## **********
## before being ready for use, change post main thread and post voting thread,
## switch to MHHCypherBot
## **********

# specifies which volume
main_sub_id = ""
voting_sub_id = ""
cuurent_vol = 0

donation_thread_link = ""

entries = []

#method to log in
def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "MHHcypherbot's comment checker v0.1")
    print("logged in successfully!")

    return r

# method that runs the bot, obtains all usernames of parent level comments
# and finds the number of times they have commented to a parent level comment
def reply_check(r):
    # the post
    submission = r.submission(id = main_sub_id)

    # the top level comments
    top_level_comments = list(submission.comments)
    usernames_list = []

    # saving each username that posted "soundcloud.com" from the top level
    # comments
    for comment in top_level_comments:
        if "soundcloud.com" in comment.body:
            usernames_list.append(comment.author)

    usernames_list = set(usernames_list)

    # putting those user_names in a dictionary
    usernames = {}

    for user in usernames_list:
        usernames[user] = 0

    # incrementing values based on amount of comments to top level comments
    for comment in top_level_comments:
        for reply in comment.replies:
            if reply.author in usernames:
                usernames[reply.author] =((usernames.get(reply.author)) + 1)

    total_entrants = 0

    for user in usernames:
        total_entrants = total_entrants + 1
        ## print(user.name + ": " + str(usernames.get(user)))

    print("there are " + str(total_entrants) + " entrants.")

    with open("cyphervol1-2018toplevel.csv", 'a') as csv_file:
        writer = csv.writer(csv_file)
        # for each comment in the top level comments

    time.sleep(2)

    print("replies have been checked in main thread")


# seems to work!
def aye_check(r):
    submission = r.submission(id = main_sub_id)
    top_level_comments = list(submission.comments)

    usernames_list = []

## finding the part of the submission text with the judges
    for line in submission.selftext.split("\n"):
        if "Judges:" in line:
            if "/u/..." not in line:
                ls = line.split()
                judge1 = ls[1][3:]
                judge2 = ls[3][3:]
                judge3 = ls[5][3:]
                print(judge1 + " " + judge2 + " " + judge3)
            else:
                judge1 = ""
                judge2 = ""
                judge3 = ""

    # saving each username that posted "soundcloud.com" from the top level
    # comments
    for comment in top_level_comments:
        if "soundcloud.com" in comment.body:
            usernames_list.append(comment.author)

    usernames_list = set(usernames_list)

    # putting those user_names in a dictionary
    usernames = {}

    for user in usernames_list:
        usernames[user] = 0

    for comment in top_level_comments:
        if "soundcloud.com" in comment.body:
            for reply in comment.replies:
                if isinstance(reply, MoreComments): # deals with MoreComments objects
                    continue
                if reply.author is not None:
                    if ((reply.author.name == judge1) | (reply.author.name == judge2)
                        | (reply.author.name == judge3)):
                        if ((reply.body.find("aye") != -1) |
                            (reply.body.find("Aye") != -1) |
                            (reply.body.find("AYE") != -1)):
                            usernames[comment.author] = ((usernames.get(comment.author)) + 1)
                            ## print(comment.author.name + " got an aye")

    print("\nhere are the entries with 2 or more ayes: \n")
    
    vt_entrants = {}

    for user, ayes in usernames.items():
        if (ayes >= 2):
            vt_entrants[user] = ""
            print(user)

    for comment in top_level_comments:
        if comment.author is not None:
            if comment.author in vt_entrants.keys():
                for line in comment.body.split('\n'):
                    ls = line.split(' ')
                    for s in ls:
                        if "soundcloud.com" in s:
                            # if "www." in s | "m." in s:
                                vt_entrants[comment.author] = s

    return vt_entrants

    print("ayes have been checked in the main thread")


def vote_check(r):
    find_voting_thread_id(r)
    submission = r.submission(id = voting_sub_id)
    submission.mod.lock()
    submission.mod.contest_mode(False)
    comments = list(submission.comments)

    comments = set(comments)

    # putting the entries in a dictionary
    entries = {}

    for comment in comments:
        if comment.author is not None:
            if (("kailman" != comment.author.name)) & ("soundcloud.com" in comment.body):
                entries[comment.body] = 0

    for comment in comments:
        for reply in comment.replies:
            if isinstance(reply, MoreComments): # deals with MoreComments objects
                continue
            if reply.author is not None:
                if reply.author != comment.author:
                    if ((reply.body.find("vote") != -1) |
                        (reply.body.find("Vote") != -1) |
                        (reply.body.find("VOTE") != -1)):
                        if comment.body in entries.keys():
                            entries[comment.body] = ((entries[comment.body]) + 1)
                        else:
                            entries[comment.body] = 1
                        ## print(comment.author.name + " got an aye")

    winner = "N/A"
    most_votes = 0
    tie_breaker = 0

    for entry, votes in entries.items():
        if votes > most_votes:
            most_votes = votes
            winner = entry
            tie_breaker = 0
        elif (votes > 0) & (votes == most_votes):
            tie_breaker = 1

    if tie_breaker == 0:
        print("This is the winner: " + winner + " " + str(most_votes))
    else:
        print("Tie-breaker functionality has not been implemented. oops")
        return None

    w_split1 = winner.split('[')
    w_split2 = w_split1[1].split(']')

    result = {}

    result[w_split2[0]] = most_votes

    print("voting thread votes have been checked")

    for comment in comments:
        if comment.author is not None:
            if w_split2[0] in comment.body:
                comment.reply("**THIS ENTRY WINS**\n\n(" + str(result[w_split2[0]]) + " votes)").mod.distinguish()
                print("voting thread reply posted")

    # file = open("/Users/kalebtsegaye/Google Drive/new_cypher_thread_info.txt", 'r')
    
    # lines = file.readlines()

    # line = lines[0]

    # l_split = line.split()

    # l_split[1] = w_split2

    # line = join(l_split)

    # lines[0] = line

    # lines = lines.join()

    # file.close()

    # file.open("/Users/kalebtsegaye/Google Drive/new_cypher_thread_info.txt", 'w')

    # file.write(lines)

    # file.close()

    find_donation_thread_link(r)

    message_body = "now, I\'m gonna need:\n\n* a beat from this [thread](" + donation_thread_link + "). The beat that you choose must\'ve been in the thread for at least 5 days.\n\n* a theme, if you want* and if you want to be a judge, lemme know.\n\nalso, i have given you the golden mic flair (https://i.imgur.com/oeNLB0J.jpg) for the week. just tell me if you want me to remove it.\n\n-------\n\nhere\'s a copy paste explanation on judging:\n\njudges just listen to every entry and reply \"aye\" to the ones they believe should make it on to the voting thread (as long as they are 8-18 bars). you can\'t give out any \"ayes\" until sunday, but i encourage early listening. look at my profile and check one of the main cypher threads to see what i mean. judging is based off of the overall quality of the entry, including lyricism, flow, mixing, etc."
    r.redditor(w_split2[0]).message('You win!!', message_body)
    print("message has been sent")

    return result


def main_thread(r, name, wlink, votes, theme, beatlink, sec):
    print("posting main thread...")
    text = post_main_thread(name, wlink, votes, theme, beatlink, sec, donation_thread_link)
    find_current_vol_num(r)
    find_donation_thread_link(r)
    new_vol = current_vol + 1
    title = "[CYPHER] VOL " + str(new_vol) + " (2018) - ALL EMCEES WELCOME TO SPIT"

    r.subreddit('makinghiphop').submit(title, selftext = text)

    print("main thread has been posted!")


def voting_thread(r, theme, judges):
    print("posting voting thread...")
    text = post_voting_thread(theme, judges)
    find_current_vol_num(r)
    title = "[CYPHER] VOL " + str(current_vol) + " (2018) VOTING THREAD"
    
    r.subreddit('makinghiphop').submit(title, selftext = text).mod.lock()

    print("voting thread has been posted!")

    time.sleep(10)

    find_voting_thread_id(r)

    # commenting all entries in
    vt_entrants = aye_check(r)

    submission = r.submission(voting_sub_id)
    
    submission.reply("**General Cypher Discussion goes here.**\n\nIf I didn't add your entry to this thread and you received at least TWO (2) ayes, tell me ASAP.").mod.distinguish()
    time.sleep(2)
    for user, link in vt_entrants.items():
        submission.reply("[" + user.name + "](" + link + ")")
    
    submission.mod.unlock()


def find_main_thread_id(r):
    global main_sub_id
    submissions = r.redditor('MHHcypherbot').submissions.new()
    for sub in submissions:
        if "ALL EMCEES WELCOME TO SPIT" in sub.title:
            main_sub_id = sub.id
            print("main thread id found")
            break

def find_voting_thread_id(r):
    global voting_sub_id
    submissions = r.redditor('MHHcypherbot').submissions.new()
    for sub in submissions:
        if "VOTING THREAD" in sub.title:
            voting_sub_id = sub.id
            print("voting thread id found")
            break

def find_current_vol_num(r):
    global current_vol
    submissions = r.redditor('MHHcypherbot').submissions.new()
    for sub in submissions:
        if "ALL EMCEES WELCOME TO SPIT" in sub.title:
            current_vol = int(sub.title[13]+sub.title[14])
            print("current volume number found")
            break
    
def retrieve_theme(r):
    find_main_thread_id(r)
    submission = r.submission(main_sub_id)
    for line in submission.selftext.split("\n"):
        if "Theme:" in line:
            ls = line.split()
            print(ls)
            theme = ls[2:]
            print(theme)
            break
    return " ".join(theme)

def retrieve_judges(r):
    find_main_thread_id(r)
    submission = r.submission(main_sub_id)
    judges = []
    for line in submission.selftext.split("\n"):
        if "Judges:" in line:
            if "/u/..." not in line:
                ls = line.split()
                judge1 = ls[1][3:]
                judge2 = ls[3][3:]
                judge3 = ls[5][3:]
            else:
                return judges
            break
    judges.append(judge1)
    judges.append(judge2)
    judges.append(judge3)
    return judges

def find_donation_thread_link(r):
    global donation_thread_link
    submissions = r.redditor('kailman').submissions.new() # change to MHHCypherBot later
    for sub in submissions:
        if "DONATION" in sub.title:
            donation_thread_link = sub.url
            print("donation thread link found")
            break

# r = bot_login()
# find_main_thread_id(r)
# find_voting_thread_id(r)
## reply_check(r)
# aye_check(r)
# vote_check(r)
# main_thread(r, "ONeill117" , "https://soundcloud.com/noodleraps/opinions-are-like-assholes-cypher-vol-8-everything" , "5", "Night / Darkness", "https://soundcloud.com/user-11475016/hip-hop-cypher-type-beat", "4")

# judges_list = ["Petravita", "razorboomarang", "kailman"]
# voting_thread(r, "step off/diss track - let's hear your harshest bars", judges_list
##
##aye_check(r)
