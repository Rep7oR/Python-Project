from django.conf import settings
from django.conf.urls.static import static

from. import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='test'),
    path('home/', views.tasklistview.as_view(),name='home'),
    path('detail/<int:pk>/',views.taskdetailview.as_view(),name='detail'),
    path('delete/<int:pk>/',views.taskdelete.as_view(),name='delete'),
    path('edit/<int:pk>/', views.taskupdate.as_view(),name='update'),
    # path('update/<int:id>',views.update,name='update'),
    # path('delete/<int:id>/', views.delete,name='delete')
    ]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
