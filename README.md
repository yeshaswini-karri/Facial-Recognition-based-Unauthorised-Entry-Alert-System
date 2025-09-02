# Facial Recognition Based Unauthorized Entry Alert System

A comprehensive security system that uses facial recognition technology to track authorized entries and send real-time alerts when unknown individuals are detected. The system features a user-friendly GUI, automated notifications, and detailed entry logging.

## 🚀 Features

- **Real-time Facial Recognition**: Uses OpenCV and LBPH (Local Binary Pattern Histogram) algorithm
- **User Registration**: Easy registration system with image capture and profile management
- **Entry Tracking**: Automatic logging of authorized entries with timestamps
- **Security Alerts**: Multi-channel alert system for unauthorized access attempts
- **Push Notifications**: Real-time mobile notifications via Pushover API
- **Email Alerts**: HTML email notifications with audio alerts
- **Data Management**: CSV-based storage for user details and entry logs
- **Password Protection**: Secure access to training functions
- **Modern GUI**: Intuitive Tkinter-based interface with real-time clock

## 📋 Requirements

### Hardware
- Computer with webcam/camera
- Internet connection (for notifications)

### Software Dependencies
```bash
pip install opencv-python
pip install numpy
pip install pandas
pip install Pillow
pip install playsound
pip install paho-mqtt
pip install requests
```

### Additional Files Required
- `haarcascade_frontalface_default.xml` (OpenCV Haar Cascade file)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/facial-recognition-entry-system.git
   cd facial-recognition-entry-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Haar Cascade file**
   Download `haarcascade_frontalface_default.xml` from OpenCV's GitHub repository and place it in the project root directory.
   ```bash
   wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
   ```

4. **Configure notification settings**
   - **Pushover Setup**: 
     - Create account at [Pushover.net](https://pushover.net)
     - Update `user_key` and `api_token` in the `send_push_notification()` function
   - **Email Setup**:
     - Update email credentials in `send_email_alert()` function
     - For Gmail, use app-specific passwords

## 🚀 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Register New Users**
   - Enter unique ID and full name
   - Click "Take Images" to capture face samples (300 images automatically)
   - Click "Save Profile" to train the recognition model

3. **Entry Tracking**
   - Click "LOG ENTRY" to start face recognition
   - System will automatically detect and log authorized entries
   - Unknown faces trigger security alerts after 15 consecutive detections

4. **Security Features**
   - Real-time push notifications for unauthorized access
   - Email alerts with audio alarms
   - Automatic entry logging with timestamps

## 📁 Project Structure

```
facial-recognition-entry-system/
│
├── main.py                              # Main application file
├── requirements.txt                     # Python dependencies
├── haarcascade_frontalface_default.xml  # Face detection model
├── README.md                           # Project documentation
├── LICENSE                             # MIT License file
│
├── UserDetails/                        # User registration data
│   └── UserDetails.csv                # Registered user information
│
├── TrainingImage/                      # Face training samples
│   └── [user_images]                  # Individual face samples
│
├── TrainingImageLabel/                 # Trained models
│   ├── Trainner.yml                   # LBPH model file
│   └── psd.txt                        # Encrypted password file
│
└── Entries/                           # Entry logs
    └── Entries_[date].csv             # Daily entry records
```

## ⚙️ Configuration

### Notification Settings

**Pushover Configuration (in main.py):**
```python
def send_push_notification():
    user_key = "your_pushover_user_key"        # Replace with your user key
    api_token = "your_pushover_api_token"      # Replace with your API token
    # ... rest of function
```

**Email Configuration (in main.py):**
```python
def send_email_alert():
    sender_email = "your_email@gmail.com"      # Replace with your email
    receiver_email = "alert_recipient@gmail.com"  # Replace with recipient
    password = "your_app_password"             # Use app password for Gmail
    # ... rest of function
```

### System Parameters
- **Recognition Threshold**: 10 consecutive frames for positive identification
- **Unknown Alert Threshold**: 15 consecutive unknown detections
- **Confidence Threshold**: 40 (lower = more strict recognition)
- **No Face Timeout**: 15 seconds before auto-exit

## 🔧 Troubleshooting

### Common Issues

1. **Camera not detected**
   - Ensure webcam is connected and not used by other applications
   - Try changing camera index in `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`

2. **Haar Cascade file missing**
   - Download from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)
   - Ensure file is in project root directory

3. **Poor recognition accuracy**
   - Ensure good lighting during image capture
   - Capture images from different angles
   - Increase number of training samples

