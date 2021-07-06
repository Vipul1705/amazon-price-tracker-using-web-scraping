from django.shortcuts import render,redirect
from django.urls.base import reverse_lazy
from .models import Link
from .forms import AddLinkForm
# from django.urls import reverse_lazys
from django.views.generic import DeleteView
# Create your views here.

def home_view(request):
    no_discounted = 0
    error = None
    form = AddLinkForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError: 
            error = "Oops...couldn't get the name or the price"
        except:
            error = "Oops..something went wrong "
        
    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no >0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            
            no_discounted = len(discount_list)
    context = {
        'qs':qs,
        'items_no':items_no,
        'no_discounted':no_discounted,
        'form':form,
        'error':error,
    }

    return render(request,'tracker/main.html', context)

class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'tracker/confirm_del.html'
    success_url = reverse_lazy('Home View')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('Home View')