from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request
from django.http import JsonResponse
from .models import Post
from .models import Like
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def typecon(request):
    cat=request.POST.get('cat','')
    loc=request.POST.get('location','')
    data ={} 
    if loc=='ALL' and cat=='ALL':
        context = {
        'location':Post.objects.values('location').distinct(),
        'cat':Post.objects.values('category').distinct(),
        'posts': Post.objects.all(),
        'data': data,
        }
    elif loc!='ALL' and cat=='ALL':
        context = {
        'location':Post.objects.values('location').distinct(),
        'posts': Post.objects.filter(location=loc) ,
        'cat':Post.objects.values('category').distinct(),
        'data': data,
    }        
    else:
        context = {
        'location':Post.objects.values('location').distinct(),
        'posts': Post.objects.filter(category=cat) ,
        'cat':Post.objects.values('category').distinct(),
        'data': data,
    }
    return render(request, 'blog/home.html', context)

'''def home(request):
    if request.method == 'POST': 
        city = request.POST.get('city','') 
         api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
           "http://api.openweathermap.org/data/2.5/weather?q="+city +"&APPID=47ac36fecbf7e55eee286bef7823f521").read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        print(list_of_data)
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
    context = {
        'location':Post.objects.values('location').distinct(),
        'cat':Post.objects.values('category').distinct(),
        'posts': Post.objects.all(),
        'data': data,
        'likes':Like.objects.all(),
    }
    return render(request, 'blog/home.html', context)'''

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','location','seed','fertilizers','treatment_details','category','Sowing_date','Harvest_date','area','net_profit','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','location','seed','fertilizers','treatment_details','category','Sowing_date','Harvest_date','area','net_profit','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    if request.method == 'POST': 
        city = request.POST.get('city','') 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
           "http://api.openweathermap.org/data/2.5/weather?q="+city +"&APPID=47ac36fecbf7e55eee286bef7823f521").read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        print(list_of_data)
        if source == None:
            data="not found"            
        else:
        # data for variable list_of_data 
            data = { 
                "country_code": str(list_of_data['sys']['country']), 
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                            + str(list_of_data['coord']['lat']), 
                "temp": str(list_of_data['main']['temp']) + 'k', 
                "pressure": str(list_of_data['main']['pressure']), 
                "humidity": str(list_of_data['main']['humidity']), 
            } 
            print(data) 
    else: 
        data ={} 
    context = {
        'data': data,
    }
    return render(request, 'blog/about.html',context)

def like(request):
    postid=request.GET.get('postid','')
    post=Post.objects.get(id=postid)
    print(post.likes.all())
    l=Like(user_id=request.user,Post_id=post)
    l.save()
    return JsonResponse("success",safe=False)

def disLike(request):
    print("ret")
    postid=request.GET.get('postid','')
    post=Post.objects.get(id=postid)
    like = Like.objects.filter(user_id=request.user,Post_id=post)
    like.delete()   
    return JsonResponse("success",safe=False)