4. **Email notifications not working**
   - Enable 2-factor authentication for Gmail
   - Use app-specific passwords instead of regular password
   - Check firewall settings

5. **Push notifications not working**
   - Verify Pushover API credentials
   - Check internet connection
   - Ensure Pushover app is installed on mobile device

## 📊 Data Management

### User Registration CSV Format
```csv
SERIAL NO.,,ID,,NAME
1,,001,,John Doe
2,,002,,Jane Smith
```

### Entry Logs CSV Format
```csv
Id,,Name,,Date,,Time
001,,John Doe,,02-09-2025,,14:30:25
002,,Jane Smith,,02-09-2025,,14:35:10
```

## 🔒 Security Features

- **Password Protection**: Training functions require password authentication
- **Unknown Detection**: Automatic alerts for unregistered individuals
- **Multiple Alert Channels**: Push notifications + email alerts
- **Entry Logging**: Comprehensive tracking of all access attempts
- **Confidence Scoring**: Adjustable recognition sensitivity
- **Auto-timeout**: System exits if no faces detected for extended period

## 🎯 System Workflow

1. **Registration Phase**
   - Capture 300+ face samples per user
   - Store user details in CSV database
   - Train LBPH recognition model

2. **Recognition Phase**
   - Real-time face detection using Haar Cascades
   - Face recognition using trained LBPH model
   - Confidence-based decision making

3. **Alert Phase**
   - Unknown face detection counting
   - Multi-channel notification system
   - Security response protocols

## 🛡️ Privacy & Ethics

- Ensure compliance with local privacy laws
- Inform users about facial recognition usage
- Securely store biometric data
- Regular data cleanup and management
- Consider opt-out mechanisms for users

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Registration Process
![Registration](screenshots/registration.png)

### Entry Tracking
![Entry Tracking](screenshots/entry_tracking.png)

## 🔧 Advanced Configuration

### Adjusting Recognition Sensitivity
```python
# In TrackImages() function
CONFIDENCE_THRESHOLD = 40  # Lower = more strict (20-100)
required_frames = 10       # Frames needed for recognition
unknown_threshold = 15     # Unknown detections before alert
```

### Camera Settings
```python
# In TrackImages() function
cam = cv2.VideoCapture(0)  # Change 0 to 1 for external camera
```

## 📱 Mobile App Integration

The system uses Pushover for mobile notifications. To receive alerts:

1. Install Pushover app on your mobile device
2. Create account and get user key
3. Configure the API settings in the code
4. Test notifications before deployment

## 🔄 Backup & Recovery

### Backing Up Data
```bash
# Backup user data
cp -r UserDetails/ backup/UserDetails_$(date +%Y%m%d)/
cp -r TrainingImage/ backup/TrainingImage_$(date +%Y%m%d)/
cp -r TrainingImageLabel/ backup/TrainingImageLabel_$(date +%Y%m%d)/
```

### Restoring Data
```bash
# Restore from backup
cp -r backup/UserDetails_YYYYMMDD/ UserDetails/
cp -r backup/TrainingImage_YYYYMMDD/ TrainingImage/
cp -r backup/TrainingImageLabel_YYYYMMDD/ TrainingImageLabel/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- Pushover for notification services
- Python community for excellent libraries
- Tkinter for GUI framework

## 📞 Support

For support and questions:
- Create an issue in this repository
- Email: your-email@example.com
- Documentation: Check the code comments for detailed explanations

## 🔄 Version History

- **v1.0.0** - Initial release with core facial recognition features
- **v1.1.0** - Added push notifications and email alerts
- **v1.2.0** - Enhanced security features and improved GUI
- **v1.3.0** - Added configuration management and better error handling

## ⚠️ Important Notes

- **Privacy**: Ensure proper consent before implementing facial recognition
- **Lighting**: Maintain consistent lighting for optimal recognition
- **Backup**: Regularly backup training data and user information
- **Testing**: Test all notification systems before production deployment
- **Security**: Keep API keys and passwords secure
- **Compliance**: Follow local laws regarding biometric data collection

## 🚀 Future Enhancements

- [ ] Web-based dashboard
- [ ] Mobile app for remote monitoring
- [ ] Multiple camera support
- [ ] Cloud storage integration
- [ ] Advanced analytics and reporting
- [ ] Integration with existing security systems
- [ ] Face mask detection capability
- [ ] Temperature scanning integration

---

**Built with ❤️ for enhanced security and peace of mind**

*For questions or contributions, please open an issue or submit a pull request.*