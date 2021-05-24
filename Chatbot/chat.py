# Pytorch (CPU): pip3 install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
# Pytorch (GPU, cuda 10): pip3 install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
# nltk: pip install nltk


import random
import json
import time
import torch
import torch.nn as nn
import numpy as np
import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
from datetime import datetime


#import mysql.connector
#Conection to BD
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="12345678",
#  database="pascalBD"
#)


def tokenize(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return out
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)
FILE = "data.pth"

data = torch.load(FILE)
#data = torch.load(FILE, map_location='cpu')

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


#Funcion de activacion bot.
bot_name = "Pascal"
print("Hablemos!")
def chatbot (sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:

            if tag == intent["tag"]:
                respuesta=random.choice(intent['responses'])
                print(f"{bot_name}: {respuesta}"+ "         Tag: "+tag)
                return (respuesta,tag)
    else:
        print(f"{bot_name}: No he entendido...")
        return ("void","void")

#Funciones de Navegacion.
def Navegacion_Biblioteca():
    print(f"{bot_name}: Quieres que te acompañe a la Biblioteca")
    Answer = input("You: ")
    if (Answer == "si" or Answer == "si porfavor"):
        print("De acuerdo vamos.......")
    else:
        print("De acuerdo aqui estare")
def Navegacion_ATM():
    print(f"{bot_name}: Quieres que te acompañe al cajero automatico")
    Answer = input("You: ")
    if (Answer == "si" or Answer == "si porfavor"):
        print("De acuerdo vamos.......")
    else:
        print("De acuerdo aqui estare")
def Navegacion_Maquinas():
            print(f"{bot_name}: Quieres que te acompañe a las maquinas dispensadoras")
            Answer = input("You: ")
            if (Answer == "si" or Answer == "si porfavor"):
                print("De acuerdo vamos.......")
            else:
                print("De acuerdo aqui estare")
def Navegacion_Internacionalizacion():
            print(f"{bot_name}: Quieres que te acompañe a la oficina de internacionalizacion")
            Answer = input("You: ")
            if (Answer == "si" or Answer == "si porfavor"):
                print("De acuerdo vamos.......")
            else:
                print("De acuerdo aqui estare")
def Navegacion_Admisiones():
    print(f"{bot_name}: Quieres que te acompañe a la oficina de admisiones")
    Answer = input("You: ")
    if (Answer == "si" or Answer == "si porfavor"):
        print("De acuerdo vamos.......")
    else:
        print("De acuerdo aqui estare")
def Navegacion_Auditorio():
    print(f"{bot_name}: Quieres que te acompañe al auditorio")
    Answer = input("You: ")
    if (Answer == "si" or Answer == "si porfavor"):
        print("De acuerdo vamos.......")
    else:
        print("De acuerdo aqui estare")
def Navegacion_Papeleria():
    print(f"{bot_name}: Quieres que te acompañe a la papeleria")
    Answer = input("You: ")
    if (Answer == "si" or Answer == "si porfavor"):
        print("De acuerdo vamos.......")
    else:
        print("De acuerdo aqui estare")
#Funcion Identificar Tag
def IdetificarTag(tag):
    if (tag=="Navegacion_Biblioteca" or tag=="Ubicacion_Biblioteca"):
        Navegacion_Biblioteca()
    if (tag=="Navegacion_ATM" or tag=="Ubicacion_ATM"):
        Navegacion_ATM()
    if (tag=="Navegacion_Maquinas" or tag=="Ubicacion_Maquinas"):
        Navegacion_Maquinas()
    if (tag=="Navegacion_Internacionalizacion" or tag=="Ubicacion_Internacionalizacion"):
        Navegacion_Internacionalizacion()
    if (tag=="Navegacion_Admisiones" or tag=="Ubicacion_Admisiones"):
        Navegacion_Admisiones()
    if (tag=="Navegacion_Auditorio" or tag=="Ubicacion_Auditorio"):
        Navegacion_Auditorio()
    if (tag=="Navegacion_Papeleria" or tag=="Ubicacion_Papeleria"):
        Navegacion_Papeleria()

#Funciones Audio
#def Audio(text):

# Answer,tag
#   [0] , [1]


while True:
    inputword = input("Tu: ")
    if inputword== "hola pascal":
        chatbot(inputword)
        while True:
            inputword = input("Tu: ")
            x = (chatbot(inputword))
            IdetificarTag(x[1])
            if x[1]== "Despedidas" or x[1]=="Gratitud":
                break

