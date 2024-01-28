import csv

from flask import Flask, render_template, url_for,request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv",newline="", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
##@app.route('/')
##def hello_world(username = None, post_id = None):
##    return render_template("index.html", name = username, post_id = post_id)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "Something went wrong"


##@app.route('/contact.html')
##def contact():
##    return render_template("contact.html")


##@app.route('/favicon.ico')
##def blog():
##    return 'These are thoughts on blogs'

#@app.route('/blog/2020/dogs')
#def blog2():
#    return 'This is my page number 2'