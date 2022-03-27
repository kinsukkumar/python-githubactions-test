from django.urls import path
#from .views import (
#    PostListView,
#    PostDetailView,
#    PostCreateView,
#    PostUpdateView,
#    PostDeleteView,
#    UserPostListView
#)
from . import views

urlpatterns = [
    path('', views.homepage, name='web-home'),
    path('userPermission', views.userPermission, name='home-userpermission'),
   #path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
   #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   #path('post/new/', PostCreateView.as_view(), name='post-create'),
   #path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('dashboard/reconciliation', views.dashboard_reconciliation, name='dashboard-reconciliation'),
   path('dashboard/userPermission', views.userPermission, name='dashboard-userpermission'),
   path('submitBOT/approval', views.submitBOT_submission, name='submitBOT-submission'),
   path('submitBOT/userPermission', views.userPermission, name='submitBOT-userpermission'),
   path('submitBOT/approvalresult', views.submitBOT_entitystatus, name='submitBOT-entitystatus'),
  
]