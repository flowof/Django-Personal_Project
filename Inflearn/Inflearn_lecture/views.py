from django.shortcuts import render
from .models import myText

# Create your views here.
def home_list(request):

    texts = myText.objects.filter() # myText에 있는 모든 정보 가져와서 texts라는 변수에 저장

    print(texts)

    return render(request, 'Inflearn_lecture\home_list.html', {'texts': texts}) # texts라는 정보를 html과 함께 보여줌

def lecture_list(request):

    texts = myText.objects.filter()
    hot_lecture = myText.objects.filter(category="인기")

    return render(request, 'Inflearn_lecture\lecture_list.html',
                  {'texts': texts, 'hot_lecture': hot_lecture}
                  )

def login(request):

    return render(request, 'Inflearn_lecture\login.html')

def join(request):
    return render(request, 'Inflearn_lecture\join.html')
