from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from Expert.models import Expert
from blog.models import Query,Query_Answer
from .forms import ExpertRegisterForm,UserUpdateForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    try:
        if username == 'admin'  or password == 'admin':
            request.session['username'] = username
            return redirect('/Expert/expertverify/') 
        else:
            user = Expert.objects.get(username=username)
            if user.password == password:
                if user.is_valid == True:
                    request.session['username'] = username
                    print(request.session['username'])
                    return HttpResponseRedirect('/Expert/loggedin/')
                else:
                    messages.info(request, 'You are not varify ')
                    return HttpResponseRedirect('/Expert/login/')
            else:
                return HttpResponseRedirect('/Expert/invalidlogin/')
    except Expert.DoesNotExist:
        return HttpResponseRedirect('/Expert/userdoesnotexist')


def loggedin(request):
    username = request.session['username'] 
    print(username)
    if username == None:
        return redirect('/Expert/login/')
    else:
        expert = Expert.objects.get(username = request.session['username'] )
        print(expert.category)
        queries= Query.objects.filter(category = expert.category,is_answer = False)
        print(queries)
        c={
            'queries' : queries
        }
    return render(request,'loggedin.html', c)

def invalidlogin(request):

    return render(request,'invalidlogin.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
        return render(request,'login.html')
    else:
        return render(request,'login.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', c)

def userdoesnotexist(request):
    c = {}
    c.update(csrf(request))
    return render(request,'userdoesnotexist.html', c)

def register(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ExpertRegisterForm(request.POST,request.FILES)
        print("reach here")
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            print("reach here")
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! ,Your account has been created! You are now able to log in')
            return redirect('/Expert/login/')
    else:
        form = ExpertRegisterForm()
    return render(request, 'Expert/register.html', {'form': form})

def submitanswer(request):
    ans = request.POST.get("reply",'')
    qid = request.POST.get("qid",'')
    print(qid)
    Q =Query_Answer(Query_id=Query.objects.get(id=qid),Query_Reply = ans , Expert_id = Expert.objects.get(username=request.session['username']))
    Q.save()
    Q = Query.objects.get(id = qid)
    Q.is_answer= True
    Q.save()
    return redirect('/Expert/loggedin')

def allansQuery(request):
    expert = Expert.objects.get(username = request.session['username'] )
    que = Query_Answer.objects.filter(Expert_id = expert.id)
    c={
        'que': que
    }
    return render(request,'Past_ans.html', c)


def updateQueryans(request):
    if request.method == 'POST':
        ans = request.POST.get("qans",'')
        qid = request.POST.get("qid",'')
        request.session['qid'] = qid
    else:
        ans = request.POST.get("qans",'')
        qid = request.POST.get("qid",'')
        request.session['qid'] = qid
    context = {
        'ans': ans
    }
    return render(request, 'Expert/Update_Query.html', context)

def updatedans(request):
    ans = request.POST.get("update_ans",'')
    qid = request.session['qid']
    q = Query_Answer.objects.get(id = qid)
    q.Query_Reply = ans
    q.save()
    return redirect('/Expert/allansQuery/')

def expertverify(request):
    username = request.session['username']
    experts=Expert.objects.filter(is_valid = False)
    c={
        'experts':experts,
        'username': username
    }
    return render(request, 'desktop.html', c)

def varify(request):
    ans=request.POST.get("message",'')
    eid=request.POST.get("eid",'')
    print(ans)
    if ans == "success":
        expert = Expert.objects.get(id = eid)
        expert.is_valid =True
        expert.save()
    elif ans == "reject":
         expert = Expert.objects.get(id = eid)
         expert.delete()
    return redirect('/Expert/expertverify/')
