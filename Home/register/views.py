from django.shortcuts import render
from .models import RegisterUser, Login_Data_Cache, New_User
from django.http import HttpResponseRedirect
import random


# Vista ~Principal
def home(request):

      pass

      return render(request, 'register/home.html')





#_________________________________________________
def login(request):
      login_data_cache = Login_Data_Cache()
      login_data = login_data_cache.Name_User


      user_on_register = str()
      cache_ready = str()

      if request.method == 'POST':
            name_user = request.POST['name']
            login_data_cache.Name_User = request.POST['name']
            login_data_cache.save()
         

            print(name_user)
            
            register_user = RegisterUser.objects.all()
            
                  # register_user.email_user = request.POST['email']      
                  # register_user.id_user = request.POST['id']  

            user_on_register = str
            
            for user in register_user:
                        user_2 = user
                        if user_2.name_user == name_user:
                              user_on_register = user.name_user
                              return HttpResponseRedirect('/perfil_user/',  
                              {'user_on_register': user_on_register,      })
                        else:
                              
                              user_on_register = 'Usuario incorrecto'


      else:
                  user_on_register 
                  
      return render(request, 'register/login.html', 
      {'user_on_register': user_on_register,  })

 




#___________________________________________       
def lista_user(request):
      register_user = RegisterUser.objects.all()


      lista_name_user = []
      for name_user in register_user:
            lista_name_user.append(name_user.name_user)
      
      # lista_number_user d
      lista_number_user = len(register_user)
      buscando_usuario = str

      # Buscar nombre especifico en la base de datos
      
      user_requered = str
      # user_requered =   request.POST["searching-user"]
      search_user = RegisterUser.objects.all()
      cache_ready = str()

            
      for user in search_user:
                  buscando_usuario = user
                  if buscando_usuario.name_user == user_requered:
                        print(buscando_usuario)
                        break      

      
      data_user = {
                  'register_user': register_user,
                  'lista_name_user': lista_name_user,
                  'lista_number_user': lista_number_user,
                  'buscando_usuario':buscando_usuario,
      }
      return render(request, 'register/lista_user.html', data_user)




#________________________________________       
def rederict(request):
      return render(request, 'register/rederict.html')







#________________________________________       
def perfil_user(request):

      login_data_cache = Login_Data_Cache.objects.all()
      # login_data = login_data_cache.Name_User
      last_user_in_data = []
      ready_last_user = str()
      

      # request_name = request.POST['name']
      # print(request_name)
      user_list = RegisterUser.objects.all()
      user_requered = 'Wandy Olivares'
      user_choice = str
      for user in user_list:
            name_user = user.name_user
            if name_user == user_requered:
                  user_choice = name_user
                  print(user_choice)

      
      for data_cache in login_data_cache:
            last_user_in_data.append(data_cache.Name_User)
      counts_user_in_data_cache = len(last_user_in_data)
      ready_last_user = last_user_in_data[counts_user_in_data_cache - 1]
      print(ready_last_user)
      
                        
                              

      context = {
                  'user_list': user_list,
                  'user_choice': user_choice,
                  'ready_last_user':ready_last_user,  }

      return render(request, 'register/perfil_user.html', context)



def register(request):
      
      new_user = New_User()
      export_user = New_User.objects.all()

      if request.method == 'POST':
            new_user.full_name = request.POST['full-name']
            new_user.email_user = request.POST['email-user']
            
            new_user.save()

      for user in export_user:
            print(user)
      


            print(' ')

            print(new_user.full_name)
            print(' ')
            print(new_user.email_user)
        
            print(' ')


      return render(request,'register/register.html')
