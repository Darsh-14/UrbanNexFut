from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key

# Database Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'green_zones.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class GreenZone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"GreenZone('{self.name}', {self.lat}, {self.lon})"

# Ensure Database is Created
with app.app_context():
    db.create_all()
    print("✅ Database initialized!")

# Form for Adding New Green Zones
class AddZoneForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lat = FloatField('Latitude', validators=[DataRequired()])
    lon = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Add Zone')

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Map Page
@app.route('/map')
def map():
    return render_template('map.html')

# Add New Green Zone Form
@app.route('/add-zone', methods=['GET', 'POST'])
def add_zone():
    form = AddZoneForm()
    if form.validate_on_submit():
        try:
            new_zone = GreenZone(name=form.name.data, lat=form.lat.data, lon=form.lon.data)
            db.session.add(new_zone)
            db.session.commit()
            logger.info(f"✅ Added Green Zone: {form.name.data} ({form.lat.data}, {form.lon.data})")
            return redirect(url_for('map'))
        except Exception as e:
            db.session.rollback()
            logger.error(f"❌ Error adding zone: {e}")
            return "Error adding zone. Please try again."
    
    return render_template('add_zone.html', form=form)

# API to Fetch Green Zones
@app.route('/green-zones')
def green_zones():
    try:
        zones = GreenZone.query.all()
        data = [{"name": zone.name, "lat": zone.lat, "lon": zone.lon} for zone in zones]
        logger.info("✅ /green-zones API called. Data:", data)
        return jsonify(data)
    except Exception as e:
        logger.error(f"❌ Error fetching green zones: {e}")
        return jsonify({"error": "Failed to fetch green zones"}), 500

# Custom Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
