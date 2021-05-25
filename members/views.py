from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Member

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/members")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})


def member_response(request):
    table = Member.objects.all()
    table_list = [record for record in table.values()]
    titles = table_list[0].keys() if table_list else [] # [0] значит передаем 1ю запись, т.к. у них совпадают id.
                                                                                # предается чистый лист
    context = {'members_table' : table_list, 'titles' : titles}
    return render(request, "memberinfo.html", context)
