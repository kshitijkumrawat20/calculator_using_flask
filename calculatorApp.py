from flask import Flask
from flask import request, render_template, jsonify 
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home_page():
    return render_template('index.html ')

@app.route('/math', methods =['POST'])
def math_operations():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = None
        
        if(ops == 'add'):
            r = num1+num2
            result = 'The sum of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'subtract'):
            r = num1-num2
            result = 'The subtract of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'multiply'): 
            r = num1*num2
            result = 'The multiply of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'divide'):
            r = num1/num2
            result = 'The divide of ' + str(num1) + ' and ' + str(num2) + ' is ' +str(r)
        return render_template('result.html',result = result)
    
#testing through postman    
@app.route('/post_man', methods =['POST'])
def math_operations1():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = None
        
        if(ops == 'add'):
            r = num1+num2
            result = 'The sum of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'subtract'):
            r = num1-num2
            result = 'The subtract of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'multiply'): 
            r = num1*num2
            result = 'The multiply of ' + str(num1) + ' and ' +str(num2) + ' is ' +str(r)
        if(ops == 'divide'):
            r = num1/num2
            result = 'The divide of ' + str(num1) + ' and ' + str(num2) + ' is ' +str(r)
        return jsonify(result)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")  