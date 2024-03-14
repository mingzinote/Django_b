from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,
DeleteView
from .models import Habit
from .forms import HabitForm

class HabitListView(ListView):
    model = Habit
    template_name = 'habits/habit_list.html'
    context_object_name = 'habits'

    
class HabitCreateView(DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'
    context_object_name = 'habit'


class HabitCreateView(CreateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'
    success_url = reverse_lazy('habit_list')


class HabitUpdateView(UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'
    success_url = reverse_lazy('habit_list')

class HabitDeleteView(DeleteView):
    model = Habit
    template_name = 'habits/habit_confirm_delete.html'
    context_object_name = 'habit'
    success_url = reverse_lazy('habit_list')


# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # 등록 후 리다이렉트 될 URL
    template_name = 'registration/signup.html'  # 사용할 템플릿 경로


from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserChangeForm()
    return render(request, 'users/register.html', {'form': form})

