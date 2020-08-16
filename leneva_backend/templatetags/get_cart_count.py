from django import template
from leneva_backend.models import Order

register = template.Library()

@register.filter
def order_cart_count(user):
    if user.is_authenticated:
        q=Order.objects.filter(user=user,ordered=False)
        if q.exists():
            return q[0].items.count()
    return 0