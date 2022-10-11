from django.shortcuts import render
from .models import *
list=[
{
"code": "AN",
"name": "Andaman and Nicobar Islands"
},
{
"code": "AP",
"name": "Andhra Pradesh"
},
{
"code": "AR",
"name": "Arunachal Pradesh"
},
{
"code": "AS",
"name": "Assam"
},
{
"code": "BR",
"name": "Bihar"
},
{
"code": "CG",
"name": "Chandigarh"
},
{
"code": "CH",
"name": "Chhattisgarh"
},
{
"code": "DH",
"name": "Dadra and Nagar Haveli"
},
{
"code": "DD",
"name": "Daman and Diu"
},
{
"code": "DL",
"name": "Delhi"
},
{
"code": "GA",
"name": "Goa"
},
{
"code": "GJ",
"name": "Gujarat"
},
{
"code": "HR",
"name": "Haryana"
},
{
"code": "HP",
"name": "Himachal Pradesh"
},
{
"code": "JK",
"name": "Jammu and Kashmir"
},
{
"code": "JH",
"name": "Jharkhand"
},
{
"code": "KA",
"name": "Karnataka"
},
{
"code": "KL",
"name": "Kerala"
},
{
"code": "LD",
"name": "Lakshadweep"
},
{
"code": "MP",
"name": "Madhya Pradesh"
},
{
"code": "MH",
"name": "Maharashtra"
},
{
"code": "MN",
"name": "Manipur"
},
{
"code": "ML",
"name": "Meghalaya"
},
{
"code": "MZ",
"name": "Mizoram"
},
{
"code": "NL",
"name": "Nagaland"
},
{
"code": "OR",
"name": "Odisha"
},
{
"code": "PY",
"name": "Puducherry"
},
{
"code": "PB",
"name": "Punjab"
},
{
"code": "RJ",
"name": "Rajasthan"
},
{
"code": "SK",
"name": "Sikkim"
},
{
"code": "TN",
"name": "Tamil Nadu"
},
{
"code": "TS",
"name": "Telangana"
},
{
"code": "TR",
"name": "Tripura"
},
{
"code": "UP",
"name": "Uttar Pradesh"
},
{
"code": "UK",
"name": "Uttarakhand"
},
{
"code": "WB",
"name": "West Bengal"
}
]


def state_data(request):
    name=[]
    code=[]
    for i  in list:
        name.append(i["name"])
        code.append(i["code"])
    print(name)
    print(code)
    for j in range(len(name)):
        data=State.objects.create(status=True,country_id=101,
        state_name=name[j],state_code=code[j])
    return render(request,"home.html")