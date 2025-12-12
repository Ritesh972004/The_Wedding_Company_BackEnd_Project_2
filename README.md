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

# 📁 Project Structure  

app/
├── routers/
├── services/
├── repositories/
├── models/
├── utils/
│ ├── config.py
│ ├── security.py
│ ├── database.py
├── main.py
.env
README.md
requirements.txt

yaml
Copy code

---

# ⚙ Installation  

Install dependencies:

```bash
pip install -r requirements.txt
🧩 MongoDB Setup
✔ Option A: Local MongoDB
Download → https://www.mongodb.com/try/download/community
Runs at:

arduino
Copy code
mongodb://localhost:27017
✔ Option B: MongoDB Atlas
Use your cloud connection string in .env.

🔧 Environment Variables
Create .env file:

ini
Copy code
SECRET_KEY=your_secret_key
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=org_master_db
▶ Running the Application
Start server:

bash
Copy code
uvicorn app.main:app --reload
Open API documentation:

arduino
Copy code
http://127.0.0.1:8000/docs
📡 API Endpoints
🟩 Organization APIs
Method	Endpoint	Description
POST	/org/create	Create organization + admin
GET	/org/get	Get organization
PUT	/org/update	Update organization
DELETE	/org/delete	Delete organization

🟦 Admin APIs
Method	Endpoint	Description
POST	/admin/login	Login with JWT

🧪 Testing Instructions
✔ Swagger UI
bash
Copy code
http://localhost:8000/docs
✔ Postman
Create organization

Login admin

Copy JWT token

Click Authorize → Add token

Test protected APIs

❗ Error Handling
Code	Meaning
400	Bad input
401	Unauthorized
404	Not found
422	Validation failed
500	Server error

All errors are returned in JSON with proper descriptions.

🔐 Security
JWT authentication

Password hashing (bcrypt)

.env used for secrets

Input validation enabled

No sensitive logs printed

🚀 Future Enhancements
Role-based access (Admin, Employee, SuperAdmin)

Email verification

Analytics dashboard

Activity logs

Cloud deployment

Rate limiting
