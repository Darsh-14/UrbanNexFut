# # # # # # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # from flask_wtf import FlaskForm
# # # # # # from wtforms import StringField, FloatField, SubmitField
# # # # # # from wtforms.validators import DataRequired
# # # # # # import os
# # # # # # import logging

# # # # # # # Configure logging
# # # # # # logging.basicConfig(level=logging.INFO)
# # # # # # logger = logging.getLogger(__name__)

# # # # # # app = Flask(__name__)
# # # # # # app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key

# # # # # # # Database Configuration
# # # # # # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # # # # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'green_zones.db')
# # # # # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # # # db = SQLAlchemy(app)

# # # # # # # Database Model
# # # # # # class GreenZone(db.Model):
# # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # #     name = db.Column(db.String(100), nullable=False)
# # # # # #     lat = db.Column(db.Float, nullable=False)
# # # # # #     lon = db.Column(db.Float, nullable=False)

# # # # # #     def __repr__(self):
# # # # # #         return f"GreenZone('{self.name}', {self.lat}, {self.lon})"

# # # # # # # Ensure Database is Created
# # # # # # with app.app_context():
# # # # # #     db.create_all()
# # # # # #     print("✅ Database initialized!")

# # # # # # # Form for Adding New Green Zones
# # # # # # class AddZoneForm(FlaskForm):
# # # # # #     name = StringField('Name', validators=[DataRequired()])
# # # # # #     lat = FloatField('Latitude', validators=[DataRequired()])
# # # # # #     lon = FloatField('Longitude', validators=[DataRequired()])
# # # # # #     submit = SubmitField('Add Zone')

# # # # # # # Home Page
# # # # # # @app.route('/')
# # # # # # def home():
# # # # # #     return render_template('home.html')

# # # # # # @app.route('/about')
# # # # # # def about():
# # # # # #     return render_template('about.html')

# # # # # # @app.route('/services')
# # # # # # def services():
# # # # # #     return render_template('services.html')

# # # # # # @app.route('/contact')
# # # # # # def contact():
# # # # # #     return render_template('contact.html')

# # # # # # # Map Page
# # # # # # @app.route('/map')
# # # # # # def map():
# # # # # #     return render_template('map.html')

# # # # # # # Add New Green Zone Form
# # # # # # @app.route('/add-zone', methods=['GET', 'POST'])
# # # # # # def add_zone():
# # # # # #     form = AddZoneForm()
# # # # # #     if form.validate_on_submit():
# # # # # #         try:
# # # # # #             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
# # # # # #             db.session.add(new_zone)
# # # # # #             db.session.commit()
# # # # # #             logger.info(f"✅ Added Green Zone: {form.name.data} ({form.lat.data}, {form.lon.data})")
# # # # # #             return redirect(url_for('map'))
# # # # # #         except Exception as e:
# # # # # #             db.session.rollback()
# # # # # #             logger.error(f"❌ Error adding zone: {e}")
# # # # # #             return "Error adding zone. Please try again."
    
# # # # # #     return render_template('add_zone.html', form=form)

# # # # # # # API to Fetch Green Zones
# # # # # # # Custom Error Handlers
# # # # # # @app.errorhandler(404)
# # # # # # def page_not_found(e):
# # # # # #     return render_template('404.html'), 404

# # # # # # @app.errorhandler(500)
# # # # # # def internal_server_error(e):
# # # # # #     return render_template('500.html'), 500

# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True, host='0.0.0.0', port=8080)

# # # # # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # from flask_wtf import FlaskForm
# # # # # from wtforms import StringField, FloatField, SubmitField
# # # # # from wtforms.validators import DataRequired
# # # # # import os
# # # # # import logging
# # # # # import google.generativeai as genai
# # # # # import os
# # # # # from dotenv import load_dotenv

# # # # # load_dotenv()  # Load API key from .env file
# # # # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # # # # Initialize Gemini API
# # # # # genai.configure(api_key=API_KEY)

# # # # # # Configure logging
# # # # # logging.basicConfig(
# # # # #     level=logging.INFO,
# # # # #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# # # # # )
# # # # # logger = logging.getLogger(__name__)

# # # # # app = Flask(__name__)

