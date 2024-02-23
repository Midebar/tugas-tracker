from django.urls import path
from .views import main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user

app_name = "main"

urlpatterns = [
    path('', main, name='main'),
    path('create-book', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]