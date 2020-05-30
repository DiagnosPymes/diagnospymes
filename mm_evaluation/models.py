from django.contrib.auth.models import User
from django.db import models


VALID_SCORES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        ]
"""Valid scores for answer instances."""

VALID_MACROPROCESS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        ]
"""Valid macroprocesses number."""

VALID_ID_TYPE = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ]
"""Valid ID type for PYME's contact."""

VALID_EDUCATION_LEVEL = [
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('tecnica', 'Técnica'),
        ('tecnologo', 'Tecnólogo'),
        ('universitario', 'Universitario'),
        ('posgrado', 'Posgrado'),
        ]
"""Valid education level for PYME's contact."""

VALID_EMPLOYEES_NUMBER = [
    ("<=10","Igual o menos de 10 empleados"),
    ("11-50","Entre 11 y 50 empleados"),
    ("51-200","Entre 51 y 200 empleados"),
    (">201","201 o mas empleados"),
    ("NS","No sabe/No conoce")
]
"""Valid Employees number for finances information"""

VALID_ASSETS = [
    ("<=500","Igual o inferior a 500 SMMLV"),
    ("501-500","Entre 501 y 5000 SMMLV"),
    ("5001-3000","Entre 5001 y 30000 SMMLV"),
    (">3000","Mas de 30000 SMMLV"),
    ("NS","No sabe/No conoce")
]
"""Valid Assets for finances information"""

VALID_PRODUCTIVE_CONFIGURATION = [
    ("PP","Por proyectos"),
    ("JS","Job Shop/Taller"),
    ("PL","Por lotes"),
    ("LEAE","Linea de ensamble acompasada por empleado"),
    ("LEAM","Linea de ensamble acompasada por maquina"),
    ("FC","Flujo continuo"),
    ("F","Flexible"),
    ("NS","No sabe/No conoce")
]
"""Valid Productive configuration for finances information"""

VALID_INVENTORY_POLITICS = [
    ("MTS","MTS: producir para inventario"),
    ("MTO","MTO: producir bajo pedido"),
    ("ATO","ATO: ensamblar bajo pedido"),
    ("ETO","ETO: hacer ingenieria bajo pedido"),
    ("PTO","PTO: pickear bajo pedido"),
    ("CTO","CTO: configurar planta bajo pedido"),
]
"""Valid inventory politics for finances information"""
    Every PYME has to be related to a Sector.

class Sector(models.Model):
    """
    Sector is the abstraction for economic sectors. Every PYME must be related to a Sector.
    """
    name        = models.CharField(help_text="Is the sector's name. Maximum is 20 characters.", max_length=20)
    description = models.CharField(help_text="Is the description of the sector. Maximum is 400 characters.", max_length=400)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'sector'


class PYME(models.Model):
    """
    This model contains general information related to the company. Must be related to a User instance and a sector
    """
    user                        = models.OneToOneField(User, help_text="It is a Foreign key with auth.models.User. Used to manage authentication and accounting.", on_delete=models.CASCADE)
    contact_sex                 = models.CharField(help_text="Is the sex of the company's contact. Maximum is 10 characters.", max_length=10)
    contact_phone_number        = models.CharField(help_text="Is the company's contact phone number. Maximum is 10 characters.", max_length=10)
    contact_birth_date          = models.DateField(help_text="Is the company's contact birthday.", )
    contact_id_type             = models.CharField(help_text="Is the company's contact id type. Maximum is 30 characters.", max_length=30, choices=VALID_ID_TYPE)
    contact_id_number           = models.CharField(help_text="Company's contact id number. Maximum is 15 characters.", max_length=15)
    contact_time_on_charge      = models.IntegerField(help_text="Is the company's contact time on charge.", )
    contact_education_level     = models.CharField(help_text="Is the company's contact education level. Maximum is 40 characters.", max_length=40,choices=VALID_EDUCATION_LEVEL)
    name                        = models.CharField(help_text="Refers to the name of the company. Maximum is 100 characters.", max_length=100)
    sector                      = models.ForeignKey(Sector, on_delete=models.CASCADE)
    nit                         = models.CharField(help_text="Refers to the tributary number of the company in Colombia. Maximum is 30 characters.", max_length=30)
    address                     = models.CharField(help_text="Is the company's general office address. Maximum is 50 characters.", max_length=50)
    phone_number                = models.CharField(help_text="Refers to the company's phone number. Maximum is 10 characters.", max_length=10)
    terms_conditions_acceptance = models.BooleanField(help_text="Depends on whether the PYME has accepted our Terms and Conditions or not.", )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pyme'


