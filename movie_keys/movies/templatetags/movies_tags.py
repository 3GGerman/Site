from django import template

register = template.Library()

@register.inclusion_tag('movies/header.html')
def header_tag():
    return {}
