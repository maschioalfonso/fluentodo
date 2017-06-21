from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from .models import TodoList
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, TodoListSerializer


class TodoListView(ListView):
    model = TodoList

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TodoListView, self).dispatch(request, *args, **kwargs)

class TodoListCreate(CreateView):
    model = TodoList
    fields = ['name']
    success_url = reverse_lazy('index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TodoListCreate, self).dispatch(request, *args, **kwargs)

class TodoListDelete(DeleteView):
    model = TodoList

    def get_success_url(self, **kwargs):
        return reverse('index') + "?just_delete_name=" + self.object.name

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TodoListDelete, self).dispatch(request, *args, **kwargs)

def TodoListUpdate(UpdateView):
    model = TodoList
    fields = ['name']
    template_name_suffix = '_update_form'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TodoListUpdate, self).dispatch(request, *args, **kwargs)

@login_required
@require_http_methods(["POST"])
def toogle_todo(request, pk):
    item = TodoList.objects.get(pk=pk)
    item.completed = not item.completed
    item.save()
    return HttpResponseRedirect('/list')


# This is really bad, the UserStory said
# "must register with the system.". I suggest to implement
# a Oauth, like auth0 Authtenticator.
@require_http_methods(["GET", "POST"])
def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list')
    return render(request, 'list/create_user.html', {'form': form})

# Rest API
#
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
