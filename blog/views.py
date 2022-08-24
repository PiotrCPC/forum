from django.shortcuts import render, get_object_or_404
from .models import Post, MojeModele, Person, Comment
from django.shortcuts import render
from django.utils import timezone
from .form import PostForm, SecondForm, EmailPostForm, FormDoMaila, CommentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def kwiaty_main(request):

    return render(request, 'blog/kwiaty_main.html', {})

def base(request):

    return render (request, 'blog/base.html', {})

def nawigacja(request):
    if request.method == "POST":
        forma = SecondForm(request.POST)
        if forma.is_valid():
            post = forma.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('nawigacja')
    else:
        forma = SecondForm()

    return render(request, 'blog/nawigacja.html', {'forma':forma})


def trzy_kolumny(request):

    return render(request, 'blog/trzy_kolumny.html', {})

def twojeimie(request):
    #zmienna = request.POST.get('twojeimie')

    if request.method == "POST":
        forma = PostForm(request.POST)
        if forma.is_valid():
            post = forma.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('nawigacja')
    else:
        forma = PostForm()

    return render(request, 'blog/nawigacja.html', {'forma':forma})

def drugaopcja(request):
    podaj_imie = PostForm(request.POST)
    form = PostForm(request.POST)
    post = form.save(commit=False)



    return render(request, 'blog/drugi.html', {})

def wyniki(request):
    wy = MojeModele.objects.all()

    paginator = Paginator(wy,3)

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/wyniki.html', {'wy':wy,
                                                'page':page,
                                                'posts':posts,
                                                'page_obj':page_obj,
                                                })

def dodaj_wpis(request):

    if request.method == "POST":
        forma = SecondForm(request.POST)
        if forma.is_valid():
            post = forma.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('wyniki')
    else:
        forma = SecondForm()

    return render(request, 'blog/dodaj_wpis.html', {'forma':forma})

def tresc(request):

    return render(request, 'blog/tresc.html', {})

def o_nas(request):
    

    return render(request, 'blog/o_nas.html', {})
                  

def zasady(request):
    
    return render(request, 'blog/zasady.html', {})


                  
def person_view(request):
    Osoba = Person.objects.all()

    return render(request, 'blog/persony.html', {'Osoba':Osoba
                                                })

def formularz(request):
    #post = get_object_or_404(Post, pk=3)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        post = get_object_or_404(Post, id=5 )
        if form.is_valid():
            cd = form.cleaned_data
            #post_url = request.build_absolute_uri(pos)
            #imie = cd['name']
            temat = cd['temat']
            tresc = cd['wiadomosc']
            #post_url = request.build_absolute_uri(post.get_absolute_url())
            #subject = '{} ({}) prosze przeczytaj "{}"'.format(cd['name'], cd['email'], post.title)
            #send_mail = ('qqq', 'standardowa wiadomosc', 'django.testowanie@gmail.com', ['django.testowanie@gmail.com'])
            send_mail(temat,tresc,'django.testowanie@gmail.com',[cd['nadawca']])
            sent = True
    else:
        form = EmailPostForm()
    #send_mail = ('qqq', 'standardowa wiadomosc', 'django.testowanie@gmail.com', ['django.testowanie@gmail.com'])
    return render(request, 'blog/formularz.html', {
                                                   'form':form,
                                                   'sent':sent,
                                                    })

# Create your views here.
