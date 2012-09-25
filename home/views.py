from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from home.models import Project, ProjectForm

def home(request):
    return render_to_response('ohmagehome/subviews/home.html', {}, context_instance=RequestContext(request))

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
    return render_to_response('ohmagehome/subviews/papers.html', {}, context_instance=RequestContext(request))

def contributors(request):
    return render_to_response('ohmagehome/subviews/contributors.html', {}, context_instance=RequestContext(request))
