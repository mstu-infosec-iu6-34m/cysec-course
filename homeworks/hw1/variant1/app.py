from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heart_type = db.Column(db.String(50))
    quantity = db.Column(db.Integer)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

# Ensure the database is created within the application context
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        heart_type = request.form['heart_type']
        quantity = request.form['quantity']
        new_order = Order(heart_type=heart_type, quantity=int(quantity))
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('index'))

    hearts = ["❤️", "💚", "💙", "🧡", "💛", "💜", "🖤", "🤍", "🤎", "🔥❤️", "🎀❤️", "⭐❤️"]
    reviews = Review.query.all()
    return render_template('index.html', hearts=hearts, reviews=reviews)

@app.route('/review', methods=['POST'])
def add_review():
    content = request.form['review']
    new_review = Review(content=content)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8888, debug=True)
