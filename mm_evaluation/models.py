from django.db import models

# Create your models here.
class Pyme(models.Model):
    sector_id = models.ForeingKey(sector, on_delet=models.CASCADE)
    username = models.CharField(max_length=80)
    pyme_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nit = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    contact_name = models.Charfield(max_length=100)
    contact_sex = models.CahrField(max_length=10)
    contact_birth_day = models.DateTimeField()
    contact_id_type = models.CharField(max_length=30)
    contact_id_number = models.CharField(max_length=15)
    contact_education_level = models.CharField(max_length=40)
    terms_conditions_acceptance = models.BooleanField()
    contact_time_on_charge = models.IntergerField()

    class Meta:
        db_table = 'pyme'


class Archive(models.Model):
    pyme_id = models.ForeingKey(pymes,on_delet=models.CASCADE)
    file_ = models.FileField()
    type_ = models.CharField(max_length=10)
    file_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'archive'


class Sector(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)

    class Meta(models.Model):
        db_table = 'sector'


class FinancesInformation(models.Model):
    pyme_id = models.ForeingKey(pyme,on_delet=models.CASCADE)
    employees_number = models.IntergerField()
    anual_income = models.BigIntergerField()
    assets = models.BigIntegerField()
    liabilities = models.IntergerField()
    monthly_production = models.IntegerField()  
    productive_configuration = models.CharField()
    inventory_politics = models.CharField(max_length=100)
    main_product = models.CharField(max_length=30)
    main_competidor = models.CharField(max_length=30)
    patrimony = models.BigIntegerField()
    sales_income = models.BigIntegerField()
    gross_profit = models.BigIntegerField()
    net_profits = models.BigIntegerField()
    fixed_costs_expences = models.BigIntegerField()
    variable_costs_expences = models.BigIntegerField()
    ebitda = models.IntegerField()

    class Meta:
        db_table = 'finances_information'
