from flask import Flask,jsonify,request
from SubActive import status
  
app =   Flask(__name__)
  
@app.route('/', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = status()
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)
