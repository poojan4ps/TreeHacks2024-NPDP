from flask import Flask, request, jsonify, render_template,redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "super secret key"

# PostgreSQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@tree-hacks-ehr-data.cn8kq2284drd.us-east-1.rds.amazonaws.com/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50),unique=True, nullable=False)
    
class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(50),unique=True, nullable=False)
    medical_history = db.Column(db.String(1000), nullable=False)
    current_problem = db.Column(db.String(1000), nullable=False)

class EhrSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session and redirect to the home page
    return redirect(url_for('index'))

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/hospital_dashboard')
def hospital_dashboard():  # Change the function name
    return render_template('hospital_dashboard.html')


@app.route('/login', methods=['POST'])
def login_post():
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
                session['user_id'] = user.id
                if user.user_type == 'user':
                    response = {'message': 'Login successful', 'redirect': url_for('user_dashboard')}
                    return jsonify(response), 200
                elif user.user_type == 'hospital':
                    response = {'message': 'Login successful', 'redirect': url_for('hospital_dashboard')}
                    return jsonify(response), 200

            else:
                # Invalid credentials
                response = {'message': 'Invalid credentials'}
                return jsonify(response), 401

        except Exception as e:
            response = {'message': 'Error: {}'.format(str(e))}
            return jsonify(response), 500
        
@app.route('/get_appointments')
def get_appointments():
    # Assuming you have an Appointments model and relevant fields
    appointments = Appointments.query.all()

    # Convert appointments to a list of dictionaries
    appointment_list = [
        {
            'patient_id': appointment.patient_id,
            'medical_history': appointment.medical_history,
            'current_problem': appointment.current_problem
        }
        for appointment in appointments
    ]

    return jsonify(appointment_list)

@app.route('/remove_appointment/<string:patient_id>', methods=['DELETE'])
def remove_appointment(patient_id):
    try:
        # Query the database for the appointment with the given patient_id
        appointment = Appointments.query.filter_by(patient_id=patient_id).first()

        if appointment:
            # Remove the appointment from the database
            db.session.delete(appointment)
            db.session.commit()

            response = {'success': True, 'message': 'Appointment removed successfully'}
            return jsonify(response), 200
        else:
            response = {'success': False, 'message': 'Appointment not found'}
            return jsonify(response), 404

    except Exception as e:
        response = {'success': False, 'message': 'Error: {}'.format(str(e))}
        return jsonify(response), 500

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    try:
        # Assuming you're passing user_id in the request
        user_id = request.json.get('user_id')

        # Fetch the user from the database
        user = User.query.filter_by(user_id= user_id).first()

        if user:
            # Assuming you have a way to get patient_id associated with the user (replace with your logic)
            
            # Fetch the EhrSummary based on the patient_id
            ehr_summary = EhrSummary.query.filter_by(patient_id=user_id).first()

            if ehr_summary:
                # Create a new appointment
                appointment = Appointments(patient_id=user_id, medical_history=ehr_summary.summary)

                # Add and commit to the database
                db.session.add(appointment)
                db.session.commit()

                print('Appointment booked successfully!')
                return jsonify({'success': True, 'message': 'Appointment booked successfully!'})
            else:
                print('No EhrSummary found for the user.')
                return jsonify({'success': False, 'message': 'No EhrSummary found for the user.'})
        else:
            print('User not found.')
            return jsonify({'success': False, 'message': 'User not found.'})

    except Exception as e:
        print('Error:', str(e))
        return jsonify({'success': False, 'message': str(e)})

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    if request.method == 'POST':
        try:
            # Assuming your front-end sends data as JSON
            data = request.get_json()

            # Get username and password from the request
            username = data.get('username')
            password = data.get('password')

            # Query the database for the user
            user = User.query.filter_by(username=username).first()

            if user and user.username == username:
                # Invalid signup
                return jsonify({"message": "User already exists!"}), 401
            else:
                # Valid Signup
                new_user = User(username=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                return jsonify({"message": "Signup successful!"})

        except Exception as e:
            return jsonify({"message": "Error: {}".format(str(e))}, 500)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

