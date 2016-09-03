from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def signup(request):
    context = {}
    return render(request, 'login/signup.html', context)

def login(request):
    if request.user.is_authenticated():
        return redirect("login:index")
    return render(request, "login/signup.html", {})
