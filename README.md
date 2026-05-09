# 🌿 FarmShop Backend

> A production-ready REST API backend for a farm-to-table organic food delivery platform, built with Django REST Framework and PostgreSQL. Designed to power a cross-platform Flutter mobile application.

![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?style=flat&logo=postgresql&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-Compatible-02569B?style=flat&logo=flutter&logoColor=white)

---

## 📖 Overview

FarmShop is a full-stack project consisting of this Django backend and a Flutter mobile frontend. The backend exposes a RESTful API that the Flutter app consumes to display organic farms, fresh produce, and artisan food products.

The project also includes a fully designed **HTML storefront** — a browser-based interface that mirrors the Flutter app's design language, built with vanilla HTML, CSS, and JavaScript.

### Key Highlights

- **RESTful API** with filtering, search, and nested serialization
- **HTML Storefront** with a custom organic farm aesthetic — no frameworks, pure CSS/JS
- **PostgreSQL** database with seeded initial data
- **Environment-based configuration** — no secrets in the codebase
- **CORS-enabled** for cross-origin Flutter/mobile access
- **Branch-based Git workflow** — `main` for stable, `dev` for active development

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.14 |
| Framework | Django 5.x |
| API | Django REST Framework |
| Database | PostgreSQL 17 |
| Auth & Security | django-cors-headers, python-decouple |
| Frontend | Vanilla HTML / CSS / JavaScript |
| Mobile Client | Flutter (separate repo) |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
farmshop-backend/
├── farm_shop/                  # Project configuration
│   ├── settings.py             # Environment-based settings
│   └── urls.py                 # Root URL configuration
│
├── shop/                       # Main application
│   ├── models.py               # FoodCategory, Shop, FoodItem models
│   ├── serializers.py          # DRF serializers (list + detail)
│   ├── views.py                # API views + HTML page views
│   ├── urls.py                 # App-level URL patterns
│   ├── admin.py                # Django admin configuration
│   │
│   ├── templates/shop/         # HTML storefront templates
│   │   ├── base.html           # Shared layout, nav, design tokens
│   │   ├── shops.html          # Shops listing with search & filters
│   │   ├── shop_detail.html    # Single shop with product grid
│   │   ├── items.html          # All products with organic filter
│   │   ├── item_detail.html    # Product detail with related items
│   │   └── categories.html     # Category browser
│   │
│   └── management/
│       └── commands/
│           └── seed_data.py    # Initial data seeder command
│
├── flutter_api_service.dart    # Drop-in Flutter API service
├── .env                        # Environment variables (not committed)
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 🗃 Data Models

### `FoodCategory`
Represents a product category (Fruits, Vegetables, Dairy, etc.)

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| name | CharField | Category name |
| emoji | CharField | Display emoji |

### `Shop`
Represents a farm or artisan producer.

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| name | CharField | Shop name |
| tag | CharField | Comma-separated tags |
| rating | DecimalField | Average rating (0–5) |
| review_count | IntegerField | Total reviews |
| delivery_time | CharField | Estimated delivery window |
| delivery_fee | CharField | Fee or "Free" |
| is_open | BooleanField | Current open status |
| emoji | CharField | Display emoji |
| color_hex | CharField | Theme color (no #) |

### `FoodItem`
Represents a product listed by a shop.

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| shop | ForeignKey | Related Shop |
| name | CharField | Product name |
| unit | CharField | Unit size (e.g. 500g, bunch) |
| price | DecimalField | Price in BDT (৳) |
| rating | DecimalField | Product rating |
| is_organic | BooleanField | Organic certification |
| emoji | CharField | Display emoji |
| color_hex | CharField | Theme color (no #) |

---

## 🔌 API Reference

### Categories

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories/` | List all food categories |

### Shops

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/shops/` | List all shops (lightweight, no items) |
| GET | `/api/shops/?search=<query>` | Search shops by name or tag |
| GET | `/api/shops/<id>/` | Shop detail with full item list |
| GET | `/api/shops/<id>/items/` | All items for a specific shop |

### Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/items/` | List all items across all shops |
| GET | `/api/items/?search=<query>` | Search items by name |
| GET | `/api/items/?is_organic=true` | Filter organic items only |
| GET | `/api/items/<id>/` | Single item detail |

### Example Response — `GET /api/shops/1/`

```json
{
  "id": 1,
  "name": "Green Harvest Farm",
  "tag": "Organic · Vegetables · Fruits",
  "rating": "4.9",
  "review_count": 312,
  "delivery_time": "25-35 min",
  "delivery_fee": "৳30",
  "is_open": true,
  "emoji": "🌿",
  "color_hex": "2D6A4F",
  "items": [
    {
      "id": 1,
      "name": "Heirloom Tomatoes",
      "shop_name": "Green Harvest Farm",
      "unit": "500g",
      "price": "85.00",
      "rating": "4.9",
      "is_organic": true,
      "emoji": "🍅",
      "color_hex": "E85D4A"
    }
  ]
}
```

---

## 🌐 HTML Storefront

A browser-based storefront is included, designed to match the Flutter app's organic farm aesthetic — deep forest greens, warm earth tones, Playfair Display typography.

| Page | URL | Description |
|------|-----|-------------|
| Shops | `/shops/browse/` | Shop grid with search, filters, stats |
| Shop Detail | `/shops/<id>/browse/` | Hero banner, info card, product grid |
| All Products | `/items/browse/` | Full product listing with organic filter |
| Product Detail | `/items/<id>/browse/` | Price card, details, related products |
| Categories | `/categories/browse/` | Category mosaic with product reveal |
| Admin | `/admin/` | Django admin panel |

All pages fetch data live from the REST API and require no page reloads.

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 17 running locally
- Git

### 1. Clone the repository

```bash
git clone https://github.com/TasinHaiwan/farmshop-backend.git
cd farmshop-backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

```bash
psql -U postgres
```

```sql
CREATE DATABASE farmshop_db;
CREATE USER farmshop_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE farmshop_db TO farmshop_user;
\q
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_django_secret_key_here
DB_NAME=farmshop_db
DB_USER=farmshop_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

> ⚠️ Never commit `.env` to version control. It is already listed in `.gitignore`.

### 6. Run migrations and seed data

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/shops/browse/` to see the storefront.

---

## 📱 Flutter Integration

The file `flutter_api_service.dart` is a drop-in API service for the Flutter client.

**Installation:**

1. Copy it to `lib/services/api_service.dart` in your Flutter project
2. Add the `http` package to `pubspec.yaml`:

```yaml
dependencies:
  http: ^1.2.0
```

3. Run `flutter pub get`

**Configuration:**

```dart
// Android emulator
static const String _base = 'http://10.0.2.2:8000/api';

// Real device — use your machine's local IP
static const String _base = 'http://192.168.x.x:8000/api';
```

**Usage:**

```dart
// Replace static constants with live API calls
final shops = await ApiService.fetchShops();
final items = await ApiService.fetchItemsForShop('1');
final organic = await ApiService.fetchItems(isOrganic: true);
```

---

## 🌿 Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready code |
| `dev` | Active development and new features |

All development happens on `dev`. Changes are merged into `main` only when tested and stable.

---

## 🚀 Roadmap

- [ ] JWT authentication for users
- [ ] Cart and order management endpoints
- [ ] Image upload support for shops and products
- [ ] Pagination on list endpoints
- [ ] Docker + deployment configuration
- [ ] Unit and integration tests

---

## 👤 Author

**Tasin Haiwan**
[GitHub](https://github.com/TasinHaiwan) · Built as part of a Flutter + Django full-stack project