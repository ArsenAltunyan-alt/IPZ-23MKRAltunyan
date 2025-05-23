from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from django.utils import timezone
from .models import Image

def gallery_view(request):
    one_month_ago = timezone.now().date() - timedelta(days=30)
    images = Image.objects.filter(created_date__gte=one_month_ago)
    return render(request, 'gallery.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {'image': image})

