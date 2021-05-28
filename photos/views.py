from django.shortcuts import render,redirect
from .models import category,photo

# Create your views here.
def gallery(request):
    categori=category.objects.all()
    photos=photo.objects.all()
    context={
        "category":categori,
        "photo":photos,
        }
    return render(request,"photos/gallery.html",context)
#to add image to album
def add(request):
    categori=category.objects.all()
    if request.method=="POST":
        data=request.POST
        images=request.FILES.get('image')

        if data['category']!='none':
            category_=category.objects.get(id=data['category'])
        elif data['category_new']!='none':
            category_,created=category.objects.get_or_create(
                name=data['category_new']
            )
        else:
            category_= None
        
        photos=photo.objects.create(
            category=category_,
            description=data['description'],
            image=images 

        )
        return redirect('gallery')





    context={
        "categories":categori
    }
    
    return render(request,"photos/add.html",context)



#image to see in album
def image(request,pk):

    photos=photo.objects.get(id=pk)
    context={
        "photo":photos
    }
    return render(request,"photos/image.html",context)