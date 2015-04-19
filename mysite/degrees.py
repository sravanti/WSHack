import tweepy
import Queue
import json

auth = tweepy.OAuthHandler("dEfqVDScKJ79t9N8f98fazqfB",
                           "WPd4nU377nXguuK5FEnm2iHykuEy6cX1IVIbwJ4PZzAxmoViD8")
auth.set_access_token("50367900-7Exv6HDv52SMr8LQT1Y59Sf87o960O2Tf9sjbinOy",
                      "JcX0CZqwemqYwdB4J8YgEDULjE6lzM0nCyk1vCj8QBmWd")
"""
auth = tweepy.OAuthHandler("GdUgSU9KafMv4rDw4jTPK2Zcw",
                           "lYY7ERRc8GlCBmvraSfuih2GJ15dNQB43UrXazYF3bg4QTMTdi")
auth.set_access_token("2244644996-yesu4bH05QsU7l6KxH9xsy9zcQfc7R7Ieosp6zF",
                      "xKUkGUUKMzK4e9I5GTzGiUuEXaFkEve2G7ITZNYIStkr8")
"""
api = tweepy.API(auth)
#prints out user IDs of followees
#fine since we only print at end
#end_username = "STekumalla"
#start_username = "WellesleyCSClub"
#MAX_DEPTH_LEVEL = 2
#start_path = []
#path = []
"""
I know this uses recursion
I know this is O(2^MAX_LEVEL_DEPTH*n)
I'M SORRY
Will fix with bidirectional BFS or something

Update: uses priority queue/BFS
Bad news: Twitter API limits number of requests
As in, if we look at beyonce's followee's followee's, 
we exceed the rate limit request.

(Cry cry cry, using extremely limited temp graph instead)
"""

def find_shortest_path(start_username, end_username, path):
    graph = {'weatherdsouls': ['katkatstarke'],
             'katkatstarke': ['CoryBooker'],
             'CoryBooker': ['HillaryClinton'],
             'takis_metaxas': ['TakisProblems'],
             'TakisProblems': ['LILBTHEBASEDGOD'],
             'LILBTHEBASEDGOD': ['chancetherapper'],
             'MariahCarey': ['justinbieber'],
             'solangeknowles': ['MariahCarey'],
             'beyonce': ['solangeknowles']
    }

    path += [start_username]
    q = Queue.Queue()
    q.put(path)
    visited = set()
    visited.add(start_username)
    while not q.empty():
        path = q.get()
        last = path[-1]
        if last == end_username:
            return path
        for node in graph[last]:
            try:
                print node
                if node not in visited:
                    visited.add(node)
                    q.put(path + [node])
            except Exception, e:
                print e
                continue 
#print find_shortest_path(graph, 'beyonce', 'sravanti', [])

user_names = []
user_follower_counts = []
user_handles = []
user_profiles = []
def users_info(follower_chain):
    try:
        users = []
        user_names = []
        user_follower_counts = []
        user_handles = []
        user_profiles = []
        for user in follower_chain:
            user = api.get_user(user)
            users.append(user)
            user_names.append(user.name)
            user_follower_counts.append(user.followers_count)
            user_profiles.append(user.profile_image_url)
            user_handles.append(user.screen_name)
    except Exception, e:
        print e
        pass
    return [user_names, user_follower_counts, user_handles, user_profiles] 
    """
    print user_names
    print user_follower_counts
    print user_handles
    print user_profiles
    return users
    """
def user_names(follower_chain):
    return user_names

def user_follower_counts(follower_chain):
    return user_follower_counts

def user_handles(follower_chain):
    return user_handles

def user_profiles(follower_chain):
    return user_profiles


"""       
    followers = tweepy.Cursor(api.friends_ids, id=start_username).items()
    for follower in followers:
        try:
            queue.put(follower)
            while not queue.empty:
                current = queue.pop(0)
                if follower == end_username:
                print "equal"
                path += [end_username]
                return path
            else:
                print "not equal"
                return find_shortest_path(follower, end_username, path, depth)
        except Exception, e:
            print e
            continue 
    """

