from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__,static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True)