from django.shortcuts import render
from .models import Tea

# Create your views here.
def tea_response(request):
    table = Tea.objects.all()
    table_list = [record for record in table.values()]
    titles = table_list[0].keys() if table_list else []
    context = {'tea_table' : table_list, 'titles' : titles}
    return render(request, "tea/teainfo.html", context)
