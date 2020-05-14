from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request
from django.http import JsonResponse
from django.template.context_processors import csrf
from .models import Post,Query_Answer,Query
from .models import Like
from datetime import datetime,date
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#from selenium import webdriver
#from bs4 import BeautifulSoup

#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

def typecon(request):
    cat=request.POST.get('cat','')
    loc=request.POST.get('location','')
    data ={} 
    if loc=='ALL' and cat=='ALL':
        context = {
        'posts': Post.objects.all(),
        'data': data,
		'today_date': date(date.today().year,date.today().month,date.today().day),
        }
    elif loc!='ALL' and cat=='ALL':
        context = {
        'posts': Post.objects.filter(location=loc) ,
        'data': data,
		'today_date': date(date.today().year,date.today().month,date.today().day),
    }
    elif loc!='ALL' and cat!='ALL':
        context = {
        'posts': Post.objects.filter(location=loc,category=cat),
        'data': data,
		'today_date': date(date.today().year,date.today().month,date.today().day),
    }        
    else:
        context = {
        'posts': Post.objects.filter(category=cat) ,
        'data': data,
		'today_date': date(date.today().year,date.today().month,date.today().day),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['today_date'] = date(date.today().year,date.today().month,date.today().day)  
        return context
    


class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-id')

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['today_date'] = date(date.today().year,date.today().month,date.today().day)
		return context
	
	

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context		
        context = super().get_context_data(**kwargs)
        
        context['today_date'] = date(date.today().year,date.today().month,date.today().day)  
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'location','seed','fertilizers','treatment_details','category','Sowing_date','Harvest_date','area','area_type','net_profit_in_INR_rupee','Tell_your_story','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','location','seed','fertilizers','treatment_details','category','Sowing_date','Harvest_date','area','area_type','net_profit_in_INR_rupee', 'Tell_your_story','image']

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


class QueryCreateView(LoginRequiredMixin, CreateView):
	model = Query 
	fields = ['category','image','Tell_your_Query']

	def form_valid(self, form):
		form.instance.user_id = self.request.user
		return super().form_valid(form)

def price(request):
    a = Rate()
    context={
        'p1_list':a.get_Rate1(),
        'p2_list':a.get_Rate2(),
        'p3_list':a.get_Rate3(),

    }
    return render(request,'blog/price.html',context)

def querygenerate(request):
	c = {}
	c.update(csrf(request))
	return render(request,'myquery.html', c)

def addquery(request):
	catagory = request.POST.get('catagorys', '')
	discription = request.POST.get('discription', '')
	images = request.FILES.get('myimage')
	u = Query(user_id=request.user,category= catagory,image = images,Tell_your_Query=discription)
	u.save()
	querys =Query.objects.filter(user_id=request.user.id,is_answer=False)
	
	c = {
		'querys':querys,
		
	}
	c.update(csrf(request))

	return render(request, 'Querys.html',c)

def myQueryans(request):
	querys =Query.objects.filter(user_id=request.user.id,is_answer=False)
	ans_query = Query.objects.filter(user_id=request.user.id,is_answer=True)
	ans_list=[]
	for a in Query_Answer.objects.all():
		for b in ans_query:
			if a.Query_id.id == b.id:
				ans_list.append(a)
	print(ans_list)
	c = {
		'querys':querys,
		'ans_query':ans_list
	}
	c.update(csrf(request))

	return render(request, 'Privious_query.html',c)
