from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class Car(models.Model):

    state_choice = (
        ('AMA', 'Amazonas'),
        ('ANT', 'Antioquia'),
        ('ARA', 'Arauca'),
        ('ATL', 'Atlántico'),
        ('BOG', 'Bogotá D.F.'),
        ('BOL', 'Bolívar'),
        ('BOY', 'Boyacá'),
        ('CAL', 'Caldas'),
        ('CAQ', 'Caquetá'),
        ('CAS', 'Casanare'),
        ('CAU', 'Cauca'),
        ('CES', 'Cesar'),
        ('CHO', 'Chocó'),
        ('COR', 'Córdoba'),
        ('CUN', 'Cundinamarca'),
        ('GUA', 'Guainía'),
        ('GUV', 'Guaviare'),
        ('HUI', 'Huila'),
        ('LAG', 'La Guajira'),
        ('MAG', 'Magdalena'),
        ('MET', 'Meta'),
        ('NAR', 'Nariño'),
        ('NSA', 'Norte de Santander'),
        ('PUT', 'Putumayo'),
        ('QUI', 'Quindío'),
        ('RIS', 'Risaralda'),
        ('SAP', 'San Andrés y Providencia  '),
        ('SAN', 'Santander'),
        ('SUC', 'Sucre'),
        ('TOL', 'Tolima'),
        ('VAC', 'Valle del Cauca'),
        ('VAU', 'Vaupés'),
        ('VID', 'Vichada'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField(max_length=5000)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=255)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title