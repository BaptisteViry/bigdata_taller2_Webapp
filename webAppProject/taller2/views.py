from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient

client = MongoClient('bigdata-mongodb-04.virtual.uniandes.edu.co', 8087)
db = client.Grupo10
collectionVenezuela = db.Venezuela
collectionMinga = db.minga
collectionJep = db.jep

def index(request):
    return render(request, "taller2/index.html")

def presentacionDB(request):
    #first consult
    countVenezuela = collectionVenezuela.find({}).count()
    countMinga = collectionMinga.find({}).count()
    countJep = collectionJep.find({}).count()
    countCollections = { 'countVenezuela':countVenezuela, 'countMinga':countMinga, 'countJep':countJep}
    context = { 'countCollections':countCollections }

    
    return render(request, "taller2/presentacionDB.html", context)

def charts(request):
    dataPolarity = { 'positive':120000, 'neutral':150000, 'negative':90000, 'insult':30000 }
    context = {'dataPolarity': dataPolarity}
    return render(request, "taller2/charts.html", context)