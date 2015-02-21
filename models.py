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

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django import forms

from datetime import datetime, timedelta
from extGenOptimizer import extGenOptimizer

import csv
import json
import re

# Create your models here.
class UploadFileForm(forms.Form):
    studentRecordFile = forms.FileField()
    timeSlotFile = forms.FileField()

# This model parses the CSV input file into the format 
# and passes to the optimizer
class extGenOptimizer1():
    def __init__(self):
        self.examEvents = []
        self.dateFormat = "%Y-%m-%d"
        self.timeFormat = "%Y-%m-%dT%H:%M:%S"
        self.inputDateTimeFormat = "%Y-%m-%d, %H:%M"
        
    def run(self, uploadFiles):
        self.addStudentRecords(uploadFiles['studentRecordFile'])
        self.addTimeSlots(uploadFiles['timeSlotFile'])
        self.runOptimizer()
        return self.getJSONdump()

    def convertScheduleToExamEvents(self):
        self.examEvents = []
        for item in self.schedule:
            self.addExamEvent(item[0], item[1], item[2])
        for item in self.timeSlots:
            self.addBackgroundTimeSlots(item[0], item[1])

    def addExamEvent(self, title, start, end):
        examEvent = {}
        examEvent['title'] = title
        examEvent['start'] = start
        examEvent['end'] = end
        examEvent['description'] = ''
        self.examEvents.append(examEvent)

    def addBackgroundTimeSlots(self, start, end):
        backgroundTimeSlot = {}
        backgroundTimeSlot['id'] = 'timeSlots'
        backgroundTimeSlot['start'] = start
        backgroundTimeSlot['end'] = end
        backgroundTimeSlot['rendering'] = 'background'
        backgroundTimeSlot['description'] = ''
        self.examEvents.append(backgroundTimeSlot)

    def addStudentRecords(self, studentRecordFile):
        tmpFile = NamedTemporaryFile()
        for chunk in studentRecordFile.chunks():
            tmpFile.write(chunk)
        tmpFile.seek(0)
        self.studentRecords = [row for row in csv.reader(tmpFile)]
        tmpFile.close()
        # Remov header
        self.studentRecords = self.studentRecords[1:]
        return True

    def addTimeSlots(self, timeSlotFile):
        tmpFile = NamedTemporaryFile()
        for chunk in timeSlotFile.chunks():
            tmpFile.write(chunk)
        tmpFile.seek(0)
        tmpTimeSlot = [row for row in csv.reader(tmpFile)]
        tmpFile.close()
        # Remov header
        tmpTimeSlot = tmpTimeSlot[1:]
        # Parse string to actual time
        self.timeSlots = []
        for t in tmpTimeSlot:
            try:
                startTime = datetime.strptime(t[0]+", "+t[1], 
                                              self.inputDateTimeFormat)
                endTime = datetime.strptime(t[0]+", "+t[2], 
                                            self.inputDateTimeFormat)
            except:
                return False
            self.timeSlots.append([startTime, endTime])
        return True

    def runOptimizer(self, verbose=False):
        myOptimizer = extGenOptimizer()
        myOptimizer.timeSlots = self.timeSlots
        myOptimizer.studentRecord = self.studentRecords
        self.schedule = myOptimizer.run(verbose=verbose)
        self.convertScheduleToExamEvents()
            
    def getJSONdump(self):
        # Sort the exam events
        self.examEvents = sorted(self.examEvents, key = lambda e: e['start'])
        # Get first exam date
        firstExamTime = datetime.strftime(self.examEvents[0]['start'], 
                                          self.dateFormat)
        defaultDateReturnString = "defaultDate: " +  \
                                  json.dumps(firstExamTime) + ","
        # Put exam events into event JSON object
        for e in self.examEvents:
            e['start'] = datetime.strftime(e['start'], self.timeFormat)
            e['end'] = datetime.strftime(e['end'], self.timeFormat)
            e['description'] = str(e['description'])
        eventReturnString = 'events:' + json.dumps(self.examEvents) + ','
        return defaultDateReturnString + eventReturnString

if __name__ == "__main__":
    t = extGenOptimizer1()

    f = File(open('static/forms/timeSlots.csv'))
    t.addTimeSlots(f)
    f.close()

    f = File(open('static/forms/studentRecords.csv'))
    t.addStudentRecords(f)
    f.close()

    t.runOptimizer(verbose=True)

    print 'JSON'
    print t.getJSONdump()

