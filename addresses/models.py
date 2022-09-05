from django.db import models

GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

RELATIONSHIP = (
        ('VO', 'Vợ'),
        ('CH', 'Chồng'),
        ('CO', 'Con'),
        ('BV', 'Bố Vợ'),
        ('MV', 'Mẹ Vợ'),
        ('BC', 'Bố Chồng'),
        ('MC', 'Mẹ Chồng'),
        ('BR', 'Bố Ruột'),
        ('MR', 'Mẹ Ruột'),
    )

# Create your models here.

class Address(models.Model):
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50)
    used = models.BooleanField(default=True)

class Phone(models.Model):
    ext_phone = models.CharField(max_length=3)
    ccn_phone = models.CharField(max_length=15)
    private_phone_1 = models.CharField(max_length=15)
    private_phone_2 = models.CharField(max_length=15)

class Site(models.Model):
    name = models.CharField(max_length=300)
    short_name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

class Department(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name
    
class Position(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)

    def __str__(self):
        return self.short_name


class PeopleRelationship(models.Model):
    name_relationship = models.CharField(max_length=2, choices=RELATIONSHIP)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_relationship


class People(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    peoplerelationship = models.ManyToManyField(PeopleRelationship)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name


