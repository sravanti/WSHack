from flask import Flask, render_template, request, url_for
import degrees
import jinja2
import webapp2
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/path/', methods=['POST'])
def process():
    user1=request.form['user1']
    user2=request.form['user2']
    return render_template('index.html', users = users_info(find_shortest_path(graph, user1, user2, [])))

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
