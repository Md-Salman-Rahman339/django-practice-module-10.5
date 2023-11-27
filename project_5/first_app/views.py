from django.shortcuts import render
from datetime import datetime


# Create your views here.

def home(request):
    d={"author":"rahim","age":20, 
       'word':'Salman',
       'slashes':"I'm Salman Rahman",
       'nothing':'',
       'number':'21',
       'ul':['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
       'formate':'123456789564126842842585456',
       'listorder':'one, two, three',
       'publication_date': datetime.strptime("your_publication_date_string", "%Y-%m-%d %H:%M:%S"),
       'sorting':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],


       
        'lst':['python','is','best'],'birthday' :datetime.now(),'courses' : [
        
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000 
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000 
        },
    ]}
    return render(request,"home.html",d)
