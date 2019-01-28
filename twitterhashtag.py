import tweepy

consumer_key = '9lDSIx1hGPkwesAqlubUVHLiz'
consumer_secret = '7WDa4wxI7z01iWJWlKix9w766m6MegJUvnGs3Ik80BBpZM37J7'
access_token = '963113574829907970-WJS4gUzvqMuqIHi8tfKDndv3SmV4d8Y'
access_token_secret = '2Jvsu3n6YpcG8C1o9jGVU4IwMK3FYt2MhDHeKq7NzhJ89'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
# csvFile = open('ua.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)
c = 0
for tweet in tweepy.Cursor(api.search,q="#metoo",count=5,
                           lang="en",
                           since="2018-09-10").items():
    try:
        print (tweet.text.encode('utf-8'))
        print()
        print()
        c = c + 1
        if c == 5:
            break
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    except UnicodeEncodeError:
        pass
