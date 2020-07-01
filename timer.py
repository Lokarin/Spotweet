import sys
import os
import time

comando = 'python /PATH/TO/spotweet.py' # Command to run the Spotweet.
comando2 = 'notify-send "Running Spotweet..."' # Just a notify, you can remove it if you want.

x = 2 

while x != 1:
    x=x-1 
    print("foi.")

    time.sleep(360) # Put here, in seconds, the time you wanted Spotweet to publish the posts.

if x == 1:
    time.sleep(15)
    os.system(comando2)
    print("deve funcionar...")
    os.system(comando)
