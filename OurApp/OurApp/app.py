from flask import request
from flask import Flask
from flask import Response
import json

app = Flask(__name__)
app.debug = True
#app.run(debug=True,host="0.0.0.0")
def verify_token(password):
    passw = 'thisisourtoken'
    if password == passw:
        return True
    
    return False

@app.route('/inventory')
def getinventory():
    if not verify_token(request.args.get('token')):
    	return ('token did not matched')
    data = {"message":"Have a great day"}
    data = json.dumps(data)
    resp = Response(response=data,
                    status=200,
                    mimetype="application/json")
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)