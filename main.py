from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def getHome() :
  return render_template('home.html', active_page = 'home')

@app.route('/about')
def getAbout() :
  return render_template('about.html')

@app.route('/contact')
def getContact() :
  return render_template('contact.html', phone = 3556269)

if __name__ == '__main__' :
  app.run(host="0.0.0.0", port = '5000', threaded = True, debug = True)