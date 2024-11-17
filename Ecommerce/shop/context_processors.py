
# dropdownlist link

from shop.models import Itemcategory
def menulink(request):
    c=Itemcategory.objects.all()

    return {'links':c}