from django import template
import random
register = template.Library()  # 对象名必须为register


@register.simple_tag()
def random_self(list):
    return random.randint(1,list)
