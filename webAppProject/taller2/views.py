from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient

import json, random

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

def hashtagWordCloud(request):
    #groupBy hashtags
    i = 10
    hashtagsArray = []
    hashtagsCursor = collectionVenezuela.aggregate([{'$unwind': '$entities.hashtags'}, { '$group': { '_id': '$entities.hashtags.text', 'count': {'$sum': 1}}}, { '$sort': { 'count': -1 }},{ '$limit': 10 }])
    for h in hashtagsCursor:
        x = {"hashtag": h["_id"], "count": h["count"], "rank": i}
        hashtagsArray.append(x)
        i -= 1 

    random.shuffle(hashtagsArray)
    print(hashtagsArray)


    context = { "hashtags": hashtagsArray}
    return render(request, "taller2/hashtagWordCloud.html", context)