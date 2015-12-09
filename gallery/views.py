from django.shortcuts import render
from .models import Before, After
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    before_images = Before.objects.all()
    after_images = After.objects.all()
    paginator = Paginator(before_images, 1)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(
        request, 'gallery/index.html', {
            'images': images,
            'after_images': after_images
        }
    )
