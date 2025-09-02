import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from playsound import playsound
import threading
import paho.mqtt.client as mqtt
import requests

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
def send_push_notification():
    user_key = "your_pushover_user_key"
    api_token = "your_pushover_api_token"
    message = "🚨 Unknown Entry Attempt Detected! 🚨\nCheck the entry gate immediately!"
    
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": api_token,
        "user": user_key,
        "message": message,
        "title": "Security Alert",
        "priority": 2,  # Force emergency priority
        "retry": 30,  # Retry every 30 seconds if not acknowledged
        "expire": 60,  # Keep retrying for 1 minute
        "sound": "siren"  # Play loud siren sound
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Push notification sent successfully!")
    else:
        print("Error sending push notification:", response.text)

##################################################################################
def send_email_alert():
    sender_email = "your_sender_email"  # Replace with your email
    receiver_email = "your_receiver_email"  # Change if needed
    password = "your_gmail_in_app_password"  # Use an app password if using Gmail
    
    subject = "URGENT: Unknown Face Detected"
    
    # Create HTML email with embedded auto-playing audio
    html_body = """
    <html>
    <head>
        <title>Security Alert</title>
    </head>
    <body>
        <h2 style="color: red;">⚠️ SECURITY ALERT ⚠️</h2>
        <p style="font-size: 16px;">An unknown person was detected during entry tracking.</p>
        <p style="font-size: 16px;">Please check the entry gate immediately.</p>
        <p style="font-size: 16px;">Time of detection: {}</p>
        
        <!-- Auto-playing audio alert -->
        <audio autoplay loop>
            <source src="https://www.soundjay.com/mechanical/sounds/smoke-detector-1.mp3" type="audio/mpeg">
            Your device does not support the audio element.
        </audio>
        
        <p><strong>Note:</strong> If you don't hear an alarm sound, please click the link below:</p>
        <p><a href="https://www.soundjay.com/mechanical/sounds/smoke-detector-1.mp3">Play Alarm Sound</a></p>
    </body>
    </html>
    """.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Attach HTML part
    msg.attach(MIMEText(html_body, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email alert sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200, tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'xxxxxxxxxxxxx@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp = (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel/psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False, False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
    lbl4.place(x=10, y=10)
    global old
    old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    old.place(x=180, y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
    nnew.place(x=180, y=80)
    cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
    if exists1:
        tf = open("TrainingImageLabel/psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel/psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

#######################################################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("UserDetails/")
    assure_path_exists("TrainingImage/")
    
    # Better serial number generation
    serial = 1
    exists = os.path.isfile("UserDetails/UserDetails.csv")
    if exists:
        # Read the CSV properly to find the highest serial number
        df = pd.read_csv("UserDetails/UserDetails.csv")
        if 'SERIAL NO.' in df.columns and not df.empty:
            # Get the highest serial number and add 1
            serial = df['SERIAL NO.'].max() + 1
    else:
        # Create new CSV file with headers if it doesn't exist
        with open("UserDetails/UserDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
        csvFile1.close()
    
    Id = (txt.get())
    name = (txt2.get())
    
    # Validate inputs
    if not Id:
        res = "Please enter an ID"
        message.configure(text=res)
        return
    
    # Check if ID already exists
    if exists:
        existing_ids = df['ID'].astype(str).tolist()
        if Id in existing_ids:
            res = f"ID {Id} already exists. Please use a different ID."
            message.configure(text=res)
            return
    
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage/ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 300:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        
        # Add the new  to the CSV with the unique serial number
        row = [serial, '', Id, '', name]
        with open('UserDetails/UserDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################
import time

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Entries/")
    assure_path_exists("UserDetails/")

    for k in tv.get_children():
        tv.delete(k)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    # Check if training file exists before reading
    try:
        recognizer.read("TrainingImageLabel/Trainner.yml")
    except Exception as e:
        # If no training file, reset recognizer to None
        mess._show(title='No Training', message='No trained model found. All faces will be treated as unknown.')
        recognizer = None

    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        mess._show(title='Error', message='Cannot access camera. Please check your camera connection.')
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']

    # Modified to handle empty CSV case
    try:
        df = pd.read_csv("UserDetails/UserDetails.csv")
        # If file is empty or only contains headers
        if df.empty:
            df = pd.DataFrame(columns=['SERIAL NO.', 'ID', 'NAME'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=['SERIAL NO.', 'ID', 'NAME'])

    attendance_marked = set()
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    attendance_file = f"Entries/Entries_{date}.csv"

    if not os.path.isfile(attendance_file):
        with open(attendance_file, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(col_names)

    face_recognition_count = {}
    unknown_face_count = 0
    required_frames = 10
    unknown_threshold = 15
    alert_sent = False
    CONFIDENCE_THRESHOLD = 40
    NO_FACE_TIMEOUT = 15  # Time limit in seconds for no face detection

    message.configure(text="Looking for registered faces...")
    window.update()

    last_face_detected_time = time.time()  # Track last face detection time

    while True:
        ret, im = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) == 0:
            cv2.imshow('Tracking', im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            # If no face detected, check timeout
            if time.time() - last_face_detected_time > NO_FACE_TIMEOUT:
                break  # Exit if no faces detected for 15 seconds

            continue  # Skip the rest of the loop if no faces found

        last_face_detected_time = time.time()  # Reset the timer when a face is detected

        entry_marked = False
        unknown_detected = True

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_roi = gray[y:y+h, x:x+w]

            try:
                # If no training data, treat all faces as unknown
                if recognizer is None:
                    cv2.putText(im, "Unknown (No Training)", (x, y-10), font, 0.7, (0, 0, 255), 2)
                    unknown_detected = True
                    continue

                serial, conf = recognizer.predict(face_roi)

                if conf < CONFIDENCE_THRESHOLD:
                    unknown_detected = False
                    unknown_face_count = 0

                    student_details = df[df['SERIAL NO.'] == serial]

                    if not student_details.empty:
                        student_id = str(student_details['ID'].values[0])
                        student_name = student_details['NAME'].values[0]

                        if student_id not in face_recognition_count:
                            face_recognition_count[student_id] = 0

                        face_recognition_count[student_id] += 1

                        recognition_progress = f"{student_name}: {face_recognition_count[student_id]}/{required_frames}"
                        cv2.putText(im, recognition_progress, (x, y-10), font, 0.7, (0, 255, 0), 2)

                        if face_recognition_count[student_id] >= required_frames and student_id not in attendance_marked:
                            ts = time.time()
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            attendance_data = [student_id, '', student_name, '', date, '', timeStamp]

                            with open(attendance_file, 'a+', newline='') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(attendance_data)

                            attendance_marked.add(student_id)
                            tv.insert('', 0, text=student_id, values=(student_name, date, timeStamp))

                            message_text = f"Entry logged for ID: {student_id}, Name: {student_name}"
                            message.configure(text=message_text)
                            window.update()

                            cv2.putText(im, "Entry Marked!", (x, y+h+25), font, 0.7, (0, 255, 0), 2)
                            cv2.imshow('Tracking', im)
                            cv2.waitKey(500)

                            entry_marked = True
                            break  
                    else:
                        cv2.putText(im, "Unknown", (x, y-10), font, 0.7, (0, 0, 255), 2)
                        unknown_detected = True
                else:
                    cv2.putText(im, "Unknown", (x, y-10), font, 0.7, (0, 0, 255), 2)
                    unknown_detected = True

            except Exception as e:
                print(f"Error: {e}")
                cv2.putText(im, "Processing Error", (x, y-10), font, 0.7, (0, 0, 255), 2)
                unknown_detected = True

        if entry_marked:
            break  

        if unknown_detected:
            unknown_face_count += 1
            cv2.putText(im, f"Unknown Detection: {unknown_face_count}/{unknown_threshold}", (10, 30), font, 0.7, (0, 0, 255), 2)

            if unknown_face_count >= unknown_threshold and not alert_sent:
                message.configure(text="⚠️ SECURITY ALERT: Unknown person detected! ⚠️")
                window.update()

                send_push_notification()
                send_email_alert()

                alert_sent = True

                cv2.putText(im, "SECURITY ALERT!", (10, 60), font, 0.7, (0, 0, 255), 2)
                
                cv2.imshow('Tracking', im)
                cv2.waitKey(500)

                break  

        else:
            unknown_face_count = 0

        cv2.imshow('Tracking', im)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    if len(attendance_marked) > 0:
        mess._show(title='Entry Complete', message=f'Successfully logged entry for {student_name}!')
    elif alert_sent:
        mess._show(title='Security Alert', message='Entry Restricted! Security has been notified.')
    else:
        mess._show(title='No Entry', message='No registered users were recognized.')
######################################## USED STUFFS ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
      '02': 'February',
      '03': 'March',
      '04': 'April',
      '05': 'May',
      '06': 'June',
      '07': 'July',
      '08': 'August',
      '09': 'September',
      '10': 'October',
      '11': 'November',
      '12': 'December'
      }


######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Facial Recognition Based Unauthorised Entry Alert System")
window.configure(background='#262523')

frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="                                                        Unauthorised Entry Alert System", fg="white", bg="#262523", width=55, height=1, font=('times', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text=day+"-"+mont[month]+"-"+year+"  |  ", fg="orange", bg="#262523", width=55, height=1, font=('times', 22, ' bold '))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="orange", bg="#262523", width=55, height=1, font=('times', 22, ' bold '))
clock.pack(fill='both', expand=1)
tick()

head2 = tk.Label(frame2, text="                                      For New Registrations                                      ", fg="black", bg="#3ece48", font=('times', 17, ' bold '))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                                      For Existing Members                                       ", fg="black", bg="#3ece48", font=('times', 17, ' bold '))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Enter ID", width=20, height=1, fg="black", bg="#00aeff", font=('times', 17, ' bold '))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="white", font=('times', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name", width=20, fg="black", bg="#00aeff", font=('times', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="white", font=('times', 15, ' bold '))
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="          Entry Details", width=20, fg="black", bg="#00aeff", height=1, font=('times', 17, ' bold '))
lbl3.place(x=100, y=115)

res = 0
exists = os.path.isfile("UserDetails/UserDetails.csv")
if exists:
    with open("UserDetails/UserDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0

##################### MENUBAR #################################

menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Change Password', command=change_pass)
filemenu.add_command(label='Contact Us', command=contact)
filemenu.add_command(label='Exit', command=window.destroy)
menubar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=82)
tv.column('name', width=130)
tv.column('date', width=133)
tv.column('time', width=133)
tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

###################### SCROLLBAR ################################

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="black", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="black", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="   LOG ENTRY  ", command=TrackImages, fg="black", bg="yellow", width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
trackImg.place(x=30, y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="black", bg="red", width=35, height=1, activebackground="white", font=('times', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()
