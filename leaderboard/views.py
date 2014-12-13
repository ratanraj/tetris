from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pymongo import MongoClient
import json

# Create your views here.

@login_required(login_url='/accounts/login/')
def leaderboard(request):
    return render(request, 'leaderboard.html', {'username':request.user.username})

def scores(request):
    client=MongoClient('mongodb://autotest:AvisoAutoTest@ec2-54-196-94-94.compute-1.amazonaws.com/autotest')
    scores = client['autotest']['scores'].find()
    data=[]
    for score in scores:
        del score['_id']
        data.append(score)
    for user in data:
        total=0
        for k,v in user['programs'].items():
            total+=v['score']
        user['total']=total
    return HttpResponse(json.dumps(data))


@login_required(login_url='/accounts/login/')
def userscore(request):
    client=MongoClient('mongodb://autotest:AvisoAutoTest@ec2-54-196-94-94.compute-1.amazonaws.com/autotest')
    score = client['autotest']['scores'].find_one({'user_name':request.user.username})
    del score['_id']
    total=0
    for k,v in score['programs'].items():
        total+=v['score']
    score['total']=total
    totals = []
    users = client['autotest']['scores'].find()
    for user in users:
        total=0
        for k,v in user['programs'].items():
            total+=v['score']
        totals.append({'user':user['user_name'],'total':total})
    sorted_totals = sorted(totals, key=lambda x:x['total'], reverse=True)
    count=1
    for st in sorted_totals:
        if st['user']==request.user.username:
            break
        count+=1
    count
    score['rank']=count
    return HttpResponse(json.dumps(score))

@login_required(login_url='/accounts/login/')
def submissions(request):
    client=MongoClient('mongodb://autotest:AvisoAutoTest@ec2-54-196-94-94.compute-1.amazonaws.com/autotest')
    user_name = request.user.username
    submissions = client['autotest']['submissions'].find({'user_name':user_name})
    data=[]
    for s in submissions:
        del s['_id']
        data.append(s)
    return HttpResponse(json.dumps(data))

def redirectview(request):
    return HttpResponseRedirect('/leaderboard')
