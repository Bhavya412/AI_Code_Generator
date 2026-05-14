import os

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from groq import Groq
from dotenv import load_dotenv

from models.history_model import db, History

load_dotenv()

app = Flask(__name__)

# SIMPLE FIX (no env secret key)
app.secret_key = "ai_code_generator_fixed_key"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# GROQ ONLY
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


def generate_code(prompt, language):

    full_prompt = f"""
You are an expert {language} programmer.

Generate professional optimized {language} code.

Rules:
- Add comments inside code
- Return ONLY code
- No explanations outside code
- Follow best practices

Task:
{prompt}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0.4,
            max_tokens=2048
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():

    generated_code = None

    if request.method == "POST":

        prompt = request.form.get("prompt")
        language = request.form.get("language")

        if not prompt:
            flash("Prompt cannot be empty", "danger")
            return redirect(url_for("home"))

        generated_code = generate_code(prompt, language)

        history = History(
            prompt=prompt,
            language=language,
            generated_code=generated_code
        )

        db.session.add(history)
        db.session.commit()

        flash("Code generated successfully", "success")

    all_history = History.query.order_by(History.created_at.desc()).all()

    return render_template(
        "index.html",
        generated_code=generated_code,
        history=all_history
    )


@app.route("/delete/<int:id>")
def delete(id):
    item = History.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()

    flash("History deleted", "warning")
    return redirect(url_for("home"))


@app.route("/clear")
def clear_history():
    History.query.delete()
    db.session.commit()

    flash("All history cleared", "danger")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )