from django.urls import path
from electronica.views import (
    create_electronica_view,
    read_electronica_view,
    update_electronica_view,
    delete_electronica_view
)

urlpatterns = [
    path('create_electronica/', create_electronica_view, name='create'),
    path('electronica_list/', read_electronica_view, name='read'),
    path('electronica_list/<int:id>/update/', update_electronica_view, name='update'),
    path('electronica_list/<int:id>/delete/', delete_electronica_view, name='delete'),
]
