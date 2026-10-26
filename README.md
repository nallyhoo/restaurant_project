# 🍽️ SVB Restaurant - Management & Online Ordering System

A full-stack web application built with **Django** for restaurant management, online food ordering, table reservations, and menu administration.

---

## 🌟 Key Features

- **Food & Drink Catalog**: Browse categorized menus (Breakfast, Lunch, Dinner, Drinks) with descriptions and prices.
- **Online Ordering & Cart**: Add food items to cart, review selections, and place orders directly.
- **Table Booking / Reservations**: Customers can reserve tables online with guest count, date/time, and special requests.
- **Contact & Feedback**: Customer messaging and testimonial submissions.
- **Admin Management Panel**:
  - Full CRUD operations for menu items and food categories.
  - Media/image upload support for dishes and team members.
  - Review and manage table reservations and online customer orders.
  - User authentication and role-based access for staff/superusers.

---

## 🛠️ Tech Stack

- **Backend**: [Django 5.0+](https://www.djangoproject.com/) (Python)
- **Database**: SQLite3 (default development database)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Image Processing**: Pillow
- **HTTP / Utilities**: Requests

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10, 3.11, or 3.12+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/nallyhoo/restaurant_project.git
cd restaurant_project
```

### 2. Create and Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Admin Account (Optional)

If you need a new administrative user:
```bash
python manage.py createsuperuser
```

> **Default Demo Admin (Local Development):**
> - **Username**: `admin`
> - **Password**: `admin123`

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
- **Main Website**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Portal**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Project Structure

```text
svb_restuarant/
│
├── myapp/                      # Core Django application
│   ├── migrations/             # Database migration history
│   ├── templates/              # HTML templates (menu, booking, shop, admin)
│   ├── models.py               # Data models (Product, Booking, Order, Chef, etc.)
│   ├── views.py                # Request handling and controller logic
│   └── admin.py                # Admin site configuration
│
├── svb_restuarant/             # Django project configuration
│   ├── settings.py             # Project settings, static, media paths
│   ├── urls.py                 # URL routing definitions
│   └── wsgi.py                 # WSGI entry point
│
├── static/                     # Static files (CSS, JS, theme assets)
├── uploads/                    # Uploaded media (product images, chef photos)
├── db.sqlite3                  # Local SQLite database
├── manage.py                   # Django CLI utility
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 📄 License

This project is open-source and available for educational and commercial development.
