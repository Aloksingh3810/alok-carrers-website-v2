
from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': "Bengaluru, India",
    'salary': 'Rs. 10 LPA'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Noida , India',
    'salary': 'Rs. 15 LPA'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 8 LPA'
    
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 7 LPA'
}]


@app.route("/")
def hello_rishav():
  return render_template('home.html', jobs=JOBS, company_name="Career's")
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
