# 🏥 Hospital CRM (Under Construction)

🚧 **Project Status:** _Under Development_

## 📌 Overview
A **Hospital CRM application** built using **Django** to manage patient appointments, reports, payments, and doctor interactions efficiently. 

## 🎯 Features (In Progress)
- ✅ User Authentication (Patients, Doctors, Admins)
- ✅ Appointment Booking & Management
- ✅ Patient Report Generation & Viewing
- ✅ Payment System Integration
- ✅ Emergency Chat with Doctors (WebSockets)
- 🔜 Video Consultation (Upcoming)
- 🔜 REST API Integration using Django REST Framework (Upcoming)

## 🛠️ Tech Stack
- **Backend:** Django, Django Channels, Django REST Framework (Upcoming)
- **Frontend:** HTML, CSS, JavaScript (React/Flutter Planned)
- **Database:** PostgreSQL / SQLite
- **Payment Gateway:** Razorpay / Stripe
- **Real-time Chat:** Django Channels (WebSockets)

## 🚀 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/rohith-dev-10/hospital-crm.git
cd hospital-crm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## 🔥 Roadmap
### **Phase 1: Web-based MVP (Without DRF) – 30 Days**
#### **Week 1: Project Setup & Authentication**
- ✅ Set up Django project, database, and virtual environment.
- ✅ Implement user authentication (Login, Register, Logout).
- ✅ Role-based access control (Patient, Doctor, Admin).
- ✅ Create dashboards for each role.

#### **Week 2: Appointments & Doctor Dashboard**
- ✅ Implement appointment booking (Patients can book, Doctors can view/manage).
- ✅ Appointment status update (Approved/Rejected/Pending).
- ✅ Doctor dashboard to view appointments & manage reports.
- ✅ Patient dashboard to view appointments & reports.

#### **Week 3: Reports, Payments & Emergency Chat**
- ✅ Implement report generation by doctors (with PDF download).
- ✅ Payment gateway integration (Razorpay/Stripe) for consultation fees.
- ✅ Emergency chat system using Django Channels (WebSockets).

#### **Week 4: UI Improvements, Testing & Deployment**
- ✅ Improve UI/UX with Bootstrap/Tailwind.
- ✅ Implement email notifications for appointments & reports.
- ✅ Profile management for users.
- ✅ Testing & debugging.
- ✅ Deploy project on Render/Vercel/DigitalOcean.

### **Phase 2: API & Mobile Support (With DRF) – 30 Days**
#### **Week 1: DRF Setup & Authentication API**
- ✅ Install & configure Django REST Framework (DRF).
- ✅ Convert authentication to JWT-based API.
- ✅ Create User Profile API (Patients & Doctors).
- ✅ Implement role-based API permissions.

#### **Week 2: Appointments & Reports API**
- ✅ Convert Appointment Booking to REST API.
- ✅ Implement API for appointment status updates & notifications.
- ✅ Convert Patient Reports into an API (View & Download).

#### **Week 3: Payments, Chat & Video Consultation API**
- ✅ Integrate payment gateway API (Razorpay/Stripe).
- ✅ Convert chat system into WebSocket API (Django Channels).
- ✅ Implement Video Consultation API using WebRTC/Twilio.

#### **Week 4: Mobile/Web Frontend & Deployment**
- ✅ Build frontend with React/Flutter.
- ✅ Fetch data via REST APIs.
- ✅ Implement real-time notifications using Firebase.
- ✅ Testing & debugging.
- ✅ Deploy backend API & frontend.

## 📢 Contributing
Contributions are welcome! Fork the repo, create a feature branch, and submit a PR. 🚀

## 📝 License
This project is licensed under the **MIT License**.

## 📬 Contact
**Developer:** [Rohith Uppunuthula](https://github.com/rohith-dev-10)  
📧 Email: uppunuthula.rohith@gmail.com

