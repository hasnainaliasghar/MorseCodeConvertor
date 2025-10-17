from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from morse import MorseCode
mor = MorseCode()
app = Flask(__name__)
app.secret_key = "dshfirjflskc"
bootstrap = Bootstrap5(app)

class Enteries(FlaskForm):
    text = StringField("Morse Code", validators=[DataRequired()])
    submit = SubmitField("Convert")

@app.route('/',methods = ["POST","GET"])
def home():
    form = Enteries()
    if form.validate_on_submit():
        morse_text = form.text.data
        if morse_text[0] in [".", "-", "_"]:
            code = mor.decrypt(morse_text)
        else:
            code = mor.encrypt(morse_text)

        # Redirect after POST to clear form
        return redirect(url_for("home", result=code))

    # Get 'result' from URL query string (after redirect)
    result = request.args.get("result")
    return render_template("index.html", form=form, result=result)

if __name__ == "__main__":
    app.run(debug=True,port=5001)