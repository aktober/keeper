from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split_by_tags(value):
    # print(value)
    arr = value.split(',')
    for a in arr:
        print(a)
    return arr