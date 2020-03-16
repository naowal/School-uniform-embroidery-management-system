from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import StudentEmbInfo, user
from .forms import StudentEmbInfoForm, userForm


class StudentEmbInfoListView(ListView):
    model = StudentEmbInfo


class StudentEmbInfoCreateView(CreateView):
    model = StudentEmbInfo
    form_class = StudentEmbInfoForm


class StudentEmbInfoDetailView(DetailView):
    model = StudentEmbInfo


class StudentEmbInfoUpdateView(UpdateView):
    model = StudentEmbInfo
    form_class = StudentEmbInfoForm


class userListView(ListView):
    model = user


class userCreateView(CreateView):
    model = user
    form_class = userForm


class userDetailView(DetailView):
    model = user


class userUpdateView(UpdateView):
    model = user
    form_class = userForm

