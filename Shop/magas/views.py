from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from rest_framework import viewsets
from .models import created_sessions
from rest_framework import viewsets
from .serializers import created_sessions_ser
from .models import created_sessions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = created_sessions.objects.all()
    serializer_class = created_sessions_ser  # Сериализатор для модели

def mainpage(request):
    print('ololo')
    return render(request,'magas/main_page.html',{'title':'Главная страница'})

def registrationpage(request):
    text=''
    if request.user.is_authenticated():
        username = request.user.username
        print(username)
    if request.method == 'POST':
        form = registeation_form(request.POST)
        print(form.is_valid())
        if form.is_valid():
            a = form.cleaned_data
            print(a)
            return HttpResponseRedirect(request.path)
        else:
            text = 'Neverno'
    else:
        form = registeation_form()
    return render(request,'magas/Registration.html',{'title':'Регистрация','form':registeation_form})
# Create your views here.

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'magas/Registration.html'
    success_url = reverse_lazy('login')

class AuthUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'magas/Authentication.html'

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('login')

def ellizium_mainpage_view(request):
    title = 'Эллизиум главная страница'
    return render(request,'magas/Ellizium_mainpage.html',{'title':title})
def ellizium_rools_view(request):
    title = 'Эллизиум страница правил'
    return render(request,'magas/haracteristiki.html',{'title':title})




def my_view(request):
    username = None
    if (request.user.is_authenticated):
        username = request.user.username
        return (username)

def view_all_games(request):
    title = 'Все игры'
    games = created_sessions.objects.all()
    players = players_in_current_game.objects.all()
    types = games_names.objects.all()
    types_=[]
    for i in types:
        types_.append([i.name,i.pk])
    for i in types_:
        print(i[0],i[1])
    print(types_[0][0])
    print(types_)
    value=2
    value2=True
    value3=2
    show_my_games = True
    if request.method == "POST":
        value = request.POST.getlist('sort')
        value2 = request.POST.getlist('on/of')
        value3 = request.POST.getlist('all')
        show_my_games = request.POST.getlist('my_games')

        print(value)
        print(value2)
        if(value):
            value = int(value[0])
        else:
            value=0
        if(value3):
            if(value3[0] == '2'):
                value3 = 2
        else:
            value3=0
        if(show_my_games):
            if(show_my_games[0] == '2'):
                show_my_games = True
        else:
            show_my_games=False
        if(value2[0]=='1'):
            value2 = True
            print('oeomfrov ej')
        else:
            value2=False
    return render(request,'magas/view_all_games.html',{'title':title , 'games':games, 'username':request.user.username,'players':players,
    'types':types_, 'value':value,'value2':value2,'value3':value3, 'show_my_games':show_my_games})




