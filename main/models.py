import os, sys
from django.db import models
from django.conf import settings
import tweepy
# The file where you're stashing all the secret stuff:
from project.settings_local import auth_settings


# If you want to save each in a database:
class ModelTweet(models.Model):
    # The tweet itself:
    tweet = models.CharField(max_length=140)
    # When you tweeted it:
    tweet_created = models.DateTimeField(auto_now_add=True)
    # Length in characters:
    tweet_length = models.IntegerField()

    def __unicode__(self):
        return self.tweet

    @staticmethod
    def thing_it_does():

        # YOUR LOGIC GOES HERE.
        # To, for example, pick a random line from a text file:
        import random
        with open('/path/to/your/text/file.txt', 'r') as f:
            line = random.choice(f.readlines())

            return line

    @staticmethod
    def your_method_name():

        # Pass in all the secret Twtitter gibberish:
        auth = tweepy.OAuthHandler(auth_settings['consumer_key'], auth_settings['consumer_secret'])
        auth.set_access_token(auth_settings['access_token_key'], auth_settings['access_token_secret'])
        api = tweepy.API(auth)

        your_logic_method = ModelTweet.thing_it_does()

        # Updates Twitter status
        api.update_status(status=your_logic_method)
        
        # These you can write to a file as a backup if you're running it on a server crontab.
        # Also handy just to check the script in the terminal.
        print your_logic_method
        print "\n\tThis tweet was %d characters long.\n" % len(your_logic_method)

        # For creating each tweet as a database object:
        tweet = ModelTweet()
        tweet.tweet = your_logic_method
        tweet.tweet_length = len(tweet.tweet)
        tweet.save()