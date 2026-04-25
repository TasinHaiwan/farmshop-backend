# Farm Shop — Django Backend

## Setup

```bash
pip install django djangorestframework django-cors-headers

django-admin startproject farm_shop .
python manage.py startapp shop
```

### settings.py additions

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'shop',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must be first
    ...
]

# Allow Flutter app (adjust in production)
CORS_ALLOW_ALL_ORIGINS = True
```

## Migrate & seed

```bash
python manage.py makemigrations
python manage.py migrate

# Create superuser for /admin
python manage.py createsuperuser

# Seed initial data from Flutter constants
python manage.py seed_data
```

## Run

```bash
python manage.py runserver 0.0.0.0:8000
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/categories/` | All food categories |
| GET | `/api/shops/` | All shops (no items) |
| GET | `/api/shops/<id>/` | Shop detail + items |
| GET | `/api/shops/<id>/items/` | Items for one shop |
| GET | `/api/items/` | All items |
| GET | `/api/items/?is_organic=true` | Organic items only |
| GET | `/api/items/<id>/` | Single item detail |

## Flutter

Copy `flutter_api_service.dart` into your project and add the `http` package:

```yaml
# pubspec.yaml
dependencies:
  http: ^1.2.0
```

Change `_base` in `ApiService` to your server IP when running on a real device.