def find_game_view(request):
    title = 'Поиск игры'
    username = my_view(request)
    print(username)
    if request.method == 'POST':
        form = Create_game(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            timer = int(a['game_type'])
            games_namess = games_names.objects.get(pk = timer)
            print(games_namess)
            print(a)
            object = created_sessions.objects.create(masters_name = username, number_of_players = int(a['number_of_players']),
            current_number_of_players = 0,description = a['description'], game_type = games_namess,price = a['price'], is_online=a['is_online'])
            object.save()
            form = Create_game()

    else:
        form = Create_game()
    return render(request,'magas/find_game.html',{'title':title , 'form':form})



#def user_profile(request):
#   return render(request,'magas/profile_template.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(user_form,profile_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            print('oololool1')
            return redirect(to='users-profile')
        print('oololool2')
    else:
        print('oololool3')
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    my_games = created_sessions.objects.filter(masters_name = request.user.username)
    form = []
    for i in range(0,len(my_games)):
        form.append(Create_game2())
        form[i].change(my_games[i])
        print(my_games[i])


    return render(request, 'magas/profile_template.html', {'user_form': user_form, 'profile_form': profile_form, 'mygames':my_games,'form':form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'magas/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('login')


def add_view(request,player,id):
    player = players_in_current_game.objects.create(player=request.user.username, game_id=id)
    player.save()
    return view_all_games(request)


def view_current_game(request,id):
    title = 'Игровая комната'
    is_in_the_game = False
    if (players_in_current_game.objects.filter(player=request.user.username, game_id = id).exists() and request.user.username != created_sessions.objects.get(pk = id).masters_name):
        is_in_the_game = True
    if request.method == "POST":
        if(not players_in_current_game.objects.filter(player = request.user.username).exists() and request.user.username != created_sessions.objects.get(pk = id).masters_name):
            pass
        else:
            id_list = request.POST.getlist('boxes')
            print(id_list)
            players_in_current_game.objects.all().update(approved_to_play = False)
            for x in id_list:
                players_in_current_game.objects.filter(pk = int(x)).update(approved_to_play = True)

            print(created_sessions.objects.filter(pk=id))
            created_sessions.objects.filter(pk=id).update(current_number_of_players=len(id_list))
            print(len(id_list))
            print(created_sessions.objects.filter(pk=id))
            if(len(id_list) > created_sessions.objects.get(pk=id).number_of_players):
                created_sessions.objects.filter(pk=id).update(number_of_players=len(id_list))

    try:
        game_info =created_sessions.objects.get(pk=id)
        players = players_in_current_game.objects.filter(game_id = id)
        game_info = created_sessions.objects.get(pk=id)
        players = players_in_current_game.objects.filter(game_id=id)
        try:
            me_approved = players_in_current_game.objects.get(game_id=id, player=request.user.username)
            return render(request, 'magas/game_room.html',
                          {'title': title, 'game': game_info, 'username': request.user.username, 'players': players,
                           'is_in_the_game': is_in_the_game, 'approved': me_approved.approved_to_play})
        except:
            return render(request, 'magas/game_room.html',
                          {'title': title, 'game': game_info, 'username': request.user.username, 'players': players,
                           'is_in_the_game': is_in_the_game, 'approved': False})
    except:
        return redirect(reverse_lazy('main'))



def delete_page(request,player,id):
    a = (players_in_current_game.objects.filter(player = player, game_id = id))

    timer = players_in_current_game.objects.get(player = player, game_id = id)
    if (timer.approved_to_play):
        created_sessions.objects.filter(pk=id).update(
            current_number_of_players=created_sessions.objects.get(pk=id).current_number_of_players - 1)
    all_players = players_in_current_game.objects.filter(player=player, game_id=id).delete()

    return view_all_games(request)

@login_required
def view_game(request,id):
    title = 'Редактировать игру'
    my_games = created_sessions.objects.filter(masters_name=request.user.username,pk=id)
    form = []
    for i in range(0, len(my_games)):
        form.append(Create_game())
        form[i].change(my_games[i])

    if request.method == 'POST':
        form_get = Create_game(request.POST)
        print(12323)
        if form_get.is_valid():
            a = form_get.cleaned_data
            print(a)
            created_sessions.objects.filter(pk = int(a['id'])).update(number_of_players = a['number_of_players'], game_type = a['game_type'],
            price = a['price'], description = a['description'], is_online = a['is_online'], contacts = a['contacts'])
            timer = created_sessions.objects.get(pk = int(a['id']))
            return redirect(reverse_lazy('main'))

    return render(request,'magas/current_game.html',{'title':title,'username':request.user.username, 'mygames':my_games,'form':form})

def approved_games(request):
    title='Мои игры'
    username = request.user.username
    my_approved_games = players_in_current_game.objects.filter(player = username, approved_to_play=True)
    print(my_approved_games)
    return render(request, 'magas/approved_games.html', {'title':title,'my_approved_games':my_approved_games})


from django.contrib.auth.models import User
import json

@api_view(['GET', 'POST'])
def getJson(request):
        if request.method == 'POST':
            print(request.data)
            user = User.objects.create_user(request.data['username'], request.data['email'], request.data['password'])
            user.save()
            return HttpResponse("{'status': 'ok'}")
        else:
            return HttpResponse("{'status': 'neok'}")


class MyViewSet(viewsets.ModelViewSet):
    queryset = created_sessions.objects.all()
    serializer_class = created_sessions_ser










