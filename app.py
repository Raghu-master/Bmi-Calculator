from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for('bmi_form'))

@app.route("/yourbmi", methods=['GET', 'POST'])
def bmi_form():
    bmi = None
    type = None

    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        feet = float(request.form.get('feet'))
        inches = float(request.form.get('inches'))
        height = (feet * 0.3048) + (inches * 0.0254)

        bmi = weight / (height ** 2)
        bmi = round(bmi,1)

        if bmi < 18.5:
            type = "Underweight"
        elif bmi < 25:
            type=  "Normal"
        elif bmi < 30:
            type=  "Overweight"
        elif bmi < 35:
            type=  "Obese Class I"
        elif bmi < 40:
                type=  "Obese Class II"
        else:
            type= "Obese Class III"
            

    return render_template('form.html', result=bmi, catagory = type)

if __name__ == "__main__":
    app.run(debug=True)
