from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()


# ===============================
# History Table Model
# ===============================
class History(db.Model):

    # Unique ID for each record
    id = db.Column(db.Integer, primary_key=True)

    # User's prompt input
    prompt = db.Column(db.Text, nullable=False)

    # Selected programming language
    language = db.Column(db.String(50), nullable=False)

    # AI-generated code output
    generated_code = db.Column(db.Text, nullable=False)

    # Timestamp of generation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    # Optional: better debug representation
    def __repr__(self):
        return f"<History {self.id} | {self.language}>"