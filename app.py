from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=30a631b0331915a04cf8b2a3ecc6a8a6')

        json_object = r.json()

        temperature = int(json_object['main']['temp']-273.15)
        feels_like = int(json_object['main']['feels_like']-273.15) 
        temp_min = int(json_object['main']['temp_min']-273.15) 
        temp_max = int(json_object['main']['temp_max']-273.15) 
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        wind = int(json_object['wind']['speed'])

        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']
        
        return render_template('home.html',temperature=temperature,feels_like=feels_like,temp_min=temp_min,temp_max=temp_max,pressure=pressure,humidity=humidity,city_name=city_name,condition=condition,wind=wind,desc=desc)
    else:
        return render_template('home.html') 


if __name__ == '__main__':
    app.run(debug=True)