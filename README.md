# 🎨 Django Personal Painting Website

A web application built with **Django** to showcase artwork, including **portraits, acrylic paintings, pencil sketches**, and more. Users can view paintings, read about the artist, and contact the artist. Only the admin (you) can upload, edit, or delete paintings.

## 🚀 Features
- 📌 **Gallery**: Displays all uploaded paintings.
- 🖼️ **Image Upload**: Admin can upload paintings with a title and medium used.
- 🔍 **View Full Image**: Click on an image to view it in full screen with a dark overlay.
- ✏️ **Edit & Delete**: Modify or remove paintings (admin only).
- 📃 **About Page**: Information about the artist.
- 📞 **Contact Page**: Display contact details.
- 🌐 **Responsive Design**: Works on all devices with a beautiful UI.

---

## 🛠️ Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/Ayan-1829/Django-Personal-Painting-Website.git
cd painting_website
```

### **2. Create & Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser** (For Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompt to set up a username and password.

### **6. Run the Server**
```bash
python manage.py runserver
```
Now, open **http://127.0.0.1:8000/** in your browser.

---

## 📂 Project Structure
```
📁 gallery/             # Main app for paintings
 ├── 📂 static/         # CSS & images
 ├── 📂 templates/      # HTML files
 ├── models.py          # Database models
 ├── views.py           # Backend logic
 ├── urls.py            # URL routing
 └── forms.py           # Django forms
📁 media/               # Uploaded paintings
📁 templates/           # Global templates
manage.py               # Django management file
requirements.txt        # Dependencies

```

## 🎨 How to Use
1. **Visit the Home Page** to see all paintings.
2. **Click on an Image** to view it in full-screen mode.
3. **Admin Login**: Go to `http://127.0.0.1:8000/admin/` to add, edit, or delete paintings.
4. **Upload a Painting** from the admin panel by specifying the title, image, and medium used.
5. **About & Contact Pages** provide artist details.

---

## 🛠️ Technologies Used
- **Python** & **Django** (Backend)
- **HTML, CSS** (Frontend)
- **SQLite** (Database)

---

## 🤝 Contributing
Want to contribute? Fork the repo, make changes, and submit a pull request!

---

## 📧 Contact
For any inquiries, reach out to **Ayan** at:
📩 Email: [ayansarkar1829@gmail.com](mailto:ayansarkar1829@gmail.com)

---

⭐ **If you like this project, don't forget to star the repository!** ⭐
