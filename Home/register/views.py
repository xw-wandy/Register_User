from django.shortcuts import render
from .models import RegisterUser
from django.http import HttpResponseRedirect
import random


# Vista ~Principal
def index(request):

      user_on_register = str()
      

      if request.method == 'POST':
            name_user =request.POST['name']
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
                  
      return render(request, 'register/index.html', {'user_on_register': user_on_register})

 

#  Vista ~Lista de Usuarios
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
            
            
      for user in search_user:
                  buscando_usuario = user
                  if buscando_usuario.name_user == user_requered:
                        print(buscando_usuario)
                        break      
                  else:
                        buscando_usuario = "No encontrado"
                        
                              
                 #________________________________________       
      
      data_user = {
                  'register_user': register_user,
                  'lista_name_user': lista_name_user,
                  'lista_number_user': lista_number_user,
                  'buscando_usuario':buscando_usuario,
      }
      return render(request, 'register/lista_user.html', data_user)

def rederict(request):
      return render(request, 'register/rederict.html')







def perfil_user(request):
      return render(request, 'register/perfil_user.html')



def register(request):
      return render(request,'register/register.html')
