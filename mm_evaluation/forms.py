
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms
from django.utils.translation import gettext_lazy as _

from .models import PYME, FinancesInformation, VALID_EMPLOYEES_NUMBER, VALID_ASSETS, VALID_PRODUCTIVE_CONFIGURATION, VALID_INVENTORY_POLITICS


class PYMERegistrationForm(forms.ModelForm):
    """Form to create PYME information in registration form.

    Inherits from ModelForm, and uses PYME model. This form will hold information related to the PYME model, 
    except for User field, which will be managed using UserRegistrationForm. This localizes `contact_birth_date`. 

    Fields:
        name (forms.CharField):
        sector (forms.ModelChoiceField): displays with a select widget.
        nit (forms.CharField):
        address (forms.CharField):
        phone_number (forms.CharField):
        contact_sex (forms.CharField):
        contact_phone_number (forms.CharField):
        contact_birth_date (forms.DateField): displays with a text widget.
        contact_id_type (forms.CharField): displays with a select widget.
        contact_id_number (forms.CharField):
        contact_time_on_charge (forms.IntegerField):
        contact_education_level (forms.CharField): displays with a select widget.
        terms_conditions_acceptance (forms.BooleanField): display as a click box widget.
        
    """

    class Meta:
        # Create form fields according to fields in PYME model
        model = PYME
        # Do not create a field for User object. In registration page, User form fields are created using UserRegistrationForm defined below
        exclude = ("user",)
        localized_fields = ("contact_birth_date",)
        # Specify labels for each field
        labels = {
            "name": _("Nombre de la empresa"),
            "sector": _("Sector"),
            "nit": _("NIT de la empresa"),
            "address": _("Dirección de la empresa"),
            "phone_number": _("Teléfono"),
            "contact_sex": _("Sexo"),
            "contact_phone_number": _("Número telefónico o celular"),
            "contact_birth_date": _("Fecha de nacimiento"),
            "contact_id_type": _("Tipo del documento"),
            "contact_id_number": _("Número del documento"),
            "contact_time_on_charge": _("Años que lleva a cargo"),
            "contact_education_level": _("Nivel de educación"),
            "terms_conditions_acceptance": _("Aceptación de Términos y Condiciones"),
        }


class UserRegistrationForm(UserCreationForm):
    """Form to create User information in registration page.

    Inherits from UserCreationForm, and uses Django's User model. Since `password1` and `password2`
    (i.e. password and password confirmation) are not fields of User model, they are created in this form. 
    Labels for each field are defined in order to display form in spanish.

    Fields:
        username (forms.CharField): username to be created in registration page.
        email (forms.CharField): email to be created in registration page.
        first_name (forms.CharField):
        last_name (forms.CharField):
        password1 (forms.CharField): password to be created in registration form.
        password2 (forms.CharField): password confirmation.

    """

    # Predefined error messages
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    # Since password is not a field in User model, one has to create a form field for this
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Ingrese nuevamente su contraseña"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        # Create form fields according to fields in PYME model
        model = User
        # Specify User model fields to use
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
        # Specify labels for each field
        labels = {
            "username": _("Nombre de usuario"),
            "email": _("Correo electrónico"),
            "first_name": _("Nombres"),
            "last_name": _("Apellidos"),
        }


class FinancesInformationForm(forms.ModelForm):
    """Form to create a Finances form.

    Inherits from ModelForm, and uses Django's FinacesInformation model.
    Labels for each field are defined in order to display form in spanish.

    Fields:
        employees_number (forms.ChoiceField): is the number of current employees in the company.
        anual_income (forms.BigIntegerField): is the anual income of a company in Colombian pesos.
        assets (forms.ChoiceField): are the assets of the company in Colombian pesos.
        liabilities (forms.IntegerField): are the liabilities of the company in Colombian pesos.
        monthly_production (forms.BigIntegerField): is the monthly production of the company in units or Colombian pesos.
        productive_configuration (forms.ChoiceField): is the productive configuration of the company.
        inventory_politics (forms.ChoiceField): are the inventory politics of the company.
        main_product (forms.CharField): is the main product the company sells.
        main_competidor (forms.CharField): is the main competidor of the company.
        patrimony (forms.BigIntegerField): is the patrimony of the company in Colombian pesos.
        sales_income (froms.BigIntegerField): is the sales income of the company in Colombian pesos.
        gross_profits (forms.BigIntegerField): are the gross profit of the company in Colombian pesos.
        net_profits (forms.BigIntegerField): are the net profits of the company in Colombian pesos.
        fixed_costs_expences (models.BigIntegerField): are the fixed cost and expenses of the company
        variable_costs_expences (forms.BigIntegerField): are the variable costs and expences of the company.
        ebitda (forms.IntegerField):is the EBITDA of the company

"""
    
    class Meta:
        model = FinancesInformation
        fields = [
            "employees_number",
            "anual_income",
            "assets",
            "liabilities",
            "monthly_production",
            "productive_configuration",
            "inventory_politics",
            "main_product",
            "main_competidor",
            "patrimony",
            "sales_income",
            "gross_profits",
            "net_profits",
            "fixed_costs_expences",
            "variable_costs_expences",
            "ebitda"
        ]

        labels = {
            "employees_number":_("Número de empleados"),
            "anual_income":_("Ingreso anual"),
            "assets":_("Activos"),
            "liabilities":_("Pasivos"),
            "monthly_production":_("Producción mensual"),
            "productive_configuration":_("Configuración productiva"),
            "inventory_politics":_("Políticas de inventario"),
            "main_product":_("Producto principal"),
            "main_copetidor":_("Competencia principal"),
            "patrimony":_("Patrimonio"),
            "sales_income":_("Ingresos de ventas"),
            "gross_profits":_("Ganacia bruta"),
            "net_profits":_("Ganacia neta"),
            "fixed_costs_expences":_("Costos y gastos fijos"),
            "variable_costs_expences":_("Costos y gastos varibales"),
            "ebitda":_("EBITDA"),
        }
