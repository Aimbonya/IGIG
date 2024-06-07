from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/new/', views.movie_new, name='movie_new'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('buy_ticket/<int:pk>/', views.buy_ticket, name='buy_ticket'),
    path('aboutus/', views.about_us, name='about_us'),
    path('news/', views.movie_news, name='movie_news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/new/', views.review_new, name='review_new'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancies/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('promocodes/', views.promocode_list, name='promocode_list'),
    path('promocodes/new/', views.promocode_new, name='promocode_new'),
    path('stats/', views.stats_view, name='stats'),
    path('faq/', views.faq_list, name='faq_list'),
    path('faq/<int:pk>/', views.faq_detail, name='faq_detail'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('check/', views.apicheck, name='apicheck'),
    path('buy_ticket/<int:pk>/', views.buy_ticket, name='buy_ticket'),
]
