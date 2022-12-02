from django.urls import path
from . import views as vues
from django.contrib.auth import views

app_name = 'presence'
urlpatterns = [
    path('login/', vues.se_connecter, name='login'),
    path('logout/', views.LogoutView.as_view(template_name='forms/logout.html', next_page='presence:login'), name='logout'),
    path('', vues.index, name='index'),
    path('utilisateurs_liste/', vues.utilisateurs_liste, name='utilisateurs_liste'),
    path('register_user/', vues.register_user, name='register_user'),
    path('update_user/<int:id>/', vues.update_user, name='update_user'),
    path('bloque_user/<int:id>/', vues.bloque_user, name='bloque_user'),
    path('my_profil/', vues.my_profil, name='my_profil'),
    path('update_username/', vues.update_username, name='update_username'),
    path('message_success_update_password/', vues.message_success_update_password, name='message_success_update_password'),
    path('password_change/', vues.PasswordChanginView.as_view(template_name="forms/password_change.html"), name='password_change'),
    path('forget_password/', vues.forget_password, name='forget_password'),
    path('add_sceance/', vues.add_sceance, name='add_sceance'),
    path('update_sceance/<int:id>/', vues.update_sceance, name='update_sceance'),
    path('open_sceance/<int:id>/', vues.open_sceance, name='open_sceance'),
    path('import_data_excel/<int:id>/', vues.import_data_excel, name='import_data_excel'),
    path('export_data_to_excel/<int:id>/', vues.export_data_to_excel, name='export_data_to_excel'),
    path('admin_views/', vues.admin_views, name='admin_views'),
    path('detail_sceance/<int:id>/', vues.detail_sceance, name='detail_sceance'),
]