from django.urls import path
from .views import index, pagination

urlpatterns = [
    path("", index, name="index"),
    path("search/<query>/page/<page_number>", pagination, name="pagination"),
]
