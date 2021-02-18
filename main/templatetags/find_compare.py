from django import template

register = template.Library()

@register.filter

def find_compare(value):
    return value.replace("_val","_atleast")