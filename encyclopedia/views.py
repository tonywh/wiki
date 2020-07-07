from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from . import util
import markdown2
from random import randrange

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    q = request.GET.get("q")
    if not q:
        raise Http404("Page not found")

    q = q.lower()

    # Get search result
    entries =  util.list_entries()

    # Check for exactly 1 exact match
    results = list(filter(lambda title: title.lower() == q, entries))
    if len(results) == 1:
        return HttpResponseRedirect(f"wiki/{results[0]}")

    # Check for part matches
    results = list(filter( lambda title: title.lower().find(q) >= 0, entries))
    return render(request, "encyclopedia/results.html", {
        "entries": results
    })

def random(request):
    # View random page
    entries =  util.list_entries()
    i = randrange(len(entries))
    return HttpResponseRedirect(f"wiki/{entries[i]}")

def wiki(request, title):
    # View a web page
    md = util.get_entry(title)
    if md == None:
        raise Http404("Topic does not exist.")        
    #return HttpResponse(markdown2.markdown(md))
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(md)
    })

def edit(request, title):
    if request.method == "GET":
        # Get web page to edit an entry
        pass

    # Post edited page for storage and display
    pass