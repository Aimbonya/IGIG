from django import template

register = template.Library()


@register.filter
def is_site_employee(user):
    return user.is_authenticated
