from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import file
from .forms import Files
import uuid

# Create your views here.
def Home (request):
    if request.method == 'POST':
        Form = Files(request.POST, request.FILES)
        for p in request.POST:
            if p == 'fil':
                print(Form.is_valid())
                if Form.is_valid():
                    print('yes')
                    post = Form.save(commit=False)
                    post.filename = uuid.uuid1()
                    print(post.filename)
                    post.save()
                    return
    else:
        Form = Files()
    return render(request, 'site.html', {'Form': Form})