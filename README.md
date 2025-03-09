# Blogi 📝  
A full-stack blog platform built with **Next.js 13+** and **FastAPI**, using **PostgreSQL** as the database. Blogi allows users to create, view, update, and delete posts with **JWT authentication** for secure access.

## 🛠️ Tech Stack
- **Frontend:** Next.js 13+, Axios  
- **Backend:** FastAPI, SQLModel, JWT  
- **Database:** PostgreSQL (hosted on Neon)  
- **Authentication:** JWT (JSON Web Tokens)  
- **Styling:** CSS Modules  

## 🚀 Features
- **User Authentication:** Register and log in securely with password hashing and JWT tokens.  
- **Post Management:** Create, view, edit, and delete posts.  
- **Public & Private Posts:** Public posts are visible to everyone; private posts are accessible only to the author.  
- **Token-Based Authorization:** Edit and delete buttons are hidden for public posts.  
- **Automatic Timestamps:** `created_at` and `last_updated` fields.  
- **Role-Based Access:** Only post authors can edit or delete their posts.  
- **Error Handling:** Frontend alerts for unauthorized access or invalid tokens.  

## 📂 Project Structure
Blogi_App/ ├── backend/ │ ├── main.py # FastAPI entry point │ ├── auth.py # Authentication routes │ ├── crud.py # CRUD operations │ ├── database.py # Database connection (PostgreSQL) │ ├── models.py # SQLModel schemas │ └── .env # Environment variables (DB credentials, secret keys) ├── frontend/ │ ├── pages/ │ │ ├── index.js # Home page (list public and private posts) │ │ ├── login.js # User login page │ │ ├── register.js # User registration page │ │ ├── create-post.js # Create a new post │ │ ├── view/[id].js # View a single post │ │ └── edit/[id].js # Edit or delete a post │ ├── components/ │ │ └── Navbar.js # Navigation bar with auth state │ ├── styles/ # CSS Modules │ └── .env.local # Frontend environment variables


## 🛠️ Setup & Installation

1. **Clone the repository:**  

git clone https://github.com/yourusername/Blogi_App.git
cd Blogi_App

2. Backend Setup:
Navigate to the backend folder:
cd backend

