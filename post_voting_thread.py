import praw
import config
import mhhcypherbot

r = mhhcypherbot.bot_login()

theme = mhhcypherbot.retrieve_theme(r)

judges = mhhcypherbot.retrieve_judges(r)

print(theme)

print(judges)

mhhcypherbot.voting_thread(r, theme, judges)