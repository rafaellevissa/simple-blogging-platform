# 📝 Simple Blogging Platform API

A RESTful API built with Django and Django REST Framework to manage a simple blogging platform, supporting posts and comments.

---

## 🚀 How to run the project

### 📦 Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)


### ⚙️ Setup

1. Create a `.env` file in the project root based on the `.env.example` file.

2. Build and start the containers:

```bash
docker compose up --build
```

3. In another terminal, apply the migrations:

```bash
docker compose exec app python manage.py migrate
```

---

## 📄 API Documentation

The documentation for the endpoints is available in the Postman collection located at the root of the project.

---

## 🛠️ Technologies

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker + Docker Compose

---

## 🔮 Next steps (if more time was available)

If I had more time, I would:

* Add JWT authentication
* Add pagination and post ordering
* Add filters and search to endpoints
* Implement automated tests with Pytest or `unittest`
* Set up automated deployment with CI/CD

