import cv2
import os
import numpy as np

dataPath ="C:/Users/USUARIO/Documents/rec_f/datos"
peopleList = os.listdir(dataPath)
labels =[]
facesData=[]
label = 0
for nameDir in peopleList:
    personPath =dataPath +'/'+nameDir
    print('read images')

    for fileName in os.listdir(personPath):
        print('Rostros:',nameDir+'/'+fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image =cv2.imread(personPath+'/'+fileName,0)
        cv2.imshow('image',image)
        cv2.waitKey(10)
    label=label+1

face_reco = cv2.face.LBPHFaceRecognizer_create()
print("entrenando")
face_reco.train(facesData,np.array(labels))
face_reco.write('modelo_recface.xml')
print("modelo entrenado")