# # # # # # Development-only secret key (REPLACE FOR PRODUCTION)
# # # # # app.config['SECRET_KEY'] = 'dev-key-123'  # Simple key for development only
# # # # # logger.warning("Using development secret key - NOT SAFE FOR PRODUCTION")

# # # # # # Database Configuration
# # # # # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # # # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'green_zones.db')
# # # # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # # db = SQLAlchemy(app)

# # # # # # Database Model
# # # # # class GreenZone(db.Model):
# # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # #     name = db.Column(db.String(100), nullable=False)
# # # # #     lat = db.Column(db.Float, nullable=False)
# # # # #     lon = db.Column(db.Float, nullable=False)

# # # # #     def __repr__(self):
# # # # #         return f"GreenZone('{self.name}', {self.lat}, {self.lon})"

# # # # #     def to_dict(self):
# # # # #         return {
# # # # #             'id': self.id,
# # # # #             'name': self.name,
# # # # #             'lat': self.lat,
# # # # #             'lon': self.lon
# # # # #         }

# # # # # # Initialize database
# # # # # with app.app_context():
# # # # #     db.create_all()
# # # # #     logger.info("Database initialized")

# # # # # # Form for Adding New Green Zones
# # # # # class AddZoneForm(FlaskForm):
# # # # #     name = StringField('Name', validators=[DataRequired()])
# # # # #     lat = FloatField('Latitude', validators=[DataRequired()])
# # # # #     lon = FloatField('Longitude', validators=[DataRequired()])
# # # # #     submit = SubmitField('Add Zone')

# # # # # # Routes
# # # # # @app.route('/')
# # # # # def home():
# # # # #     return render_template('home.html')

# # # # # @app.route('/about')
# # # # # def about():
# # # # #     return render_template('about.html')

# # # # # @app.route('/services')
# # # # # def services():
# # # # #     return render_template('services.html')

# # # # # @app.route('/contact')
# # # # # def contact():
# # # # #     return render_template('contact.html')

# # # # # @app.route('/map')
# # # # # def map():
# # # # #     return render_template('map.html')

# # # # # @app.route('/add-zone', methods=['GET', 'POST'])
# # # # # def add_zone():
# # # # #     form = AddZoneForm()
# # # # #     if form.validate_on_submit():
# # # # #         try:
# # # # #             new_zone = GreenZone(
# # # # #                 name=form.name.data,
# # # # #                 lat=form.lat.data,
# # # # #                 lon=form.lon.data
# # # # #             )
# # # # #             db.session.add(new_zone)
# # # # #             db.session.commit()
# # # # #             logger.info(f"Added Green Zone: {form.name.data}")
# # # # #             return redirect(url_for('map'))
# # # # #         except Exception as e:
# # # # #             db.session.rollback()
# # # # #             logger.error(f"Error adding zone: {str(e)}")
# # # # #             return "Error adding zone. Please try again."
    
# # # # #     return render_template('add_zone.html', form=form)

# # # # # # API Endpoint
# # # # # @app.route('/api/green-zones', methods=['GET'])
# # # # # def get_green_zones():
# # # # #     try:
# # # # #         zones = GreenZone.query.all()
# # # # #         return jsonify([zone.to_dict() for zone in zones])
# # # # #     except Exception as e:
# # # # #         logger.error(f"Error fetching zones: {str(e)}")
# # # # #         return jsonify({'error': 'Unable to fetch zones'}), 500
    
# # # # #     #read more
# # # # # @app.route('/read-more')
# # # # # def read_more():
# # # # #     return render_template('RA.html')

# # # # # # Error Handlers
# # # # # @app.errorhandler(404)
# # # # # def page_not_found(e):
# # # # #     return render_template('404.html'), 404

# # # # # @app.errorhandler(500)
# # # # # def internal_server_error(e):
# # # # #     return render_template('500.html'), 500

# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True, host='0.0.0.0', port=8080)

# # # # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # # # from flask_sqlalchemy import SQLAlchemy
# # # # from flask_wtf import FlaskForm
# # # # from wtforms import StringField, FloatField, SubmitField
# # # # from wtforms.validators import DataRequired
# # # # import os
# # # # import logging
# # # # import google.generativeai as genai
# # # # from dotenv import load_dotenv

