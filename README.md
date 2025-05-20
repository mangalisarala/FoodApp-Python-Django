# 🍔 FoodApp - Django Web Application
A simple and dynamic Django web app to display and manage food items like Pizza and Burger. Includes an intuitive UI with images, a details button, and navigation with options to add items or logout. Clicking the **FoodApp** brand takes you to the homepage.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS

## ✨ Features

- 🏠 **Homepage** with a list of food items (image, name, details button)
- ➕ **Add Item**: Authenticated users can add new food items
- 🔐 **Login/Logout** functionality
- 🔗 **Navbar** with:
  - `FoodApp` → Homepage
  - `Add Item` → Form to add new food
  - `Logout` → Ends session
## 🚀 Getting Started

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/myapp.git
cd myapp
```

### **2. Set Up a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux

python -m venv myenv
source myenv/Scripts/activate # For Windows
```

### **3. Install Dependencies**
```sh
pip install django
```

### **4. Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
```sh
python manage.py createsuperuser
```

### **6. Run the Development Server**
```sh
python manage.py runserver
```
Now open your browser at: http://127.0.0.1:8000/

