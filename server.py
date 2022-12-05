from flask import Flask
import random

app = Flask(__name__)

topics = [ 
    {'id': 1, 'title' : 'html', 'body' : 'html is...'},
    {'id': 2, 'title' : 'css', 'body' : 'css is...'},
    {'id': 3, 'title' : 'javascript', 'body' : 'javascript is...'},
]

@app.route('/')
def index():
    liTags = ''

    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    print(liTags)

    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB<a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''
    
@app.route('/create/')
def index2():
    return 'Create 03'

@app.route('/read/<int:id>/')
def read(id):
    liTags = ''

    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    title = ''
    body = ''
    
    for topic in topics:
        if id == topic["id"]:
            title = topic["title"]
            body = topic["body"]
            break

    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB<a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>{title}</h2>
            {body}
        </body>
    </html>
    '''

app.run(port=8080, debug=True)
