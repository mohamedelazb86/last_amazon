from .models import Settings

def get_contect_data(request):
    data=Settings.objects.last()
    return {'data':data}