from django.shortcuts import render
from .models import Question
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request,question_id):
	question = Question.objects.get(pk=question_id)
	return render(request,'index.html',{'question':question,})

def welcome(request):
	return HttpResponse("Hello, world. You're at the polls.")

def vote(request,question_id):
	#p = get_object_or_404(Question,pk=question_id)
	p = Question.objects.get(pk=question_id)
	selected_choice=p.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse("polls:welcome"))
