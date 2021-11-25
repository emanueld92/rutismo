from django import forms
from django.forms import ModelForm


from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.core.files.images import get_image_dimensions
from django.forms.models import fields_for_model
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class formularioLogin(AuthenticationForm):
    
    class Meta:
        model=CustomUser
    
    def __init__(self,*args,**kwargs):
        super(formularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder']= 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class']= 'form-control'
        self.fields['password'].widget.attrs['placeholder']= 'Contraseña'
         
    
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'archivo no puede superar los 20kb.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields.pop('password')
        # self.fields.pop('is_staff')
        # self.fields.pop('last_login')
        # self.fields.pop('date_joined')
        # self.fields.pop('groups')
        # self.fields.pop('is_active')
        # self.fields.pop('user_permissions')
        # self.fields.pop('is_superuser')
        
    

    class Meta:
        model = CustomUser
        fields = ('email',
                  'password',
                  'avatar',
                  'first_name',
                  'last_name')
        labels = {  # Esto nos permite renderisar los label con codigo python y no html
            'email': 'Correo Electronico',
            'password': 'Contraseña',
            'Avatar': 'Foto',
            'first_name': 'Nombre',
            'last_name': 'Apellido',


        }
        widgets = {  # los Widgets te permiten darle estilo a nuestros imput y attrs son los atributos de imput
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Correo electronico',
                    'id': 'email',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password1',

                }
            ),

            'Avatar': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'avatar',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id':'first_name',

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Apellido',
                    'id': 'last_name',
                }
            )
            

        }




