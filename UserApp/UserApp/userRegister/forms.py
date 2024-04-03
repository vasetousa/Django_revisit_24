from django.contrib.auth import forms as auth_forms, get_user_model

from UserApp.userRegister.models import Profile

UserModel = get_user_model()

''' In views, use directly UserCreationForm as a form or create your own form, inheriting from UserCreationForm '''


# Username was changed to email. Now email is the username used to log in
class UserRegistrationForm(auth_forms.UserCreationForm):
    # if any other field must be shown or changed, add class Meta
    class Meta:
        model = UserModel
        fields = ('email',)

    # extend with other methods
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        # If we want to create a profile while registering the user.
        profile = Profile.objects.create(
            user=user,
            first_name=self.cleaned_data.get('first_name', '..........'),
            last_name=self.cleaned_data.get('last_name', '..........'),
            date_of_birth=self.cleaned_data.get('date_of_birth', None),
            phone_number=self.cleaned_data.get('phone_number', '..........'),
        )

        return user
