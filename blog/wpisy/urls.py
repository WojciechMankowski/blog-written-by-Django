from django.urls import path
from wpisy.views import Home, About, post_detail, Send_messege

urlpatterns = [
    path("", Home, name="Home"),
    path("omnie", About, name="O mnie"),
    path("kontakt", Send_messege),
    path("<int:id>", post_detail, name="post_detail"),
]
