from flask import Flask, render_template, make_response, redirect, request
import random

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route("/")

def home():

    x = ['https://www.youtube.com/embed/2lm6OEa24Iw', 'https://www.youtube.com/embed/m7lhwK843i8', 'https://www.youtube.com/embed/iJIOi3jrlXY', 'https://www.youtube.com/embed/YlkJrqjXuj4', 'https://www.youtube.com/embed/VnqgtG7ZADI', 'https://www.youtube.com/embed/FMUn8y819lE']
    v = random.choice(x)
    return render_template('home.html', v=v)

@app.route('/sitemap.xml')

def sitemap():
    resp = make_response(render_template('sitemap.xml'))
    resp.headers['Content-type'] = 'text/xml; charset=utf-8'
    return resp

@app.route('/robots.txt')

def robots():
    resp1 = make_response(render_template('robots.txt'))
    resp1.headers['Content-type'] = 'text/txt; charset=utf-8'
    return resp1

@app.route('/style.css')


def style():
    resp1 = make_response(render_template('style.css'))
    resp1.headers['Content-type'] = 'text/css; charset=utf-8'
    return resp1

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
