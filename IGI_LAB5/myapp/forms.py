from django import forms
from django.core.validators import RegexValidator
from .models import Movie, Review, PromoCode, FAQ, Vacancy, CustomUser, Hall, Genre
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from datetime import date


class MovieFilterForm(forms.Form):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, label='Genre')


class TicketPurchaseForm(forms.Form):
    hall = forms.ModelChoiceField(queryset=Hall.objects.all(), label='Select Hall')
    showtime = forms.ChoiceField(label='Select Showtime')
    ticket_count = forms.IntegerField(min_value=1, label='Number of Tickets')
    promo_code = forms.CharField(max_length=50, required=False, label='Promo Code')

    def __init__(self, *args, **kwargs):
        super(TicketPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['showtime'].choices = self.generate_showtime_choices()

    def generate_showtime_choices(self):
        choices = []
        for hour in range(11, 23):  # Shows from 11:00 to 22:00
            choices.append((f"{hour}:00", f"{hour}:00"))
        return choices


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^\+37529\d{3}\d{2}\d{2}$',
                message="Phone number must be entered in the format: '+375 (29) XXX-XX-XX'."
            )
        ],
        label="Phone Number"
    )

    birth_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget(years=range(date.today().year - 100, date.today().year + 1)),
        label="Date of Birth"
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'birth_date', 'password1', 'password2')

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        age = (date.today() - birth_date).days / 365.25
        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to register.")
        return birth_date

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data["phone_number"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.role = 'customer'
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')


class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'country', 'genre', 'duration', 'budget', 'poster', 'description', 'rating']


class PromoCodeForm(forms.ModelForm):
    class Meta:
        model = PromoCode
        fields = ['code', 'description', 'start_date', 'end_date', 'is_active']
