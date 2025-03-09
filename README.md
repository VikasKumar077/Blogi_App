# Blogi 📝  
A full-stack blog platform built with modern technologies, designed to create, view, edit, and delete posts with secure authentication. 

🟩 **Live Project:** [Blogi App](https://blogi-frontend.vercel.app/) 🚀

## 🛠️ Tech Stack  

### 🖼️ **Frontend:**  
- 🟢 **Next.js 13+** — For server-side rendering and client-side navigation  
- ⚡ **Axios** — For making HTTP requests to the backend  
- 🎨 **Tailwind CSS** — For styling the UI with pre-built components and responsiveness  

### ⚙️ **Backend:**  
- 🚀 **FastAPI** — For building the RESTful API  
- 🟡 **SQLModel** — For interacting with the database using Python models  
- 🟠 **SQLAlchemy** — For advanced ORM capabilities  
- 🔐 **JWT (JSON Web Tokens)** — For secure user authentication and authorization  
- 📘 **Pydantic** — For data validation and serialization  

### 🗃️ **Database:**  
- 🐘 **PostgreSQL** — A powerful relational database  
- ☁️ **Neon (Cloud PostgreSQL)** — For hosting the database  

### 📡 **Deployment:**  
- ▲ **Vercel** — For deploying the Next.js frontend  
- 🌍 **Render/Any Cloud Service** — For deploying the FastAPI backend  

---

With **Blogi**, users can:  
- 📝 **Create** public or private posts  
- ✏️ **Update** their own posts  
- 🗑️ **Delete** their posts  
- 👀 **View** public posts (even without logging in)  

Public posts are visible to everyone, while private posts are only accessible to logged-in users. Role-based access control ensures users can only edit or delete their own content.  


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

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create your .env file:
DATABASE_URL=postgresql://username:password@host:port/dbname
SECRET_KEY=your_secret_key

Run the FastAPI server:
uvicorn main:app --reload

3. Frontend Setup:
Navigate to the frontend folder:
cd ../frontend

Install dependencies:
npm install

Run the Next.js development server:
npm run dev

4. Access the App:
Frontend: http://localhost:3000
Backend (API docs): http://localhost:8000/docs


🔐 Authentication Flow
Register: Create an account with a unique username and password.
Login: Receive a JWT token upon successful login.
Protected Routes: Token is stored in localStorage, and Axios adds it to the headers (Authorization: Bearer <token>).


⚠️ Authorization Rules
Only authors can edit or delete their posts.
Unauthorized actions show proper alerts in the frontend.
Token expiration or invalid tokens return appropriate errors.


🛡️ Security Features
Password Hashing: Uses bcrypt for hashing user passwords.
JWT Tokens: Encodes user ID and username, with an expiration time.
Token Verification: Validates the token in protected routes.


🐛 Error Handling
401 Unauthorized: Token missing, invalid, or expired.
403 Forbidden: Trying to edit/delete someone else's post.
404 Not Found: Post doesn't exist.
422 Unprocessable Entity: Invalid or missing data.


🟢 API Endpoints
Authentication
POST /auth/register/: Register a new user
POST /auth/login/: Login and receive a token
Posts
GET /public-posts/: View all public posts
GET /posts/{id}: View a specific post by ID
POST /create-post/: Create a new post (protected)
PUT /update-post/{id}: Update a post (protected)
DELETE /delete-post/{id}: Delete a post (protected)


🛠️ Deployment
You can deploy the backend with services like Render or Railway and the frontend with Vercel. Make sure to update the API URLs accordingly!

🙌 Contributing
If you’d like to contribute, feel free to fork the repo and create a pull request!

📄 License
This project is licensed under the MIT License.






