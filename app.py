# from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, FloatField, SubmitField
# from wtforms.validators import DataRequired
# import os
# import logging
# import google.generativeai as genai
# from dotenv import load_dotenv
# from flask_cors import CORS
# from flask import Flask, send_from_directory
# import os




# # Initialize Flask App
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Load API Key Securely
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")
# if not API_KEY:
#     raise ValueError("❌ GEMINI_API_KEY is missing. Set it in your .env file!")
# genai.configure(api_key=API_KEY)

# # Configure Logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger(__name__)

# # Flask App Configuration
# app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "dev-key-123")
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Database Setup
# db = SQLAlchemy(app)

# # Database Model
# class GreenZone(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     lat = db.Column(db.Float, nullable=False)
#     lon = db.Column(db.Float, nullable=False)

#     def to_dict(self):
#         return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

# # Ensure Database is Created
# def init_db():
#     with app.app_context():
#         db.create_all()
#         logger.info("✅ Database Initialized!")
# init_db()

# # Form for Adding Green Zones
# class AddZoneForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])
#     lat = FloatField("Latitude", validators=[DataRequired()])
#     lon = FloatField("Longitude", validators=[DataRequired()])
#     submit = SubmitField("Add Zone")

# # Routes
# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/services")
# def services():
#     return render_template("services.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# @app.route("/map")
# def map_page():
#     return render_template("map.html")

# @app.route("/add-zone", methods=["GET", "POST"])
# def add_zone():
#     form = AddZoneForm()
#     if form.validate_on_submit():
#         try:
#             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
#             db.session.add(new_zone)
#             db.session.commit()
#             logger.info(f"✅ Added Green Zone: {form.name.data}")
#             return redirect(url_for("map_page"))
#         except Exception as e:
#             db.session.rollback()
#             logger.error(f"❌ Error adding zone: {str(e)}")
#             return "Error adding zone. Please try again."
#     return render_template("add_zone.html", form=form)

# @app.route("/api/green-zones", methods=["GET"])
# def get_green_zones():
#     try:
#         zones = GreenZone.query.all()
#         return jsonify([zone.to_dict() for zone in zones])
#     except Exception as e:
#         logger.error(f"❌ Error fetching zones: {str(e)}")
#         return jsonify({"error": "Unable to fetch zones"}), 500

# # AI Chatbot Endpoint
# # @app.route("/chat", methods=["POST"])
# # def chat():
# #     try:
# #         data = request.get_json()
# #         prompt = data.get("prompt", "").strip()
# #         if not prompt:
# #             return jsonify({"error": "No prompt provided"}), 400
        
# #         logger.info(f"Received prompt: {prompt}")
# #         model = genai.GenerativeModel("gemini-2.0-flash


# ") 
# #         response = model.generate_content(prompt)
        
# #         if not response or not response.text:
# #             return jsonify({"error": "AI response empty"}), 500

# #         return jsonify({"response": response.text})
# #     except Exception as e:
# #         logger.error(f"❌ AI Chatbot Error: {str(e)}")
# #         return jsonify({"error": f"Server error: {str(e)}"}), 500

# @app.route('/chat')
# def chat():
#     return render_template('chat.html')  # Now served from the templates folder

# # Other routes like /map, /add-zone, etc.

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)

# # Custom Error Pages
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template("500.html"), 500

# # Run Flask Server
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8080)
from flask import Flask, request, jsonify, render_template, redirect, flash, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_cors import CORS
from functools import wraps
import logging
import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")

# App setup
app = Flask(_name_)
app.secret_key = 'secretkey123'
CORS(app, resources={r"/api/": {"origins": ""}})
genai.configure(api_key=GEMINI_API_KEY)

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(_name_)

# Database setup
BASE_DIR = os.path.abspath(os.path.dirname(_file_))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class GreenZone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

with app.app_context():
    db.create_all()

# Forms
class AddZoneForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    lat = FloatField("Latitude", validators=[DataRequired()])
    lon = FloatField("Longitude", validators=[DataRequired()])
    submit = SubmitField("Add Zone")

