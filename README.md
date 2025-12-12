# 🚀 Organization Management Service – Backend API  
A complete, modular, multi-tenant backend built using **FastAPI** and **MongoDB**.  
Designed for assignments, interviews, real-world backend systems, and scalable SaaS platforms.

---

## 📸 Project Screenshot  


---
<img width="1813" height="911" alt="Page" src="https://github.com/user-attachments/assets/fd1cb77a-ff7b-44b2-a9f4-dd848791d7fc" />

# 📝 Overview  
This backend service supports:

- Multi-organization onboarding  
- Admin account creation for each organization  
- JWT authentication  
- CRUD operations for organizations  
- A clean, custom white-themed Swagger UI for easy testing  
- A properly modular architecture for maintainability  

The system follows industry best practices and is suitable for internship assignment evaluation.

---

# ⭐ Features  

### 🏢 Organization Module  
- Create organization  
- Auto-create admin user  
- Update organization  
- Delete organization  
- Each organization gets its **own MongoDB collection**

### 🔐 Admin Module  
- Secure login using JWT tokens  
- Password hashing with bcrypt  

### 🎨 Custom Swagger UI  
- Light theme  
- Elegant white interface  
- Version badges removed  
- Designed for clean submission  

---

# 🛠 Tech Stack  

| Component | Technology |
|----------|------------|
| Language | Python 3.8+ |
| Framework | FastAPI |
| Database | MongoDB |
| Auth | JWT, Passlib |
| Validation | Pydantic |
| Server | Uvicorn |

---

# 🏗 High-Level Architecture Diagram  

<img width="583" height="708" alt="High-Level Architecture Diagram" src="https://github.com/user-attachments/assets/61eef665-883e-4961-b35b-95631766a4e5" />


# 💡 Design Choices  

### 1️⃣ Modular Architecture  
- `routers/` → API endpoints  
- `services/` → Business logic  
- `repositories/` → DB operations  
- `utils/` → Config, security, DB manager  

This ensures clean, scalable, testable code.

---

### 2️⃣ Multi-Tenant Database  
Each organization has its own collection:

org_master_db
├── org_company_one
├── org_company_two
└── org_company_three

yaml
Copy code

Benefits:  
✔ Isolation  
✔ Easy scaling  
✔ Better security  
✔ Clear structure  

---

### 3️⃣ JWT Authentication  
Used to secure all protected routes.  
Easy for scaling and frontend integration.

---

### 4️⃣ Customized Swagger UI  
- Clean white theme  
- Modern styling  
- Simplified UI for easy testing during evaluation  

---
🚀 Instructions to Run the Application

Follow the steps below to set up and run the Organization Management Service locally.

1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd organization-management-service

2️⃣ Create a Virtual Environment (recommended)
python -m venv .venv

3️⃣ Activate the Virtual Environment
Windows (PowerShell)
.\.venv\Scripts\Activate.ps1


If activation is blocked, run:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


Then activate again.

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Set Up Environment Variables

Create a .env file in the project root with the following content:

MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=org_master_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Organization Management Service
DEBUG=True


Make sure MongoDB is running on your machine.

6️⃣ Start the FastAPI Application
uvicorn app.main:app --reload --port 8000

7️⃣ Open the API Documentation
Swagger UI

👉 http://127.0.0.1:8000/docs


✔ The application is now running successfully!

You can test all API endpoints directly from Swagger UI.
