from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html', {
        'pages': [
            {'title': 'toyota mark 2', 'id': 1},
            {'title': 'toyota supra', 'id': 2},
            {'title': 'toyota mark x', 'id': 3},
        ]
    })

def page(request, id):
    return render(request, 'page.html', {'data': {
        'id': id
    }})