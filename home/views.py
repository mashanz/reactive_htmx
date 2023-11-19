from django.shortcuts import render


# Create your views here. well, ini cuma index 🧪
def index(request):
    return render(request, "home/index.html", {'MENU': ""})


# SSR Component LOL 🤣
def components(request):
    q = request.GET.get("q")
    return render(request, f"home/components/{q}.html")


# SSR Content LOL 🤣
def contents(request):
    q = request.GET.get("q")
    print(q)
    context ={'MENU': q}
    return render(request, f"home/contents/{q}.html", context)
