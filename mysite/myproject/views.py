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
        user_path = degrees.users_info(degrees.find_shortest_path(user1, user2, []))
        print user_path
        return render(request,'index.html', {'users': user_path})
