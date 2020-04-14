from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listingshofa(request):
    queryset_list = [ProductMobil.objects.all(), ProductMotor.objects.all(), ProductElectronics.objects.all()]

    paginator = Paginator(queryset_list, 2)

    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page_obj': queryset})