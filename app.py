from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle


app=Flask(__name__)#initializing flask app

@app.route("/",methods=["GET"])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def index():
    if request.method == "POST":
        try:
            print("entered")
            gre_score=float(request.form['gre_score'])
            toefl_score=float(request.form['toefl_score'])
            university_rating=float(request.form['university_rating'])
            sop=float(request.form['sop'])
            lor=float(request.form['lor'])
            cgpa=float(request.form['cgpa'])
            is_research=request.form['research']
            if(is_research=='yes'):
                research=1
            else:
                research=0
            filename='admission_prediction_lr_model.pickle'
            scaler_object='scaler_object.pickle'
            loaded_model=pickle.load(open(filename,'rb'))#loading model file from storage
            loaded_scaler=pickle.load(open(scaler_object,'rb'))
            ##predictions using loaded model file
            # prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            transformed_input=loaded_scaler.transform([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            # transformed_input=scaler.transform([gre_score,toefl_score,university_rating,sop,lor,cgpa,research])
            prediction=loaded_model.predict(transformed_input)
            print("prediction is ",prediction)
            #showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print("The exception message is ",e)
            return "something is wrong"
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
            