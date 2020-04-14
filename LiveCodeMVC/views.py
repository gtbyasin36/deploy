from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ListProduct(request):
    mobil_tv = ProductMobil
    motor = ProductMotor
    electronics = ProductElectronics
    template_name = 'index.html'
    query = request.GET.get('q')
    obj_mobil = ProductMobil.objects.filter(name__icontains=query)
    obj_motor = ProductMotor.objects.filter(name__icontains=query)
    obj_motor = ProductMotor.objects.filter(name__icontains=query)
        
    return render(request, 'search_result.html',{
        'obj_mobil':obj_mobil,
        'obj_motor':obj_motor,
        'obj_electronics': obj_electronics,
        'query' : query,
        
    })