# # # # # 🔹 Load API Key Securely
# # # # load_dotenv()
# # # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # # # 🔹 Initialize Gemini API
# # # # genai.configure(api_key=API_KEY)

# # # # # 🔹 Configure Logging
# # # # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# # # # logger = logging.getLogger(__name__)

# # # # # 🔹 Flask App Configuration
# # # # app = Flask(__name__)
# # # # app.config['SECRET_KEY'] = 'dev-key-123'  # Change in Production
# # # # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # # # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
# # # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # # 🔹 Database Setup
# # # # db = SQLAlchemy(app)

# # # # # ✅ Database Model
# # # # class GreenZone(db.Model):
# # # #     id = db.Column(db.Integer, primary_key=True)
# # # #     name = db.Column(db.String(100), nullable=False)
# # # #     lat = db.Column(db.Float, nullable=False)
# # # #     lon = db.Column(db.Float, nullable=False)

# # # #     def to_dict(self):
# # # #         return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

# # # # # ✅ Ensure Database is Created
# # # # with app.app_context():
# # # #     db.create_all()
# # # #     logger.info("✅ Database Initialized!")

# # # # # ✅ Form for Adding Zones
# # # # class AddZoneForm(FlaskForm):
# # # #     name = StringField("Name", validators=[DataRequired()])
# # # #     lat = FloatField("Latitude", validators=[DataRequired()])
# # # #     lon = FloatField("Longitude", validators=[DataRequired()])
# # # #     submit = SubmitField("Add Zone")

# # # # # ✅ Routes
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("home.html")

# # # # @app.route("/about")
# # # # def about():
# # # #     return render_template("about.html")

# # # # @app.route("/services")
# # # # def services():
# # # #     return render_template("services.html")

# # # # @app.route("/contact")
# # # # def contact():
# # # #     return render_template("contact.html")

# # # # @app.route("/map")
# # # # def map_page():
# # # #     return render_template("map.html")

# # # # # ✅ Add New Green Zone Form
# # # # @app.route("/add-zone", methods=["GET", "POST"])
# # # # def add_zone():
# # # #     form = AddZoneForm()
# # # #     if form.validate_on_submit():
# # # #         try:
# # # #             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
# # # #             db.session.add(new_zone)
# # # #             db.session.commit()
# # # #             logger.info(f"✅ Added Green Zone: {form.name.data}")
# # # #             return redirect(url_for("map_page"))
# # # #         except Exception as e:
# # # #             db.session.rollback()
# # # #             logger.error(f"❌ Error adding zone: {str(e)}")
# # # #             return "Error adding zone. Please try again."

# # # #     return render_template("add_zone.html", form=form)

# # # # # ✅ API Endpoint
# # # # @app.route("/api/green-zones", methods=["GET"])
# # # # def get_green_zones():
# # # #     try:
# # # #         zones = GreenZone.query.all()
# # # #         return jsonify([zone.to_dict() for zone in zones])
# # # #     except Exception as e:
# # # #         logger.error(f"❌ Error fetching zones: {str(e)}")
# # # #         return jsonify({"error": "Unable to fetch zones"}), 500

# # # # # ✅ AI Integration (Example)
# # # # @app.route("/ai-suggest", methods=["POST"])
# # # # def ai_suggest():
# # # #     try:
# # # #         user_input = request.json.get("query", "")
# # # #         model = genai.GenerativeModel("gemini-pro")
# # # #         response = model.generate_content(user_input)
# # # #         return jsonify({"response": response.text})
# # # #     except Exception as e:
# # # #         logger.error(f"❌ AI Suggestion Error: {str(e)}")
# # # #         return jsonify({"error": "AI processing failed"}), 500

# # # # # ✅ Read More Page
# # # # @app.route("/read-more")
# # # # def read_more():
# # # #     return render_template("RA.html")

# # # # # ✅ Custom Error Pages
# # # # @app.errorhandler(404)
# # # # def page_not_found(e):
# # # #     return render_template("404.html"), 404

# # # # @app.errorhandler(500)
# # # # def internal_server_error(e):
# # # #     return render_template("500.html"), 500

# # # # @app.route('/chat')
# # # # def chat():
# # # #     return render_template('chat.html')


