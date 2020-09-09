from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from bug_app.models import MyUser, Ticket
from bug_app.forms import TicketForm, LoginForm, SignupForm


def index_view(request):
    tickets = Ticket.objects.all()
    return render(request, "index.html", {"tickets": tickets})
    
def ticket_view(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request,"ticket_detail.html",{"ticket":ticket})
   
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(request,username=data.get("username"),password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next',reverse("homepage")))


    form = LoginForm()
    return render(request,"form.html",{"form":form})  

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

@login_required
def create_ticket_view(request):
        if request.method == "POST":
            form = TicketForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                open_user=request.user,
                )
                return HttpResponseRedirect(reverse('homepage'))    
        form = TicketForm()
        return render(request, "form.html", {"form": form})
def assign_view(request,ticket_id):
    if request.method =='GET':
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.user_assigned = request.user
        ticket.status = "IN PROGRESS"
        ticket.save()
        return HttpResponseRedirect(f"/ticket/{ticket_id}")

    return render(request,"ticket_detail.html")

def completed_view(request,ticket_id):
    if request.method =='GET':
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.user_assigned=None
        ticket.user_completed=request.user
        ticket.status = "COMPLETED"
        ticket.save()
        return HttpResponseRedirect(f"/ticket/{ticket_id}")

    return render(request,"ticket_detail.html")


def invalid_view(request,ticket_id):
    if request.method =='GET':
        ticket = Ticket.objects.get(id=ticket_id)
        ticket.user_assigned=None
        ticket.user_completed=None
        ticket.status = "INVALID"
        ticket.save()
        return HttpResponseRedirect(f"/ticket/{ticket_id}")

    return render(request, "ticket_detail.html")
    
def user_view(request, username):
    tickets = Ticket.objects.all()
    user=MyUser.objects.get(username=username)
    return render(request,"user_detail.html",{"tickets":tickets,"user":user})


def edit_view(request, ticket_id):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.title = data.get("title")
            ticket.description = data.get("description")
            ticket.save()
            return HttpResponseRedirect(f"/ticket/{ticket_id}")
        
    form=TicketForm()
    return render(request,"form.html",{"form":form})