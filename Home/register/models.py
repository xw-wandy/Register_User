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


class Login_Data_Cache(models.Model):
      Name_User = models.CharField(max_length=200)
      

      def __str__(self):
          return self.Name_User 
      



class New_User(models.Model):
      full_name = models.CharField(max_length=50)
      email_user = models.CharField(max_length=200)

      def __str__(self):
          return self.full_name




      
      