# # # # # ✅ Run Flask Server
# # # # if __name__ == "__main__":
# # # #     app.run(debug=True, host="0.0.0.0", port=8080)

# # # from flask import Flask, render_template, request, redirect, url_for, jsonify
# # # from flask_sqlalchemy import SQLAlchemy
# # # from flask_wtf import FlaskForm
# # # from wtforms import StringField, FloatField, SubmitField
# # # from wtforms.validators import DataRequired
# # # import os
# # # import logging
# # # import google.generativeai as genai
# # # from dotenv import load_dotenv

# # # # 🔹 Load API Key Securely
# # # load_dotenv()
# # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # if not API_KEY:
# # #     raise ValueError("❌ GEMINI_API_KEY is missing. Set it in your .env file!")

# # # # 🔹 Initialize Gemini API
# # # genai.configure(api_key=API_KEY)

# # # # 🔹 Configure Logging
# # # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# # # logger = logging.getLogger(__name__)

# # # # 🔹 Flask App Configuration
# # # app = Flask(__name__)
# # # app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "dev-key-123")  # Secure it in production!
# # # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # 🔹 Database Setup
# # # db = SQLAlchemy(app)

# # # # ✅ Database Model
# # # class GreenZone(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     name = db.Column(db.String(100), nullable=False)
# # #     lat = db.Column(db.Float, nullable=False)
# # #     lon = db.Column(db.Float, nullable=False)

# # #     def to_dict(self):
# # #         return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

# # # # ✅ Ensure Database is Created
# # # with app.app_context():
# # #     db.create_all()
# # #     logger.info("✅ Database Initialized!")

# # # # ✅ Form for Adding Zones
# # # class AddZoneForm(FlaskForm):
# # #     name = StringField("Name", validators=[DataRequired()])
# # #     lat = FloatField("Latitude", validators=[DataRequired()])
# # #     lon = FloatField("Longitude", validators=[DataRequired()])
# # #     submit = SubmitField("Add Zone")

# # # # ✅ Routes
# # # @app.route("/")
# # # def home():
# # #     return render_template("home.html")

# # # @app.route("/about")
# # # def about():
# # #     return render_template("about.html")

# # # @app.route("/services")
# # # def services():
# # #     return render_template("services.html")

# # # @app.route("/contact")
# # # def contact():
# # #     return render_template("contact.html")

# # # @app.route("/map")
# # # def map_page():
# # #     return render_template("map.html")

# # # # ✅ Add New Green Zone Form
# # # @app.route("/add-zone", methods=["GET", "POST"])
# # # def add_zone():
# # #     form = AddZoneForm()
# # #     if form.validate_on_submit():
# # #         try:
# # #             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
# # #             db.session.add(new_zone)
# # #             db.session.commit()
# # #             logger.info(f"✅ Added Green Zone: {form.name.data}")
# # #             return redirect(url_for("map_page"))
# # #         except Exception as e:
# # #             db.session.rollback()
# # #             logger.error(f"❌ Error adding zone: {str(e)}")
# # #             return jsonify({"error": "Failed to add zone"}), 500

# # #     return render_template("add_zone.html", form=form)

# # # # ✅ API Endpoint for Green Zones
# # # @app.route("/api/green-zones", methods=["GET"])
# # # def get_green_zones():
# # #     try:
# # #         zones = GreenZone.query.all()
# # #         return jsonify([zone.to_dict() for zone in zones])
# # #     except Exception as e:
# # #         logger.error(f"❌ Error fetching zones: {str(e)}")
# # #         return jsonify({"error": "Unable to fetch zones"}), 500

# # # # ✅ AI-Powered Chatbot Using Gemini API
# # # @app.route("/ai-suggest", methods=["POST"])
# # # def ai_suggest():
# # #     try:
# # #         data = request.json
# # #         user_input = data.get("query", "").strip()

# # #         if not user_input:
# # #             return jsonify({"response": "Please enter a valid query!"}), 400

# # #         model = genai.GenerativeModel("gemini-pro")
# # #         response = model.generate_content(user_input)

# # #         if response.text:
# # #             return jsonify({"response": response.text})
# # #         else:
# # #             return jsonify({"response": "Sorry, I couldn't generate a response. Try again!"}), 500

