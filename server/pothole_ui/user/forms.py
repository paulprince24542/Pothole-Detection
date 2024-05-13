# from django import forms
# from .models import User

# class UserForm(forms.ModelForm):
#     # name = forms.CharField(label='Name', max_length=100)
#     # email = forms.CharField(label='Email', max_length=100)
#     # image = forms.FileField()
#     class Meta:
#         model = User
#         fields = ('name', 'email', 'image')
#     widgets = {
#         'image': forms.FileInput(attrs={'multiple': True, 'allow_multiple_selected': True})
#     }