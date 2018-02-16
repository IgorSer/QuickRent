from django.shortcuts import render, redirect
from .models import category, item
from django.contrib.auth.decorators import login_required
from .forms import postForm
from django.views import generic
from django.views.generic import TemplateView
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    category_num = category.objects.all().count()
    item_num = item.objects.all()
    last_pub = item.objects.order_by('-date_added')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context = {
        'category': category_num,
        'item': item_num,
        'last_pub': last_pub,
        'num_visits': num_visits
    }
    return render(request, 'RentAnItem/index.html',context)

class cpost_item_view(TemplateView):
    template_name='RentAnItem/post_item.html'
    def get(self, request):
        form = postForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
        return HttpResponseRedirect('/')
#class priceViews(ListView):

def priceView(request):
    items = item.objects.all()
    pricefrom = int('0'+request.GET.get('pricefrom'))
    priceto = int('0'+request.GET.get('priceto'))
    return render(request,'RentAnItem/list_view.html',{'items':items,'a':pricefrom,'b':priceto})

#def post_item_view(request):
 #   cat = category.objects.all()
  #  post_form = postForm()
   # context = {'post_form':post_form, 'cat':cat}
    #if request.method == 'POST':
     #   if post_form.is_valid():
      #      return HttpResponseRedirect('index')
    #return render(request, 'RentAnItem/post_item.html',context)

class item_detail_view(generic.DetailView):
    model = item
    template_name = 'RentAnItem/item_detail.html'