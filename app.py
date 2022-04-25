
from flask import Flask, make_response, redirect, render_template, request, url_for, jsonify, abort
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = '<24F6991FCF76C>'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    
    resp = make_response(render_template('page.html'))
    resp.set_cookie('username', 'lakhdar')
    return resp

@app.route('/about/<name>')
def about(name=None):
    
    print(request.cookies.get('username'))

    if name == 'noprocess':

        abort(401)

    return render_template('about.html', name=name)

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        code = request.json['code']
        country = request.json['country']

        return jsonify(
            name= 'lakhdar',
            post='developer',
            age = 28, 
            company = 'ssss'
        )

    else:

        return '<h1>contact test get </h1>'

@app.route('/page')
def page():

    return '<h1>Page </h1>'


@app.route('/repage')
def repage():

    return redirect(url_for('page'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == "__main__":
    app.run()