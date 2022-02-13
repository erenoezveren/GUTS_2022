# GUTS_2022
This program enables downloading trending twitch clips with subtitles and display them in discord using a discord bot.

How to use:

1) Set up bot for your discord server - create your own Token on the discord developer token, and replace the one in the script.  
                                        Add permissions on the developers portal for your bot to join the desired channel. Create a .env file with your discord token!
2) Download the required libraries, you can do this using `pip install --no-cache-dir -r requirements.txt` (run multiple times in case of failure).
3) Go onto your discord server
4) Run ClipBot.py in Python Shell
5) Use the following commands in a text channel on discord to use the bot:
  - !info (Information about this bot)
  - !update (Extracts the hottest clips from r/livestreamfail and uses AssemblyAI to put subtitles on them)
  - !clip (display a clip)
  - !clip [number] (display a certain clip)


Here is a video introducing the project and showcasing its features:
https://streamable.com/c7hpqn
