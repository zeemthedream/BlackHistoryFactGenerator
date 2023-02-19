import io
import requests
import webbrowser
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image #install packages via terminal if you have not, see README
from googleapiclient.discovery import build #install packages via terminal if you have not, see README
from secret import blackHistoryToken, googleApiKey, engineCode

class BlackHistoryFactGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.myFont = tkfont.Font(family='Kefa', size=20, weight='bold')
        self.person = ""
        self.fact = ""
        self.source = ""
        self.customSearchResponse = ""

    def start(self):
        self.createScreen()

    def requests(self):
        #Black History Fact API request
        header = {
            "accept": "application/json",
            "x-api-key": blackHistoryToken
        }
        factResponeLength = 200
        response = (requests.get("https://rest.blackhistoryapi.io/fact/random?length={}".format(factResponeLength), headers=header)).json()
        print(response)
        self.person = response['Results'][0]['people'][0].split(",")[0]
        self.fact = response['Results'][0]['text']
        self.source = response['Results'][0]['source']

        #view response info in the console
        print("this is the person: ", self.person)
        print("this is the fact: ", self.fact)
        print("this is the source: ", self.source)

        #Google Custom Search API Requests
        resource = build('customsearch', 'v1', developerKey=googleApiKey).cse()
        result = resource.list(q=self.person, cx=engineCode, searchType='image', exactTerms=self.person).execute()
        personImageUrl = result['items'][0]['link']
        self.customSearchResponse = requests.get(personImageUrl)

        self.generateFact()
        self.generatePerson()

    def generateFact(self):
        self.formatFactString()
        factFont = tkfont.Font(family='Kefa', size=10)
        factLabel = tk.Label(self.root, text=self.fact, font=factFont)
        factLabel.place(relx=0.05, rely=0.68, relwidth=0.90, relheight=0.1)


    def generatePerson(self):
        try:
            imageInBytes = io.BytesIO(self.customSearchResponse.content)
            pilImage = Image.open(imageInBytes)
            pilImageResized = pilImage.resize((200,200))
            photo = ImageTk.PhotoImage(pilImageResized)

            #display photo on screen
            person = tk.Label(self.root, image=photo)
            person.image = photo #this is the convention to set image on window
            person.place(relx=0.25, rely=0.071, relwidth=0.55, relheight=0.55)

        except:
            print("Image of person was not found")

            # display empty person icon photo
            emptyIconImage = ImageTk.PhotoImage(file='images/icon.png')
            emptyIconLabel = tk.Label(self.root, image=emptyIconImage)
            emptyIconLabel.image = emptyIconImage #this is the convention to set image on window
            emptyIconLabel.place(relx=0.25, rely=0.071, relwidth=0.55, relheight=0.55)


    def learnMore(self):
        #open the source of the fact in the web browser
        webbrowser.open(self.source)

    def formatFactString(self):
        #format the fact string for the size of screen (9 words/line)
        if self.fact.count(" ") > 9:
            formattedString = ""
            count = 0
            for c in self.fact:
                if count % 9 == 0 and count != 0:
                    formattedString += "\n"
                    count = 0
                if c == " ":
                    count += 1
                formattedString += c
            self.fact = formattedString

    def createScreen(self):
        self.root.title("Black History Fact Generator")
        canvas = tk.Canvas(self.root, width=400, height=400, bd=1)
        canvas.pack()

        #background image for our TKinter Window
        background_image = tk.PhotoImage(file='images/background.png')
        background = tk.Label(self.root, image=background_image)
        background.place(relwidth=1, relheight=1)

        #frame for the picture of the person
        personFrame = tk.Frame(self.root,bg='brown')
        personFrame.place(relx=0.05, rely=0.05, relwidth=0.90, relheight=0.60)

        #frame for the fact about the person
        factFrame = tk.Frame(self.root)
        factFrame.place(relx=0.05, rely=0.68, relwidth=0.90, relheight=0.1)

        #buttons on the screen
        generateButtonFrame = tk.Frame(self.root, bg='brown')
        generateButtonFrame.place(relx=0.28, rely=0.85, relwidth=0.4, relheight=0.08, anchor='n')
        generate_button = tk.Button(generateButtonFrame, text="Generate Fact", font=self.myFont, command=self.requests)
        generate_button.pack()

        learnButtonFrame = tk.Frame(self.root, bg='brown')
        learnButtonFrame.place(relx=0.72, rely=0.85, relwidth=0.35, relheight=0.08, anchor='n')
        learn_button = tk.Button(learnButtonFrame, text="Learn More", font=self.myFont, command=self.learnMore)
        learn_button.pack()

        self.root.mainloop()

if __name__== '__main__':
    factGenerator = BlackHistoryFactGenerator()
    factGenerator.start()