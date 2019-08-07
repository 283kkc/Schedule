from django import forms
from .models import Staff, Entry

class PostForm(forms.Form):
    staff = forms.ModelChoiceField(
        queryset=Staff.objects.all(),
        label='スタッフを選択してください',
        error_messages={'required': '選択されていません。'},
    )

    choice = forms.ChoiceField(
        label='選択してください',
        choices=((0, "出社"), (1, "退社")),
        widget=forms.RadioSelect,
        error_messages={'required': '選択されていません。'},
    )

class EndForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('timeOfBreak',)