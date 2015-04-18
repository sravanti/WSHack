import tweepy

auth = tweepy.OAuthHandler("dEfqVDScKJ79t9N8f98fazqfB",
                           "WPd4nU377nXguuK5FEnm2iHykuEy6cX1IVIbwJ4PZzAxmoViD8")
auth.set_access_token("50367900-7Exv6HDv52SMr8LQT1Y59Sf87o960O2Tf9sjbinOy",
                      "JcX0CZqwemqYwdB4J8YgEDULjE6lzM0nCyk1vCj8QBmWd")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
