# Hospital Appointment Portal - Security Project

## Project Overview

This project is a Django-based Hospital Appointment Portal developed for a cybersecurity course.

The project demonstrates common web application security vulnerabilities and their corresponding security fixes using a controlled local environment.

## Technologies Used

* Python 3.13
* Django 6.1
* SQLite
* HTML
* Cryptography (Fernet)
* Git
* GitHub

## Security Vulnerabilities and Fixes

### 1. Broken Access Control - Patient Medical Records

**Vulnerability:**
Unauthorized users could potentially access another patient's medical record.

**Fix:**
Access is restricted to the patient themselves or authorized staff users.

The application checks the logged-in user before displaying medical-record information.

---

### 2. Broken Access Control / IDOR - Appointment Details

**Vulnerability:**
An authenticated user could attempt to access another patient's appointment by changing the appointment ID in the URL.

**Example:**

```text
/appointment/2/
```

Changing the appointment ID could expose another patient's appointment if authorization checks were missing.

**Fix:**
The application verifies that the logged-in user owns the appointment or is an authorized staff user before displaying the appointment.

---

### 3. SQL Injection - Doctor Search

**Vulnerability:**
Unsafe database querying can allow malicious input to alter database queries.

**Fix:**
The application uses Django ORM filtering instead of constructing SQL queries directly from user input.

Example:

```python
Doctor.objects.filter(name__icontains=search)
```

---

### 4. Cross-Site Scripting (XSS)

**Vulnerability:**
Appointment reason data containing malicious HTML/JavaScript could be rendered by the browser if unsafe template rendering was used.

**Demonstration:**
The vulnerable version was tested with an XSS payload:

```html
<script>alert("XSS Test")</script>
```

**Fix:**
Django's normal template escaping is used:

```django
{{ appointment.reason }}
```

instead of unsafe rendering with:

```django
{{ appointment.reason|safe }}
```

This prevents the submitted JavaScript from being executed as HTML/JavaScript.

---

### 5. Security Misconfiguration

**Vulnerability:**
Django was initially configured with:

```python
DEBUG = True
```

Debug mode can expose detailed application information.

**Fix:**

```python
DEBUG = False
```

The application also uses configured allowed hosts:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

The Django secret key was also rotated after the original key was exposed during development.

---

## Medical Record Encryption

As an additional security measure, patient medical records are protected using Fernet encryption before being stored.

The `PatientProfile` model provides methods for encrypting and decrypting medical-record data.

This provides an additional layer of protection for sensitive patient information if the database contents are exposed.

## Authentication and Authorization

The application requires authentication for protected resources.

Authorization checks are performed before allowing users to access:

* Patient medical records
* Appointment details

Patients can access their own information, while authorized staff users can access protected records where permitted.

## Security Testing

Each vulnerability was tested in a controlled local Django environment.

For each vulnerability, BEFORE and AFTER screenshots were captured where applicable to demonstrate:

1. The vulnerable behavior.
2. The security fix.
3. The corrected behavior.

## Running the Project

Run database migrations:

```bash
python manage.py migrate
```

Check the Django project:

```bash
python manage.py check
```

Start the development server:

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
hospital-appointment-portal/
|
+-- appointments/
|   +-- migrations/
|   +-- templates/
|   +-- models.py
|   +-- views.py
|
+-- hospital/
|   +-- settings.py
|   +-- urls.py
|   +-- ...
|
+-- db.sqlite3
+-- manage.py
+-- README.md
```

## Security Configuration

The project uses:

* `DEBUG = False`
* Configured `ALLOWED_HOSTS`
* Rotated Django `SECRET_KEY`
* Authentication for protected views
* Authorization checks for patient-owned resources
* Django ORM queries
* Django template escaping
* Fernet encryption for medical records

## Repository

**Hospital Appointment Portal Security Project**
