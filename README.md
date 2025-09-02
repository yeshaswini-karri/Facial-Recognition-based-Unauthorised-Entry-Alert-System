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


🛠️ Additional Requirements
Python 3.7+
Gmail account with App Password enabled for email alerts
Pushover account (for push notifications)
⚙️ Setup
Clone this repository or download the code.
Ensure haarcascade_frontalface_default.xml is in the project folder.
Update email credentials in the send_email_alert() function:
sender_email = "youremail@gmail.com"
receiver_email = "securityteam@gmail.com"
password = "your-app-password"
Update Pushover API credentials in send_push_notification().
▶️ Usage
Run the program:
python security_system.py
For new users:
Enter ID and Name → Take Images → Save Profile.
For existing users:
Click Log Entry → The system verifies faces in real-time.
If authorized → entry is logged.
If unauthorized → alerts are triggered.
📂 Project Structure
├── haarcascade_frontalface_default.xml   # Face detection model
├── UserDetails/                          # Stores registered user details
├── TrainingImage/                        # Captured training images
├── TrainingImageLabel/                   # Trained model (Trainner.yml)
├── Entries/                              # Entry/attendance logs
├── security_system.py                    # Main project file
⚠️ Notes
Use strong app passwords instead of plain Gmail passwords.
Ensure webcam access is enabled.
Press Q anytime to quit face tracking.
Unknown faces trigger alerts after repeated detections (to avoid false alarms).
📧 Contact
For queries or support, please contact:
📩 yourname@example.com

