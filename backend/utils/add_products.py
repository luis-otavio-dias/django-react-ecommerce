import os
import sys
import django
from pathlib import Path

DJANGO_BASE_DIR = Path(__file__).parent.parent

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "backend.settings"

django.setup()


if __name__ == "__main__":
    from products import products
    from base.models import Product

    Product.objects.all().delete()

    db_products = []

    for product in products:

        db_products.append(
            Product(
                _id=product["_id"],
                name=product["name"],
                image=product["image"],
                description=product["description"],
                brand=product["brand"],
                category=product["category"],
                price=product["price"],
                countInStock=product["countInStock"],
                rating=product["rating"],
                numReviews=product["numReviews"],
            )
        )

    Product.objects.bulk_create(db_products)
