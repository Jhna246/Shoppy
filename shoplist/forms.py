from django.forms import ModelForm
from .models import Shoplist, Items

class ShopForm(ModelForm):
    class Meta:
        model = Shoplist
        fields = ['title',]


class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['item']