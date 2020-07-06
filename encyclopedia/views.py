from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from . import util
import markdown2

def index(request):
    q = request.GET.get("q")
    if q:
        return searchWiki(request, q)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def searchWiki(request, q):
    q = q.lower()

    # Get search result
    entries =  util.list_entries()

    # Check for exactly 1 exact match
    results = list(filter(lambda title: title.lower() == q, entries))
    if len(results) == 1:
        return HttpResponseRedirect(f"wiki/{results[0]}")

    # Check for part matches
    results = filter( lambda title: title.lower().find(q) >= 0, entries)
    return render(request, "encyclopedia/results.html", {
        "entries": list(results)
    })

def random(request):
    # View random page
    pass

def wiki(request, title):
    # View a web page
    md = util.get_entry(title)
    if md == None:
        raise Http404("Topic does not exist.")        
    return HttpResponse(markdown2.markdown(md))

def edit(request, title):
    if request.method == "GET":
        # Get web page to edit an entry
        pass

    # Post edited page for storage and display
    pass