from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.PhotoUpload.as_view(), name="upload_photo"),
    url(r'^(?P<file_name>[a-zA-Z0-9_]+)/$',views.PhotoUpload.as_view(), name="upload_photo"),
    #url(r'^delete/$',views.PhotoDelete.as_view(), name="delete_photo")
]