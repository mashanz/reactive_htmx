from django.shortcuts import render
from django.template import engines
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token

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

# Reactive Forma LOL 🤣
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def reactive(request):
    #object_lists = []

    if request.method == 'POST':
        object_lists.append({
            "id": 0,
            "type": "text",
            "label": "label",
            "placeholder": "Placeholder Text",
            "helper_text": "Helper Text",
        })
    elif request.method == 'DELETE':
        object_lists.pop(request.GET.get("id"))

    str_template = ""
    csrf_token = get_token(request)
    csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
    for ol in object_lists:
        str_template += f"""
        <div>
            <div>
                <label for='form_{ol['id']}'><b>{ol['label']}</b></label>
            </div>
            <input 
                type='{ol['type']}' 
                id='form_{ol['id']}' 
                name='form_{ol['id']}' 
                placeholder='{ol['placeholder']}'>
            <div>
                <i>{ol['helper_text']}</i>
            </div>
            <form hx-delete="/reactive/?id={ol['id']}" hx-triger="submit" hx-target="#object_lists">
                {csrf_token_html}
                <button class="btn btn-danger" type="submit">
                    DELETE
                </buton>
            </form>
        </div>
        """

    print(object_lists)
    django_engine = engines["django"]
    template = django_engine.from_string(str_template)
    return HttpResponse(template.render())
