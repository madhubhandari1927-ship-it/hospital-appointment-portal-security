\# Hospital Appointment Portal – Security Project



\## Project Overview



This project is a Django-based Hospital Appointment Portal developed for a cybersecurity course. The application demonstrates common web application security vulnerabilities and their corresponding security fixes.



\## Technologies Used



\* Python 3.13

\* Django 6.1

\* SQLite

\* HTML

\* Git and GitHub



\## Security Vulnerabilities and Fixes



\### 1. Broken Access Control – Patient Medical Records



\*\*Vulnerability:\*\* Unauthorized users could potentially access another patient's medical record.



\*\*Fix:\*\* Access is restricted to the patient themselves or authorized staff users.



\### 2. Broken Access Control / IDOR – Appointment Details



\*\*Vulnerability:\*\* An authenticated user could attempt to access another patient's appointment by changing the appointment ID in the URL.



\*\*Fix:\*\* The application verifies that the logged-in user owns the appointment or is an authorized staff user.



\### 3. SQL Injection



\*\*Vulnerability:\*\* Unsafe database querying can allow malicious input to alter database queries.



\*\*Fix:\*\* Django ORM filtering is used instead of constructing SQL queries directly from user input.



\### 4. Cross-Site Scripting (XSS)



\*\*Vulnerability:\*\* Appointment reason data containing malicious HTML/JavaScript could be rendered by the browser.



\*\*Demonstration:\*\* The vulnerable version used unsafe rendering and demonstrated an XSS alert.



\*\*Fix:\*\* Django's normal template escaping is used by rendering:



`{{ appointment.reason }}`



instead of unsafe rendering with `|safe`.



\### 5. Security Misconfiguration



\*\*Vulnerability:\*\* Django was configured with `DEBUG = True`, which can expose detailed application and debugging information.



\*\*Fix:\*\* Debug mode was disabled:



`DEBUG = False`



and allowed hosts were configured for local testing.



\## Medical Record Encryption



Patient medical records are protected using Fernet encryption before being stored.



The application provides methods to encrypt and decrypt medical-record data.



\## Security Testing



Each vulnerability was tested using a controlled local Django environment.



For each vulnerability, BEFORE and AFTER screenshots were captured to demonstrate:



1\. The vulnerable behavior.

2\. The security fix.

3\. The corrected behavior.



\## Running the Project



Clone the repository and enter the project directory.



Install the required dependencies, then run:



```bash

python manage.py migrate

python manage.py check

python manage.py runserver

```



Open the application at:



`http://127.0.0.1:8000/`



\## Project Structure



```text

hospital-appointment-portal/

│

├── appointments/

│   ├── migrations/

│   ├── templates/

│   ├── models.py

│   ├── views.py

│   └── ...

│

├── hospital/

│   ├── settings.py

│   ├── urls.py

│   └── ...

│

├── db.sqlite3

├── manage.py

└── README.md

```



\## Repository



GitHub repository:



Hospital Appointment Portal Security Project