# # #     except Exception as e:
# # #         logger.error(f"❌ AI Suggestion Error: {str(e)}")
# # #         return jsonify({"response": "AI processing failed. Please try again later."}), 500

# # # # ✅ Read More Page
# # # @app.route("/read-more")
# # # def read_more():
# # #     return render_template("RA.html")

# # # # ✅ Chatbot Page
# # # @app.route('/chat')
# # # def chat():
# # #     return render_template('chat.html')


# # # # ✅ Custom Error Pages
# # # @app.errorhandler(404)
# # # def page_not_found(e):
# # #     return render_template("404.html"), 404

# # # @app.errorhandler(500)
# # # def internal_server_error(e):

# # #     return render_template("500.html"), 500

# # # # ✅ Run Flask Server
# # # if __name__ == "__main__":
# # #     app.run(debug=True, host="0.0.0.0", port=8080)

# # # 523from flask import Flask, render_template, request, redirect, url_for, jsonify
# # # from flask_sqlalchemy import SQLAlchemy
# # # from flask_wtf import FlaskForm
# # # from wtforms import StringField, FloatField, SubmitField
# # # from wtforms.validators import DataRequired
# # # import os
# # # import logging
# # # import google.generativeai as genai
# # # from dotenv import load_dotenv

# # # # 🔹 Load API Key Securely
# # # load_dotenv()
# # # API_KEY = os.getenv("GEMINI_API_KEY")
# # # genai.configure(api_key=API_KEY)

# # # # 🔹 Configure Logging
# # # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# # # logger = logging.getLogger(__name__)

# # # # 🔹 Flask App Configuration
# # # app = Flask(__name__)
# # # app.config['SECRET_KEY'] = 'dev-key-123'  # Change for Production
# # # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # 🔹 Database Setup
# # # db = SQLAlchemy(app)

# # # # ✅ Database Model
# # # class GreenZone(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     name = db.Column(db.String(100), nullable=False)
# # #     lat = db.Column(db.Float, nullable=False)
# # #     lon = db.Column(db.Float, nullable=False)

# # #     def to_dict(self):
# # #         return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

# # # # ✅ Ensure Database is Created
# # # with app.app_context():
# # #     db.create_all()
# # #     logger.info("✅ Database Initialized!")

# # # # ✅ Form for Adding Zones
# # # class AddZoneForm(FlaskForm):
# # #     name = StringField("Name", validators=[DataRequired()])
# # #     lat = FloatField("Latitude", validators=[DataRequired()])
# # #     lon = FloatField("Longitude", validators=[DataRequired()])
# # #     submit = SubmitField("Add Zone")

# # # # ✅ Routes
# # # @app.route("/")
# # # def home():
# # #     return render_template("home.html")

# # # @app.route("/about")
# # # def about():
# # #     return render_template("about.html")

# # # @app.route("/services")
# # # def services():
# # #     return render_template("services.html")

# # # @app.route("/contact")
# # # def contact():
# # #     return render_template("contact.html")

# # # @app.route("/map")
# # # def map_page():
# # #     return render_template("map.html")

# # # # ✅ Add New Green Zone Form
# # # @app.route("/add-zone", methods=["GET", "POST"])
# # # def add_zone():
# # #     form = AddZoneForm()
# # #     if form.validate_on_submit():
# # #         try:
# # #             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
# # #             db.session.add(new_zone)
# # #             db.session.commit()
# # #             logger.info(f"✅ Added Green Zone: {form.name.data}")
# # #             return redirect(url_for("map_page"))
# # #         except Exception as e:
# # #             db.session.rollback()
# # #             logger.error(f"❌ Error adding zone: {str(e)}")
# # #             return "Error adding zone. Please try again."

# # #     return render_template("add_zone.html", form=form)

# # # # ✅ API Endpoint for Green Zones
# # # @app.route("/api/green-zones", methods=["GET"])
# # # def get_green_zones():
# # #     try:
# # #         zones = GreenZone.query.all()
# # #         return jsonify([zone.to_dict() for zone in zones])
# # #     except Exception as e:
# # #         logger.error(f"❌ Error fetching zones: {str(e)}")
# # #         return jsonify({"error": "Unable to fetch zones"}), 500

