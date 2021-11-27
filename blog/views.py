from django.shortcuts import render

# Create your views here.
def post_list(request):
    print(request)
    return render(request, "blog/post_list.html", {})

def otra(request):
    return render(request, "blog/otra.html", {})