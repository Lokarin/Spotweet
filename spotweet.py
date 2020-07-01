# -*- coding: utf-8 -*-
import tweepy
import subprocess
import sys
import os

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

comando = 'python /PATH/TO/timer.py' # Command to run the timer.

def exitErr(err):
    print("Error: " + err)
    sys.exit(1)

class main():

    	def __init__(self):
        	callStatus = subprocess.Popen(['playerctl', 'status'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        	stdout,stderr = callStatus.communicate()

        	if "Playing" in str(stdout) or "Paused" in str(stdout):
            		try:
                		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                		auth.secure = True
                		auth.set_access_token(access_token, access_token_secret)

                		global api
                		api = tweepy.API(auth)
            		except BaseException as e:
                		exitErr(str(e))

            		artistcall = subprocess.Popen(['playerctl', 'metadata', 'artist'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            		artist_stdout,stderr = artistcall.communicate()

            		songcall = subprocess.Popen(['playerctl', 'metadata', 'title'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            		song_stdout,stderr = songcall.communicate()

            		status = ("A ouvir %s - %s" %  (str(artist_stdout)[:-3][2:],str(song_stdout)[:-3][2:]))
            		api.update_status(str(status))

        	else:
            		exitErr("Nothing playing found.")

main()

os.system(comando)
