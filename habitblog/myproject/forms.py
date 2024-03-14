from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['field1', 'field2']     # 'field1', 'field2' 등은 Habit 모델의 필드 이름이다.
