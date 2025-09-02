# Facial Recognition-Based Unauthorized Entry Alert System  

## 📌 Overview  
This project is a **real-time facial recognition security system** that detects and prevents unauthorized entry using **OpenCV and machine learning techniques**. It employs the **Haar Cascade Classifier** for face detection and the **LBPH algorithm** for recognition.  

The system provides **multi-layered alerts**:  
- **Tkinter GUI pop-ups** for local monitoring  
- **Email notifications** with sound alerts for remote security staff  
- **Push notifications (via Pushover API)** for instant mobile alerts  

It also maintains **robust entry logs**, supports **new registrations**, and offers a **user-friendly interface** for seamless management.  

---

## 🚀 Features  
- Real-time **face detection** using Haar Cascade  
- **LBPH recognition** for known individuals  
- **Automated alerts**:  
  - GUI pop-ups  
  - Email alerts with embedded alarm sound  
  - Push notifications with siren sound  
- **Entry logging** (CSV-based attendance system)  
- **New user registration** with ID and name  
- **Password-protected training and management**  
- **Tkinter-based GUI** for easy interaction  
- **Contactless, cost-effective security solution**  

---

## 🛠️ Requirements  

Install dependencies before running:  

```bash
pip install opencv-contrib-python pillow pandas playsound requests

