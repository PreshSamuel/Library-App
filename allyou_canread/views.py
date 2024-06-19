from django.shortcuts import render, redirect

# Create your views here.

def AYCR_Genre_Pick(request):
    try:
        if request.method == 'POST':
            genre = request.POST['choice']
            print(genre)
            request.session['choice'] = genre
            return redirect('allyou_canread:library')
        else:
            template_name = 'genre.html'
            return render(request, template_name)
    except Exception:
        return redirect('allyou_canread:no_value')
    

def Choosen_Genre(request):
    template_name = 'library.html'
    context = {
        'Choosen': request.session['choice']
    }
    return render(request, template_name, context)


def NoneValue(request):
    try:
        if request.method == 'POST':
            genre = request.POST['choice']
            print(genre)
            request.session['choice'] = genre
            return redirect('allyou_canread:library')
        else:
            template_name = 'no_value.html'
            return render(request, template_name)
    except Exception:
        return redirect('allyou_canread:no_value')