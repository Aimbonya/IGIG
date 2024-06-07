from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Genre, Movie, Hall, Showtime, Employee, TicketSale, News, Term, Contact, Review, Vacancy, PromoCode, FAQ
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Showtime)
admin.site.register(Employee)
admin.site.register(TicketSale)
admin.site.register(News)
admin.site.register(Term)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Vacancy)
admin.site.register(PromoCode)
admin.site.register(FAQ)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'role')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
