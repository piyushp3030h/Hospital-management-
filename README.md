# 🏥 PatientPro — Hospital Management System

A full-featured **Hospital Management System** built with Django that streamlines patient records, doctor management, and department organization. The platform provides role-based dashboards for **Patients** and **Doctors**, along with a RESTful API for seamless integration.

---

## ✨ Features

### 🔐 Authentication & Authorization
- User registration with role selection (Patient / Doctor)
- Doctor accounts require **admin approval** before activation
- Secure login/logout with session management
- JWT-based API authentication via Django REST Framework SimpleJWT
- Django Allauth integration for extensible authentication

### 👨‍⚕️ Doctor Portal
- **Doctor Dashboard** — Centralized overview for doctors
- **My Patients** — View and search all assigned patients with pagination
- **Patient Records** — Create, view, and update patient medical records
- **Profile Management** — Update personal and professional details
- **Department Management** — Browse doctors and patients within departments

### 🧑‍🤝‍🧑 Patient Portal
- **Patient Dashboard** — View personal medical records and history
- **View Records** — Access diagnostics, treatments, observations, and prescriptions
- **Download Prescriptions** — Download medicine descriptions as text files
- **Profile Updates** — Edit personal information

### 🏢 Department Management
- Browse all hospital departments
- View doctors and patients organized by department
- Department-based filtering and specialization tracking

### 🔌 REST API
- Full CRUD API endpoints for Patients, Doctors, Departments, and Records
- JWT token authentication (`/api/token/` and `/api/token/refresh/`)
- CORS enabled for frontend integration

---

## 🛠️ Tech Stack

| Layer         | Technology                                      |
|---------------|--------------------------------------------------|
| **Backend**   | Python 3.12, Django 5.x                          |
| **Database**  | SQLite (development) — easily swappable to PostgreSQL |
| **API**       | Django REST Framework, SimpleJWT                 |
| **Auth**      | Django Allauth, Custom User Model                |
| **Frontend**  | Django Templates, HTML5, CSS3                    |
| **Static**    | WhiteNoise (production-ready static file serving)|
| **Deployment**| Gunicorn, Procfile (Heroku-ready)                |

---

## 📁 Project Structure

```
Hospital-Main/
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
└── PatientPro/                 # Django project root
    ├── manage.py               # Django management script
    ├── db.sqlite3              # SQLite database
    ├── Procfile                # Deployment config
    │
    ├── PatientPro/             # Project settings
    │   ├── settings.py         # Configuration
    │   ├── urls.py             # Root URL routing
    │   ├── wsgi.py             # WSGI entry point
    │   └── asgi.py             # ASGI entry point
    │
    ├── MediAccess/             # Main application
    │   ├── models.py           # Data models (CustomUser, Department, PatientRecord)
    │   ├── views.py            # View logic & controllers
    │   ├── forms.py            # Form definitions
    │   ├── urls.py             # App URL routing
    │   ├── admin.py            # Admin configuration
    │   ├── backends.py         # Custom authentication backend
    │   └── api/                # REST API
    │       ├── views.py        # API views
    │       ├── serializers.py  # DRF serializers
    │       └── urls.py         # API URL routing
    │
    └── templates/              # HTML templates
        ├── base.html           # Base layout
        ├── login.html          # Login page
        ├── register.html       # Registration page
        ├── home.html           # Home page
        ├── doctor_dashboard.html
        ├── patient_dashboard.html
        ├── doctor_list.html
        ├── patient_list.html
        ├── department_list.html
        └── ...                 # Additional templates
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** installed
- **pip** package manager
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/piyushp3030h/Hospital-management-.git
   cd Hospital-management-
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv env
   source env/bin/activate        # Linux/macOS
   env\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install whitenoise
   ```

4. **Apply database migrations**
   ```bash
   cd PatientPro
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 👤 User Roles

| Role        | Access                                                              |
|-------------|----------------------------------------------------------------------|
| **Admin**   | Full access via `/admin/` — manage users, approve doctors, manage departments |
| **Doctor**  | Dashboard, patient records, department views, profile management     |
| **Patient** | Dashboard, view own records, download prescriptions, update profile  |

> **Note:** Doctor accounts are **inactive by default** and must be approved by an admin before they can log in.

---

## 📡 API Endpoints

| Method | Endpoint                  | Description               |
|--------|---------------------------|---------------------------|
| POST   | `/api/token/`             | Obtain JWT access token   |
| POST   | `/api/token/refresh/`     | Refresh JWT token         |
| GET    | `/api/patients/`          | List all patients         |
| GET    | `/api/doctors/`           | List all doctors          |
| GET    | `/api/departments/`       | List all departments      |
| GET    | `/api/records/`           | List patient records      |

---

## ⚙️ Configuration

Key settings in `PatientPro/PatientPro/settings.py`:

| Setting               | Default       | Description                        |
|-----------------------|---------------|------------------------------------|
| `DEBUG`               | `True`        | Set to `False` in production       |
| `ALLOWED_HOSTS`       | `['*']`       | Restrict in production             |
| `DATABASES`           | SQLite        | Switch to PostgreSQL for production|
| `CORS_ALLOW_ALL_ORIGINS` | `True`     | Restrict in production             |

---

## 📄 License

This project is developed for educational purposes as part of a university semester project.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request
