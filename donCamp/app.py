from flask import Flask, render_template
import razorpay


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/donate')
def donate():
    return render_template('donate.html')


if __name__ == "__main__":
    app.run(debug=True)
