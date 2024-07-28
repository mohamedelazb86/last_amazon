import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product,Brand


def seed_brand(n):
    fake=Faker()
    image=['0.jpg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','45.jpg','46.jpg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_product/{image[random.randint(0,11)]}'

        )

def seed_product(n):
    fake=Faker()
    image=['0.jpg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','45.jpg','46.jpg']
    flag=['New','Sale','Feature']
    brands=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            price=round(random.uniform(5.55,99.99),2),
            flag=flag[random.randint(0,2)],
            quantity=round(random.uniform(5.5,99.99),2),
            sku=random.randint(100,10000000),
            subtitle=fake.text(max_nb_chars=4000),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brands[random.randint(0,len(brands)-1)],
            image=f'photo_product/{image[random.randint(0,11)]}'





        )


#seed_brand(200)
seed_product(1500)