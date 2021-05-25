from django.shortcuts import render
from .models import Kofe

# Create your views here.
def coffee_response(request):
    table = Kofe.objects.all()
    table_list = [record for record in table.values()]
    titles = table_list[0].keys() if table_list else [] # [0] значит передаем 1ю запись, т.к. у них совпадают id.
                                                                                # предается чистый лист
    context = {'coffee_table' : table_list, 'titles' : titles}
    return render(request, "coffee/coffeeinfo.html", context)
