# Setup Guide

## Prerequisites

- Node.js 16+ and npm
- Python 3.8+ and pip
- Git
- MongoDB Atlas account
- Firebase / Google Cloud account

## 1. Clone repository

git clone https://github.com/YOUR_USERNAME/edupresence-mvp.git
cd edupresence-mvp


## 2. Environment variables

Copy the example file and fill in real values:

cp .env.example .env # Linux/macOS
REM or manually copy on Windows


Also copy component‑level examples:

- `backend/.env.example` → `backend/.env`
- `facial-recognition-service/.env.example` → `.env` in that folder

## 3. Install dependencies

### Mobile app

cd mobile-app
npm install
cd ..


### Backend

cd backend
npm install
cd ..


### Facial‑recognition service

cd facial-recognition-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
cd ..


### Faculty dashboard

cd faculty-dashboard
npm install
cd ..


## 4. Running the system in development

Open 4 terminals:

**Terminal 1 – Backend**

cd backend
npm run dev


**Terminal 2 – Facial recognition service**

cd facial-recognition-service
venv\Scripts\activate
python src/app.py


**Terminal 3 – Mobile app**

cd mobile-app
npm start


**Terminal 4 – Faculty dashboard**

cd faculty-dashboard
npm start


## 5. Testing

- Backend: `cd backend && npm test`
- Mobile: `cd mobile-app && npm test`
- Dashboard: `cd faculty-dashboard && npm test`

See `docs/SETUP.md` and `docs/TROUBLESHOOTING.md` for more details.