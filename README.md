# EduPresence – Automated Student Attendance System

EduPresence is a 5‑week MVP project to build a facial‑recognition based attendance system for college classrooms.  
It includes a React Native student app, Node.js backend, Python facial‑recognition microservice, and a React faculty dashboard.

## Project structure

edupresence-mvp/
├── mobile-app/ # React Native student app
├── backend/ # Node.js/Express API server
├── facial-recognition-service/ # Python/Flask + DeepFace service
├── faculty-dashboard/ # React web dashboard for faculty
├── docs/ # Setup, API, architecture, troubleshooting
├── .github/workflows/ci.yml # CI tests (backend, mobile, dashboard)
├── README.md
├── SETUP.md
├── CONTRIBUTING.md
└── .env.example

text

## Tech stack

- **Mobile:** React Native (Expo)
- **Backend:** Node.js, Express, MongoDB, Firebase
- **ML service:** Python, Flask, DeepFace, TensorFlow
- **Dashboard:** React, React Router, Socket.io
- **Cloud:** MongoDB Atlas, Google Cloud / Firebase

## Team roles

- Member 1 – UI/UX Designer (Figma)
- Member 2 – Frontend (React Native)
- Member 3 – Backend (Node/Express)
- Member 4 – AI/ML (Facial Recognition)
- Member 5 – Database & Cloud
- Member 6 – Integration & QA Lead

## Development workflow

- Work happens on feature branches (see `CONTRIBUTING.md`).
- PRs are merged into `develop` after tests pass and review.
- `main` is kept production‑ready.