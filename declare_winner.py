import praw
import config
import mhhcypherbot

r = mhhcypherbot.bot_login()

winner = mhhcypherbot.vote_check(r)
