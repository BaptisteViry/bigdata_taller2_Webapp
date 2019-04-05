from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient

client = MongoClient('bigdata-mongodb-04.virtual.uniandes.edu.co', 8087)
db = client.Grupo10
collection = db.test

def index(request):
    return render(request, "taller2/index.html")

def presentacionDB(request):

    context = { 'test': collection.find_one()}

    return render(request, "taller2/presentacionDB.html", context)
