from django.shortcuts import render
import pyrebase
from django.contrib import auth
import time

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

def chat(request):
    print(request.session['accessToken'])
    return render(request,'groupchat.html',{"idToken":request.session['accessToken'],"email":request.session['email']})

def sendmsg(request):
    import time
    import datetime
    from datetime import  timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    msg = request.POST.get('msg')
    user_email = request.session['email']
    print(msg,user_email)
    print(time_now,millis)
    msg_data = {
        'message' : msg,
        'user' : user_email,
    }
    database.child("chatsroom").child(millis).set(msg_data)
    #timestamps = database.child("chatsroom").shallow().get().val()
    #print(database.child("chatrooms").child().get().val())
    #print(timestamps)

    idtoken = request.session['accessToken']
    # a=authe.get_account_info(idtoken)
    # a=a['users']
    # a=a[0]
    # a=a['localId']
    a=idtoken

    timestamps = database.child("chatsroom").shallow().get().val()
    lis_time=[]
    for i in timestamps:
        lis_time.append(i)

    message = []
    user_list = []
    date_list = []
    lis_time.sort(reverse=True)
    for i in lis_time:
        msg = database.child("chatsroom").child(i).child('message').get().val()
        user = database.child("chatsroom").child(i).child('user').get().val()
        message.append(msg)
        user_list.append(user)
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date_list.append(dat)

    chat = zip(date_list,message,user_list)
    """
    for i in lis_time:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date_list.append(dat)
    """
    #print(chat)
    print(date_list)
    print(message)
    print(user_list)


    return render(request,'chat.html',{"chat":chat})

    #return render(request,'chat.html',{"idToken":request.session['uid']})

def checkmsg(request):

    import datetime

    idtoken = request.session['accessToken']
    # a=authe.get_account_info(idtoken)
    # a=a['users']
    # a=a[0]
    # a=a['localId']
    a=idtoken
    timestamps = database.child("chatsroom").shallow().get().val()
    lis_time=[]
    for i in timestamps:
        lis_time.append(i)

    message = []
    user_list = []
    date_list = []
    lis_time.sort()
    for i in lis_time:
        msg = database.child("chatsroom").child(i).child('message').get().val()
        user = database.child("chatsroom").child(i).child('user').get().val()
        message.append(msg)
        user_list.append(user)
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date_list.append(dat)

    chat = zip(date_list,message,user_list)
    """
    for i in lis_time:
        i = float(i)
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date_list.append(dat)
    """
    #print(chat)
    print(date_list)
    print(message)
    print(user_list)

    return render(request,'checkmsg.html',{"chat":chat})

def getChat(request):
    try:
        if request.session['accessToken']:
            a=request.session['accessToken']
            user_detail = database.child("users").child(a).child("details").child('name').get().val()
            print(user_detail)
            
            if user_detail == "anonymoususer":
                print("hello")
                return render(request,"ftrHR.html")
            user_id = request.GET.get('user_id')
            print(user_id)
            chatId = getChatID(a,user_id,user_detail)
            print(chatId)
            return render(request,"chat.html",{"username":user_detail,"chatId":chatId['chatId'],"recUser":chatId['user']})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"signIn.html")

def getGroupChat(request):
    try:
        if request.session['accessToken']:
            a=request.session['accessToken']
            user_detail = database.child("users").child(a).child("details").child('name').get().val()
            print(user_detail)
            
            if user_detail == "anonymoususer":
                print("hello")
                return render(request,"ftrHR.html")
            chatName = request.GET.get('chatName')
            print(chatName)
            
            return render(request,"chat.html",{"username":user_detail,"chatId":chatName,"recUser":chatName})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"signIn.html")

def getChatID(a,user_id,uname):
    print("Inside getChatId")
    try:
        chatId = database.child("users").child(a).child("Chats").child(user_id).get().val()
        print(chatId)
        if chatId is not None:
            #chatId = (chatId)
            return chatId

        millis = int(round(time.time() * 1000))
        NullData ={
            'user1' : a,
            'user2' : user_id
        }
        database.child("Chats").child(millis).set(NullData)
        database.child("Chats").child(millis).remove()
        chatId = millis
        data = {
            'user' : uname,
            'chatId' : chatId
        }
        database.child("users").child(user_id).child("Chats").child(a).set(data)
        data['user'] = database.child("users").child(user_id).child("details").child('name').get().val()
        database.child("users").child(a).child("Chats").child(user_id).set(data)
        return data
    except:
        print("eooorr")
        return


def savedChats(request):
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
                return render(request,"signIn.html")
            savedChats = database.child("users").child(a).child("Chats").get().val()
            chat_keys = list(savedChats.keys())
            user_name_list=[]
            user_loc_list=[]
            user_gender_list=[]
            userId_list=[]
            
            for i in chat_keys:
                user_details =  database.child("users").child(i).child("details").get().val()
                user_name_list.append(user_details['name'])
                user_loc_list.append(user_details['country'])
                user_gender_list.append(user_details['gender'])
                userId_list.append(i)
                
            print(user_name_list,user_loc_list,user_gender_list,userId_list)
            chat_list = zip(user_name_list,user_loc_list,user_gender_list,userId_list)
            return render(request,"savedChats.html",{"username":user_detail,"chat_list":chat_list})
            #return render(request,"index.html",{"username":request.session['username']})
    except:
        print("errrrrr")
    return render(request,"signIn.html")