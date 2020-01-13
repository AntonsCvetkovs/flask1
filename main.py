from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def getHome() :
  return render_template('home.html')

@app.route('/about')
def getSayMyName() :
  return render_template('about.html')

@app.route('/contact')
def getContact() :
  return render_template('contact.html', phone = 3556269)

app.run(host = '0.0.0.0', port = 8020)