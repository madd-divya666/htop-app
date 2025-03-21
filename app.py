from flask import Flask
import os
import datetime
import subprocess
import getpass 

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask htop App</h1><p>Go to <a href='/htop'>/htop</a> to see system info.</p>"

@app.route('/htop')
def htop():
    
    full_name = "Divya Maddheshia"  
    username = getpass.getuser()  
   
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')

    
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True, text=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error fetching 'top' output: {e}"

    
    response = f"""
    <h2>Name: {full_name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {ist_time_str}</h3>
    <h3>TOP output:</h3>
    <pre>{top_output}</pre>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
