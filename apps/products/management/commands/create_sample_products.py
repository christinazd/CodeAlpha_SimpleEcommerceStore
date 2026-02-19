from django.core.management.base import BaseCommand
from apps.products.models import Product


class Command(BaseCommand):
    help = 'Create sample products for the store'

    def handle(self, *args, **options):
        samples = [
            {
                'name': 'Classic Cotton T-Shirt',
                'description': 'Comfortable unisex cotton t-shirt. Perfect for everyday wear. Available in multiple colors. Machine washable.',
                'price': 24.99,
                'stock': 50,
            },
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': 'High-quality wireless headphones with noise cancellation. 20-hour battery life. Foldable design with carrying case.',
                'price': 79.99,
                'stock': 30,
            },
            {
                'name': 'Stainless Steel Water Bottle',
                'description': 'Keep your drinks cold or hot for hours. BPA-free, 500ml capacity. Leak-proof lid. Eco-friendly choice.',
                'price': 19.99,
                'stock': 100,
            },
            {
                'name': 'Minimalist Backpack',
                'description': 'Lightweight laptop backpack with padded compartment. Water-resistant material. Multiple pockets for organization.',
                'price': 49.99,
                'stock': 25,
            },
            {
                'name': 'LED Desk Lamp',
                'description': 'Adjustable brightness and color temperature. USB charging port. Modern design. Energy-efficient LED.',
                'price': 34.99,
                'stock': 40,
            },
            {
                'name': 'Organic Skincare Set',
                'description': 'Cleanser, toner, and moisturizer. Made with natural ingredients. Suitable for all skin types. Cruelty-free.',
                'price': 44.99,
                'stock': 35,
            },
        ]
        created = 0
        for data in samples:
            _, created_flag = Product.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'price': data['price'],
                    'stock': data['stock'],
                },
            )
            if created_flag:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Sample products ready. Created {created} new products.'))
