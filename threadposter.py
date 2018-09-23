def post_main_thread(a, b, c, d, e, f, g):
   text = '''
   \n \n \n \n Welcome to this week's cypher submission thread!\n \n
   ------
   \n
   If you want to donate ONE beat for the chance to be used in the cypher, do so [here]({}).
   \n
   \n
   ------
   \n
   \n
   **Participation/Rules**
   \n
   1. Download the beat. New cyphers are put up every Tuesday.
   \n
   2. Spit 8-16 bars (you may go up to 18 if you need to) based on each week's theme. The only alterations allowed to the beat are muting/\"cutting the beat off\" for short phrases and looping certain parts of the beat you want to rap over (ONLY 4-8 BAR SECTIONS OF THE BEAT. DON'T GO AHEAD AND START CHOPPING UP A NEW BEAT).
   \n
   3. Upload (to Soundcloud please).
   \n
   4. Post the link in this thread. Posting feedback is encouraged. **Submission deadline is Saturday 11:59 PM EST.**
   \n
   5. Three judges will listen to every entry and reply \"aye\" to every entry they believe should move on to the voting thread. They must give 4-15 \"ayes\". Judges may post entries but cannot win or be voted on.
   \n
   6. **A voting thread will be put up on Sunday at 9 PM EST**. Only entries that receive at least 2 \"ayes\" will be posted in it. **You MUST vote if you enter**. Votes from friends/non-members of /r/makinghiphop, votes for yourself, and votes outside of the voting thread will be disqualified. Members who are not participating in that week's cypher may still vote. Listen to every entry before choosing a favourite.
   \n
   7. **Voting ends on Monday at 11 PM EST.** A winner will be declared and contacted to choose the next week's beat and theme. The winner MUST pick a beat from the beat donation thread and the chosen beat must've been posted in the thread for at least five days. The producer of the beat may choose to be a judge for that week.
   \n
   Contact for any questions.
   \n
   \n
   ------------
   \n
   \n'''.format(g)
    
   text = text + "* Last week's winner: [" +a+ "]("+b+ ") with " +c +" votes." + "\n\n"
   text = text + "* **Theme: "+d+"**" + "\n\n"
   text = text + "* [This week's beat]("+e+ ") \n\n"
   text = text + "* MirkyJ's Original *TheFactThatYouNeedThisIsProofYouShouldKeepYourRapsInYourNoteBook5000* says that 16 bars on this beat is about " +f+ " seconds." + "\n\n" + "----------" + "\n"
   text = text + "Judges: /u/..."

   return text

def post_voting_thread(theme, judges):
   text = '''
   **Rules:**\n

   **SAY "VOTE" IN YOUR COMMENT OR IT WON'T BE COUNTED**\n

   **You have until 11:59 PM EST Sunday (approx 3 hours after the thread is posted) to notify me if I missed your entry.**\n

   If you submitted, YOU MUST VOTE\n

   Cannot Vote For Your Own Submission (includes using an alternate username (Honor Code))\n

   Comment/Reply to the Track You Like The Best (Upvotes Don't = Votes)\n

   Voting Continues Until Monday Night (11ish PM), EST\n

   Upvote this so it get the most exposure possible.\n

   -----------\n
   '''

   text = text + "**Theme: " + theme + "\n\n" + "Judges: "

   i = 1
   
   for judge in judges:
      if i < 3:
         text = text + "/u/" + judge + " , "
      else:
         text = text + "/u/" + judge
      i = i + 1

   return text


##string = post_main_thread("ha", "ha", "ha", "ha", "h", "a")
##print(string)
##
##theme = "yeah"
##judges = {"judge1", "judge2", "judge3"}
##string = post_voting_thread(theme, judges)
##
##print(string)
##print(string)

