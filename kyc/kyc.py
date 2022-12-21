
from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request






app= Flask(__name__)

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

monq = PyMongo(app)


@app.route('/kyc',methods =['POST'])
def district():
    _json =request.json
    _code =_json['code']
    


    if  _code and   request.method =='POST':
        
        
        id= monq.db.kyc_login.insert_one({'code':_code})
   
   
   
   
  
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()



@app.route('/kyc_get_data')
def d1():
        d1 = monq.db.kyc_login.find()
        resp =dumps(d1)
        return resp



@app.route("/kyc_one_data/<id>")
def d2():
    user = monq.db.kyc_login.find({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp



@app.route("/delete/<id>",methods =['DELETE'])
def delete(id):
    monq.db.kyc_login.delete_one({'_id':ObjectId(id)})
    resp =jsonify("user deleted successfully")

    resp.status_code = 200

    return resp






@app.route('/update/<id>',methods =['PUT'])
def update(id):
    _id =id
    _json =request.json
    _code =_json['code']
    


    if  _code and   request.method =='POST':
        
        
        id= monq.db.kyc_login.insert_one({'_id': ObjectId (_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                                                {'$set':{'code':_code}})

        resp = jsonify("user updataed the data")

        resp.status_code =200

        return resp

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







