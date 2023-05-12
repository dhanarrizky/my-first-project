from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
#from django.template import loader
from .models import Members
from django.db.models import Q

def members(request):
#    template = loader.get_template('index.html')
    mymembers = Members.objects.all().values
    context = {'mymembers' : mymembers,}
    return render(request,'all_members.html',context)

def details(request,id):
    mymembers = Members.objects.get(id=id)
    context = {'mymembers':mymembers}
    return render(request,'detail.html',context)

def main(request):
    return render(request,'main.html')

def testing(request):
    mymembers = Members.objects.all()
    mydata = Members.objects.filter(firstname='dhanar').values()#values_list('firstname')
    #mydata di gunakkan untuk mencari suatu object atau mengambil data dari database dengan values yang sama adalah firstname yaitu dhanar
    #pengambilan data di atas seperti => SELECT * FROM members WHERE firstname = 'Emil';
    
    #ada juga cara pencarian lain
    mydata2 = Members.objects.filter(lastname='Refsnes', id=2).values()
    # pengambilan data di atas seperti => SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;
    
    mydata3 = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()
    # pengambilan data di atas seperti => SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';
    
    mydata4 = Members.objects.filter(firstname__startswith='L').values()
    # pengambilan data di atas seperti => WHERE firstname LIKE 'L%'


    context = {
        #'fruits':['apple','banana','cherry'],
        #'mymembers':mymembers,
        'mymembers' : mydata,
    }
    return render(request,'template.html',context)


    #ada juga untuk mendapatkan atau order
    '''
    mydata = Member.objects.all().order_by('firstname').values()
    --> SELECT * FROM members ORDER BY firstname;
    
    mydata = Member.objects.all().order_by('-firstname').values()
    -->SELECT * FROM members ORDER BY firstname DESC;
    
    mydata = Member.objects.all().order_by('lastname', '-id').values()
    -->SELECT * FROM members ORDER BY lastname ASC, id DESC;
    '''