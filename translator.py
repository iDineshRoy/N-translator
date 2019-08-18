import speech_recognition as sr
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import clipboard

def Record():

    r = sr.Recognizer()
    setText("Say something..")
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ne-NP')
            setText("Done!")
            entryText.insert(END,text+"। ")
        except:
            setText('Sorry, could not understand you!')

def Upload():
    try:
        sourceFile = fd.askopenfilename(initialdir= "/", title='Please select a file')
        processUploaded(sourceFile)
    except:
        setText("Error occured while selecting the file!")

def setText(text):
    labeltext.set(text)

def copyToClipboard():
    input = entryText.get("1.0",END)
    clipboard.copy(input)

def showmessageBox():
    messagebox.showinfo("About N-translator", "Developed by: Dinesh Kumar Roy\nEmail: dinesh.roy@hotmail.com\n\nA VPIT Software\nwww.vpit.com.np")

def processUploaded(sourceFile):
    r=sr.Recognizer()
    fileName=sourceFile
    with sr.AudioFile(fileName) as source:
        audio = r.listen(source)
        setText("Processing done!")
        try:
            text = r.recognize_google(audio, language='ne-NP')
            
            entryText.insert(END,text+"। ")
        except:
            setText('Sorry, could not understand you!')


def main_screen():
    root = Tk()
    root.geometry("830x460")
    root.title("N-translator")
    

    topFrame = Frame(root)
    topFrame.pack(side=TOP)
    bottomFrame = Frame(root)
    bottomFrame.pack()

    labelName = Label(topFrame, text="Speech-To-Text converter", font=("Calibri", 14), fg="green")
    labelName.pack(fill=X)

    bgcolor = "green"
    recordButton = Button(bottomFrame, text="Record", fg="white", bg=bgcolor, command=Record)
    uploadButton = Button(bottomFrame, text="Upload", fg="white", bg=bgcolor, command=Upload)
    aboutButton = Button(bottomFrame, text="About", fg="white", bg=bgcolor, command=showmessageBox)
    copyButton = Button(bottomFrame, text="Copy to Clipboard", fg="white", bg=bgcolor, command=copyToClipboard)
    

    recordButton.grid(row=0,column=0,padx=5,pady=10, sticky="n")
    uploadButton.grid(row=1,column=0)
    aboutButton.grid(row=0,column=2, padx=5,pady=10, sticky="n")
    copyButton.grid(row=1, column=2)

    global labeltext
    labeltext=StringVar()
    labelStatus = Label(bottomFrame, textvariable=labeltext, text="", font=("Calibri", 14), fg="blue")
    labelStatus.grid(row=1, column=1)


    global entryText
    global translatedtext
    translatedtext=StringVar()
    entryText = Text(bottomFrame)
    entryText.grid(row=0, column=1, ipadx=5, ipady=5)

    
    root.mainloop()

main_screen()