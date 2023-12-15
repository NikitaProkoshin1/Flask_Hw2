from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'a036d0d6a76c0e1522467f9cc1681db0a5472bd1c30832d1af4b71f3816d8f84' 


@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/loginit/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()