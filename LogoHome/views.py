from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect
# from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Suppliers, Hats

from django.utils import timezone
import datetime

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'LogoHome/index.html'
    context_object_name = 'latest_suppliers_list'

    def get_queryset(self):
        """ return the last three registrated suppliers (not including those who set to be published in the future) """
        # return Suppliers.objects.order_by('-registration_date')[:4]
        return Suppliers.objects.filter(registration_date__lte=timezone.now()).order_by('-registration_date')[:4]

#def myindex(request):
#    latest_suppliers_list = Suppliers.objects.order_by('-registration_date')[:3]
##    output = ', '.join([s.no_char for s in latest_suppliers_list])
##    template = loader.get_template('LogoHome/index.html')
#    context = {
#        'latest_suppliers_list': latest_suppliers_list,
#    }
##    return HttpResponse(template.render(context, request))
#    return render(request, 'LogoHome/index.html', contex)

class DetailView(generic.DetailView):
    model = Suppliers
    template_name = 'LogoHome/detail.html'

    def get_queryset(self):
        """ Excludes any supplier who are not registered yet. """
        return Suppliers.objects.filter(registration_date__lte=timezone.now())


# def suppliername(request, id):
#     response = "This supplier's name has the no of %s."
#     return HttpResponse(response %id)

class ResultsView(generic.DetailView):
    model = Suppliers
    template_name = 'LogoHome/results.html'

# def supplierlocation(request, id):
#     return HttpResponse("This supplier's location has the no of %s." %id)

# def detail(request, id):
#     # try:
#     #     suppliers = Suppliers.objects.get(pk=suppliersno_id)
#     # except Suppliers.DoesNotExist:
#     #     raise Http404("Suppliers does not exist")
#     suppliers = get_object_or_404(Suppliers, pk=id)
#     return render(request, 'LogoHome/detail.html', {'suppliers': suppliers})

def type(request, supplier_id):
    supplier = get_object_or_404(Suppliers, pk=supplier_id)
    try:
        selected_hat = supplier.hats_set.get(pk=request.POST['hats'])
    except (KeyError, Hats.DoesNotExist):
        return render(request, 'LogoHome/detail.html', {
            'supplier': supplier,
            'error_message': "You didn't select a hat.",
        })
    else:
        selected_hat.memo_text = "Selected - " + str(datetime.datetime.now())
        selected_hat.save()

        return HttpResponseRedirect(reverse('LogoHome:results', args=(supplier.id,)))

def results(request, supplier_id):
    supplier = get_object_or_404(Suppliers, pk=supplier_id)
    return render(request, 'LogoHome/results.html', {'supplier': supplier})