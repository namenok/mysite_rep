from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text', ]
        labels = {'text': 'Topic name'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', ]
        labels = {'text': 'Entry text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(label='Your email')
