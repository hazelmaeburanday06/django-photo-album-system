# Production-Ready Django Photo Album Management System

## Features
- Django Class-Based Views (CBVs)
- Role-Based Access Control (RBAC)
- Cloudinary image storage
- PostgreSQL support
- Render deployment ready
- User authentication
- Album CRUD operations
- Photo upload management

## Setup

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate environment
Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env
```env
SECRET_KEY=your_secret_key
DEBUG=True

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

DATABASE_URL=postgresql://user:password@host:5432/dbname
```

### 5. Migrate database
```bash
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run server
```bash
python manage.py runserver
```

## Render Deployment
- Create PostgreSQL database in Render
- Create Web Service
- Connect GitHub repository
- Add environment variables
- Deploy

## Admin Permissions
Superusers can:
- Delete any album
- Manage users
- View admin dashboard

Regular users can:
- Create albums
- Upload photos
- Edit only their own albums