from app import db, GreenZone, app

with app.app_context():
    new_zone1 = GreenZone(name="Eco Park", lat=28.6139, lon=77.2090)
    new_zone2 = GreenZone(name="Green Garden", lat=28.6456, lon=77.2153)

    db.session.add(new_zone1)
    db.session.add(new_zone2)
    db.session.commit()

    print("✅ Data inserted successfully!")
