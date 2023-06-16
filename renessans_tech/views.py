from django.shortcuts import render

# Create your views here.

def fun1(request):
    name = 'x'
    context = {'name':name}
    return render(request=request, template_name='renessans_tech/index.html', context=context)
