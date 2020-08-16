from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('S', 'Vegtables'),
    ('F', 'Fruit'),
    ('O', 'Others')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')  
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True,null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField(default="veggi")
    description = models.TextField()
    inside_cart = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("leneva_backend:product", kwargs={
            'slug':self.slug
        })

    def get_add_to_cart(self):
        return reverse("leneva_backend:add-to-cart", kwargs={
            'slug':self.slug
        })

    def get_remove_from_cart(self):
        return reverse("leneva_backend:remove-from-cart", kwargs={
            'slug':self.slug
        })

    def __str__(self):
        return self.title

    

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username} : {self.item.title} in {self.quantity} amount'
    
    def price(self):
        if self.item.discount_price:
            return self.item.discount_price
        else:
            return self.item.price

    def total_item_price(self):
        return self.price()*self.quantity


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

    def total_cart_price(self):
        total=0
        for o_item in self.items.all():
            total += o_item.total_item_price()
        return total