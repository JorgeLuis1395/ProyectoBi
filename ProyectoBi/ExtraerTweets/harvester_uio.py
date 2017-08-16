'''

 
 QUITO 
==============
'''
import couchdb
import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
 
##########API CREDENTIALS ############   Poner sus credenciales del API de dev de Twitter
ckey = "qcF1yEV4iV1LeeAPHQ5juu7Jh"
csecret = "WMkEE7LN408uMhuVpUJCR9yHJHnW35hHa3RVQBFepNKFx5qS0E"
atoken = "620138022-WjJZn3UiOtE6Vtpw7S7QAyvbFbbCueH2Sqr0exnT"
asecret = "kIzyCb8xGy6mUOnHHWAlzgxbzIzFkmnhEd7KzFGSrA0R9"
 
class listener(StreamListener):
 
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
 
    def on_error(self, status):
        print status
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

 
URL = sys.argv[1]
db_name = sys.argv[2]
 
 
'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #() poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
 
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()
 
 
'''===============LOCATIONS=============='''

twitterStream.filter(locations=[-79.47,-1.37,-77.73,0.31])  #QUITO
