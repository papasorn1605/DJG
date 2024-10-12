from django.shortcuts import render

def renderTemplate(request):
    myDict={"name":"Papasorn"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request):
    myDict = {"id": 347, "name": "Papasorn", "salary": 0}  # แก้ไขชื่อเป็น "name" และ "salary"
    return render(request, 'templatesApp/employeeTemplate.html', context=myDict)
