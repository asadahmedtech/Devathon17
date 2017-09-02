from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import problemPost, profile
from .forms import PostForm
# Create your views here.
COUNCIL_LIST = {'a':'AC','b':'HK'}

def index(request):
    return render(request, 'problempost/login.html')
def new_form(request):
    return render(request, 'problempost/prob_post.html', {'form':PostForm})
@csrf_exempt
def signin(request):
    username = request.POST['Username']
    password = request.POST['Password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/new')
    else:
        return redirect('/redirect')
def signout(request):
    logout(request)
    return redirect('/redirect')
@csrf_exempt
@login_required
def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.councilMem = assignCouncilMember(post.problemType)
            post.published_date = timezone.now()
            post.status = 'notfixed'

            post.save()
            return redirect('/show')
    else:
        form = PostForm()
    return redirect('/new')
@login_required
def post_get(request):
    posts = problemPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'problempost/show_post.html', {'posts': posts})
@login_required
def councilMemComplaint(request):
    try:
        pr = profile.objects.get(user=request.user)

        if pr is not [] and pr.councilID != None:
            complaints = problemPost.objects.filter(councilMem = pr.councilID).order_by('published_date')
            return render(request, 'problempost/show_griv_council.html', {'grivs': complaints})
    except:
        return redirect('/new')
def statuschange(request):
  if request.method == 'POST':
    recieveData = request.POST['value']
    probID = recieveData[1:]
    print(probID)
    print("okay")
    problem = problemPost.objects.filter(id = int(probID))
    problem.status = 'in progress' if probID[:1] == '1' else 'fixed'
    return redirect('/showtocouncil')
def assignCouncilMember(problemType):
    return COUNCIL_LIST[problemType]
