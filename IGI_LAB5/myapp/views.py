import requests
import matplotlib.pyplot as plt
import base64
from io import BytesIO

from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum
from django.utils import timezone
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Movie, Employee, Hall, News, Review, PromoCode, Genre, FAQ, Vacancy
from .forms import TicketPurchaseForm, MovieForm, ReviewForm, PromoCodeForm, MovieFilterForm, LoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test


def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return redirect('login')
        return _wrapped_view
    return decorator


def buy_ticket(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            hall = form.cleaned_data['hall']
            showtime = form.cleaned_data['showtime']
            ticket_count = form.cleaned_data['ticket_count']
            movie.tickets_sold += ticket_count
            promo_code = form.cleaned_data['promo_code']
            ticket_price = hall.ticket_cost
            discount = 1.0

            if promo_code:
                try:
                    promo = PromoCode.objects.get(code=promo_code, is_active=True)
                    if promo.start_date <= promo.end_date:
                        discount = promo.discount
                except PromoCode.DoesNotExist:
                    pass

            final_price = ticket_price * ticket_count * discount
            context = {
                'movie': movie,
                'hall': hall,
                'showtime': showtime,
                'ticket_count': ticket_count,
                'ticket_price': ticket_price,
                'final_price': final_price,
                'promo_code': promo_code,
            }
            return render(request, 'ticket_summary.html', context)
    else:
        form = TicketPurchaseForm()

    return render(request, 'buy_ticket.html', {'movie': movie, 'form': form})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    current_date = timezone.now()
    today = current_date.date()
    user_timezone = timezone.get_current_timezone_name()
    context = {
        'today': today,
        'movie': movie,
        'current_date': current_date,
        'user_timezone': user_timezone
    }
    return render(request, 'movie_detail.html', context)


def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('movie_list')


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


@login_required
def review_new(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'review_new.html', {'form': form})


def apicheck(request):
    joke = get_joke()
    return render(request, 'APICHECK.html', {'joke': joke})


def get_joke():
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    data = response.json()

    setup = data["setup"]
    punch = data["punchline"]
    return f"{setup} - {punch}"


def movie_list(request):
    form = MovieFilterForm(request.GET)
    movies = Movie.objects.all()

    if form.is_valid():
        genre = form.cleaned_data.get('genre')
        if genre:
            movies = movies.filter(genre=genre)

    return render(request, 'movie_list.html', {'movies': movies, 'form': form})


def about_us(request):
    employees = Employee.objects.all()
    halls = Hall.objects.all()
    return render(request, 'about_us.html', {'employees': employees, 'halls': halls})


def movie_news(request):
    news = News.objects.all()
    return render(request, 'movie_news.html', {'news': news})


def news_detail(request, pk):
    new = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': new})


def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movie_edit.html', {'form': form})


def terms_of_use(request):
    return render(request, 'terms_of_use.html')


def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.save()
                return redirect('review_list', pk=review.pk)
        else:
            form = ReviewForm(instance=review)
        return render(request, 'review_edit.html', {'form':form})
    else:
        return redirect('review_list', pk=review.pk)


def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_edit.html', {'form': form})


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movie_list')


def promocode_list(request):
    promocodes = PromoCode.objects.all()
    return render(request, 'promocode_list.html', {'promocodes': promocodes})


def promocode_new(request):
    if request.method == "POST":
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            promocode = form.save(commit=False)
            promocode.save()
            return redirect('promocode_list')
    else:
        form = PromoCodeForm()
    return render(request, 'promocode_new.html', {'form': form})


def stats_view(request):
    movies = Movie.objects.order_by('title')

    total_sales = Movie.objects.aggregate(total=Sum('tickets_sold'))['total']

    sales = list(Movie.objects.values_list('tickets_sold', flat=True))
    avg_sales = sum(sales) / len(sales) if sales else 0
    sales_sorted = sorted(sales)
    median_sales = sales_sorted[len(sales_sorted) // 2] if sales else 0
    mode_sales = max(set(sales), key=sales.count) if sales else 0

    popular_genre = Genre.objects.annotate(num_movies=Count('movie')).order_by('-num_movies').first()

    profitable_genre_data = (
        Movie.objects.values('genre__name')
        .annotate(total_sales=Sum('tickets_sold'))
        .order_by('-total_sales')
        .first()
    )
    profitable_genre = profitable_genre_data['genre__name'] if profitable_genre_data else None

    total_profit = Movie.objects.aggregate(profit=Sum('tickets_sold') * 5)['profit']

    movie_titles = [movie.title for movie in movies]
    ticket_sales = [movie.tickets_sold for movie in movies]

    fig, ax = plt.subplots()
    ax.bar(movie_titles, ticket_sales)
    ax.set_xlabel('Movies')
    ax.set_ylabel('Tickets Sold')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'movies': movies,
        'total_sales': total_sales,
        'avg_sales': avg_sales,
        'median_sales': median_sales,
        'mode_sales': mode_sales,
        'popular_genre': popular_genre.name if popular_genre else None,
        'profitable_genre': profitable_genre,
        'total_profit': total_profit,
        'graphic': graphic,
    }
    return render(request, 'stats.html', context)


def faq_list(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'faq_list.html', {'faqs': faqs})


def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'faq_detail.html', {'faq': faq})


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy_list.html', {'vacancies': vacancies})


def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})


def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        return view_func(request, *args, **kwargs)

    return _wrapped_view

@admin_required
def admin_page(request):
    return render(request, 'admin_page.html')
