import pyrebase

firebaseConfig = {
    "apiKey": " ",
    "storageURL": " ",
    "databaseURL": " ",
    "authDomain": " ",
    "projectId": " ",
    "storageBucket": " ",
    "messagingSenderId": " ",
    "appId": " ",
    "measurementId": " ",
    "serviceAccount": " "
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()

#TO DOWNLOAD STORAGE DIRECTORY
#path = "DownloadImages"
#all_files = storage.child("ImageSourceDirectory").list_files() #Enter the name of the folder
#for file in all_files:
#    try:
#        print(file.name+" Downloading")
#        file.download_to_filename(file.name)
#    except:
#       print('Images Downloaded')

#RETURN VALUE TO SEARCH
from Search import *
def returnValues(id):
    flag = False
    result = db.child("csvTable").get()
    for res in result.each():
        if res.key() == id:
            flag = True
    return flag

#EMPTY THE csvTable
#result = db.child("csvTable").get()
#for res in result.each():
#    db.child("csvTable").remove()

#db.child("idTable").child("0206ct181100").remove()

# INSERT DATA db
# data={'Name':"PRIYANSH VERMA"}
# db.child("idTable").child("0206cs181118").set(data)

#data1={'Name':"SHUBH AGRAWAL"}
#db.child("idTable").child("0208cs181100").set(data1)

#data2={'Name':"YOGESH DIXIT"}
#db.child("idTable").child("0208cs181128").set(data2)

#data3={'Name':"YASH MISHRA"}
#db.child("idTable").child("0206cs181186").set(data3)

#data4={'Name':"VIDHUSHI CHOUBEY"}
#db.child("idTable").child("0206cs181183").set(data4)

#data5={'Name':"RITIKA TRIVEDI"}
#db.child("idTable").child("0206cs181130").set(data5)

#data6={'Name':"PURVI ANAND"}
#db.child("idTable").child("0206cs181119").set(data6)

#data7={'Name':"PRAVEEN TIWARI"}
#db.child("idTable").child("0206cs181116").set(data7)

#data8={'Name':"PRACHI GUJAR"}
#db.child("idTable").child("0206cs181108").set(data8)

#data9={'Name':"NEHA NORIYA"}
#db.child("idTable").child("0206cs181096").set(data9)

#data10={'Name':"NEHA DWIVEDI"}
#db.child("idTable").child("0206cs181094").set(data10)

#data11={'Name':"MOHIT HIRDE"}
#db.child("idTable").child("0206cs181086").set(data11)

#data12={'Name':"KRATIKA VYAS"}
#db.child("idTable").child("0206cs181079").set(data12)

#data13={'Name':"KAUSHIKIE SHRIVASTAVAA"}
#db.child("idTable").child("0206cs181077").set(data13)

#data14={'Name':"ARPIT PHILLAURA"}
#db.child("idTable").child("0206cs181030").set(data14)

#data15={'Name':"APURVA SHRIVASTAVA"}
#db.child("idTable").child("0206cs181029").set(data15)



# GET DATA db
#print("Realtime DB")
#result=db.child("idTable").get()
#for res in result.each():
#    print(res.key())

# UPLOAD FILE storage
# file=input("Name of file") #local
# cloudfilename=input("File name in storage") #remote
# storage.child(cloudfilename).put(file)

# GET URL storage
# print(storage.child(cloudfilename).get_url(none))

# DOWNLOAD FILE storage
# cloudfilename=input("File name in storage: ")
# print(storage.child(cloudfilename).get_url(None))
# downloadlink=input("URL: ")
# storage.child(downloadlink).download(img)

# READ FILE storage
# path=input("enter the path want to read")
# url=storage.child(path).get_url(None)
# f=urllib.request.urlopen(url).read(url)
# print(f)
