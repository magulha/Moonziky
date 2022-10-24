from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model
from models import playlist
from django.urls import reverse

# Create your tests here.

class AutenticacaoUsuario(TestCase):

        def setUp(self):
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.user={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'password',
        }
        self.senha.invalida={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
        }
        self.email.invalido={            
            'email':'test.com',
            'username':'username',
            'password':'teslatt',
        }
        return super().setUp()

    
        def pode_fazer_login(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

        def nao_pode_logar_com_email_ja_usado(self):
        self.client.post(self.register_url,self.user,format='text/html')
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,400)

class loginUsuario(TestCase):

        def pode_acessar_pagina(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')

        def login_sucesso(self):
        self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.filter(email=self.user['email']).first()
        user.is_active=True
        user.save()
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

        def nao_pode_logar_sem_senha(self):
        response= self.client.post(self.login_url,{'username':'passwped','password':''},format='text/html')
        self.assertEqual(response.status_code,401)

class playlisttest(TestCase):

    def ver_playlist(self):
        playlist = Playlist.objects.get(name='Rock and Roll')
        response = self.client.get(self.uri_playlist_one(playlist.user.id, playlist.id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'playlist/playlist.html')

    def remover_playlist(self, name):
        playlist = Playlist.objects.filter(name=name).delete()
        return None

    def apagar_playlist(self, auth):
        user = User.objects.get(username='test')
        self.remove_playlist('Delete This')
        playlist = Playlist.objects.create(name='Delete This', user=user)
        self.authorize(auth)
        response = self.client.post('%s?action=delete' % (self.uri_playlist_one(playlist.user.id, playlist.id)))
        return response