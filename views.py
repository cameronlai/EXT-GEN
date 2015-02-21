# The MIT License (MIT)

# Copyright (c) 2015 Cameron Lai

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

