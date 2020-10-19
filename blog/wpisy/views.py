from django.shortcuts import render, get_object_or_404
from wpisy.models import Post, kontakt
from wpisy.forms import Kontakt


def Home(request):
    lista_postow = Post.objects.order_by("-published_date")
    return render(request, "index.html", {"lista_postow": lista_postow})


def About(request):
    return render(request, "about.html")


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "post.html", {"post": post})


def Send_messege(request):
    form = Kontakt(request.GET)
    if request.method == "POST":
        form = Kontakt(request.POST)
        if form.is_valid():
            kontakt.objects.create(**form.cleaned_data)
    else:
        form = Kontakt()
    return render(request, "kontakt.html", {"form": form})