class Autoevaluation(models.Model):
    """
    This model contains the summary result autoevaluations. This model is related to only one PYME object and as many Answer instances as the number of Process instances in existence.
    """
    pyme                  = models.ForeignKey(PYME, on_delete=models.CASCADE)
    start_time            = models.DateField()
    last_time_edition     = models.DateField()
    final_score           = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_1_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_2_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_3_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_4_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_5_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_6_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_7_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_8_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_9_score  = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    macroprocess_10_score = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return 'Autoevaluation of {} last edited on {}'.format(self.pyme.name, self.last_time_edition)

    class Meta:
        db_table = 'autoevaluation'


class Macroprocess(models.Model):
    """
    This model contains general information of each Macroprocess.\
    This model contains the information regarding the different macroprocesses, which are 10 and describe the large \
    areas of concern when it comes to logistical performance.
    """

    name   = models.CharField(help_text="Is the name of the macroprocess. Maximum is 50 characters.", max_length = 50)
    number = models.IntegerField(help_text="Is the number identifying the macroprocess. ID is no sufficient\
            because of the following scenario: if one deleted the the first macroprocess and created it again, \
            querying the macroprocess with ID 1 would fail, and instead one would have to query ID 11 (as we\
            have always 10 macroprocesses). Having this field, one can query macroprocess with number 1, and\
            it will always be the one we expect. Also, IDs depends on the order in which macroprocesses were added\
            to the database. This field makes our lives easier.", choices=VALID_MACROPROCESS, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'macroprocess'
        ordering = ['number']


class Process(models.Model):
    """
    Saves each Process's information. This is the model where general information related to each process is stored. This will be used when creating Answer instances for autoevaluations.
    """
    macroprocess     = models.ForeignKey(Macroprocess, on_delete=models.CASCADE)
    name             = models.CharField(help_text="Makes reference to the process's name. Maximum is 50 characters.", max_length=50, default='')
    description      = models.CharField(help_text="Makes reference to the process's description. Maximum is 500 characters.", max_length=500)
    guiding_question = models.CharField(help_text="When answering the autoevaluation, this field will be used to help \
            the user this process's maturity level. Maximum is 400 characters.", max_length=400,default=' ')
    weight           = models.FloatField(help_text="Is needed when computing the macroprocess score.", )

    @property
    def sorted_specificpractices(self):
        return list(self.specificpractice_set.order_by('score'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'process'


class Answer(models.Model):
    """
    Saves needed information to store the score related to a Process and an Autoevaluation When a process is evaluated in an autoevaluation, an instance of the Answer model will be created.
    """
    process        = models.ForeignKey(Process, on_delete=models.CASCADE)
    autoevaluation = models.ForeignKey(Autoevaluation, on_delete=models.CASCADE)
    score          = models.IntegerField(help_text="Is the score given by the user.", choices=VALID_SCORES)

    def __str__(self):
        return 'Answer from {} to "{}" in autoevalution with id {}'.format(self.autoevaluation.pyme.name, self.process, self.autoevaluation.id)

    class Meta:
        db_table = 'answer'
        constraints = [
                models.UniqueConstraint(fields=['autoevaluation', 'process'], name='unique_answer'),
                ]


class SpecificPractice(models.Model):
    """
    Saves SpecificPractice instances related information. This table contains the information regarding specific practices, which are directly related to each level of each process and are used to describe the behaviour of a certain level in each process.
    """
    process        = models.ForeignKey(Process,on_delete=models.CASCADE)
    score          = models.IntegerField(help_text="Score is the level of process this specific practive is related to, \
            it is a number between 0 and 5.", choices=VALID_SCORES)
    description    = models.CharField(help_text="Is a text field which contains a brief explanations of a particular\
            specific practice. Maximum is 400 characters.", max_length = 400)
    recommendation = models.CharField(help_text="Is a text which tells the user how to achieve the level of this \
            specific practice. Maximum is 400 characters.", max_length = 400)

    def __str__(self):
        return 'Specific practice for process {} on score {}'.format(self.process.name, self.score)

    class Meta:
        db_table = 'specific_practice'


class GeneralPractice(models.Model):
    """
    This model saves GeneralPractice instances information. This table contains the information regarding general practices, which are related to global levels of performance and are used to describe briefly the behaviour of a PYME in a given level.
    """
    name           = models.CharField(help_text="Refers to the name of the respective general practice level. Maximum is 40 characters.", max_length=40, default='')
    score          = models.IntegerField(help_text="Is the level of overall logistic performance this specific practive is related to,\
            it is a number between 0 and 5.", choices=VALID_SCORES)
    description    = models.CharField(help_text="Is a text field which contains a brief explanations of a particular general practice.\
            Maximum is 500 characters.", max_length = 500)
    recommendation = models.CharField(help_text="Is a text which tells you how to achieve the level of this general practice.\
            Maximum is 500 characters.", max_length = 500)

    def __str__(self):
        return 'General practice {} to score {}'.format(self.name, self.score)

    class Meta:
        db_table = 'general_practice'


class Archive(models.Model):
    """
    This model saves important information for each file. The class Archive is for making an Archive table in MariaDB.
    """
    pyme        = models.ForeignKey(PYME,on_delete=models.CASCADE)
    file_object = models.FileField(help_text="Is a file that the user attachs.", )
    file_type   = models.CharField(help_text="Is the type of the file attached. Maximum is 10 characters.", max_length=10)
    name        = models.CharField(help_text="Is the name of the file attached. Maximum is 40 characters.", max_length=40)

    def __str__(self):
        return 'File with name {} created by {}'.format(self.name, self.pyme.name)

    class Meta:
        db_table = 'archive'


class FinancesInformation(models.Model):
    """
    Saves finances information for each PYME registered. The class FinancesInformation is for making a finances information table in MariaDB. This hols general finances information for each PYME registered, and is mandatory that each PYME has at least one instance of this model.
    """
    
    pyme                     = models.ForeignKey(PYME, on_delete=models.CASCADE)
    employees_number         = models.CharField(help_text="Is the number of current employees in the company. Can be null and blank.", max_length=100, choices=VALID_EMPLOYEES_NUMBER, null=True, blank=True)
    anual_income             = models.BigIntegerField(help_text="Is the anual income of a company in Colombian pesos.Can be null and blank.", null=True, blank=True)
    assets                   = models.CharField(help_text="Are the assets of the company in Colombian pesos. Can be null and blank.", max_length=100, choices=VALID_ASSETS, null=True, blank=True)
    liabilities              = models.IntegerField(help_text="Are the liabilities of the company in Colombian pesos. Can be null and blank.", null=True, blank=True)
    monthly_production       = models.BigIntegerField(help_text="Is the monthly production of the company in units or Colombian pesos. Can be null and blank.", null=True, blank=True)
    productive_configuration = models.CharField(help_text="Is the productive configuration of the company. Maximum is 300 characters. Can be null and blank.", max_length=100, choices=VALID_PRODUCTIVE_CONFIGURATION, null=True, blank=True)
    inventory_politics       = models.CharField(help_text="Are the inventory politics of the company. Maximum is 100 characters. Can be null and blank.", max_length=100, choices=VALID_INVENTORY_POLITICS, null=True, blank=True)
    main_product             = models.CharField(help_text="Is the main product the company sells. Maximum is 30 characters. Can be null and blank.", max_length=30, null=True, blank=True)
    main_competidor          = models.CharField(help_text="Is the main competidor of the company. Maximum is 30 characters. Can be null and blank.", max_length=30, null=True, blank=True)
    patrimony                = models.BigIntegerField(help_text="Is the patrimony of the company in Colombian pesos. Can be null and blank.", null=True, blank=True)
    sales_income             = models.BigIntegerField(help_text="Is the sales income of the company in Colombian pesos. Can be null and blank.", null=True, blank=True)
    gross_profits            = models.BigIntegerField(help_text="Are the gross profit of the company in Colombian pesos. Can be null and blank.", null=True, blank=True)
    net_profits              = models.BigIntegerField(help_text="Are the net profits of the company in Colombian pesos. Can be null and blank.", null=True, blank=True)
    fixed_costs_expences     = models.BigIntegerField(help_text="Are the fixed cost and expenses of the company. Can be null and blank.", null=True, blank=True)
    variable_costs_expences  = models.BigIntegerField(help_text="Are the variable costs and expences of the company. Can be null and blank.", null=True, blank=True)
    ebitda                   = models.IntegerField(help_text="Is the EBITDA of the company. Can be null and blank.", null=True, blank=True)

    def __str__(self):
        return 'Finances information from {}'.format(self.pyme.name)

    class Meta:
        db_table = 'finances_information'
