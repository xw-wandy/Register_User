from django.shortcuts import render
from .models import RegisterUser
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
      
      if request.method  == 'POST':
            register_user = RegisterUser()
            register_user.name_user = request.POST['name']      
            register_user.email_user = request.POST['email']      
            register_user.id_user = request.POST['id']      
            register_user.save()
            print(register_user.name_user)
            print(register_user.id_user)
            print(register_user.name_user)
            print("Primera validacion")
            return  HttpResponseRedirect('/lista_user/')
      else:
            print("Segunda validacion")
       
            # return HttpResponseRedirect('/rederict/')



      return render(request, 'register/index.html')

def lista_user(request):
      register_user = RegisterUser.objects.all()
      lista_name_user = []
      for name_user in register_user:
            lista_name_user.append(name_user.name_user)
      
      lista_number_user = len(lista_name_user)      
      
      
      # Buscar nombre especifico en la base de datos
      if request.method == 'POST':
            
            user_requered = request.POST["searching-user"]
            search_user = RegisterUser.objects.all()
                   # search_name_user = RegisterUser.objects.get('')
      
      
      data_user = {
                  'register_user': register_user,
                  'lista_name_user': lista_name_user,
                  'lista_number_user': lista_number_user,
      }
      return render(request, 'register/lista_user.html', data_user)

def rederict(request):
      return render(request, 'register/rederict.html')