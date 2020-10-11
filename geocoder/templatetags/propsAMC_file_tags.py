from django import template
register = template.Library()

@register.filter(name = 'file_name_with_ext')
def file_name_with_ext_format(value):
    return value.url.split('/')[-1]