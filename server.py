from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)


def save_data(d):
    with open('database.csv', 'a') as db:
        fullname = d['fullname']
        email = d['email']
        subject = d['subject']
        message = d['message']
        csv_writer = csv.writer(db, delimiter=';', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        # csv_writer.writeheader(['fullname', 'email', 'subject', 'message']) # it doesn't work
        csv_writer.writerow([fullname, email, subject, message])
        # db.write(f'\n{fullname};{email};{subject};{message}')


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/<path>")
def page(path):
    return render_template(path)


@app.route("/submit_form", methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_data(data)
        return render_template('thankyou.html')
    else:
        return "Something went wrong. Try again later."
