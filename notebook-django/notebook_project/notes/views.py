from django.shortcuts import render

# Create your views here.
mynotes =[{'id':1,'title':'First Note ','Entries':['Entry 1.1','Entry 1.2','Entry 1.2']},
          {'id':2,'title':'Second Note','Entires':['Entry 2.1','Entry 2.2','Entry 2.3']},
          {'id':2,'title':'Second Note','Entires':['Entry 3.1','Entry 3.2','Entry 3.3']},
          ]

def home(request):
    return render(request,'notes/index.html')

def notes(request):
    context = {'mynotes':mynotes}
    return render(request,'notes/notes.html',context)

def note(request,note_id):
    for mynote in mynotes:
        if mynote['id'] == note_id:
            note = mynote
        
    entries = note['Entries']
    
    contex = {'note':note , 'entries':entries}
    
    return render(request,'notes/note.html',contex)