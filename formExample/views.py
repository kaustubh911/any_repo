from django.shortcuts import render
from formExample.forms import FormExample

def form_example(request):
    formObj = FormExample()
    # print(formObj)
    # print(request.method)
    # print(request.GET)

    if request.method == 'POST':
        formObj = FormExample(request.POST)

        if formObj.is_valid():
            pass
            # print(request.POST)


    return render(request, 'form_example.html', {'form':formObj})


def static_view(request):
    return render(request, 'static_example.html')
