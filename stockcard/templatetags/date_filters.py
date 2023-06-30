from django import template

register = template.Library()

@register.filter
def date_format(value, format_string):
    return value.strftime(format_string)