# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
    # when they hit the index, we want them to see the initial flow
    context = {
    }

    return render_to_response('ohmagehome/subviews/index.html', context, context_instance=RequestContext(request))