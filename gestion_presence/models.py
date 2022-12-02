from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

sexe_choice = (
    ('Masculin', 'Masculin'),
    ('Féminin', 'Féminin'),
    ) 

class Enseignant(models.Model):
    user_account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_account')
    nom = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    pre_nom = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, choices=sexe_choice, default='Masculin')
    phone_number = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.nom} {self.post_nom} {self.pre_nom}"
    
class Sceance(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    promotion = models.CharField(max_length=30)
    cours = models.CharField(max_length=30)
    date_create = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.enseignant.nom
    
    def number_seance(self):
        number_seance = SceanceDay.objects.filter(sceance=self).count()
        if number_seance <= 0:
            return 1
        return number_seance
    
class SceanceDay(models.Model):
    sceance = models.ForeignKey(Sceance, on_delete=models.CASCADE)
    date_sceance = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.sceance.promotion    
    
class Participant(models.Model):
    matricule = models.IntegerField()
    nom = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    pre_nom = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, choices=sexe_choice, default='Masculin')
    presences = models.ManyToManyField(SceanceDay, blank=True, related_name='presences')
    sceance = models.ForeignKey(Sceance, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nom
    
    def pourcentage_presence(self):
        nb_sceance = self.sceance.number_seance()
        nb_participation = self.presences.count()
        pourcentage = round((nb_participation * 100) / nb_sceance, 2)
        return pourcentage
    
    def is_presente(self):
        sceance = SceanceDay.objects.filter(sceance=self.sceance)
        try:
            sceance_day = sceance.get(date_sceance=date.today())
            if self.presences.filter(id=sceance_day.id):
                return True
            return False
        except Exception as e:
            return False
