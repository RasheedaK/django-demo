from django.forms import ModelForm
from polls.models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']