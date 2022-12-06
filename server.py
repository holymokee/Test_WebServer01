from flask import Flask, request, redirect
import random

app = Flask(__name__)

nextID = 4
topics = [ 
    {'id': 1, 'title' : 'html', 'body' : 'html is...'},
    {'id': 2, 'title' : 'css', 'body' : 'css is...'},
    {'id': 3, 'title' : 'javascript', 'body' : 'javascript is...'},
]

def SetHtml(contents, context, id = None):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB<a></h1>
            <ol>
                {contents}
            </ol>
            {context}
            <ul>
                <li><a href="/create/">Create</a></li>
            </ul>    
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
    
@app.route('/create/', methods = ['GET', 'POST'])
def index2():
    global nextID

    if request.method == 'GET':
        content = '''
            <form action="/create/" method = "POST">
                <p><input type = "text" name = "title" placeholder = "title"></p>
                <p><textarea name = "body" placeholder = "body"></textarea></p>
                <p><input type = "submit" value="create"></P>
                <p><input type = "submit" value="update"></P>
            </form>
        '''
        return SetHtml(GetTags(), content)

    elif request.method == 'POST':     
        title = request.form['title']
        body = request.form['body']

        newTopic = {'id' : nextID , 'title' : title, 'body' : body}
        url = '/read/' + str(nextID) + '/'
        nextID += 1

        topics.append(newTopic)

        return redirect(url)


@app.route('/read/<int:id>/')
def read(id):

    body = ''
    
    for topic in topics:
        if id == topic["id"]:
            title = topic["title"]
            body = topic["body"]
            break

    return SetHtml(GetTags(), f'<h2>{title}</h2>{body}', id)

app.run(debug=True)
