from django.http import HttpResponse, HttpResponseRedirect#, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.template import RequestContext, loader
from store import models
from carton.cart import Cart
from django.utils import translation
#auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.contrib.auth.models import User
from store.models import Address
#from django.utils.translation import ugettext as _

#pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#import json

# Create your views here.


#pagination
def shop(request):
	product_list = models.Product.objects.all()
	paginator = Paginator(product_list, 16) # Show 16 contacts per page

	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
	   products = paginator.page(1)
	except EmptyPage:
	   # If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)

	return render(request,'store/shop.html', {"products": products, 'site_title':"Shop | Natural Guide"})


def index(request):
	context = {
		'product_list': models.Product.objects.order_by('-category')[:5],
		'product_list_recommended': models.Product.objects.filter(is_recommended=True),
		'product_list_popular': models.Product.objects.filter(is_popular=True),
		'product_list_new': models.Product.objects.filter(is_new=True),
		'product_list_sale': models.Product.objects.filter(is_on_sale=True),

		'site_title':"Home | Natural Guide"
		}
	context.update(csrf(request))
	return render(request, 'store/index.html', context,)

def details(request, id):
	product =get_object_or_404(models.Product, pk=id)
	return render(request, 'store/product-details.html',{'product':product, 'product_list_recommended':models.Product.objects.filter(is_recommended=True), 'site_title':"Details | Natural Guide"})

def contact_us(request):
	context = {

		'site_title': "Contact | Natural Guide"
		}
	return render(request, 'store/contact-us.html', context)

def about_us(request):
	context = {
		'site_title':"About | Natural Guide"
		}
	return render(request, 'store/about-us.html', context,)
##def shop(request):
###    context = {
###        'product_list': models.Product.objects.order_by('-id')[:10]
###        }
##    return render(request, 'store/shop.html')

def checkout(request):
	context = {
		'product_list': models.Product.objects.order_by('-category')[:10]
		}
	return render(request, 'store/checkout.html', context)

def showcart(request):
	context = {
		'site_title':"Your cart | Natural Guide"
	}
	return render(request, 'store/cart.html', context)

def add(request, id):
	cart = Cart(request.session)
	product = get_object_or_404(models.Product, pk=id)
	cart.add(product, price=product.price)
	return HttpResponse(product.price)

def remove(request, id):
	cart = Cart(request.session)
	product = get_object_or_404(models.Product, pk=id)
	cart.remove(product)
	return HttpResponseRedirect('../../../cart/showcart')

def remove_single(request, id):
	cart = Cart(request.session)
	product = get_object_or_404(models.Product, pk=id)
	cart.remove_single(product)
	return HttpResponse({product.price:'pr' })

#def switch_language(request):
	#return HttpResponse("")

def search(request):
	if 'q' in request.POST and request.POST['q']:
		q = request.POST['q']
		products = models.Product.objects.filter(name__icontains=q)
		return render(request, 'store/search-results.html',
			{'products': products, 'query': q, 'product_list_recommended': models.Product.objects.filter(is_recommended=True)})
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

def categories(request, cat):
	products = models.Product.objects.filter(category__iexact=cat)  #__iexact helps to ignore case sensitivity, e.g. Body=body, Verana=verana
	context = {
		'site_title': 'Natural Guide | ' + cat.capitalize(),        #Category name starts with the capital letter - cat.capitalize()
		'products': products,
		'product_list_recommended': models.Product.objects.filter(is_recommended=True),
		'cat': cat
	}  
	return render(request, 'store/search-results.html', context)

def brands(request, br):
	products = models.Product.objects.filter(brand__iexact=br)  #__iexact helps to ignore case sensitivity, e.g. Body=body, Verana=verana
	context = {
		'site_title': 'Brands: ' + br.capitalize(),             #Brend name starts with the capital letter - br.capitalize()
		'products': products,
		'product_list_recommended': models.Product.objects.filter(is_recommended=True),
		'cat': br
	}  
	return render(request, 'store/search-results.html', context)

def search_results(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

#auth login

def auth_view(request):
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			if request.user.first_name and request.user.last_name:
				request.session['welcome'] = request.user.first_name+" "+request.user.last_name
			else:
				request.session['welcome'] = username
			return HttpResponseRedirect('/')
		else:
			request.session['error'] = 'Invalid credentials!'
			return HttpResponseRedirect('/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

#auth register
##def sign_up(request):
##    return render_to_response('store/login.html',
##                        {'site_title':"Signup | Natural Guide"})




##def register_user(request):
##    if request.method == 'POST':
##        form = MyRegistrationForm(request.POST)
##        if form.is_valid():
##            form.save()
##            message="success"
##            return HttpResponse(message)
##    args = {}
##    args.update(csrf(request))
##
##    args['form'] = MyRegistrationForm()
##
##    return render_to_response('store/login.html', args)

def register_user(request):
	if request.method == 'POST':
		firstName = request.POST.get('firstName', False)
		secondName = request.POST.get('secondName', False)
		email = request.POST.get('email', False)
		password = request.POST.get('password1', False)
		country = request.POST.get('country', False)
		postal_code = request.POST.get('postal_code', False)
		city = request.POST.get('city', False)
		address = request.POST.get('address', False)

		if not User.objects.filter(username__iexact=email).exists():

			if email and password and country and postal_code and city and address and firstName and secondName:
				#user = User.objects.create_user(username1,email,password)
				a = User.objects.create_user(email,email,password)
				a.first_name = firstName
				a.last_name = secondName
				a.save()
				user = Address()
				user.user = a
				user.country = country
				user.city = city
				user.postal_code = postal_code
				user.address = address
				user.save()
				message = "You are successfuly registered"
				return HttpResponse(message)
			elif email and password:
				a = User.objects.create_user(email, email, password)
				a.save()
				message = "You are successfuly registered"
				return HttpResponse(message)
			else:
				message = "denied"
				return HttpResponse(message)
		else:
			message = "your email is already in use"
			return HttpResponse(message)

	args = {}
	args.update(csrf(request))

	#args['form'] = MyRegistrationForm()

	return render(request, 'store/login.html', args)