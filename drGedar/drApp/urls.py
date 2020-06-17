from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('blog/',views.blog,name='blog'),
   path('contact/',views.contact,name='contact'),
   path('gallery/',views.gallery,name='gallery'),
   path('get_query/',views.get_query,name='get_query'),
   path('contact_form/',views.contact_form,name='contact_form'),
   path('comment_form/',views.comment_form,name='comment_form'),
   path('<slug>/',views.cat,name='cat'),
   path('blog/<slug:slug>/',views.blog_detail,name='blog_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)