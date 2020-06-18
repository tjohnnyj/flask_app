from flask import Flask, jsonify, request, url_for, redirect, session, render_template
import pprint as pp
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/')
def index():
  return 'hello! you are on the index'

@app.route('/home', defaults={'name':'yeahdude'})
@app.route('/home/<name>', methods=['GET','POST'])
def home(name):
  session['username'] = name
  return render_template('home.html', name=name, display=None, mylist= [1,2,3,4,5], listofdicts=[{'name':'Trace'}, {'name':'Gomer'}])

@app.route('/json')
def json():
  if 'username' in session: 
    name = session['username']
    return jsonify({'key': 'value', 'listkey': [1,2,3,4,5], 'name':name})
  else:
    return 'no username'
  
  

@app.route('/processjson', methods=['POST'])
def processjson():
  data = request.get_json()
  name = data['name']
  location = data['location']

  randomlist = data['data']

  return jsonify({'result!': 'Success', 'name': name, 'location':location, 'keyinlist':random.choice(randomlist)})

@app.route('/query')
def query():
  name = request.args.get('name')
  location = request.args.get('location')
  return '<h1> hi {}, how is the weather in {}? You are on the query page</h1>'.format(name, location)

#getting form data
@app.route('/theform', methods=['GET','POST'])
def theform():
  if request.method == 'GET':
    return render_template('form.html')

  else:
    name=request.form['name']
    #location = request.form['location']

    #return 'Hello {}. You are from {}. You have submitted for form successfully'.format(name, location)
    return redirect((url_for('home',name=name)))

if __name__ == '__main__':
  app.run()

