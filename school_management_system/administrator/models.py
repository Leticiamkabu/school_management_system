from django.db import models
import random
from django.db.models.signals import pre_save, post_delete, post_save
from django.dispatch import receiver
import os
from django.conf import settings
# from authentication.models import StudentRegisteration



GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


# Create your models here.

class Admission_Forms_detail(models.Model):
    form_id = models.AutoField(primary_key = True)
    date = models.DateTimeField(auto_now= True )
    admission_number = models.IntegerField(null=True, blank=True, unique = True)
    image = models.ImageField(upload_to=('img/students/'), height_field=None, width_field=None, max_length=None)
    first_name = models.CharField(max_length = 200, unique = True)
    last_name = models.CharField(max_length = 200, unique = True)
    age = models.IntegerField()
    email = models.EmailField(max_length=200, default = None)
    phone_number = models.IntegerField(blank = False)
    level = models.CharField(max_length = 200)
    grade = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length = 200)
    nationality = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 30, choices= GENDER, default = True)
    residential_address = models.CharField(max_length = 200)
    language = models. CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    father_name = models.CharField(max_length = 200)
    status = models.CharField(max_length = 50, default = 'Pending Approval')
    
    
    
@receiver(pre_save, sender= Admission_Forms_detail)
def generate_random_number(sender, instance, *args, **kwargs):
    if not instance.admission_number:  # Only generate if the field is empty
        instance.admission_number = random.randint(100, 5000)
        
@receiver(pre_save, sender= Admission_Forms_detail)
def change_image_name(sender, instance, *args, **kwargs):
    file_path = instance.image.name 
    file_dir, file_name = os.path.split(file_path)
    instance.image.name = os.path.join(file_dir, instance.first_name + ".jpg" )
    
    
def delete_image(sender, instance, **kwargs):
    if instance.image:
        file_path = instance.image.path
        
        if os.path.exists(file_path):
            os.remove(file_path)
    

    
WORK_DURATION = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
) 
        
class Application_Form_detail(models.Model):
    application_number = models.IntegerField(unique = True)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    contact = models.IntegerField()
    email = models.EmailField(max_length = 200)
    location = models.CharField(max_length = 200)
    application_position = models.CharField(max_length = 200)
    certificate = models.ImageField(upload_to = 'img/teachers/',unique = True)
    work_experience = models.CharField(max_length = 200)
    reference =  models.CharField(max_length = 200)
    duration_of_work = models.CharField(max_length = 20, choices = WORK_DURATION, default = 'Full Time')
    status = models.CharField(max_length = 30, default = 'Pending Approval')
    
    
    

    
    
@receiver(pre_save, sender = Application_Form_detail)
def change_image_name(sender, instance, *args, **kwargs):
    # get the current file path
    file_path = instance.certificate.name
    # slit the file path and fiel name into respective value holders
    file_dir, file_name = os.path.split(file_path)
    # join the filepath and the new file name
    instance.certificate.name = os.path.join(file_dir, instance.first_name + ".jpg")
    
    
@receiver(pre_save, sender = Application_Form_detail)
def generate_application_id(sender, instance, *args, **kwargs):
    instance.application_number= random.randint(70000, 2040000000)
   
@receiver(post_delete, sender= Application_Form_detail)
def delete_applicant_image(sender, instance, **kwargs):
    # Delete the associated image file
    if instance.certificate:
        # Get the file path of the image
        file_path = instance.certificate.path
        # Check if the file exists and delete it
        if os.path.exists(file_path):
            os.remove(file_path)
            

from authentication.models import StudentRegisteration
class Student_Payment_Details(models.Model):
    student = models.OneToOneField(StudentRegisteration, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, unique = False)
    level = models.CharField(max_length = 200)
    total_amount = models.IntegerField(default = 0)
    amount_paid = models.IntegerField(default = 0)
    amount_left = models.IntegerField(default = 0)
    
    
    
@receiver(pre_save, sender= Student_Payment_Details)
def adding_fee_amount_to_payment_form(sender,instance, **kwargs):
    if instance.level == 'Form1':
       instance.total_amount = 5000
       
    elif instance.level == 'Form2':
        instance.total_amount = 3000
        
    elif instance.level == 'Form3':
        instance.total_amount = 1000
        
        
# from authentication.models import TeacherRegisteration
class Course(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    description = models.TextField(max_length = 500)
    course_number = models.IntegerField()
    level = models.CharField(max_length = 200)
    teacher = models.OneToOneField('authentication.TeacherRegisteration', on_delete= models.SET_NULL, null = True)
    student = models.ForeignKey(StudentRegisteration, on_delete= models.CASCADE)
    
       
@receiver(pre_save, sender = Course)
def generate_course_number(sender, instance, **kwargs):
    instance.course_number = random.randint(500000, 20000000)
    
    
@receiver(pre_save, sender = Course)
def get_associated_students(sender, instance, **kwargs):
    instance.student = StudentRegisteration.objects.get(level = instance.level)