import tkinter as tk
import requests
import json
from PIL import ImageTk,Image  


err=None
img=None
cloud=None
pres_temp=None
mintemp=None
maxtemp=None
pressure=None
humid=None

def weath_disp(city):
    global err
    global img
    global cloud
    global pres_temp
    global mintemp
    global maxtemp
    global pressure
    global humid
    
    

    api_key="9a5124291d9068671d05524842e31964"
    base_url=f"http://api.openweathermap.org/data/2.5/weather?q={city.get()}&appid={api_key}"
    response=requests.get(base_url)
    data=response.json() 
    if data["cod"]==200:  
        if err:
            err.destroy()
        if img:
            img.destroy()
        if cloud:
            cloud.destroy()
        if pres_temp:
            pres_temp.destroy()
        if mintemp:
            mintemp.destroy()
        if maxtemp:
            maxtemp.destroy()
        if pressure:
            pressure.destroy()
        if humid:
            humid.destroy()
        
        
        cloud_situ= (data["weather"][0]["description"])
        temp_situ= round(data["main"]["temp"]-273,2)
        tempmin=round(data["main"]["temp_min"]-273,2)
        tempmax=round(data["main"]["temp_max"]-273,2)
        press_situ=(data["main"]["pressure"])
        hum_situ=(data["main"]["humidity"])
        cloud=tk.Label(root, text=f"Clouds: {cloud_situ}", font=("Comic Sans",15))
        cloud.place(x=150,y=160)
        pres_temp=tk.Label(root, text=f"Present temperature: {temp_situ} degree celsius", font=("Comic Sans",15))
        pres_temp.place(x=150,y=190)
        mintemp=tk.Label(root, text=f"Minimum Temperature: {tempmin} degree celsius", font=("Comic Sans",15))
        mintemp.place(x=150,y=220)
        maxtemp=tk.Label(root, text=f"Maximum Temperature: {tempmax} degree celsius", font=("Comic Sans",15))
        maxtemp.place(x=150,y=250)
        pressure=tk.Label(root, text=f"Pressure: {press_situ}", font=("Comic Sans",15))
        pressure.place(x=150,y=280)
        humid=tk.Label(root, text=f"Humidity: {hum_situ}", font=("Comic Sans",15))
        humid.place(x=150,y=310)
        if temp_situ>=30:
            load = Image.open("hot.png")
            loader = load.resize((75, 75), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(loader)
            img = tk.Label(root, image=render)
            img.image = render
            img.place(x=35, y=200)
        elif temp_situ<=18:
            load = Image.open("cold.png")
            loader = load.resize((75, 75), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(loader)
            img = tk.Label(root, image=render)
            img.image = render
            img.place(x=35, y=200)
        else:
            load = Image.open("warm.png")
            loader = load.resize((75, 75), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(loader)
            img = tk.Label(root, image=render)
            img.image = render
            img.place(x=35, y=200)
              
    else:
        err=tk.Label(root,fg="red",text="Please enter a valid city", font=("Comic Sans",15,"bold"))
        err.place(x=150,y=150)
        err.update()
        city.delete("0","end")


root=tk.Tk()
root.geometry("600x400")
root.title("Weather Report")
root.resizable(False,False)

main_head=tk.Label(root, text="Basic weather forecast", font=("Comic Sans",18,"bold"))
main_head.place(x=170,y=10)

ent=tk.Label(root, text="Enter the city you want the report for: ", font=("Comic Sans",15))
ent.place(x=130,y=50)

box=tk.Entry(root, width=35,font=("Comic Sans",12))
box.place(x=135,y=90)

box.bind("<Return>",lambda x:weath_disp(box))

butt=tk.Button(root,text="Enter", font=("Comic Sans",12),command=lambda :weath_disp(box))
butt.place(x=280,y=120)


tk.mainloop()

