from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.contrib.auth.views import login, logout
from list.views import TodoListView, TodoListCreate, TodoListDelete, toogle_todo,UserViewSet,GroupViewSet, TodoListViewSet
from .serializers import UserSerializer, GroupSerializer, TodoListSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'todolist-api', TodoListViewSet)


urlpatterns = [
    url(r'^$', TodoListView.as_view(), name='index'),
    url(r'create_todo', TodoListCreate.as_view(), name='create_todo'),
    url(r'delete_todo/(?P<pk>\d+)/$', TodoListDelete.as_view(), name='delete_todo'),
    url(r'toogle_todo/(?P<pk>[0-9]+)/$', toogle_todo, name='toogle_todo'),
    url(r'create_user', views.create_user, name='create_user'),
    url(r'^accounts/login/$', login,
       {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', logout,  {'next_page': '/list'}),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]