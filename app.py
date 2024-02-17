from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database'

mysql = MySQL(app)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            # Assuming your front-end sends data as JSON
            data = request.get_json()

            # Get username and password from the request
            username = data.get('username')
            password = data.get('password')

            # Query the database for the user
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            cur.close()

            if user and user['password'] == password:
                # Successful login
                return jsonify({"message": "Login successful"})
            else:
                # Invalid credentials
                return jsonify({"message": "Invalid credentials"}), 401

        except Exception as e:
            return jsonify({"message": "Error: {}".format(str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
