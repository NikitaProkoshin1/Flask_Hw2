from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = 'fc12c7bde0b466cc42ee768df600398ab90d92fca47fe234949e75f6dd9fc0b1'



@app.route('/flashh/', methods=['GET', 'POST'])
def flashh():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flashh'))
    return render_template('flashh.html')

if __name__ == '__main__':
    app.run()