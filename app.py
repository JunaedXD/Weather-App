from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "8a953deef4ad5e5404dc16965370f23b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.json.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400

    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            result = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
            return jsonify(result)
        else:
            return jsonify({"error": "City not found"}), 404

    except requests.exceptions.RequestException:
        return jsonify({"error": "Could not connect to weather service"}), 500

if __name__ == "__main__":
    app.run(debug=True)
