from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age > 0 and age < 100:

           return render_template('age_result.html', age=age, name=name.capitalize())
        else:
            return render_template('age_error.html', age=age)
    return render_template('age.html')

@app.route('/name/')
def name_page():
    name_ = 'Ivan'
    return render_template('greetings.html', name=name_)


if __name__ == '__main__':
    app.run()