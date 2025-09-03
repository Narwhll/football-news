from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406409504',
        'name' : 'Davin Fauzan Akmalianto',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)