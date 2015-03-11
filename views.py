from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import Context, Template

from models import UploadFileForm
from models import extGenOptimizer1

OPTIONS = """
header: {
left:  'prev,next today',
center: 'title',
right: 'month,agendaWeek',
},
defaultView: 'agendaWeek',
editable: true,
eventLimit: true, // allow "more" link when too many events
scrollTime: '08:00:00',
"""

# Create your views here.
def index(request):
    indexContext = {}
    indexContext['fileReturnError'] = 'false'
    events = 'events:[],'
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myOptimizerParser = extGenOptimizer1()
            events = myOptimizerParser.run(request.FILES)
            # indexContext['fileReturnError'] = 'true'
    else:
        form = UploadFileForm()
    
    indexContext['form'] = form
    indexContext['calendar_config_options'] = OPTIONS
    indexContext['calendar_events'] = events
    return render(request, 'EXT_GEN/index.html', indexContext)

