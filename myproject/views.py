from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import degrees
@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        user1 = request.POST["user1"]
        user2 = request.POST["user2"]
        user_path = degrees.users_info(degrees.find_shortest_path(user1, user2,[]))
        user_names = user_path[0]
        user_follower_counts = user_path[1]
        user_handles = user_path[2]
        user_profiles = user_path[3]
        return render(request,'index.html', {'user_names': user_names,
                                             'user_follower_counts':user_follower_counts,
                                             'user_handles': user_handles,
                                             'user_profiles': user_profiles})
