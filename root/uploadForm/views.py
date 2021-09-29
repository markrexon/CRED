from django.shortcuts import render
from .forms import Forms 


def addData(request):
    form = Forms()
    if request.method == "POST":
        print("submitted")
        form = Forms(request.POST)
        if form.is_valid():
            form.save()
    content = {"forms": form}
    return render(request, 'index.html', content)
    