# # # # ✅ AI Chatbot Route
# # # @app.route("/ai-suggest", methods=["POST"])
# # # def ai_suggest():
# # #     try:
# # #         # Get user input from JSON request
# # #         data = request.get_json()
# # #         user_input = data.get("query", "")

# # #         if not user_input:
# # #             return jsonify({"error": "No query provided"}), 400

# # #         # Initialize AI Model
# # #         model = genai.GenerativeModel("gemini-pro-1.5")
# # #         response = model.generate_content(user_input)

# # #         # Check if response is valid
# # #         if response and hasattr(response, 'text'):
# # #             return jsonify({"response": response.text})
# # #         else:
# # #             return jsonify({"error": "Empty response from AI"}), 500

# # #     except Exception as e:
# # #         logger.error(f"❌ AI Suggestion Error: {str(e)}")
# # #         return jsonify({"error": f"AI processing failed: {str(e)}"}), 500

# # # # ✅ Read More Page
# # # @app.route("/read-more")
# # # def read_more():
# # #     return render_template("RA.html")

# # # # ✅ Custom Error Pages
# # # @app.errorhandler(404)
# # # def page_not_found(e):
# # #     return render_template("404.html"), 404

# # # @app.errorhandler(500)
# # # def internal_server_error(e):
# # #     return render_template("500.html"), 500

# # # # ✅ Chatbot Page
# # # @app.route("/chat", methods=["GET", "POST"])
# # # def chat():
# # #     if request.method == "POST":
# # #         data = request.get_json()
# # #         user_input = data.get("query", "")

# # #         if not user_input:
# # #             return jsonify({"error": "No query provided"}), 400

# # #         model = genai.GenerativeModel("gemini-pro")
# # #         response = model.generate_content(user_input)

# # #         return jsonify({"response": response.text if response and hasattr(response, 'text') else "No response from AI"})

# # #     return render_template("chat.html")  # For GET requests


# # # # ✅ Run Flask Server
# # # if __name__ == "__main__":
# # #     app.run(debug=True, host="0.0.0.0", port=8080)

# # from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_wtf import FlaskForm
# # from wtforms import StringField, FloatField, SubmitField
# # from wtforms.validators import DataRequired
# # import os
# # import logging
# # import time
# # import google.generativeai as genai
# # from dotenv import load_dotenv
# # from flask_cors import CORS

# # # 🔹 Load API Key Securely
# # load_dotenv()
# # API_KEY = os.getenv("GEMINI_API_KEY")
# # if not API_KEY:
# #     raise ValueError("❌ GEMINI_API_KEY is missing. Set it in your .env file!")

# # genai.configure(api_key=API_KEY)

# # # 🔹 Configure Logging
# # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# # logger = logging.getLogger(__name__)

# # # 🔹 Initialize Flask App (Only Once)
# # app = Flask(__name__)
# # CORS(app)  # Enable CORS for all routes

# # # 🔹 Flask App Configuration
# # app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", "dev-key-123")  # Change for Production
# # BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'green_zones.db')}"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # 🔹 Database Setup
# # db = SQLAlchemy(app)

# # # ✅ Database Model
# # class GreenZone(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)
# #     lat = db.Column(db.Float, nullable=False)
# #     lon = db.Column(db.Float, nullable=False)

# #     def to_dict(self):
# #         return {"id": self.id, "name": self.name, "lat": self.lat, "lon": self.lon}

# # # ✅ Ensure Database is Created
# # with app.app_context():
# #     db.create_all()
# #     logger.info("✅ Database Initialized!")

# # # ✅ Form for Adding Zones
# # class AddZoneForm(FlaskForm):
# #     name = StringField("Name", validators=[DataRequired()])
# #     lat = FloatField("Latitude", validators=[DataRequired()])
# #     lon = FloatField("Longitude", validators=[DataRequired()])
# #     submit = SubmitField("Add Zone")

# # # ✅ Routes
# # @app.route("/")
# # def home():
# #     return render_template("home.html")

# # @app.route("/about")
# # def about():
# #     return render_template("about.html")

# # @app.route("/services")
# # def services():
# #     return render_template("services.html")

# # @app.route("/contact")
# # def contact():
# #     return render_template("contact.html")

# # @app.route("/map")
# # def map_page():
# #     return render_template("map.html")

