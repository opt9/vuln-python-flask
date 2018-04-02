from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)
#app.debug = True

@app.route('/hello')
def hello_world():
    user = {'username':"world", 'secret':"dG9wIHNlY3JldA=="}
    if request.args.get('username'):
        user['username'] = request.args.get('username')
    template = '''<h2>Hi %s!</h2>''' % user['username']
    return render_template_string(template, user=user)


@app.errorhandler(404)
def not_found_error(error):
    template = '''{%% extends "layout.html" %%}
{%% block content %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template), 404


@app.errorhandler(500)
def internal_error(error):
    template = '''{%% extends "layout.html" %%}
{%% block content %%}
    <div class="center-content error">
        <h1>Oops! Something wrong!</h1>
        <h3>%s</h3>
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template), 500
