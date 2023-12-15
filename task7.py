from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square_result.html', data=data)
    return render_template('square.html')

if __name__ == '__main__':
    app.run()