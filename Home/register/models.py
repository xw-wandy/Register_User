from django.db import models
# RegisterUser is a model for register of ;
# 1:Name
# 2:Email
# 3:ID
# Where with table is unique 

class RegisterUser(models.Model):
      name_user = models.CharField(max_length=100)
      email_user = models.CharField(max_length=100)
      id_user = models.CharField(max_length=100)
      
      def __str__(self) -> str:
            return self.name_user