from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request




app= Flask(__name__)




app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

monq = PyMongo(app)


@app.route('/district',methods =['POST'])
def district():
    _json =request.json
    _state =_json['state']
    _District = _json['district']
    


    if  _state and _District and  request.method =='POST':
        
        
        id= monq.db.District_login.insert_one({'state':_state,
                                                    'district':_District})
   
   
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
  
    

@app.errorhandler(404)
def not_found(error =None):
    message ={
        'status':404,
        'message':"not found" + request.url
        
    }
    resp =jsonify(message)
    
    resp.status_code=404
    
    return resp
    
    

if __name__=="__main__":
    app.run(host='0.0.0.0')                                       