# API key protection
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        client_key = request.headers.get("x-api-key")
        if not client_key or client_key != INTERNAL_API_KEY:
            abort(401, description="Unauthorized: Invalid or missing API key")
        return f(*args, **kwargs)
    return decorated

# Utility
def get_city_coordinates(city_name):
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={GOOGLE_MAPS_API_KEY}"
        response = requests.get(url).json()
        if response['status'] == 'OK':
            location = response['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    except Exception as e:
        logger.error(f"Geocode error: {str(e)}")
    return None, None

def get_aqi_data_grid(city_name):
    lat, lon = get_city_coordinates(city_name)
    if lat is None or lon is None:
        return None

    points = []
    step = 0.05
    for i in range(-3, 4):
        for j in range(-3, 4):
            lat_val = lat + i * step
            lon_val = lon + j * step
            url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat_val}&lon={lon_val}&appid={OPENWEATHER_API_KEY}"
            try:
                response = requests.get(url).json()
                if response.get("list"):
                    aqi = response["list"][0]
                    points.append({
                        "lat": lat_val,
                        "lon": lon_val,
                        "aqi": aqi["main"]["aqi"],
                        "pm2_5": aqi["components"]["pm2_5"],
                        "pm10": aqi["components"]["pm10"]
                    })
            except Exception as e:
                logger.warning(f"AQI fetch failed at ({lat_val}, {lon_val}): {e}")
    return points

# API Routes
@app.route("/weather/<city>")
@require_api_key
def get_weather(city):
    points = get_aqi_data_grid(city)
    if not points:
        return jsonify({"error": "Could not fetch AQI data"}), 500
    return jsonify(points)

@app.route("/gemini", methods=["POST"])
@require_api_key
def use_gemini():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return jsonify({"response": response.text})

@app.route("/api/map")
@require_api_key
def get_map_url():
    return jsonify({
        "embed_url": f"https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_API_KEY}&q=Eiffel+Tower,Paris+France"
    })

@app.route("/api/green-zones")
def get_green_zones():
    try:
        zones = GreenZone.query.all()
        return jsonify([z.to_dict() for z in zones])
    except Exception as e:
        logger.error(f"API Fetch Error: {e}")
        return jsonify({"error": "Unable to fetch zones"}), 500

@app.route("/predict-green-locations", methods=["POST"])
def predict_green_locations():
    try:
        data = request.get_json()
        city = data.get("city")
        if not city:
            return jsonify({"error": "City is required"}), 400
        points = get_aqi_data_grid(city)
        if not points:
            return jsonify({"error": "Failed to fetch AQI data"}), 500
        hotspots = sorted(points, key=lambda x: x['aqi'], reverse=True)[:3]
        prompt = "Suggest plantation ideas for:\n"
        for i, pt in enumerate(hotspots):
            prompt += f"{i+1}. Lat: {pt['lat']}, Lon: {pt['lon']}, AQI: {pt['aqi']}\n"
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return jsonify({
            "city": city,
            "hotspots": hotspots,
            "gemini_suggestions": response.text or "No suggestion returned"
        })
    except Exception as e:
        logger.error(f"Gemini Prediction Error: {e}")
        return jsonify({"error": str(e)}), 500

# Web Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/services/aqi')
@app.route('/services/ai-green')
@app.route('/services/manual-add')
def coming_soon():
    return render_template("coming_soon.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        logger.info(f"Contact Message Received - Name: {name}, Email: {email}, Message: {message}")
        flash("Thanks for contacting us! We'll get back to you soon 🌿", "success")
        return redirect(url_for('contact'))
    return render_template("contact.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/add-zone", methods=["GET", "POST"])
def add_zone():
    form = AddZoneForm()
    if form.validate_on_submit():
        try:
            new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
            db.session.add(new_zone)
            db.session.commit()
            flash("Green Zone added successfully!", "success")
            return redirect(url_for("map_page"))
        except Exception as e:
            db.session.rollback()
            logger.error(f"Add Zone Error: {e}")
            flash("Failed to add zone. Try again.", "danger")
    return render_template("add_zone.html", form=form)

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500

# Run the app
if _name_ == "_main_":
    app.run(debug=True)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))
#     app.run(host='0.0.0.0', port=port)


