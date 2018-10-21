from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the diary index.")

def detail(request, diary_id):
    return HttpResponse("%s番の日記を見ます。" % diary_id)