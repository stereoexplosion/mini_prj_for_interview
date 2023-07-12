from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import FileRequestForm
import re

from .models import FileRequest


def do_count(file, put_word):
    with open(f'media/uploads/{file}', 'r', encoding="utf-8") as f_input:
        count = 0
        list_data = f_input.read()
        list_data = re.sub(r'[^\w\s]', '', list_data).split()
        for word in list_data:
            if word == put_word:
                count += 1
        return count


@csrf_exempt
def count_view(request):
    wordcount = None
    if request.method == 'POST':
        if 'delete' in request.POST:
            FileRequest.objects.all().delete()
            form = FileRequestForm()
        else:
            form = FileRequestForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                word = form.cleaned_data['word_to_find']
                form.save()
                wordcount = do_count(file, word)
                return render(request, 'default.html', {'form': form, 'wordcount': wordcount})
    else:
        form = FileRequestForm()
    return render(request, 'default.html', {'form': form, 'wordcount': wordcount})
