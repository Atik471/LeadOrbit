from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_details(request, pk):
    
    
    lead = get_object_or_404(Lead, id=pk)
        
    context = {
        'lead': lead
    }
    
    return render(request, "leads/lead_details.html", context)
    
    
def lead_create(request):
    form = LeadModelForm()
    
    if request.method == 'POST':
        print("Recieving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("Lead is created")
            return redirect('/leads')
        
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


'''
def lead_create(request):
    form = LeadForm()
    
    if request.method == 'POST':
        print("Recieving a post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data["first_name"]
            last_name = data["last_name"]
            age = data["age"]
            agent = Agent.objects.first()
            
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("Lead is created")
            return redirect('/leads')
        
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
'''


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    
    form = LeadModelForm(instance=lead)
    
    if request.method == 'POST':
        print("Recieving a post request")
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            print("Lead is updated")
            return redirect('/leads')
    
    
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context)
    
    
    
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')