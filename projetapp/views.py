

# Create your views here.
# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
# views.py
from .models import Mesure
   
   # views.py
from django.shortcuts import render
import psycopg2

def liste_mesures(request):
    conn = psycopg2.connect(
        database="temphum",
        user="postgres",
        password="Marikoben10",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mesures")
    mesures = cursor.fetchall()
    print(mesures)  # Ajoutez cette ligne pour afficher les données dans la console
    context = {'mesures': mesures}
    return render(request, 'projetapp/fichier.html', context)
