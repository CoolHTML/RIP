from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class registeation_form(forms.Form):
    nickname = forms.CharField(
        min_length=1,
        widget=forms.TextInput(
            attrs={'placeholder': 'Как Вас называть?',
                   'style': 'margin-bottom : 20px; margin-top : 5px; width : 200px;'}
        ), label='В'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email', 'style': 'margin-bottom : 20px; margin-top : 5px'
            }), label='Email'
    )
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Passord again', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from .models import *

game_types = games_names.objects.all()
game_types_ = []
k = 1
for i in game_types:
    game_types_.append((k, i.name))
    k += 1
game_types_ = tuple(game_types_)
print(game_types_)


class Create_game(forms.Form):
    form_number = created_sessions.objects.get(pk=1)

    number_of_players = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Число игроков', 'class': 'form-control',
                   'style': 'margin-bottom : 20px; margin-top : 5px'}
        ), label='Число игроков'
    )
    game_type = forms.ChoiceField(
        choices=game_types_
    )

    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Цена', 'class': 'form-control', 'style': 'margin-bottom : 20px; margin-top : 5px'}
        ), label='Цена с игрока за 1 сессию'
    )

    description = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': 'Что Вы хотите нам сказать?', 'class': 'form-control', 'rows': '5',
                   'style': ' margin-bottom : 20px; margin-top : 5px'}
        ), label='Ваш комментарий'
    )
    id = forms.CharField(initial=form_number.pk,widget = forms.HiddenInput(), required = False, label='')
    is_online = forms.BooleanField(initial=False,required=False, label='Игра онлайн?')

    contacts = forms.CharField(max_length=40, required=True, label='Введите контакт для связи с Вами')

    def change(self, a):
        self.form_number = a
        self.fields['price'].initial = a.price
        print(a.game_type.pk)
        self.fields['game_type'].initial = a.game_type.pk
        self.fields['number_of_players'].initial = a.number_of_players
        self.fields['description'].initial = a.description
        self.fields['id'].initial = a.pk
        self.fields['is_online'].initial = a.is_online
        self.fields['contacts'].initial = a.contacts


from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-class'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-class'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-class'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-class', 'rows': 5, 'style':'height:90px;'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class Create_game2(forms.Form):
    form_number = created_sessions.objects.get(pk=1)
    name = forms.CharField(
        disabled=True,
        min_length=1,
        initial=form_number.masters_name,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form-control',
                   'style': 'margin-bottom : 20px; margin-top : 5px'}
        ), label='Ваше имя'
    )
    number_of_players = forms.IntegerField(
        disabled=True,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Число игроков', 'class': 'form-control',
                   'style': 'margin-bottom : 20px; margin-top : 5px'}
        ), label='Число игроков'
    )
    game_type = forms.ChoiceField(
        disabled=True,
        choices=game_types_,

    )

    price = forms.IntegerField(
        disabled=True,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Цена', 'class': 'form-control', 'style': 'margin-bottom : 20px; margin-top : 5px'}
        ), label='Цена с игрока за 1 сессию'
    )

    description = forms.CharField(
        disabled=True,
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': 'Что Вы хотите нам сказать?', 'class': 'form-control', 'rows': '5',
                   'style': ' margin-bottom : 20px; margin-top : 5px'}
        ), label='Ваш комментарий'
    )
    id = forms.CharField(initial='ololo', disabled=True)

    is_online = forms.BooleanField(initial=False, label='Игра онлайн?', disabled=True)
    contacts = forms.CharField(max_length=40, disabled=True)


    def change(self,a):
        self.form_number = a
        self.fields['name'].initial = a.masters_name
        self.fields['price'].initial = a.price
        print(a.game_type.pk)
        self.fields['game_type'].initial = a.game_type.pk
        self.fields['number_of_players'].initial = a.number_of_players
        self.fields['description'].initial = a.description
        self.fields['id'].initial = a.pk
        self.fields['is_online'].initial = a.is_online
        self.fields['contacts'].initial = a.contacts



