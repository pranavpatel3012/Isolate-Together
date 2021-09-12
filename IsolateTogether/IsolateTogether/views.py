from django.shortcuts import render
import pyrebase
from django.contrib import auth
import time
from datetime import date 


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

def whyIsolateTogether(request):
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
                return render(request,"index.html")
            return render(request,"whyIT.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"whyIT.html")


def ourServiceCard(request):
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
                return render(request,"index.html")
            return render(request,"ourService_card.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ourService_card.html")

def aboutus(request):
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
                return render(request,"aboutus.html")
            return render(request,"aboutus.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"aboutus.html")

def tips(request):
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
                return render(request,"tips.html")
            return render(request,"tips.html",{"username":user_detail})
    except:
        print("errrrrr")
    return render(request,"tips.html")

def games(request):
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
                return render(request,"games.html")
            return render(request,"games.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"games.html")


def EnterHospital(request):
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
                return render(request,"EnterHospital.html")
            return render(request,"EnterHospital.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"EnterHospital.html")


def homeRemedies(request):
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
                return render(request,"homeRemedies.html")
            return render(request,"homeRemedies.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"homeRemedies.html")

def experience(request):
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
                return render(request,"experience.html")
            return render(request,"experience.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"experience.html")


def skills(request):
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
                return render(request,"skills.html")
            return render(request,"skills.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"skills.html")


def ourService(request):
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
                return render(request,"index.html")
            return render(request,"ourService.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ourService.html")


def recoveredService(request):
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
                return render(request,"index.html")
            return render(request,"recoveredService.html",{"username":user_detail})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"recoveredService.html")




def Homea(request):
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
                return render(request,"index.html")
            return render(request,"index.html",{"username":user_detail})
    except:
        pass
    return render(request,"index.html")

def Home(request):
    print("-----------------------------------------------------------------------")
    try:
         #idtoken = request.session['uid']
            #a=authe.get_account_info(idtoken)
            #a=a['users']
            #a=a[0]
            #a=a['localId']
        a=request.session['accessToken']
        user_detail = database.child("users").child(a).child("details").child('name').get().val()
        print(user_detail)
        return render(request,"index.html",{"username":user_detail})
    except:
        pass

    return render(request,'index.html')

def myProfile(request):
    print("-----------------------------------------------------------------------")
    try:
        a=request.session['accessToken']
        user_detail = database.child("users").child(a).child("details").child('name').get().val()
        print(a)
        interests_area_dict = database.child("users").child(a).child("Interests").get().val()
        print(interests_area_dict)
        inte = database.child("users").child("details").get()
        print(inte.val())
        
        print("Outside MLModel")
        #user = database.child("users").get(idtoken)
        #print(user)    
        #interests_area = list(interests_area_dict)
        #print(interests_area)
        #interest_sub = {}
        #for i in interests_area:
        
        """
        print("---------------------bijo koi----------------")
        user_bijo = database.child("users").child('BTeQmgnwmCYzZWSQk3TK9l2KhZv2').child("details").child('name').get('eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ5YWQ5YmM1ZThlNDQ3OTNhMjEwOWI1NmUzNjFhMjNiNDE4ODA4NzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaXNvbGF0ZS10b2dldGhlci04OGI2MyIsImF1ZCI6Imlzb2xhdGUtdG9nZXRoZXItODhiNjMiLCJhdXRoX3RpbWUiOjE1OTk4OTk4ODMsInVzZXJfaWQiOiJCVGVRbWdud21DWXpaV1NRazNUSzlsMktoWnYyIiwic3ViIjoiQlRlUW1nbndtQ1l6WldTUWszVEs5bDJLaFp2MiIsImlhdCI6MTU5OTg5OTg4MywiZXhwIjoxNTk5OTAzNDgzLCJlbWFpbCI6Im1paXRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1paXRAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.zPeOJxGD5uDEiNNOZKbErWh627xv4C9qCMwsfA4eZx4U4H10UMlw6uk38qFxP1NTGSuLw7CezHRJj3z4t33GbPt--gHefEw4-BN1H7L2vLhi8efCL6WjAE6vhMpWbQeUfu3Ihrmaq88APSS0u1a7vhYTqTeruCyrvZ8paVqhdyqG8BIf2Np8Fadx3Tzdl_RkeF-14nl5crC4QmnQFa0zKrIV4w358KbSYVgao3fflIi5NmO0cZzgk2f_O8UFvnt4SRO8LX4Cz7YFG7_7vSBdzxYAjarGBpOY2lyxCU4AVbna8Kl54jVk9Yxwleh4ZWj482ujwSk3GkbDqiL_9mxz-w').val()
        print(user_bijo)
        print(database.child("users").child('BTeQmgnwmCYzZWSQk3TK9l2KhZv2').child("Interests").get('eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ5YWQ5YmM1ZThlNDQ3OTNhMjEwOWI1NmUzNjFhMjNiNDE4ODA4NzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaXNvbGF0ZS10b2dldGhlci04OGI2MyIsImF1ZCI6Imlzb2xhdGUtdG9nZXRoZXItODhiNjMiLCJhdXRoX3RpbWUiOjE1OTk4OTk4ODMsInVzZXJfaWQiOiJCVGVRbWdud21DWXpaV1NRazNUSzlsMktoWnYyIiwic3ViIjoiQlRlUW1nbndtQ1l6WldTUWszVEs5bDJLaFp2MiIsImlhdCI6MTU5OTg5OTg4MywiZXhwIjoxNTk5OTAzNDgzLCJlbWFpbCI6Im1paXRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1paXRAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.zPeOJxGD5uDEiNNOZKbErWh627xv4C9qCMwsfA4eZx4U4H10UMlw6uk38qFxP1NTGSuLw7CezHRJj3z4t33GbPt--gHefEw4-BN1H7L2vLhi8efCL6WjAE6vhMpWbQeUfu3Ihrmaq88APSS0u1a7vhYTqTeruCyrvZ8paVqhdyqG8BIf2Np8Fadx3Tzdl_RkeF-14nl5crC4QmnQFa0zKrIV4w358KbSYVgao3fflIi5NmO0cZzgk2f_O8UFvnt4SRO8LX4Cz7YFG7_7vSBdzxYAjarGBpOY2lyxCU4AVbna8Kl54jVk9Yxwleh4ZWj482ujwSk3GkbDqiL_9mxz-w').val())
        """
    except:
        print("its ans")
    
    return render(request,'welcome.html')


def postRemedies(request):
    #remedies = request.POST.get('remedies')
    try:
        a=request.session['accessToken']
        data = {
            'Remedy' : request.POST.get('remedies'),
            'user'  : a
        }
        print(data)
        millis = int(round(time.time() * 1000))
        database.child("Home Remedies").child(millis).set(data)
        user_detail = database.child("users").child(a).child("details").child('name').get().val()

        return render(request,"recoveredService.html",{"username":user_detail})
    except:
        print("errrr")
    return render(request,'signIn.html')


def postExperience(request):
    #remedies = request.POST.get('remedies')
    try:
        a=request.session['accessToken']
        data = {
            'Experience' : request.POST.get('experience'),
            'user'  : a
        }
        print(data)
        millis = int(round(time.time() * 1000))
        database.child("Experiences").child(millis).set(data)
        user_detail = database.child("users").child(a).child("details").child('name').get().val()

        return render(request,"recoveredService.html",{"username":user_detail})
    except:
        print("errrr")
    return render(request,'signIn.html')


def postSkill(request):
    #remedies = request.POST.get('remedies')
    try:
        a=request.session['accessToken']
        data = {
            'Skill' : request.POST.get('skill'),
            'user'  : a
        }
        profession = request.POST.get('profession')
        print(data,profession)
        millis = int(round(time.time() * 1000))
        database.child("Skills").child(profession).child(millis).set(data)
        user_detail = database.child("users").child(a).child("details").child('name').get().val()

        return render(request,"recoveredService.html",{"username":user_detail})
    except:
        print("errrr")
    return render(request,'signIn.html')


def postHospital(request):
    #remedies = request.POST.get('remedies')
    try:
        a=request.session['accessToken']
        state=request.POST.get('state'),
        print((state[0]))
        city =  request.POST.get('city'),
        data = {
            'Hospital' : request.POST.get('hospital'),
            'user'  : a
        }
        print(data)
        millis = int(round(time.time() * 1000))
        database.child("Hospital").child(state[0]).child(city[0]).child(millis).set(data)
        user_detail = database.child("users").child(a).child("details").child('name').get().val()

        return render(request,"recoveredService.html",{"username":user_detail})
    except:
        print("errrr")
    return render(request,'signIn.html')


def ftrExp(request):
    experience = database.child("Experiences").get().val()
    exp_list = list(experience.keys())
    user_exp_name=[]
    user_exp=[]
    print(experience)
    for i in exp_list:
        exp_temp = experience[i]
        print(exp_temp['Experience'],exp_temp['user'])
        user = database.child("users").child(exp_temp['user']).child("details").child('name').get().val()
        user_exp_name.append(user)
        user_exp.append(exp_temp['Experience'])
    print(user_exp_name,user_exp)
    exp = zip(user_exp_name,user_exp)
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
                return render(request,"ftrExp.html",{"exp":exp})

            experience = database.child("Experiences").get().val()
            print(experience)
            return render(request,"ftrExp.html",{"username":user_detail,"exp":exp})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ftrExp.html",{"exp":exp})


def ftrHR(request):

    homeRemedies = database.child("Home Remedies").get().val()
    homeRemedies_list = list(homeRemedies.keys())
    user_HR_name=[]
    user_HR=[]
    age_HR = []
    print(homeRemedies)
    for i in homeRemedies_list:
        exp_temp = homeRemedies[i]
        print(exp_temp['Remedy'],exp_temp['user'])
        user = database.child("users").child(exp_temp['user']).child("details").child('name').get().val()
        user_HR_name.append(user)
        user_HR.append(exp_temp['Remedy'])
        age = database.child("users").child(exp_temp['user']).child("details").child('age').get().val()
        age_HR.append(calculateAge(age))

    print(user_HR_name,user_HR,age_HR)
    HR = zip(user_HR_name,user_HR,age_HR)

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
                return render(request,"ftrHR.html")

            return render(request,"ftrHR.html",{"username":user_detail,'HR':HR})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ftrHR.html",{'HR':HR})


  
def calculateAge(age):
    ageInt = age.split('-')
    birthDate = date(int(ageInt[0]),int(ageInt[1]),int(ageInt[2]))
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    
    return age 


def ftrHospital(request):
    # experience = database.child("Experiences").get().val()
    # exp_list = list(experience.keys())
    # user_exp_name=[]
    # user_exp=[]
    # print(experience)
    # for i in exp_list:
    #     exp_temp = experience[i]
    #     print(exp_temp['Experience'],exp_temp['user'])
    #     user = database.child("users").child(exp_temp['user']).child("details").child('name').get().val()
    #     user_exp_name.append(user)
    #     user_exp.append(exp_temp['Experience'])
    # print(user_exp_name,user_exp)
    # exp = zip(user_exp_name,user_exp)
    print("IT is sdhcwhiu")
    try:

        state = request.POST.get('state'),
        city = request.POST.get('city'),
        print(state,city)
        hospitals = database.child("Hospital").child(state[0]).child(city[0]).get().val()
        hos_list = list(hospitals.keys())
        hos_name=[]
        for i in hos_list:
            hosp = hospitals[i]
            hos_name.append(hosp['Hospital'])
    except:
        return render(request,"ftrHospital.html")
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
                return render(request,"ftrHospital.html",{'hospital':hos_name})

            
            return render(request,"ftrHospital.html",{"username":user_detail,'hospital':hos_name})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ftrHospital.html",{'hospital':hos_name})


def ftrskill(request):
    
    print("IT is sdhcwhiu")
    try:

        profession = request.POST.get('proffesion'),
        
        print(profession)
        skills = database.child("Skills").child(profession[0]).get().val()
        skill_list = list(skills.keys())
        skill_name=[]
        for i in skill_list:
            skill = skills[i]
            skill_name.append(skill['Skill'])
    except:
        return render(request,"ftrskill.html")
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
                return render(request,"ftrskill.html",{'skills':skill_name})

            
            return render(request,"ftrskill.html",{"username":user_detail,'skills':skill_name})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"ftrskill.html",{'skills':skill_name})