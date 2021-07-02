from flask import Flask, render_template, request, flash
from password_generator import pass_gen
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.secret_key = str(pass_gen(100))  # generated secret key by using the same function
run_with_ngrok(app)


@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        return render_template('error.html',
                               error=e)


@app.route('/pwd_gen', methods=['POST'])
def pwd_gen():
    if request.method == 'POST':
        formdata = request.form.to_dict()
        if int(formdata['pwd_length']) > 7:
            final_pwd = pass_gen(int(formdata['pwd_length']))
            return render_template('home.html', pwd_generated=final_pwd)
        else:
            flash(f'Password length is too short to generate strong password Please have at least 8 characters'
                  f' you had entered {formdata["pwd_length"]}')
            return render_template('home.html')
    else:
        return render_template('error.html',
                               error='Method is not allowed')


if __name__ == '__main__':
    app.run()
