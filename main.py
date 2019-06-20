# A simple Flast application to calculate and deduct expenses from income.

from flask import Flask, jsonify, request, json, redirect, render_template
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from models.models import Income, Expense, db
from app import create_app

app = create_app()
CORS(app, support_credentials=True)
cors = CORS(app, resources={r"/addincome": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

#Adding to Income Table
@app.route('/add_income', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def add_income():

    if request.method == 'POST':
        data = request.get_json()
        inc = data['inc']
        amt = data['amt']
        
        if inc and amt:
            print('added!')
            db.session.add(Income(description= inc, amount= amt))
            db.session.commit()
            return jsonify({inc:amt})
        
    return redirect('/')

#Adding to Expense Table    
@app.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        data = request.get_json()
        exp = data['exp']
        amt = data['amt']
        if exp and amt:
            db.session.add(Expense(exp_description = exp, exp_amount= amt))
            db.session.commit()
            return jsonify({exp:amt})

    return redirect('/')

#Deleting from Expense Table
@app.route('/delete_income', methods=['DELETE']) 
def delete_income():
    if request.method == 'DELETE':
        data = request.get_json()
        key = data['key']
        print("delete", key)
        if key:
            obj = db.session.query(Income).get(key)
            db.session.delete(obj)
            db.session.commit()
            return jsonify({'Action': 'Deleted!'})
    return jsonify({"Error": "Wrong method"})

@app.route('/delete_expense', methods=['DELETE']) 
def delete_expense():
    if request.method == 'DELETE':
        data = request.get_json()
        key = data['key']
        print("delete", key)
        if key:
            obj = db.session.query(Expense).get(key)
            db.session.delete(obj)
            db.session.commit()
            return jsonify({'Action': 'Deleted!'})
    return jsonify({"Error": "Wrong method"})

#Getting savings and results from both tables    
@app.route('/get_result', methods=['GET'])
def get_result():
    inc = []
    exp = []
#List of dics
    inc_list = []
    exp_list = []
#Query objects
    income = Income.query.all()
    expense = Expense.query.all()
    
    for i in income:
        inc.append(i.amount)
        dic={i.id: {i.description:i.amount}}
        inc_list.append(dic)
    
    for e in expense:
        exp.append(e.exp_amount)
        dic = {e.id: {e.exp_description:e.exp_amount}}
        exp_list.append(dic)
    
    total_inc = sum(inc)
    total_exp = sum(exp)
    
    saving = total_inc - total_exp
    print(saving)

    return jsonify({"saving":saving, "income":inc_list, "expense":exp_list})

#index route
@app.route('/', methods=['GET'])
def index():
    
    return render_template("index.html")

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8000, debug=True)