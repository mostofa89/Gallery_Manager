from django.contrib import messages as message
from django.shortcuts import render, redirect
from .models import UploadedImage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user:login')
def gallery_view(request):
    gallery = UploadedImage.objects.filter(user=request.user)
    return render(request, 'Gallery/gallery.html', {'gallery': gallery})


@login_required(login_url='user:login')
def upload_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        UploadedImage.objects.create(
            title=title,
            description=description,
            image=image,
            user=request.user
        )
        message.success(request, 'Image uploaded successfully.')
        return redirect('gallery:gallery')
    

    return render(request, 'Gallery/upload.html') 


@login_required(login_url='user:login')
def delete_image_view(request, image_id):
    try:
        image = UploadedImage.objects.get(id=image_id, user=request.user)
        image.delete()
        message.success(request, 'Image deleted successfully.')
        
    except UploadedImage.DoesNotExist:
        message.error(request, 'Image not found or you do not have permission to delete it.')
    
    return redirect('gallery:gallery')


@login_required(login_url='user:login')
def edit_image_view(request, image_id):
    try:
        image = UploadedImage.objects.get(id=image_id, user=request.user)
    except UploadedImage.DoesNotExist:
        message.error(request, 'Image not found or you do not have permission to edit it.')
        return redirect('gallery:gallery')

    if request.method == 'POST':
        image.title = request.POST.get('title')
        image.description = request.POST.get('description')
        if 'image' in request.FILES:
            image.image = request.FILES.get('image')
        image.save()
        message.success(request, 'Image updated successfully.')
        return redirect('gallery:gallery')

    return render(request, 'Gallery/edit.html', {'image': image})