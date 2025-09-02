from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello {user_input}, Welcome to this app for Docker demonstration. Please consider like and subscribe to the channel."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



# host="0.0.0.0"
# Makes your app available on all network interfaces (not just your computer).
# Useful when you run inside Docker, VM, or want others on your Wi-Fi to access your app.
# If you keep it as 127.0.0.1 (or localhost), then only your machine can access it.

# port=5000
# This is the port number. You can set it to anything free (e.g., 8000, 8080, etc.).
# Default Flask port is 5000, but you can change it if needed.

# host = where it listens (your machine only, or all network devices)
# port = which “door” it listens on (number after : in the URL)