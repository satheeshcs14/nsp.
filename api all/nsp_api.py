from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify,request

from werkzeug.security import  generate_password_hash,check_password_hash





app= Flask(__name__)


app.secret_key="secretkey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/nsp"

source = PyMongo(app)


@app.route('/fresh',methods =['POST'])
def fresh():
    _json =request.json
    _state_of_Domicile =_json['domicile']
    _Name_of_student = _json['student']
    _Data_of_Birth = _json['birth']
    _mobile_number = _json['mobile']
    _bank_ifsc = _json['ifsc']
    _bank_A_c_no = _json['bank']
    _identification_details =_json['details']
    _scholorship_category =_json['category']
    _scheme_type = _json['scheme']
    _Gender = _json['gender']
    _Email_id =_json['email']


    
    if  _state_of_Domicile and _Name_of_student and _Data_of_Birth and _mobile_number and _bank_ifsc and _bank_A_c_no and _identification_details and _scholorship_category and _scheme_type and _Gender and _Email_id and  request.method =='POST':
        
        
        id= source.db.fresh_registration.insert_one({'domicile':_state_of_Domicile,
                                                      'student':_Name_of_student,
                                                      'birth':_Data_of_Birth,
                                                      'mobile':_mobile_number,
                                                       'ifsc':_bank_ifsc,
                                                       'bank':_bank_A_c_no,
                                                       'details':_identification_details,
                                                       'category':_scholorship_category,
                                                       'scheme':_scheme_type,
                                                       'gender':_Gender,
                                                       'email':_Email_id})
        
        resp = jsonify("User data add  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    

    
    
    
    
    
     

@app.route('/institute',methods =['POST'])
def nodal():
    _json =request.json
    nodal_officer=_json['nodal']
    Academic_year =_json['Academic_year']
    User_id =_json['user']
    password =_json['pwd']
    
    
     
    if nodal_officer and Academic_year and User_id and password and  request.method =='POST':
        _hashed_password = generate_password_hash(password)
        
        id = source.db.Institude_login.insert_one({'nodal':nodal_officer,'Academic_year':Academic_year, 'user':User_id ,'pwd':_hashed_password })
        
        resp = jsonify("User add  the institude login successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
    
        
    
    

@app.route('/district',methods =['POST'])
def district():
    _json =request.json
    _state =_json['state']
    _District = _json['district']
    


    if  _state and _District and  request.method =='POST':
        
        
        
        id= source.db.District_login.insert_one({'state':_state,
                                                    'district':_District})
        resp = jsonify(" submit  successfully")
        
        resp._status_code = 200
        
        return resp
        
    else:
        return not_found()
      
    
    
    
 
  

@app.route('/loginF',methods =['POST'])
def loginF():
    _json =request.json
    _application_id =_json['A_id']
    _password = _json['pwd']
    


    if  _application_id and _password and  request.method =='POST':
        _hashed_password = generate_password_hash(_password)
        
        
        id= source.db.login_fresh.insert_one({'A_id':_application_id,
                                                    'pwd':_hashed_password})
        resp = jsonify(" User is login successfully")
        
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