'''class Rate():
	def __init__(self):
		self.commodity = ""
		self.center = ""
		self.price = ""

	def get_Rate1(self):
		driver = webdriver.Chrome(executable_path = r'C:\chromedriver.exe',chrome_options=options)

		url = 'https://www.commodityonline.com/mandiprices/all/gujarat/0/12'

			# download html page
		driver.get(url)

			# print driver.page_source

			# create soup
		soup = BeautifulSoup(driver.page_source, 'lxml')
		div = soup.find('div', class_="boder_left_sp_bottom")

		row1=div.find_all('div',class_="row")

		#print(row1)

		#print("ROW 2\n")
		#row2=row1[4]
		#print(row1[4])

		#row2=row1.nextSibling

		#print(row2)
		#row2=div.find_all('div',class_="dt_ta_14")
		#p=div.find_all('div',class_"dt_ta_14")
		#print("parth \n")
		#print(row2)
		c_list = []
		m_list = []
		p_list = []
		Rate_list = []

		n=0
		for a in div.find_all('div',class_="dt_ta_14"):
			if(n==0):
				n=1
				p_list.append(a.text)
				#print(a.text)
			else:
				n=0

		#for a in div.find_all('div',class_="dt_ta_14"):
		#	p_list.append(a.text)
		#print(p_list)
			
		for a in div.find_all('div',class_="dt_ta_10"):
			c_list.append(a.text)
		#	print(a.text)
			
		for a in div.find_all('div',class_="dt_ta_11"):
			m_list.append(a.text)
		#	print(a.text)

		#print(p_list)
		#print(c_list)
		#print(m_list)

		for i in range(0,36):
			new_item = Rate()
			new_item.commodity = c_list[i]
			new_item.center = m_list[i]
			new_item.price = p_list[i]
			Rate_list.append(new_item)


		for one_player in Rate_list:
				print(one_player.commodity)
				print(one_player.center)
				print(one_player.price)
				print("\n")
		
		driver.quit()

		return Rate_list
		
	def get_Rate2(self):
		driver = webdriver.Chrome(executable_path = r'C:\chromedriver.exe',chrome_options=options)

		url = 'https://www.commodityonline.com/mandiprices/all/gujarat/0/12/36'

			# download html page
		driver.get(url)

			# print driver.page_source

			# create soup
		soup = BeautifulSoup(driver.page_source, 'lxml')
		div = soup.find('div', class_="boder_left_sp_bottom")

		row1=div.find_all('div',class_="row")

		#print(row1)

		#print("ROW 2\n")
		#row2=row1[4]
		#print(row1[4])

		#row2=row1.nextSibling

		#print(row2)
		#row2=div.find_all('div',class_="dt_ta_14")
		#p=div.find_all('div',class_"dt_ta_14")
		#print("parth \n")
		#print(row2)
		c_list = []
		m_list = []
		p_list = []
		Rate_list = []

		n=0
		for a in div.find_all('div',class_="dt_ta_14"):
			if(n==0):
				n=1
				p_list.append(a.text)
				#print(a.text)
			else:
				n=0

		#for a in div.find_all('div',class_="dt_ta_14"):
		#	p_list.append(a.text)
		#print(p_list)
			
		for a in div.find_all('div',class_="dt_ta_10"):
			c_list.append(a.text)
		#	print(a.text)
			
		for a in div.find_all('div',class_="dt_ta_11"):
			m_list.append(a.text)
		#	print(a.text)

		#print(p_list)
		#print(c_list)
		#print(m_list)

		for i in range(0,36):
			new_item = Rate()
			new_item.commodity = c_list[i]
			new_item.center = m_list[i]
			new_item.price = p_list[i]
			Rate_list.append(new_item)


		for one_player in Rate_list:
				print(one_player.commodity)
				print(one_player.center)
				print(one_player.price)
				print("\n")
		
		driver.quit()

		return Rate_list

	def get_Rate3(self):
		driver = webdriver.Chrome(executable_path = r'C:\chromedriver.exe',chrome_options=options)

		url = 'https://www.commodityonline.com/mandiprices/all/gujarat/0/12/72'

			# download html page
		driver.get(url)

			# print driver.page_source

			# create soup
		soup = BeautifulSoup(driver.page_source, 'lxml')
		div = soup.find('div', class_="boder_left_sp_bottom")

		row1=div.find_all('div',class_="row")

		#print(row1)

		#print("ROW 2\n")
		#row2=row1[4]
		#print(row1[4])

		#row2=row1.nextSibling

		#print(row2)
		#row2=div.find_all('div',class_="dt_ta_14")
		#p=div.find_all('div',class_"dt_ta_14")
		#print("parth \n")
		#print(row2)
		c_list = []
		m_list = []
		p_list = []
		Rate_list = []

		n=0
		for a in div.find_all('div',class_="dt_ta_14"):
			if(n==0):
				n=1
				p_list.append(a.text)
				#print(a.text)
			else:
				n=0

		#for a in div.find_all('div',class_="dt_ta_14"):
		#	p_list.append(a.text)
		#print(p_list)
			
		for a in div.find_all('div',class_="dt_ta_10"):
			c_list.append(a.text)
		#	print(a.text)
			
		for a in div.find_all('div',class_="dt_ta_11"):
			m_list.append(a.text)
		#	print(a.text)

		#print(p_list)
		#print(c_list)
		#print(m_list)

		for i in range(0,10):
			new_item = Rate()
			new_item.commodity = c_list[i]
			new_item.center = m_list[i]
			new_item.price = p_list[i]
			Rate_list.append(new_item)


		for one_player in Rate_list:
				print(one_player.commodity)
				print(one_player.center)
				print(one_player.price)
				print("\n")
		
		driver.quit()

		return Rate_list'''