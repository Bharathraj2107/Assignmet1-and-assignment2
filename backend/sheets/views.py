from django.http import JsonResponse

def save(request):
    if request.method == 'POST':
        data = request.POST
        # Save data to a file or database
        return JsonResponse({"message": "Data saved successfully"})

def load(request):
    if request.method == 'GET':
        # Load data from a file or database
        return JsonResponse({"data": []})