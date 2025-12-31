from django.contrib import messages as message
from django.shortcuts import render, redirect
from .models import UploadedImage

# Create your views here.
def gallery_view(request):
    gallery = UploadedImage.objects.filter(user=request.user)
    return render(request, 'Gallery/gallery.html', {'gallery': gallery})


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
        return redirect('gallery')
    

    return render(request, 'Gallery/upload.html')       