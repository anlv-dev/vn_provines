from django.contrib import admin
from .models import Site, Department, Address, Phone, Position, PeopleRelationship, People
# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ("name","short_name", "status")

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name","short_name", "status", "display_name", "site")

class AddressAdmin(admin.ModelAdmin):
    list_display = ("province","district", "ward", "street", "building", "house_no","used" )

class PhoneAdmin(admin.ModelAdmin):
    list_display = ("ext_phone","ccn_phone", "private_phone_1", "private_phone_2")

class PositionAdmin(admin.ModelAdmin):
    list_display = ("name","short_name",)

class PeopleRelationshipAdmin(admin.ModelAdmin):
    list_display = ("name_relationship","first_name","middle_name", "last_name", "gender", "dob", "age", "is_staff", "status")


class PeopleAdmin(admin.ModelAdmin):
    list_display = ("first_name","middle_name", "last_name", "gender", "dob", "age", "is_staff", "status")

class PositionAdmin(admin.ModelAdmin):
    list_display = ("name","short_name",)

admin.site.register(Site, SiteAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(PeopleRelationship, PeopleRelationshipAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Position, PositionAdmin)
    


# class PeopleRelationship(models.Model):
#     name_relationship = models.CharField(max_length=2, choices=RELATIONSHIP)
#     first_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     gender = models.CharField(max_length=1, choices=GENDER)
#     dob = models.DateField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     is_staff = models.BooleanField(default=False)
#     status = models.BooleanField(default=True)
#     phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name_relationship


# class People(models.Model):
#     first_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     gender = models.CharField(max_length=1, choices=GENDER)
#     dob = models.DateField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     is_staff = models.BooleanField(default=True)
#     status = models.BooleanField(default=True)
#     peoplerelationship = models.ForeignKey(PeopleRelationship, on_delete=models.CASCADE)
#     position = models.ForeignKey(Position, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.first_name + self.middle_name + self.last_name
