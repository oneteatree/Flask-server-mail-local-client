


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('tmp.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
    user = request.form['nm']
   
   resp = make_response('set')
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)