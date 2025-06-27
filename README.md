
# SocialMedia Backend

A scalable and secure backend architecture developed with **Django** and **Django REST Framework**, serving as the core engine for an Instagram-inspired social media platform. This project emphasizes software development best practices, data security, and extensibility.

---

## Key Features

- ### User Management & Authentication  
  - Robust user registration and login with strict data validation  
  - JWT (JSON Web Tokens) based authentication for high security and scalability  
  - Support for password reset and email verification  
  - Easily extendable to support OAuth2 and social logins

- ### RESTful API Design  
  - Reliable and standardized APIs for managing posts, comments, likes, and followers  
  - Custom serializers ensuring data integrity and validation  
  - Pagination, filtering, and search capabilities to improve performance and UX

- ### Security & Data Protection  
  - Implementation of Django’s best security practices including protection against CSRF, XSS, and SQL Injection  
  - Secure storage and hashing of sensitive data like passwords using bcrypt algorithms  
  - Rate limiting to prevent DoS and brute-force attacks  
  - Secure token and secret key management in production environments

- ### Scalability & Maintainability  
  - Modular project structure adhering to SOLID principles  
  - Use of design patterns to separate business logic from presentation layers  
  - Database migrations managed with Django Migrations  
  - Easy to extend by adding new apps without impacting overall architecture

---

## Technologies & Tools

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- PostgreSQL / MySQL / SQLite (configurable)  
- JWT Authentication (via django-rest-framework-simplejwt)  
- Docker & Docker Compose (optional for development and deployment)  
- Git (version control)  

---

## Development Setup

```bash
# Clone the repository
git clone https://github.com/M-Tinati/socialmedia-backend.git
cd socialmedia-backend

# Run development server
python manage.py runserver

```
---

## Contact

For questions or collaboration, please reach out via email:
[mohammad_tinati@yahoo.com](mailto:mohammad_tinati@yahoo.com)




