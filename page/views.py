from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from .models import Contact
from .models import Reservation,User,Menu,category
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from .forms import Reservation_create_form


# Create your views here.

def home(request):
    return render(request, 'page/home.html')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "page/registeration.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "page/registeration.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "page/registeration.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "page/registeration.html")

def contact(request):
    if request.method == 'POST':
        # 1: get the data from the form
        v_name = request.POST.get('name')
        v_email = request.POST.get('email')
        v_subject = request.POST.get('subject')
        v_message = request.POST.get('message')

        # 2: send this data to the DB (Models)
        v_contact = Contact(name=v_name, email=v_email, subject=v_subject, message=v_message)
        v_contact.save()
        return render(request, 'page/thank.html')
    else:
        return render(request, 'page/contact.html')


def about(request):
    return render(request, 'page/about.html')


def chatbot(request):
    return render(request, 'page/chatbot.html')


# def reservations(request):
#     if request.method == 'POST':
#         # 1: get the data from the form
#         r_name = request.POST.get('name')
#         r_email = request.POST.get('email')
#         r_phone = request.POST.get('phone')
#         r_no_of_people = request.POST.get('no_of_people')
#         r_date = request.POST.get('date')
#         r_time = request.POST.get('time')
#
#         # 2: send this data to the DB (Models)
#         r_reservations = Reservations(name=r_name, email=r_email, phone=r_phone, no_of_people=r_no_of_people,
#                                       date=r_date, time=r_time)
#         r_reservations.save()
#
#         return render(request, 'page/thank.html')
#     else:
#         return render(request, 'page/baiz.html')

class New_reservation_view(CreateView):
    model = Reservation
    template_name = "page/reservation.html"
    form_class = Reservation_create_form

    # you can provide a url with the success_url attribute
    # at which the user will be redirected to if the if listing
    # was created successfully but i have provided a url at the model
    def get_success_url(self):
        return reverse('thank')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


    @method_decorator(login_required(redirect_field_name="next", login_url="login"))
    def post(self,request,*args,**kwargs):
        return super().post(request,*args,**kwargs)

    @method_decorator(login_required(redirect_field_name="next", login_url="login"))
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)

class list_menu(ListView):
    template_name = 'menu/menu.html'


    def get_queryset(self):
        print(Menu.objects.filter(item_category = category.objects.get(item = self.kwargs['cat']).id ))
        return Menu.objects.filter(item_category = category.objects.get(item = self.kwargs['cat']).id )

def thank(request):
    return render(request,"page/thank.html")