from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def home(request):
    data = {
        "id": "00001",
        "name": "Mahfuzur Rahman",
        "nickname": "linkon",
        "email": "linkonmahfuz@gmail.com",
        "age": 17,
        "description": "I'm Mahfuz. I live in Bangladesh. I'm a Python developer.",
        "descriptionBN": "",
        "friends": ["Rizan", "Mehedi", "Nokib"],
        "friends2": ["John", "Dho", "Alex"],
        "date": datetime.datetime.now(),
        "friends3": [
            {"name": "zed", "age": 19},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 31},
        ],
        "lineText": """cat
            dog
            horse """,
    }
    return render(request, "data_filter/home.html", context=data)
