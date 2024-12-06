from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Simulated database for users (username: {password, email})
users_db = {}


@app.route('/')
def home():
    # Redirect to login page by default
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists and password matches
        if username in users_db and users_db[username]['password'] == password:
            # Set session variable
            session['username'] = username
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Ensure user doesn't already exist
        if username in users_db:
            return render_template('register.html', error="User already exists")
        
        # Register new user
        users_db[username] = {"email": email, "password": password}
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/logout')
def logout():
    # Clear session data
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/main', methods=['GET', 'POST'])
def main():
    # Ensure only logged-in users can access this route
    if 'username' not in session:
        return redirect(url_for('login'))

    # Handle user input from the form
    output = None
    if request.method == 'POST':
        user_name = request.form['user_name']
        target_name = request.form['target_name']
        output = f"Processed Input: {user_name} & {target_name}"

    return render_template('main.html', username=session['username'], output=output)


if __name__ == '__main__':
    app.run(debug=True)
