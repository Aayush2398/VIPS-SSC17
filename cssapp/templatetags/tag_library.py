from django import template

register = template.Library()

@register.filter()
def to_int(value):
	return int(value)

@register.filter()
def increment(value):
	value = value+1
	return range(value)

@register.filter()
def to_string(value):
	return str(value)