
def mainfirebaseinteraction():
    import cv2
    import numpy as np
    import face_recognition
    import os
    import datetime
    import dlib
    import pyrebase

    firebaseConfig = {
        "apiKey": "",
        "storageURL": "",
        "databaseURL": "",
        "authDomain": "",
        "projectId": "",
        "storageBucket": "",
        "messagingSenderId": "",
        "appId": "",
        "measurementId": "",
        "serviceAccount": ""
    }
    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    storage = firebase.storage()


    path = 'ImageSourceDirectory'
    images = []
    classRollnos = []
    myList = os.listdir(path)
    camname = {0: "ENTRANCE", 1: "ADMIN BLOCK", 2: "LOBBY", 3: "CAFETERIA", 4: "CONTROL CENTRE", 5: "AMPHITHEATRE"}

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classRollnos.append(os.path.splitext(cl)[0])

    # print("[INFO: ImageSourceDirectory","Count=",len(myList),",ID's=",classRollnos,"]")

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    # CODE DUMP
    # INSERT DATA db
    # data={'Name':"PRIYANSH VERMA",'Location':"webcam",'Date':"06/05/21",'Time':"09:21:24"}
    # db.child("csvTable").child("0206cs181118").set(data)
    # data = {'Name': name , 'Location': camname.get(caplist.get(cap)) , 'Date': datenow, 'Time': timenow}
    # db.child("csvTable").child(name).set(data)
    # DOWNLOAD FILE storage
    # cloudfilename=input("File name in storage: ")
    # print(storage.child(cloudfilename).get_url(None))
    # downloadlink=input("URL: ")
    # storage.child(downloadlink).download(img)

    def timelocated(name, cap):
        noww = datetime.datetime.now()
        datenow = noww.strftime('%Y-%m-%d')
        timenow = noww.strftime('%I:%M:%S')

        personname = db.child("idTable").order_by_key().equal_to(name).get()
        for person in personname.each():
            studentname = person.val()['Name']
        data = {'Name': studentname,
                'Location': [camname.get(caplist.get(cap)), datenow, timenow, str(caplist.get(cap))]}
        db.child("csvTable").child(name).set(data)
        user = db.child("csvTable").get()
        users = user.val()
        val = False
        for i in users:
            if i == name:
                val = True

        if val == True:
            print("sending")
            db.child("csvTable").child(name).update(
                {"Location": [camname.get(caplist.get(cap)), datenow, timenow, str(caplist.get(cap))]})
        else:
            val = False

    encodeListKnown = findEncodings(images)
    # print("[INFO: Encodings Completed]")

    index = 0  # starting index fo cameras : 0 being the webcam
    getcam = []  # empty list to store camera indexing
    caplist = {}  # empty dictionary to store video stream and the cam index
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if not cap.read()[0]:
            break
        else:
            getcam.append(index)
        cap.release()
        index += 1

    for value in getcam:
        current = cv2.VideoCapture(value)
        caplist[current] = value
    print("[INFO:",caplist,"]")

    # The above code generates a dictionary with key as the name of the current
    # stream of video capture with the index from getcam as a value
    # the key <VideoCapture 0000017290F2F3B0> is used in the below code as the actual stream
    # where as the value is used for the display of which cam is showing , 0 always being the integrated webcam

    while True:

        for cap in caplist:
            try:
                success, img = cap.read()
                imgS = cv2.resize(img, (0, 0), None, 1, 1)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            except cv2.error as error:
                print("[Error]: {}".format(error))

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for (encodeFace, (top, right, bottom, left)) in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                count = 0

                if matches[matchIndex]:
                    name = classRollnos[matchIndex]
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
                    timelocated(name, cap)

                else:
                    name = "Unknown"
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)

            try:
                cv2.imshow(str(caplist.get(cap)), img)
            except cv2.error as error:
                print("[Error]: {}".format(error))
            cv2.waitKey(1)
