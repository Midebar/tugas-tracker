from django.urls import path
from .views import (
    main, create_item, edit_item, delete_item, create_item_ajax,
    show_json, show_json_by_id, 
    show_xml, show_xml_by_id, 
    register, login_user, logout_user, create_item_flutter)

app_name = "main"

urlpatterns = [
    path('', main, name='main'),
    path('create-item', create_item, name='create_item'),
    path('create-item-ajax', create_item_ajax, name='create_item_ajax'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete-item/<int:id>', delete_item, name='delete_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-flutter/', create_item_flutter, name='create_book_flutter'),
]