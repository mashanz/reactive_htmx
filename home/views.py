from django.shortcuts import render
from django.template import engines
from django.http import HttpResponse

# make it global because I am lazy to install/config redis here, well harus nya ini di masukin ke redis LOL 🤣
object_lists = []

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
    context ={'MENU': q}
    return render(request, f"home/contents/{q}.html", context)

def render_html(obj):
    str_template = ""
    for ol in obj:
        str_template += f"""
        <div class="card bg-base-100 p-4">
            <div class="p-2">
                <label for='form_{ol['id']}'><b>{ol['label']}</b></label>
            </div>
            <input 
                class="input outline"
                type='{ol['type']}' 
                id='form_{ol['id']}' 
                name='form_{ol['id']}' 
                placeholder='{ol['placeholder']}'>
            <div class="p-2">
                <i>{ol['helper_text']}</i>
            </div>
            <button class="btn btn-error" hx-get="/reactive/delete/?id={ol['id']}" hx-target="#object_lists">
                DELETE
            </buton>
        </div>
        """

    django_engine = engines["django"]
    template = django_engine.from_string(str_template)
    return HttpResponse(template.render())

# Delete ADD
def reactive_add(request):
    object_lists.append({
        "id": 0,
        "type": "text",
        "label": "label",
        "placeholder": "Placeholder Text",
        "helper_text": "Helper Text",
    })
    return render_html(object_lists)

# Delete
def reactive_delete(request):
    object_lists.pop(int(request.GET.get("id")))
    return render_html(object_lists)

# Reactive Form LOL 🤣
def reactive_get(request):
    return render_html(object_lists)
