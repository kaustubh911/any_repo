from django.shortcuts import render

def studentfunc(request):
    d1 = {
        'name':'Kaustubh',
        'email_id':'kaustubh_619@gmail.com',
        'l1':[1,2,3,4,5],
        'd2':{'city':'Bengaluru', 'address':'BTM'}
    }
    return render(request, 'studentPage.html',  d1)
