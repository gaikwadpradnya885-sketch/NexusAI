from app.database import SessionLocal
from app.models.user import User

db = SessionLocal()

admin = User(
    email="admin@nexusai.com",
    password="admin123"
)

db.add(admin)
db.commit()

print("Admin created successfully!")