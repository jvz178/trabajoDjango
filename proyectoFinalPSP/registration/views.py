from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name="registration/registro.html"

    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    
    def get_form(self,form_class=None):
        form=super(SignupView,self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb2',
                                         'placeholder':'Introduce el nombre de usuario'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb2',
                                                    'placeholder':'Introduce una contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb2',
                                        'placeholder':'Introduce la contraseña de nuevo'})

        return form