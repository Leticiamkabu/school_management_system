from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_delete, post_save
import random
from django.dispatch import receiver
# import random
# from administrator.models import Student_Payment_Details
# from administrator.models import Student_Payment_Details


# class TeacherRegisteration(models.Model):
#     username = models.CharField(max_length = 200)
#     email = models.EmailField(max_length = 200)
#     password = models.CharField(max_length = 200)
#     position = models.CharField(max_length = 200)
#     application_number = models.IntegerField(default = 0)
#     teacher_id = models.IntegerField()
        
ROLE_SELECTION = (
    ('Student', 'Student'),
    ('Stuff', 'Stuff'),
)
class SystemUserData(AbstractUser):
    status = models.CharField(max_length = 20, choices= ROLE_SELECTION , default = 'Student')
    registration_date = models.DateTimeField(auto_now_add=True)
    # user = models.OneToOneField(StudentRegisteration, on_delete = models.CASCADE)



LEVEL_SELECTION = (
    ('Form1','Form1'),
    ('Form2', 'Form2'),
    ('Form3', 'Form3'),
 ) 

# from administrator.models import Student_Payment_Details  
class StudentRegisteration(models.Model):
    username = models.CharField(max_length = 200, unique = False )
    email = models.EmailField(max_length = 200, unique = True)
    password = models.CharField(max_length = 200, unique = True)
    level = models.CharField(max_length = 50, choices = LEVEL_SELECTION , default = "None")
    admission_number = models.IntegerField(unique= True, default = 'None')
    registered_student_id = models.IntegerField(unique= True)
    


@receiver(pre_save, sender = StudentRegisteration )
def generate_student_ID(instance,*args,**kwargs):
    instance.registered_student_id = random.randint(100, 100000)
    
 
@receiver(pre_save, sender = StudentRegisteration )
def generate_student_Email(instance,*args,**kwargs):
    instance.email = instance.username + str(instance.registered_student_id)+ "@merge.edu.gh"
    
from administrator.models import Student_Payment_Details 
@receiver(post_save, sender = StudentRegisteration )
def generate_student_payment_details(sender, instance, created, **kwargs):
    if created:
        payment_details = Student_Payment_Details.objects.create(
            student=instance,
            name=instance.username,
            level=instance.level,
            
        )
        payment_details.save()  
        
        
@receiver(post_save, sender = StudentRegisteration )
def create_student_user_details(sender, instance, created, **kwargs):
    if created:
        student_user = SystemUserData.objects.create(
            
           
            username = instance.username, 
            email = instance.email, 
            status = 'Student',
        )
        student_user.set_password(instance.password)
        student_user.save()  
        
        
        
class TeacherRegisteration(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    application_number = models.IntegerField(default = 0)
    teacher_id = models.IntegerField()
    
    
@receiver(pre_save, sender = TeacherRegisteration)
def generate_teacher_email(sender, instance, **kwargs):
    
    instance.email = instance.username + str(instance.teacher_id) + '@merge.edu.gh'
    
    
@receiver(pre_save, sender = TeacherRegisteration)
def generate_teacher_id(sender, instance, **kwargs):
    instance.teacher_id = random.randint(20000, 2000000000)
    # instance.registered_student_id = random.randint(100, 100000)
    
    
@receiver(post_save, sender = TeacherRegisteration)
def create_a_teacher_user_instance(sender,instance,created, **kwargs ):
    if created:
        teacher_user = SystemUserData.objects.create(
            username = instance.username, 
            email = instance.email, 
            status = 'Teacher',
        )
        teacher_user.set_password(instance.password)
        teacher_user.save()
      
        
        
