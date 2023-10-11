from django import template

register = template.Library()


@register.filter(name="get_attr")
def get_attr(obj, key):
    return getattr(obj, key, None)


@register.filter(name="times")
def times(number):
    return range(number)
