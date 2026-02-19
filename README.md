# Simple E-commerce Store

A full-stack e-commerce web application built with **Django** (backend) and **HTML, CSS, Vanilla JavaScript** (frontend), using the [Color Hunt palette](https://colorhunt.co/palette/15173d982598e491c9f1e9e9): Navy `#15173D`, Purple `#982598`, Pink `#E491C9`, Cream `#F1E9E9`.

## Features

- **Product listing** – Responsive grid, image, name, price, short description, View Details
- **Product detail** – Large image, full description, price, Add to Cart, stock, back to products
- **Shopping cart** – Session-based: add, remove, update quantity, total, dynamic cart counter in navbar
- **User auth** – Register, Login, Logout (Django auth), form validation, redirect after login
- **Orders** – Checkout, place order, save Order + OrderItems (user, products, quantity, total, date, status)
- **Admin** – Customized header; product image upload; manage products and orders

## Project structure

```
CodeAlpha_SimpleEcommerceStore/
├── config/                 # Django project settings
├── apps/
│   ├── products/           # Product model, listing, detail
│   ├── cart/               # Session cart logic, views
│   ├── orders/             # Order, OrderItem, checkout
│   └── users/              # Register, Login, Logout
├── templates/              # Base + app templates
├── static/
│   ├── css/style.css       # Palette-based styles
│   ├── js/main.js          # Nav toggle, etc.
│   └── images/placeholder.svg
├── media/                  # Product uploads (created at runtime)
├── manage.py
└── requirements.txt
```

## How to run

1. **Install dependencies** (from project root):

   ```bash
   pip install -r requirements.txt
   ```
   Or: `python -m pip install -r requirements.txt`

2. **Apply migrations** (if not already done):

   ```bash
   python manage.py migrate
   ```

3. **Create sample products** (optional, adds 6 products):

   ```bash
   python manage.py create_sample_products
   ```

4. **Create a superuser** (for admin):

   ```bash
   python manage.py createsuperuser
   ```
   Enter username, email, and password when prompted.

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. Open in browser:

   - **Store:** http://127.0.0.1:8000/
   - **Admin:** http://127.0.0.1:8000/admin/

## What you need

- **Python 3.8+** with pip.
- **Images:** Product images are optional. If a product has no image, the app uses the included placeholder (`static/images/placeholder.svg`). You can add images via the Django admin: **Products** → edit a product → set **Image** and save.

## Quick test flow

1. Open http://127.0.0.1:8000/ → see product list.
2. Click **View Details** → product page → **Add to Cart**.
3. Open **Cart** in navbar → update quantity or remove items.
4. **Register** a new account → **Login**.
5. **Cart** → **Checkout** → **Place Order** → order success page.
6. Visit **Admin** (with superuser) to manage products (including image upload) and orders.

## Tech stack

- **Backend:** Django (ORM, auth, sessions, messages, CSRF)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, Vanilla JS
- **Static:** Django static files; optional product images in `media/products/`

  ##Preview
  <img width="1878" height="892" alt="image" src="https://github.com/user-attachments/assets/cd66ca5d-4527-4961-b306-7ec1d991557c" />
  <img width="1906" height="903" alt="image" src="https://github.com/user-attachments/assets/6bb17100-d53d-4d24-85b1-13b85c7cb762" />
  <img width="1906" height="897" alt="image" src="https://github.com/user-attachments/assets/03d49304-10e9-42dd-a900-0ef45f0e6dab" />
  <img width="1880" height="884" alt="image" src="https://github.com/user-attachments/assets/fb43bef3-9e55-40c0-bd7f-ec9bed035d7b" />
  <img width="1897" height="896" alt="image" src="https://github.com/user-attachments/assets/dd7f62bf-4988-4c87-9ff4-a8c97e7392de" />
  <img width="1892" height="881" alt="image" src="https://github.com/user-attachments/assets/f6dd903f-5445-4c04-b43b-9c475c8afd37" />






