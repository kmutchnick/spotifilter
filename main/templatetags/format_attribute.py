from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter

def format_attribute(value):
    s = value.replace('_val','')
    s = s.capitalize()
    s = s.replace('_ms',' (ms)')
    return s