from django import forms
from .models import Group, GroupMember


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description', )
