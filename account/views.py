from django.shortcuts import render,redirect
from .forms import AccountForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('account:signin')

def register(request):
    form = AccountForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = (request.POST["username"]).lower()
            email = (request.POST["email"]).lower()
            phone_number = request.POST["phone_number"]
            sex = request.POST["gender"]
            city = request.POST["city"]
            country = request.POST["country"]
            password1 = request.POST["password1"]
            password2 = request.POST["password1"]
            obj = Account.objects.filter(username=username, email=email).exists()
            print(obj)
            #Demo.objects.filter(category_id=23, subcategory_id=1, post_id=445).exists()

            #print(obj.username)
            #instance = form.save(False)
            if (not obj) and (password1==password2):
                #instance.password = password1
                #instance.save()
                user = Account.objects.create_user(first_name, last_name,username,email,sex,phone_number,city,country, password1)
                user.save()
                account = authenticate(email=email, password=password1)
                login(request, account)
                return redirect('account:signin')
            else: 
                print('Ay aay ay ay co rui')
            
            #do more action with data
            #return redirect success view
    context = {
        'form':form
    }

    return render(request,'my_tmp/reg.html', context)


def signin(request):

    context = {}
    login_message= ""
    user = request.user
    if user.is_authenticated: 
        return redirect("my_app:index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = (request.POST['email']).lower()
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("my_app:index")
            else:
                login_message = "Opp something went wrong. Maybe you do not have account or wrong password"
                print("Login mess : " + login_message)

    else:
        form = AccountAuthenticationForm()
        
    #print("Login mess : " + login_message)
    context = {
        'login_form': form,
        'login_message': login_message
    }

    # print(form)
    return render(request, "my_tmp/signin.html", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = AccountForm()
        context['AccountForm'] = form
    return render(request, 'my_tmp/signin.html', context)



def account_view(request):

	if not request.user.is_authenticated:
			return redirect("account:signin")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	#blog_posts = BlogPost.objects.filter(author=request.user)
	#context['blog_posts'] = blog_posts

	return render(request, "my_tmp/account.html", context)