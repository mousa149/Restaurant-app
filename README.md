# 🍔 Restaurant App

> A simple Django-based application for adding, listing and managing food items.

---

## 🧩 Project Overview
Food App is a web application built with **Django** that allows users to register, log in, and manage food items with images, descriptions, and prices. The app features user authentication, CRUD operations for food items, and a clean UI using Bootstrap.

---

## ⚙️ Tech Stack
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap 4, minimal JS  
- **Templating:** Django Templates  
- **Database:** SQLite (default Django DB)  
- **Media Handling:** Pillow (for image upload fields)

---

## 🏗️ Architecture
- **Pattern:** Django MTV (Model–Template–View)  
- **Apps:**
  - `food` — handles food item models, templates, and CRUD logic  
  - `users` — handles registration, login/logout, and profile management
- **Templates:** Shared `base.html` with Bootstrap navigation and message alerts  
- **Static & Media:** Managed via Django staticfiles and media configuration

---

## ✨ Features
- ✅ User registration, login, logout  
- 🍽️ Add, list, and delete food items  
- 🖼️ Image upload support for each food item  
- 👤 User profiles with avatar support  
- 🔔 Flash messages for success and errors  
- 🧭 Responsive Bootstrap-based layout

---

## 🧪 Testing
Currently no test files included, but recommended:
- Unit tests for models, forms, and views (`python manage.py test`)  
- UI tests with Selenium or Playwright  
- Mock database setup for isolated testing

---

## 📁 Folder Structure
```
mysite/
├── food/
│   ├── static/food/style.css
│   ├── templates/food/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── detail.html
│   │   ├── item-form.html
│   │   └── item-delete.html
│   └── (models.py, views.py, forms.py, urls.py)
├── users/
│   └── templates/users/
│       ├── login.html
│       ├── logout.html
│       ├── register.html
│       └── profile.html
├── manage.py
└── README.md
```

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔮 Future Improvements
- Add unit/integration tests  
- Implement pagination and search filters  
- Add API endpoints with Django REST Framework  
- Improve UI and responsiveness  
- Add permissions for edit/delete actions  
- Dockerize the app for deployment  
- CI/CD pipeline integration with GitHub Actions

---

## 📸 Screenshots


```
my_project/
│
├── screenshots/
│   ├── home.png
│   ├── detail.png
│   └── profile.png
```


### 🏠 Home Page
![Home Page]screenshots\home page.png)

### 🍔 Item Detail Page
![Item Detail](screenshots\item details.png)

### 👤 User Profile
![User Profile](screenshots\user profile.png)
<img width="1920" height="1080" alt="add item" src="https://github.com/user-attachments/assets/52b423cf-a7c5-4af9-b3ef-8b7f55c4e975" />
<img width="1920" height="1080" alt="admin" src="https://github.com/user-attachments/assets/e74ecd0c-e6b4-4c06-bdc9-e3c11366f736" />
<img width="1920" height="1080" alt="home page" src="https://github.com/user-attachments/assets/1b5ab01d-a209-4020-8cd5-3e8c51591912" />
<img width="1920" height="1080" alt="item details" src="https://github.com/user-attachments/assets/49c563d5-56ea-4b03-a069-f4965e38373c" />
<img width="1920" height="1080" alt="items" src="https://github.com/user-attachments/assets/fc561474-640f-4879-8ce5-d077a6962cac" />
<img width="1920" height="1080" alt="user details" src="https://github.com/user-attachments/assets/f73cec82-26f6-4913-b48d-de65f7fd40ad" />
<img width="1920" height="1080" alt="user profile" src="https://github.com/user-attachments/assets/0b779d49-f603-4e0d-b2f9-ca71f00f5fe3" />
<img width="1920" height="1080" alt="users" src="https://github.com/user-attachments/assets/5211de39-1469-4402-b277-2cdfdd4d1d5d" />



---

## 🌐 Social Links
- **Author:** MOUSA IBRAHIM ALI 
- **GitHub:** https://github.com/mousa149
- **Email:** mousa1499@gmail.com  
- **LinkedIn:** www.linkedin.com/in/mousa-ibrahim-2409781a6


- **Upwork:** https://www.upwork.com/freelancers/~01d500fffb37be33ca?mp_source=share

---

Made with ❤️ using Django.
