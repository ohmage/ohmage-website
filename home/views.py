from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from home.models import Project, ProjectForm, PaperForm, Paper

def home(request):
    context = {
        'css': 'home-alt.css' if 'alt' in request.GET else 'home.css'
    }

    return render_to_response('ohmagehome/subviews/home.html', context, context_instance=RequestContext(request))

def usage(request):
    return render_to_response('ohmagehome/subviews/usage.html', {}, context_instance=RequestContext(request))

def projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # save the unapproved project
            form.save()
            return redirect('home:projects')
    else:
        form = ProjectForm() # An unbound form

    context = {
        'projects': Project.objects.filter(approved=True),
        'add_project_form': form
    }

    return render_to_response('ohmagehome/subviews/projects.html', context, context_instance=RequestContext(request))

def papers(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            # save the unapproved project
            form.save()
            return redirect('home:papers')
    else:
        form = PaperForm() # An unbound form

    context = {
        'papers': Paper.objects.filter(approved=True),
        'add_paper_form': form
    }

    return render_to_response('ohmagehome/subviews/papers.html', context, context_instance=RequestContext(request))

def contributors(request):
    return render_to_response('ohmagehome/subviews/contributors.html', {}, context_instance=RequestContext(request))
