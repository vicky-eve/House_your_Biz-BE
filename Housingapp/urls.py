from django.urls import path
from . import views

urlpatterns= [
    path('api/tenant/', views.TenantList.as_view()),
    path('api/user/', views.UserList.as_view()),
    path('api/comment/', views.CommentList.as_view()),
    path('api/house/', views.HouseList.as_view()),
    path('api/merch/tenant-id/(?P<pk>[0-9]+)/',views.TenantDescription.as_view()),
    path('api/merch/user-id/(?P<pk>[0-9]+)/',views.UserDescription.as_view()),
    path('api/merch/comment-id/(?P<pk>[0-9]+)/',views.CommentDescription.as_view()),
    path('api/merch/house-id/(?P<pk>[0-9]+)/',views.HouseDescription.as_view()),
]
