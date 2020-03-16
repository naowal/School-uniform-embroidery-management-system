from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'studentembinfo', api.StudentEmbInfoViewSet)
router.register(r'user', api.userViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for StudentEmbInfo
    path('Studentemb/studentembinfo/', views.StudentEmbInfoListView.as_view(), name='Studentemb_studentembinfo_list'),
    path('Studentemb/studentembinfo/create/', views.StudentEmbInfoCreateView.as_view(), name='Studentemb_studentembinfo_create'),
    path('Studentemb/studentembinfo/detail/<slug:slug>/', views.StudentEmbInfoDetailView.as_view(), name='Studentemb_studentembinfo_detail'),
    path('Studentemb/studentembinfo/update/<slug:slug>/', views.StudentEmbInfoUpdateView.as_view(), name='Studentemb_studentembinfo_update'),
)

urlpatterns += (
    # urls for user
    path('Studentemb/user/', views.userListView.as_view(), name='Studentemb_user_list'),
    path('Studentemb/user/create/', views.userCreateView.as_view(), name='Studentemb_user_create'),
    path('Studentemb/user/detail/<slug:slug>/', views.userDetailView.as_view(), name='Studentemb_user_detail'),
    path('Studentemb/user/update/<slug:slug>/', views.userUpdateView.as_view(), name='Studentemb_user_update'),
)

