from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    imagen = models.ImageField(upload_to='uploads/', null=True, blank=True)

    # Views register from django administrator
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # Delete image from django administrator - interface user
    # def delete(self, using=None, keep_parents=False):
    #     self.imagen.storage.delete(self.imagen.name)
    #     super().delete()
    
