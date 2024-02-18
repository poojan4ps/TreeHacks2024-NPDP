from flask import Flask, request, jsonify, render_template,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@tree-hacks-ehr-data.cn8kq2284drd.us-east-1.rds.amazonaws.com/ehr_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            # Assuming your front-end sends data as JSON
            data = request.get_json()

            # Print received data for debugging
            print("Received data:", data)

            # Get username and password from the request
            username = data.get('username')
            password = data.get('password')

            # Query the database for the user
            user = User.query.filter_by(username=username).first()

            if user and user.password == password:
                # Successful login
                response = {'message': 'Login successful', 'redirect': url_for('user_dashboard')}
                return jsonify(response), 200
            else:
                # Invalid credentials
                response = {'message': 'Invalid credentials'}
                return jsonify(response), 401

        except Exception as e:
            response = {'message': 'Error: {}'.format(str(e))}
            return jsonify(response), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

