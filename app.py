import os
from flask import Flask, render_template,jsonify

from database import load_jobs_from_db



db_connection_string = os.getenv("db_connection_string")



app = Flask(__name__)


@app.route("/")
def hello_rishav():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Career's")


@ app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
