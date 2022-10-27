from tkinter import *
import json
import requests

root=Tk()
root.title("My Weather App")
root.geometry("600x600")
root.overrideredirect(True)

root.configure(background="red")
#Setting labels
capital_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="white")
capital_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.35,rely=0.25,anchor=CENTER)

country_info_label = Label(root,text="Country: ", bg="white", font=("bold", 10))
country_info_label.place(relx=0.23,rely=0.5,anchor=CENTER) 

region_info_label = Label(root,text="Region: ", bg="white", font=( "bold",10)) 
region_info_label.place(relx=0.22,rely=0.55,anchor=CENTER)

language_info_label = Label(root,text="Language: ", bg="white", font=( "bold",10)) 
language_info_label.place(relx=0.22,rely=0.6,anchor=CENTER) 

population_info_label = Label(root,text="Population: ", bg="white", font=( "bold",10)) 
population_info_label.place(relx=0.22,rely=0.65,anchor=CENTER)
    
area_info_label = Label(root,text="Area: ", bg="white", font=( "bold",10)) 
area_info_label.place(relx=0.22,rely=0.7,anchor=CENTER) 
    
def cityDetails():
    api = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    apiOutputJSON= json.loads(api.content)
    cityName = city_entry.get()
    
    country = apiOutputJSON[0]["name"]
    print(country)
    
    region = apiOutputJSON[0]["region"]
    print(region)
    
    language = apiOutputJSON[0]["languages"][0]["name"]
    print(language)
    
    population = apiOutputJSON[0]["population"]
    print(population)
    
    area = apiOutputJSON[0]["area"]
    print(area)
    
    
    country_info_label['text'] = "Country:" + str(country)
    region_info_label['text'] = "Region:" + str(region)
    language_info_label['text'] = "Language:" + str(language)
    population_info_label['text'] = "Population:" + str(population)
    area_info_label['text'] = "Area:" + str(area)
    
    city_entry.destroy()
    btn.destroy()
    
    root.title(cityName)
    
btn = Button(root, text="search", command = cityDetails)
btn.place(relx=0.3, rely=0.8)

root.mainloop()