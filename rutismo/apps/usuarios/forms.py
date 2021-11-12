from django import forms


from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.core.files.images import get_image_dimensions
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class formularioLogin(AuthenticationForm):
    
    class Meta:
        model:CustomUser
    
    def __init__(self,*args,**kwargs):
        super(formularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
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

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


# class formularioUsuario(UserCreationForm):
#     class Meta:
#         model:CustomUser
#         fields = ['username','email','avatar','password']
    
#     def __init__(self,*args,**kwargs):
#         super(formularioUsuario,self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class']= 'form-control'
#         self.fields['username'].widget.attrs['placeholder']= 'Nombre de Usuario'
#         self.fields['email'].widget.attrs['class']= 'form-control'
#         self.fields['email'].widget.attrs['placeholder']= 'Correo Electronico'
#         self.fields['avatar'].widget.attrs['class']= 'form-control'
#         self.fields['avatar'].widget.attrs['placeholder']= 'Avatar'
#         self.fields['password'].widget.attrs['class']= 'form-control'
#         self.fields['password'].widget.attrs['placeholder']= 'Contraseña'
        
  
