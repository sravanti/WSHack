import tweepy

auth = tweepy.OAuthHandler("dEfqVDScKJ79t9N8f98fazqfB",
                           "WPd4nU377nXguuK5FEnm2iHykuEy6cX1IVIbwJ4PZzAxmoViD8")
auth.set_access_token("50367900-7Exv6HDv52SMr8LQT1Y59Sf87o960O2Tf9sjbinOy",
                      "JcX0CZqwemqYwdB4J8YgEDULjE6lzM0nCyk1vCj8QBmWd")

api = tweepy.API(auth)

#prints out user IDs of followees
#fine since we only print at end
end_username = "STekumalla"
start_username = "WellesleyCSClub"
MAX_DEPTH_LEVEL = 2
start_path = []
path = []

"""
I know this uses recursion
I know this is O(2^MAX_LEVEL_DEPTH*n)
I'M SORRY
Will fix with bidirectional BFS or something
"""
def find_shortest_path(start_username, end_username, path):
    path += [start_username]
    followers = tweepy.Cursor(api.friends_ids, id=start_username).items()
    for follower in followers:
        print "follower: " + str(follower)
        print "end: " + str(end_username)
        if follower == end_username:
            print "equal"
            path += [end_username]
            return path
        else:
             print "not equal"
             return find_shortest_path(follower, end_username, path)

def fsp(start, end):
    start = api.get_user(start).id
    end = api.get_user(end).id
    result = find_shortest_path(start, end, [])
    for r in result:
        print api.get_user(r).screen_name
    


"""
print find_shortest_path(api.get_user(start_username).id, 
                        api.get_user(end_username).id, start_path, 0)
"""
print fsp(start_username, end_username)
