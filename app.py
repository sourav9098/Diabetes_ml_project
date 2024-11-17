from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  if request.method == "POST" :

     FS = int(request.form["FS"])
     FU = int(request.form["FU"])  
     with open('my_model','rb') as f:
         model=pickle.load(f)    
     result = model.predict([[FS,FU]])
     if result[0] == "NO":
       return render_template('index.html',data=["Congratulations,You do not have diabetes.","green"])  
     else:
        return render_template('index.html',data=["Sorry Diabetes Detected..Please Consult With a Doctor."," red"])    


if __name__ == "__main__":
    app.run(debug=True)