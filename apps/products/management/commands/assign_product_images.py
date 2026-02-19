"""
Assign images from assets/ folder to products by name mapping.
Run from project root: python manage.py assign_product_images
"""
import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.core.files import File

from apps.products.models import Product


# Product name (exact) -> asset filename in assets/
ASSET_MAP = {
    'Classic Cotton T-Shirt': 'tshirt.jpg',
    'Wireless Bluetooth Headphones': 'headphones.jpg',
    'Stainless Steel Water Bottle': 'waterbottle.jpg',
    'Minimalist Backpack': 'backpack.jpg',
    'LED Desk Lamp': 'leddesklamp.jpg',
    'Organic Skincare Set': 'skincare.jpg',
}


class Command(BaseCommand):
    help = 'Assign images from assets/ folder to products by name'

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent.parent
        assets_dir = base_dir / 'assets'
        if not assets_dir.is_dir():
            self.stdout.write(self.style.ERROR(f'Assets folder not found: {assets_dir}'))
            return

        media_products = base_dir / 'media' / 'products'
        media_products.mkdir(parents=True, exist_ok=True)

        updated = 0
        for product_name, filename in ASSET_MAP.items():
            product = Product.objects.filter(name=product_name).first()
            if not product:
                continue
            src = assets_dir / filename
            if not src.is_file():
                self.stdout.write(self.style.WARNING(f'Asset not found: {filename}'))
                continue
            dest_path = media_products / filename
            with open(src, 'rb') as f:
                product.image.save(filename, File(f), save=True)
            updated += 1
            self.stdout.write(f'  Assigned {filename} -> {product_name}')

        self.stdout.write(self.style.SUCCESS(f'Assigned {updated} product images.'))
