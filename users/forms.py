from django import forms

from users.models import Profile


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeHolder':'First Name'}),
            'last_name': forms.TextInput(attrs={'placeHolder': 'Last Name'}),
            'bio': forms.TextInput(attrs={'placeHolder': 'Bio'}),
        }

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Save your profile
        profile = Profile()
        profile.user = user
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.bio = self.cleaned_data['bio']
        profile.save()