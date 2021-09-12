from django.shortcuts import render
import pyrebase
from django import contrib
from django.http import HttpResponse,JsonResponse
from multiprocessing import Process
from .MLModel import addProfile,seeData,findSimilarProfile

import firebase_admin
from firebase_admin import credentials,auth


cred = credentials.Certificate("C:/Users/admin/Downloads/isolate-together.json")


default_app = firebase_admin.initialize_app(cred)

# Obviously keys are fake
config = {
    'apiKey' : "AIzaSyD-Eq232dW_9loS8h6f-KWAFFIivAsdylbc",
    'authDomain' : "isolate-together-88b63.firebaseapp.com",
    'databaseURL' : "https://isolate-together-88b63.firebaseio.com",
    'projectId' : "isolate-together-8c363",
    'storageBucket' : "isolate-together-8c363.appspot.com",
    'messagingSenderId' : "769043346241",
    'appId' : "1:76904251146241:web:c69ad42353107adbca6320"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
authe = firebase.auth()


# Create your views here.

def signIn(request):
    return render(request,"signIn.html")

def postsign(request):
    email = request.POST.get('email')

    if request.POST.get('normalSignin')=="0":
        
        a=request.POST.get('idToken')
        decoded_token = auth.verify_id_token(a)
        a = decoded_token['uid']
        print(a)
        request.session['accessToken'] = str(a)
        request.session['googleSignin'] = 1
        request.session['email'] = email

    else:
        
        try:
            password = request.POST.get('password')
            user = authe.sign_in_with_email_and_password(email, password)
            session_id = user['idToken']
            #print(user)
            print(session_id)
            request.session['uid'] = str(session_id)
            request.session['email'] = email
            a=authe.get_account_info(user['idToken'])
            print(a)
            a=a['users']
            a=a[0]
            a=a['localId']
            request.session['accessToken'] = str(a)
            request.session['googleSignin'] = 0
            request.session['email'] = email
            
        except:
            message = "Invalid Crediantials"
            return render(request,"signIn.html",{'msg':message})
    Interests = database.child("users").child(a).child("Interests").get().val()
    # p1 = Process(target=findSimilarProfile(a))
    # p1.start()
    # print("Outside MLModel")
    user_name = database.child("users").child(a).child("details").child('name').get().val()
    print(user_name)
    request.session['user_name'] = str(user_name)
    return render(request,"index.html",{"user":email,"username":user_name})
    

def logOut(request):
    contrib.auth.logout(request)
    try:
        del request.session
    except KeyError:
        pass
    return render(request,"index.html")

def checkEmail(request):
    #print("hiii")
    email = request.POST['email']
    print("checking email exist")
    print(email)
    #user = authe.sign_in_with_email_and_password(email, " ")
    try:
        user = authe.sign_in_with_email_and_password(email, " ")
    except Exception  as e:
        p = str(e)
        print(p)
        print(len(p))
        if len(p)>370:
            return JsonResponse({'exist': '1'})
        else:
            return JsonResponse({'exist': '0'})

def select(request):

    return render(request,'card.html')

def covidSignUp(request):

    return render(request,'covidSignUp.html')

def recoveredSignUp(request):

    return render(request,'recoveredSignUp.html')


def signUp(request):

    return render(request,'signUp.html')

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')
    
    user = authe.create_user_with_email_and_password(email,passw)
    
    uid = user['localId']
    data = {'name':name,'status':1}
    database.child("users").child(uid).child("details").set(data,user['idToken'])

    user = authe.sign_in_with_email_and_password(email, passw)
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    request.session['email'] = email
    return render(request,'enterInterest.html')

def registered(request):
    if request.POST.get('normalSignin')=="0":
        a=request.POST.get('idToken')
        decoded_token = auth.verify_id_token(a)
        a = decoded_token['uid']
        print(a)
        request.session['accessToken'] = str(a)
        request.session['googleSignin'] = 1
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        user = authe.create_user_with_email_and_password(email,passw)
        user = authe.sign_in_with_email_and_password(email, passw)
        idToken = user['idToken']
        request.session['uid'] = str(idToken)
        request.session['username'] = name
        a=authe.get_account_info(idToken)
        a=a['users']
        a=a[0]
        a=a['localId']
        request.session['accessToken'] = str(a)
        request.session['googleSignin'] = 0
    return render(request,'enterInterest.html')


def enterInterest(request):
    #uid = request.session['uid']
    a = request.session['accessToken']
    data = {
        'name':request.POST.get('name'),
        'age' : request.POST.get('age'),
        'gender' : request.POST.get('gender'),
        'country' : request.POST.get('country'),
        'Oxygen level' : request.POST.get('oxygenlevel'),
        'Body Temperature' : request.POST.get('bodytemperature'),
        'coughandcold' : request.POST.get('coughandcold'),
        'shortness of Bredth' : request.POST.get('shortnessOfBredth'),
        'loss of Taste' : request.POST.get('lossOfTaste'),
        'loss of Apetite' : request.POST.get('lossOfApetite'),
        'Covid status' : "1",
    }
    database.child("users").child(a).child("details").set(data)

    moviedata = {
        'value' : request.POST.get('movie'),
        'hollywood' : request.POST.get('hollywood'),
        'bollywood' : request.POST.get('bollywood'),
        'action' : request.POST.get('action'),
        'romantic' : request.POST.get('romantic'),
        'comedy' : request.POST.get('comedy'),
        'drama' : request.POST.get('drama'),
        'thriller' : request.POST.get('thriller'),
        'horror' : request.POST.get('horror'),
        'detective' : request.POST.get('detective'),
        'scifi' : request.POST.get('scifi'),
    }

    bookdata = {
        'value' : request.POST.get('book'),
        'fiction' : request.POST.get('fiction'),
        'non fiction' : request.POST.get('nonFiction'),
        'biography' : request.POST.get('biography'),
        'novel' : request.POST.get('novel'),
        'mystery' : request.POST.get('mystery'),
        'detective' : request.POST.get('detective')
    }

    #music = request.POST.get('music')
    #rock = request.POST.get('rock')
    #pop = request.POST.get('pop')
    #jazz = request.POST.get('jazz')
    musicdata = {
        'value' : request.POST.get('music'),
        'rock' : request.POST.get('rock'),
        'pop' : request.POST.get('pop'),
        'hip hop' : request.POST.get('hipHop'),
        'jazz' : request.POST.get('jazz'),
        'heavy metal' : request.POST.get('heavyMetal'),
        'country music' : request.POST.get('countryMusic'),
        'edm' : request.POST.get('edm')
    }

    sportdata = {
        'value' : request.POST.get('sport'),
        'cricket' : request.POST.get('cricket'),
        'football' : request.POST.get('football'),
        'basketball' : request.POST.get('basketball'),
        'hockey' : request.POST.get('hockey'),
        'baseball' : request.POST.get('baseball'),
        'chess' : request.POST.get('chess'),
        'bandmiton' : request.POST.get('bandmiton')
    }
    Interests = {
        'Movie' : moviedata,
        'Book' : bookdata,
        'Music' : musicdata,
        'Sport' : sportdata
    }
    p1 = Process(target=addProfile(Interests,a))
    p1.start()
    print("Outside MLModel")
    
    try:
        database.child("users").child(a).child("Interests").set(Interests)
        name = database.child("users").child(a).child("details").child("name").get().val()
        return render(request,"index.html",{"username":name})
    

    except KeyError:
        message = "Oops user logged out! Please signin again"
        return render(request,"signIn.html",{'msg':message})

def postRecoveredSignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')
    user = authe.create_user_with_email_and_password(email,passw)
    
    uid = user['localId']
    data = {
        'name':request.POST.get('name'),
        'age' : request.POST.get('age'),
        'gender' : request.POST.get('gender'),
        'country' : request.POST.get('country'),
        'Tested Covid Positive Date' : request.POST.get('covidPositiveDate'),
        'Tested Covid Negative Date' : request.POST.get('covidNegativeDate'),
        'Covid status' : "0",
    }
    database.child("users").child(uid).child("details").set(data,user['idToken'])

    user = authe.sign_in_with_email_and_password(email, passw)
    idToken = user['idToken']
    request.session['uid'] = str(idToken)
    request.session['username'] = name

    try:
        print(idToken)
        name = database.child("users").child(uid).child("details").child("name").get(idToken).val()
        return render(request,"index.html",{"user":email,"username":name})
    
    except KeyError:
        message = "Oops user logged out! Please signin again"
        return render(request,"signIn.html",{'msg':message})


def match(request):
    try:
        if request.session['accessToken']:
            #idtoken = request.session['uid']
            #a=authe.get_account_info(idtoken)
            #a=a['users']
            #a=a[0]
            #a=a['localId']
            a=request.session['accessToken']
            user_detail = database.child("users").child(a).child("details").child('name').get().val()
            print(user_detail)
            
            if user_detail == "anonymoususer":
                print("hello")
                return render(request,"match.html")

            similar_user_list=findSimilarProfile(a)
            print("Outside MLModel")
            print(similar_user_list)
            user_name_list=[]
            user_loc_list=[]
            user_gender_list=[]
            it=[]
            j=0
            for i in similar_user_list:
                user_details =  database.child("users").child(i).child("details").get().val()
                user_name_list.append(user_details['name'])
                user_loc_list.append(user_details['country'])
                user_gender_list.append(user_details['gender'])
                it.append(j)
                j=j+1
            print(user_name_list,user_loc_list,user_gender_list,it)
            su_list = zip(similar_user_list,user_name_list,user_loc_list,user_gender_list,it)
            return render(request,"match.html",{"username":user_detail,"su_list":su_list})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"match.html")