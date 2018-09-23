import praw
import config
import mhhcypherbot

r = mhhcypherbot.bot_login()

file = open("/Users/kalebtsegaye/Google Drive/new_cypher_thread_info.txt", 'r')

info = file.readlines()

name = info[0].split(' ')[1].split('\n')[0]
wlink = info[1].split(' ')[1].split('\n')[0]
votes = info[2].split(' ')[1].split('\n')[0]
theme = info[3][7:].split('\n')[0]
beatlink = info[4].split(' ')[1].split('\n')[0]
sec = info[5].split(' ')[1].split('\n')[0]

print(name)
print(wlink)
print(votes)
print(theme)
print(beatlink)
print(sec)

mhhcypherbot.main_thread(r, name, wlink, votes, theme, beatlink, sec)