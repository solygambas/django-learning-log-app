from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # model used for the form
        fields = ['text']
        labels = {'text': ''} # no label

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry # model used for the form
        fields = ['text']
        labels = {'text': ''} 
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # 40 by default