# # # ✅ Add New Green Zone Form
# # @app.route("/add-zone", methods=["GET", "POST"])
# # def add_zone():
# #     form = AddZoneForm()
# #     if form.validate_on_submit():
# #         try:
# #             new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
# #             db.session.add(new_zone)
# #             db.session.commit()
# #             logger.info(f"✅ Added Green Zone: {form.name.data}")
# #             return redirect(url_for("map_page"))
# #         except Exception as e:
# #             db.session.rollback()
# #             logger.error(f"❌ Error adding zone: {str(e)}")
# #             return "Error adding zone. Please try again."
# #     return render_template("add_zone.html", form=form)

# # # ✅ API Endpoint for Green Zones
# # @app.route("/api/green-zones", methods=["GET"])
# # def get_green_zones():
# #     try:
# #         zones = GreenZone.query.all()
# #         return jsonify([zone.to_dict() for zone in zones])
# #     except Exception as e:
# #         logger.error(f"❌ Error fetching zones: {str(e)}")
# #         return jsonify({"error": "Unable to fetch zones"}), 500

# # # ✅ AI-Powered Chatbot Using Gemini API
# # @app.route("/ai-suggest", methods=["POST"])
# # def ai_suggest():
# #     try:
# #         user_input = request.json.get("query", "")
        
# #         if not user_input:
# #             return jsonify({"error": "No input provided"}), 400
        
# #         model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model
# #         response = model.generate_content(user_input)

# #         if response and hasattr(response, 'text') and response.text:
# #             return jsonify({"response": response.text})
# #         else:
# #             return jsonify({"error": "AI did not return a valid response"}), 500

# #     except Exception as e:
# #         logger.error(f"❌ AI Suggestion Error: {str(e)}")
# #         return jsonify({"error": f"AI processing failed: {str(e)}"}), 500

# # # ✅ Chatbot Page
# # @app.route('/chat', methods=['POST'])
# # def chat():
# #     return render_template("chat.html")
# #     try:
# #         data = request.get_json()
# #         prompt = data.get("prompt", "")

# #         if not prompt:
# #             return jsonify({"error": "No prompt provided"}), 400  # Bad Request
        
# #         print(f"Received prompt: {prompt}")  # Debugging

# #         # 🔥 Generate AI Response
# #         model = genai.GenerativeModel("gemini-pro")  
# #         response = model.generate_content(prompt)
        
# #         if response and hasattr(response, 'text') and response.text:
# #             return jsonify({"response": response.text})
# #         else:
# #             return jsonify({"error": "AI response empty"}), 500  # Internal Server Error

# #     except Exception as e:
# #         logger.error(f"❌ Chatbot Error: {str(e)}")
# #         return jsonify({"error": f"Server error: {str(e)}"}), 500

# # # ✅ Read More Page
# # @app.route("/read-more")
# # def read_more():
# #     return render_template("RA.html")

# # # ✅ Custom Error Pages
# # @app.errorhandler(404)
# # def page_not_found(e):
# #     return render_template("404.html"), 404

# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     return render_template("500.html"), 500

# # # ✅ Run Flask Server (Fixed Duplicate Calls)
# # if __name__ == '__main__':
# #     app.run(debug=True, port=8080)
# import express from "express";
# import cors from "cors";
# import dotenv from "dotenv";
# import { GoogleGenAI } from "@google/genai";

# dotenv.config();
# const app = express();
# app.use(cors());  // ✅ Allow frontend requests
# app.use(express.json());  // ✅ Parse JSON request bodies

# const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

# app.post("/chat", async (req, res) => {
#     try {
#         console.log("Received request:", req.body); // Debugging log

#         const { message } = req.body;
#         if (!message) {
#             return res.status(400).json({ reply: "Message is required!" });
#         }

#         const response = await ai.models.generateContent({
#             model: "gemini-2.0-flash",
#             contents: message,
#         });

#         console.log("AI Response:", response); // Debugging log

#         res.json({ reply: response.text || "No response from AI." });
#     } catch (error) {
#         console.error("AI Error:", error); // Log the actual error
#         res.status(500).json({ reply: "Error processing request." });
#     }
# });

# const PORT = process.env.PORT || 5001;
# app.listen(PORT, () => console.log(Server running on http://localhost:${PORT}/chat));