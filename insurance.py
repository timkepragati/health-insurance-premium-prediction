from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("insurance_premium_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods=["POST"])
def fun2():
    try:
        name = request.form["name"]
        age = int(request.form["age"])
        gender = request.form["gender"]
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = request.form["smoker"]
        region = int(request.form["region"])

        gender = 1 if gender == "female" else 0
        smoker = 1 if smoker == "yes" else 0

        prediction = model.predict([[age, gender, bmi, children, smoker, region]])

        return f"Predicted Premium for {name}: {prediction[0]:.2f}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
if __name__ == "__main__":
    #app.run(debug=True)
     app.run(host='0.0.0.0', port=8080)
    
