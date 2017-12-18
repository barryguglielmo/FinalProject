from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
def FP_Home(request):
	return render(request, 'FP_Home.html')
def Cell_and_Molecular(request):
	return render(request, 'Cell_and_Molecular.html')
def Clinical_Study(request):
	return render(request, 'Clinical_Study.html')
def Gene_Alignments(request):
	return render(request, 'Gene_Alignments.html')
def Protein_Structure(request):
	return render(request, 'Protein_Structure.html')
def Refferences_and_Resources(request):
	return render(request, 'Refferences_and_Resources.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

