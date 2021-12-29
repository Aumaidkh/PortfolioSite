from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')
# files that need to be sent using templates
# have to be placed in templates folder


# routing every page to its template
@app.route("/<string:page_name>")
def route(page_name):
    return render_template(page_name)


# post routes
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    # receiving information
    if request.method == 'POST':
       #saving data to database
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')

        except :
            return "Didn't save to database"

    else:
        return 'Error submitting form'


# Saving data
def write_to_file(data):
    with open("database.txt", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\nEmail: {email}, Subject: {subject},Message: {message}")


def write_to_csv(data):
    with open("database.csv", mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])




