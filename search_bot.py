import tweepy
import time

consumer_key = 'GxIrHhxOmAI7zQhbc5GWTeOQH'
consumer_secret = 'xgwMV6w3fCnCrmOjRlDLIFviIXZsmdI5GQNHgBsWNbMEKmmFIr'
key = '1281155539024543751-Hz2o1Ux7Mdaj8R2vpZkOPSXpXnH92W'
secret = 'BlF0xJbVOKxQvvfOcgGBjRqGDPRXlYyqpZ24CV4x7MP9n'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

hashtag = "100daysofcode"
tweetno = 3

tweets = tweepy.Cursor(api.search,hashtag).items(tweetno)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()

