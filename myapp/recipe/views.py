from django.shortcuts import render
from .models import *
def contribute(request):
    if request.method == 'POST':
      rname=request.POST.get("recipe_name")
      rdes=request.POST.get("description")
      rimage=request.FILES.get("image")
      Recipe.objects.create(recipe_name=rname,description=rdes,image=rimage)
    return render(request,'mainpage.html')
def main(request):
    rec_data = Recipe.objects.all()
    return render(request,'show.html',{'rec_data': rec_data})
