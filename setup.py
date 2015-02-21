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

import pip
import os

projectName = ''

def install(package):
    pip.main(['install', package])

def installAll():
    allPackages = [
        'deap',
        'numpy',
        'tabulate',
    ]
    for p in allPackages:
        install(p)

def getProjectName():
    initialDir = os.getcwd()
    os.chdir('../')
    dirList1 = os.listdir('.')
    dirList2 = os.listdir('..')
    tmpSet = set(dirList1).intersection(set(dirList2))
    tmpList = list(tmpSet)
    if len(tmpSet) == 0:
        print 'Cannot find project name'
    else:
        projectName = tmpList[0]
        print 'Project name = ' + projectName
    os.chdir(initialDir)

#Main
if __name__ == '__main__':
    installAll()
