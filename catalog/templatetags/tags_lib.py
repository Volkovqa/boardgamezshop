from django import template

register = template.Library()


@register.simple_tag
def mediapath(path):
    if path:
        return '/media/' + str(path)
    return '/media/products/no_image.jpg'


@register.filter(name='mediapath')
def mediapath(path):
    if path:
        return '/media/' + str(path)
    return '/media/products/no_image.jpg'
