from flask import Flask, render_template

app = Flask(__name__)

# Main app route
@app.route("/")
def index():
	return render_template('index.html');
