from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms
from django.utils.translation import gettext_lazy as _

from .models import PYME

class PYMERegistrationForm(forms.ModelForm):
    class Meta:
        model = PYME
        exclude = ('user',)
        localized_fields = ('contact_birth_date',)

        labels = {
            'pyme_name': _('Nombre de la empresa'),
            'sector_id': _('Nombre del sector económico al cual pertenece la empresa'),
            'nit': _('NIT de la empresa'),
            'address': _('Dirección de la empresa'),
            'phone_number': _('Número telefónico de la empresa'),
            'contact_sex': _('Sexo del contacto de la empresa'),
            'contact_phone_number': _('Número telefónico del contacto de la empresa'),
            'Contact_birth_date': _('Fecha de nacimiento del contacto de la empresa'),
            'contact_id_type': _('Tipo del documento del contacto de la empresa'),
            'contact_id_number': _('Número del documento del contacto de la empresa'),
            'contact_time_on_charge': _('Tiempo que lleva a cargo el contacto de la empresa'),
            'contact_education_level': _('Nivel de educación del contacto de la empresa'),
            'terms_conditions_acceptance': _('Aceptación de Términos y Condiciones'),
        }

        

class UserRegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Ingrese nuevamente su contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

        labels = {
            'username': _('Nombre de usuario'),
            'email': _('Ingrese el correo electrónico del contacto de la empresa'),
            'first_name': _('Nombres del contacto de la empresa'),
            'last_name': _('Apellidos del contacto de la empresa'),
        }
