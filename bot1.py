import tweepy
import time

consumer_key = 'GxIrHhxOmAI7zQhbc5GWTeOQH'
consumer_secret = 'xgwMV6w3fCnCrmOjRlDLIFviIXZsmdI5GQNHgBsWNbMEKmmFIr'
key = '1281155539024543751-Hz2o1Ux7Mdaj8R2vpZkOPSXpXnH92W'
secret = 'BlF0xJbVOKxQvvfOcgGBjRqGDPRXlYyqpZ24CV4x7MP9n'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# api.update_status('This is a Test Tweet Number 1')


# print(tweet[0].text)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read =open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

# id = read_last_seen(FILE_NAME)
# print(id)

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

# store_last_seen(FILE_NAME,'1281229776481447966')

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in tweets:
        if '#RandomTweet' in tweet.full_text:
            # print("Tweet Found!!!")
            print("Replied to ID -" + str(tweet.id) )
            api.update_status("@" + tweet.user.screen_name + " Good Luck of 100Daysofcode!" ,tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME,tweet.id)

while True:
    reply()
    time.sleep(15)
