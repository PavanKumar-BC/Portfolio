from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "change-this-secret")

# Replace these project placeholders later with your real projects
PROJECTS = [
    {
        "title": "Project Alpha",
        "desc": "Short description: what it does, your role, and notable tech.",
        "tech": "Flask • PostgreSQL • Docker",
        "thumb": "/static/images/project1.png",
        "link": "#"
    },
    {
        "title": "Project Beta",
        "desc": "Short description: features and impact.",
        "tech": "React • Spring Boot",
        "thumb": "/static/images/project2.png",
        "link": "#"
    },
    {
        "title": "Project Gamma",
        "desc": "Short description: demo or link to repo.",
        "tech": "Java • Spring Boot",
        "thumb": "/static/images/project3.png",
        "link": "#"
    }
]

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Basic server-side validation
        if not name or not email or not message:
            flash("Please fill all fields.", "danger")
            return redirect(url_for('contact'))

        # Save contact to a simple file (you can replace with DB or email later)
        os.makedirs('contacts', exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        filename = f"contacts/contact_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage:\n{message}\n\n---\n")

        flash("Thanks — your message was received. I'll get back to you soon!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
