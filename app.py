# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Study
import logging

app = Flask(__name__)

# Configure the database URI (Change this as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:localhost:/study_db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

# Initialize the database
db.init_app(app)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

with app.app_context():
    db.create_all()  # Create database tables

@app.route('/')
def index():
    studies = Study.query.all()
    return render_template('index.html', studies=studies)

@app.route('/add_study', methods=['GET', 'POST'])
def add_study():
    if request.method == 'POST':
        new_study = Study(
            name=request.form['name'],
            description=request.form['description'],
            phase=request.form['phase'],
            sponsor_name=request.form['sponsor_name']
        )
        db.session.add(new_study)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_study.html')

@app.route('/update_study/<int:id>', methods=['GET', 'POST'])
def update_study(id):
    study = Study.query.get_or_404(id)
    if request.method == 'POST':
        study.name = request.form['name']
        study.description = request.form['description']
        study.phase = request.form['phase']
        study.sponsor_name = request.form['sponsor_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_study.html', study=study)

@app.route('/delete_study/<int:id>', methods=['GET'])
def delete_study(id):
    study = Study.query.get_or_404(id)
    db.session.delete(study)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
