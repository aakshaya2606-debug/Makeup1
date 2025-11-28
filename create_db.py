# create_db.py
from app import app, db
from models import Product

def seed():
    sample = [
        {"name":"Blue Heaven Hyper Matte Foundation (SPF 25, 30ml)", "price":299, "company":"Blue Heaven", "category":"Foundation", "use":"Face", "stock":10},
        {"name":"Blue Heaven Long-Lasting Makeup Fixer (60ml)", "price":199, "company":"Blue Heaven", "category":"Setting", "use":"Face", "stock":15},
        {"name":"Rare Beauty Find Comfort Hair & Body Mist", "price":899, "company":"Rare Beauty", "category":"Fragrance", "use":"Hair/Body", "stock":8},
        {"name":"Chanel Coco Mademoiselle Hair Perfume", "price":2500, "company":"Chanel", "category":"Fragrance", "use":"Hair", "stock":5},
        {"name":"Brillare Love Ceramide Hair Perfume", "price":699, "company":"Brillare", "category":"Fragrance", "use":"Hair", "stock":12},
        {"name":"Sol de Janeiro Cheirosa ’76 Hair & Body Mist (90 ml)", "price":1499, "company":"Sol de Janeiro", "category":"Fragrance", "use":"Hair/Body", "stock":7},
    ]

    for p in sample:
        exists = db.session.query(Product).filter_by(name=p["name"]).first()
        if not exists:
            prod = Product(
                name=p["name"],
                price=p["price"],
                company=p["company"],
                category=p["category"],
                use=p["use"],
                stock=p["stock"]
            )
            db.session.add(prod)
    db.session.commit()
    print("Seeded sample products.")

if __name__ == "__main__":
    with app.app_context():
        print("Creating tables (if needed) and DB file...")
        db.create_all()
        seed()
        print("Done. DB path should be in project folder as makeup.db")
