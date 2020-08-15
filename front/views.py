from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('front/index.html')
    context = {
        'latest_question_list': 'a context',
    }
    return HttpResponse(template.render(context, request))
