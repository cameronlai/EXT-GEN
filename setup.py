import pip
import os

projectName = ''

def install(package):
    pip.main(['install', package])

def installAll():
    allPackages = [
        'deap',
        'numpy',
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
