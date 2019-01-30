from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate
from .forms import CandidateModelForm
from .forms import VotesForm
from django.utils import timezone

# Create your views here.


def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)

def detail(request, candidate_id):
    context = {}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'candidate_detail.html', context)

def update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate updated')
        else:
            context['form'] = form
            return render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateModelForm(instance=candidate)
        return render(request, 'candidate_update.html', context)

def comment(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = VotesForm(request.POST, instance=candidate)
        if form.is_valid():
            comment = form.save()
            comment.candidate = candidate
            comment.save()
            return HttpResponse('Votes added')
        else:
            context['form'] = form
            return render(request, 'candidate_comment.html', context)
    else:
        context['form'] = VotesForm(instance=candidate)
        return render(request, 'candidate_comment.html', context)


def create(request):

    context = {}
    form = CandidateModelForm(initial={"bday":timezone.now()})

    if request.method == 'POST':
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate:index')

    return render(request, 'candidate_create.html', {'form': form})
