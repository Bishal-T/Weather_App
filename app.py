from flask import Flask, render_template, request, flash, redirect, url_for
import requests, time, os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv('API')
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route("/")
def index():
    
        
    return render_template("index.html")




@app.post("/weather")
def weather():
    t = time.strftime("%I:%M %p")
       

    city = request.form.get("search-box")
    
    if not city:
        flash('Please enter a city', category='error')
        return redirect(url_for('index'))
    
    else:
        URL = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API}')
    
        data = requests.get(URL).json()
                
        weather = {
                        'city' : city,
                        'temperature' : data['main']['temp'],
                        'description' : data['weather'][0]['description'],
                        'humidity' : data['main']['humidity'],
                        'feels_like' : data['main']['feels_like'],
                        'icon' : data['weather'][0]['icon'],
                        'wind' : data['wind']['speed'],
                    }
        
    
    return render_template("weather.html", w = weather, time=t)
