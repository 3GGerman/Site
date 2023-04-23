from django import template

register = template.Library()

@register.inclusion_tag('movies/tags/header.html')
def header_tag():
    return {}

