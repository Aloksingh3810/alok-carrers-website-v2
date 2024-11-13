import os


from flask import Flask, render_template,jsonify,request

from database import load_jobs_from_db, load_job_from_db , add_application_to_db

db_connection_string = os.getenv("db_connection_string")



app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello_rishav():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@ app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    jobs=load_job_from_db(id)

    if not jobs:
        return "Page Not Found", 404

    return render_template('jobpage.html', job=jobs)

@app.route("/api/job/<id>")
def show_job_json(id):
    job=load_job_from_db(id)
    return jsonify(job)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form  # Get the form data
    experience = data.get('experience')  # Use .get() to avoid KeyError

    if not experience:
        experience = "No experience provided"  # Or any default value

    job = load_job_from_db(id)

    # Prepare the application data
    application = {
        'full_name': data.get('full_name'),
        'email': data.get('email'),
        'linkedin_url': data.get('linkedin_url'),
        'education': data.get('education'),
        'experience': experience,
        'resume_url': data.get('resume_url')
    }

    # Add application to the database
    add_application_to_db(id, application)

    # Pass 'application' and 'job' to the template
    return render_template('application_submitted.html', application=application, job=job)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
