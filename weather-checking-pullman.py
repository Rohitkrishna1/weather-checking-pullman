from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root = Tk()
root.title('rohit krishna weather')
root.iconbitmap('')
root.geometry("400x50")

##api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=99163&distance=5&API_KEY=F8603563-300A-4302-89C3-58DCA821B983")
try:

    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=99163&distance=5&API_KEY=F8603563-300A-4302-89C3-58DCA821B983")
    api = json.loads(api_request.content)
    city =api[0]['ReportingArea']
    quality= api[0]['AQI']
    category=api[0]['Category']['Name']
except Exception as e:
    api = "Error....."

myLabel = Label(root, text=city +"Air Quality"+str(quality) + "   " + category)
myLabel.pack()


root.mainloop()