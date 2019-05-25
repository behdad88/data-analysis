import json

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener


consumer_key = 'DWyns3ufZNhFmviTMI0Q6gQW3'
consumer_secret = '1VJmYVxc4Z4eP1bF3vOeS2lah93hpi2WoBdgiFwEe67Tx8SUcr'
access_token = '53356414-4nudZCcY47Xnsz7S6cB9CQQpsgZ3KuXSTtbn2OSJQ'
access_token_secret = 'PMgeSNsiWIXJHhkls5y2d5D30BUOQQNvWIA61R6cpG3C8'

auth = OAuthHandler(consumer_key,
                    consumer_secret)

auth.set_access_token(access_token, access_token_secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)
    stream.sample()


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    print_to_terminal()
    # pull_down_tweets(auth.username)