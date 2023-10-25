from django.shortcuts import render


#SZjrtFKYqN0DGqQgCdEGiw==qguXA82YiA66F8Pl
# Create your views here.

def home(request):

    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'SZjrtFKYqN0DGqQgCdEGiw==qguXA82YiA66F8Pl'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = 'oops! Error'
            print(e)
        return render(request, 'calorie_app/home.html', context={'api': api})
    else:
        return render(request, 'calorie_app/home.html', context={'query': 'Введите корректный запрос'})
