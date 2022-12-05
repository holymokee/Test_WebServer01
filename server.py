from flask import Flask
import random

app = Flask(__name__)

topics = [ 
    {'id': 1, 'title' : 'html', 'body' : 'html is...'},
    {'id': 2, 'title' : 'css', 'body' : 'css is...'},
    {'id': 3, 'title' : 'javascript', 'body' : 'javascript is...'},
]

def SetHtml(contents, context):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB<a></h1>
            <ol>
                {contents}
            </ol>
            {context}
        </body>
    </html>
    '''

def GetTags():
    liTags = ''

    for topic in topics:
        liTags += f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return liTags

@app.route('/')
def index():

    return SetHtml(GetTags(), f'<h2>Welcome</h2>Hello, Web')
    
@app.route('/create/')
def index2():
    return 'Create 03'

@app.route('/read/<int:id>/')
def read(id):

    title = ''
    body = ''
    
    for topic in topics:
        if id == topic["id"]:
            title = topic["title"]
            body = topic["body"]
            break

    return SetHtml(GetTags(), f'<h2>{title}</h2>{body}')

app.run(debug=True)
